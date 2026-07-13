import logging
from app.core.state.cognitive_state import CognitiveState
from app.core.routing.intent_router import IntentRouter
from app.core.classification.memory_classifier import MemoryClassifier
from app.core.evolution.memory_evolution_engin import MemoryEvolutionEngine
from app.core.context.context_engine import ContextEngine
from app.core.reasoning.reasoning_service import ReasoningService
from app.core.reflection.reflection_engine import ReflectionEngine
from app.services.knowledge_service import KnowledgeService

logger = logging.getLogger(__name__)


class CognitivePipeline:

    def __init__(self):

        self.router = IntentRouter()

        self.classifier = MemoryClassifier()

        self.evolution = MemoryEvolutionEngine()

        self.context = ContextEngine()

        self.reflection = ReflectionEngine()

        self.reasoning = ReasoningService()

        self.knowledge = KnowledgeService()

    def run(
        self,
        state: CognitiveState
    ) -> CognitiveState:

        # -----------------------------------
        # Intent Routing
        # -----------------------------------

        state.intent = self.router.route(
            state.message
        )

        # -------------------------------------------------
         # Classification
        # -------------------------------------------------

        state.classification = self.classifier.classify(
            state.message
        )

        #-------------------------
        #Evolution
        #------------------------

        state = self.evolution.process(
            state
        )


        return state
