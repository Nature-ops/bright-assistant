from app.core.state.cognitive_state import (CognitiveState,Context,)
from app.services.knowledge_service import KnowledgeService



class ContextEngine:

    def __init__(self):

        self.knowledge_service = KnowledgeService()

    def process(
        self,
        state: CognitiveState
    ) -> CognitiveState:
        
        knowledge = self.knowledge_service.get_all()

        if state.intent == "learning":

            state.context = Context(
                knowledge=knowledge,
                learning=knowledge["Learning"],
                goals=knowledge["Goals"]
            )

        elif state.intent == "knowledge_summary":

            state.context = Context(
                 knowledge=knowledge
            )

        else:

            state.context = Context(
                knowledge={}
             )
            

          

        return state   