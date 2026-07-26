"""
Data Loader

Loads processed images for CycleGAN inference.
"""

from pathlib import Path
import yaml


class DataLoader:
    """
    Loads processed images for CycleGAN inference.
    """

    def __init__(self, config_path="configs/model_config.yaml"):
        with open(config_path, "r") as f:
            self.config = yaml.safe_load(f)

        self.input_dir = Path(self.config["input_dir"])
        self.num_samples = self.config["num_samples"]

    def load_images(self):
        """
        Returns a list of image paths.
        """

        image_extensions = {
            ".jpg",
            ".jpeg",
            ".png",
            ".bmp",
            ".webp",
        }

        images = sorted([
            p for p in self.input_dir.iterdir()
            if p.is_file() and p.suffix.lower() in image_extensions
        ])

        if len(images) == 0:
            raise FileNotFoundError(
                f"No images found in {self.input_dir}"
            )

        return images[: self.num_samples]
