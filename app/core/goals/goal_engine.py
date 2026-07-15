from app.core.base.cognitive_engine import CognitiveEngine
from app.core.state.cognitive_state import (CognitiveState,Goal,)
from app.utils.logger import logger



class GoalEngine(CognitiveEngine):

    def process(
        self,
        state: CognitiveState
    ) -> CognitiveState:
        
        if state.context is None:
            return state
        
        knowledge = state.context.knowledge
        goals = knowledge.get("Goals", [])

        if not goals:
            return state
        
        goal = goals[0]

        state.goal = Goal(
        title=goal["content"],
        status="active",
        )    

        logger.info(
            f"Goal detected: {state.goal.title}"
        )


        return state



        