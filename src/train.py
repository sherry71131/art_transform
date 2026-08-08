import subprocess
import sys
from pathlib import Path

import yaml


class Trainer:
    """Train the CycleGAN model using the project configuration."""

    def __init__(self, config_path="configs/model_config.yaml"):
        self.project_root = Path(__file__).resolve().parent.parent

        config_file = self.project_root / config_path

        with open(config_file, "r") as file:
            self.config = yaml.safe_load(file)

        self.repo_path = (
            self.project_root / self.config["cyclegan_repo"]
        ).resolve()

        self.dataset_path = (
            self.project_root
            / "data"
            / "processed"
            / self.config["dataset_name"]
        ).resolve()

    def train(self):
        """Train the CycleGAN model using the project configuration."""

        if not self.repo_path.exists():
            raise FileNotFoundError(
                f"CycleGAN repository not found: {self.repo_path}"
            )

        if not self.dataset_path.exists():
            raise FileNotFoundError(
                f"Training dataset not found: {self.dataset_path}"
            )

        command = [
            sys.executable,
            "train.py",
            "--dataroot",
            str(self.dataset_path),
            "--name",
            self.config["model_name"],
            "--model",
            "cycle_gan",
            "--batch_size",
            str(self.config["batch_size"]),
            "--lr",
            str(self.config["learning_rate"]),
            "--n_epochs",
            str(self.config["n_epochs"]),
            "--n_epochs_decay",
            str(self.config["n_epochs_decay"]),
        ]

        total_epochs = (
            self.config["n_epochs"]
            + self.config["n_epochs_decay"]
        )

        print("=" * 60)
        print("Training CycleGAN")
        print("=" * 60)
        print(f"Repository      : {self.repo_path}")
        print(f"Dataset         : {self.dataset_path}")
        print(f"Model           : {self.config['model_name']}")
        print(f"Batch size      : {self.config['batch_size']}")
        print(f"Learning rate   : {self.config['learning_rate']}")
        print(f"Initial epochs  : {self.config['n_epochs']}")
        print(f"Decay epochs    : {self.config['n_epochs_decay']}")
        print(f"Total epochs    : {total_epochs}")
        print()
        print("Command:")
        print(" ".join(command))
        print()

        subprocess.run(
            command,
            cwd=self.repo_path,
            check=True,
        )

        print("\nTraining completed successfully.")