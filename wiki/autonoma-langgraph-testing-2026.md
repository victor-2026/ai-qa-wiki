# LangGraph Testing and Debugging: A Practical Guide

**Source:** https://getautonoma.com/blog/langgraph-testing
**Date:** 2026-07-24
**Tags:** #autonoma
**Raw:** [autonoma-langgraph-testing-2026.md](../raw/autonoma-langgraph-testing-2026.md)

---

## What It Is

- **LangGraph testing at three connected levels** — node-level unit tests via checkpointer isolation, trajectory/route verification via `get_state_history`, and multi-turn simulation over one `thread_id`, plus state inspection and time-travel debugging — Tom Piaggio (Autonoma, 2026-07-24). The piece's premise: official docs cover node tests briefly; the rest is scattered across version-specific posts, so this stitches the workflow once against current LangGraph.
- **Reference agent**: `StateGraph` with four nodes `classify_ticket → fetch_account_context → draft_response → (escalate | resolve)` compiled once with a checkpointer so every invocation is tied to `thread_id` (`src/graph.py`). Nodes are plain functions on state — no real model call needed for node isolation.
- **Runnable pyramid** `Autonoma-Tools/langgraph-testing`: `tests/test_node_isolation.py`, `tests/test_trajectory.py`, `tests/test_multi_turn_simulation.py`, `scripts/debug_replay.py` — all deterministic stand-ins, zero API keys, with CI wiring notes.
- **Core distinction**: graph-level correctness (right node produced right state, right path taken, right accumulation across turns) vs product-level correctness (queue page actually shows escalated, status widget updated, alert fired). The guide covers the first; Autonoma's behavioral E2E is positioned as the layer above the graph.

## Key Patterns / Techniques

| Layer | Pattern (from raw) | Assertion detail |
|-------|--------------------|------------------|
| **Node isolation** | Compile with static `interrupt_after=["fetch_account_context"]`, seed upstream state via `update_state(as_node="classify_ticket")`, resume `graph.invoke(None, config)`, assert via `graph.get_state(config)` | Tests exactly one node; nothing downstream executes; pure-function nodes need no LLM call; milliseconds per test |
| **Trajectory / route** | Recover executed node sequence via `graph.stream(stream_mode="updates")` or `graph.get_state_history(config)` (reverse most-recent-first) and compare list to expected path | Catches `add_conditional_edges` routing bugs (flipped comparison, string-vs-bool) that node tests never see; e.g., high-priority billing → `classify, fetch, draft, escalate` vs routine → `..., resolve` |
| **Multi-turn simulation** | Loop `graph.invoke` N times against same `thread_id` config; `graph.get_state(config)` reads accumulated state after last turn | Pin `temperature=0` where possible; assert on structure/invariants (final `status ∈ {escalated,resolved}`, escalation at most once, facts echoed exactly) not wording; reserve LLM-as-judge for semantic equivalence only |
| **State inspection** | `graph.get_state(config)` → current snapshot + `next`; `graph.get_state_history(config)` → full audit trail per thread | Same data that trajectory tests assert against, reused for debugging |
| **Time-travel replay** | Pick earlier checkpoint's `checkpoint_id` config, `graph.invoke(None, config)` resumes from there; optionally `update_state` on earlier checkpoint to fork with corrected input | Skips earlier nodes, re-executes downstream; for subgraph nodes pass `subgraphs=True` or only parent state is visible — common stall when subgraph state is never inspected |
| **Cost pyramid** | Node = ms/no LLM, Trajectory = one graph run, Multi-turn = seconds per turn (several LLM calls) | Shapes CI placement: node on every commit, trajectory on every PR, multi-turn smoke per PR + full suite nightly |

**Cheap-vs-expensive note**: LLM-as-judge as default assertion turns a fast deterministic test into a slow non-deterministic one grading another non-deterministic one — raw reserves it for the one semantic check that needs it.

## Relevance to QA/QE

| QA Concern | Action |
|------------|--------|
| **Routing bugs hide in edges** | Add trajectory list assertion per ticket class; node tests passing with wrong `conditional_edges` is the classic false-green |
| **Deterministic first** | Keep node functions pure where possible (state in → state out) so node isolation needs no model call and runs on every commit |
| **Invariant over wording** | In multi-turn, assert IDs/statuses exactly, statuses from fixed sets, escalation count ≤1; wording variance is expected, not a failure |
| **Subgraph blind spot** | If graph contains compiled subgraphs, always inspect with `subgraphs=True`; parent `get_state` alone hides subgraph internal state |
| **Flake triage** | Multi-turn variance at `temperature=0` can still come from retrieval/summarization/tool results — tighten persona and criteria before loosening threshold |
| **CI economy** | Node (commit) → trajectory (PR) → multi-turn 1-scenario smoke (PR) + full suite nightly; treat failing nightly as incident to triage same day |
| **Graph vs app gap** | Pair graph trajectory pass with behavioral E2E: escalated ticket actually in queue, customer widget updated, on-call alert fired — graph state dict claiming it is not proof |

## Critical Analysis

**Strengths:**
- Treats unit → trajectory → multi-turn → debugging as one connected workflow instead of four disconnected recipes; checkpointer is the connective tissue and the same API powers both tests and debugging.
- Concrete isolation recipe (`interrupt_after` at compile time + `update_state(as_node=upstream)` + `invoke(None)`) is non-obvious and repeatedly version-confused online — the guide nails the current correct form.
- Time-travel debugging section (fork with `update_state` before replay, `subgraphs=True` caveat) gives a genuinely actionable debugging path that most "how to test LangGraph" posts omit entirely.
- Cost table (ms vs one run vs seconds per turn) drives CI placement decisions correctly; LLM-as-judge restraint is the right default.

**Gaps:**
- Example graph uses deterministic stand-ins for model calls — variance sources that hit real LLM-backed nodes (sampling, tool choice branching, retrieval drift) are abstracted away inside the simulation section and not quantified.
- No coverage of persistence backends beyond the `InMemorySaver` warning (Postgres/SQLite needed in production, memory saver for tests only) — durability and cross-process sharing not exercised.
- CrewAI equivalence is noted (`crewai-evaluation` sibling) but porting details are delegated rather than shown.
- Error handling inside nodes (tool failure, timeout, retry) is not part of the trajectory assertions — delegated to simulation testing's failure-recovery pattern.

## Worked Example (from raw)

- **Graph**: `StateGraph` `classify_ticket → fetch_account_context → draft_response → escalate/resolve` via `add_conditional_edges` on priority; compiled with checkpointer and `thread_id` (`src/graph.py`).
- **Node isolation**: test `fetch_account_context` by compiling with `interrupt_after=["fetch_account_context"]`, `update_state(as_node="classify_ticket", values={category: "billing"})`, then `invoke(None, config)` and `get_state` asserts `account_context` populated — downstream `draft_response` never runs.
- **Trajectory**: run high-priority billing ticket, `get_state_history` yields `[classify_ticket, fetch_account_context, draft_response, escalate]`; assert equals expected; flipped boolean in `conditional_edges` would yield `resolve` and fail trajectory while node test stays green.
- **Multi-turn**: same `thread_id` over 3 turns — customer adds new info, agent re-classifies, final `status` asserted `escalated` and escalation count ≤1; wording variance ignored, IDs exact.
- **Time-travel**: `get_state_history` → pick checkpoint before `draft_response` → `update_state(category="technical")` → `invoke(None, that_config)` forks new timeline without re-running `classify_ticket`.

## FAQ Highlights (from raw)

- **What is LangGraph testing?** Three levels (node isolation via checkpointer, trajectory path assertion, multi-turn accumulation) plus state inspection/time-travel debugging — same checkpointer powers tests and debugging.
- **How to unit test one node?** Compile with `InMemorySaver` + `interrupt_after` (static at compile), `update_state(as_node=upstream)` to seed, `invoke(None)` to run exactly that node, `get_state` to assert.
- **How to check expected path?** `stream(stream_mode="updates")` node names or `get_state_history` reversed list, then list comparison.
- **How to debug wrong branch?** `get_state` for current snapshot + `next`; `get_state_history` for audit trail; replay from earlier `checkpoint_id` via `invoke`, optionally `update_state` to fork.
- **InMemorySaver in prod?** No — in-memory only, dies on restart, not shared; use Postgres/SQLite saver in production, memory saver is test/local only.

## Reuse Checklist

- Add `src/graph.py` pattern: compile once with `InMemorySaver` for tests; keep node functions pure (state in → changed fields out) so isolation needs no LLM.
- Copy `tests/test_node_isolation.py` template per node: compile-interrupt-seed-resume-assert; keep per-node file to avoid coupling.
- Add `tests/test_trajectory.py`: one test per ticket class with expected path list; run on every PR along with node tests.
- Add `tests/test_multi_turn_simulation.py`: fixed `thread_id` loop, `temperature=0` where model is behind node, invariants not wording; smoke 1 scenario per PR, full suite nightly.
- Keep `scripts/debug_replay.py` for on-call use: `get_state_history` → pick `checkpoint_id` → `update_state` → replay; document `subgraphs=True` for subgraph graphs.
- Pair graph pass with one behavioral check per decision — escalated ticket in queue page, widget updated, alert fired — graph dict is not proof.

## Cross-links

- CrewAI counterpart: [CrewAI Evaluation](autonoma-crewai-evaluation-2026.md) — same three-layer arc (isolate agent → verify routing → multi-turn), different seed/inspect APIs
- Tool calls: [Testing Tool Calls](autonoma-testing-tool-calls-2026.md) — tool-call sequence discipline applied to LangGraph nodes+edges
- Simulation harness: [Agent Simulation](autonoma-agent-simulation-2026.md) — three-actor harness generalizes the multi-turn simulation beyond LangGraph's thread model
- E2E arc: [How to Test an AI Agent E2E](autonoma-how-to-test-ai-agent-e2e-2026.md) — Stage 4 trajectory and Stage 5 behavioral mapping for graph agents
- Multi-agent: [Multi-Agent Handoffs](autonoma-multi-agent-handoffs-2026.md) — node routing as single-graph analog of cross-agent handoff correctness
- Memory: [Agent Memory](autonoma-agent-memory-2026.md) — `thread_id` persistence vs cross-session memory testing (fresh `thread_id` accumulation vs new thread probe)
- Regression: [Agent Regression](autonoma-agent-regression-2026.md) — N-run + tolerance pattern for graph nodes that call LLM
- Evidence: [AI QA Evidence Layer](ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md) — graph trajectory = eval; queue/dashboard state = downstream validation
- Deep dive: [LangGraph Testing raw](https://getautonoma.com/blog/langgraph-testing), [Agent Simulation Testing](https://getautonoma.com/blog/agent-simulation-testing)

*Ingested: 2026-08-31*
