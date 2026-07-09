from abc import ABC, abstractmethod


class BaseAIProvider(ABC):

    @abstractmethod
    def generate(self, messages: list) -> str:
        """
        Generate a response from a list of chat messages.
        """
        pass