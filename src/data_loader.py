
"""
Data Loader

51403c7 (Initialize project structure and integrate CycleGAN framework)
"""

from pathlib import Path
from PIL import Image
=======
from pathlib import Path
import yaml
>>>>>>> aeaf913 (Complete CycleGAN project modules and evaluation)


class DataLoader:
<<<<<<< HEAD
    def __init__(self):
        self.project_root = Path(__file__).resolve().parents[1]

        self.photo_dir = (
            self.project_root /
            "data" /
            "processed" /
            "photos" /
            "val"
        )

    def list_images(self):
        """Return all jpg/png images in the validation folder."""

        images = list(self.photo_dir.glob("*.jpg"))
        images.extend(self.photo_dir.glob("*.jpeg"))
        images.extend(self.photo_dir.glob("*.png"))

        return sorted(images)

    def load_image(self, image_path):
        """Load an image using PIL."""

        return Image.open(image_path).convert("RGB")
=======
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

<<<<<<< HEAD
    def get_dataset_paths(self):
        """
        Return the dataset directory paths.

        Returns
        -------
        dict
            Dictionary containing CycleGAN dataset paths.
        """

        return {
            "trainA": self.trainA,
            "trainB": self.trainB,
            "testA": self.testA,
            "testB": self.testB,
        }
>>>>>>> 51403c7 (Initialize project structure and integrate CycleGAN framework)
=======
        return images[: self.num_samples]
>>>>>>> aeaf913 (Complete CycleGAN project modules and evaluation)
