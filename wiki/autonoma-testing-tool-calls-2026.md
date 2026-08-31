# How to Test AI Agents That Take Actions (Tool Calls)

**Source:** https://getautonoma.com/blog/testing-ai-agent-tool-calls
**Date:** 2026-07-24
**Tags:** #autonoma #tool-calls #trajectory-evaluation
**Raw:** [autonoma-testing-ai-agent-tool-calls-2026.md](../raw/autonoma-testing-ai-agent-tool-calls-2026.md)

---

## What It Is (3-5 bullets)

- **Trajectory evaluation** for tool-calling agents: capture the ordered list of tool calls (tool name, arguments, result, error) produced during a run and assert against it after the fact, instead of judging only the final text.
- **Framework-neutral runnable guide** by Tom Piaggio (Autonoma, 2026-07-24) with companion repo `Autonoma-Tools/testing-ai-agent-tool-calls` — `agent.py` harness, `conftest.py` fixtures (`AppState`, `search_flights`, `book_flight`, `get_weather`, `ScriptedLLM`), and one pytest file per assertion type.
- **Three independent decision layers** fail independently: right tool (rarest after real usage), right order (dependency + user-expected sequence), right arguments (most frequent and highest value). A correct tool with wrong arguments looks like success until argument-accuracy is checked.
- **Covers 6 assertion types plus CI wiring** and explicitly scopes trajectory checks to the call boundary — they never confirm the tool's effect landed correctly in the running app (that requires a behavioral E2E layer).

## Key Patterns / Techniques (table or bullets)

| Pattern | How it works (from raw) | File in repo |
|---------|-------------------------|--------------|
| **Framework-neutral harness** | `Agent` loops until done, calls real tool functions, records trajectory; `llm_decide` seam swapped for `ScriptedLLM` in tests for determinism | `agent.py`, `conftest.py` |
| **Right tool** | Assert expected tool appears, irrelevant tool (`get_weather`) absent | `test_right_tool.py` |
| **Right order** | Assert sequence matches dependency (search before book); 3-tool trajectory used to catch reordering under rephrased prompts | `test_tool_order.py` |
| **Right arguments (highest value)** | Assert payload matches user intent; example books one day off — tool selection passes, argument check correctly fails | `test_argument_accuracy.py` |
| **Mock vs live** | Mock asserts on call (fast, isolates decision logic); live asserts on effect (booking record exists in `AppState.bookings`) | `test_mocking_vs_live.py` |
| **Failure handling** | Inject transient 5xx/timeout → assert retry succeeds + booking present; inject permanent failure → assert error visible in trajectory + no false success state | `test_failure_handling.py` |
| **Non-determinism (K-of-N)** | Run N times, require K passes; assert on invariant (tool name, argument shape/type) not literal string (`2026-08-01` vs `08/01/2026`); treat flaky drop as signal to tighten assertion or tool description, not threshold | `test_non_determinism.py` |
| **CI wiring** | Deterministic + K-of-N in same required check; report pass rate (`17/20`) in job summary for trend detection | `.github/workflows/test.yml` |

Additional details: `book_flight` writes to `AppState.bookings` to enable mock-vs-live contrast; MCP variant noted as separate surface (`/blog/how-to-test-an-mcp-server`); LangGraph formalizes trajectory as first-class concept (see `langgraph-testing` guide).

## Relevance to QA/QE (table QA Action)

| QA Concern | Action |
|------------|--------|
| **Argument accuracy is #1 priority** | If only one trajectory check ships, ship argument-accuracy — "called `book_flight()`" is not a finding; "called with user-requested date" is |
| **Separate decision from effect** | Pair every trajectory assertion with a behavioral check that the booking/record appears where the user looks (UI, itinerary, DB) |
| **Mock vs live trade-off** | Use mocks in fast inner loop for decision logic; use live execution whenever "did it actually change state" matters (most tool-call tests) |
| **Failure handling as prod readiness** | Require explicit trajectory evidence for retry on transient and explicit error + no partial state on permanent failure; fail if agent swallows exception and reports success |
| **Non-determinism gating** | Adopt K-of-N (e.g., 17/20) as hard gate in required CI job, not best-effort; log token/latency alongside pass rate to catch cost drift |
| **Tool design feedback** | When K-of-N flakes, first tighten tool description/prompt ambiguity before loosening assertion |

## Critical Analysis (Strengths/Gaps)

**Strengths:**
- Runnable, not conceptual — 6 pytest files + harness paste-ready; closes the gap where "trajectory evaluation" is explained but rarely asserted.
- Correctly prioritizes argument accuracy over tool selection and flags the trajectory-vs-outcome gap with clear diagrams.
- Failure-handling dual assertion (transient retry + permanent explicit error) catches the dangerous "reassuring message with no action" mode.
- Non-determinism advice is practical: invariant over literal, K-of-N in required check, pass-rate trending.

**Gaps:**
- Toy domain (3 tools, booking dict) — scaling to 20+ tools with overlapping descriptions and real auth/rate-limit not shown.
- K threshold guidance remains heuristic; no data on choosing 17/20 vs 18/20 or cost of 20x runs in CI.
- MCP and framework-specific plumbing deferred to separate guides; integration between trajectory and behavioral E2E layers is described at Autonoma product level, not as generic harness.
- No coverage of argument schema validation (Pydantic/jsonschema) at the handoff between LLM output and tool call.

## Worked Example (from raw)

Booking system: `AppState.bookings` dict + `search_flights` / `book_flight` / `get_weather`.

- **Happy path:** user asks "book flight 2026-08-01" → trajectory `[search_flights, book_flight(date=2026-08-01)]` → live assertion checks `bookings` contains entry with that date.
- **Argument off-by-one:** same request, agent calls `book_flight(date=2026-08-02)` → tool-selection pass, argument-accuracy fail — the guide's central illustration.
- **Transient failure:** inject `book_flight` → `TimeoutError` once → assert trajectory shows `error → retry → success` and booking present.
- **Permanent failure:** inject 5xx always → assert trajectory shows explicit error and `bookings` still empty (catches swallowed exception + reassuring message).
- **Non-determinism:** same prompt 20x → agent sometimes formats date as `08/01/2026` → literal equality would flake; invariant `is_date_shape` passes, K-of-N reports 19/20.

## FAQ Highlights (from raw)

- Trajectory evaluation = capturing ordered tool list with args/results and asserting after run; white-box on call, not effect.
- Right tool ≠ right outcome — argument check is the discriminator for most real bugs.
- Non-determinism: N runs, K threshold, invariant shape, same required CI job; report trend not just verdict.
- Mock vs live: mock proves tried, live proves landed — use both, they answer different questions.

## Reuse Checklist

- Clone `Autonoma-Tools/testing-ai-agent-tool-calls`, run `pytest` — all tests pass as written with `ScriptedLLM`; swap seam for real model in prod.
- Start with `test_argument_accuracy.py` pattern — copy invariant check `assert call.args["date"] == user_date` before adding order/tool checks.
- Add failure injection fixture that raises once then succeeds; verify both trajectory length and `AppState` state in same test.
- For K-of-N, wrap flaky scenario in loop of 20, assert `sum(passed)/20 >= 0.85`; keep in required job, emit `Passed 17/20 (85%)` to job summary.
- Document tool descriptions alongside tests — when routing or argument flakes, diff tool description first.

## Cross-links

- E2E arc: [How to Test an AI Agent E2E](autonoma-how-to-test-ai-agent-e2e-2026.md) — Stage 4 trajectory in full 6-stage pipeline; `offline-evaluation-trajectories-2026.md` for trajectory replay without live calls
- Multi-agent: [Multi-Agent Handoffs](autonoma-multi-agent-handoffs-2026.md) — same trajectory idea extended to inter-agent handoff contracts
- Memory: [Agent Memory](autonoma-agent-memory-2026.md) — memory store is the persistent trajectory context across sessions
- Reliability: [Agent Reliability](autonoma-agent-reliability-2026.md) — baseline diff + canary extends trajectory checks over time
- Evidence layer: [AI QA Evidence Layer](ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md) — trajectory = model eval, outcome = downstream validation; `testing-ai-agent-tool-calls-autonoma.md` (earlier wiki summary) before this page
- External: [Autonoma repo — testing-ai-agent-tool-calls](https://github.com/Autonoma-Tools/testing-ai-agent-tool-calls), [Testing MCP Server](https://getautonoma.com/blog/how-to-test-an-mcp-server), [LangGraph Testing](https://getautonoma.com/blog/langgraph-testing)

*Ingested: 2026-08-31*
