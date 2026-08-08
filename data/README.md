# Data Directory

This directory contains the raw and processed datasets used for the
Artistic Style Transformation project.

> **Note:** Large datasets and generated files are intentionally excluded
> from GitHub. They must be downloaded and prepared locally before running
> the complete pipeline.

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
    └── japanese_style/
        ├── trainA/
        ├── trainB/
        ├── testA/
        └── testB/