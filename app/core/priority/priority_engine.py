from app.core.base.cognitive_engine import CognitiveEngine
from app.core.state.cognitive_state import (CognitiveState,Priority,)
from app.utils.logger import logger



class PriorityEngine(CognitiveEngine):

    def process(
        self,
        state: CognitiveState
    ) -> CognitiveState:
        
        if state.goal is None:
            return state
        

        state.priority = Priority(
            title=state.goal.title,
            reason="Current active goal",
        )

        logger.info(
            f"Priority selected: {state.priority.title}"
        )




        return state