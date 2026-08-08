"""
Evaluation Module

Displays input photographs alongside generated CycleGAN samples
for qualitative evaluation.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from PIL import Image
import yaml


class Evaluator:
    """Display generated CycleGAN results for qualitative evaluation."""

    def __init__(self, config_path="configs/model_config.yaml"):
        self.project_root = Path(__file__).resolve().parent.parent

        config_file = self.project_root / config_path

        with open(config_file, "r") as file:
            self.config = yaml.safe_load(file)

        self.dataset_name = self.config["dataset_name"]
        self.num_samples = self.config["num_samples"]

    def _get_output_directory(self):
        """Return the project output directory containing generated images."""

        return (
            self.project_root
            / self.config["output_dir"]
            / self.dataset_name
            / "pretrained_baseline"
        )

    def _get_input_directory(self):
        """Return the test images used as CycleGAN input."""

        return (
            self.project_root
            / "data"
            / "processed"
            / self.dataset_name
            / "testA"
        )

    def evaluate(self):
        """Display input and generated images for qualitative evaluation."""

        print("=" * 60)
        print("Qualitative Evaluation")
        print("=" * 60)

        output_dir = self._get_output_directory()
        input_dir = self._get_input_directory()

        if not output_dir.exists():
            print(f"No generated results found at: {output_dir}")
            print("Run inference before evaluating the results.")
            return

        generated_images = sorted(
            output_dir.glob("*_fake.png")
        )

        if not generated_images:
            print("No generated images found.")
            print("Run inference before evaluating the results.")
            return

        num_samples = min(
            self.num_samples,
            len(generated_images)
        )

        generated_images = generated_images[:num_samples]

        print(f"\nInput directory   : {input_dir}")
        print(f"Output directory  : {output_dir}")
        print(f"Generated images  : {len(generated_images)}")
        print(f"Images displayed  : {num_samples}\n")

        for generated_path in generated_images:

            input_name = generated_path.name.replace(
                "_fake.png",
                ".jpg"
            )

            input_path = input_dir / input_name

            if not input_path.exists():
                print(
                    f"Input image not found for "
                    f"{generated_path.name}"
                )
                continue

            with Image.open(input_path) as input_image:
                input_image = input_image.copy()

            with Image.open(generated_path) as generated_image:
                generated_image = generated_image.copy()

            figure, axes = plt.subplots(
                1,
                2,
                figsize=(12, 5)
            )

            axes[0].imshow(input_image)
            axes[0].set_title("Original Photograph")
            axes[0].axis("off")

            axes[1].imshow(generated_image)
            axes[1].set_title("CycleGAN Generated Style")
            axes[1].axis("off")

            figure.suptitle(generated_path.stem)
            plt.tight_layout()
            plt.show()

        print("\nQualitative evaluation completed.")