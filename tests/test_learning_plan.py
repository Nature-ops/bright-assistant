from app.services.planning_engine import PlanningEngine


def print_learning_plan(plan):
    print("=" * 50)
    print("Learning Plan")
    print("=" * 50)

    print(f"\nMilestone")
    print(f"---------")
    print(plan.milestone.title)

    print(f"\nDescription")
    print(f"-----------")
    print(plan.milestone.description)

    print("\nSkills")
    print("------")

    for skill in plan.skills:
        print(f"• {skill.name}")
        print(f"  {skill.description}")

    print("\nResources")
    print("---------")

    for resource in plan.resources:
        print(f"• {resource.title}")
        print(f"  {resource.url}")

    print("\nCompletion")
    print("----------")
    print(f"Method: {plan.milestone.completion.method}")
    print(f"Required: {plan.milestone.completion.required}")


def main():

    planner = PlanningEngine()

    planner.load_framework(
        "knowledge/cloud/frameworks/aws-sa.yaml"
    )
    planner = PlanningEngine()

    planner.load_framework(
        "knowledge/cloud/frameworks/aws-sa.yaml"
    )

    plan = planner.create_learning_plan_for_framework(
    "aws-sa"
    )

    if plan is None:
        print("Framework completed.")
        return

    print_learning_plan(plan)


if __name__ == "__main__":
    main()