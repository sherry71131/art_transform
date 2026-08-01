"""
===========================================================
CycleGAN Training Module
===========================================================

This module launches the official PyTorch CycleGAN
training script using the configuration file.


"""

import subprocess
from pathlib import Path
import yaml


class Trainer:

    def __init__(self, config_path="configs/model_config.yaml"):

        with open(config_path, "r") as f:
            self.config = yaml.safe_load(f)

        self.project_root = Path(__file__).resolve().parent.parent

        self.repo_path = (
            self.project_root /
            self.config["cyclegan_repo"]
        ).resolve()

    def train(self):

        dataset_path = "../../data/processed/" + self.config["dataset_name"]

        command = [
            "python",
            "train.py",
            "--dataroot",
            dataset_path,
            "--name",
            self.config["model_name"],
            "--model",
            "cycle_gan",
        ]

        print("=" * 60)
        print("Training CycleGAN")
        print("=" * 60)
        print(" ".join(command))
        print()

        subprocess.run(
            command,
            cwd=self.repo_path,
            check=True
        )

        print("\nTraining completed successfully.")
