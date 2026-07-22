from pathlib import Path
from app.models.resource import Resource
from app.services.file_loader import FileLoader


class ResourceLoader:

    @staticmethod
    def load(path: str | Path) -> list[Resource]:
        data = FileLoader.load_yaml(path)

        return [
            Resource.model_validate(item)
            for item in data
        ]