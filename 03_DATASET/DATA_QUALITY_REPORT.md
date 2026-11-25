# Data Quality Report — Bitext Customer Support Dataset

**File Audited:** `03_DATASET/raw/20000-Utterances-Training-dataset-for-chatbots-virtual-assistant-Bitext-sample.csv`  
**Audit Date:** 25 November 2026  
**Tooling:** `04_DATA_ANALYTICS/dataset_profiler.py` & Python `pandas` validation

---

## 1. Executive Data Quality Summary

| Quality Dimension | Result | Assessment |
|---|---|---|
| **Total Rows** | `21,534` | Matches Kaggle description ("over 20,000 utterances"). |
| **Total Columns** | `4` (`flags`, `utterance`, `category`, `intent`) | Matches documented schema (`100%` header integrity). |
| **Missing / Null Values** | `0` across all 4 columns (`0.00%`) | Excellent completeness; no imputation needed. |
| **Exact Duplicate Rows** | `12` (`0.056%`) | Negligible impact; keep raw file untouched and optionally deduplicate during NLU training (`21,522` unique rows). |
| **Duplicate Utterance Texts** | `21` (`0.098%`) | Some short utterances repeat with minor flag differences (`21,513` unique text strings). |
| **Label Consistency (Intent → Category)** | `27/27` strictly 1-to-1 | Zero cross-category label leakage (`100%` hierarchical taxonomy consistency). |
| **Class Imbalance Ratio** | `121.28x` (`payment_issue`: 4,366 vs. `cancel_order`: 36) | Severe intentional/stratified skew; critical limitation for classifier training and interpretation. |
| **Text Length Range** | `2–28` words (`10–128` chars) | Clean, realistic short-message range; zero empty strings or extreme outliers. |

---

## 2. Detailed Checks

### 2.1 Completeness & Encoding
- Encoded in UTF-8 (handled via `utf-8-sig` cleanly with zero decoding errors).
- Zero `NaN`, empty string, or whitespace-only entries in any column.

### 2.2 Duplicates & Redundancy
- `12` exact duplicate rows `(flags, utterance, category, intent)` exist out of `21,534` (`0.056%`).
- `21` repeated `utterance` strings exist beyond first occurrence (`21,513` unique utterance strings).
- For exploratory distribution counting, the raw file is preserved without silent row deletion; for model training, deduplicating exact rows reduces train/test leakage.

### 2.3 Class Imbalance & Companion File Comparison
- In the primary `21,534`-row file, the top 5 intents (`payment_issue`, `create_account`, `contact_customer_service`, `get_invoice`, `track_order`) account for `11,197` rows (`52.00%` of the entire dataset), while the bottom 5 intents (`registration_problems`, `change_shipping_address`, `set_up_shipping_address`, `place_order`, `cancel_order`) account for only `442` rows (`2.05%`).
- By contrast, the companion file included in the same Kaggle ZIP (`Bitext_Sample_Customer_Service_Training_Dataset.csv`, `8,175` rows, `0` exact duplicates) is nearly uniformly balanced (`~295–324` rows per intent).
- **Implication:** Any model trained on the `21,534`-row sample requires class weighting or stratified evaluation; conversely, the proportions in the `21,534`-row file reflect Bitext's stratified sampling design (extracted from `288,000` synthetic/curated utterances), **not** live customer ticket frequencies in Egypt, Saudi Arabia, or the UAE.

### 2.4 Representativeness & Geographic Validity Limitations
1. **Language Limitation:** 100% English (`en`). Contains zero Modern Standard Arabic (MSA), Egyptian Arabic, Gulf/Saudi dialects, or Arabizi code-switching.
2. **Channel & Context Limitation:** No channel tag (WhatsApp vs. web chat vs. email), no voice-note indicator, no SME vertical tag, no customer satisfaction (`CSAT`), and no resolution cost or willingness-to-pay field.
3. **Regional Regulatory Limitation:** Cannot test PDPL compliance, data residency, or local payment workflows (e.g., Mada, Fawry, Tabby/Tamara, Cash-on-Delivery).
