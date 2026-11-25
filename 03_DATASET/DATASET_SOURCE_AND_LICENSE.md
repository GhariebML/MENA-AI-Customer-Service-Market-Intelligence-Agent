# Dataset Source and License Record

| Attribute | Verified Record |
|---|---|
| **Dataset Title** | Training Dataset for Chatbots / Virtual Assistants (Bitext Sample Pre-built Customer Support Dataset for English) |
| **Author / Creator** | Bitext Innovations (2020) |
| **Official Kaggle URL** | https://www.kaggle.com/datasets/bitext/training-dataset-for-chatbotsvirtual-assistants |
| **Direct API Download URL** | https://www.kaggle.com/api/v1/datasets/download/bitext/training-dataset-for-chatbotsvirtual-assistants |
| **Date Accessed & Downloaded** | 25 November 2026 |
| **Archive Filename** | `training-dataset-for-chatbotsvirtual-assistants.zip` (`1,214,677` bytes) |
| **Archive SHA-256 Checksum** | `f9bc8f3991e769515680ced429fa80bc60a98a7cdb9c1c82bcf33abd53413a1b` |
| **Primary CSV Analyzed** | `20000-Utterances-Training-dataset-for-chatbots-virtual-assistant-Bitext-sample.csv` (`21,534` rows, 4 columns) |
| **Companion CSV in Archive** | `Bitext_Sample_Customer_Service_Training_Dataset.csv` (`8,175` rows, 4 columns, balanced ~295–324 rows/intent) |
| **License** | Community Data License Agreement – Sharing – Version 1.0 (**CDLA-Sharing-1.0**) |
| **Language** | English (`en`) |

---

## Archive Structure Note

The official Kaggle ZIP archive contains two distinct sub-directories published by Bitext:

1. **`20000-Utterances-Training-dataset-for-chatbots-virtual-assistant-Bitext-sample/`**
   - `20000-Utterances-Training-dataset-for-chatbots-virtual-assistant-Bitext-sample.csv` (`21,534` rows)
   - `20000-Utterances-Training-dataset-for-chatbots-virtual-assistant-Bitext-sample.xlsx`
   - `LICENSE.txt` (CDLA-Sharing-1.0) and `README.txt`
   - **Analytical Role:** Primary dataset profiled across this project, matching the Kaggle description ("over 20,000 utterances, with a varying number of utterances per intent") and preserving realistic class skew across 27 customer support intents.

2. **`Bitext_Sample_Customer_Service_Training_Dataset/Training/`**
   - `Bitext_Sample_Customer_Service_Training_Dataset.csv` (`8,175` rows)
   - `Bitext_Sample_Customer_Service_Training_Dataset.xlsx`
   - `LICENSE.txt` and `README.txt`
   - **Analytical Role:** Companion balanced training sample across the same 27 intents (using singular category labels `REFUND`, `INVOICE`, `SHIPPING_ADDRESS` and ~300 utterances per intent). Retained untouched in `03_DATASET/raw/` for completeness and cross-check.

---

## License Summary (CDLA-Sharing-1.0)

Under **Community Data License Agreement – Sharing, Version 1.0**:
- **Permitted Use:** Worldwide, non-exclusive right to access, study, analyze, perform Computational Use, and publish Results (statistical aggregations, visualizations, and insights).
- **Attribution Condition:** Preserve attribution to the Data Provider (`Bitext Innovations`) and retain the unmodified `LICENSE.txt` text when redistributing the dataset.
- **No Warranty:** Data is provided "AS IS" without implied warranties; analytical users remain responsible for compliance with applicable privacy and data protection laws.
