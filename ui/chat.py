"""
Chat interface component for Mystica Oracle
"""

import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage

from settings import settings
from ui.state import StateManager


class ChatInterface:
    """Handles chat UI rendering"""

    def __init__(self, state_manager: StateManager):
        self.state_manager = state_manager

    def render(self):
        """Render the chat interface and return user input"""
        st.subheader("💬 The Oracle's Chamber")

        # Create chat container with fixed height
        chat_container = st.container(height=settings.CHAT_HEIGHT)

        # Get messages from state
        messages = self.state_manager.get_messages()

        # Render messages
        with chat_container:
            for msg in messages:
                if isinstance(msg, HumanMessage):
                    self._render_user_message(msg)
                elif isinstance(msg, AIMessage):
                    self._render_assistant_message(msg)

        # Return chat input
        return st.chat_input("Whisper your query to Mystica...")

    def _render_user_message(self, message: HumanMessage):
        """Render a user message"""
        st.chat_message(settings.CHAT_USER_AVATAR).write(message.content)

    def _render_assistant_message(self, message: AIMessage):
        """Render an assistant message"""
        # Check if this is a recommendation message
        if self._is_recommendation_message(message.content):
            avatar = settings.CHAT_RECOMMENDATION_AVATAR
        else:
            avatar = settings.CHAT_ASSISTANT_AVATAR

        st.chat_message("assistant", avatar=avatar).write(message.content)

    def _is_recommendation_message(self, content: str) -> bool:
        """Check if message contains product recommendations"""
        return "🎁" in content and "Mystica also senses" in content
