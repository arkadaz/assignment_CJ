"""
Control panel component for Mystica Oracle
"""

import streamlit as st
from langchain_core.messages import AIMessage
from utils.image_processing import convert_image_to_base64

from agents.workflow import MysticaWorkflow
from settings import settings
from ui.state import StateManager


class ControlPanel:
    """Handles control panel UI"""

    def __init__(self, state_manager: StateManager, workflow: MysticaWorkflow):
        self.state_manager = state_manager
        self.workflow = workflow

    def render(self):
        """Render the control panel"""
        st.subheader("✨ Seeker's Tools & Omens")

        # Handprint upload section
        self._render_handprint_upload()

        # Oracle's knowledge section
        self._render_oracle_knowledge()

    def _render_handprint_upload(self):
        """Render handprint upload section"""
        uploaded_file = st.file_uploader(
            "Offer an image of your palm (optional):",
            type=settings.ALLOWED_IMAGE_TYPES,
            key="handprint_uploader",
        )

        if uploaded_file is not None:
            self._handle_handprint_upload(uploaded_file)

    def _handle_handprint_upload(self, uploaded_file):
        """Handle handprint image upload"""
        # Check if it's a new file
        last_filename = self.state_manager.get_handprint_state("last_uploaded_filename")

        if last_filename != uploaded_file.name:
            self.state_manager.set_handprint_state(
                "handprint_analyzed_for_current_file", False
            )
            self.state_manager.set_handprint_state(
                "last_uploaded_filename", uploaded_file.name
            )

        # Display image
        st.image(
            uploaded_file,
            caption="Your Palm's Map",
            width=settings.HANDPRINT_IMAGE_WIDTH,
        )

        # Handle analysis
        if not self.state_manager.get_handprint_state(
            "handprint_analyzed_for_current_file", False
        ):
            self._render_analyze_button(uploaded_file)
        else:
            self._render_analysis_status()

    def _render_analyze_button(self, uploaded_file):
        """Render analyze button and handle analysis"""
        if st.button("Analyze Handprint with Mystica", key="analyze_handprint_btn"):
            with st.spinner("Mystica consults the lines of your hand..."):
                try:
                    # Convert image to base64
                    image_base64 = convert_image_to_base64(uploaded_file)

                    # Analyze handprint
                    analysis = self.workflow.process_handprint(image_base64)

                    # Mark as analyzed
                    self.state_manager.set_handprint_state(
                        "handprint_analyzed_for_current_file", True
                    )

                    # Add message about analysis
                    message = AIMessage(
                        content=f'Mystica has gleaned from your palm: "{analysis}" '
                        f"This insight will guide our session."
                    )
                    self.state_manager.add_message(message)

                    st.rerun()

                except Exception as e:
                    st.error(f"Could not process handprint: {e}")

    def _render_analysis_status(self):
        """Render handprint analysis status"""
        profile = self.state_manager.get_user_profile()
        if profile.handprint_analysis:
            st.success("Palm analysis incorporated.")

    def _render_oracle_knowledge(self):
        """Display Oracle's current knowledge"""
        st.markdown("---")
        st.write("**Oracle's Knowledge:**")

        profile = self.state_manager.get_user_profile()

        # Display name
        st.caption(f"Name: {profile.name or 'Unknown'}")

        # Display date of birth
        st.caption(f"DOB: {profile.date_of_birth or 'Unknown'}")

        # Display handprint status
        if profile.handprint_analysis:
            st.caption(f"Handprint: {profile.handprint_analysis}")
        else:
            st.caption("Handprint: Not yet offered")
