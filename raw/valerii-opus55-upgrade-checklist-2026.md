# Valerii K. (ODDITY): Opus 5.5 Upgrade Validation Checklist (2026-09-25)

**Author:** Valerii K. (Director QA at ODDITY; Quality Engineering & AI in QA; scaling without headcount). Post pasted by user 2026-09-25 (~2d old).
**Source:** user-pasted post substance. Model numbers are Anthropic-reported (Terminal-Bench 4.0): Opus 5.5 66.4%, GPT-6 Astra 57.9%, Opus 5 52.3% — vendor numbers, directional. Effort-settings caveat is the author's (verified logic, widely true).
**Context:** Model-upgrade validation protocol: never accept leaderboard, test on YOUR workloads. Checklist: task completion, tool calls + fallback behavior, cost per successful task, latency + token usage, evidence quality + human review. Migration notes: adaptive thinking, forced tool use, conversation state, computer use. Claim: typical workloads 40% cheaper than Opus 5 (unvalidated).
**Captured:** 2026-09-25 from user paste.

---

## Use for us

- Upgrade-validation checklist (5 rows) = reusable protocol for our own model swaps (qwen2.5→qwen3→gemma deltas!) and for Phase B validity framing (same-workload comparison).
- "Models not tested at identical effort settings" = effort-parity rule for benchmarks (pairs with our temperature/prompt freeze doctrine).
- Cost-per-SUCCESSFUL-task (not per token) = the right denominator for tier-model economics.
- Radar, not endorsement (author's own framing) — quote with that caveat.
