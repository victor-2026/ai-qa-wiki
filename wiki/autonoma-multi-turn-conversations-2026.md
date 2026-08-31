# How to Test Multi-Turn Conversations and Context Retention

**Source:** https://getautonoma.com/blog/how-to-test-multi-turn-conversations
**Date:** 2026-07-29
**Tags:** #autonoma
**Raw:** [autonoma-multi-turn-conversations-2026.md](../raw/autonoma-multi-turn-conversations-2026.md)

---

## What It Is

- **Testing multi-turn conversations = verifying state holds correctly across many turns in one session, not just that any single reply is correct** — Tom Piaggio (Autonoma, 2026-07-29). Response-level evals check a reply given the transcript; these tests check whether the transcript itself survived.
- **Three failure modes tested separately**: (1) topic-switch-then-return coreference break (Maya/7, turns 3-11 distractors, turn 14 "she" → must still resolve to Maya), (2) context-window overflow truncation boundary (confident confabulation vs graceful degrade), (3) long-conversation drift over 20-60+ turns (persona, instruction, commitment decay) — runnable repo `Autonoma-Tools/how-to-test-multi-turn-conversations`.
- **Harness seam**: same three-actor shape as agent simulation — `send(conversation, message)` appends user turn, calls chat client with full history, appends reply; `Conversation` + `pinned_facts` fixture + `lib/judge.py` boolean/scored questions replace exact text match — `lib/harness.py`, `tests/conftest.py`.
- **Core distinction: in-window retention ≠ persistent memory** (table in raw). Retention = current session's token window, dies on session end; memory = durable store survives sessions. Multi-turn tests cover the first column; [how-to-test-ai-agent-memory](https://getautonoma.com/blog/how-to-test-ai-agent-memory) covers the second. Passing one says nothing about the other.
- **Explicit app gap**: a booking bot can hold Maya perfectly across 14 turns and still leave reservation unchanged — transcript coherent, app state wrong. Harness asserts on conversation; Autonoma behavioral E2E asserts on product (passenger count, credit, ticket owner) and Diffs Agent keeps scripted conversations aligned per PR.

## Key Patterns / Techniques

| Failure mode | Pattern (from raw) | Assertion |
|--------------|--------------------|-----------|
| **Topic-switch-then-return** | Establish fact → 3 unrelated turns → probe with pronoun, not restatement | Judge checks meaning still resolves to original referent; two correct replies can share no words — string match fails by design — `tests/test_topic_switch_return.py` |
| **Context-window overflow** | Pad conversation with filler turns past actual truncation threshold, then probe pinned fact | Two allowed outcomes: remembered OR gap acknowledged; failure = confidently invented substitute; fix is pinned-facts layer — short summary re-injected every turn regardless of truncation — `tests/test_context_window_overflow.py` |
| **Long-conversation degradation** | Score every turn against same invariant; track trend; assert score doesn't regress past threshold as length grows + separate self-contradiction check | Action-level drift (constraint at turn 3 stops applying at turn 40) needs check on account/state, not transcript — transcript judge scores prose as fine — `tests/test_long_conversation_degradation.py` |
| **Harness reuse** | `Conversation` object, `send()` seam, `pinned_facts` fixture, `lib/judge.py` helper | All tests build on same fixtures so they drop into any agent server / hosted API / SDK without rewriting |
| **Flakiness handling** | Assert invariants never exact wording; run N times, require pass rate (5 runs, 4 pass floor); prefer judge/similarity over string; `temperature=0` is start, not guarantee | Compounding flake math: 98% per-step × 6 steps ≈ 89% all-green; three causes for flake — assertion too strict, prompt ambiguous, or strategy genuinely non-deterministic |
| **CI placement** | Topic-switch + overflow (cheap, handful of turns) per PR with reruns; long-conversation (40+ turns × judge calls) nightly | Budget judge calls: 40-turn × 1 invariant = 40 extra model calls beyond conversation itself; gate on suite-level pass rate, not single flake |

**Where each fails**: truncation strategy "drop oldest first" drops the most important turn (what user actually wanted) — mature fix is pinned-facts summary, not longer window.

## Relevance to QA/QE

| QA Concern | Action |
|------------|--------|
| **Turn-14 Maya bug escapes turn-by-turn grading** | Add topic-switch-then-return test per coreference that must survive distractors; assert via judge on pronoun resolution, not substring |
| **Truncation invents a fact** | Pad to real threshold in test; gate on "remembered OR acknowledged gone" — block merges that silently confabulate; add pinned-facts layer for the handful of facts that must never drop |
| **Gradual drift invisible to end-of-run check** | Score every turn against invariant; assert trend not just final answer; add self-contradiction check against earlier commitments |
| **Action vs answer drift** | Pair long-conversation pass with product-state check: same 40-turn replay drives running app and asserts passenger count / credit / constraints, not just reply prose |
| **Retention vs memory confusion** | Keep multi-turn suite (this page) and cross-session memory suite separate — green on one must not be reported as coverage of the other; memory needs close-session → fresh user_id probe |
| **Flake triage** | On failure, first tighten assertion strictness and prompt specificity; only then adjust pass bar; log truncation/summarization as variance sources even at temperature 0 |
| **Maintenance** | Scripted conversations are long, hand-built, and easy to trust on reputation — review on every prompt/flow change; Autonoma Diffs Agent pattern is the automated version of that review |

## Critical Analysis

**Strengths:**
- Topic-switch-then-return scenario (Maya at turn 2 → refund/baggage/seats 3-11 → "she" at 14) is a crisp real-world anchor that makes coreference testing unmistakably concrete; the "every reply defensible alone, conversation broken" framing is the right diagnostic.
- Overflow section names the right failure (confident invention, not forgetting) and the right fix (pinned-facts re-injected summary, not just longer window), with an explicit flawed default (drop-oldest) called out.
- Long-conversation trend assertion (score every turn vs threshold + contradiction check) correctly distinguishes step-function from gradual decay — single end check would miss it.
- Practical flakiness math (98% → 89% over 6 steps) and three-cause heuristic give a triage checklist that prevents the "just add retries" habit.

**Gaps:**
- No quantified truncation thresholds or strategies compared (summarization vs drop vs pinned-facts performance); pinned-facts itself is sketched, not measured for recall vs window trade-off.
- Long-conversation judge cost (40+ extra calls per scenario) is budgeted qualitatively; pass-rate threshold for "drift is real" vs noise is not derived from data.
- Voice or multi-modal turns not covered; all examples are text chat — additional variance sources for speech transcription states not considered.
- Coverage guidance for how many topics/distractors or how long a "long" suite should be (20 vs 60 vs 100 turns) is heuristic, not risk-based.

## Worked Example (from raw)

- **Maya bug**: turn 2 "I'm booking for my daughter Maya, she's 7" → turns 3-11 refund windows, baggage, seat selection (distractors) → turn 14 "can she bring a friend?" → bot answers "who is she?" — every single reply graded alone was defensible; failure exists only at conversation level.
- **Topic-switch test**: `tests/test_topic_switch_return.py` establishes pin, inserts 3 unrelated turns, probes pronoun; judge checks resolution to Maya, not wording — "she can bring a friend if listed" and "yes, one additional passenger on Maya's booking" both pass.
- **Overflow test**: `tests/test_context_window_overflow.py` pads past truncation threshold, probes pinned fact; allowed outcomes remembered OR acknowledged gone; failure is confident invention (e.g., invented age 9). Pinned-facts re-injection is the fix over drop-oldest.
- **Degradation test**: `tests/test_long_conversation_degradation.py` scores every turn against invariant ("stop using bullet points", persona, prior commitment); 40-turn run must not regress past threshold; self-contradiction checked separately. Constraint at turn 3 applied at turn 40 needs product-state check — transcript judge sees fine prose, account shows unwanted credit.
- **Harness seam**: `lib/harness.py` `Conversation` + `send(conversation, message)` + `pinned_facts` fixture — same code drives own agent server, hosted API, or wrapped SDK.

## FAQ Highlights (from raw)

- **How to test multi-turn?** Script with user simulator, run vs system, assert invariants via judge not exact text; test coreference, overflow, long-drift separately.
- **What is context window testing?** Pad filler turns until truncation/summarization threshold crossed, probe pinned fact; pass if remembered or acknowledged gone, block if invented substitute.
- **How to test long-conversation drift?** Score every turn vs invariant, assert no regression with length; single end check misses gradual decay.
- **Retention vs memory?** Retention = current token window, dies on session end; memory = durable store survives sessions — need different tests; passing one says nothing about other.
- **Tests pass but users say bot didn't do it?** Transcript layer proven; app layer missing — drive running app and assert on product state (passenger count, credit) not reply.

## Reuse Checklist

- Copy `lib/harness.py` + `tests/conftest.py`: `Conversation`, `send()` seam, `pinned_facts` fixture, `lib/judge.py` boolean/scored helper — thin fixtures, fresh conversation per file.
- Add `tests/test_topic_switch_return.py` per coreference that must survive — one pin per test, 3 unrelated distractors, pronoun probe, judge on referent.
- Add `tests/test_context_window_overflow.py`: pad to real threshold (measure yours), probe, assert remembered-or-acknowledged, add pinned-facts re-injection for must-not-drop facts.
- Add `tests/test_long_conversation_degradation.py`: score every turn vs invariant, threshold on trend + contradiction; pair with one product-state invariant per action that mutates state.
- CI: topic-switch + overflow per PR with reruns; long suite nightly (40 turns × judge calls = expensive); gate on suite pass rate, not single flake; budget ~40 extra judge calls per 40-turn scenario.
- Review scripted conversations on every prompt/flow change — long, hand-built, easy to trust on reputation; Diffs Agent pattern automates that review.

## Cross-links

- Foundation harness: [Agent Simulation](autonoma-agent-simulation-2026.md) — three-actor pattern (simulator, adapter, judge) that this suite extends for retention
- Memory counterpart: [Agent Memory](autonoma-agent-memory-2026.md) — cross-session store/retrieve/staleness vs in-window retention (this page); same teardown-strength ladder applies
- LangGraph binding: [LangGraph Testing](autonoma-langgraph-testing-2026.md) — `thread_id` accumulation and `get_state_history` as framework-specific retention surface
- Reliability: [Agent Reliability](autonoma-agent-reliability-2026.md) — context-window truncation as one of five non-determinism sources; trajectory + baseline diff for drift
- CrewAI: [CrewAI Evaluation](autonoma-crewai-evaluation-2026.md) — multi-turn at crew orchestration layer; delegation carries context that this suite's pins mirror
- E2E arc: [How to Test an AI Agent E2E](autonoma-how-to-test-ai-agent-e2e-2026.md) — multi-turn is Stage 4/5 at conversation scope; Stage 5 behavioral maps to product-state gap
- Regression: [Agent Regression](autonoma-agent-regression-2026.md) — nightly + on-change gate for prompt/window changes that break retention
- Evidence: [AI QA Evidence Layer](ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md) — transcript verdict = eval; booking state = downstream validation
- Deep dive: [How to Test Multi-Turn Conversations raw](https://getautonoma.com/blog/how-to-test-multi-turn-conversations), [How to Test AI Agent Memory](https://getautonoma.com/blog/how-to-test-ai-agent-memory)

*Ingested: 2026-08-31*
