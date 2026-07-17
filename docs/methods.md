# Methods and Model Selection

## Task

Unpaired image-to-image translation for artistic style transfer:
- Input domain: real-world photos (Flickr Creative Commons).
- Output domains: artistic styles (e.g., Japanese art from WikiArt, anime from Danbooru).

## Model

We use **CycleGAN** (Zhu et al., 2017), which trains two generators and two discriminators
with adversarial and cycle-consistency losses to learn mappings between two domains
without paired examples.

Key losses:
- Adversarial loss: encourages realistic images in each domain.
- Cycle-consistency loss: enforces that translating from A→B→A recovers the original.
- Identity loss: helps preserve color and content when appropriate.

## Framework

We use **PyTorch** and an existing CycleGAN implementation (or a custom implementation
based on the original paper) to focus on understanding generative modeling principles
rather than building everything from scratch.

## Datasets

- **WikiArt**: paintings across many styles (Impressionism, Post-Impressionism, etc.).
- **Danbooru**: high-quality anime illustrations.
- **Flickr Creative Commons**: real-world photos for input domain.

## Preprocessing Choices

- Resize all images to 256×256 pixels.
- Convert to RGB.
- Organize into train/validation splits for each domain:
  - `photos/train`, `photos/val`
  - `japanese/train`, `japanese/val`
  - `anime/train`, `anime/val`

## Planned Metrics

- Qualitative: visual inspection, content preservation, user feedback.
- Quantitative: - **LPIPS (content preservation):** ≤ 0.3  
                - **FID (style realism):** ≤ 80
