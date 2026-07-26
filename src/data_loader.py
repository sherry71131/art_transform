"""
data_loader.py

Loads the processed datasets used by the CycleGAN model.
"""

from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Processed dataset directory
PROCESSED_DATA = PROJECT_ROOT / "data" / "processed"

PHOTO_DIR = PROCESSED_DATA / "photos"
ANIME_DIR = PROCESSED_DATA / "anime"
JAPANESE_DIR = PROCESSED_DATA / "japanese"
