from src.cyclegan_wrapper import CycleGANWrapper


class Inference:
    """Run image-to-image translation using CycleGAN."""

    def __init__(self):
        self.wrapper = CycleGANWrapper()

    def run(self):
        """Run inference using the project CycleGAN model."""

        print("\nStarting image style transfer...\n")

        self.wrapper.run_inference()

        print("\nStyle transfer completed.\n")

    def run_pretrained(self):
        """Run the existing pretrained CycleGAN model as a baseline."""

        print("\nRunning pretrained CycleGAN baseline...\n")

        pretrained_wrapper = CycleGANWrapper(use_pretrained=True)
        pretrained_wrapper.run_inference()

        print("\nPretrained baseline completed.\n")
