# CrewAI Evaluation and Testing: How to Test CrewAI Agents

**Source:** https://getautonoma.com/blog/crewai-evaluation
**Date:** 2026-07-24
**Tags:** #autonoma
**Raw:** [autonoma-crewai-evaluation-2026.md](../raw/autonoma-crewai-evaluation-2026.md)

---

## What It Is

- **CrewAI evaluation as three layers of increasing resolution** — `crewai test` CLI aggregate score → DeepEval span-level tool/agent assertions → LangWatch Scenario delegation testing — Tom Piaggio (Autonoma, 2026-07-24). Each layer catches what the one above structurally cannot see.
- **Reference crew**: two-agent support crew — triage agent (`allow_delegation=True`, instructed never to answer billing questions itself) + billing resolver with `look_up_order` tool (`src/crew.py`). Delegation is a model decision, not a written function call — where the interesting bugs live.
- **Runnable repo** `Autonoma-Tools/crewai-evaluation`: `scripts/baseline_eval.sh`, `tests/test_deepeval_spans.py`, `tests/test_delegation_scenario.py`, plus `examples/autogen_groupchat_test.py` and `examples/openai_agents_sdk_test.py` showing the same handoff assertion ported to AutoGen and OpenAI Agents SDK; CI at `.github/workflows/agent-tests.yml`.
- **Gap named**: a `crewai test` 8.2/10 can coexist with a broken delegation (triage answered itself and got lucky on wording); framework docs stop at the CLI, scattered guides for DeepEval/Promptfoo/Scenario do not build on each other. The piece builds the progression as one runnable path and separates conversation grading from application-state verification (Autonoma behavioral layer).

## Key Patterns / Techniques

| Layer | Catches | Misses | How (from raw) |
|-------|---------|--------|----------------|
| **Layer 1 — `crewai test` CLI** | Overall quality drift, N-run average | Which agent, which tool, which args | Run `crewai test -n 5 -m gpt-4o-mini` (default 3 iters, grading model `gpt-4o-mini`); aggregate score is smoke check after prompt edit; re-averaging absorbs variance like any N-run gate |
| **Layer 2 — DeepEval spans** | Wrong tool args, wrong agent behavior | Whether delegation happened at all | `instrument_crewai()` once; `Agent`/`tool` accept `metrics` like `Task` accepts `expected_output`; assertions attach to spans from `crew.kickoff()` → agent → tool; reserve exact-match for hard facts (order ID, status), semantic/`GEval` for phrasing; gate on pass rate over 3-5 runs, not one run |
| **Layer 3 — Scenario delegation** | Right agent, full context, clean handoff | Real app state after crew runs | Wrap crew behind `AgentAdapter` (adapter boundary makes framework reusable); `UserSimulatorAgent` drives request, `JudgeAgent` grades transcript against 3 explicit criteria: triage delegated (not answered itself), delegated task carried exact order ID, final answer reflects real status; middle criterion catches the silent-ID-drop bug that final-answer checks miss |

**Criteria discipline (cross-cutting):** write judge criteria as checkable claims ("order ID intact"), not vague ("helpful"); if delegation test flakes, tighten `goal` text and `JudgeAgent` criteria before loosening pass threshold — underspecified persona/goal is the usual variance source. Same three checks ported to AutoGen (`RoundRobinGroupChat` message sources) and OpenAI Agents SDK (`HandoffOutputItem` in `new_items`).

**Cost/CI split:** CLI + DeepEval spans on every PR (cheap); Scenario delegation (5 runs for stable pass rate) nightly; failing nightly is an incident to triage same day, not a badge to ignore.

## Relevance to QA/QE

| QA Concern | Action |
|------------|--------|
| **"Score looked fine, crew was broken"** | Never gate on `crewai test` aggregate alone; add at least DeepEval span assertions on every mutating tool's arguments |
| **Plausible final answer hiding broken handoff** | Add delegation criteria that separately assert: right agent chosen, context (order ID) intact in handoff, handoff not dropped — final text alone cannot prove the second |
| **Flaky semantic assertions** | Use exact-match only for IDs/statuses; use `GEval`/similarity for phrasing; run 3-5 times and gate on pass rate; tighten goal/criteria first when flaky |
| **Framework lock-in** | Keep `AgentAdapter` boundary; same three checkpoints (right agent, complete context, clean handoff) port to AutoGen/OpenAI SDK by locating where that framework exposes the handoff event |
| **Mutation of state not checked** | Pair span/delegation pass with behavioral E2E: `cancel_order` flipped DB row, dashboard shows resolved, inventory not stale — none of the three layers check app state |
| **CI signal** | Treat regressed nightly delegation pass rate as incident; badge it like a failed canary, not a flaky stat |
| **When Layer 3 can wait** | Solo crew, single owner: `crewai test` in CI + handful of span assertions is defensible; add Scenario delegation once >2 agents or silent bad handoff is customer-facing |

## Critical Analysis

**Strengths:**
- Correctly frames `crewai test` as smoke check, not verification — the "8.2 but which agent did the work" example is a crisp false-confidence story and the table (catches/misses per layer) makes the blind spot explicit.
- Span-level guidance is precise: `instrument_crewai()` one-liner, `metrics` on `Agent`/`tool`, and the exact-match-vs-semantic discipline (order ID exact, wording judged) with N-run pass-rate gating is the right non-determinism playbook.
- Delegation testing is the highest-value contribution — almost uncovered elsewhere — and the three checkpoints (right agent, ID intact, not dropped) plus the ID-drop silent-failure mode are a design that directly transfers to AutoGen/OpenAI SDK with concrete example files.
- Honest cost ladder and CI split (cheap on PR, expensive nightly) prevents the "run everything on every commit" expense trap.

**Gaps:**
- `crewai test` grading model choice and its own variance/grading accuracy are not characterized — threshold for "score drift is real" vs noise is left to the reader's CI history.
- DeepEval `GEval` calibration (agreement vs human, prompt sensitivity, cost per span) is not quantified; no guidance on embedding model vs judge trade-off for semantic checks.
- Delegation Scenario examples are CrewAI-native; AutoGen/OpenAI SDK are sketched as equivalents but not run as full peers in the same suite.
- Application-state gap is scoped to Autonoma's product surface (Planner/Execution/Diffs); hand-rolled alternative for that gap is not demonstrated.

## Worked Example (from raw)

- **Crew**: triage (`allow_delegation=True`, prompt says never answer billing) + billing resolver (`look_up_order`); customer asks "what is status of order A1092 pending cancellation?"
- **Layer 1**: `crewai test -n 5 -m gpt-4o-mini` returns 8.2/10 — looks fine even if triage delegated with dropped order ID and resolver guessed.
- **Layer 2 DeepEval**: `tests/test_deepeval_spans.py` instruments `crew.kickoff()`; metric on `look_up_order` asserts `order_id == "A1092"` exactly and status phrasing via `GEval` similarity — catches invented ID even when final answer reads plausibly.
- **Layer 3 Scenario**: `tests/test_delegation_scenario.py` wraps crew in `AgentAdapter`; `UserSimulatorAgent` sends billing request; `JudgeAgent` checks (a) triage delegated vs answered itself, (b) delegated payload still contains `A1092`, (c) final answer reflects real `pending_cancellation` — middle check fails if handoff drops ID.
- **Port**: same three checks re-expressed as AutoGen `RoundRobinGroupChat` source-agent list and OpenAI Agents SDK `HandoffOutputItem` in `new_items` (`examples/autogen_groupchat_test.py`, `examples/openai_agents_sdk_test.py`).

## FAQ Highlights (from raw)

- **What does CrewAI evaluation mean?** Verify crew behavior not just final wording — aggregate score + span-level tool assertions + delegation correctness (right agent, intact context, clean handoff).
- **How to use `crewai test`?** Run from project root, `-n` iters (default 3), `-m` grading model (default `gpt-4o-mini`); returns average quality score, not who did the work.
- **What is span-level testing?** Attach assertions to individual steps inside `crew.kickoff()` (agent execution, tool call) via DeepEval spans so wrong args fail even when final answer looks correct.
- **How to test delegation?** `AgentAdapter` + `UserSimulatorAgent` + `JudgeAgent` with 3 criteria (right agent, exact order ID carried, final answer reflects real status) — LangWatch Scenario implements this natively.
- **Different from AutoGen / OpenAI SDK?** Same question, different surface: CrewAI `allow_delegation`/`Process`, AutoGen source-tagged messages, OpenAI `HandoffOutputItem` — pattern ports once built.

## Reuse Checklist

- Run `crewai test -n 5` in CI as smoke; treat score drop as trigger to drill into spans, not as gate alone.
- Add `instrument_crewai()` in `tests/test_deepeval_spans.py` once; attach one metric per mutating tool arguing exact IDs and `GEval` for phrasing; gate on 3/5 or 4/5 pass rate.
- Add `tests/test_delegation_scenario.py`: `AgentAdapter` wrapper, explicit judge criteria file (3 bullets), `UserSimulatorAgent` goal text reviewed in PR; run 5 times nightly.
- On flaky delegation, tighten goal and criteria prose first; only loosen pass rate after proving criteria unambiguous via 3 consecutive green nightlies.
- Search for handoff surface when porting: CrewAI delegation, AutoGen message sources, OpenAI handoff item — assert the same three claims.
- Add one behavioral E2E query per crew tool that mutates — DB row flipped, dashboard resolved — no conversation layer checks it.

## Cross-links

- LangGraph counterpart: [LangGraph Testing](autonoma-langgraph-testing-2026.md) — same isolate → verify routing → multi-turn arc for graph orchestration (`get_state_history` vs `AgentAdapter`)
- Simulation harness: [Agent Simulation](autonoma-agent-simulation-2026.md) — three-actor pattern (simulator, adapter, judge) generalized beyond CrewAI; raw-Python harness is the portable reference
- Tool calls: [Testing Tool Calls](autonoma-testing-tool-calls-2026.md) — span assertions are the CrewAI binding of the same tool-call argument discipline
- Multi-agent: [Multi-Agent Handoffs](autonoma-multi-agent-handoffs-2026.md) — handoff contract (right agent, complete context) as framework-agnostic principle
- E2E arc: [How to Test an AI Agent E2E](autonoma-how-to-test-ai-agent-e2e-2026.md) — Layers 1-3 map to eval/trajectory stages; Stage 5 behavioral is the app-state gap none of them cover
- Regression: [Agent Regression](autonoma-agent-regression-2026.md) — N-run averaging + tolerance for crew spans
- Evidence: [AI QA Evidence Layer](ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md) — crew reply grading vs downstream state validation; `offline-evaluation-trajectories-2026.md` for trajectory replay
- Deep dive: [CrewAI Evaluation raw](https://getautonoma.com/blog/crewai-evaluation), [Agent Simulation Testing](https://getautonoma.com/blog/agent-simulation-testing)

*Ingested: 2026-08-31*
