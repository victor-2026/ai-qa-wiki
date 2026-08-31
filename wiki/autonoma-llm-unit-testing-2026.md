# LLM Unit Testing: Writing Tests for Your Prompts

**Source:** https://getautonoma.com/blog/llm-unit-testing
**Date:** 2026-07-27
**Tags:** #autonoma #llm-unit-testing #prompt-testing #promptfoo #deepeval
**Raw:** [autonoma-llm-unit-testing-2026.md](../raw/autonoma-llm-unit-testing-2026.md)

---

## What It Is (3-5 bullets)

- **Prompt as a unit of code**: fast, framework-native tests against one prompt's output inside pytest (or Promptfoo YAML), living beside app tests, running on every commit — distinct from broad eval suites with aggregated scoring and nightly trends (Tom Piaggio, Autonoma, 2026-07-27).
- **Ladder of three assertion types in strict preference order**: deterministic schema and string checks where contract is exact, semantic similarity where correct answers vary in wording, LLM-as-judge only for the residual open-ended quality nothing cheaper can express.
- **Runnable project** `Autonoma-Tools/llm-unit-testing`: versioned prompt fixture `prompts/summarize_ticket/v3.yaml` with golden cases, Pydantic schema checks, must-contain/must-not-contain, similarity with calibrated threshold, judge with explicit rubric at temperature 0, mocked logic tier, Promptfoo and DeepEval configs side by side, three-tier CI workflow.
- **Prompt fixtures as versioned files**: one file per version, loaded by tests; a wording edit becomes a diff reviewed with its golden cases and a CI result in the same PR — catches the ticket-summarizer bug (tightened sign-off sentence silently dropped account ID for ~50% inputs) before a support engineer does.

## Key Patterns / Techniques (table or bullets)

| Assertion / Practice | When to use (from raw) | File in repo |
|----------------------|------------------------|--------------|
| **Schema (Pydantic) validation** | Prompt asks for JSON with required fields/types; catch omitted field that loose `"id" in response` would miss | `tests/test_structured_output.py` |
| **Must-contain / must-not-contain strings** | Field present but wrong: empty account ID, missing disclaimer, reintroduced boilerplate; cheaper than embedding, more specific than "looks fine" | `tests/test_string_assertions.py` |
| **Semantic similarity** | Explain build failure in user's words — dozen correct phrasings exist; must-contain is too strict or too loose; embedding cosine vs reference + threshold calibrated empirically | `tests/test_semantic_similarity.py` |
| **Threshold calibration** | Run known-good reference answers against golden inputs, look at score distribution, set floor just below worst true positive — not a round 0.8 guess; domain-specific | Inline in similarity helper |
| **LLM-as-judge hygiene** | Tone, helpfulness, engagement — only when no schema or single reference; pin judge model by name/version, temp 0, explicit rubric ("3-4 criteria"), not "rate 1-5" | `tests/test_llm_judge.py` |
| **Versioned prompt fixture** | `prompts/<name>/v3.yaml` + golden cases traveling together; edit → diff + test result; intentional behavior change updates golden in same commit | `prompts/summarize_ticket/v3.yaml` |
| **Promptfoo vs DeepEval** | Promptfoo: declarative YAML, matrix many variants fast, CLI eval; DeepEval: pytest-native, metrics as assertions, alongside other pytest files | `promptfooconfig.yaml` vs `tests/test_deepeval_metrics.py` |
| **Three-tier CI split** | Mocked logic every commit (free, ms), small live golden set every PR (bounded cost), full eval nightly (broad, paid once/day) | `tests/test_prompt_logic_mocked.py` + `.github/workflows/test.yml` |

Decision tree from raw: exact schema/substring → deterministic → correct answer varies → similarity → open-ended quality → judge. Judge is most expensive/slow/least deterministic — last choice every time.

## Relevance to QA/QE (table QA Action)

| QA Concern | Action |
|------------|--------|
| **Prompt edit broke field silently** | Require must-contain on account-id pattern and Pydantic required fields — story's six-day lag would have failed on first commit |
| **Reaching for judge on first test** | Ask if contract is deterministically testable first; only after schema/string ruled out, use similarity; only after similarity insufficient, use judge |
| **Threshold guessing** | Calibrate per prompt: run golden inputs → distribution → floor below worst true positive; re-calibrate when domain or embedding model changes |
| **Prompt lives in vendor UI or inline string** | Extract to versioned file with golden cases; PR must show wording diff + golden update + test result as one reviewable unit |
| **Suite too slow/expensive for CI** | Mock template rendering/parsing/budget/retry paths with fake model response — no live call; gate real calls to PR golden set + nightly full |
| **Model provider updated under you** | Re-run golden suite against new version before adoption; pin judge version separately so judge doesn't drift with system under test |

## Critical Analysis (Strengths/Gaps)

**Strengths:**
- Correctly orders assertions by cost/determinism and gives an explicit decision rule; mocks-first CI tier keeps suite on every commit rather than weekly guilt run.
- Versioned fixture + golden co-change turns prompt engineering into reviewable engineering, not judgment call.
- Side-by-side Promptfoo vs DeepEval mapping helps teams pick by existing harness, not hype; notes neither replaces assertion types.

**Gaps:**
- Similarity ceiling acknowledged (fluent wrong answer can score high on cosine) but not paired with a concrete faithfulness check for numeric/factual fields in the same suite.
- Judge calibration (agreement rate, threshold, rubric versioning) and embedding-model selection not quantified; cost of judge on borderline cases not budgeted.
- Golden drift maintenance (product copy, pricing, policy aging) referenced only as "update in same commit" — no ownership or review cadence.
- No guidance on golden set size per prompt beyond "a handful" — risk of under-covering distinct behaviors.

## Worked Example (from raw)

- **Ticket summarizer v2→v3:** one sentence added to stop sign-off padding → no linter or schema failed → account ID extraction dropped for ~50% of tickets for six days.
- **Pydantic catch:** `account_id: str` required in schema → empty or missing ID fails `test_structured_output.py` even though JSON valid.
- **String catch:** `must_contain("Account: ")` + pattern would have failed the tightened prompt on first commit, before support noticed.
- **Fixture flow:** bump `prompts/summarize_ticket/v3.yaml` → golden cases parameterized automatically → PR shows diff of wording and expected behavior together.
- **CI gate:** mocked parsing tests run on every commit in ms; 4-5 golden cases hit real model on PR; full matrix runs nightly on schedule.

## FAQ Highlights (from raw)

- Most contracts are deterministically testable — schema + presence/absence cover more than teams assume; judge is residual.
- Prompt unit test = one prompt, handful of cases, fast, in normal suite; eval = larger set, aggregated scoring, regression thresholds, separate pipeline.
- Keep prompt version + golden set together; treat wording edit as diff that must pass cases before merge.
- Split tiers: mocked (every commit), golden PR (small, paid), full nightly (broad); neither Promptfoo nor DeepEval proves the feature did the right thing in the app.

## Reuse Checklist

- Extract one prompt to `prompts/<feature>/v1.yaml` with `goldens: [{input, expected_fields, reference_answer}]`; parametrize pytest from the file.
- Add Pydantic model per structured output; fail on missing/incorrect type, not just key presence; add two string assertions (must-contain, must-not-contain) per prompt.
- For variable wording, add similarity test with threshold set from actual golden distribution, not 0.8 — record calibration snippet in helper docstring.
- Keep judge file `tests/test_llm_judge.py` gated to ≤1 case per prompt; pin `judge_model: gpt-4o-2026-05-13` (example) and version rubric in `rubrics/`.
- Wire `.github/workflows/test.yml` with three triggers as in repo; ensure mocked job is required, eval jobs are PR/nightly only.

## Cross-links

- Non-determinism deep dive: [Non-Deterministic Outputs](autonoma-non-deterministic-outputs-2026.md) — K-of-N patterns underlying prompt tests
- Pipeline: [LLM Evals in CI/CD](autonoma-llm-evals-cicd-2026.md) — dataset, scoring aggregation, threshold gate, nightly drift catch
- Tool calls: [Testing Tool Calls](autonoma-testing-tool-calls-2026.md) — assertions that do not touch final text
- E2E arc: [How to Test an AI Agent E2E](autonoma-how-to-test-ai-agent-e2e-2026.md) — Stages 2-3 are this layer; Stages 4-5 prove the action
- Feature gate: [QA a Generative AI Feature](autonoma-qa-ai-feature-2026.md) — feature-level gate consuming this unit layer
- Streaming: [Streaming Responses](autonoma-streaming-responses-2026.md) — fake-server mocks parallel mocked-logic mocks here
- Evidence: [AI QA Evidence Layer](ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md) — response score vs downstream validation
- External: [Promptfoo](https://www.promptfoo.dev/docs/intro/) + [DeepEval](https://docs.confident-ai.com) + pillar [Testing Generative AI Applications](https://getautonoma.com/blog/testing-generative-ai-applications)
- Repo: [Autonoma-Tools/llm-unit-testing](https://github.com/Autonoma-Tools/llm-unit-testing)

## Reuse Notes

- Keep unit tests next to app tests in `tests/` so prompt changes share the same PR gate as code changes.

---
*Ingested: 2026-08-31*
