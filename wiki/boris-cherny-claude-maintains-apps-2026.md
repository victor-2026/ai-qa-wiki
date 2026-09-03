---
source: "boris-cherny-claude-maintains-apps-2026.md"
ingested: "2026-09-01"
---

## Boris Cherny - Claude Maintains Apps (Slack proj-claude-maintains-apps)

**Summary**
Creator and Head of Claude Code at Anthropic (Boris Cherny) describes experiment where Claude takes over day-to-day maintenance via Slack channel `proj-claude-maintains-apps`. Claude Tag runs daily routines across iOS, Android, Desktop, web, CLI, Agent SDK: crash fuzzer (tap to crash + fix), dup unifier (unify divergent abstractions), dead-code remover (static + logging check), abstraction police etc. Results: 388 PRs opened in few weeks, 180 merged after Claude Code Review + human review. Tuning via prompt iteration over days.

---

## Key Concepts

| Routine | What it does | QA relevance |
|---------|--------------|--------------|
| **Crash fuzzer** | Opens app in simulator, taps around to crash, root causes and fixes | Autonomous exploratory + fix loop - needs deterministic verifier |
| **Dup unifier** | Scans for similar yet divergent abstractions, PRs to unify | Refactor at scale - risk of semantic drift without state check |
| **Dead-code remover** | Removes statically unreachable, logs suspected dead code, removes next day | Two-phase verification - static + runtime signal |
| **Abstraction police** | Fixes leaky abstractions | Code health via agent - needs human tuning |

**Loop:** Claude opens PR -> Claude Code Review + human review -> merge -> tune routine via prompt if wrong -> better next day.

---

## Our analysis (for Victor)

1. **Daily maintenance is loop engineering at scale.** This is Andrew Ng's three loops in production: agentic coding loop (spec+eval -> code -> test -> iterate) + engineering loop (build/test every few minutes) + developer feedback loop (human steers via prompt tuning). Cherny shows the outer loop tuning cost: "sometimes it takes a few days of tuning."

2. **180/388 = 46% merge rate is the signal, not the failure.** Less than half merged after dual review - the filter is working. For Article 16 Productivity Paradox: generation is cheap (388), verification is the bottleneck (human + Claude review). Without that gate, 208 PRs of noise would land.

3. **Dead-code remover is the model for trustworthy automation.** Two-phase: static unreachable -> remove immediately; suspected dead -> add logging, remove next day only if no hit. This is the same as Victor's confirm/dismiss gate and "couldn't confirm" verdict - honest abstention beats false confidence.

4. **Fuzzer + deterministic verifier is the missing piece.** Cherny's fuzzer finds crashes by tapping - but does it verify state correctly or just that it didn't crash? The hard half (Radik's point) is the verdict. Needs external state check, not just "app didn't crash."

---

## Cross-links
- [Andrew Ng Loop Engineering](wiki/andrew-ng-loop-engineering-2026.md) — three loops, evals
- [Ishan Anand Persona Feedback](wiki/ishan-anand-llm-persona-feedback-failure-modes-2026.md) — sampling != significance, prompt sensitivity
- [Radik Zagirov - Rotting Gate](wiki/radik-zagirov-rotting-gate-2026.md) — verifier must be external, state verification
- [AI QA Evidence Layer](wiki/ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md) — passive layer, confirm/dismiss

---

*Source: Boris Cherny LinkedIn (2w) via https://lnkd.in/gqSqTtDF · Ingested 2026-09-01*
