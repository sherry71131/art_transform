# Artistic Style Transformation with CycleGAN

This project explores unpaired image-to-image translation for artistic style transfer using CycleGAN. We transform real-world photos into artistic styles such as Japanese art paintings or anime illustrations.

## Project Goals

- Use CycleGAN for unpaired image-to-image translation.
- Train on separate photo and artwork datasets (no paired images).
- Analyze trade-offs between content preservation and stylization.

## Repository Structure

- `data/` – raw and processed datasets, plus data documentation.
- `notebooks/` – Jupyter notebooks for data preprocessing and exploration.
- `models/` – CycleGAN configuration and model placeholder.
- `docs/` – documentation of methods and design choices.

## Setup

1. Create a Python environment (example with conda):
   ```bash
   conda create -n art_transform python=3.10
   conda activate art_transform

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Download datasets following `data/README.md`.

4. Launch Jupyter:
   ```bash
   jupyter notebook

5. Run the notebooks in `notebooks/` in order:
   - `01_data_download_and_preprocess.ipynb`
   - `02_data_exploration.ipynb`