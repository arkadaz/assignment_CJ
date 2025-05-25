from typing import List

from langchain_core.messages import AIMessage, BaseMessage
from ui.state import StateManager

from core.exceptions import WorkflowError
from core.interfaces import (
    FortuneGenerator,
    HandprintAnalyzer,
    MessageExtractor,
    ProductRecommender,
)
from core.models import FortuneContext, Product
from data.repositories import ProductRepository


class MysticaWorkflow:
    """Orchestrates the fortune telling workflow"""

    def __init__(
        self,
        extractor: MessageExtractor,
        fortune_generator: FortuneGenerator,
        handprint_analyzer: HandprintAnalyzer,
        product_recommender: ProductRecommender,
        product_repository: ProductRepository,
        state_manager: StateManager,
    ):
        self.extractor = extractor
        self.fortune_generator = fortune_generator
        self.handprint_analyzer = handprint_analyzer
        self.product_recommender = product_recommender
        self.product_repository = product_repository
        self.state_manager = state_manager

    def process_message(self, user_message: str) -> List[BaseMessage]:
        """Process a user message and return response messages"""
        try:
            responses = []

            # Get current state
            current_profile = self.state_manager.get_user_profile()

            # Extract information from message
            updated_profile = self.extractor.extract(user_message, current_profile)
            self.state_manager.set_user_profile(updated_profile)

            # Generate fortune
            context = FortuneContext(
                user_profile=updated_profile, latest_message=user_message
            )
            fortune_text, colors = self.fortune_generator.generate(context)
            responses.append(AIMessage(content=fortune_text))

            # Handle product recommendations if colors were mentioned
            if colors:
                self.state_manager.set_color_associations(colors)
                products = self.product_repository.get_all_products()
                recommendations = self.product_recommender.recommend(colors, products)

                if recommendations:
                    rec_message = self._format_recommendations(recommendations)
                    responses.append(AIMessage(content=rec_message))

            return responses

        except Exception as e:
            raise WorkflowError(f"Workflow processing failed: {str(e)}")

    def process_handprint(self, image_base64: str) -> str:
        """Process handprint image and return analysis"""
        try:
            analysis = self.handprint_analyzer.analyze(image_base64)

            # Update profile with handprint analysis
            profile = self.state_manager.get_user_profile()
            profile.handprint_analysis = analysis
            profile.handprint_image_base64 = image_base64
            self.state_manager.set_user_profile(profile)

            return analysis

        except Exception as e:
            raise WorkflowError(f"Handprint processing failed: {str(e)}")

    def _format_recommendations(
        self, recommendations: List[tuple[Product, str]]
    ) -> str:
        """Format product recommendations as markdown"""
        header = "🎁 **Mystica also senses these items might align with your path:**"
        items = []

        for product, reason in recommendations:
            item_text = f"**{product.item_name_thai}**\n_{reason}_"
            items.append(item_text)

        return f"{header}\n\n" + "\n\n---\n\n".join(items)
