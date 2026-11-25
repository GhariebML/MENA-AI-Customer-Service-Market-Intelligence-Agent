# Dataset Analysis Summary — Bitext Customer Support Corpus

**Source:** `20000-Utterances-Training-dataset-for-chatbots-virtual-assistant-Bitext-sample.csv`  
**Analyzed Rows:** `21,534` | **Categories:** `11` | **Intents:** `27` | **Analysis Date:** 25 November 2026

---

## 1. Key Quantitative Findings (Computed Actuals)

1. **Top Support Categories Concentrating Inquiry Volume:**
   - **PAYMENT** (`4,636` rows | `21.53%`) and **ACCOUNT** (`4,557` rows | `21.16%`) together make up `42.69%` (`9,193` rows) of the dataset.
   - Followed by **CONTACT** (`3,081` | `14.31%`), **INVOICES** (`2,443` | `11.34%`), **ORDER** (`2,256` | `10.48%`), and **REFUNDS** (`1,932` | `8.97%`).
   - Together, the top 6 categories represent `87.79%` (`18,905` rows) of all utterances, while **FEEDBACK** (`6.16%`), **DELIVERY** (`2.33%`), **CANCELLATION_FEE** (`1.67%`), **NEWSLETTER** (`1.10%`), and **SHIPPING** (`0.96%`) represent the remaining `12.21%`.

2. **Extreme Concentration in Top Intents:**
   - **Top 5 intents** = `52.00%` (`11,197` rows): `payment_issue` (`4,366` | `20.27%`), `create_account` (`2,122` | `9.85%`), `contact_customer_service` (`2,055` | `9.54%`), `get_invoice` (`1,430` | `6.64%`), and `track_order` (`1,224` | `5.68%`).
   - **Top 10 intents** = `75.68%` (`16,297` rows), adding `get_refund` (`1,150`), `contact_human_agent` (`1,026`), `check_invoices` (`1,013`), `recover_password` (`986`), and `change_order` (`926`).

3. **Automation Tier Architecture Implications:**
   - **Tier 4 — Human-in-the-Loop Priority (`10,292` rows | `47.79%`):** `payment_issue`, `contact_customer_service`, `get_refund`, `contact_human_agent`, `delete_account`, `complaint`, `cancel_order`. Nearly half of all intents require sensitive financial authorization, policy exceptions, PDPL identity verification, or live human escalation.
   - **Tier 2 — Read-Only API Lookup (`4,956` rows | `23.01%`):** `get_invoice`, `track_order`, `check_invoices`, `recover_password`, `track_refund`. High-ROI automation targets once connected to order-management, ERP, or invoicing APIs.
   - **Tier 3 — Authenticated Transactional Action (`4,546` rows | `21.11%`):** `create_account`, `change_order`, `review`, `switch_account`, `newsletter_subscription`, `edit_account`, `change_shipping_address`, `set_up_shipping_address`, `place_order`. Requires structured slot-filling and confirmed API writes.
   - **Tier 1 — Knowledge-Base RAG (`1,740` rows | `8.08%`):** `check_refund_policy`, `check_cancellation_fee`, `delivery_options`, `check_payment_methods`, `delivery_period`, `registration_problems`. Pure static FAQ/RAG addresses less than one-tenth of the taxonomy—confirming that a generic FAQ-only chatbot is insufficient without API integrations and seamless human handoff.

4. **Linguistic Complexity & Noise Profile:**
   - `44.36%` (`9,552` rows) exhibit colloquial phrasing (`Q`), `15.84%` (`3,412` rows) contain spelling/punctuation noise (`Z`), `12.06%` (`2,596` rows) use indirect phrasing (`D`), and `4.86%` (`1,047` rows) include offensive/frustrated language (`W`)—notably spiking in complaints and payment issues.
   - **Utterance Conciseness:** Mean length is `10.86` words (`52.54` characters), closely resembling chat/messaging turn lengths rather than long-form emails.

---

## 2. Strategic Analytical Caution

These statistics rigorously characterize the **Bitext English dataset only**. They provide a validated taxonomy and technical architecture blueprint (showing why RAG + API Actions + Safe Human Escalation must work together), but **do not** prove ticket volume distribution, language mix, or willingness-to-pay among SMEs in Egypt, Saudi Arabia, or the UAE.
