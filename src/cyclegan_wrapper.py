import shutil
import subprocess
import sys
from pathlib import Path

import yaml


class CycleGANWrapper:
    """Run CycleGAN inference using the project configuration."""

    def __init__(
        self,
        config_path="configs/model_config.yaml",
        use_pretrained=False
    ):
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
            / "testA"
        ).resolve()

        self.output_dir = (
            self.project_root / self.config["output_dir"]
        ).resolve()

        if use_pretrained:
            self.model_name = self.config["pretrained_model_name"]
            self.output_name = "pretrained_baseline"
        else:
            self.model_name = self.config["model_name"]
            self.output_name = "trained_model"

        self.checkpoint_path = (
            self.repo_path
            / "checkpoints"
            / self.model_name
        ).resolve()

    def _clear_previous_results(self):
        """Remove results from an earlier inference run."""

        results_dir = (
            self.repo_path
            / "results"
            / self.model_name
            / "test_latest"
        )

        if results_dir.exists():
            shutil.rmtree(results_dir)

    def _copy_generated_images(self):
        """Copy generated images from CycleGAN results into project outputs."""

        results_dir = (
            self.repo_path
            / "results"
            / self.model_name
            / "test_latest"
            / "images"
        )

        output_dir = (
            self.output_dir
            / self.config["dataset_name"]
            / self.output_name
        )

        output_dir.mkdir(parents=True, exist_ok=True)

        # Remove generated images from an earlier project run.
        for image_path in output_dir.glob("*_fake.png"):
            image_path.unlink()

        generated_images = sorted(results_dir.glob("*_fake.png"))

        if not generated_images:
            raise FileNotFoundError(
                f"No generated images found in {results_dir}"
            )

        # Keep only the number of images requested in the configuration.
        generated_images = generated_images[: self.config["num_samples"]]

        for image_path in generated_images:
            shutil.copy2(
                image_path,
                output_dir / image_path.name
            )

        print(f"\nCopied {len(generated_images)} generated images to:")
        print(output_dir)

    def run_inference(self):
        """Run CycleGAN on the configured test images."""

        if not self.repo_path.exists():
            raise FileNotFoundError(
                f"CycleGAN repository not found: {self.repo_path}"
            )

        if not self.dataset_path.exists():
            raise FileNotFoundError(
                f"Test dataset not found: {self.dataset_path}"
            )

        if not self.checkpoint_path.exists():
            raise FileNotFoundError(
                f"CycleGAN checkpoint not found: {self.checkpoint_path}"
            )

        command = [
            sys.executable,
            "test.py",
            "--dataroot",
            str(self.dataset_path),
            "--name",
            self.model_name,
            "--model",
            "test",
            "--dataset_mode",
            "single",
            "--direction",
            "AtoB",
            "--no_dropout",
            "--num_test",
            str(self.config["num_samples"]),
        ]

        print("=" * 60)
        print("Running CycleGAN inference")
        print("=" * 60)
        print(f"Repository : {self.repo_path}")
        print(f"Dataset    : {self.dataset_path}")
        print(f"Model      : {self.model_name}")
        print(f"Checkpoint : {self.checkpoint_path}")
        print(f"Samples    : {self.config['num_samples']}")
        print()
        print(" ".join(command))
        print()

        # Start each run with a clean result directory so that
        # older generated images are not mixed with the new results.
        self._clear_previous_results()

        subprocess.run(
            command,
            cwd=self.repo_path,
            check=True,
        )

        self._copy_generated_images()

        print("\nInference completed successfully.")