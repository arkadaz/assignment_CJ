import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from utils.dependencies import DIContainer


class MysticaOracleApp:
    """Main application class"""

    def __init__(self):
        self.container = DIContainer()
        self.state_manager = self.container.get_state_manager()
        self.workflow = self.container.get_workflow()
        self.chat_interface = self.container.get_chat_interface()
        self.control_panel = self.container.get_control_panel()

    def initialize(self):
        """Initialize the application"""
        if not self.state_manager.is_initialized():
            # Process initial greeting
            initial_messages = self.workflow.process_message(
                "Hello, I wish to know my future!"
            )

            self.state_manager.add_message(
                HumanMessage(content="Hello, I wish to know my future!")
            )
            for msg in initial_messages:
                self.state_manager.add_message(msg)

            self.state_manager.set_initialized()

    def run(self):
        """Run the application"""
        self.initialize()

        col1, col2 = st.columns([2, 1])
        with col1:
            user_input = self.chat_interface.render()
        with col2:
            self.control_panel.render()

        if user_input:
            self._handle_user_input(user_input)

    def _handle_user_input(self, user_input: str):
        """Handle user input"""
        self.state_manager.add_message(HumanMessage(content=user_input))

        with st.spinner("The Oracle contemplates..."):
            try:
                responses = self.workflow.process_message(user_input)
                for response in responses:
                    self.state_manager.add_message(response)

            except Exception as e:
                error_msg = AIMessage(
                    content="The threads of fate are tangled. The Oracle needs a moment. Please try your query again."
                )
                self.state_manager.add_message(error_msg)
                st.error(f"An error occurred: {e}")

        st.rerun()


def main():
    """Main entry point"""
    st.set_page_config(page_title="Mystica's Oracle", layout="wide")

    app = MysticaOracleApp()
    app.run()


if __name__ == "__main__":
    main()
