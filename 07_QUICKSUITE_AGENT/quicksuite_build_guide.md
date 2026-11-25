# Step-by-Step Amazon QuickSuite Build Guide (Udacity AWS Lab)

Follow these exact steps inside your authenticated Udacity AWS QuickSuite session to complete the live cloud execution and capture the required screenshots.

---

## Step 1: Launch Udacity AWS QuickSuite Environment
1. Log into your Udacity classroom for **Course 3: Building No-Code AI Agents with Amazon Quick**.
2. Click **Cloud Resources** -> **Start Cloud Resources** -> **Open Cloud Console**.
3. Open the **QuickSuite / QuickSight Lab** portal tile.

## Step 2: Create and Populate the Project Space
1. Navigate to **Spaces** and click **Create Space**.
2. Name the Space: `MENA AI Customer Service – Market Intelligence 2026`.
3. Upload the following verified files from this submission folder:
   - `03_DATASET/raw/20000-Utterances-Training-dataset-for-chatbots-virtual-assistant-Bitext-sample.csv`
   - `03_DATASET/processed/dataset_profile.md`
   - `04_DATA_ANALYTICS/analysis_results.csv`
   - `06_QUICK_RESEARCH/actual_research_outputs/QR01_Market_Overview_Egypt_KSA_UAE.md` through `QR04_*.md`
4. **Capture Screenshot #1:** `01_space_overview.png` showing the created Space and uploaded source files.

## Step 3: Create & Configure the Market Intelligence Agent
1. Open **Agents** (or **Chat Agents**) -> **Create Agent**.
2. Enter exact Agent Name: `MENA Market Intelligence Agent – AI Customer Service Automation`.
3. Copy the full contents of `07_QUICKSUITE_AGENT/system_instructions.txt` into the **Instructions / Purpose** box.
4. Attach `20000-Utterances-Training-dataset-for-chatbots-virtual-assistant-Bitext-sample.csv` (and the research outputs) as the Agent's Knowledge Sources.
5. Save the Agent.
6. **Capture Screenshots #2 & #3:** `02_agent_overview.png` (name + instructions) and `03_dataset_attached.png` (attached Kaggle CSV knowledge source).

## Step 4: Execute Amazon Quick Research (QR-01 to QR-04)
1. Open **Quick Research** inside QuickSuite.
2. Run prompts `QR-01`, `QR-02`, `QR-03`, and `QR-04` from `06_QUICK_RESEARCH/research_prompts.md` one by one.
3. Save each completed native Quick Research report directly into your Space (`MENA AI Customer Service – Market Intelligence 2026`).
4. **Capture Screenshots #4 & #5:** `04_quick_research_prompts.png` and `05_quick_research_outputs.png` (showing visible URLs/citations).

## Step 5: Execute Quick Chat Analysis & Reliability Review (QC-01 to QC-06)
1. Open **Quick Chat** and select `MENA Market Intelligence Agent – AI Customer Service Automation`.
2. Run `QC-01` through `QC-06` from `07_QUICKSUITE_AGENT/quick_chat_prompts.md` in order.
3. Verify the Agent outputs `21,534` rows, `11` categories, and `27` intents for `QC-01`.
4. Save the generated Market Analysis, Reliability Evaluation, and Final Brief into your Space.
5. **Capture Screenshots #6, #7, #8, #9, #10:**
   - `06_agent_dataset_qa.png`
   - `07_market_analysis_output.png`
   - `08_reliability_evaluation_output.png`
   - `09_quicksuite_space_deliverables.png`
   - `10_final_brief_in_space.png`

## Step 6: Save Screenshots & Submit via Udacity
1. Save all genuine `.png` screenshots into `09_QUICKSUITE_EVIDENCE/screenshots/`.
2. Verify Space sharing permissions match Udacity mentor grading instructions.
3. Submit your Space link and `10_FINAL_SUBMISSION/FINAL_RESEARCH_BRIEF.pdf` (plus the complete submission pack if requested) in the Udacity portal.
