from app.core.state.cognitive_state import CognitiveState
from app.services.knowledge_service import KnowledgeService
from app.utils.logger import logger


class KnowledgeEngine:

    def __init__(self):

        self.knowledge_service = KnowledgeService()

    def process(
        self,
        state: CognitiveState
    ) -> CognitiveState:

        if (
            state.classification
            and state.classification.intent == "store"
        ):

            self.knowledge_service.process_memory(
                state.classification,
                state.message
            )

            logger.info(
                "Knowledge stored successfully."
            )

        return state