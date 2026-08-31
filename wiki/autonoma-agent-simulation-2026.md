# What Is Agent Simulation Testing? A 3-Actor Harness

**Source:** https://getautonoma.com/blog/agent-simulation-testing
**Date:** 2026-07-22
**Tags:** #autonoma
**Raw:** [autonoma-agent-simulation-testing-2026.md](../raw/autonoma-agent-simulation-testing-2026.md)

---

## What It Is

- **Agent simulation testing = a synthetic LLM user (persona + goal) drives multi-turn conversation against the agent, then a separate LLM judge scores the full transcript against explicit pass/fail criteria** — Tom Piaggio (Autonoma, 2026-07-22). Multi-turn counterpart to a single-shot eval: instead of grading one reply, it validates the whole path including tool-failure recovery.
- **Three-actor harness** (vendor-neutral raw Python, `Autonoma-Tools/agent-simulation-testing`): `UserSimulatorAgent` (persona/goal, generates next user message, decides when goal done) + `AgentAdapter` (one interface `history → reply + tool calls`, wraps any framework: LangGraph/CrewAI/OpenAI) + `JudgeAgent` (rubric-graded transcript, not vague "helpful") + `SimulationRunner` (alternates turns to limit, hands full transcript to judge even on early exit) — `src/harness.py`.
- **Worked scenario**: order-cancellation for A1092 where `cancel_order` times out on first attempt and succeeds on retry; user simulator pushes back if agent gives up; judge criteria require: status changed to cancelled AND agent acknowledged failure before retry AND never repeated same failing action >2× without telling user — `src/order_cancellation_scenario.py`.
- **Portability claim**: LangWatch Scenario is the best public artifact of this pattern (`AgentAdapter` + `UserSimulatorAgent` + `JudgeAgent`, 6-turn failure-recovery example) but is SDK-locked; raw harness is the portable derivation with one provider seam (`LLMClient`) to swap.
- **Boundary made explicit**: transcript verdict proves conversation correctness; it does not prove the tool actually flipped state in the running app (DB, dashboard, inventory) — that gap is Autonoma's behavioral E2E (Planner + Executor on PreviewKit + Reviewer + Diffs Agent).

## Key Patterns / Techniques

| Pattern | Detail from raw |
|---------|-----------------|
| **UserSimulator as LLM persona** | Not a script; reasons about intent, can push back / get confused / rephrase — the behavior that breaks agents in production and never appears in scripted fixtures |
| **AgentAdapter seam** | Single interface hides framework; harness reusable across every agent without one test file per framework |
| **Judge rubric** | Explicit checkable criterion e.g., "PASS only if status→cancelled AND failure acknowledged before retry" — vague criteria ("helpful") give random verdicts; worth versioning as artifact |
| **SimulationRunner** | Alternates user/agent up to turn limit, stops early if simulator signals done, always judges full transcript (early give-up must fail rubric as loudly as wrong answer after 8 turns) |
| **Non-determinism handling** | Run N times (5 runs, 4/5 pass starting point); flaky = tighten persona/goal + judge criteria before loosening threshold — ambiguity, not randomness, is the usual cause |
| **Assertion matching** | Exact-match for hard facts (`A1092`, `cancelled`) + semantic similarity / judge for phrasing around them ("Your order has been cancelled" vs "I've cancelled A1092" both correct); `tests/test_non_determinism.py` shows both patterns |
| **Tool vs platform trade-off** | LangWatch (full harness, pytest-native, SDK-locked), Maxim (simulation + dashboard, less control), Retell (voice-only callers) — raw harness is right for 1 agent, platforms earn cost when 5-6 agents need dashboard, trends, persona UI |
| **CI economy** | 1 repetition per scenario on PR (smoke) + full 5-rep threshold-gated suite nightly; every run costs user-sim + agent + judge LLM calls, so full suite on every commit gets expensive fast |

**Deterministic recovery check**: scenario adds a non-judge assertion alongside the judge — both the conversational acknowledgment and the underlying status flip must hold; silent retry that eventually succeeds is a UX bug even with correct final state.

## Relevance to QA/QE

| QA Concern | Action |
|------------|--------|
| **Single-turn eval misses 3-turn failures** | Add simulation for any journey where user pushes back or tool can fail mid-conversation; one-shot prompt-response is not coverage |
| **Silent retry bug** | Assert failure was acknowledged before retry (transcript), not just that final state eventually became correct; second deterministic check enforces it |
| **Flaky multi-LLM harness** | Gate on pass rate (4/5) not single boolean; on inconsistent rate, first rewrite persona/goal and rubric specificity, only then adjust threshold |
| **Assertion strictness** | Use semantic/judge for phrasing freedom, exact for IDs/statuses; exact-match on free text flakes and erodes trust |
| **Framework reuse** | Keep `AgentAdapter` seam; same harness drives LangGraph, CrewAI, or bespoke agents without per-framework test files |
| **Cost control** | Run one repetition per scenario per PR, full N-run nightly; treat failing nightly as same-day incident, not a red badge to defer |
| **Conversation ≠ application** | Pair transcript pass with behavioral E2E: order row shows Cancelled, team dashboard shows it, inventory released — transcript alone is claim, not proof |

## Critical Analysis

**Strengths:**
- Cleanly derives the three roles and their responsibilities, with the adapter boundary as the reuse enabler — the "three LLM calls, a loop, and an assertion" framing demystifies what platforms productize.
- Tool-failure recovery scenario is well-chosen: first `cancel_order` timeout → acknowledge → retry → success; the middle criterion (acknowledged before retry) is the high-value insight that a final-state-only check misses, and the deterministic second check strengthens it.
- Non-determinism guidance is practical and correctly ordered: run N, gate on threshold, tighten persona/criteria first, don't chase flakes with looser bars; assertion-matching discipline (exact for facts, semantic for prose) prevents the most common flake source.
- Build-vs-adopt criteria (agent count >5-6, non-engineers authoring personas, need for history/trends) are concrete purchase signals, not generic "at scale consider a platform."

**Gaps:**
- Voice vs chat distinction (Retell) is table-level but not exercised; no guidance on modalities where transcription/speech adds its own variance.
- Persona/goal authoring quality — the largest lever on flake rate — is advised as "tighten" but has no rubric or review checklist for what "tight" means.
- Judge calibration (agreement vs human, prompt sensitivity, cost per verdict) is not measured; embedding-similarity alternative is mentioned but not benchmarked.
- Application-state gap is delegated to Autonoma's stack (PreviewKit etc.) without a hand-rolled minimal alternative for teams not on the platform.

## Worked Example (from raw)

- **Scenario**: customer wants order A1092 cancelled; simulator persona "impatient customer who pushes back once if agent gives up" with goal "A1092 status is cancelled."
- **Turns**: T1 user asks cancel A1092 → T2 agent calls `cancel_order(A1092)` → tool raises timeout → T3 agent must acknowledge failure ("the cancellation hit a hiccup") → T4 agent retries `cancel_order(A1092)` → succeeds → T5 agent confirms cancelled.
- **Judge rubric**: PASS only if (1) order status → cancelled by end, (2) transcript shows acknowledgment before retry, (3) agent never blindly repeats failing call >2× silently. Silent retry that succeeds fails criterion 2 even though criterion 1 passes — that is the UX bug simulation catches.
- **Deterministic double-check**: alongside judge, assert transcript contains "retry" acknowledgment string and final DB/API state shows cancelled — two independent signals.
- **Platform contrast**: same 5-turn timeline exists as LangWatch Scenario example; raw harness reproduces it without SDK by swapping `LLMClient` provider class only.

## FAQ Highlights (from raw)

- **What is agent simulation testing?** Synthetic LLM user (persona+goal) vs agent over N turns, judge scores full transcript against explicit rubric; validates path including failure recovery, not a single reply.
- **How is it different from LLM eval?** Eval grades one input-output pair (point); simulation validates multi-turn journey (path) — pushback, tool failure, recovery.
- **Need a vendor SDK?** No — three roles + loop + assertion in raw Python on any provider; LangWatch/Maxim/Retell productize the same pattern with dashboard + trends.
- **How many runs to trust?** Five with 4/5 threshold as starting point; tightening persona/goal and criteria beats loosening threshold for inconsistency.
- **Build vs adopt?** Build for 1-few agents (afternoon of Python); adopt LangWatch/Maxim/Retell once 5-6 agents need managed metrics, historical trends, non-engineer persona UI.

## Reuse Checklist

- Copy `src/harness.py`: `LLMClient`, `UserSimulatorAgent`, `AgentAdapter`, `JudgeAgent`, `SimulationRunner`; only `LLMClient` touches provider SDK — swap there.
- Copy `src/order_cancellation_scenario.py` as template: inject one real failure mode per scenario (timeout, 500, write not landed); make simulator push back once.
- Keep judge criteria file small and versioned (3 bullets max); criteria like "helpful" produce random verdicts — rewrite to checkable claims.
- Add `tests/test_non_determinism.py` patterns: exact for IDs/statuses, semantic/judge for phrasing, 5-run gating before shipping to main.
- CI: one repetition per scenario per PR (smoke) + full 5-rep suite nightly with pass-rate gate; treat nightly red as incident.
- Add one behavioral probe per mutating tool after transcript pass — cancel_order flipped row, dashboard shows Cancelled, inventory released — transcript is claim, not proof.

## Cross-links

- Simulation detail: [Multi-Turn Conversations](autonoma-multi-turn-conversations-2026.md) — extends same harness for three multi-turn retention failure modes on top of failure-recovery
- LangGraph binding: [LangGraph Testing](autonoma-langgraph-testing-2026.md) — multi-turn simulation over one `thread_id` as framework-specific implementation of same loop
- CrewAI binding: [CrewAI Evaluation](autonoma-crewai-evaluation-2026.md) — Scenario delegation as the CrewAI-flavored three-actor pattern (simulator, adapter, judge)
- E2E arc: [How to Test an AI Agent E2E](autonoma-how-to-test-ai-agent-e2e-2026.md) — simulation is Stage 4 trajectory + Stage 3 judge fused across turns; Stage 5 behavioral is the gap
- Tool calls: [Testing Tool Calls](autonoma-testing-tool-calls-2026.md) — tool-failure injection and argument correctness inside the simulated path
- Multi-agent: [Multi-Agent Handoffs](autonoma-multi-agent-handoffs-2026.md) — recovery at handoff boundary is the multi-agent analog of this single-agent recovery
- Regression: [Agent Regression](autonoma-agent-regression-2026.md) — N-run + threshold gating pattern reused at conversation scope
- Evidence: [AI QA Evidence Layer](ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md) — judge verdict = eval; DB/dashboard state = downstream validation
- Deep dive: [Agent Simulation Testing raw](https://getautonoma.com/blog/agent-simulation-testing), [Testing an MCP Server](https://getautonoma.com/blog/how-to-test-an-mcp-server)

*Ingested: 2026-08-31*
