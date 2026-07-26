"""
Training Entry Point

This script initializes the CycleGAN environment and prepares the
project for model training.
"""

from src.model_runner import ModelRunner


def main():
    """Initialize the training environment."""

    print("=" * 60)
    print("Artistic Style Transformation using CycleGAN")
    print("=" * 60)

    runner = ModelRunner()

    try:
        if runner.initialize():
            print("\n✓ CycleGAN environment initialized successfully.")
            print("✓ Ready for model training.")
        else:
            print("\nInitialization failed.")

    except Exception as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    main()
