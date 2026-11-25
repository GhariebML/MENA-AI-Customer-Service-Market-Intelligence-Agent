# Data Dictionary — Bitext Customer Support Dataset

**Primary File:** `03_DATASET/raw/20000-Utterances-Training-dataset-for-chatbots-virtual-assistant-Bitext-sample.csv`  
**Total Records:** `21,534` | **Total Columns:** `4` | **Missing Values:** `0`

---

## 1. Column Schema

| Column Name | Data Type | Nullable | Unique Values | Description |
|---|---|---|---|---|
| `flags` | `string` | No (0 nulls) | `511` combinations (`12` atomic flag letters) | Concatenated uppercase single-letter codes describing syntactic, lexical, register, and noise variations present in the utterance. |
| `utterance` | `string` | No (0 nulls) | `21,513` unique strings | Natural-language English customer support query or request (length: `10–128` characters, `2–28` words). |
| `category` | `string` | No (0 nulls) | `11` categories | High-level business/functional support domain grouping related intents. |
| `intent` | `string` | No (0 nulls) | `27` intents | Specific actionable customer goal (strictly 1-to-1 mapped to a parent `category`). |

---

## 2. Linguistic Flag Code Definitions (Verified Across 21,534 Rows)

Every row includes a string composed of one or more of the following 12 flag codes documented in Bitext's `README.txt` and verified in the CSV:

| Code | Linguistic Phenomenon | Row Count | Share of Dataset | Relevance to MENA SME Automation |
|---|---|---:|---:|---|
| `B` | Basic syntactic structure | 21,534 | 100.00% | Baseline clause structure present in all utterances. |
| `L` | Lexical variation (synonyms) | 18,752 | 87.08% | Tests semantic retrieval rather than brittle keyword matching. |
| `I` | Interrogative structure | 12,766 | 59.28% | Question-phrased tickets requiring direct factual or status answers. |
| `C` | Complex / coordinated syntactic structure | 10,911 | 50.67% | Multi-clause requests that often mix context and requests. |
| `Q` | Colloquial variation | 9,552 | 44.36% | Informal everyday phrasing; critical analogy for Arabic dialect/Arabizi normalization. |
| `Z` | Noise (spelling mistakes, punctuation, run-on words) | 3,412 | 15.84% | Simulates real mobile WhatsApp/chat typing errors. |
| `P` | Politeness variation | 2,888 | 13.41% | Respectful phrasing requiring matching polite tone in replies. |
| `M` | Morphological variation (plurals, tenses) | 2,836 | 13.17% | Inflected word forms; Arabic morphology is even richer and requires lemmatization/LLM handling. |
| `D` | Indirect speech (e.g., *"ask an agent to..."*) | 2,596 | 12.06% | Indirect intent phrasing where naive keyword triggers fail. |
| `S` | Syntactic structure variation | 1,884 | 8.75% | Non-canonical word order variations. |
| `W` | Offensive / swearing language | 1,047 | 4.86% | Frustrated or abusive messages requiring sentiment-aware escalation to human agents. |
| `E` | Expanded abbreviations (*"I'm"* to *"I am"*) | 392 | 1.82% | Formalized contraction expansions. |

---

## 3. Category & Intent Taxonomy (11 Categories → 27 Intents)

| Category | Category Count | Category Share | Mapped Intents |
|---|---:|---:|---|
| `PAYMENT` | 4,636 | 21.53% | `payment_issue` (4,366), `check_payment_methods` (270) |
| `ACCOUNT` | 4,557 | 21.16% | `create_account` (2,122), `recover_password` (986), `delete_account` (913), `switch_account` (273), `edit_account` (133), `registration_problems` (130) |
| `CONTACT` | 3,081 | 14.31% | `contact_customer_service` (2,055), `contact_human_agent` (1,026) |
| `INVOICES` | 2,443 | 11.34% | `get_invoice` (1,430), `check_invoices` (1,013) |
| `ORDER` | 2,256 | 10.48% | `track_order` (1,224), `change_order` (926), `place_order` (70), `cancel_order` (36) |
| `REFUNDS` | 1,932 | 8.97% | `get_refund` (1,150), `check_refund_policy` (479), `track_refund` (303) |
| `FEEDBACK` | 1,326 | 6.16% | `complaint` (746), `review` (580) |
| `DELIVERY` | 501 | 2.33% | `delivery_options` (360), `delivery_period` (141) |
| `CANCELLATION_FEE` | 360 | 1.67% | `check_cancellation_fee` (360) |
| `NEWSLETTER` | 236 | 1.10% | `newsletter_subscription` (236) |
| `SHIPPING` | 206 | 0.96% | `change_shipping_address` (110), `set_up_shipping_address` (96) |
