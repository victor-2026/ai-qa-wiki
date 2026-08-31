# AI Agent Reliability Testing: Catching Silent Failures

**Source:** https://getautonoma.com/blog/ai-agent-reliability-testing
**Date:** 2026-07-24
**Tags:** #autonoma #reliability #silent-failures
**Raw:** [autonoma-ai-agent-reliability-testing-2026.md](../raw/autonoma-ai-agent-reliability-testing-2026.md)

---

## What It Is (3-5 bullets)

- **Reliability testing for LLM agents as a distinct discipline** (Autonoma, Tom Piaggio, 2026-07-24, refs `arxiv:2602.16666` Towards a Science of AI Agent Reliability and `arxiv:2603.02601` AgentAssay). Silent failure = agent returns plausible, confident, specific answer (correct order number, amount, timeline) that is actually wrong — final-answer grading (keyword, 9/10 helpfulness) is structurally blind to it.
- **Premise**: same input does not reliably produce same behavior due to 5 non-determinism sources; standard deterministic test (run once, assert equality) will both miss unreliable agents and flake on reliable ones. Testing must move from last message to full trajectory (tools, order, arguments, resulting state).
- **Runnable suite** `Autonoma-Tools/ai-agent-reliability-testing`: trajectory recorder (`trajectory_recorder.py`), baseline differ (`baseline_differ.py`), canary gate (`canary_gate.py`) — the three layers between "response looks right" and "action was right on the live app."
- **Five-layer stack** referenced: final-answer check → step-level assertions → trajectory comparison → behavioral baseline diff → canary rollout gate; each layer catches what the one below cannot. Autonoma's behavioral E2E (Planner reading routes/components, Execution driving PreviewKit, HealingAgent, DiffsAgent) extends beyond trajectory to live-app state.

## Key Patterns / Techniques (table or bullets)

| Source of Variance | Why it matters | What reliability suite does |
|--------------------|----------------|-----------------------------|
| **Sampling temperature** (>0 draws from distribution) | First token runner-up diverges trajectory | Trajectory-level assertions + baseline diff, not final text |
| **Model version drift** (silent update behind same alias) | Monday vs Tuesday behavior changes with zero code diff | Golden trajectory diff flags drift |
| **Tool-call ordering** (several valid tools per step) | Different first choice cascades | `assert_step_sequence` checks ordering invariants (lookup before mutating, mutating args reference prior lookup) |
| **Retrieval variance** (near-duplicate chunks, embedding drift) | Different context → different reasoning | Compare trajectory logs per scenario keyed by input |
| **Context-window truncation** (old turns dropped/summarized) | Lost constraint 3 steps back, no error | Structured append-only JSON log per run (input, every tool call + args+result, decision points, final action separate from final text) |

**Suite components (from raw):**
- **Trajectory recorder** (`reliability_suite/trajectory_recorder.py`): wraps tool calls, appends structured event (tool, args, result, timestamp), exposes `assert_step_sequence` — catches missing `refund_api.create` that text implied.
- **Behavioral baseline diff** (`baseline_differ.py`): run representative scenarios once under controlled conditions → golden trajectory (like visual regression reference screenshot); diff new run step-by-step. Reports 3 divergences separately: tools added/missing, arguments changed, final action category changed (last is paging-worthy). Small argument drift = warning; changed/missing terminal action = hard failure.
- **Canary + staged rollout** (`canary_gate.py`): percentage rollout (5%→25%→100%) with shadow runs (new version processes copy, no user-facing output, double inference cost) and automatic rollback tied to reliability metric (baseline-diff pass rate, hard-failure rate on terminal actions). Catches what offline baseline sampling missed.

Instrumentation minimum for a usable trajectory log: exact input (prompt/history/retrieved context), every tool call with full args+raw result, every decision between valid next steps, final action separate from final text, keyed by scenario+timestamp as JSON.

## Relevance to QA/QE (table QA Action)

| QA Concern | Action |
|------------|--------|
| **Silent refund bug** | Add step-level assertion that `refund_api.create` happened after lookup with correct args — final-answer grader will score 9/10 and miss it |
| **Drift without code change** | Build golden trajectory set per scenario; diff every run against baseline, treat model-alias update as expected drift source, not anomaly |
| **Diff triage thresholds** | Classify divergences: added/missing tool, argument change, final action change — warn on phrasing drift, fail on terminal action change |
| **Log discipline** | Enforce 4-field structured log (input, tool calls, decisions, final action vs text) as append-only JSON; without it, post-hoc diff is impossible months later |
| **Canary sizing** | Route 5% → 25% → 100%; run shadow traffic in parallel where risk warrants; auto-rollback on reliability regression without human dashboard watch |
| **Cost/latency as reliability signal** | Assertions can stay green while token spend doubles or latency +500ms — log and gate on those metrics separately |
| **Build order** | Recorder + step assertions (one afternoon) → baseline once you have >1 version → canary once real traffic is at stake; none replaces the others |

## Critical Analysis (Strengths/Gaps)

**Strengths:**
- Five-sources taxonomy makes non-determinism inspectable, not mystical; ties to academic framing (`Science of AI Agent Reliability`, `AgentAssay`) strengthens the trajectory-not-reply argument.
- Recorder → baseline diff → canary is a coherent, incremental build order with concrete files and thresholds (warning vs hard failure).
- Explicitly scopes Autonoma as live-app complement, not replacement for trajectory/retrieval/baseline — avoids "one tool fixes all."
- Diagram of 5 layers each catching what the one below cannot is an accurate mental model for layered defense.

**Gaps:**
- Golden-trajectory maintenance cost not quantified — every intentional prompt/tool change invalidates baselines; re-baselining workflow is deferred to DiffsAgent (product-specific).
- Representative scenario selection for baseline is unaddressed — sampling risk means canary is required but sampling strategy is not guided.
- No guidance on setting canary thresholds (pass-rate vs hard-failure rate) or shadow-traffic cost tolerance.
- Conversational multi-turn reliability explicitly out of scope and delegated to agent simulation testing (three-actor: simulator, agent, judge).

## Worked Example (from raw)

- **Silent failure opening:** refund agent says "Refund processed for order 4821, $42.00" — warm, specific, confident. Eval scores 9/10 helpfulness. But trajectory has no `refund_api.create` event — `assert_step_sequence` fails, final-answer check passes.
- **Baseline drift:** reference run 5 steps matched; new run after silent model-alias update changes step 4 arguments (same tool, different query phrasing) — differ flags argument change; final-answer wording unchanged so grader misses it.
- **Canary:** 5% traffic to new agent version shows baseline-diff pass rate 98% → 82% and hard-failure rate on terminal actions +3pp → gate halts at 5%, rolls back remaining traffic automatically before support queue sees it.
- **Instrumentation:** per-scenario JSON keyed `scenario: refund-4821, timestamp: 2026-07-24T10:00Z` containing prompt, history, retrieved chunks, tool calls with args+results, decision points, final action vs final text — enables diff months later.

## FAQ Highlights (from raw)

- Reliability testing = verifying correct sequence of actions across non-determinism, moving target from last message to full trajectory + state.
- Final answer not enough: can skip tool calls while sounding right; agent improves at sounding right, gap gets more dangerous.
- Log behavior as structured append-only JSON per run; diff two runs for tools added/args changed/final action changed.
- Canary rollout = 5%/25%/100% + shadow runs + auto-rollback on reliability regression.
- Each layer catches what the one below structurally cannot — build from cheapest (recorder) upward.

## Reuse Checklist

- Start with `trajectory_recorder.py` in one afternoon — wrap 2-3 critical tool calls, add `assert_step_sequence(["lookup", "refund_api.create"])` to catch silent skip.
- Create `baselines/golden/<scenario>.json` per representative input; add CI step `python baseline_differ.py --reference baselines/ --candidate runs/` with warning vs hard-failure thresholds.
- Log token count + latency per step in same JSON; add separate gates `tokens < baseline*1.2` and `p95_latency < 800ms` — green assertions can hide cost drift.
- Canary gate: start with 5% traffic, require `pass_rate >= 95% && hard_fail == 0` to promote; shadow run duplicate traffic where double inference cost is acceptable.
- Keep conversational reliability separate — delegate multi-turn to `agent-simulation-testing` (simulator, agent, judge) once single-trajectory suite is solid.

## Cross-links

- Tool calls: [Testing Tool Calls](autonoma-testing-tool-calls-2026.md) — same `assert_step_sequence` at single-agent granularity; trajectory recorder is the implementation
- E2E arc: [How to Test an AI Agent E2E](autonoma-how-to-test-ai-agent-e2e-2026.md) — reliability is Stage 4 (trajectory) + Stage 5 (behavioral) + Stage 6 (CI/canary) combined over time
- Multi-agent: [Multi-Agent Handoffs](autonoma-multi-agent-handoffs-2026.md) — silent drops and cascading errors are the multi-agent analogs of single-agent silent failures
- Memory: [Agent Memory](autonoma-agent-memory-2026.md) — truncation is shared variance source; memory persistence is the long-term reliability case
- Evidence: [AI QA Evidence Layer](ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md) — trajectory diff = model eval; live-app check = downstream validation; `offline-evaluation-trajectories-2026.md` for replay without live calls
- Deeper: [Agent Regression Testing](https://getautonoma.com/blog/agent-regression-testing), [Agent Simulation Testing](https://getautonoma.com/blog/agent-simulation-testing), [arXiv:2602.16666](https://arxiv.org/abs/2602.16666), [AgentAssay:2603.02601](https://arxiv.org/abs/2603.02601)

*Ingested: 2026-08-31*
