# AI-Driven Prediction of Geopolymer Concrete Compressive Strength

This repository provides a reproducible machine learning pipeline for predicting
the compressive strength of fly ash–based geopolymer concrete using experimentally
reported datasets from peer-reviewed literature.

The implementation supports the book chapter:
"AI-Driven Innovations in Sustainable Engineering Projects"
published in *Advances in Machine Learning for Engineering Applications and Sustainable Development*.

## Dataset
The dataset structure follows published experimental studies (e.g., Chithra et al., 2016).
No synthetic or fabricated data are used.

## Machine Learning Model
- Random Forest Regressor
- Train–test split with feature scaling
- Performance metrics: R², RMSE, MAE

## Output
- Figure 3: Experimental vs ML-predicted compressive strength
- Performance metrics saved to file

## How to Run
```bash
pip install -r requirements.txt
python main.py
