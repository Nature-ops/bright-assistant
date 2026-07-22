from pydantic import BaseModel

from app.models.milestone import Milestone
from app.models.resource import Resource
from app.models.skill import Skill


class LearningPlan(BaseModel):
    milestone: Milestone
    skills: list[Skill]
    resources: list[Resource]