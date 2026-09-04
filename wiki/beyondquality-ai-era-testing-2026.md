# BeyondQuality: QA in the Age of AI-Accelerated Development

**Source:** https://beyondquality.org/research/ai-era-testing/ (Vitaly Sharovatov — developer advocate @ Qase + Liliia Abdulina, updated June 22, 2026, Discussion #28)
**Sponsors:** Qase, Regent AB, TestSolutions
**Tags:** #comprehension-debt #intent-debt #Boehm-curve #generative-ratification #BeyondQuality
**Raw:** [beyondquality-ai-era-testing-2026.md](../raw/beyondquality-ai-era-testing-2026.md)
**SlopCodeBench companion:** [SlopCodeBench 2026](slopcodebench-2026.md) — 36 programs, 196 checkpoints, 0/15 agents end-to-end

---

## What It Is

Hub research diagnosing why "testing-after" (already doomed pre-AI under scale, kept alive by human domain understanding accumulated via collaboration) collapses when agents enter. Produces volume at machine speed; existing appraisal loops don't scale. Proposes **two debts** and reshaped Boehm curve, then 4 conditions for any Direction 3 solution (AI-enabled collaborative building as testable hypothesis, not settled answer).

Reading order: `analysis.md` (hub) → `analysis-pre-ai.md` (pre-AI ceilings) → `analysis-agents.md` (two debts, Boehm) → `analysis-lifecycle.md` (generative ratification loop) → `analysis-research-question.md` (asymmetry, 4 conditions) → `proposal.md` (collaborative building) → `evaluation.md` (Direction 1/2: Claude Code Review, JiTTests ceilings) → `references.md`.

## The Two Debts (analysis-agents.md)

When AI writes code, humans stop accumulating **comprehension** (how system works) and **intent** (why it exists / why built this way). Two debts accumulate invisibly; ability to change system degrades even though rewriting single function is cheap.

- **Comprehension inversion:** before, implementer understood best. Now agent (implementer) has no persistent understanding. Code exists, nobody has deep understanding author had. Syntactically fluent, subtly wrong. Each session roughly fresh; shared understanding doesn't accumulate.
- **Novel failure modes:** AI bugs not off-by-one but plausible-looking, subtly wrong logic — existing heuristics miss.
- **Testing stress:** verdict overwhelmed (more code, same humans), learning broken (testing→implementation feedback severely degraded, same bug recurs), AI-generated tests bootstrap problem (code and tests share blind spots), human testers bring independent domain perspective AI lacks.

**Business domain understanding degraded (how + why):** agent lacks *consequence-grounded calibration, contextual exception recognition, project-specific accumulated knowledge* — has broad statistical pattern recognition from training, lacks lived consequence. Human who fixed payment incident carries it; agent starts fresh.

Empirical support:
- **Bastani et al. 2025, PNAS:** students with GPT-4 performed 17% worse once access removed vs never had access.
- **Shen & Tamkin 2026, Anthropic:** engineers delegating generation scored 50% comprehension vs 67% manual; those using AI for conceptual questions maintained comprehension.
- **METR 2025 (Becker et al.):** experienced devs with AI took 19% longer on own repos while believing 20% faster — perception gap = invisible debt.

Intent debt: eroding business rationale, design decisions, consciously accepted tradeoffs — manifests not when things break but when decisions needed (should we build this feature?).

## Boehm's Curve Reshaped

Pre-AI: fixing defect grows exponentially across requirements→design→code→testing→production (rework volume). AI era: writing/rewriting cheap, **finding what to rewrite very expensive** (comprehension gap).

| Activity | Pre-AI | AI Era |
|----------|--------|--------|
| Writing code | Expensive (human) | **Cheap** (agent) |
| Understanding code | Free (author understands) | **Expensive** (nobody deeply understands) |
| Rewriting code | Expensive | **Cheap** |
| Finding what to rewrite | Moderate (trace via understanding) | **Very expensive** |
| Production failure | Expensive | **Unchanged** (churn, outage, fines) |

Wrong ideas amplified at machine speed → volumes of wrong code. Diagnosis cost up even though rewrite down. **Prevention (idea/spec) becomes more critical** — Cost of Quality: prevention cheaper than appraisal cheaper than failure, gap widens.

Compensation mechanisms (external persistence: CLAUDE.md/memory/REVIEW.md; hosted fine-tuning; LoRA) persist snapshots, not self-correcting process; lack economic weighting, stale triggers, awareness of unwritten, operate at human speed vs machine-speed risk emergence.

## Two Types of Companies

- **Proactive QA:** prevention partially breaks (TDD works if human writes tests first, but spec problem returns; pair with agent ≠ thinking partner), but mindset is "embed quality" → will adapt (better prompts, architectural guardrails). Scaling O(n+εn²): effective n ↑ (code volume) + ε ↑ (coordination cost as agent code less comprehensible) → uncertain but plausibly manageable.
- **Reactive QC:** already struggling superlinear, now multiplicative: effective n ↑ dramatically, ε already large + grows, r(n) ↑ (rework introduces defects higher rate as less understanding). Superlinear costs accelerate via O((n+εn²)/(1-r(n))).

## Counter-Argument & SlopCodeBench Illustration

Counter: "Who needs to know code now, AI can do it all. We don't inspect ASM anymore, specs only, AI adapts forever, cost stays minimal."

**SlopCodeBench (Vitaly's experiment, exactly this mode):** 36 programs, 3-8 checkpoints each, each checkpoint agent gets human-written spec (far more precise than typical PRD) + its own code from previous checkpoint, must extend. Intent fully preserved, nobody carries comprehension — agent re-derives from code surface each time.

**Result across 15 frontier agents:** **0 solves single problem end-to-end**, best strict solve **14.8% checkpoints** (isolated 28.1% GPT 5.5/Codex). Cost per checkpoint **>×2**, share changed **97%→30%** (spends more to change less). **Erosion and verbosity grow in 75% trajectories, 5-7× faster than 473 human repos.** Perfect illustration.

This validates two-debts thesis: specs alone insufficient, even when precise.

## Why It Matters for AI-QA

| Debt | QA Gate |
|------|---------|
| Comprehension (how) | Human must retain ability to answer what code does — mutation, review, risk-based gate preserve it |
| Intent (why) | Record rationale/tradeoffs as artifact, not head — RACI + PR block (Julia Pottinger) |
| Boehm reshaped | Shift investment to prevention (spec quality, contract) not late appraisal |

## Critical Analysis

**Strengths:**
- Qualitative diagnosis with quantitative illustration (SlopCodeBench + Bastani/Shen/METR) — not just opinion.
- Names structural ceilings for Direction 1/2 (appraisal tools) vs Direction 3 candidate needing validation.

**Gaps:**
- Hypothesis still needs empirical validation (proposal §5 open) — not prescription.

## Cross-links

- **SlopCodeBench:** [slopcodebench-2026.md](slopcodebench-2026.md) — 36 programs, 196 checkpoints, erosion 5-7×
- Related: [Zalando agentic snapshot](zalando-agentic-engineering-snapshot-2026.md) (risk-based gate as prevention)
- Related: [Keith Klain testing mindset](keith-klain-testing-mindset-after-all-2026.md) (evaluator independence vs comprehension)
- Related: [Julia Pottinger who-validates](julia-pottinger-who-validates-ai-generated-code-2026.md) (RACI + sign-off as comprehension preservation)

---

*Ingested: 2026-09-03 · Via beyondquality.org 8-page hub + analysis-agents.md + Vitaly LinkedIn post 11m (11m ago, #BeyondQuality)*
