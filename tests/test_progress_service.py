from app.services.progress_service import ProgressService


def main():

    service = ProgressService()

    framework_id = "aws-sa"

    print("=" * 50)
    print("Progress Service Test")
    print("=" * 50)

    # Load or create progress
    progress = service.get_progress(framework_id)

    print("\nInitial Progress")
    print("----------------")
    print(f"Framework: {progress.framework_id}")
    print(f"Completed Milestones: {progress.completed_milestones}")

    # Complete the first milestone
    print("\nCompleting milestone: aws-fundamentals")

    service.complete_milestone(
        framework_id,
        "aws-fundamentals"
    )

    # Reload to verify persistence
    progress = service.get_progress(framework_id)

    print("\nUpdated Progress")
    print("----------------")
    print(f"Framework: {progress.framework_id}")
    print(f"Completed Milestones: {progress.completed_milestones}")

    assert "aws-fundamentals" in progress.completed_milestones

    print("\n✅ Progress saved successfully!")


if __name__ == "__main__":
    main()