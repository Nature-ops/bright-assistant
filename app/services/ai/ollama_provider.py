from ollama import chat

from app.config.settings import settings
from app.services.ai.base_provider import BaseAIProvider


class OllamaProvider(BaseAIProvider):

    def generate(self, messages: list) -> str:

        response = chat(
            model=settings.OLLAMA_MODEL,
            messages=messages
            
        )

        return response["message"]["content"]