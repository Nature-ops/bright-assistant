from app.core.context.context_engine import ContextEngine
from app.core.evolution.memory_evolution_engin import MemoryEvolutionEngine
from app.core.classification.memory_classifier import MemoryClassifier
from app.core.reasoning.reasoning_service import ReasoningService
from app.core.routing.intent_router import IntentRouter
from app.core.state.cognitive_state import (CognitiveState,Classification,)
from app.core.reflection.reflection_engine import ReflectionEngine
from app.services.ai.ollama_provider import OllamaProvider
from app.services.conversation_service import ConversationService
from app.services.knowledge_service import KnowledgeService
from app.services.memory_service import MemoryService
from app.services.prompt_service import PromptService
from app.utils.logger import logger







class ChatService:

    def __init__(self):

        self.provider = OllamaProvider()

        self.router = IntentRouter()

        self.classifier = MemoryClassifier()

        self.evolution = MemoryEvolutionEngine()

        self.context = ContextEngine()

        self.reasoning = ReasoningService()

        self.knowledge_service = KnowledgeService()

        self.memory = MemoryService()

        self.prompt_service = PromptService()

        self.conversation = ConversationService()
        
        self.reflection = ReflectionEngine()





    def chat(self, message: str) -> str:

        logger.info(f"Received message: {message}")

        # -------------------------------------------------
        # Create Cognitive State
        # -------------------------------------------------

        state = CognitiveState(
            message=message
        )

        # -------------------------------------------------
        # Intent Routing
        # -------------------------------------------------

        state.intent = self.router.route(
            state.message
        )

        # -------------------------------------------------
        # Classification
        # -------------------------------------------------

        state.classification = self.classifier.classify(
            state.message
        )

        logger.info(
            f"Classification: {state.classification}"
        )

        # -------------------------------------------------
        # Memory Evolution
        # -------------------------------------------------

        state.classification = self.evolution.evolve(
            state.classification,
            state.message
        )

        logger.info(
            f"Evolution: {state.classification}"
        )

        # -------------------------------------------------
        # Store Memory
        # -------------------------------------------------

        if state.classification.intent == "store":
            self.knowledge_service.process_memory(
                state.classification,
                state.message
            )

            logger.info(
                "Knowledge stored successfully."
            )



            state = self.reflection.process(
                state
            )

        # -------------------------------------------------
        # Intent Handlers
        # -------------------------------------------------

        handlers = {

            "learning": self.reasoning.recommend_learning,

            "knowledge_summary": self.reasoning.summarize_user,

        }

        handler = handlers.get(
            state.intent
        )

        if handler:

            knowledge = self.knowledge_service.get_all()

            context = self.context.build(
                state.intent,
                knowledge
            )

            return handler(
                context
            )

        # -------------------------------------------------
        # Continue Normal Conversation
        # -------------------------------------------------

        self.memory.add(
            role="user",
            content=state.message
        )

        logger.info(
            "User message saved."
        )

        system_prompt = self.prompt_service.get(
            "system_prompt.txt"
        )

        messages = self.conversation.build(
            system_prompt=system_prompt,
            history=self.memory.recent(20)
        )

        response = self.provider.generate(
            messages
        )

        self.memory.add(
            role="assistant",
            content=response
        )

        logger.info(
            "Assistant response saved."
        )

        return response