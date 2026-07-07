from ollama import chat

from app.config.settings import settings
from app.services.ai.base_provider import BaseAIProvider


class OllamaProvider(BaseAIProvider):

    def generate(self, system_prompt: str, user_message: str) -> str:

        response = chat(
            model=settings.OLLAMA_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": user_message,
                },
            ],
        )

        return response["message"]["content"]