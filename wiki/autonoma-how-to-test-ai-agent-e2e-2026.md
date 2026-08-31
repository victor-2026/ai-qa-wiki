# How to Test an AI Agent (End to End)

**Source:** https://getautonoma.com/blog/how-to-test-an-ai-agent
**Date:** 2026-07-24
**Tags:** #autonoma #ai-agent #e2e-testing
**Raw:** [autonoma-how-to-test-an-ai-agent-2026.md](../raw/autonoma-how-to-test-an-ai-agent-2026.md)

---

## What It Is (3-5 bullets)

- **Six-stage runnable arc** for testing AI agents end to end by Tom Piaggio (Autonoma, 2026-07-24): trace → deterministic evals → LLM-as-judge → trajectory → behavioral E2E → CI regression. Each stage catches a failure the others cannot see; repo `Autonoma-Tools/how-to-test-an-ai-agent` implements all stages with pytest.
- **Distinction framing**: testing an agent's behavior ≠ using an agent to do your testing; a response that sounds correct ≠ an action that happened correctly (tool can be called with right words while app state stays unchanged).
- **Tracing is foundational**: wrapper around every LLM and tool call producing typed events (`llm_call`, `tool_call`, `decision`) in order — the record that Stages 2-4 actually assert against (`src/tracing.py`).
- **Behavioral E2E is the gap most guides skip**: Stages 1-4 can all pass at 5/5 while the running app is untouched; Stage 5 queries API/DB or drives UI independently to confirm state changed. Autonoma's role is positioned as that layer (Planner + Execution Agent + PreviewKit + GenerationReviewer + Diffs Agent).

## Key Patterns / Techniques (table or bullets)

| Stage | Verifies | Misses | Tooling (from raw) |
|-------|----------|--------|--------------------|
| **1. Trace** | What steps ran | Whether steps were correct | Wrapper / spans → `src/tracing.py` |
| **2. Deterministic evals** | Structured fields, enums, JSON schema | Free-text quality | pytest, jsonschema → `tests/test_structured_output.py` |
| **3. LLM-as-judge** | Free-text quality | Whether tools ran correctly | Judge model + rubric (3-4 yes/no questions, not "is it good") → `tests/test_llm_judge.py` |
| **4. Trajectory** | Tool order, arguments, failure recovery | App-side effects | Trace replay + pytest → `tests/test_trajectory.py` (asserts `process_refund` sequence + recovery) |
| **5. Behavioral E2E** | What the app actually did | Nothing upstream, but needs 1-4 first | Live preview, browser checks, API/DB query → `tests/test_behavioral_e2e_illustration.py` |
| **6. CI regression** | All of above per PR | Anything not in suite | GitHub Actions → `.github/workflows/agent-tests.yml` |

**Non-determinism handling (cross-cutting):**
- Majority vote: run N times, require K passes (e.g., 5 runs, ≥4 pass) rather than single-run exact match — `lib/majority_vote.py`.
- Semantic similarity over string equality (embedding or judge yes/no on equivalence); a drop from 5/5 to 3/5 is a real signal, always 5/5 on exact match often means too loose.
- Version rubric as artifact — tightening rubric is raising the bar; loosening to make a test pass lowers production bar.

**CI cost/latency note:** Deterministic per commit (no API), judge+trajectory per PR (costly), behavioral E2E per PR against PreviewKit (long pole). Log tokens + latency alongside pass/fail; flag drift vs rolling baseline. Stable canary pattern referenced via `ai-agent-reliability-testing`.

## Relevance to QA/QE (table QA Action)

| QA Concern | Action |
|------------|--------|
| **Build order, not checklist** | Implement sequentially: tracing → deterministic (cheapest) → judge (once rubric trusted) → trajectory (once traces known) → behavioral E2E → CI gate |
| **Deterministic first** | If structured output fails, stop — fix enum/schema before spending judge calls; deterministic should absorb as much surface as shape allows |
| **Rubric discipline** | Write judge rubric as versioned file with 3-4 checkable yes/no items (e.g., "mentions refund amount", "avoids promising timeline"); never inline-tweak to make a test pass |
| **Trajectory vs outcome split** | Pair `process_refund(order_id, amount)` trajectory assertion with independent state query — refund row exists, order status flipped, email sent |
| **CI gating** | Wire deterministic + judge + trajectory + behavioral into required PR checks; surface per-scenario pass rate (17/20) not just green checkmark |
| **Regression from provider drift** | Expect silent model updates behind same alias; majority-vote trend + token/latency tracking catches changes with zero code diff on your side |
| **Autonomy scaling** | The more multi-step tool use an agent has, the more Stages 4-5 matter — chaining correct-looking decisions into wrong final action |

## Critical Analysis (Strengths/Gaps)

**Strengths:**
- Complete arc with runnable code per stage — rare among "how to test an agent" prose; PostHog/IBM/Salesforce comparisons explicitly note the code gap.
- Clear stage table (verifies/misses/tooling) makes ownership and blind spots explicit; Stage 5 gap (response-correct, action-wrong) illustrated with `process_refund` returning success without side effect.
- Non-determinism guidance is concrete: N-run majority + semantic similarity + trend reporting, with helper implementation.
- Positions Autonoma without claiming to replace evals — maps Planner/Execution/GenerationReviewer/Diffs to the behavioral layer Stages 1-4 cannot cover.

**Gaps:**
- Example agent is small (lookup + refund) — no vector-store retrieval, no multi-session memory, no tool auth/scope edge cases.
- Judge calibration not quantified (agreement rate, threshold tuning); no guidance on embedding model choice for semantic similarity.
- Behavioral E2E illustration is hand-rolled API/DB check; scaling to N tools × M UI surfaces maintenance cost is acknowledged but not solved generically (PreviewKit is product-specific).
- Canary/cost/latency mentioned but not implemented in the companion workflow — left as "worth watching separately."

## Worked Example (from raw)

Support agent with `lookup` + `refund` tools:

- **Stage 1 trace:** `llm_call(decide) → tool_call(lookup order 4821) → llm_call(interpret) → tool_call(process_refund) → llm_call(respond)` — typed events enable all later assertions.
- **Stage 2 deterministic:** enum `status: refunded` and JSON schema for decision object — fails fast before judge.
- **Stage 3 judge:** rubric asks 4 yes/no — mentions amount, mentions order id, avoids promising timeline, tone appropriate — thresholded score.
- **Stage 4 trajectory:** asserts `process_refund(order_id="4821", amount=42.00)` happened after lookup and retried after injected timeout.
- **Stage 5 behavioral:** after `process_refund`, independently query refund table/API — row exists, order status flipped; catches the "said refund processed but never called API" case from raw opening.
- **Stage 6 CI:** deterministic on every commit, judge+trajectory on PR with majority vote, behavioral on PreviewKit; silent provider model update surfaces as red PR not customer ticket.

## FAQ Highlights (from raw)

- How to test end to end = run 6 stages; each catches what others miss.
- Testing agent vs using agent to test software are unrelated categories.
- Validate structured with pytest/jsonschema, free-text with judge rubric, non-deterministic with N-run majority + semantic similarity.
- Trajectory = tool order/args/recovery; behavioral = app state actually changed — need both.

## Reuse Checklist

- Copy `src/tracing.py` wrapper first — without trace, Stages 2-4 degrade to black-box final-output guessing.
- Seed deterministic evals with your agent's real schemas; run on every commit — cheapest gate, should block before judge spend.
- Keep rubric in `rubrics/refund.md` versioned; change requires PR review, not inline tweak when test flakes.
- Reuse `lib/majority_vote.py` for any judge or trajectory scenario; start with 5 runs / 4-pass threshold and tune from trend data.
- For Stage 5, add one API/DB state query per tool that mutates — refund row, status field, email outbox — before adding full browser E2E.

## Cross-links

- Tool calls deep dive: [Testing Tool Calls](autonoma-testing-tool-calls-2026.md) — expands Stage 4 with 6 assertion types and mock-vs-live
- Multi-agent: [Multi-Agent Handoffs](autonoma-multi-agent-handoffs-2026.md) — same tracing idea at handoffs between agents
- Memory: [Agent Memory](autonoma-agent-memory-2026.md) — cross-session persistence that tracing alone does not cover
- Reliability: [Agent Reliability](autonoma-agent-reliability-2026.md) — trajectory + baseline diff + canary for drift over time
- Evidence layer: [AI QA Evidence Layer](ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md) — response eval vs downstream validation; `offline-evaluation-trajectories-2026.md` for trajectory replay
- Deeper: [Agent Simulation Testing](https://getautonoma.com/blog/agent-simulation-testing), [Agent Regression Testing](https://getautonoma.com/blog/agent-regression-testing), [Reliability Testing](https://getautonoma.com/blog/ai-agent-reliability-testing)

*Ingested: 2026-08-31*
