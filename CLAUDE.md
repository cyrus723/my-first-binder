# CLAUDE.md — my-first-binder

## Project Overview
A Binder-compatible Python data science and finance research repository. Contains Jupyter notebooks covering quantitative finance, NLP, regression modeling, and data analysis.

Binder launch URL: https://mybinder.org/v2/gh/cyrus723/my-first-binder/main?labpath=simple_regression_1.ipynb

## Repository Structure
- `*.ipynb` — Jupyter notebooks (main work)
- `*.py` — standalone Python scripts
- `data/` — local datasets (CSV, TSV, XLSX, TXT)
- `requirements.txt` — Python dependencies
- `olympics.csv`, `factsets_etf.csv` — root-level data files

## Key Data Files (in `data/`)
- `sp500.csv`, `sp500list_risk.csv` — S&P 500 data
- `compustat_2010_2022.csv` — WRDS Compustat data
- `Corona_NLP_train.csv`, `Corona_NLP_test.csv` — NLP sentiment dataset
- `SMSSpamCollection.tsv` — spam classification dataset
- `hist_ret.csv`, `historical_return.csv` — historical returns
- `earnings.csv`, `fed.csv` — macro/earnings data
- `Facset1.csv`, `Factset_corp.csv` — FactSet financial data
- `newspaper.csv` — news data for NLP

## Dependencies
Install with:
```bash
pip install -r requirements.txt
```
Key packages: `numpy`, `pandas`, `statsmodels`, `matplotlib`, `seaborn`, `sklearn`, `torch`, `transformers`, `gensim`, `spacy`, `openai`, `anthropic`, `streamlit`

## Notebook Topics
- **Finance**: CAPM, OLS regression, bond pricing, FactSet, WRDS (CRSP/Compustat), S&P 500, yfinance, stock charts
- **NLP/ML**: LDA topic modeling, sentiment analysis, word embeddings (gensim), Keras, word clouds
- **Data**: EPL soccer stats, Olympics, Kaggle API, FRED economic data, pandas basics

## Notes
- Notebooks may contain hardcoded local paths (e.g. `C:/Users/...`) — update paths to use `data/` directory before running
- Magic commands like `%config` are Jupyter-only and must be removed when running as `.py` scripts
- To convert a notebook to a script: `jupyter nbconvert --to script notebook.ipynb`
- Some notebooks require external API credentials (WRDS, Kaggle, FactSet, OpenAI)
