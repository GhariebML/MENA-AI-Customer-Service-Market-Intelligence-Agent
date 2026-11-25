#!/usr/bin/env python3
"""Profile the Kaggle Bitext customer-support CSV and export analytical tables.

Usage:
  python dataset_profiler.py ../03_DATASET/raw/20000-Utterances-Training-dataset-for-chatbots-virtual-assistant-Bitext-sample.csv --out-dir ../03_DATASET/processed

Computes all statistics directly from the input CSV without external network calls
or fabricated estimates.
"""
from __future__ import annotations

import argparse
import csv
import datetime
import json
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, List

EXPECTED_FIELDS = ["flags", "utterance", "category", "intent"]

FLAG_DESCRIPTIONS = {
    "B": "Basic syntactic structure",
    "S": "Syntactic structure variation",
    "L": "Lexical variation (synonyms)",
    "M": "Morphological variation (plurals, tenses)",
    "I": "Interrogative structure",
    "C": "Complex/Coordinated syntactic structure",
    "P": "Politeness variation",
    "Q": "Colloquial variation",
    "W": "Offensive language",
    "E": "Expanded abbreviations",
    "D": "Indirect speech",
    "Z": "Noise (spelling, punctuation, run-on words)",
}

AUTOMATION_TIER_MAP = {
    # Tier 1: Knowledge-Base / Policy RAG
    "check_refund_policy": ("Tier 1 - Knowledge-Base RAG", "Policy retrieval from verified bilingual KB; zero write access", "No (unless policy exception)"),
    "check_cancellation_fee": ("Tier 1 - Knowledge-Base RAG", "Fee rules and contract tier lookup via KB/plan rules", "No (unless fee waiver requested)"),
    "check_payment_methods": ("Tier 1 - Knowledge-Base RAG", "Supported payment rail & country availability FAQ", "No"),
    "delivery_options": ("Tier 1 - Knowledge-Base RAG", "Shipping tiers, COD availability, SLA zones via KB", "No"),
    "delivery_period": ("Tier 1 - Knowledge-Base RAG", "Estimated delivery SLA lookup by city/country", "No"),
    "registration_problems": ("Tier 1 - Knowledge-Base RAG", "Guided troubleshooting + OTP/account verification flow", "Conditional (if blocked)"),
    # Tier 2: Read-Only API / Transactional Lookup
    "track_order": ("Tier 2 - API Status Lookup", "Authenticated order/shipment API lookup (order ID + phone)", "Conditional (if delayed/lost)"),
    "track_refund": ("Tier 2 - API Status Lookup", "Refund ledger/gateway status check via CRM/ERP API", "Conditional (if SLA breached)"),
    "get_invoice": ("Tier 2 - API Status Lookup", "Fetch and deliver PDF/e-invoice via WhatsApp or email", "No"),
    "check_invoices": ("Tier 2 - API Status Lookup", "Billing history retrieval from invoicing API", "Conditional (disputed charge)"),
    "recover_password": ("Tier 2 - API Status Lookup", "Automated OTP / password-reset trigger", "Conditional (locked account)"),
    # Tier 3: Authenticated Transactional Action
    "create_account": ("Tier 3 - Authenticated Action", "Guided onboarding workflow + validation + consent capture", "No"),
    "edit_account": ("Tier 3 - Authenticated Action", "Authenticated profile update via API", "No"),
    "switch_account": ("Tier 3 - Authenticated Action", "Plan/account switch workflow with confirmation", "Conditional (downgrade/retention)"),
    "change_order": ("Tier 3 - Authenticated Action", "Order modification before fulfillment cutoff via OMS API", "Conditional (already shipped)"),
    "place_order": ("Tier 3 - Authenticated Action", "Conversational catalog + cart + checkout confirmation", "No"),
    "change_shipping_address": ("Tier 3 - Authenticated Action", "Address update via OMS/courier API prior to dispatch", "Conditional (in transit)"),
    "set_up_shipping_address": ("Tier 3 - Authenticated Action", "Structured address capture + geocoding validation", "No"),
    "newsletter_subscription": ("Tier 3 - Authenticated Action", "Opt-in / opt-out preference update with PDPL consent log", "No"),
    "review": ("Tier 3 - Authenticated Action", "CSAT / review capture and sentiment tagging", "Conditional (negative score)"),
    # Tier 4: Mandatory / High-Priority Human-in-the-Loop Escalation
    "payment_issue": ("Tier 4 - Human-in-the-Loop Priority", "Triage payment gateway error, collect transaction ID, escalate failed/double charges", "Yes (financial risk)"),
    "contact_customer_service": ("Tier 4 - Human-in-the-Loop Priority", "Intent clarification, pre-collect context, route to right queue", "Yes (explicit request)"),
    "contact_human_agent": ("Tier 4 - Human-in-the-Loop Priority", "Immediate warm handoff with conversation summary to live agent", "Yes (mandatory)"),
    "get_refund": ("Tier 4 - Human-in-the-Loop Priority", "Verify eligibility, check order status, escalate or trigger bounded auto-refund", "Yes (financial approval)"),
    "delete_account": ("Tier 4 - Human-in-the-Loop Priority", "PDPL deletion request workflow, identity check, retention log", "Yes (compliance/retention)"),
    "complaint": ("Tier 4 - Human-in-the-Loop Priority", "Empathetic acknowledgement, structured case creation, urgent supervisor routing", "Yes (reputation/escalation)"),
    "cancel_order": ("Tier 4 - Human-in-the-Loop Priority", "Cancellation eligibility check, retention option, OMS cancel or handoff", "Yes (order state/fees)"),
}


def clean_header(value: str) -> str:
    return value.strip().lower().replace("\ufeff", "")


def write_counter_csv(path: Path, label: str, counter: Counter, total: int) -> None:
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow([label, "count", "share_pct"])
        for item, count in counter.most_common():
            pct = (count / total * 100) if total else 0.0
            writer.writerow([item, count, round(pct, 4)])


def main() -> int:
    parser = argparse.ArgumentParser(description="Profile a Kaggle customer-support intent CSV")
    parser.add_argument("csv_file", help="Path to the downloaded Kaggle CSV")
    parser.add_argument("--out-dir", default="../03_DATASET/processed", help="Output directory")
    parser.add_argument("--analysis-csv", default=None, help="Optional path for consolidated intent analysis CSV")
    parser.add_argument("--encoding", default="utf-8-sig", help="CSV encoding (default: utf-8-sig)")
    args = parser.parse_args()

    source = Path(args.csv_file).expanduser().resolve()
    out_dir = Path(args.out_dir).expanduser().resolve()
    if not source.exists() or not source.is_file():
        print(f"ERROR: Input file not found: {source}", file=sys.stderr)
        return 2
    out_dir.mkdir(parents=True, exist_ok=True)

    row_count = 0
    missing_counts: Counter = Counter()
    category_counts: Counter = Counter()
    intent_counts: Counter = Counter()
    flags_counts: Counter = Counter()
    single_flag_counts: Counter = Counter()
    intent_to_category: Dict[str, str] = {}
    crosstab_counts: Dict[str, Counter] = defaultdict(Counter)
    intent_char_lens: Dict[str, List[int]] = defaultdict(list)
    intent_word_lens: Dict[str, List[int]] = defaultdict(list)
    intent_flag_hits: Dict[str, Counter] = defaultdict(Counter)
    distinct: Dict[str, set] = {k: set() for k in EXPECTED_FIELDS}
    exact_row_signatures = set()
    duplicate_exact_rows = 0
    utterance_counts: Counter = Counter()
    all_char_lens: List[int] = []
    all_word_lens: List[int] = []
    headers: List[str] = []

    try:
        with source.open("r", newline="", encoding=args.encoding) as f:
            reader = csv.DictReader(f)
            if not reader.fieldnames:
                print("ERROR: CSV header row is missing or unreadable.", file=sys.stderr)
                return 3
            original_headers = reader.fieldnames
            headers = [clean_header(h or "") for h in original_headers]
            original_to_clean = dict(zip(original_headers, headers))
            for raw in reader:
                row_count += 1
                row = {original_to_clean[k]: (v or "").strip() for k, v in raw.items() if k in original_to_clean}
                signature = tuple(row.get(h, "") for h in headers)
                if signature in exact_row_signatures:
                    duplicate_exact_rows += 1
                else:
                    exact_row_signatures.add(signature)
                for field in headers:
                    if not row.get(field, "").strip():
                        missing_counts[field] += 1
                for key in EXPECTED_FIELDS:
                    if key in row and row[key]:
                        distinct[key].add(row[key])

                cat = row.get("category", "")
                intent = row.get("intent", "")
                fl = row.get("flags", "")
                utt = row.get("utterance", "")

                if cat:
                    category_counts[cat] += 1
                if intent:
                    intent_counts[intent] += 1
                    if cat:
                        intent_to_category[intent] = cat
                        crosstab_counts[cat][intent] += 1
                if fl:
                    flags_counts[fl] += 1
                    for ch in fl:
                        single_flag_counts[ch] += 1
                        if intent:
                            intent_flag_hits[intent][ch] += 1
                if utt:
                    utterance_counts[utt] += 1
                    clen = len(utt)
                    wlen = len(utt.split())
                    all_char_lens.append(clen)
                    all_word_lens.append(wlen)
                    if intent:
                        intent_char_lens[intent].append(clen)
                        intent_word_lens[intent].append(wlen)

    except UnicodeDecodeError as exc:
        print(f"ERROR: Could not decode CSV using {args.encoding}: {exc}", file=sys.stderr)
        return 4
    except csv.Error as exc:
        print(f"ERROR: CSV parsing failed: {exc}", file=sys.stderr)
        return 5

    if row_count == 0:
        print("ERROR: CSV contains a header but no data rows.", file=sys.stderr)
        return 6

    max_intent = intent_counts.most_common(1)[0]
    min_intent = intent_counts.most_common()[-1]
    imbalance_ratio = round(max_intent[1] / min_intent[1], 2) if min_intent[1] else None

    profile = {
        "source_file_name": source.name,
        "profiled_at_local_date": datetime.date.today().isoformat(),
        "row_count": row_count,
        "column_count": len(headers),
        "columns": headers,
        "expected_fields_present": {field: field in headers for field in EXPECTED_FIELDS},
        "missing_values_by_column": {col: missing_counts.get(col, 0) for col in headers},
        "exact_duplicate_rows": duplicate_exact_rows,
        "duplicate_utterance_values_beyond_first": sum(n - 1 for n in utterance_counts.values() if n > 1),
        "unique_counts": {field: len(distinct[field]) for field in EXPECTED_FIELDS if field in headers},
        "class_imbalance": {
            "top_intent": {"intent": max_intent[0], "count": max_intent[1], "share_pct": round(max_intent[1] / row_count * 100, 4)},
            "bottom_intent": {"intent": min_intent[0], "count": min_intent[1], "share_pct": round(min_intent[1] / row_count * 100, 4)},
            "max_to_min_intent_ratio": imbalance_ratio,
        },
        "utterance_length_summary": {
            "char_min": min(all_char_lens),
            "char_median": round(statistics.median(all_char_lens), 2),
            "char_mean": round(statistics.mean(all_char_lens), 2),
            "char_max": max(all_char_lens),
            "word_min": min(all_word_lens),
            "word_median": round(statistics.median(all_word_lens), 2),
            "word_mean": round(statistics.mean(all_word_lens), 2),
            "word_max": max(all_word_lens),
        },
        "category_counts": dict(category_counts.most_common()),
        "intent_counts": dict(intent_counts.most_common()),
        "single_flag_counts": dict(single_flag_counts.most_common()),
        "top_15_flag_combinations": dict(flags_counts.most_common(15)),
        "notes": [
            "Counts in this file are computed strictly from the downloaded Kaggle CSV.",
            "This dataset is English-only and is not a representative sample of Egypt, Saudi Arabia, or UAE customer demand.",
            "No raw user utterance text is copied into summary JSON/MD outputs.",
        ],
    }

    (out_dir / "dataset_profile.json").write_text(json.dumps(profile, indent=2, ensure_ascii=False), encoding="utf-8")
    write_counter_csv(out_dir / "category_counts.csv", "category", category_counts, row_count)
    write_counter_csv(out_dir / "intent_counts.csv", "intent", intent_counts, row_count)
    write_counter_csv(out_dir / "flags_counts.csv", "flags", flags_counts, row_count)

    # Single linguistic flag breakdown
    with (out_dir / "linguistic_flag_breakdown.csv").open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["flag_code", "description", "row_occurrences", "share_of_rows_pct"])
        for ch, cnt in single_flag_counts.most_common():
            writer.writerow([ch, FLAG_DESCRIPTIONS.get(ch, "Other"), cnt, round(cnt / row_count * 100, 4)])

    # Intent vs Category crosstab (long format + mapping)
    with (out_dir / "intent_category_crosstab.csv").open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["category", "intent", "count", "share_of_dataset_pct", "share_within_category_pct"])
        for cat, cat_cnt in category_counts.most_common():
            for intent, cnt in crosstab_counts[cat].most_common():
                writer.writerow([
                    cat,
                    intent,
                    cnt,
                    round(cnt / row_count * 100, 4),
                    round(cnt / cat_cnt * 100, 4),
                ])

    # Text length statistics by category & overall
    with (out_dir / "text_length_statistics.csv").open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["intent", "category", "count", "mean_chars", "median_chars", "min_chars", "max_chars", "mean_words", "median_words", "min_words", "max_words"])
        for intent, cnt in intent_counts.most_common():
            cl = intent_char_lens[intent]
            wl = intent_word_lens[intent]
            writer.writerow([
                intent,
                intent_to_category.get(intent, ""),
                cnt,
                round(statistics.mean(cl), 2),
                round(statistics.median(cl), 2),
                min(cl),
                max(cl),
                round(statistics.mean(wl), 2),
                round(statistics.median(wl), 2),
                min(wl),
                max(wl),
            ])

    # Automation suitability mapping & consolidated analysis_results.csv
    mapping_rows = []
    tier_totals = Counter()
    for intent, cnt in intent_counts.most_common():
        cat = intent_to_category.get(intent, "")
        tier, workflow, hitl = AUTOMATION_TIER_MAP.get(intent, ("Unclassified", "Review manually", "Yes"))
        tier_totals[tier] += cnt
        cl = intent_char_lens[intent]
        wl = intent_word_lens[intent]
        fl_hits = intent_flag_hits[intent]
        mapping_rows.append([
            intent,
            cat,
            cnt,
            round(cnt / row_count * 100, 4),
            tier,
            workflow,
            hitl,
            round(statistics.mean(wl), 2),
            round(statistics.mean(cl), 2),
            round(fl_hits["Q"] / cnt * 100, 2),
            round(fl_hits["P"] / cnt * 100, 2),
            round(fl_hits["Z"] / cnt * 100, 2),
            round(fl_hits["W"] / cnt * 100, 2),
        ])

    headers_map = [
        "intent", "category", "count", "share_pct", "automation_tier",
        "recommended_ai_workflow", "human_escalation_required",
        "mean_words", "mean_chars", "colloquial_Q_pct", "polite_P_pct",
        "noise_typo_Z_pct", "offensive_W_pct"
    ]
    for target_path in [out_dir / "automation_suitability_mapping.csv"] + ([Path(args.analysis_csv).resolve()] if args.analysis_csv else []):
        target_path.parent.mkdir(parents=True, exist_ok=True)
        with target_path.open("w", newline="", encoding="utf-8-sig") as f:
            writer = csv.writer(f)
            writer.writerow(headers_map)
            writer.writerows(mapping_rows)

    lines = [
        "# Bitext Dataset Profile (Computed Actuals)",
        "",
        f"**Source file:** `{source.name}`",
        f"**Profiled date:** {datetime.date.today().isoformat()}",
        f"**Rows:** {row_count:,}",
        f"**Columns:** {len(headers)} ({', '.join(headers)})",
        f"**Missing values:** {sum(missing_counts.values()):,}",
        f"**Exact duplicate rows:** {duplicate_exact_rows:,}",
        f"**Duplicate utterance strings beyond first occurrence:** {profile['duplicate_utterance_values_beyond_first']:,}",
        f"**Class imbalance (top vs. bottom intent):** {max_intent[0]} ({max_intent[1]:,}) vs. {min_intent[0]} ({min_intent[1]:,}) = {imbalance_ratio}x",
        f"**Utterance length (words):** mean {profile['utterance_length_summary']['word_mean']}, median {profile['utterance_length_summary']['word_median']}, range {profile['utterance_length_summary']['word_min']}–{profile['utterance_length_summary']['word_max']}",
        f"**Utterance length (chars):** mean {profile['utterance_length_summary']['char_mean']}, median {profile['utterance_length_summary']['char_median']}, range {profile['utterance_length_summary']['char_min']}–{profile['utterance_length_summary']['char_max']}",
        "",
        "## Schema",
        "",
        "| Column | Present | Missing values | Unique values |",
        "|---|---:|---:|---:|",
    ]
    for col in headers:
        uniq = len(distinct[col]) if col in distinct else "N/A"
        lines.append(f"| `{col}` | Yes | {missing_counts.get(col, 0):,} | {uniq:,} |")

    lines += ["", "## Category distribution (11 categories)", "", "| Category | Count | Share |", "|---|---:|---:|"]
    for item, count in category_counts.most_common():
        lines.append(f"| {item} | {count:,} | {count / row_count * 100:.2f}% |")

    lines += ["", "## Intent distribution (27 intents)", "", "| Intent | Category | Count | Share | Automation Tier |", "|---|---|---:|---:|---|"]
    for item, count in intent_counts.most_common():
        tier = AUTOMATION_TIER_MAP.get(item, ("Unclassified",))[0]
        lines.append(f"| {item} | {intent_to_category.get(item, '')} | {count:,} | {count / row_count * 100:.2f}% | {tier} |")

    lines += ["", "## Automation Tier Rollup", "", "| Automation Tier | Utterance Count | Share of Dataset |", "|---|---:|---:|"]
    for tier, cnt in tier_totals.most_common():
        lines.append(f"| {tier} | {cnt:,} | {cnt / row_count * 100:.2f}% |")

    lines += [
        "",
        "## Analytical Guardrails",
        "",
        "- Every count and percentage above is computed strictly from the downloaded CSV.",
        "- The dataset is English-only synthetic/curated training data and cannot establish MENA market size, SME demand, or willingness to pay.",
        "- Use these intent patterns as discovery hypotheses to validate against local SME Arabic/English support logs.",
        "",
    ]
    (out_dir / "dataset_profile.md").write_text("\n".join(lines), encoding="utf-8")

    print(f"Profile complete: {out_dir}")
    print(f"Rows: {row_count:,} | Categories: {len(category_counts)} | Intents: {len(intent_counts)} | Exact dups: {duplicate_exact_rows}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
