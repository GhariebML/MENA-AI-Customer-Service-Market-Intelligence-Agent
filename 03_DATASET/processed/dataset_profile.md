# Bitext Dataset Profile (Computed Actuals)

**Source file:** `20000-Utterances-Training-dataset-for-chatbots-virtual-assistant-Bitext-sample.csv`
**Profiled date:** 2026-11-25
**Rows:** 21,534
**Columns:** 4 (flags, utterance, category, intent)
**Missing values:** 0
**Exact duplicate rows:** 12
**Duplicate utterance strings beyond first occurrence:** 21
**Class imbalance (top vs. bottom intent):** payment_issue (4,366) vs. cancel_order (36) = 121.28x
**Utterance length (words):** mean 10.86, median 10.0, range 2–28
**Utterance length (chars):** mean 52.54, median 51.0, range 10–128

## Schema

| Column | Present | Missing values | Unique values |
|---|---:|---:|---:|
| `flags` | Yes | 0 | 511 |
| `utterance` | Yes | 0 | 21,513 |
| `category` | Yes | 0 | 11 |
| `intent` | Yes | 0 | 27 |

## Category distribution (11 categories)

| Category | Count | Share |
|---|---:|---:|
| PAYMENT | 4,636 | 21.53% |
| ACCOUNT | 4,557 | 21.16% |
| CONTACT | 3,081 | 14.31% |
| INVOICES | 2,443 | 11.34% |
| ORDER | 2,256 | 10.48% |
| REFUNDS | 1,932 | 8.97% |
| FEEDBACK | 1,326 | 6.16% |
| DELIVERY | 501 | 2.33% |
| CANCELLATION_FEE | 360 | 1.67% |
| NEWSLETTER | 236 | 1.10% |
| SHIPPING | 206 | 0.96% |

## Intent distribution (27 intents)

| Intent | Category | Count | Share | Automation Tier |
|---|---|---:|---:|---|
| payment_issue | PAYMENT | 4,366 | 20.27% | Tier 4 - Human-in-the-Loop Priority |
| create_account | ACCOUNT | 2,122 | 9.85% | Tier 3 - Authenticated Action |
| contact_customer_service | CONTACT | 2,055 | 9.54% | Tier 4 - Human-in-the-Loop Priority |
| get_invoice | INVOICES | 1,430 | 6.64% | Tier 2 - API Status Lookup |
| track_order | ORDER | 1,224 | 5.68% | Tier 2 - API Status Lookup |
| get_refund | REFUNDS | 1,150 | 5.34% | Tier 4 - Human-in-the-Loop Priority |
| contact_human_agent | CONTACT | 1,026 | 4.76% | Tier 4 - Human-in-the-Loop Priority |
| check_invoices | INVOICES | 1,013 | 4.70% | Tier 2 - API Status Lookup |
| recover_password | ACCOUNT | 986 | 4.58% | Tier 2 - API Status Lookup |
| change_order | ORDER | 926 | 4.30% | Tier 3 - Authenticated Action |
| delete_account | ACCOUNT | 913 | 4.24% | Tier 4 - Human-in-the-Loop Priority |
| complaint | FEEDBACK | 746 | 3.46% | Tier 4 - Human-in-the-Loop Priority |
| review | FEEDBACK | 580 | 2.69% | Tier 3 - Authenticated Action |
| check_refund_policy | REFUNDS | 479 | 2.22% | Tier 1 - Knowledge-Base RAG |
| check_cancellation_fee | CANCELLATION_FEE | 360 | 1.67% | Tier 1 - Knowledge-Base RAG |
| delivery_options | DELIVERY | 360 | 1.67% | Tier 1 - Knowledge-Base RAG |
| track_refund | REFUNDS | 303 | 1.41% | Tier 2 - API Status Lookup |
| switch_account | ACCOUNT | 273 | 1.27% | Tier 3 - Authenticated Action |
| check_payment_methods | PAYMENT | 270 | 1.25% | Tier 1 - Knowledge-Base RAG |
| newsletter_subscription | NEWSLETTER | 236 | 1.10% | Tier 3 - Authenticated Action |
| delivery_period | DELIVERY | 141 | 0.65% | Tier 1 - Knowledge-Base RAG |
| edit_account | ACCOUNT | 133 | 0.62% | Tier 3 - Authenticated Action |
| registration_problems | ACCOUNT | 130 | 0.60% | Tier 1 - Knowledge-Base RAG |
| change_shipping_address | SHIPPING | 110 | 0.51% | Tier 3 - Authenticated Action |
| set_up_shipping_address | SHIPPING | 96 | 0.45% | Tier 3 - Authenticated Action |
| place_order | ORDER | 70 | 0.33% | Tier 3 - Authenticated Action |
| cancel_order | ORDER | 36 | 0.17% | Tier 4 - Human-in-the-Loop Priority |

## Automation Tier Rollup

| Automation Tier | Utterance Count | Share of Dataset |
|---|---:|---:|
| Tier 4 - Human-in-the-Loop Priority | 10,292 | 47.79% |
| Tier 2 - API Status Lookup | 4,956 | 23.01% |
| Tier 3 - Authenticated Action | 4,546 | 21.11% |
| Tier 1 - Knowledge-Base RAG | 1,740 | 8.08% |

## Analytical Guardrails

- Every count and percentage above is computed strictly from the downloaded CSV.
- The dataset is English-only synthetic/curated training data and cannot establish MENA market size, SME demand, or willingness to pay.
- Use these intent patterns as discovery hypotheses to validate against local SME Arabic/English support logs.
