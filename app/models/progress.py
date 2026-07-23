from datetime import datetime, UTC

from pydantic import BaseModel, Field


class Progress(BaseModel):
    framework_id: str

    completed_milestones: list[str] = Field(default_factory=list)

    completed_skills: list[str] = Field(default_factory=list)

    started_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    updated_at: datetime = Field(default_factory=lambda: datetime.now(UTC))