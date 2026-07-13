from app.utils.logger import logger

class IntentRouter:

    def route(self, message: str) -> str:

        text = message.lower()

        if "what am i studying" in text:
            return "learning"

        if "what do you know about me" in text:
            return "knowledge_summary"
        

        logger.info(f"Intent routed: {text}")

        return "conversation"
    

