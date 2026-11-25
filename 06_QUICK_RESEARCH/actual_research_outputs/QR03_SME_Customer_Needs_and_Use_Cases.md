# QR-03: SME Customer Needs, WhatsApp Channels & Automation Use Cases

**Research Task:** QR-03 — Customer Needs & Operational Workflows  
**Evidence Sources:** Bitext Customer Support Corpus (`N = 21,534`, internal taxonomy [S1]), Meta WhatsApp Business Platform Pricing Documentation [S22], and MENA Messaging Adoption Signals.

---

## 1. Separating Verified Signals from Hypotheses

| Finding Type | Statement | Evidence Status |
|---|---|---|
| **Verified Platform Rule** | Effective **1 July 2025**, Meta shifted WhatsApp Business Platform from 24-hour conversation windows to **per-template message delivery pricing** (Marketing always charged; Utility free inside an open 24-hour customer-service window; non-template replies inside 24h free). | **VERIFIED** [S22] |
| **Verified Dataset Composition** | Across `21,534` English support utterances in the Bitext sample, `47.79%` (`10,292`) involve payment issues, refunds, complaints, account deletion, or explicit human contact; `44.13%` (`9,502`) involve API lookups or transactional actions; only `8.08%` (`1,740`) are pure policy FAQs. | **VERIFIED (Bitext sample only)** [S1] |
| **Industry Signal / Regional Trend** | WhatsApp functions as primary business communication across Egypt (`57M+` users), Saudi Arabia, and UAE; many SMEs still share informal mobile numbers causing lost chat history and slow manual replies. | **DIRECTIONAL INDUSTRY SIGNAL** (requires SME validation) |
| **Unproven Hypothesis** | Regional SME willingness to pay (`$X/month`) and exact share of voice-note vs. text inquiries across verticals. | **HYPOTHESIS** (must test via interviews) |

---

## 2. Operational Pain Points to Validate in Discovery Interviews

1. **Channel Fragmentation & Lost Context:** SMEs frequently handle inquiries across personal WhatsApp devices, Instagram DMs, and web forms without unified ticketing or SLA tracking.
2. **Response-Time Expectations vs. Staffing Costs:** Out-of-hours inquiries (evenings/weekends, Ramadan shift patterns) create order-abandonment risk unless automated triage answers immediate status and policy questions.
3. **WhatsApp Cost Optimization Post-July 2025:** Because Meta makes free-form and utility messages **free inside an active 24-hour user-initiated service window** [S22], fast AI response within the 24-hour window protects SME margins versus delayed template follow-ups.
4. **Dialect, Code-Switching & Noisy Input:** In Bitext (`S1`), `44.36%` of utterances use colloquial style (`Q`) and `15.84%` contain spelling/punctuation noise (`Z`). In MENA WhatsApp chats, customers additionally switch between Egyptian/Gulf Arabic, MSA, English product terms, and Arabizi.
5. **Human-in-the-Loop Escalation Friction:** Generic bots trap angry customers in loops. Bitext shows `payment_issue` alone accounts for `20.27%` of utterances (`4,366`), and `4.86%` (`1,047`) contain offensive/frustrated phrasing (`W`). Safe escalation with full conversation summaries is mandatory.

---

## 3. Candidate Automation Use Cases to Test (Ranked Hypotheses)

1. **Order Tracking & Courier Status (`track_order`):** Read-only API lookup triggered by order number/phone inside WhatsApp.
2. **Invoice Delivery & Billing History (`get_invoice`, `check_invoices`):** Automated PDF/ZATCA/e-invoice retrieval inside the 24h free service window.
3. **Payment Failure Triage & Handoff (`payment_issue`):** Structured capture of error/transaction ID + immediate escalation to finance/support agent.
4. **Bilingual Policy & Delivery FAQ RAG (`check_refund_policy`, `delivery_options`):** Grounded answers in Arabic/English with source-citation guardrails.
5. **Pre-Fulfillment Order & Address Edits (`change_order`, `change_shipping_address`):** Authenticated OTP confirmation before warehouse dispatch.
6. **Warm Human Escalation (`contact_human_agent`, `complaint`):** Sentiment-triggered handoff summarizing customer intent and prior chat turns.
