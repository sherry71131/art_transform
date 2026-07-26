from src.data_loader import DataLoader
import src.data_loader as dl

print("Imported from:", dl.__file__)

loader = DataLoader()

print("Has load_images:", hasattr(loader, "load_images"))

images = loader.load_images()

print(f"Loaded {len(images)} images")