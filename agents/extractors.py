from typing import Optional

from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI

from core.exceptions import ExtractionError
from core.models import UserProfile


class ExtractedInfo(BaseModel):
    """Pydantic model for extracted information"""

    user_name: Optional[str] = Field(default=None)
    user_dob: Optional[str] = Field(default=None)
    handprint_analysis: Optional[str] = Field(default=None)


class LLMMessageExtractor:
    """Extracts user information from messages using LLM"""

    def __init__(self, llm: ChatOpenAI):
        self.structured_llm = llm.with_structured_output(
            ExtractedInfo, include_raw=False
        )

    def extract(self, message: str, current_profile: UserProfile) -> UserProfile:
        """Extract user information from message"""
        prompt = self._build_prompt(message, current_profile)

        try:
            extracted_info: ExtractedInfo = self.structured_llm.invoke(prompt)
            return self._merge_profiles(current_profile, extracted_info)
        except Exception as e:
            raise ExtractionError(f"Failed to extract information: {str(e)}")

    def _build_prompt(self, message: str, profile: UserProfile) -> str:
        """Build extraction prompt"""
        return (
            f"Current knowledge: "
            f"Name: {profile.name or 'Unknown'}, "
            f"DOB: {profile.date_of_birth or 'Unknown'}, "
            f"Handprint Analysis: {'Known' if profile.handprint_analysis else 'Unknown'}. "
            f'User\'s latest message: "{message}". '
            f"Extract 'user_name', 'user_dob'. "
            f"If message is textual handprint analysis, extract as 'handprint_analysis'. "
            f"Output nulls if no new info."
        )

    def _merge_profiles(
        self, current: UserProfile, extracted: ExtractedInfo
    ) -> UserProfile:
        """Merge extracted info with current profile"""
        return UserProfile(
            name=extracted.user_name if extracted.user_name else current.name,
            date_of_birth=extracted.user_dob
            if extracted.user_dob
            else current.date_of_birth,
            handprint_analysis=extracted.handprint_analysis
            if extracted.handprint_analysis
            else current.handprint_analysis,
            handprint_image_base64=current.handprint_image_base64,
        )
