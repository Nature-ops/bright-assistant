import logging
from app.core.state.cognitive_state import CognitiveState
from app.core.routing.intent_router import IntentRouter
from app.core.classification.memory_classifier import MemoryClassifier
from app.core.evolution.memory_evolution_engin import MemoryEvolutionEngine
from app.core.context.context_engine import ContextEngine
from app.core.reasoning.reasoning_engine import ReasoningEngine
from app.core.reflection.reflection_engine import ReflectionEngine
from app.core.knowledge.knowledge_engine import KnowledgeEngine
logger = logging.getLogger(__name__)


class CognitivePipeline:

    def __init__(self):

        self.router = IntentRouter()

        self.classifier = MemoryClassifier()

        self.evolution = MemoryEvolutionEngine()

        self.context = ContextEngine()

        self.reflection = ReflectionEngine()

        self.reasoning = ReasoningEngine()


        self.knowledge = KnowledgeEngine()

        

    def run(
        self,
        state: CognitiveState
    ) -> CognitiveState:

        # -----------------------------------
        # Intent Routing
        # -----------------------------------

        state = self.router.process(
            state
        )


        

        # -------------------------------------------------
         # Classification
        # -------------------------------------------------

        state = self.classifier.process(
            state
        )

        #-------------------------
        #Evolution
        #------------------------

        state = self.evolution.process(
            state
        )


        # -------------------------------------------------
        # Knowledge
        # -------------------------------------------------

        state = self.knowledge.process(
        state
        )

        # -------------------------------------------------
        # Reflection
        # -------------------------------------------------

        state = self.reflection.process(
        state
        )


        # -------------------------------------------------
        # Context
        # -------------------------------------------------

        state = self.context.process(state)


        # -------------------------------------------------
        # Reasoning
        # -------------------------------------------------

        state = self.reasoning.process(state)

        return state


        
