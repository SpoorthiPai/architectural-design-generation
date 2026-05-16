# Architectural Design Generation from Textual Descriptions

## Overview

This project focuses on generating architectural designs from textual descriptions using Machine Learning and Generative AI techniques.

The primary objective of the project is to explore how Natural Language Processing (NLP) and Generative AI models can be used to convert descriptive architectural prompts into meaningful architectural visualizations and layout representations.

The project combines:

- Text preprocessing
- Semantic caption understanding
- Dataset curation
- Image generation workflows
- Deep learning-based architectural visualization

to study AI-assisted architectural design automation.

---

# Problem Statement

Architectural visualization and conceptual design traditionally require significant manual effort, time, and iterative drafting processes.

This project aims to simplify the early-stage architectural ideation process by enabling AI systems to generate architectural concepts directly from textual prompts.

Examples:

```text
"
Full front view of a luxurious 
modern villa with large glass 
facades, minimalistic concrete walls, 
swimming pool reflecting the sky, 
landscaped garden, sunlit exterior "
```

↓
<img width="743" height="644" alt="image" src="https://github.com/user-attachments/assets/e9ed186c-b5c7-4e94-9138-d24289c9a257" />

AI-generated architectural output.

text
"Full front view of a cozy Nordic 
cabin in a snowy pine forest, smoke 
curling from the chimney, snow
covered roof and trees, warm golden 
light from windows "
```

<img width="724" height="649" alt="image" src="https://github.com/user-attachments/assets/abec79f0-4f06-4272-9782-594939496ab3" />

text
"Japanese Machiya house with 
wooden lattice windows, sliding 
doors "
```

<img width="808" height="617" alt="image" src="https://github.com/user-attachments/assets/3b45fa79-ff7e-4650-ae5b-b50dff494d3b" />

text
"A grand colonial mansion with white 
pillars, expansive garden with 
trimmed hedges, red-tiled roof, 
symmetrical windows, soft natural 
lighting, wide-angle exterior view "
```

<img width="837" height="671" alt="image" src="https://github.com/user-attachments/assets/59fd8c4f-15e5-4039-9b24-c1195941aefe" />

text
"African village with mud huts 
surrounded with small green plants "
```

<img width="820" height="752" alt="image" src="https://github.com/user-attachments/assets/30ed047b-0d21-451f-b0ee-4fea39e51396" />

---

# Objectives

- Generate architectural designs from textual descriptions
- Explore text-to-image generation workflows
- Build a structured architectural dataset
- Study semantic alignment between prompts and generated outputs
- Investigate AI-assisted architectural visualization systems

---

# Technologies Used

## Programming & Development
- Python
- Jupyter Notebook

## Machine Learning & AI
- PyTorch
- Stable Diffusion
- LoRA Fine-Tuning
- NLP-based Prompt Structuring

## Data Processing
- NumPy
- Pandas
- OpenCV
- Matplotlib

## Version Control
- Git
- GitHub

---

# Dataset Information

The dataset was created and curated as part of the project workflow.

## Dataset Statistics

- Initial dataset collection: 10,000+ images
- Final cleaned dataset: ~5,000 architectural images
- Detailed captions generated: 2,000+ captions
- Dataset size: ~2.7 GB

---

# Dataset Features

The dataset contains:

- Architectural exterior images
- Detailed architectural captions
- Multiple architectural styles
- Structural and façade descriptions
- Roof geometry descriptions
- Environmental context annotations
- Lighting and scene details
- Camera angle and perspective information

---

# Architectural Categories

The dataset includes diverse architectural styles such as:

- Modern Villas
- Contemporary Houses
- Japanese Machiya Structures
- Colonial Buildings
- Apartments
- Rural Houses
- Nordic Cabins
- Minimalist Structures
- Urban Buildings
- Bamboo Houses
- Skyscrapers
- Commercial Structures

---

# Captioning Methodology

Detailed captions were generated for architectural images to improve semantic understanding for text-to-image generation tasks.

Each caption includes:

- Architectural style
- Number of floors
- Roof structure and geometry
- Exterior materials
- Window and door arrangements
- Façade symmetry
- Color palette
- Environmental surroundings
- Lighting conditions
- Camera angle and framing

---

# Project Workflow

## 1. Dataset Collection
Architectural images from multiple categories and styles were collected.

## 2. Dataset Cleaning
Duplicate and low-quality images were removed.

## 3. Caption Generation
Detailed captions were generated to provide semantic architectural descriptions.

## 4. Data Preprocessing
Images and captions were prepared for model workflows.

## 5. Embedding & Prompt Structuring
Textual prompts were processed for model understanding.

## 6. Model Training & Fine-Tuning
Generative AI workflows were explored using Stable Diffusion and related techniques.

## 7. Output Evaluation
Generated outputs were analyzed for architectural consistency and visual quality.

---

# Repository Structure

```text
project-root/
│
├── dataset/
│   ├── captions/
│   ├── sample-images/
│   └── dataset-info.md
│
├── docs/
│
├── notebooks/
│
├── outputs/
│
├── screenshots-results/
│   └── result-info.md
│
├── src/
│
├── README.md
└── requirements.txt
```

---

# Sample Results

The repository includes representative generated outputs and architectural visualization samples.

The outputs demonstrate:

- Architectural structure generation
- CAD-inspired layouts
- Text-to-image generation workflows
- AI-assisted architectural concepts
- Multi-style architectural visualization

---

# CAD-Based Outputs

Some generated outputs include CAD-inspired architectural visualizations intended to simulate:

- Structural layouts
- Building elevations
- Conceptual drafting representations
- Architectural planning references

---

# Research Contributions

Key contributions explored in this project include:

- Structured architectural dataset curation
- Rich semantic caption generation
- Architectural prompt engineering
- AI-assisted architectural visualization workflows
- Exploration of Generative AI for design automation

---

# Applications

Potential applications include:

- AI-assisted architectural ideation
- Automated design visualization
- Smart architectural planning systems
- Generative design workflows
- Architectural concept prototyping
- Educational and research applications

---

# Future Enhancements

- Interactive user interface
- Cloud deployment
- Advanced fine-tuning workflows

---

# Learning Outcomes

This project provided practical exposure to:

- Machine Learning workflows
- Dataset preprocessing
- Generative AI systems
- NLP-based prompt engineering
- Computer Vision concepts
- Research-oriented implementation workflows

---

# Contributors

- Spoorthi Pai
- Project Team Members

---

# Note

This repository contains representative samples and project documentation intended for academic, research, and portfolio purposes.

Due to GitHub storage limitations, only selected sample files and outputs are included.

```
