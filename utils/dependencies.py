import streamlit as st
from langchain_openai import ChatOpenAI

from agents.analyzers import VisionHandprintAnalyzer
from agents.extractors import LLMMessageExtractor
from agents.fortune_teller import MysticaFortuneGenerator
from agents.recommenders import MysticaProductRecommender
from agents.workflow import MysticaWorkflow
from data.repositories import ProductRepository
from settings import settings
from ui.chat import ChatInterface
from ui.controls import ControlPanel
from ui.state import StateManager


class DIContainer:
    """Dependency injection container for managing app dependencies"""

    def __init__(self):
        self._instances = {}

    @st.cache_resource
    def get_llms(_self):
        """Get LLM instances (cached)"""
        llm = ChatOpenAI(
            model=settings.LLM_MODEL,
            temperature=settings.LLM_TEMPERATURE,
            max_tokens=settings.LLM_MAX_TOKENS,
        )
        vision_llm = ChatOpenAI(
            model=settings.VISION_LLM_MODEL,
            temperature=settings.VISION_LLM_TEMPERATURE,
            max_tokens=settings.VISION_LLM_MAX_TOKENS,
        )
        return llm, vision_llm

    def get_state_manager(self) -> StateManager:
        """Get state manager instance"""
        if "state_manager" not in self._instances:
            self._instances["state_manager"] = StateManager()
        return self._instances["state_manager"]

    def get_product_repository(self) -> ProductRepository:
        """Get product repository instance"""
        if "product_repository" not in self._instances:
            self._instances["product_repository"] = ProductRepository()
        return self._instances["product_repository"]

    def get_workflow(self) -> MysticaWorkflow:
        """Get workflow instance"""
        if "workflow" not in self._instances:
            llm, vision_llm = self.get_llms()

            # Create service instances
            extractor = LLMMessageExtractor(llm)
            fortune_generator = MysticaFortuneGenerator(llm)
            handprint_analyzer = VisionHandprintAnalyzer(vision_llm)
            product_recommender = MysticaProductRecommender(llm)

            # Create workflow
            self._instances["workflow"] = MysticaWorkflow(
                extractor=extractor,
                fortune_generator=fortune_generator,
                handprint_analyzer=handprint_analyzer,
                product_recommender=product_recommender,
                product_repository=self.get_product_repository(),
                state_manager=self.get_state_manager(),
            )

        return self._instances["workflow"]

    def get_chat_interface(self) -> ChatInterface:
        """Get chat interface instance"""
        if "chat_interface" not in self._instances:
            self._instances["chat_interface"] = ChatInterface(self.get_state_manager())
        return self._instances["chat_interface"]

    def get_control_panel(self) -> ControlPanel:
        """Get control panel instance"""
        if "control_panel" not in self._instances:
            self._instances["control_panel"] = ControlPanel(
                self.get_state_manager(), self.get_workflow()
            )
        return self._instances["control_panel"]
