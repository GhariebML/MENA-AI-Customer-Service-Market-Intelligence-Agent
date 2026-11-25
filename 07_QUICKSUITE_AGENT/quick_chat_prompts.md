# Quick Chat Prompt Library (QC-01 to QC-06)

Execute these prompts sequentially inside **Amazon Quick Chat** connected to `MENA Market Intelligence Agent – AI Customer Service Automation` and your attached dataset + Quick Research outputs.

---

## QC-01 — Internal Dataset Profiling & Integrity Verification
> Profile the attached Bitext Kaggle CSV (`20000-Utterances-Training-dataset-for-chatbots-virtual-assistant-Bitext-sample.csv`). Report exact row count, column count, data types, missing values, exact duplicates, distinct categories (`11`), distinct intents (`27`), and top 10 categories/intents with exact counts and percentages. Do not extrapolate or infer MENA regional prevalence from these counts.

## QC-02 — Automation Architecture & Human-in-the-Loop Mapping
> Using the verified Bitext profile, classify all 27 intents into four operational automation tiers: (1) Knowledge-Base RAG, (2) Read-Only API Status Lookup, (3) Authenticated Transactional Action, and (4) Mandatory Human-in-the-Loop Escalation. Report the utterance share per tier, analyze linguistic flags (`Q` colloquial, `Z` noise/typos, `W` offensive), and explain what tools/APIs each tier needs.

## QC-03 — Cross-Source Market & Competitor Synthesis
> Synthesize the Bitext dataset insights with our saved Quick Research streams (QR-01 to QR-04). Compare Egypt, Saudi Arabia, and the UAE separately across AI policy catalysts, SME digital signals, and PDPL privacy gates. Compare Zendesk, Freshdesk, Intercom Fin, Salesforce Agentforce, and regional MENA providers (Unifonic, CEQUENS, ZIWO AI) on pricing meters, Arabic/dialect documentation, and WhatsApp workflows.

## QC-04 — Red-Team Challenge & Uncertainty Audit
> Act as a skeptical investment committee reviewer. Challenge every draft market insight by identifying: strongest counter-evidence, dated figures (e.g., 2022–2023 SME counts), unverified dialect quality claims, incompatible pricing meters, missing SME willingness-to-pay data, and hidden assumptions. Downgrade confidence ratings wherever primary proof is absent.

## QC-05 — Reliability & Confidence Evaluation Matrix
> Generate a structured Reliability Evaluation table covering all 5 key insights: Insight Summary, Source Quality (High/Medium/Low), Evidence Strength, Cross-Source Consistency, Geographic Relevance, Timeliness, Overall Confidence, Key Limitation, and "What Would Change Our Mind?". Include at least two concrete risks and two explicit non-conclusions.

## QC-06 — Final Leadership-Ready Market Intelligence Brief
> Produce the final executive Market Intelligence Brief containing: Research Objective, Scope & Methodology, 3–5 Evidence-Backed Insights, Visual Evidence explanations, Reliability & Limitations, Strategic Implications & Prioritized Actions (including objective NexaServe evaluation), at least two Explicit Non-Conclusions, and a 5–7 sentence Summary for Leadership.
