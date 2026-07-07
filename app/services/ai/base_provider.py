from abc import ABC, abstractmethod


class BaseAIProvider(ABC):

    @abstractmethod
    def generate(self, system_prompt: str, user_message: str) -> str:
        """
        Generate a response from the AI model.
        """
        pass