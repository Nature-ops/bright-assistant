from app.services.planning_engine import PlanningEngine


def main():
    planner = PlanningEngine()

    planner.load_framework(
        "knowledge/cloud/frameworks/aws-sa.yaml"
    )

    milestone = planner.get_first_milestone()

    print("\n=== First Milestone ===")
    print(f"ID: {milestone.id}")
    print(f"Title: {milestone.title}")
    print(f"Description: {milestone.description}")


if __name__ == "__main__":
    main()