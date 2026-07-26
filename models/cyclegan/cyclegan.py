"""
CycleGAN Wrapper

This module provides a simple interface between the main project
and the official PyTorch CycleGAN implementation.
"""

from pathlib import Path


class CycleGANWrapper:
    """Wrapper for loading and running a pretrained CycleGAN model."""

    def __init__(self):
        self.project_root = Path(__file__).resolve().parents[2]

        self.external_repo = (
            self.project_root /
            "external" /
            "pytorch-CycleGAN-and-pix2pix"
        )

        self.checkpoint_dir = (
            self.project_root /
            "models" /
            "cyclegan" /
            "checkpoint"
        )

        self.loaded = False

    def load_model(self):
        """
        Placeholder for loading the pretrained CycleGAN model.
        """
        print(f"External repository: {self.external_repo}")
        print(f"Checkpoint directory: {self.checkpoint_dir}")

        self.loaded = True

    def is_loaded(self):
        return self.loaded
