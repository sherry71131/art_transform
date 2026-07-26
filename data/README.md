# Data Directory

This directory contains the raw and processed datasets used for the Artistic Style Transformation project.

> **Note:** Due to the large size of the datasets, no images or archives are included in this GitHub repository. Please download them separately and place them in the expected folders before running the project.

---

# Directory Structure

```text
data/
├── raw/
│   ├── flickr/
│   │   ├── flickr30k_images/
│   │   └── flickr-image-dataset.zip
│   │
│   ├── danbooru/
│   │   ├── portraits/
│   │   └── highresolution-anime-face-dataset-512x512.zip
│   │
│   └── wikiart/
│       ├── wikiart-art-movementsstyles/
│       │   ├── Academic_Art/
│       │   ├── Art_Nouveau/
│       │   ├── Baroque/
│       │   ├── Expressionism/
│       │   ├── Japanese_Art/
│       │   ├── Neoclassicism/
│       │   ├── Primitivism/
│       │   ├── Realism/
│       │   ├── Renaissance/
│       │   ├── Rococo/
│       │   ├── Romanticism/
│       │   ├── Symbolism/
│       │   └── Western_Medieval/
│       │
│       └── wikiart-art-movementsstyles.zip
│
└── processed/
```

---

# Datasets

## 1. Flickr30K Dataset (Real-world Photographs)

**Purpose**

Provides real-world photographs that serve as the source domain for CycleGAN training.

**Source**

Flickr30K Dataset (Kaggle)

**Expected Location**

```text
data/raw/flickr/flickr30k_images/
```

---

## 2. WikiArt Dataset

**Purpose**

Provides artistic paintings used as the target domain for style transfer.

This project uses the **Japanese_Art** subset of the WikiArt dataset.

**Source**

WikiArt Art Movements/Styles Dataset (Kaggle)

**Expected Location**

```text
data/raw/wikiart/wikiart-art-movementsstyles/
```

The preprocessing pipeline automatically selects the required style folder.

Current project style:

```text
Japanese_Art
```

Other art movements can also be used by updating the dataset configuration.

---

## 3. Danbooru Anime Face Dataset

**Purpose**

Provides anime-style portraits for future experiments and additional style-transfer tasks.

**Source**

High-Resolution Anime Face Dataset (512×512) (Kaggle)

**Expected Location**

```text
data/raw/danbooru/portraits/
```

---

# Preprocessing

Run the preprocessing notebook:

```text
notebooks/01_data_download_and_preprocess.ipynb
```

The notebook performs the following tasks:

- Validates images
- Removes unreadable or corrupted files
- Converts images to RGB (if required)
- Resizes images to 256 × 256 pixels
- Splits the datasets for training and testing
- Generates the directory structure required by the official CycleGAN implementation

The processed dataset is written to:

```text
data/processed/
```

---

# Notes

- Raw datasets are **not** committed to GitHub.
- Processed datasets are **not** committed to GitHub.
- Model checkpoints are **not** committed to GitHub.
- Output images are **not** committed to GitHub.

Only the source code, notebooks, configuration files, and documentation are included in the repository.

---

# Reproducing the Project

1. Clone the repository.

2. Download the required datasets.

3. Extract the datasets into the `data/raw/` directory.

4. Run:

```text
notebooks/01_data_download_and_preprocess.ipynb
```

5. Train the CycleGAN model using:

```bash
py -m src.train
```

6. Generate stylized images using the inference pipeline.

---

# Repository Policy

To keep the repository lightweight:

- Large datasets are excluded using `.gitignore`.
- Trained models and checkpoints are excluded.
- Generated outputs are excluded.
- Only reproducible source code and documentation are version controlled.