from app.services.planning_engine import PlanningEngine


def run_scenario(completed):
    planner = PlanningEngine()

    planner.load_framework(
        "knowledge/cloud/frameworks/aws-sa.yaml"
    )

    milestone = planner.get_next_milestone(completed)

    if milestone is None:
        print("🎉 Congratulations! Framework completed.")

    else:
        print(f"Next: {milestone.id}")
        print(f"Title: {milestone.title}")


def main():
    run_scenario([])

    run_scenario([
        "aws-fundamentals"
    ])

    run_scenario([
        "aws-fundamentals",
        "iam"
    ])


if __name__ == "__main__":
    main()