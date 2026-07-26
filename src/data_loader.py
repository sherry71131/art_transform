"""
Data Loader

<<<<<<< HEAD
Loads images from the processed dataset for CycleGAN inference.
=======
Provides access to the processed datasets used for CycleGAN training
and inference.
>>>>>>> 51403c7 (Initialize project structure and integrate CycleGAN framework)
"""

from pathlib import Path
from PIL import Image


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
    Loads and validates the processed datasets required by CycleGAN.
    """

    def __init__(self):
        """Initialize dataset locations."""

        self.project_root = Path(__file__).resolve().parents[1]

        self.processed_dir = (
            self.project_root /
            "data" /
            "processed"
        )

        self.trainA = self.processed_dir / "trainA"
        self.trainB = self.processed_dir / "trainB"
        self.testA = self.processed_dir / "testA"
        self.testB = self.processed_dir / "testB"

    def validate(self):
        """
        Verify that all required dataset folders exist.

        Raises
        ------
        FileNotFoundError
            If any required dataset directory is missing.
        """

        required_dirs = [
            self.trainA,
            self.trainB,
            self.testA,
            self.testB,
        ]

        for directory in required_dirs:
            if not directory.exists():
                raise FileNotFoundError(
                    f"Missing dataset directory:\n{directory}"
                )

        print("✓ Dataset structure validated.")

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
