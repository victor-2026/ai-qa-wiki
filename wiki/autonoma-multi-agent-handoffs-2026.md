# How to Test Multi-Agent Systems (Handoffs and Orchestration)

**Source:** https://getautonoma.com/blog/how-to-test-multi-agent-systems
**Date:** 2026-07-29
**Tags:** #autonoma #multi-agent #handoffs
**Raw:** [autonoma-how-to-test-multi-agent-systems-2026.md](../raw/autonoma-how-to-test-multi-agent-systems-2026.md)

---

## What It Is (3-5 bullets)

- **Testing a multi-agent system = testing handoffs, delegation, and orchestration**, not just individual agents. A pipeline can pass every single-agent suite and still answer the wrong question because the drafting agent never received the constraint the planner locked in three steps earlier.
- **Runnable pytest suite** by Tom Piaggio (Autonoma, 2026-07-29) for the 4 most common multi-agent failures: handoff context loss, wrong delegation, orchestration silent drops, cascading error amplification. Repo `Autonoma-Tools/how-to-test-multi-agent-systems`.
- **Three assertion surfaces** + debugging aid: handoff contract (payload schema at boundary, Pydantic), delegation correctness (routing decision, majority-vote for non-deterministic routers), orchestration sequence (executed step list vs plan), and trace-bisection via correlation ID (W3C Trace Context).
- **Integration-bug framing**: failures are not language failures and are invisible in final output — they require asserting on what the system *did* (message, routing, step sequence) rather than what it *returned*, plus a separate behavioral E2E check that the product effect actually happened.

## Key Patterns / Techniques (table or bullets)

| Failure Class | Observable Symptom | What to Assert | Where in repo |
|---------------|--------------------|----------------|---------------|
| **Handoff context loss** (most common) | Downstream agent asks again or guesses; planner's $200 cap forwarded as "find hotel" | Full payload schema at boundary, Pydantic contract — fail immediately on missing field before next agent invents answer | `tests/test_handoff_contract.py` |
| **Wrong delegation** | Right-sounding output, wrong agent used; refund routed to general support → polite reply, no refund | Routing decision (did orchestrator pick capable agent, inside allowed set), not final text; majority vote over N runs for stochastic routers; pair with outcome check (refund record) | `tests/test_delegation_routing.py` |
| **Orchestration silent drop** | Step missing from execution log; 4-step plan runs 3 steps, returns plausible answer | Full executed step sequence vs planned sequence as structured list comparison, not regex on free-text logs | `tests/test_orchestration_sequence.py` |
| **Cascading amplification** | Small early error (wrong date) treated as ground truth downstream, grows by step 4 | Intermediate values, not just final output |

**Orchestration extras:** out-of-order steps (dependency violation), deadlock (mutual wait = hang), retry storm (flaky step without backoff → duplicate calls). Structured step logging makes all four catchable.

**Debugging pattern:** correlation ID on every inter-agent message (W3C Trace Context), capture full message log, bisect to first divergent message — the agent that visibly fails is usually the first to *notice*, not the cause (`tools/trace_bisect.py`).

**CI & terminology:** `.github/workflows/multi-agent-tests.yml` runs suite per PR; agent-to-agent (A2A) is same testing under different names; framework-agnostic (CrewAI/AutoGen/LangGraph/hand-rolled) — see `crewai-evaluation` for CrewAI hooks. Other surfaces referenced: `non-deterministic AI outputs`, `agent-simulation-testing`.

## Relevance to QA/QE (table QA Action)

| QA Concern | Action |
|------------|--------|
| **Handoff contracts first** | Define Pydantic schema for every inter-agent message; assert at the edge that required fields are present — do not wait for downstream text quality to degrade |
| **Route vs result separation** | Add routing-level assertion ("picked billing agent") AND outcome assertion ("refund record exists") — routing test stays green when billing tool changes, outcome reveals it |
| **Orchestration sequence as list** | Log executed steps as structured data; assert list equality vs plan — catches silent drops and reordering that final-output checks miss |
| **Non-deterministic router handling** | Assert on structure/constraints (capable agent, allowed set) not literal path; for stochastic routing, run N times and assert majority |
| **Silent misroute detection** | Watch for competent-but-wrong-agent producing plausible output — only routing assertion catches this; text grading never will |
| **Traceability in CI** | Put correlation ID tracing in before you need it; bisect helper turns afternoon debug into minutes |
| **Behavioral complement** | Pair contract/routing/sequence with Autonoma-style behavioral E2E on deployed app (record changed, email sent) — pipeline can be internally correct and still produce wrong product outcome |

## Critical Analysis (Strengths/Gaps)

**Strengths:**
- Correctly reframes multi-agent QA as integration testing of probabilistic components — 4 failure classes are concrete and observable, not abstract.
- Actionable repo mapping per surface (contract, routing, sequence, bisect) plus W3C Trace Context reuse instead of custom ID.
- Distinguishes flake signal vs noise: "delegation test flakes → assertion too strict or handoff underspecified" is the right triage.
- Explicitly warns that contract/routing/sequence together still do not prove product effect — ties to behavioral layer.

**Gaps:**
- No quantitative guidance on handoff schema strictness (optional vs required fields) or schema evolution versioning.
- Majority-vote threshold for routing left generic — no cost/latency trade-off for N runs in orchestration pipeline.
- Deadlock and retry-storm detection described but not demonstrated as assertions (timeouts, call counts) in the excerpted files.
- Example is linear planning→research→drafting; fan-out/fan-in, human-in-loop approval, and long-lived session persistence not covered.

## Worked Example (from raw)

Linear pipeline: planner → research → drafting.

- **Planner:** locks budget cap $200 + question "best boutique hotel under cap for 2 nights." If handoff forwards only "find a hotel" without cap, drafting produces wrong recommendation — invisible in single-agent pass.
- **Research:** returns 3 correctly cited sources; drafting receives them but loses the cap constraint from planner — final output answers wrong question with right citations.
- **Handoff assertion:** Pydantic schema requires `budget_cap`, `nights`, `constraints` at planner→research and research→drafting boundaries; missing cap fails before research even runs.
- **Delegation:** orchestrator must pick research agent with browsing tool for "find sources" not drafting agent; route assertion catches misroute even when drafting writes plausible text.
- **Orchestration:** plan `[plan, research, draft, fact-check]` → execution log `[plan, research, draft]` silently dropped `fact-check`; list comparison fails even though draft reads fine.
- **Debug:** message log with `trace_id=abc123` → bisect finds Message 2 (planner→research) already divergent; Fact-Check failure is symptom not cause.

## FAQ Highlights (from raw)

- Test 3 surfaces: handoff (schema at boundary), delegation (routing decision, not text), orchestration (full step sequence, not just output).
- A2A testing = same testing under different label; framework does not change surfaces (CrewAI/AutoGen/LangGraph all have them).
- Non-deterministic orchestrator: assert on capability/allowed set, N-run majority for stochastic routing.
- If every agent passes but workflow wrong → add behavioral assertion on outcome (refund record, email sent).

## Reuse Checklist

- Define `class HandoffMessage(BaseModel)` per edge with required fields; add `model_validate` assertion at orchestrator output boundary.
- Log `executed_steps: List[str]` as structured field, not log line — assert `executed == planned` list equality per run.
- For delegation, store `routing_decision` + `chosen_agent` in trace; assert `chosen_agent in capable_set` not literal equality.
- Instrument `trace_id` via `X-Trace-ID` header or `contextvars`; capture full message log for `trace_bisect.py` — run on every failure in CI artifact.
- Add one behavioral probe per workflow (e.g., after pipeline, query refund table) — keeps contract tests debuggable and outcome tests honest.

## Cross-links

- Single-agent trajectory: [Testing Tool Calls](autonoma-testing-tool-calls-2026.md) — same trajectory-replay idea per agent; [How to Test an AI Agent E2E](autonoma-how-to-test-ai-agent-e2e-2026.md) — Stage 4 trajectory generalized to 6-stage arc
- Memory: [Agent Memory](autonoma-agent-memory-2026.md) — cross-session persistence is the handoff across time
- Reliability: [Agent Reliability](autonoma-agent-reliability-2026.md) — silent failures and baseline diff apply at orchestration layer too
- Context: [Context Loss — Orchestration Separation](context-loss-orchestration-separation-2026.md), [Agent Simulation Testing](https://getautonoma.com/blog/agent-simulation-testing)
- Evidence: [AI QA Evidence Layer](ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md) — contract/routing/sequence = model eval; product effect = downstream validation; `ai-qa-tool-evaluation-mutation-matrix.md` as method for testing the testing tool itself

*Ingested: 2026-08-31*
