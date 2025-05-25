from typing import List, Protocol, Tuple

from core.models import FortuneContext, Product, UserProfile


class MessageExtractor(Protocol):
    """Interface for extracting information from messages"""

    def extract(self, message: str, current_profile: UserProfile) -> UserProfile:
        """Extract user information from message"""
        ...


class FortuneGenerator(Protocol):
    """Interface for generating fortunes"""

    def generate(self, context: FortuneContext) -> Tuple[str, List[str]]:
        """Generate fortune and return (fortune_text, color_associations)"""
        ...


class HandprintAnalyzer(Protocol):
    """Interface for analyzing handprint images"""

    def analyze(self, image_base64: str) -> str:
        """Analyze handprint image and return analysis text"""
        ...


class ProductRecommender(Protocol):
    """Interface for recommending products"""

    def recommend(
        self, colors: List[str], products: List[Product]
    ) -> List[Tuple[Product, str]]:
        """Recommend products based on colors and return list of (product, reason) tuples"""
        ...
