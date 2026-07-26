import subprocess
from pathlib import Path
import yaml


class CycleGANWrapper:

    def __init__(self, config_path="configs/model_config.yaml"):

        with open(config_path, "r") as f:
            self.config = yaml.safe_load(f)

        # Absolute path to the CycleGAN repository
        self.repo_path = (
            Path(__file__).resolve().parent.parent
            / self.config["cyclegan_repo"]
        ).resolve()

    def run_inference(self):

        # IMPORTANT:
        # test.py runs INSIDE the CycleGAN repository.
        # Therefore the dataset path must be relative to that folder.
        dataset_path = "../../data/processed/" + self.config["dataset_name"]

        command = [
            "python",
            "test.py",
            "--dataroot",
            dataset_path,
            "--name",
            self.config["model_name"],
            "--model",
            "test",
            "--no_dropout",
        ]

        print("=" * 60)
        print("Running CycleGAN inference...")
        print("=" * 60)
        print("Repository :", self.repo_path)
        print("Dataset    :", dataset_path)
        print()
        print(" ".join(command))
        print()

        subprocess.run(
            command,
            cwd=self.repo_path,
            check=True,
        )

        print("\nInference completed successfully!")
        