"""
Art Style Transfer System

Main entry point for training, inference, and evaluation.
"""

from src.train import Trainer
from src.inference import Inference
from src.evaluation import Evaluator


class ModelRunner:

    def __init__(self):
        self.trainer = Trainer()
        self.inference = Inference()
        self.evaluator = Evaluator()

    def menu(self):

        while True:

            print("\n" + "=" * 60)
            print("      Art Style Transfer using CycleGAN")
            print("=" * 60)
            print("1. Train Model")
            print("2. Run Inference")
            print("3. Run Pretrained Baseline")
            print("4. Evaluate Results")
            print("5. Exit")

            choice = input("\nEnter your choice: ")

            if choice == "1":
                print("\nStarting Training...\n")
                self.trainer.train()

            elif choice == "2":
                print("\nRunning Inference...\n")
                self.inference.run()

            elif choice == "3":
                print("\nRunning Pretrained Baseline...\n")
                self.inference.run_pretrained()

            elif choice == "4":
                print("\nEvaluating Results...\n")
                self.evaluator.evaluate()

            elif choice == "5":
                print("\nThank you for using the Art Style Transfer System.")
                break

            else:
                print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    runner = ModelRunner()
    runner.menu()