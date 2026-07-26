"""
Data Loader

Loads images from the processed dataset for CycleGAN inference.
"""

from pathlib import Path
from PIL import Image


class DataLoader:
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
