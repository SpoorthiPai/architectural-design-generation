# Dataset Information

## Overview

This dataset was created and curated as part of a Machine Learning research project focused on generating architectural designs from textual descriptions using Generative AI techniques.

The dataset contains architectural exterior images paired with detailed descriptive captions designed for text-to-image generation workflows, semantic understanding, and architectural visualization tasks.

The primary objective of this dataset is to support AI models in understanding complex architectural descriptions and generating visually coherent architectural designs.

---

# Dataset Development Process

The dataset creation process involved multiple stages of collection, cleaning, filtering, caption generation, and preprocessing.

## Initial Dataset Collection

- More than 10,000 architectural images were initially collected from multiple architectural categories and design styles.

## Dataset Cleaning and Filtering

- Duplicate, low-quality, noisy, and irrelevant images were removed through manual and preprocessing-based filtering techniques.

## Final Curated Dataset

- The cleaned dataset was reduced to approximately 5,000 high-quality architectural images suitable for model training and experimentation.

## Caption Generation

- Detailed architectural captions were generated for more than 2,000 images within the dataset.

These captions were structured to provide rich semantic information for text-to-image generation tasks.

---

# Dataset Characteristics

The dataset includes:

- Architectural exterior images
- Detailed architectural captions
- Multiple architectural styles
- Structural descriptions
- Roof and façade information
- Material descriptions
- Environmental context descriptions
- Lighting and scene information
- Camera angle and perspective details

---

# Architectural Categories

The dataset contains diverse architectural styles including:

- Modern Villas
- Traditional Japanese Machiya Houses
- Colonial Architecture
- Contemporary Residences
- Farmhouses
- Bamboo Structures
- Nordic Cabins
- Urban Buildings
- Apartments
- Minimalist Concrete Houses
- Skyscrapers
- Rural Vernacular Structures
- Mixed-use Buildings

---

# Captioning Methodology

The captions were designed to provide highly descriptive semantic information for training generative models.

Each caption may include:

- Architectural style
- Number of visible floors
- Roof type and geometry
- Exterior wall materials
- Window and door arrangements
- Façade symmetry
- Color palette
- Environmental surroundings
- Lighting conditions
- Camera angle and framing
- Scale references

This detailed captioning strategy improves alignment between textual prompts and generated visual outputs.

---

# Example Caption Structure

The captions are stored in JSON format using image filenames as keys and descriptive architectural annotations as values.

Example:

```json
{
  "Modern_villa_00001.jpg": "Detailed architectural description..."
}
```

---

# Dataset Preparation Workflow

## 1. Image Collection
Architectural images representing multiple building styles and environmental contexts were collected.

## 2. Dataset Cleaning
Duplicate and low-quality images were removed to improve dataset consistency.

## 3. Caption Generation
Detailed captions describing architectural and environmental characteristics were generated.

## 4. Data Structuring
Images and captions were paired systematically for model training workflows.

## 5. Image Preprocessing
Images were resized, normalized, and prepared for generative AI pipelines.

---

# Dataset Structure

```text
dataset/
│
├── sample-images/
├── captions/
└── dataset-info.md
```

---

# Repository Samples

This repository includes:

- 27 representative sample architectural images
- Sample caption files
- Dataset documentation
- Dataset structure overview

The uploaded sample images demonstrate the diversity of architectural styles used in the complete dataset.

---

# Storage Note

The complete dataset contains approximately:

- 5,000 curated architectural images
- 2,000+ detailed architectural captions

The total dataset size is approximately 2.7 GB.

Due to GitHub storage limitations, only representative samples of the dataset are included in this repository.

---

# Applications

This dataset can support:

- Text-to-image generation
- Architectural visualization
- Generative AI research
- NLP and Computer Vision tasks
- Diffusion model training
- Prompt engineering workflows
- AI-assisted design systems

---

# Technologies Associated with Dataset Development

- Python
- Stable Diffusion
- LoRA Fine-tuning
- NLP-based Caption Structuring
- Image Preprocessing Pipelines
- Deep Learning Workflows

---

# Research Context

This dataset was developed as part of an academic research project exploring the intersection of:

- Artificial Intelligence
- Computer Vision
- Natural Language Processing
- Architectural Design Automation

The project focuses on generating architectural layouts and design concepts directly from textual prompts using Machine Learning and Generative AI models.

---

# Contributors

- Spoorthi Pai
- Project Team Members
