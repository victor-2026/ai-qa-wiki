# Anthropic: Demystifying Evals for AI Agents (Jan 2026)

**Source:** Mikaela Grace et al., Anthropic Engineering, 2026-01-09. Full text read via guest fetch (no raw file — vendor primary). Vendor-employed voice; banked as method, not endorsement.

## Vocabulary (locks our terms)

- **task** = single test + success criteria; **trial** = one attempt (run many — outputs vary); **grader** = scoring logic (assertions/checks); **transcript/trace/trajectory** = complete record (outputs, tool calls, reasoning); **outcome** = final environment state (reservation in SQL, not "flight booked" said); **evaluation harness** = runs evals end-to-end; **agent harness/scaffold** = what makes a model an agent (evaluating "an agent" = harness + model); **suite** = task collection.

## Three grader types

| Grader | Strengths | Weaknesses |
|---|---|---|
| Code-based (string match, fail-to-pass, lint/type/security, outcome + tool-call verification) | fast, cheap, objective, reproducible | brittle to valid variation, no nuance |
| Model-based (rubrics, NL assertions, pairwise, reference, multi-judge) | flexible, nuance, open-ended | non-deterministic, needs human calibration |
| Human (SME, crowds, spot-checks, A/B, inter-rater) | gold standard, calibrates judges | expensive, slow |

Scoring: weighted / binary / hybrid. Prefer deterministic where possible, LLM where necessary, human judiciously.

## Capability vs regression (+graduate rule)

Capability evals ("what can it do well?") start at LOW pass rate — a hill to climb. Regression evals ("does it still?") stay near 100%. High-pass capability evals **graduate** into the regression suite ("can we still do this reliably?").

## pass@k vs pass^k (pick by product)

- **pass@k** (≥1 success in k): rises with k — for tools where one success matters.
- **pass^k** (all k succeed): falls with k — for customer-facing consistency (75%³ ≈ 42%).
- At k=1 identical; by k=10 opposite stories.

## 0–8 roadmap (condensed)

0. Start early: 20–50 real-failure tasks suffice (large effect sizes). 1. Convert manual checks + bug-tracker failures. 2. Unambiguous tasks + reference solutions (two experts → same verdict; 0% pass@100 = broken task, not incapable agent). 3. Balanced sets (test should AND shouldn't — one-sided evals breed one-sided agents). 4. Isolated stable env per trial (shared state inflates or correlates; git-history leakage observed). 5. Grade product not path (tool-call-sequence checks too brittle — creativity punished); partial credit; calibrate judges + "Unknown" way out; cheat-resistant graders. 6. Read transcripts (failures must seem fair). 7. Watch saturation (SWE-Bench 30%→80%; Qodo one-shot missed Opus 4.5 gains). 8. Living suite with owners; eval-driven development (capability evals before the model can pass).

## Methods stack (Swiss-cheese)

Automated evals (pre-launch/CI) + production monitoring (ground truth, reactive) + A/B (slow, causal) + user feedback (sparse, real) + transcript review (weekly sampling) + human studies (calibration). No single layer catches everything. Frameworks: Harbor, Braintrust, LangSmith, Langfuse, Arize (tasks matter more than tooling).

## Corroborations inside

- Opus 4.5 CORE-Bench 42%→95% after grader/scaffold fixes (rigid "96.12" vs "96.124991", ambiguous specs) — matches Huang preview datum; measurement-bug class confirmed by vendor.
- τ-bench/τ2-bench (user-simulator + state checks); BrowseComp (easy-verify/hard-solve); WebArena (backend-state, not confirmation-page); OSWorld (artifacts).
- Opus 4.5 τ2 flight-booking "failure" that was a better user solution — eval-beats-rubric case (grade the outcome, allow appeal).

## QA interpretation

- **Outcome-over-transcript** is our effect-over-claim doctrine, vendor-stated (SQL row, not "booked" said).
- **Graduate rule** gives regression suites a principled source (climbed hills become guards).
- **Grade-product-not-path** constrains trajectory-evals (our delegation-routing stance, same doctrine).
- **0%-pass@100 = broken task** is the falsifiability gate for eval authors — seeder-side thinking.
- **Eval-driven development** (evals before capability) = our pre-registration in vendor words.

## See also

- [[arbiter-prompt-interference-mason-2026]] — cheat-resistant graders
- [[aqef-seeded-controls-spec-2026]] — oracle proves itself every run
- [[anthropic-claude-code-expertise-2026]] — same-house expertise study
- [[kenhuang-maestro-google-control-roadmap-2026]] — control mapping
