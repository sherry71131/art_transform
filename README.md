# Art Style Transfer using CycleGAN

## Project Overview

This project implements an image-to-image translation system using the CycleGAN architecture. The objective is to transform images from one artistic style into another without requiring paired training data. The implementation uses the official PyTorch CycleGAN repository wrapped inside a modular Python application.

## Features

- Data preprocessing pipeline
- Modular project structure
- CycleGAN training
- Image style transfer (inference)
- Generated image evaluation
- Menu-driven application
- Configuration support using YAML

---

## Project Structure

```
art_transform/
│
├── configs/
│   └── model_config.yaml
│
├── data/
│   ├── raw/
│   └── processed/
│
├── external/
│   └── pytorch-CycleGAN-and-pix2pix/
│
├── outputs/
│
├── src/
│   ├── data_loader.py
│   ├── cyclegan_wrapper.py
│   ├── train.py
│   ├── inference.py
│   ├── evaluation.py
│   └── model_runner.py
│
└── README.md
```

---

## Datasets

The project uses two artistic image domains.

**Domain A**
- Japanese Ukiyo-e artwork

**Domain B**
- Anime artwork

The datasets are organized as:

```
data/processed/

japanese_style/
    trainA
    trainB
    testA
    testB
```

---

## Technologies Used

- Python
- PyTorch
- CycleGAN
- Matplotlib
- Pillow
- YAML
- VS Code

---

## Installation

Clone the project.

```bash
git clone https://github.com/sherry71131/art_transform
cd art_transform
```

Install dependencies.

```bash
pip install torch torchvision matplotlib pillow pyyaml wandb
```

---

## Running the Project

Start the application.

```bash
python -m src.model_runner
```

The menu provides:

```
1. Train Model
2. Run Inference
3. Evaluate Results
4. Exit
```

---

## Training

Select option **1** from the menu.

The application launches the official CycleGAN training script using the configured dataset.

---

## Inference

Select option **2**.

The trained model generates stylized images from the test dataset.

Generated images are stored in the official CycleGAN results directory.

---

## Evaluation

Select option **3**.

The evaluation module displays generated images for qualitative assessment using Matplotlib.

---

## Results

The project successfully performs unpaired image-to-image translation between Japanese artwork and Anime style using CycleGAN.

Example outputs include:

- Original Image
- Generated Stylized Image



---

## Future Improvements

- Quantitative evaluation using FID score
- GPU optimization
- Web-based interface
- Support for additional artistic styles
- Automated model comparison

---

## References

Zhu, J. Y., Park, T., Isola, P., & Efros, A. A. (2017). *Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks.*

Official CycleGAN Repository:
https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix
