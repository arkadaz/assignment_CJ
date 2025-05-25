"""
State management for Mystica Oracle UI
"""

from typing import List, Optional

import streamlit as st
from langchain_core.messages import BaseMessage

from core.models import UserProfile
from settings import settings


class StateManager:
    """Manages application state"""

    def __init__(self):
        self.key_prefix = settings.STATE_KEY_PREFIX

    def get_user_profile(self) -> UserProfile:
        """Get current user profile from session state"""
        key = f"{self.key_prefix}user_profile"
        if key not in st.session_state:
            return UserProfile()
        return st.session_state[key]

    def set_user_profile(self, profile: UserProfile):
        """Set user profile in session state"""
        st.session_state[f"{self.key_prefix}user_profile"] = profile

    def get_messages(self) -> List[BaseMessage]:
        """Get conversation messages"""
        key = f"{self.key_prefix}messages"
        if key not in st.session_state:
            return []
        return st.session_state[key]

    def add_message(self, message: BaseMessage):
        """Add a message to the conversation"""
        key = f"{self.key_prefix}messages"
        if key not in st.session_state:
            st.session_state[key] = []
        st.session_state[key].append(message)

    def get_color_associations(self) -> Optional[List[str]]:
        """Get current color associations"""
        return st.session_state.get(f"{self.key_prefix}color_associations")

    def set_color_associations(self, colors: Optional[List[str]]):
        """Set color associations"""
        st.session_state[f"{self.key_prefix}color_associations"] = colors

    def is_initialized(self) -> bool:
        """Check if the application is initialized"""
        return f"{self.key_prefix}initialized" in st.session_state

    def set_initialized(self):
        """Mark application as initialized"""
        st.session_state[f"{self.key_prefix}initialized"] = True

    def get_handprint_state(self, key: str, default=None):
        """Get handprint-related state"""
        return st.session_state.get(key, default)

    def set_handprint_state(self, key: str, value):
        """Set handprint-related state"""
        st.session_state[key] = value
