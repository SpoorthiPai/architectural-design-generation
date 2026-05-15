# Dataset Information

## Overview

The dataset used in this project was created and curated by the project team for generating architectural designs from textual descriptions using Machine Learning and Generative AI techniques.

The dataset contains paired architectural images and highly detailed textual captions describing structural, architectural, environmental, and visual characteristics of buildings.

This dataset was designed specifically for text-to-image architectural generation tasks and focuses on improving descriptive richness, architectural diversity, and contextual understanding for generative models.

---

# Dataset Objectives

The primary objectives of this dataset are:

- Generate architectural designs from textual prompts
- Improve semantic understanding of architectural descriptions
- Support text-to-image generation workflows
- Enable training and evaluation of generative AI models
- Explore AI-assisted architectural visualization

---

# Dataset Characteristics

The dataset includes:

- Architectural exterior images
- Detailed image captions
- Structural descriptions
- Material descriptions
- Roof and façade descriptions
- Environmental context information
- Lighting and viewpoint descriptions
- Architectural style classifications

---

# Captioning Methodology

Each image in the dataset is paired with a highly detailed descriptive caption.

The captions include:

- Architectural style
- Roof structure and geometry
- Building materials
- Façade symmetry and layout
- Window and door descriptions
- Color palette
- Environmental surroundings
- Lighting conditions
- Camera angle and framing
- Scale references

This detailed captioning approach was designed to improve semantic alignment between textual prompts and generated architectural outputs.

---

# Example Caption Structure

The captions describe multiple architectural attributes including:

- Building type
- Number of visible floors
- Roof style and pitch
- Exterior wall materials
- Window and door arrangements
- Architectural symmetry
- Environmental surroundings
- Lighting conditions
- Perspective and camera angle

Example categories include:

- Modern Villas
- Traditional Japanese Machiya Houses
- Colonial Architecture
- Rural Houses
- Urban Buildings
- Apartments
- Skyscrapers
- Nordic Cabins
- Farmhouses
- Mixed-use Buildings

---

# Dataset Categories

The dataset contains diverse architectural styles such as:

- Modern Architecture
- Traditional Japanese Architecture
- Colonial Structures
- Contemporary Villas
- Rural and Vernacular Housing
- Urban Residential Buildings
- Commercial Structures
- High-rise Buildings
- Scandinavian and Nordic Cabins
- Minimalist Concrete Houses
- Eco-friendly and Bamboo Structures

---

# Image Characteristics

The dataset includes architectural images with:

- Multiple façade types
- Different roof geometries
- Various material combinations
- Diverse environmental settings
- Seasonal variations
- Multiple architectural scales
- Daylight and natural illumination conditions

---

# Dataset Preparation Workflow

## 1. Image Collection
Architectural images representing multiple building styles and regions were collected and organized.

## 2. Image Filtering
Low-quality, duplicated, and irrelevant images were removed.

## 3. Caption Generation
Detailed captions were manually curated/generated to describe architectural and environmental features.

## 4. Data Structuring
Images and captions were paired and organized systematically for model training.

## 5. Preprocessing
Images were resized, normalized, and prepared for generative model workflows.

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

# Captions

The dataset includes more than 2000 detailed architectural captions paired with corresponding images.

Captions are structured in JSON format using image filenames as keys and descriptive architectural annotations as values.

Example format:

```json
{
  "Modern_villa_00001.jpg": "Detailed architectural description..."
}
```

---

# Sample Dataset Files

This repository includes:

- Representative sample images
- Sample captions
- Dataset documentation
- Dataset structure overview

---

# Storage Note

The complete dataset size is approximately 2.7 GB.

Due to GitHub storage limitations, only representative samples of the dataset are included in this repository.

---

# Applications

This dataset can support:

- Text-to-image generation
- Architectural visualization
- Generative AI research
- NLP and vision-language tasks
- Diffusion model training
- Prompt engineering research
- Design automation systems

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

This dataset was developed as part of an academic Machine Learning research project focused on generating architectural designs from textual descriptions.

The project explores the intersection of:

- Artificial Intelligence
- Computer Vision
- Natural Language Processing
- Architectural Design Automation

---

# Contributors

- Spoorthi Pai
- Project Team Members

