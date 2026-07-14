from app.core.state.cognitive_state import CognitiveState
from app.utils.logger import logger


class IntentRouter:

    def process(
        self,
        state: CognitiveState
    ) -> CognitiveState:

        text = state.message.lower()

        if "what am i studying" in text:

            state.intent = "learning"

        elif "what do you know about me" in text:

            state.intent = "knowledge_summary"

        else:

            state.intent = "conversation"

        logger.info(
            f"Intent routed: {state.intent}"
        )

        return state