# How to Test Non-Deterministic AI Outputs

**Source:** https://getautonoma.com/blog/how-to-test-non-deterministic-ai-outputs
**Date:** 2026-07-27
**Tags:** #autonoma #non-deterministic #llm-testing #flaky-tests
**Raw:** [autonoma-non-deterministic-ai-outputs-2026.md](../raw/autonoma-non-deterministic-ai-outputs-2026.md)

---

## What It Is (3-5 bullets)

- **Shift from equality to invariants**: assert what must be TRUE about output (structure, entities, forbidden content) and measure pass rate across N runs, not single-run string equality. Flaky AI test = assertion too strict OR prompt too ambiguous — almost never a third thing (Tom Piaggio, Autonoma, 2026-07-27).
- **Four runnable patterns** in repo `Autonoma-Tools/how-to-test-non-deterministic-ai-outputs`: `test_invariants.py` (property assertions), `lib/semantic_similarity.py` (calibrated cosine), `lib/sampling.py` (N-run majority + mean-similarity), `lib/threshold_gate.py` (suite-level floor with CI exit code).
- **Why variance exists even at temperature=0**: sampling temperature/top-p, context and retrieval drift (RAG/tool/history), prompt phrasing edits, silent provider model updates behind same alias, plus hardware-level batching, floating-point non-associativity, GPU kernels, and MoE routing — `temperature=0` reduces but does not eliminate variance.
- **Suite-level gating plus build order**: start with cheapest invariants, add semantic checks once references exist, wrap flaky scenarios in N-run sampling, then roll per-scenario rates into a threshold gate set from a measured baseline on a trusted version, not a round number.

## Key Patterns / Techniques (table or bullets)

| Pattern | What it does (from raw) | File in repo |
|---------|-------------------------|--------------|
| **Invariant / property assertions** | Cheapest first: non-empty, length bound, required entities (order ID, status), forbidden content (leaked prompt, unqualified promise); no embeddings or judge needed; floor every acceptable answer must clear | `tests/test_invariants.py` — includes `temperature=0` multi-draw check |
| **Semantic similarity vs exact match** | Embed response + reference, cosine similarity vs threshold calibrated from hand-labeled same/different pairs; threshold is domain-specific (refund cutoff ≠ medical cutoff); catches paraphrase, not factual truth | `lib/semantic_similarity.py` — threshold calibration documented in code |
| **N-run sampling and self-consistency** | Run same input N times (5 default, catches ~1-in-5 failure without 20x cost), score each, report pass rate; two verdicts: majority vote (4/5 common) vs mean-similarity; spread 5/5→3/5 overnight = upstream change signal | `lib/sampling.py` — generalizes Wang et al. self-consistency |
| **Threshold gating at suite level** | Roll per-scenario pass rates into one suite gate; floor set a few points below measured noise floor on trusted version; 95% gate on 88% baseline = permanently red and ignored | `lib/threshold_gate.py` — returns process exit code for CI |
| **Practitioner rule: strict vs ambiguous** | Run same input 10-20 times, inspect spread: same meaning + different wording → assertion too strict (fix threshold/invariant); different meaning/structure → prompt ambiguous (add constraint, split prompt) | Diagnostic rule, no retry/quarantine |

> Retrying a non-deterministic AI failure hides signal; retrying a network timeout recovers false negative — opposite semantics. Autonoma's complementary layer verifies deterministic product outcome (ticket moved, refund changed, screen rendered) independent of wording variance.

## Relevance to QA/QE (table QA Action)

| QA Concern | Action |
|------------|--------|
| **Flaky AI suite on CI** | Replace exact-match with invariant + semantic checks; never `retry` a non-deterministic failure — run 10-20 spread instead and gate on rate |
| **Temperature=0 still flakes in prod** | Treat `temperature=0` as variance reduction, not determinism; budget for batching/GPU/MoE and silent provider updates in baseline measurement |
| **Threshold guessed at 0.8** | Empirically calibrate: embed labeled pairs, pick cutoff minimizing misclassification; re-calibrate per domain and per scorer change |
| **Wall of per-scenario pass rates** | Add suite-level gate with floor below trusted-version baseline; track spread over time, not single verdict — 5/5→3/5 drop is the early warning |
| **CI cost vs signal** | Default 5 runs per flaky scenario; raise only near majority line; clean 5/5 or 0/5 needs no bigger sample — saves token calls |
| **Prompt vs assertion triage** | Use 10-20-run spread to route fix: same meaning → loosen assertion or threshold; different meaning → tighten prompt format/constraints |

## Critical Analysis (Strengths/Gaps)

**Strengths:**
- Four patterns are ordered by cost and codified as runnable code, not prose — invariant first keeps most value without embeddings.
- Calibrated threshold guidance plus domain-transfer warning avoids the common 0.8-guess failure mode.
- Practitioner rule (strict vs ambiguous) gives a 10-20-run diagnostic that routes the fix to the right layer.
- Explicitly scopes semantic similarity ceiling (meaning-close ≠ factually correct) and hands off to LLM-as-judge and behavioral E2E where needed.

**Gaps:**
- No quantified trade-off for choosing N (5 vs 10 vs 20) across suite size and token budget; majority vs mean-similarity selection left heuristic.
- Provider-update detection assumes periodic re-baselining but gives no cadence or ownership for re-measuring the trusted baseline.
- Context/retrieval drift is named as variance source but not paired with a concrete RAG-snapshot or tool-result pinning pattern at assertion level.
- Embedding model choice and its own drift not addressed as a second non-determinism source in the similarity check.

## Worked Example (from raw)

- **Friday 4pm flake:** CI red → rerun green → ship → same test fails again; cause is exact-match against sampled output, not infra.
- **Invariant pass:** response contains order ID 4821, no leaked system prompt, under length bound — passes even when phrasing shifts.
- **Similarity decision:** three paraphrases of correct refund answer fail exact-match 2/3 times, pass semantic similarity 3/3 — demonstrates assertion shape matters.
- **N-run gate:** five runs 4-pass / 80% rate vs 75% floor = suite pass; same inputs next week 3/5 = signal of prompt or model change, not noise.
- **Triage:** outputs agree in meaning, differ in wording → loosen threshold; outputs disagree (confirm vs clarify vs wrong amount) → fix prompt.

## FAQ Highlights (from raw)

- Test by asserting what must be true + semantic similarity + N-run pass rate + suite threshold from measured baseline, not guessed number.
- Same question diverges due to temperature, context drift, prompt edits, provider updates, and even at T=0 via batching/GPU/MoE.
- Run flaky case 10-20 times; inspect spread to choose assertion fix vs prompt fix; do not quarantine.
- Five runs is pragmatic default (catches ~1-in-5 fail); raise only near majority line; 5/5 or 0/5 rarely needs larger sample.

## Reuse Checklist

- Copy `tests/test_invariants.py` as floor check per response type — required entities + forbidden patterns before any similarity spend.
- Build `lib/semantic_similarity.py` helper with calibration script: label ~50 pairs per domain, select cutoff minimizing misclassification.
- Wrap known-flaky scenarios with `lib/sampling.py` (5 runs, 4/5 majority default); emit `4/5 (80%)` to CI log, not just pass/fail.
- Store trusted-version baseline pass rate in repo; set `lib/threshold_gate.py` floor a few points below it; re-measure on intentional prompt/model change.
- Keep Autonoma-style behavioral assertion alongside: refund amount in DB matches amount in message, ticket status flipped — proves correctness beyond wording.

## Cross-links

- Prompt unit detail: [LLM Unit Testing](autonoma-llm-unit-testing-2026.md) — schema/string → similarity → judge ladder
- CI wiring: [LLM Evals in CI/CD](autonoma-llm-evals-cicd-2026.md) — N=5 averaging, tolerance band, eval dataset, nightly catch for provider drift
- Trajectory: [Testing Tool Calls](autonoma-testing-tool-calls-2026.md) — K-of-N for non-deterministic routing/arguments
- E2E arc: [How to Test an AI Agent E2E](autonoma-how-to-test-ai-agent-e2e-2026.md) — Stage 6 majority vote + semantic gate
- Reliability: [Agent Reliability](autonoma-agent-reliability-2026.md) — baseline diff extends non-determinism pattern to trajectories + canary
- Memory: [Agent Memory](autonoma-agent-memory-2026.md) — same N-run and semantic checks for carryover phrasing variance
- Feature gate: [QA a Generative AI Feature](autonoma-qa-ai-feature-2026.md) — N-run pass-rate foundation for eval set
- Evidence: [AI QA Evidence Layer](ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md) — pass rate = model eval, outcome = downstream validation
- External: [Batch invariance deep dive](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/) + [Self-consistency (Wang et al.)](https://arxiv.org/abs/2203.11171)
- Repo: [Autonoma-Tools/how-to-test-non-deterministic-ai-outputs](https://github.com/Autonoma-Tools/how-to-test-non-deterministic-ai-outputs)

## Reuse Notes

- Start behavioral check on one dollar-amount field: DB value equals message value — the invariant wording variance never hides.

---
*Ingested: 2026-08-31*
