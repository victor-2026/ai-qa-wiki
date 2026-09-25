# Nace AI Drex: Small Diffusion Decision Model, Decision Index #1 (2026-09-25)

**Vendor:** Nace AI (https://nace.ai/drex, playground https://drex.nace.ai free no-card). Solutions: financial/transactional audit, SME lending, pre-billing, AP automation, claims.
**Source:** vendor page fetched 2026-09-25 (Eduardo Ordax post pointed here; LinkedIn corpse text "Jev is dead" is hype, page substance below).
**Context:** Direct Jev competitor, different lineage (Small Diffusion Model + RLAF, <6B params — smallest top-10). Decision Index 0.2: Drex 51.73 vs Jev 1.13.0 51.67, wins 22/39 tests; tokens/decision 70 vs 367 (5x). Deploy: self-host (one accelerator), managed, hybrid; tuned on customer decisions (weights shipped). Same 3 question types (choice/yes-no/scale). Honest vendor bits: trained on official splits (stated), ALL losses published in table, axis starts at 44 (chart-truncation flagged openly-ish). Vendor claims, directional.
**Captured:** 2026-09-25 from webfetch.

---

## Key facts

- Architecture: small diffusion model + RLAF (reinforcement learning from attributed feedback? — expansion unverified, vendor term), <6B total params.
- Index: 40 chance-corrected decision tests (contracts, causes, tool calls, routing, judgment); Drex leads 50 entries; margins biggest on chord/sarcasm/causal/contract; trails on graduate science, broad knowledge, multi-step reasoning, MMLU-Pro (37.8 vs Jev 80.5!), GPQA, HLE 0.0.
- Notable splits: BANKING77 macro-F1 86.0 vs Jev 79.5; BFCL 89.2 vs 94.3 (Jev wins); RouterBench ~tie 52.8/52.7; RAGTruth hallucinated-class F1 72.3 vs 60.1; When2Call 88.1 vs 74.6; Home appliances 16.3 vs 52.5 (Jev wins big).
- Head-to-head board games 117-92 (256 matches, Kaggle Game Arena harness, OpenSpiel).
- Live playground: same case to both columns (recorded 2026-09-24); verdict distributions thresholdable, routable to humans.
- Pricing per post: $0.04/1M input, sub-second; 250M welcome credits (post-level, verify before citing).

## Use for us

- New lineage for W3 Jev-replacement landscape (diffusion vs transformer judges; <6B self-hostable; tuned-weights model = calibration-by-training precedent).
- Decision Index 0.2 as third-party benchmark scaffold (40 tests, chance-corrected, per-test table) — methodology reference for our own eval design; note what's missing (no latency distribution, no calibration/ECE column visible).
- BANKING77 86.0 adds a third datapoint to high-cardinality capability (Jev published ~0.87, Laya 0.425, Drex 0.860 macro-F1 — metric mismatch warning: macro-F1 vs accuracy, not directly comparable).
- "Distribution, not a verdict" (threshold + route uncertain to human) = our escalation-rule language in vendor words.
- Caveats: vendor page (losses shown = good sign, but selection of 40 tests is theirs); MMLU/GPQA craters show narrow specialization; pricing/credits post-level only.
