import json
from pathlib import Path


class KnowledgeService:

    def __init__(self):

        self.knowledge_file = Path("data/knowledge.json")

    def load(self):

        with open(
            self.knowledge_file,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    def save(self, knowledge):

        with open(
            self.knowledge_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                knowledge,
                file,
                indent=4,
                ensure_ascii=False
            )

    def add_fact(self, fact):

        knowledge = self.load()
        knowledge["facts"].append(fact)
        self.save(knowledge)

    def add_goal(self, goal):

        knowledge = self.load()
        knowledge["goals"].append(goal)
        self.save(knowledge)

    def add_learning(self, learning):

        knowledge = self.load()
        knowledge["learning"].append(learning)
        self.save(knowledge)

    def add_project(self, project):

        knowledge = self.load()
        knowledge["projects"].append(project)
        self.save(knowledge)

    def add_preference(self, preference):

        knowledge = self.load()
        knowledge["preferences"].append(preference)
        self.save(knowledge)

    def add_task(self, task):

        knowledge = self.load()
        knowledge["tasks"].append(task)
        self.save(knowledge)

    def add_contact(self, contact):

        knowledge = self.load()
        knowledge["contacts"].append(contact)
        self.save(knowledge)

    def add_event(self, event):

        knowledge = self.load()
        knowledge["events"].append(event)
        self.save(knowledge)

    def store_classification(self, classification, message):

        memory_type = classification["type"]

        if memory_type == "fact":
            self.add_fact(message)

        elif memory_type == "goal":
            self.add_goal(message)

        elif memory_type == "learning":
            self.add_learning(message)

        elif memory_type == "project":
            self.add_project(message)

        elif memory_type == "preference":
            self.add_preference(message)

        elif memory_type == "task":
            self.add_task(message)