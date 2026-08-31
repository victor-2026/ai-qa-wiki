# Agent Regression Testing: When Your Agent Breaks Without a Deploy

**Source:** https://getautonoma.com/blog/agent-regression-testing
**Date:** 2026-07-24
**Tags:** #autonoma
**Raw:** [autonoma-agent-regression-testing-2026.md](../raw/autonoma-agent-regression-testing-2026.md)

---

## What It Is

- **Agent regression testing = re-running a fixed set of golden trajectories against every model, prompt, or KB change and flagging an averaged score drop** — Tom Piaggio (Autonoma, 2026-07-24). No deploy event exists to trigger it; the LLM provider can swap the model behind the same API name mid-week with no changelog your CI watches.
- **Motivating incident from raw**: support-routing agent (billing / technical / account-access / escalate-to-human) held 93% routing accuracy for 6 weeks, then dropped to 71% with an empty deploy log — billing tickets mis-routed to technical queue due to silent provider model update.
- **Core insight**: a single agent run is non-deterministic, so one pass/fail is noise. The suite runs each golden case N times (5 is the raw's starting point), averages the score, and gates on `average >= baseline - tolerance` (0.05 tolerance band suggested).
- **Runnable harness referenced**: `Autonoma-Tools/agent-regression-testing` — `src/capture_baseline.py` (golden capture), `src/scorer.py` (structural + similarity scorer), `tests/test_regression.py` (N-run pytest), `.github/workflows/agent-regression.yml` (threshold gate).
- **Scope boundary made explicit**: trajectory-level regression (decision + wording vs baseline) is a different verification problem from application-state regression (did `route_to_queue("billing")` actually move the ticket in the dashboard). The harness covers the first; Autonoma's behavioral E2E covers the second.

## Key Patterns / Techniques

| Pattern | What it does | Detail from raw |
|---------|--------------|-----------------|
| **Golden trajectory** | Record of one input + full tool-call sequence + final output at a human-verified "good" moment | Capture shape, not just outcome: `classify_intent → route_to_queue("billing")` + confidence, not just "routed to billing"; stored as JSON next to tests (`src/capture_baseline.py`) |
| **Structural + similarity scorer** | Two measurements folded into one float 0-1 | Tool-call sequence = exact structural match; final text = embedding / string-similarity / LLM-as-judge; `src/scorer.py` combines both so threshold gate has one number |
| **N-run averaging** | Absorbs run-to-run noise | 5 runs, averaged; one low run barely moves average; genuine regression drags all 5 down; `tests/test_regression.py` — one test per golden case, N invocations, one averaged assertion |
| **Threshold gate** | One averaged number, one gate | Baseline minus tolerance (0.05); no individual run decides outcome alone |
| **CI wiring: nightly + on-change** | Covers both failure sources | Nightly cron → catches silent provider swap; path-filtered trigger on model config / prompt templates / KB docs → catches deliberate edits; running only one leaves a gap |
| **Golden-set lifecycle** | Habit, not one-off | New intent → new golden case; deliberate prompt change → human re-checks baselines before re-trusting; golden set reviewed like a schema migration in PR |

**Why exact-match fails**: same prompt → different phrasing every call; exact-match flakes on correct paraphrases and trains the team to ignore the test within a month (raw). Reference to AgentAssay (arXiv 2603.02601): compare structured execution traces, not raw text, cheaply enough to run continuously.

## Relevance to QA/QE

| QA Concern | Action |
|------------|--------|
| **Silent model drift with no code diff** | Schedule regression suite nightly + on prompt/KB/model-config change; do not wire only to merge/deploy hook |
| **Flaky non-deterministic assertions** | Replace single-run pass/fail with 5-run average vs baseline minus tolerance; treat one outlier as noise, not failure |
| **Tool vs text correctness** | Score tool-call sequence structurally (ids, queue names) and text via similarity/judge; never grade only the words around the decision |
| **Baseline quality** | Capture golden trajectories while behavior is verified by a human; check JSON baselines into repo and review additions/updates in PR like migrations |
| **Two-layer verification gap** | Pair trajectory regression (did agent pick right tool) with behavioral E2E (did ticket status actually flip in admin dashboard / queue counts) — trajectory diff cannot see app-state break |
| **CI cost** | 5x runs per case is the cheapest insurance; nightly + filtered PR runs cost minutes vs weeks of mis-routed tickets |
| **Diagnosis** | On failure, inspect drop shape: uniform across all N = regression; one outlier = scorer strictness or paraphrase variance |

## Critical Analysis

**Strengths:**
- Diagnoses a real gap most teams miss — regression with no deploy to blame — and anchors it in a concrete 93→71 incident with a reproducible empty deploy log narrative.
- Gives a complete, vendor-neutral runnable harness with four concrete files (capture, scorer, pytest, workflow) instead of prose-only guidance; switching model/provider means swapping the agent callable, not rewriting the pattern.
- Non-determinism handling is disciplined: exact structure for tools + similarity for text, N-run averaging, tolerance band — avoids both the exact-match flake trap and the looser-threshold blind spot.
- CI scheduling advice is specific and justified: two triggers for two failure modes, with explicit cost of skipping either one.

**Gaps:**
- Embedding / LLM-as-judge choice for the similarity half is not evaluated (model, threshold, cost, calibration vs human labels).
- Golden-trajectory maintenance at scale (dozens of intents, evolving prompts) — re-baselining workflow, storage growth, and review load — is named as a habit but not quantified.
- No guidance on setting the tolerance band empirically (0.05 is a starting point; real threshold needs per-suite variance data over weeks).
- Application-state layer is correctly scoped out but remains product-specific (Autonoma PreviewKit); hand-rolled alternative for that layer is not sketched.

## Worked Example (from raw)

- **Capture**: run support-routing agent on labeled ticket "My invoice shows double charge" while routing is at 93%; `capture_baseline.py` writes JSON with input, `classify_intent(billing, 0.94)`, `route_to_queue("billing")`, and final reply text.
- **Score**: fresh run after provider swap calls `route_to_queue("technical")` — structural half fails immediately; even if it had called billing, paraphrased reply still passes similarity half, so scorer isolates decision regressions from wording variance.
- **N-run**: 5 fresh runs all score ~0.71 vs baseline ~0.93; average 0.72 triggers `0.72 < 0.93 - 0.05` → gate fails. Single outlier run at 0.88 alone would not have failed the averaged gate.
- **CI gate**: GitHub Actions runs `agent-regression.yml` nightly at 03:00 UTC plus on PRs touching `prompts/**`, `kb/**`, `model-config.yaml`; failure posts Slack alert same day instead of silent queue buildup.
- **Two-layer proof**: trajectory suite proves agent still picks billing; Autonoma layer proves ticket status flips to `routed: billing` in dashboard and technical queue count drops — second check would still catch a later endpoint rework that the trajectory suite would not see.

## FAQ Highlights (from raw)

- **What is agent regression testing?** Re-running golden trajectories (input + tool sequence + output from known-good runs) against every model/prompt/KB update and flagging averaged score drop; no deploy event to hook into.
- **Why did accuracy drop without a deploy?** Silent model update behind same API name — deploy-triggered gate never fires; need nightly + path-filtered triggers.
- **What is a golden trajectory?** Recorded baseline of one correct run: input, full tool calls with args/results, final text — decision path, not just final label.
- **How to test non-deterministic outputs?** 5 runs, structural match for tools + similarity for text, average vs tolerance band; single low outlier is not failure.
- **How often to run?** Nightly for provider swaps + PR-triggered for prompt/KB/config changes; running only one leaves either gap open.

## Reuse Checklist

- Copy `src/capture_baseline.py` and run once per labeled case while agent is verified-good; commit JSON baselines alongside tests.
- Adapt `src/scorer.py` to your tools: exact compare for function names/queue enums, similarity/judge for free text; keep scorer threshold versioned.
- Add `tests/test_regression.py` pattern: one test per golden file, `N=5`, `tolerance=0.05`; start there and tune from variance data after 2 weeks of nightlies.
- Wire `.github/workflows/agent-regression.yml` with `schedule: cron 0 3 * * *` plus `paths: [prompts/**, kb/**, model-config.yaml]`; fail job and notify.
- Seed at least one golden per queue/category plus one escalate-to-human; add new golden whenever a new intent ships.
- Pair suite with one behavioral check per mutating tool — dashboard/query that route actually landed — so trajectory pass does not mask app-state break.

## Cross-links

- E2E arc: [How to Test an AI Agent E2E](autonoma-how-to-test-ai-agent-e2e-2026.md) — regression is Stage 6; broader pyramid context for when response-level vs trajectory vs behavioral checks apply
- Reliability: [Agent Reliability](autonoma-agent-reliability-2026.md) — extends golden-trajectory diff to live drift (baseline diff + canary) over time; shares non-determinism sources
- Trajectory: [Testing Tool Calls](autonoma-testing-tool-calls-2026.md) — structural tool-call assertions reused inside scorer
- Simulation: [Agent Simulation](autonoma-agent-simulation-2026.md) — multi-turn complement where N-run + judge pattern also applies
- Multi-turn: [Multi-Turn Conversations](autonoma-multi-turn-conversations-2026.md) — context-window truncation as another silent-change source needing same gate
- Evidence layer: [AI QA Evidence Layer](ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md) — trajectory score = model eval; dashboard state = downstream validation
- Memory/context: [Agent Memory](autonoma-agent-memory-2026.md) — memory store drift is another silent-change source that needs same nightly gate
- Deep dive: [Agent Regression Testing raw](https://getautonoma.com/blog/agent-regression-testing), [LLM Evals in CI/CD](https://getautonoma.com/blog/llm-evals-ci-cd), [Reliability Testing](https://getautonoma.com/blog/ai-agent-reliability-testing)

*Ingested: 2026-08-31*
