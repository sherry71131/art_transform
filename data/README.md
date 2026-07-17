# Data Directory

This folder contains raw and processed data for the project.

## Structure

- `raw/`
  - `wikiart/` – raw paintings.
  - `danbooru/` – raw anime images.
  - `flickr/` – raw photos.
- `processed/`
  - `photos/train`, `photos/val`
  - `japanese/train`, `japanese/val`
  - `anime/train`, `anime/val`

## Datasets and How to Download

### 1. WikiArt Dataset (Paintings)

- Source: Kaggle – search for "WikiArt dataset".
- Steps:
  1. Create a Kaggle account.
  2. Go to the WikiArt dataset page.
  3. Download the dataset as a `.zip` file.
  4. Extract the images into `data/raw/wikiart/`.

You may optionally filter for specific styles (e.g., Japanese art, Impressionism) by selecting folders or using tags provided in the dataset.

### 2. Danbooru Anime Dataset

- Source: Danbooru community dataset (search "Danbooru dataset").
- Steps:
  1. Find a curated subset or smaller mirror of the Danbooru dataset.
  2. Download a subset of 5,000–10,000 images.
  3. Extract the images into `data/raw/danbooru/`.


### 3. Flickr Creative Commons Photos

- Source: Flickr – search for Creative Commons photos.
- Steps:
  1. Use Flickr's search with a Creative Commons license filter.
  2. Download around 2,000 photos that match your desired content (e.g., landscapes, portraits).
  3. Save them into `data/raw/flickr/`.


## Preprocessing

Preprocessing (resizing, splitting into train/val) is done in the notebook:
`notebooks/01_data_download_and_preprocess.ipynb`.

Processed images are saved into `data/processed/...` and are **not** committed to GitHub to avoid large files.
