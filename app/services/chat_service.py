from app.services.ai.ollama_provider import OllamaProvider
from app.services.prompt_service import PromptService
from app.services.memory_service import MemoryService
from app.utils.logger import logger


class ChatService:
    def __init__(self):
        self.provider = OllamaProvider()
        self.prompt_service = PromptService()
        self.memory = MemoryService()

    def chat(self, message: str) -> str:
        """
        Process a user message and return the AI response.
        """

        logger.info(f"Received message: {message}")

        # Save the user's message
        self.memory.add(
            role="user",
            content=message
        )

        logger.info("User message saved to memory.")

        # Load the system prompt
        system_prompt = self.prompt_service.get("system_prompt.txt")

        logger.info("System prompt loaded.")

        # Generate a response using Ollama
        response = self.provider.generate(
            system_prompt=system_prompt,
            user_message=message
        )

        logger.info("AI response generated.")

        # Save the assistant's response
        self.memory.add(
            role="assistant",
            content=response
        )

        logger.info("Assistant response saved to memory.")

        return response