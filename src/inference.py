from src.cyclegan_wrapper import CycleGANWrapper


class Inference:

    def __init__(self):
        self.wrapper = CycleGANWrapper()

    def run(self):
        print("\nStarting image style transfer...\n")
        self.wrapper.run_inference()
        print("\nStyle transfer completed.\n")
