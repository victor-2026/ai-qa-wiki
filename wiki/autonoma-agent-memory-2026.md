# How to Test AI Agent Memory (Short- and Long-Term)

**Source:** https://getautonoma.com/blog/how-to-test-ai-agent-memory
**Date:** 2026-07-29
**Tags:** #autonoma #agent-memory #memory-testing
**Raw:** [autonoma-how-to-test-ai-agent-memory-2026.md](../raw/autonoma-how-to-test-ai-agent-memory-2026.md)

---

## What It Is (3-5 bullets)

- **Testing AI agent memory = verifying store, retrieve, and apply across sessions**, not just plausible replies. Framework from Tom Piaggio (Autonoma, 2026-07-29) covering 4 dimensions: within-session recall past distractors, cross-session persistence into a new thread, retrieval accuracy against decoys, and staleness (newer fact must override older).
- **Runnable Python/pytest suite** `Autonoma-Tools/how-to-test-ai-agent-memory`: persistent `memory_client.py` store + fresh-namespace helper + agent read/write interface; tests include `test_within_session_recall.py`, `test_cross_session_memory.py`, `test_retrieval_accuracy.py`, `test_context_carryover.py`.
- **Core distinction: memory ≠ context**. Context = what survives in the active window this conversation; memory = persistent storage (DB/cache/vector store) outliving window and session. Conflating them hides the Priya bug: greeting by name today, "who am I speaking with?" two days later in a new thread despite green single-conversation suite.
- **Behavioral threshold**: hardest check is not string containment but whether memory *changes behavior* (Free-plan user must not be offered enterprise-only action). Requires LLM-as-judge/rubric + downstream state check; that gap is where Autonoma's behavioral E2E layer is positioned.

## Key Patterns / Techniques (table or bullets)

| Dimension | Pattern (from raw) | Assertion detail |
|-----------|--------------------|------------------|
| **Within-session recall** | State fact, inject 3 distractor turns, assert reply carries fact semantically (not exact wording: "Tuesdays 2-4pm" vs "Tuesday afternoon 2 to 4" both correct) | `test_within_session_recall.py`; builds on multi-turn harness (`agent simulation testing`) |
| **Cross-session persistence** | Session A writes fact → tear down completely (no shared object) → Session B same `user_id`, fresh agent instance, read fact. Fresh object < fresh process < fresh browser+real DB | `test_cross_session_memory.py`; also asserts correct "I don't know" fallback for never-stored query |
| **Retrieval accuracy (decoy problem)** | Seed one correct + two similar decoys (e.g., three addresses), query for one, assert correct present AND decoys absent — second assertion catches "dumped whole memory into prompt" | `test_retrieval_accuracy.py`; no-memory case should not hallucinate |
| **Context carryover (behavioral)** | "I'm on Free plan" stored earlier → later request must withhold enterprise action; assert withholding + reason references plan tier | `test_context_carryover.py` — LLM-as-judge/rubric, not substring; paired with app-state check |
| **Staleness** | Write same key twice conflicting (Lisbon March → Berlin June), query July → assert only Berlin, not both | Store overwrites by key; retrieval suite already exercises it, asserted explicitly by name |
| **Non-determinism** | Semantic containment for free-phrased replies; exact-match only for hard values (order id, dollar); threshold 4/5 for variance-sensitive; flaky = assertion too strict or prompt ambiguous — tighten persona/rubric before loosening bar | Cross-cutting |
| **CI wiring** | Unit (within-session, retrieval, staleness) in main PR job vs integration (cross-session) in separate job against disposable per-run backend with fresh unique user_id per run (shared id → leftover pollution) | `.github/workflows/memory-tests.yml` |

Memory vs Context table from raw reproduced: what it is, where it lives, how it fails (write/retrieve vs truncation), how you test it.

## Relevance to QA/QE (table QA Action)

| QA Concern | Action |
|------------|--------|
| **Green suite with Priya bug** | Add cross-session test with genuine teardown; do not reuse in-memory state between sessions — only persistent store must connect them via `user_id` |
| **Decoy retrieval gap** | Require negative assertion (decoys absent) alongside positive; seed near-miss memories before trusting recall |
| **Behavior over words** | For plan/permission-gated actions, assert downstream state (action unavailable, upgrade path rendered, audit record) not just reply mentioning the plan |
| **Staleness as storage decision** | Write explicit overwrite test per key; treat as regression gate for storage-layer refactor |
| **Teardown strength ladder** | Prefer fresh process / fresh browser + real DB over fresh Python object; Autonoma-style preview environment is strongest (no accidental shared state) |
| **CI isolation** | Generate unique `user_id` per run; run cross-session against real disposable backend, not in-memory stub (stub survives teardown trivially and false-passes) |
| **Flaky triage** | On intermittent failure, first tighten stored fact / query / judge rubric phrasing; add K-of-N only for genuinely behavioral thresholds |

## Critical Analysis (Strengths/Gaps)

**Strengths:**
- Distinction memory vs context is clean and actionable; teardown-strength ladder (object < process < browser+DB) gives concrete false-pass model.
- Decoy negative assertion is the high-value insight most memory tests skip; staleness framed as explicit overwrite contract.
- Runnable repo with isolation helper (`fresh-namespace`) and CI split (unit vs integration) makes adoption paste-ready.
- Correctly escalates from text match to behavioral judge and then to application-state verification — three layers, not one.

**Gaps:**
- Vector-store specifics underplayed: embedding drift, top-k, chunking, hybrid search not detailed as retrieval variance sources.
- No guidance on retention/TTL, eviction policy, or privacy/PII scoping of long-term memory — left as storage-layer decision.
- Judge/rubric calibration for carryover not quantified; cost of 5x runs per behavioral check not budgeted.
- Single fact per session focus; multi-fact conflict resolution and partial updates across long histories not exercised.

## Worked Example (from raw)

- **Priya bug scenario:** Session 1: "Hey Priya, welcome back" — name stored. Session 2 (2 days later, new thread): agent says "I don't have your name on file" — suite that only tests fresh conversations stays green.
- **Within-session:** state "deploy window Tuesdays 2-4pm" → 3 distractor turns (weather, joke, unrelated task) → ask "when is deploy?" → semantic assertion passes on "Tuesday afternoon, 2 to 4" even though wording differs.
- **Cross-session:** Session A stores "deploy window Tuesdays 2-4pm" for `user_id=priya123` → teardown (new agent instance, no shared object) → Session B asks same → retrieval query must match via `user_id` not `session_id`; in-memory stub would false-pass.
- **Decoy:** store addresses `123 Main`, `123 Main St Apt 2`, `124 Main` → query "123 Main" → assert `123 Main` present AND `Apt 2` absent; catches full-dump-into-prompt bug.
- **Staleness:** March "I live in Lisbon" → June "I moved to Berlin" → July query → must be Berlin only; storage layer overwrites by key.
- **Carryover:** store "I'm on Free plan" → later "enable SSO" → judge rubric checks withheld + reason references plan tier; downstream check confirms enterprise action still disabled.

## FAQ Highlights (from raw)

- Test 4 dimensions: within-session, cross-session, retrieval vs decoys, staleness (newer wins).
- Memory is DB/cache/vector store, cross-session; context is live prompt, this conversation only; need different tests (see `how-to-test-multi-turn-conversations` for context).
- Long-term test = write tear down → new session same user_id → read + overwrite + many-similar-facts; run against real backend.
- If tests pass but user got wrong action → suite checks words not state; add product-state assertion.

## Reuse Checklist

- Use `memory_client.py` pattern: `store.write(user_id, key, value)` + `store.read(user_id, query)` + `fresh_namespace()` for isolation.
- Seed decoy set before every retrieval test — at least 2 near-miss values per correct one; assert decoys absent not just correct present.
- For cross-session, parameterize over `user_id` UUID per run; never share `memory` object between Session A and B.
- Add staleness test per mutable key (address, plan, location) — write v1, write v2, assert only v2 returned; run against disposable Postgres/Redis per CI job.
- For carryover, keep behavioral probe small: 1 plan-gated action, judge rubric `withheld==true && reason_contains_plan==true`, plus state check action unavailable.
- Keep memory prompts scoped by `user_id` not `session_id` — scoping bug is the most common cross-session failure in raw.

## Cross-links

- Trajectories: [Testing Tool Calls](autonoma-testing-tool-calls-2026.md) — trajectory logging is the context-window record; memory is the cross-session extension; [How to Test an AI Agent E2E](autonoma-how-to-test-ai-agent-e2e-2026.md) — Stage 2/3 evals complement memory checks
- Multi-agent: [Multi-Agent Handoffs](autonoma-multi-agent-handoffs-2026.md) — handoff contract across agents parallels memory handoff across sessions; same Pydantic/schema discipline
- Reliability: [Agent Reliability](autonoma-agent-reliability-2026.md) — behavioral baseline diff applies to memory-backed actions over time
- Evidence: [AI QA Evidence Layer](ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md) — memory recall = model eval; effect on product = downstream validation; `offline-evaluation-trajectories-2026.md` for trajectory replay
- Context window: [How to Test Multi-Turn Conversations](https://getautonoma.com/blog/how-to-test-multi-turn-conversations), [Agent Simulation Testing](https://getautonoma.com/blog/agent-simulation-testing)

*Ingested: 2026-08-31*
