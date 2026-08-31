# Continuous Prompt Evaluation: LLM Judges and Live Signals

**Source:** https://kiro.dev/blog/continuous-prompt-evaluation/
**Date:** August 21, 2026
**Authors:** Myeongsoo Kim, Patrick Chapman, Sai Srinivas Somarouthu, Jay Agrawal, Murali Krishna Ramanathan (Applied Science)
**Tags:** #kiro #llm-judge #evaluation #prompt-engineering #ab-testing
**Raw:** [kiro-continuous-prompt-evaluation-2026.md](../raw/kiro-continuous-prompt-evaluation-2026.md)

---

## What It Is

Kiro's 4-stage methodology for evaluating human-authored system prompt changes using live internal traffic plus an LLM-as-judge. Benchmarks alone miss real-work context (codebase, tools, resumed sessions). Kiro pairs benchmark deltas with behavioral analysis of thousands of internal developer conversations.

Cycle: **Diagnose → Design → Test (cohorts) → Evaluate**. Re-runs on every model upgrade.

## The Four Stages

1. **Diagnose** — Run judge on internal traffic, cluster high-frequency complaints (e.g., "incomplete task"), trace to prompt instruction (e.g., "explain plan vs execute").
2. **Design** — Draft targeted candidate fixes per cluster (safety, verification, tone, behavior), state intended behavior and regression risk.
3. **Test** — Compare control vs isolated candidate cohorts plus a combined cohort (reveals interactions). Deterministic hash bucketing. Small cohorts = directional signal, not production estimate.
4. **Evaluate** — Same judge rubric on all cohorts: explicit dissatisfaction + behavioral quality issues. Ship / revise / reject.

In one deployment: 27 candidates across 4 categories screened via isolated + combined cohorts; degraded candidates revised or removed.

## LLM-as-Judge (15 Behavioral Dimensions)

- Task completeness, claim accuracy (verified before asserting?), code style adherence, repeated unsuccessful approaches, destructive-action flagging, tool use appropriateness, verification behavior (tests, compilation)
- Requires explicit evidence: corrections, complaints, abandoned tasks. Ambiguous conversations excluded (conservative, low false positives).
- Two primary signals:
  - **Explicit dissatisfaction** — user expressed frustration, abandoned conversation, redid agent's work
  - **Behavioral quality issues** — missed one of 15 standards (claims without reading code, incomplete tasks, ignoring project patterns)

## Experiment Infrastructure

- Stable bucketing by user identity hash; same rubric across cohorts; judge scores conversation outcomes.
- Also used to evaluate config choices (e.g., reasoning effort levels — higher effort improved code modification/debugging).
- Caveats: assignment controls prompt-experiment selection but not all live-traffic bias; sample size determines conclusion strength.

## Results (Internal Comparisons — Not Universal Production Estimates)

**Initial experiments (first model-and-prompt config):**
- **Kiro CLI:** dissatisfaction -5%, behavioral issues -32%, task completeness issues -10.6%
- **Kiro IDE:** behavioral -20%, incomplete task -21%, repeated unsuccessful approaches -36%, style mismatches -54%

**Re-validation on newer model (harder baseline, less headroom):**
- Behavioral -4% further, dissatisfaction -2.6 pp — directional confirmation fixes still help.
- Newer model followed instructions more literally; guidance tuned for prior model didn't transfer cleanly → treat each model upgrade as new config: replay complaint cases, regression checks, retune before rollout.

## Why Prompt Effects Are Model-Dependent

Same prompt changes: -32% behavioral on one model version vs -4% on another. Newer models more literal at low effort levels. Implication: prompts and models must be validated together.

## Takeaways for Teams

- **Live usage complements benchmarks** — real sessions expose context benchmarks miss.
- **Isolated cohorts localize regressions; combined + powered cohorts decide.**
- **Retire stale guidance** — largest gains from removing outdated constraints (line limits, deprecated tool workarounds). Simpler prompts align better.
- **Repeat cycle as prompts/models/usage evolve.**

## Relevance to QA/QE

| Pattern | QA Application |
|---------|----------------|
| LLM-as-judge with evidence requirement | Apply same rubric to agent-generated tests: explicit failure evidence, not implied |
| 15-dimension behavioral rubric | Extend to code-review agents: verification before claiming fix, style adherence |
| Isolated vs combined cohorts | Mutation testing: isolated mutations localize, combined validates interaction |
| Re-validation on model upgrade | Every model swap = new validation pass; reuse prior complaint cases as regression suite |
| Retire outdated constraints | Steering files accumulate debt — prune regularly |

## Critical Analysis

**Strengths:**
- Evidence-based (explicit feedback only), conservative.
- Real-work signal beyond synthetic benchmarks.
- Formal A/B with interaction detection (combined cohort).

**Gaps:**
- Internal-only, not external user distribution; bucketing doesn't eliminate all bias.
- Small cohorts directional, risk of over-reading.
- 15 dimensions — rubric itself needs validation (judge quality).

## Cross-links

- Related: [Kiro diagnostics over time](kiro-diagnostics-over-time-agent-quality-2026.md) — diagnostics vs judge signals
- Related: [Trust agent triage](kiro-trust-agent-triage-2026.md) — same Kiro CLI harness, skills + MCP
- QA evidence layer: [ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md](ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md)

---

*Ingested: 2026-08-30*
