# Geldium Reproducible Research

## Project Overview
This project focuses on reproducible research and customer delinquency analysis using the Geldium dataset.

## Research Question
Can customer financial characteristics and payment history help predict whether a customer will become delinquent?

## Objectives
- Understand customer financial and payment behaviour.
- Identify factors associated with customer delinquency.
- Develop predictive models.
- Evaluate model performance using appropriate metrics.
- Ensure the analysis is reproducible and transparent.

## Dataset
The project uses the Geldium customer dataset.

Target variable: `Delinquent_Account`

## Methodology
1. Data loading and inspection.
2. Data cleaning and preprocessing.
3. Exploratory Data Analysis.
4. Feature selection and engineering.
5. Predictive modelling using Logistic Regression and Decision Tree.
6. Model evaluation using stratified cross-validation.
7. Robustness and reproducibility checks.

## Repository Structure
- `data/raw/` – Original dataset.
- `data/interim/` – Intermediate datasets.
- `data/processed/` – Cleaned datasets.
- `notebooks/` – Research notebooks.
- `reports/` – Research reports.
- `src/` – Python source code.
- `tests/` – Synthetic pipeline tests.

## Reproducibility
Python dependencies and their versions will be documented in the environment requirements file. Synthetic data will be used to validate the pipeline without inspecting actual outcome patterns.

## Research Integrity
The research question, hypotheses, exclusion criteria, transformations and analysis methods will be documented before examining outcome patterns.

## Status
Research repository setup in progress.
