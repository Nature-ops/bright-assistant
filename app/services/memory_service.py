import json
from pathlib import Path


class MemoryService:

    def __init__(self):
        self.memory_file = Path("data/conversation.json")

        if not self.memory_file.exists():
            self.memory_file.write_text("[]", encoding="utf-8")

    def load(self):

        try:
            with open(self.memory_file, "r", encoding="utf-8") as file:
                return json.load(file)

        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def save(self, messages):

        with open(self.memory_file, "w", encoding="utf-8") as file:
            json.dump(
                messages,
                file,
                indent=4,
                ensure_ascii=False
            )

    def add(self, role: str, content: str):

        history = self.load()

        history.append({
            "role": role,
            "content": content
        })

        self.save(history)

    def history(self):
        return self.load()

    def clear(self):
        self.save([])