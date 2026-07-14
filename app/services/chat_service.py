from app.core.context.context_engine import ContextEngine
from app.core.reasoning.reasoning_engine import ReasoningEngine
from app.services.ai.ollama_provider import OllamaProvider
from app.services.conversation_service import ConversationService
from app.services.knowledge_service import KnowledgeService
from app.services.memory_service import MemoryService
from app.services.prompt_service import PromptService
from app.utils.logger import logger
from app.core.pipeline.cognitive_pipeline import CognitivePipeline
from app.core.state.cognitive_state import CognitiveState






class ChatService:

    def __init__(self):

        self.provider = OllamaProvider()

        self.reasoning = ReasoningEngine()

        self.knowledge_service = KnowledgeService()

        self.memory = MemoryService()

        self.prompt_service = PromptService()

        self.conversation = ConversationService()
        
        

        self.pipeline = CognitivePipeline()

        self.context = ContextEngine()

        





    def chat(self, message: str) -> str:

        logger.info(f"Received message: {message}")

        # -------------------------------------------------
        # Create Cognitive State
        # -------------------------------------------------

        state = CognitiveState(
            message=message
        )


        #---------------------------------------------------
        # Cognitive Pipeline
        #---------------------------------------------------

        state = self.pipeline.run(state)

        logger.info(
            "Cognetive Pipeline completed."
        )


      
        # -------------------------------------------------
        # Intent Handlers
        # -------------------------------------------------

        if state.response:
            return state.response.message
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