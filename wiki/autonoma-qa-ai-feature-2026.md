# How to QA a Generative AI Feature Before You Ship

**Source:** https://getautonoma.com/blog/how-to-qa-an-ai-feature
**Date:** 2026-07-27
**Tags:** #autonoma #generative-ai #qa-strategy #ship-gate
**Raw:** [autonoma-qa-ai-feature-2026.md](../raw/autonoma-qa-ai-feature-2026.md)

---

## What It Is (3-5 bullets)

- **Six-step pre-ship gate as a gated sequence, not checklists**: tier by cost of a wrong output → eval set from real inputs → guardrail/red-team pass → behavioral E2E in the running app → staged rollout behind a kill switch → production monitoring that feeds back into the eval set (Tom Piaggio, Autonoma, 2026-07-27, repo `Autonoma-Tools/how-to-qa-an-ai-feature`).
- **Risk tier decides how much of the playbook is mandatory**: Cosmetic, Advisory, Actionable, Irreversible cover most features; cosmetic can stop after eval, irreversible cannot skip behavioral + rollout + monitoring even with strong eval numbers.
- **Runnable gate as one exit code**: `eval_suite/eval_runner.py` (N-run pass-rate + semantic vs exact), `eval_suite/redteam_runner.py` (adversarial subset), `ship_gate.py` (composes both, exits non-zero below threshold), `.github/workflows/ai-feature-gate.yml` on every PR touching the feature.
- **Closes the response-vs-action gap**: eval set grades the sentence; behavioral E2E checks the side effect the sentence was supposed to trigger (ticket status flipped, refund amount in DB, screen advanced) — the step most teams skip until prod.

## Key Patterns / Techniques (table or bullets)

| Step | What it does (from raw) | Mandatory for tier |
|------|-------------------------|--------------------|
| **1. Tier by cost of wrong output** | Cosmetic (blurb human-reviewed) / Advisory (suggestion, person decides) / Actionable (output triggers next action, auto-sent reply) / Irreversible (refund, delete, un-sendable message) | Tier is the gate — not a suggestion |
| **2. Eval set from real inputs** | Mine tickets/transcripts/logs (typos, half-sentences, 3-in-1 intents, post-return refund ask); run each case N times, assert pass-rate ≥4/5; exact for structured (amount, status, date), semantic/judge for free text sampled across runs | Mandatory for all tiers |
| **3. Guardrail + red-team pass** | After eval passes: injection/jailbreak/override attempts + data-exfiltration probes + faithfulness (stays grounded in context); reuse same pass-rate machinery on adversarial payload set | Advisory and above |
| **4. Behavioral E2E** | In running app: did ticket status change, did refund amount in DB match message, did UI advance — eval cannot see this; a correct sentence with wrong/missing side effect still passes eval | Actionable and Irreversible |
| **5. Staged rollout + kill switch** | Flag from day one, ramp 5%→25%→100% with dwell; rollback trigger decided before ramp (hard-failure rate on actionable outputs, support spike, metric threshold); switch flippable without deploy (flag service, not code boolean) | Irreversible (recommended for Actionable) |
| **6. Monitor + feed back** | Log input, model+prompt version, response, resulting action; human-sample production slice including non-flagged cases; alert on drift (tool-call success rate, length/tone, refusal rate); confirmed failure → new eval row | All tiers; growth loop |

Adversarial specifics delegated: `how-to-test-for-prompt-injection` for payload set + `how-to-test-ai-guardrails` for block vs over-block + `how-to-test-for-ai-hallucinations` for faithfulness — ordering matters (cooperative eval before red-team, red-team before behavioral).

## Relevance to QA/QE (table QA Action)

| QA Concern | Action |
|------------|--------|
| **"Looks good, ready to test?" with no sequence** | Replace ad-hoc try with six-step gate; cosmetic=stop after 2, irreversible=run through 6 — tier determines ceremony, not deadline pressure |
| **Synthetic 20-prompt eval set** | Borrow adjacent support queue data if feature has no traffic yet; mine real ugliness (typos, pasted walls) — synthetic misses the edge cases that reach prod |
| **Flaky eval on single run** | N-run sampling + semantic threshold; on flake decide: assertion too strict (vary phrasing) vs prompt ambiguous (underinstructed) — do not rerun to green |
| **Injection reaches running app** | Run guardrail pass before behavioral: blocking at response layer is cheaper than auditing a triggered action |
| **Sentence correct, action wrong** | Add one behavioral probe per actionable outcome (DB row, API field, email outbox, UI state) — the confirmation "ticket escalated" must have a flipped status field behind it |
| **Rollback needs a deploy at 2am** | Put kill switch in flag service; test flipping it before launch; if rollback needs PR+review+build, there is no kill switch |
| **Eval set frozen at launch** | Close loop: every confirmed prod failure becomes a new eval case; assign dataset owner and review cadence |

## Critical Analysis (Strengths/Gaps)

**Strengths:**
- Six steps as a gated sequence with tiered mandation makes "how much testing" an engineering decision, not a negotiation under deadline.
- Reuses N-run + semantic machinery for both normal and adversarial sets and composes them into one CI exit code — paste-ready gate.
- Behavioral distinction (response vs side effect) plus rollout/monitoring loop acknowledges sample ≠ whole input space.
- Correct sequencing: cooperative eval before adversarial before behavioral, with explicit references to deeper payload/guardrail/faithfulness guides.

**Gaps:**
- Red-team specifics summarized rather than shown — payload construction and guardrail-over-block trade-off left to separate guides.
- Staged rollout percentages (5/25/100) given as illustration without sizing guidance for traffic volume or dwell time needed to notice signal.
- Production sampling rate for human review ("meaningful slice") not quantified and no sampling strategy for high-volume features.
- Faithfulness checks called out as essential but not wired into `ship_gate.py` in the excerpt — implied rather than exited on.

## Worked Example (from raw)

- **Merged SLM/PR scenario:** support assistant / smart search / autofill draft — deterministic regression suite has nothing to say about it; gate is needed.
- **Tier mapping:** marketing blurb = Cosmetic → eval only; search ranking = Advisory → + red-team; auto-sent reply = Actionable → + behavioral; refund assistant = Irreversible → + rollout & kill switch.
- **Eval mining:** half-finished sentence, three intents in one message, refund about already-returned item — all real inputs that synthetic set would miss.
- **Behavioral catch:** assistant says "ticket escalated" with correct wording (eval pass) but ticket status never updated — behavioral query of ticket table catches it.
- **Ship gate composition:** `ship_gate.py` composes `eval_runner.py` + `redteam_runner.py` on each PR touching the feature and fails the check like a unit test when either drops below threshold.

## FAQ Highlights (from raw)

- Six-step gate: tier, real-input eval with N-run pass rate, guardrail/red-team (injection + faithfulness), behavioral E2E (state not sentence), flag + rollback trigger, drift monitoring feeding back into eval.
- Checklist that blocks release: eval pass rate ≥ threshold, red-team critical 0, behavioral green on staging/preview, rollback defined+tested, kill switch without deploy, monitoring wired.
- Handle non-determinism via N runs + pass-rate threshold + semantic/judge for free text; route flake to assertion vs prompt fix.
- Kill switch = flag-service toggle without code deploy, paired with pre-decided rollback trigger (failure rate or metric threshold), not decided mid-incident.

## Reuse Checklist

- Tier your feature using the 4-row table and record the mandatory steps in PR template — require waiver for skipped steps on Actionable/Irreversible.
- Build `eval_suite/eval_runner.py` with N=5 per case, `exact` scorer for fields `amount/status/date`, `similarity` for free text, threshold ≥ threshold from baseline.
- Copy `eval_suite/redteam_runner.py` pointing at `data/adversarial.jsonl` (injection, jailbreak, disclosure, faithfulness 10-20% of set) with same pass-rate machinery.
- Add behavioral probe: after feature action, query DB/API (ticket row, refund record) — one probe per irreversible side effect before adding browser coverage.
- Wire `ship_gate.py` + `.github/workflows/ai-feature-gate.yml` on `paths: [src/feature/**]`; test kill switch flip in staging before launch; log every prod action with input, model+prompt version, response, resulting state.

## Cross-links

- Non-determinism: [Non-Deterministic Outputs](autonoma-non-deterministic-outputs-2026.md) — strict vs ambiguous triage applied to eval flakes
- Unit layer: [LLM Unit Testing](autonoma-llm-unit-testing-2026.md) — per-prompt schema/similarity/judge before feature-level gate
- CI wiring: [LLM Evals in CI/CD](autonoma-llm-evals-cicd-2026.md) — merge+nightly two-speed pipeline + JSONL dataset that backs this eval set
- Streaming/UI dynamics: [Streaming Responses](autonoma-streaming-responses-2026.md) — lifecycle state machine for chat features within this gate
- Trajectories & actions: [Testing Tool Calls](autonoma-testing-tool-calls-2026.md) + [How to Test an AI Agent E2E](autonoma-how-to-test-ai-agent-e2e-2026.md) — trajectory vs behavioral outcome
- Reliability: [Agent Reliability](autonoma-agent-reliability-2026.md) — trajectory baseline diff + canary after ship
- Evidence layer: [AI QA Evidence Layer](ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md) — eval = model eval, guardrail = policy, telemetry = live
- Deeper guides: [Prompt Injection](https://getautonoma.com/blog/how-to-test-for-prompt-injection) + [Guardrails](https://getautonoma.com/blog/how-to-test-ai-guardrails) + [Hallucinations](https://getautonoma.com/blog/how-to-test-for-ai-hallucinations)
- Repo: [Autonoma-Tools/how-to-qa-an-ai-feature](https://github.com/Autonoma-Tools/how-to-qa-an-ai-feature)

## Reuse Notes

- Record rollback-trigger test in gate PR: demonstrate kill switch flip disables feature without deploy before marking gate green.

---
*Ingested: 2026-08-31*
