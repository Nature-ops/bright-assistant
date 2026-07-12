from app.core.state.cognitive_state import CognitiveState
from app.core.reflection.reflection_rules import ReflectionRules
from app.utils.logger import logger
from app.core.reflection.insights import Insight
from datetime import datetime, UTC

class ReflectionEngine:

    def __init__(self):
        self.insights = []

    def process(
        self,
        state: CognitiveState
    ) -> CognitiveState:

        text = state.message.lower()

        for keyword in ReflectionRules.ACHIEVEMENTS:

            if keyword in text:
                insight = Insight(
                    title="Learning Milestone",
                    description="User completed a learning objective.",
                    category="learning",
                    confidence=0.95,
                    source="reflection",
                    created_at=datetime.now().isoformat()
                )
    
                self.insights.append(insight)

        return state