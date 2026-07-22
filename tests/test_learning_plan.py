from app.services.planning_engine import PlanningEngine


def run_scenario(completed):
    planner = PlanningEngine()

    planner.load_framework(
        "knowledge/cloud/frameworks/aws-sa.yaml"
    )

    plan = planner.create_learning_plan(completed)

    print(f"\nCompleted: {completed}")

    if plan is None:
        print("🎉 Framework completed.")
        return

    print("=== Learning Plan ===")
    print(f"Milestone: {plan.milestone.title}")
    print(f"Description: {plan.milestone.description}")

    if plan.milestone.skills:
        print("\nSkills:")
        for skill in plan.milestone.skills:
            print(f" - {skill}")

    if plan.milestone.resources:
        print("\nResources:")
        for resource in plan.milestone.resources:
            print(f" - {resource}")

    print("\nCompletion:")
    print(f"Method: {plan.milestone.completion.method}")
    print(f"Required: {plan.milestone.completion.required}")


def main():
    run_scenario([])

    run_scenario([
        "aws-fundamentals"
    ])

    run_scenario([
        "aws-fundamentals",
        "iam",
        "ec2"
    ])


if __name__ == "__main__":
    main()