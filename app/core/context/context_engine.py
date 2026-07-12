class ContextEngine:

    def build(
        self,
        intent: str,
        knowledge: dict
    ) -> dict:

        if intent == "learning":

            return {
                "Learning": knowledge["Learning"],
                "Goals": knowledge["Goals"]
            }

        if intent == "knowledge_summary":

            return knowledge

        return {}