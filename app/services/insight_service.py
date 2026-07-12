import json
from pathlib import Path

from app.core.reflection.insights import Insight


class InsightService:

    def __init__(self):

        self.file = Path("data/insights.json")

    def load(self):

        if not self.file.exists():

            return {
                "insights": []
            }

        with open(
            self.file,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    def save(self, data):

        with open(
            self.file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

    def add(self, insight: Insight):

        data = self.load()

        data["insights"].append(
            {
                "title": insight.title,
                "description": insight.description,
                "category": insight.category,
                "confidence": insight.confidence,
                "source": insight.source,
                "created_at": insight.created_at,
            }
        )

        self.save(data)

    def get_all(self):

        return self.load()["insights"]