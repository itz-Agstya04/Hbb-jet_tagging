# Hbb Jet Tagging

Machine Learning Pipeline for Identifying Higgs Boson Decays to Bottom Quarks (H → bb)

## Overview

This repository implements a complete **machine learning pipeline for jet tagging**, with a specific focus on identifying jets originating from **Higgs boson decays into bottom quark pairs (H → bb)**. Jet tagging is a central problem in high-energy physics, where the goal is to classify particle jets produced in collider experiments according to their physical origin.

The project uses supervised learning models to distinguish **Higgs jets** from background jets using kinematic and substructure features derived from jet constituents. The repository is designed as a **research-oriented implementation**, emphasizing clarity, interpretability, and reproducibility.


## Motivation

At particle colliders such as the Large Hadron Collider (LHC), the decay channel H → bb has the largest branching ratio for the Standard Model Higgs boson. However, identifying these events is challenging due to overwhelming background from QCD jet production.

Machine learning models have become a standard tool in jet tagging because they can learn complex correlations in high-dimensional feature spaces that are difficult to capture with traditional cut-based methods. This project explores such models in a controlled, reproducible setting.


## Project Goals

- Build a supervised learning model for Higgs jet tagging  
- Train and evaluate classifiers on H → bb jet data  
- Compare classical machine learning and neural network approaches  
- Analyze model performance using standard classification metrics  
- Provide a clean and extensible codebase for further experimentation  


## Dataset Description

The dataset used in this project consists of jet-level features derived from simulated high-energy collision events. Each jet is labeled according to whether it originates from a Higgs boson decay into bottom quarks or from background processes.

Typical features include:
- Jet kinematic variables
- Substructure observables
- Aggregate properties of jet constituents

The dataset is preprocessed to ensure consistency and suitability for machine learning models.


## Machine Learning Approach

The project follows a standard supervised learning workflow:

1. **Data Loading and Preprocessing**
   - Feature normalization and cleaning
   - Label preparation
   - Train–test split

2. **Model Training**
   - Classical machine learning models (e.g., gradient-boosted trees)
   - Neural network–based classifiers
   - Hyperparameter tuning

3. **Evaluation**
   - Classification accuracy
   - ROC curves and AUC
   - Confusion matrices
   - Comparative performance analysis

4. **Visualization**
   - Feature distributions
   - Model performance plots
   - Training diagnostics
   - ## Results Summary

The jet tagging models were evaluated using standard binary classification metrics.
Both classical machine learning and neural network–based models were trained and compared.

Key observations:
- Gradient-boosted tree models provide a strong baseline performance.
- Neural network models achieve improved discrimination by learning nonlinear feature interactions.
- The results demonstrate that machine learning–based approaches can effectively separate Higgs-origin jets from background jets in this dataset.

Performance is reported using ROC curves and AUC scores, with visualizations available in the notebooks.



## Repository Structure

```text
Hbb-jet_tagging/
│
├── notebooks/
│   Jupyter notebooks for data exploration, model training,
│   evaluation, and result visualization.
│
├── src/
│   Core Python scripts for data handling, model training,
│   and evaluation logic.
│
├── artifacts/
│   Saved model outputs, plots, and intermediate results.
│
├── requirements.txt
│   Python dependencies required to run the project.
│
└── README.md
