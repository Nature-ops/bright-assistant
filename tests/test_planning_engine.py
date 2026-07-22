from app.services.planning_engine import PlanningEngine


def main():
    planner = PlanningEngine()

    planner.load_framework(
        "knowledge/cloud/frameworks/aws-sa.yaml"
    )

    milestone = planner.get_first_milestone()

    print("\n=== First Milestone ===")
    if milestone is None:
        print("No milestone found.")
        return

    print(f"ID: {milestone.id}")
    print(f"Title: {milestone.title}")
    print(f"Description: {getattr(milestone, 'description', '')}")


if __name__ == "__main__":
    main()