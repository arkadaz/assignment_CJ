import os
from typing import List


class Settings:
    """Application settings"""

    # LLM Settings
    LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4o")
    LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", "1.0"))
    LLM_MAX_TOKENS = int(os.getenv("LLM_MAX_TOKENS", "1200"))

    # Vision LLM Settings
    VISION_LLM_MODEL = os.getenv("VISION_LLM_MODEL", "gpt-4o-mini")
    VISION_LLM_TEMPERATURE = float(os.getenv("VISION_LLM_TEMPERATURE", "1.0"))
    VISION_LLM_MAX_TOKENS = int(os.getenv("VISION_LLM_MAX_TOKENS", "1200"))

    # UI Settings
    CHAT_HEIGHT = 550
    HANDPRINT_IMAGE_WIDTH = 150
    MAX_PRODUCT_RECOMMENDATIONS = 3

    # Session State Settings
    STATE_KEY_PREFIX = "mystica_"

    # Fortune Teller Settings
    POSSIBLE_COLORS: List[str] = [
        "gold",
        "brown",
        "orange",
        "yellow",
        "green",
        "pink",
        "blue",
        "red",
        "black",
        "silver",
        "violet",
        "emerald",
        "purple",
    ]

    # Extended color vocabulary for fortune telling
    COLOR_VOCABULARY: List[str] = [
        "gold",
        "golden",
        "brown",
        "bronze",
        "orange",
        "amber",
        "copper",
        "yellow",
        "ivory",
        "green",
        "emerald",
        "jade",
        "pink",
        "rose",
        "coral",
        "blue",
        "azure",
        "sapphire",
        "turquoise",
        "red",
        "crimson",
        "scarlet",
        "ruby",
        "black",
        "ebony",
        "onyx",
        "silver",
        "silvery",
        "pearl",
        "violet",
        "purple",
        "lavender",
    ]

    # Divination Choices
    DIVINATION_CHOICES: List[str] = [
        "work",
        "love",
        "wealth",
        "all",
        "all of them",
        "everything",
        "general",
        "general vision",
        "tell me about work",
        "tell me about love",
        "tell me about wealth",
        "work and love",
        "love and wealth",
        "work and wealth",
        "work, love, and wealth",
        "yes tell me more",
        "proceed",
        "continue",
        "yes please",
    ]

    # File Upload Settings
    ALLOWED_IMAGE_TYPES = ["jpg", "jpeg", "png"]

    # Oracle Messages
    INITIAL_GREETING = "Hello, I wish to know my future!"
    ERROR_MESSAGE = "The threads of fate are tangled. The Oracle needs a moment. Please try your query again."
    HANDPRINT_ERROR = "The lines of fate are momentarily obscured for this image."

    # Styling
    CHAT_USER_AVATAR = "user"
    CHAT_ASSISTANT_AVATAR = "🔮"
    CHAT_RECOMMENDATION_AVATAR = "🎁"


settings = Settings()
