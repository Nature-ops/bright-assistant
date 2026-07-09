class MemoryClassifier:

    def classify(self, message: str) -> dict:

        text = message.lower()

        if "my name is" in text:
            return {
                "type": "fact",
                "category": "identity"
            }

        if "i am studying" in text:
            return {
                "type": "learning",
                "category": "education"
            }

        if "i want to" in text:
            return {
                "type": "goal",
                "category": "personal"
            }

        if "i am working on" in text:
            return {
                "type": "project",
                "category": "development"
            }

        return {
            "type": "conversation",
            "category": "general"
        }