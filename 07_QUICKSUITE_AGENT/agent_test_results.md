# Agent Test Results — Offline Reference Benchmark vs. Pending Live AWS Execution

**Transparency Status:**  
- **Offline Reference Verification:** COMPLETE (25 November 2026) — Verified using the actual `21,534`-row Bitext dataset outputs (`dataset_profiler.py`) and the 22-source Evidence Register (`S1`–`S22`).
- **Live Amazon QuickSuite Portal Execution:** **PENDING AUTHENTICATED LEARNER SESSION** inside the Udacity AWS Lab. Once executed in QuickSuite, append observed live agent outputs and screenshot filenames below.

---

## Reference Output Summary for Key Validation Prompts

| Test ID | Verified Offline Ground-Truth Benchmark | Live QuickSuite Status |
|---|---|---|
| **T-01 (Dataset Profile)** | `21,534` rows, `4` columns (`flags`, `utterance`, `category`, `intent`), `0` missing values, `12` exact duplicate rows, `11` categories, `27` intents. Top category: `PAYMENT` (`4,636` / `21.53%`); top intent: `payment_issue` (`4,366` / `20.27%`). | Pending AWS Lab screenshot (`04_dataset_analysis.png`) |
| **T-02 (Representativeness Guardrail)** | Confirmed Bitext CSV contains zero country, channel, SME size, or currency columns and is 100% English (`en`). Cannot estimate Egyptian/GCC demand. | Pending live Quick Chat check |
| **T-03 (Automation Architecture)** | Tier 1 KB RAG = `8.08%` (`1,740`); Tier 2 API Lookup = `23.01%` (`4,956`); Tier 3 Auth Action = `21.11%` (`4,546`); Tier 4 Human Handoff = `47.79%` (`10,292`). | Pending live Quick Chat check |
| **T-04 (Pricing Normalization)** | At `5,000` chats/mo (5 seats, 60% resolution), illustrative unit costs span `$275` (Zendesk Suite Team seats), `$2,300` (Freshdesk Growth seats + 45 overage packs), `$2,970+` (Intercom Fin outcome fees excl. base seats), and `$10,000+` (Salesforce Agentforce convs excl. CRM seats). | Pending live Quick Chat check |
| **T-05 (Arabic & Dialect Gap)** | Zendesk [S7] and Intercom Fin [S10] list Arabic/MSA; regional players (Unifonic [S19], CEQUENS [S20], ZIWO AI [S21]) target MENA Arabic/voice; independent blind dialect benchmarks remain absent. | Pending live Quick Chat check |
| **T-06 to T-10 (Strategy, PDPL & Leadership Summary)** | Policy momentum exists (`S2, S3, S16, S18`), PDPL acts as Day-1 gate (`S12–S15`), TAM remains unverified, and NexaServe should pursue controlled discovery pilots rather than immediate commercial rollout. | Pending AWS Lab screenshots (`06_market_analysis.png`, `07_reliability.png`, `08_final_brief.png`) |
