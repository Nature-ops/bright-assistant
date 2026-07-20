from pathlib import Path

from app.models.milestone import Milestone
from app.services.knowledge_engine import KnowledgeEngine


class PlanningEngine:

    def __init__(self):
        self.knowledge = KnowledgeEngine()

    def load_framework(self, path: str | Path) -> None:
        self.knowledge.load_framework(path)

    def get_first_milestone(self) -> Milestone:
        milestones = self.knowledge.get_milestones()

        if not milestones:
            raise RuntimeError("The framework contains no milestones.")

        return milestones[0]