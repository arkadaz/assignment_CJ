from typing import List, Tuple

from langchain_openai import ChatOpenAI

from core.exceptions import FortuneGenerationError
from core.models import FortuneContext
from settings import settings


class MysticaFortuneGenerator:
    """Generates mystical fortunes using LLM"""

    def __init__(self, llm: ChatOpenAI):
        self.llm = llm

    def generate(self, context: FortuneContext) -> Tuple[str, List[str]]:
        """Generate fortune and return (fortune_text, color_associations)"""
        prompt = self._build_prompt(context)

        try:
            response = self.llm.invoke(prompt)
            fortune_text = response.content
            colors = self._extract_colors(fortune_text)
            return fortune_text, colors
        except Exception as e:
            raise FortuneGenerationError(f"Failed to generate fortune: {str(e)}")

    def _build_prompt(self, context: FortuneContext) -> str:
        """Build fortune generation prompt"""
        name = context.user_profile.name or "Awaiting Whisper from the Stars"
        dob = context.user_profile.date_of_birth or "Echoes of a Past Yet Unsung"
        handprint = context.user_profile.handprint_analysis

        return f"""
You are **Mystica, the All-Seeing Oracle**. Your voice is ancient, your wisdom vast, your pronouncements both enigmatic and deeply insightful. You peer through the veils of time and fate.

**Seeker Information:**
* **Name:** {name}
* **Date of Birth:** {dob}
* **Handprint Analysis:** {"Palm Lines Revealed: " + handprint if handprint else "Fate's Imprint Optional, Yet Potent"}
* **Seeker's Latest Utterance:** "{context.latest_message}"

**Your Sacred Duty: Continue the Dialogue**
Your response MUST be ONLY the direct words of Mystica to the seeker.

**The Unfolding Path of Revelation:**

1.  **If 'Name' is 'Awaiting Whisper from the Stars':**
    * You MUST beckon forth their name with mystical urgency.
    * *Example*: "The mists swirl, seeker, but your essence remains shrouded. Whisper to me the name the spirits call you by, that I may part the veils for you."

2.  **Else if 'Date of Birth' is 'Echoes of a Past Yet Unsung':**
    * Addressing them by their now-known **Name**, you MUST request their birth-sign from the cosmic calendar.
    * *Example*: "{name}, the celestial spheres align with your presence, yet the exact moment of your arrival upon this earthly coil is needed. Share with me your date of birth, that the stars may illuminate your path."

3.  **Else (Name and Date of Birth are KNOWN):**
    * **Consider the Seeker's Latest Utterance: "{context.latest_message}".**
    * **Perform a case-insensitive check. If the user_input_text matches or strongly implies one of the following choices: {settings.DIVINATION_CHOICES}:**
        * Then assume the Seeker has made a choice. Proceed directly to **Section 4: Main Divination** below.
    * **Else:**
        * This is the **Invitation to Choose**. Acknowledge the seeker by **Name**.
        * **You MUST then invite the seeker to choose their focus of inquiry.**
        * *Example Query*: "The threads of your destiny are complex, {name}. Do you seek insight into the realm of **Work**, the tender dance of **Love**, or the shifting tides of **Wealth**?"
        if you does not know just give user all of the choices.

4.  **Main Divination:**
    * **If the Seeker's Latest Utterance clearly indicates specific categories:**
        * For EACH category, provide a mystical fortune with a color mention.
        * Use colors like: **gold**, **silver**, **red**, **pink**, **blue**, **green**, **brown**, **orange**, **yellow**, **black**, **purple**
        * You may also use poetic variations like **crimson** (for red), **rose** (for pink), **emerald** (for green), etc.
    * **Else if general fortune:**
        * Provide an encompassing mystical fortune with color recommendations.

**Guiding Principles:** Be mystical, mention colors in bold (e.g., **gold**, **emerald**, **crimson**, **rose**).
Your response should be ONLY Mystica's words.
"""

    def _extract_colors(self, text: str) -> List[str]:
        """Extract mentioned colors from fortune text"""
        text_lower = text.lower()
        colors = []

        # Extended color mapping to handle variations
        color_mappings = {
            # Direct matches
            "gold": "Gold",
            "brown": "Brown",
            "orange": "Orange",
            "yellow": "Yellow",
            "green": "Green",
            "pink": "Pink",
            "blue": "Blue",
            "red": "Red",
            "black": "Black",
            "silver": "Silver",
            "violet": "Violet",
            "emerald": "Green",
            "purple": "Purple",
            "crimson": "Red",
            "rose": "Pink",
            "scarlet": "Red",
            "azure": "Blue",
            "golden": "Gold",
            "silvery": "Silver",
            "ebony": "Black",
            "ivory": "Yellow",
            "jade": "Green",
            "ruby": "Red",
            "sapphire": "Blue",
            "amber": "Orange",
            "coral": "Pink",
            "lavender": "Purple",
            "turquoise": "Blue",
            "bronze": "Brown",
            "copper": "Orange",
            "pearl": "Silver",
            "onyx": "Black",
        }

        # Check for each color mapping
        for color_variant, base_color in color_mappings.items():
            if (
                f" {color_variant}" in text_lower
                or f"**{color_variant}**" in text_lower
            ):
                colors.append(base_color)

        return list(set(colors))
