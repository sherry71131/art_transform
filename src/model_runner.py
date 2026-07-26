"""
Model Runner

This module coordinates interactions between the project and the
official CycleGAN implementation through the CycleGAN wrapper.
"""

from models.cyclegan.cyclegan import CycleGANWrapper


class ModelRunner:
    """
    Coordinates model initialization, training, and inference.
    """

    def __init__(self):
        """Initialize the CycleGAN wrapper."""
        self.model = CycleGANWrapper()

    def initialize(self):
        """
        Initialize the CycleGAN environment.

        Returns
        -------
        bool
            True if initialization is successful.
        """
        self.model.load_model()
        return self.model.is_loaded()

    def get_model(self):
        """
        Return the initialized model wrapper.
        """
        return self.model
