"""
Product recommendation service for Mystica Oracle
"""

from typing import List, Tuple

from langchain_openai import ChatOpenAI

from core.models import Product
from settings import settings


class MysticaProductRecommender:
    """Recommends products based on color associations"""

    def __init__(self, llm: ChatOpenAI):
        self.llm = llm

    def recommend(
        self, colors: List[str], products: List[Product]
    ) -> List[Tuple[Product, str]]:
        """Recommend products based on colors and return list of (product, reason) tuples"""
        matching_products = self._find_matching_products(colors, products)

        if not matching_products:
            return []

        reasons = self._generate_reasons(matching_products)
        return list(zip(matching_products, reasons))

    def _find_matching_products(
        self, colors: List[str], products: List[Product]
    ) -> List[Product]:
        """Find products matching the given colors"""
        matching_products = []

        for product in products:
            product_color = self._extract_product_color(product)
            if (
                product_color in colors
                and len(matching_products) < settings.MAX_PRODUCT_RECOMMENDATIONS
            ):
                matching_products.append(product)

        return matching_products

    def _extract_product_color(self, product: Product) -> str:
        """Extract normalized color from product"""
        # Extract base color, removing any parenthetical descriptions
        color_string = product.inferred_color_association_primary.split("(")[0].strip()

        # Normalize color mappings (same as in fortune_teller.py)
        color_mappings = {
            "Gold": "Gold",
            "Brown": "Brown",
            "Orange": "Orange",
            "Yellow": "Yellow",
            "Green": "Green",
            "Pink": "Pink",
            "Blue": "Blue",
            "Red": "Red",
            "Black": "Black",
            "Silver": "Silver",
            "Violet": "Purple",
            "Purple": "Purple",
        }

        # Return the normalized color
        return color_mappings.get(color_string.capitalize(), color_string.capitalize())

    def _generate_reasons(self, products: List[Product]) -> List[str]:
        """Generate mystical reasons for product recommendations"""
        if not products:
            return []

        prompt = self._build_reasons_prompt(products)

        try:
            response = self.llm.invoke(prompt)
            return self._parse_reasons(response.content, len(products))
        except Exception:
            # Return default reasons if generation fails
            default_reason = (
                "This item carries an auspicious resonance with the guiding energies."
            )
            return [default_reason] * len(products)

    def _build_reasons_prompt(self, products: List[Product]) -> str:
        """Build prompt for generating recommendation reasons"""
        prompt_items = "\n".join(
            [
                f'{i + 1}. Item: "{p.item_name_thai}" '
                f'(English: "{p.item_name_english_approximation}", '
                f"Color Energy: {p.inferred_color_association_primary})"
                for i, p in enumerate(products)
            ]
        )

        return f"""You are Mystica, the All-Seeing Oracle, continuing your guidance for a seeker.
The seeker has been attuned to specific color energies that align with their current path.
For the following items, each resonating with one of these auspicious colors, provide a brief, mystical, and positive suitability reason (1 sentence per item).
Focus on how the item's essence, combined with its associated color's energy, might uniquely benefit the seeker or illuminate their journey. Be poetic and insightful.

Here are the items:
{prompt_items}

Please provide your reasons in a numbered list, corresponding to the item numbers above. Ensure each reason is a single, flowing sentence.
Example format for your response:
1. [Mystical reason for item 1, linking its essence and color to the seeker's path.]
2. [Mystical reason for item 2, linking its essence and color to the seeker's path.]
"""

    def _parse_reasons(self, text: str, expected_count: int) -> List[str]:
        """Parse numbered reasons from LLM response"""
        reasons = []

        for line in text.splitlines():
            line = line.strip()
            if line and line[0].isdigit():
                parts = line.split(".", 1)
                if len(parts) == 2:
                    try:
                        num = int(parts[0].strip())
                        if 1 <= num <= expected_count:
                            reasons.append(parts[1].strip())
                    except ValueError:
                        continue

        # Fill with default reasons if needed
        default_reason = (
            "This item carries an auspicious resonance with the guiding energies."
        )
        while len(reasons) < expected_count:
            reasons.append(default_reason)

        return reasons[:expected_count]
