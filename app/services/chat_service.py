from app.services.ai.ollama_provider import OllamaProvider
from app.services.prompt_service import PromptService
from app.utils.logger import logger


class ChatService:

    def __init__(self):

        self.provider = OllamaProvider()
        self.prompt_service = PromptService()

    def chat(self, message: str) -> str:

        logger.info(f"Received message: {message}")

        system_prompt = self.prompt_service.load("system_prompt.txt")

        response = self.provider.generate(
            system_prompt,
            message
        )

        logger.info("AI response generated.")

        return response