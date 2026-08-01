"""
===========================================================
Evaluation Module
===========================================================

Purpose:
--------
This module displays generated images produced by the
CycleGAN model for qualitative evaluation.


"""

from pathlib import Path
import matplotlib.pyplot as plt
from PIL import Image


class Evaluator:

    def __init__(self):

        self.project_root = Path(__file__).resolve().parent.parent

        self.results_dir = (
            self.project_root /
            "external" /
            "pytorch-CycleGAN-and-pix2pix" /
            "results"
        )

    def evaluate(self):

        print("=" * 60)
        print("Evaluating Generated Images")
        print("=" * 60)

        images = list(self.results_dir.rglob("*.png"))

        if len(images) == 0:
            print("No generated images found.")
            return

        print(f"\nFound {len(images)} generated images.\n")

        for image_path in images[:5]:

            image = Image.open(image_path)

            plt.figure(figsize=(6, 6))
            plt.imshow(image)
            plt.title(image_path.name)
            plt.axis("off")
            plt.show()

        print("\nEvaluation completed successfully.")

if __name__ == "__main__":
    evaluator = Evaluator()
    evaluator.evaluate()
