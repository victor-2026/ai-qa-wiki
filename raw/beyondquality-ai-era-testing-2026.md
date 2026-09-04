# BeyondQuality Research: QA in the Age of AI-Accelerated Development

**Authors:** Lilia Abdulina, Vitaly Sharovatov (developer advocate @ Qase)
**Date:** Updated June 22, 2026 (Active research, Discussion https://github.com/BeyondQuality/beyondquality/discussions/28)
**Source:** https://beyondquality.org/research/ai-era-testing/
**Sponsors:** Qase, Regent AB, TestSolutions
**Reading order:** analysis.md (hub) → analysis-pre-ai.md → analysis-agents.md → analysis-lifecycle.md → analysis-research-question.md → proposal.md → evaluation.md → references.md

---

# QA in the Age of AI-Accelerated Development

## What this research does

Many companies hitting same wall: as teams adopt agentic AI for code generation, code output accelerates, and existing testing (manual + automated) cannot cope. Underlying problem (traditional "testing-after" straining under scale) not new; agents multiplied to point where previous coping mechanisms no longer work.

Research does two things:
1. Diagnoses what changed qualitatively: two debts (comprehension, intent), generative ratification loop, Boehm-curve reshape. Explains why current industry responses (Direction 1/2 appraisal tools) hit structural ceilings.
2. Formulates four conditions any solution must satisfy, and advances one candidate (AI-enabled collaborative building) as testable hypothesis. Not settled answer; needs empirical validation (proposal §5).

Status: Active research, open to critique, sponsored by Qase/Regent/TestSolutions.

## With Agents: How Process Works Now (analysis-agents.md)

Pre-AI baseline: "testing-after" already doomed under scale; business domain understanding accumulated implicitly through human collaboration kept process working.

With agents:
- Decision: spec now serves humans + agents; agent has no shared understanding, history, tacit knowledge. Spec simultaneously more critical and more insufficient.
- Implementation: Comprehension inversion — before implementer understood best, now implementer (agent) has no persistent understanding. Code exists but nobody has deep understanding the author had. Syntactically fluent but subtly wrong. Shared understanding doesn't accumulate — agent starts fresh each session.
- Testing: Verdict overwhelmed (more code, same humans), Learning broken (testing→implementation feedback degraded, same bug recurs indefinitely), AI-generated tests bootstrap problem (code and tests share blind spots), novel failure modes (plausible-looking but subtly wrong).
- Economics: Boehm's curve reshapes — writing/rewriting cheap, understanding expensive, finding what to rewrite very expensive, production failure costs unchanged. Cost driver shifts from rework volume to comprehension debt. Prevention (idea/spec) becomes more critical.

Empirical support: Bastani et al. 2025 PNAS: students with GPT-4 17% worse once removed; Shen & Tamkin 2026 Anthropic: engineers delegating generation 50% comprehension vs 67% manual; METR 2025: experienced devs with AI took 19% longer while believing 20% faster.

Two debts: comprehension debt (how) and intent debt (why). Intent: business rationale, design decisions, consciously accepted tradeoffs — eroding as decision-makers rotate/forget/leave.

## Two Types of Companies

Proactive QA (TDD, pair programming, shared understanding amplifiers) better positioned — mindset embed quality into process, will adapt to embed constraints into agent workflows. Reactive QC already struggling superlinear scaling O(n+εn²)/(1-r(n)) — all three terms move wrong simultaneously with agents, costs accelerate.

## SlopCodeBench Illustration (Vitaly post 2026-08, 11m)

Thesis: when AI writes code, humans stop accumulating comprehension and intent. Two debts accumulate, ability to change degrades even though rewriting single function cheap.

Counter-argument: who needs to know code now, AI can do it all. We don't write ASM anymore, specs only, AI adapts forever, cost minimal.

Experiment SlopCodeBench [2]: 36 programs, 3-8 checkpoints each, at each checkpoint agent gets human-written spec (far more precise than typical PRD) plus its own code from previous checkpoint and has to extend it. Intent fully preserved, nobody carries comprehension, agent re-derives from code surface each time, exactly "specs only, AI does the rest".

Across 15 frontier agents no agent solves SINGLE problem end to end, best strict solve rate 14.8% checkpoints. Cost per checkpoint more than doubles while share of code changed per step falls 97%→30% — spends more to change less. Erosion and verbosity grow in three quarters trajectories, 5-7× faster than in 473 human-maintained repositories. Perfect illustration.

Links:
1. BeyondQuality: https://beyondquality.org/research/ai-era-testing/
2. SlopBench: https://www.scbench.ai (docs https://github.com/SprocketLab/slop-code-bench/tree/main/docs, paper https://arxiv.org/abs/2603.24755, leaderboard https://www.scbench.ai/leaderboard — top GPT 5.5/Codex 28.1% isolated, erosion 0.494 etc.)

[Full research 8 pages — see wiki for structured summary; fetched 2026-09-03 via webfetch]

