from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

from core.exceptions import HandprintAnalysisError
from settings import settings


class VisionHandprintAnalyzer:
    """Analyzes handprint images using vision LLM"""

    def __init__(self, vision_llm: ChatOpenAI):
        self.vision_llm = vision_llm

    def analyze(self, image_base64: str) -> str:
        """Analyze handprint image and return analysis text"""
        try:
            response = self.vision_llm.invoke(
                [
                    HumanMessage(
                        content=[
                            {
                                "type": "text",
                                "text": (
                                    "You are a mystical palm reader. Analyze this handprint image. "
                                    "Provide a short (1-2 sentences), mystical-sounding summary of its key features. "
                                    "Be concise and evocative."
                                ),
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{image_base64}"
                                },
                            },
                        ]
                    )
                ]
            )
            return response.content
        except Exception as e:
            raise HandprintAnalysisError(
                f"Failed to analyze handprint: {str(e)}. {settings.HANDPRINT_ERROR}"
            )
