class ConversationService:

    def build(
        self,
        system_prompt: str,
        history: list
    ) -> list:

        messages = [
            {
                "role": "system",
                "content": system_prompt
            }
        ]

        messages.extend(history)

        return messages
    
    

        