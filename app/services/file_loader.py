from pathlib import Path
from typing import Any

import yaml


class FileLoader:

    @staticmethod
    def load_yaml(path: str | Path) -> dict[str, Any] | list[dict[str, Any]]:
        yaml_path = Path(path)

        if not yaml_path.exists():
            raise FileNotFoundError(
                f"YAML file not found: {path}"
            )

        with yaml_path.open(
            "r",
            encoding="utf-8"
        ) as file:
            return yaml.safe_load(file)