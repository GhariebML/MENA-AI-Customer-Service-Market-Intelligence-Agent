# Reproducibility Guide — Data Science & Visual Evidence Pipeline

**Project:** MENA AI Customer Service Automation Market Intelligence  
**Student:** Mohamed Abd Elsalam Mohamed Gharieb  
**Program:** AWS AI & ML Scholars Program — Future AWS Agentic AI Business Professional  
**Dataset:** Bitext — Training Dataset for Chatbots / Virtual Assistants (Kaggle)

---

## 1. Environment Setup

```bash
python -m venv .venv
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
# Linux / macOS:
# source .venv/bin/activate

pip install -r 04_DATA_ANALYTICS/requirements.txt
```

## 2. Dataset Acquisition Verification

The official archive was retrieved on **25 November 2026** from:  
`https://www.kaggle.com/api/v1/datasets/download/bitext/training-dataset-for-chatbotsvirtual-assistants`

- **Archive path:** `03_DATASET/raw/training-dataset-for-chatbotsvirtual-assistants.zip`
- **Archive size:** `1,214,677` bytes
- **Archive SHA-256:** `f9bc8f3991e769515680ced429fa80bc60a98a7cdb9c1c82bcf33abd53413a1b`
- **Primary dataset file:** `03_DATASET/raw/20000-Utterances-Training-dataset-for-chatbots-virtual-assistant-Bitext-sample.csv` (`21,534` rows, 4 columns)
- **Companion dataset file in archive:** `03_DATASET/raw/Bitext_Sample_Customer_Service_Training_Dataset.csv` (`8,175` rows, 4 columns)

## 3. Reproducing Dataset Profiling Outputs

Run the standalone profiler script from `04_DATA_ANALYTICS/`:

```bash
python dataset_profiler.py ^
  "../03_DATASET/raw/20000-Utterances-Training-dataset-for-chatbots-virtual-assistant-Bitext-sample.csv" ^
  --out-dir "../03_DATASET/processed" ^
  --analysis-csv "./analysis_results.csv"
```

### Expected Generated Outputs
- `03_DATASET/processed/dataset_profile.json`
- `03_DATASET/processed/dataset_profile.md`
- `03_DATASET/processed/category_counts.csv`
- `03_DATASET/processed/intent_counts.csv`
- `03_DATASET/processed/flags_counts.csv`
- `03_DATASET/processed/linguistic_flag_breakdown.csv`
- `03_DATASET/processed/intent_category_crosstab.csv`
- `03_DATASET/processed/text_length_statistics.csv`
- `03_DATASET/processed/automation_suitability_mapping.csv`
- `04_DATA_ANALYTICS/analysis_results.csv`

## 4. Reproducing the Exploratory Data Analysis Notebook

Open `04_DATA_ANALYTICS/Market_Intelligence_EDA.ipynb` in JupyterLab or VS Code and run all cells sequentially, or execute via CLI if `jupyter` is installed:

```bash
jupyter nbconvert --to notebook --execute --inplace 04_DATA_ANALYTICS/Market_Intelligence_EDA.ipynb
```

## 5. Analytical Guardrails

1. Every chart and statistical table reads strictly from `03_DATASET/raw/` and `03_DATASET/processed/`.
2. Do not infer regional MENA demand, country market shares, or willingness-to-pay from this English training sample.
3. Keep raw files in `03_DATASET/raw/` read-only and unmodified.
