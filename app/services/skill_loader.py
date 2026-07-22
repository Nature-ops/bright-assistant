from pathlib import Path
from app.models.skill import Skill
from app.services.file_loader import FileLoader


class SkillLoader:

    @staticmethod
    def load(path: str | Path) -> list[Skill]:
        data = FileLoader.load_yaml(path)

        return [
            Skill.model_validate(item)
            for item in data
        ]