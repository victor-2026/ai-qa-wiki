# Source: https://getautonoma.com/blog/how-to-run-llm-evals-in-ci-cd

---
title: "How to Run LLM Evals in CI/CD"
description: "How to run evals in CI/CD: deterministic tests every commit, LLM evals at merge and nightly, N-run averaging, threshold gates, and a versioned dataset."
date: "2026-07-27"
canonical: "https://getautonoma.com/blog/how-to-run-llm-evals-in-ci-cd"
authors:
  - "Tom Piaggio"
tags:
  - "AI"
  - "Testing"
  - "LLM Evals"
---

# How to Run LLM Evals in CI/CD

> **LLM evals** are automated checks that score a model's output against a quality bar, correctness, faithfulness, tone, using a scoring function instead of an exact-match assertion, which is what separates them from a normal unit test. Running evals in CI/CD means splitting the pipeline into two lanes: fast, free, deterministic tests that gate every commit, and slower, token-costly eval tests that run on merge to main and nightly, scored by averaging several runs against a tolerance threshold instead of failing on any single miss.

> The full runnable pipeline from this article: a semantic-similarity plus groundedness scorer, an N-run averaging pytest suite gated on a stored baseline, a versioned JSONL eval dataset, and the GitHub Actions workflow splitting deterministic tests on every commit from evals at merge and nightly. Clone it and point it at your own feature. [Source on GitHub](https://github.com/Autonoma-Tools/how-to-run-llm-evals-in-ci-cd).

Ask a team if they run evals in CI and most say yes. Ask to see the job, and what shows up is one Python script, run by hand before a release, scored by someone eyeballing a spreadsheet of forty examples. Nothing gates a merge. Nothing runs on a schedule. Nobody would notice a five-point accuracy drop until a customer complained about it.

That gap, between "we run evals" and an actual CI gate, is the subject of this piece. What a deterministic test proves that an eval test cannot. Why the two need entirely different scheduling inside your pipeline. And how to wire a threshold gate that survives the fact that the same prompt against the same model can return a different string on every single call.

The first time I wired an eval suite into a merge queue, I made the obvious mistake: I ran the whole thing on every commit, the same way the rest of the test suite ran. It worked, for about a week, until a teammate opened a PR with six small commits pushed in an afternoon and the eval job burned through a token bill that would have paid for a month of the model API on its own. The fix wasn't a smarter model or a cheaper provider. It was admitting that an eval test and a unit test are not the same kind of check, and treating them like the same thing is what makes the bill hurt.

## What an LLM Eval Actually Tests (and Why a Unit Test Can't Do the Job)

A deterministic test in your existing suite asserts a fact about code: given this input, the function returns exactly this output, every time. An LLM eval asserts something softer: given this input, is the model's answer good enough, correct, grounded in the source material, on topic, appropriately toned, according to a scoring function rather than a string comparison. The two are catching different failure modes, and that's the whole reason they need to live in different parts of your pipeline.

An exact-match assertion can't do an eval's job because the same prompt against the same model rarely returns the same string twice. "The refund was processed" and "I've gone ahead and processed your refund" are both correct answers to the same support query, and a test that fails one of them because the words don't line up is a test your team will start ignoring within a sprint. An eval test replaces the string comparison with a scoring function: an [LLM-as-judge](https://arxiv.org/abs/2306.05685) call, a semantic-similarity check against a reference answer, a faithfulness check against retrieved context, or a rubric score, and it asserts that the score clears a threshold, not that the text matches a fixture.

[DeepEval](https://github.com/confident-ai/deepeval)'s own documentation gets closer to this than most of the search results on "how to run evals in CI/CD" do. Its `LLMTestCase` and `assert_test` primitives are a legitimate pytest-native way to express exactly this kind of threshold assertion, and its docs are one of the few places that explicitly recommends averaging three or more runs to absorb non-deterministic variance rather than trusting a single pass. Where that documentation stops short is the pipeline wrapped around those primitives: what runs on every commit versus what waits for merge, how the dataset backing those test cases gets versioned, and what the actual workflow file looks like end to end. That's the gap the rest of this piece fills in.

| Dimension | Deterministic test | Eval test |
| --- | --- | --- |
| What it asserts | Exact output or behavior | Score above a threshold |
| Speed | Milliseconds | Seconds per case |
| Cost | Free, no model call | Paid model tokens |
| Determinism | Same input, same output | Same input, varying output |
| When it runs | Every commit | Merge to main, nightly |

That last row is the spine of everything that follows. A deterministic test costs nothing to run on every commit, so it runs on every commit. An eval test costs a model call, real tokens, real seconds, real dollars, per case, and running the full eval suite on every keystroke would push your CI bill and your CI wait time in the wrong direction at the same time. The scheduling decision below isn't a nice-to-have. It's the difference between a pipeline that stays affordable and one that quietly gets disabled the first time someone notices the invoice.

> **Tests that check what your AI feature actually did.** Autonoma runs agentic end-to-end tests on every pull request. [Try Autonoma](https://autonoma.app).

## The Pipeline Pattern: Deterministic on Every Commit, Evals on Merge and Nightly

The pattern that holds up in practice is a two-speed pipeline. Deterministic tests, the ones checking your prompt-building code, your response parsing, your retry handling, your API schema, run on every single commit and every pull request, exactly like any other unit test suite. They're free and they're fast, so there's no reason to gate them any less aggressively than you'd gate a normal test.

Eval tests run on two triggers only: merge to main, and a nightly cron. Merge to main catches a deliberate change, a new prompt, a new model version pinned in config, a new retrieval source, before it reaches production. The nightly run catches the thing a merge trigger cannot: a model provider quietly rolling a new version behind the same API name, with no pull request and no commit for a merge hook to catch. Skip the nightly run and a silent provider-side regression sits undetected until a user notices. Skip the merge-gated run and a bad prompt edit ships straight to production, waiting for the next night's cron to flag it.

> **Diagram:** Two speeds, two triggers. Deterministic tests run on every commit and pull request. Eval tests run only on merge to main and on a nightly cron, both feeding the same threshold gate.

*Deterministic tests gate every commit. Eval tests gate two things only: a merge, and the clock.*

Worth being precise about what each stage actually proves. The eval job above scores whether the model's response clears a quality bar. It says nothing about whether that response, once it reaches your product, actually flips the right database row or renders the right screen, a gap [Autonoma](https://getautonoma.com) closes with a separate behavioral E2E layer that can run as its own gate further down the same pipeline.

## The GitHub Actions Workflow, Wired End to End

Here's what that two-speed pattern looks like as an actual pipeline, not a diagram. Two jobs, two triggers: `deterministic-tests` runs on every push and pull request, and `llm-evals` runs on push to main plus a nightly `schedule:` cron, with a `workflow_dispatch` trigger so anyone can kick it off by hand before a release.

[.github/workflows/evals.yml](https://github.com/Autonoma-Tools/how-to-run-llm-evals-in-ci-cd/blob/main/.github/workflows/evals.yml)

The eval job's last step is a reporting script, not the raw pytest output. Pytest tells you which assertions failed. It doesn't summarize the run for a teammate skimming a failed check three days later, and it won't exit with a clean non-zero code when the aggregate score has regressed even if every individual case still limps over its own threshold. Here's that script: it runs the suite, computes the averaged score per case, compares each average against a stored baseline file, and fails the job the moment any case regresses past its tolerance.

[scripts/run_evals.py](https://github.com/Autonoma-Tools/how-to-run-llm-evals-in-ci-cd/blob/main/scripts/run_evals.py)

## Where Autonoma Fits in an LLM Eval Pipeline

LLM evals answer whether a response clears a quality bar. Autonoma covers the next gate: whether that response caused the correct result in the running product. Its Planner reads the code paths a feature touches and plans behavioral test cases for a live preview environment; its Executor drives the real UI and asserts on the resulting state, such as a record update, navigation, or side effect. Run that behavioral gate beside the eval jobs when a model response can trigger an action, and let Diffs Agent keep the affected coverage current as the application changes.

## Threshold Gating: Averaging Runs So Noise Doesn't Fail Your Build

A single eval run is not a reliable signal, and treating it like one is the fastest way to make a team stop trusting the suite. Call the same model with the same prompt five times and the score will typically wobble, not because anything regressed, but because sampling temperature, token-level randomness, and small phrasing differences move a similarity or judge score by a few points in either direction on their own. Fail the build on any single low run, and you'll be re-running CI by hand within a week. Keep that up, and the team starts merging past red checks on principle.

The fix DeepEval's own docs get right, and that most teams skip anyway: run each case N times, average the score, and compare the average against a baseline minus a tolerance band, never any individual run against an exact target. Three runs is a floor. Five is a comfortable default for anything that isn't prohibitively expensive to call repeatedly. A tolerance of 0.05 to 0.1 on a 0-to-1 scale absorbs normal sampling noise without absorbing a real regression, since a genuine drop tends to drag every one of the N runs down together, not just one of them.

Exact match versus semantic similarity is the other half of this. Scoring "the refund was processed" against "I've processed your refund" with a string comparison manufactures a failure out of a correct answer. Scoring the same pair with an embedding-similarity or LLM-as-judge comparison against a reference answer correctly calls it a pass. If a case turns out flaky under this setup, meaning it passes on some runs and fails on others even at N=5, the honest read is one of two things: either the assertion is too strict for the range of correct phrasings the model can produce, or the prompt itself is ambiguous enough that the model's answer legitimately varies in substance, not just in wording. Both are real bugs. Neither one is in your code.

> **Diagram:** One bad run is noise. Five bad runs is a regression. Two panels of five scored runs each. In the first, four runs score high and one is a low outlier, and the average still clears the threshold, a pass. In the second, all five runs score low together, and the average falls below the threshold, a fail.

*Same five-run average, same threshold. One scenario is sampling noise. The other is a real drop.*

Here's the scorer that folds a semantic-similarity check and a groundedness check into one float, so the threshold comparison downstream has a single number to work with:

[src/scorer.py](https://github.com/Autonoma-Tools/how-to-run-llm-evals-in-ci-cd/blob/main/src/scorer.py)

And here's the pytest suite that calls it: one test per dataset case, five invocations per test, one averaged assertion against the stored baseline and tolerance:

[tests/test_evals.py](https://github.com/Autonoma-Tools/how-to-run-llm-evals-in-ci-cd/blob/main/tests/test_evals.py)

Notice what this test does not do. It never asserts that a single run matches a target exactly, and it never fails on one below-average outlier on its own. Non-determinism gets absorbed by the average. A real regression, consistent across all five runs, still gets caught, because there's nowhere for it to hide once five numbers are being averaged instead of one noisy one being trusted on its own.

## Storing and Versioning the Eval Dataset

An eval suite is only as good as the dataset it runs against, and the most common way teams sabotage their own pipeline is pasting golden answers straight into the test file, where nobody outside the person who wrote them can review a change to one. Treat the dataset the way you'd treat a database migration: a versioned file in the repo, reviewed in a pull request, with a schema everyone on the team actually understands.

A workable schema is small on purpose: an id, the input, a reference answer or grounding context, and the tags a case needs, which query type it represents, which past regression it was added to catch. Store it as JSON Lines, one case per line, so adding a new case is a one-line diff and a reviewer can see exactly what changed without a data-tooling detour.

[data/eval_dataset.jsonl](https://github.com/Autonoma-Tools/how-to-run-llm-evals-in-ci-cd/blob/main/data/eval_dataset.jsonl)

Golden-answer drift is the maintenance cost nobody budgets for. A reference answer written against last quarter's product copy, last quarter's pricing, or last month's policy becomes wrong in a way that has nothing to do with the model, and a stale reference will flag a perfectly correct answer as a regression indefinitely, until someone happens to catch it. Give the dataset an owner, review it on the same cadence you'd review any other test fixture, and treat "is this reference still true" as its own checklist item whenever the product copy it's testing against changes.

New cases should come from two sources, not one. Some get written up front, covering the query types the product is known to handle. The rest should come from production: a support escalation, a confusing transcript, a case where the model gave a confident but wrong answer. Turn each of those into a dataset row with the correct reference answer attached, and the eval suite grows in the direction your actual users are pushing it, instead of only covering what someone imagined at design time. A dataset that only ever grows from the design phase stops testing the failure modes that show up once real traffic hits the feature.

None of this replaces the harder problem one layer up: nothing here tells you whether an agent kept the same tool-call decision it made last week, only that a fixed set of eval cases still scores where it should. If what you actually need to catch is drift after a silent model update rather than a general quality bar, [agent regression testing](/blog/agent-regression-testing) is the pattern built specifically for that, golden trajectories instead of golden answers, and the same N-run averaging idea applied to a tool-call sequence instead of a text score.

The prompt-level unit tests this pipeline gates on every commit, the deeper non-determinism patterns underneath the averaging above, and the guardrail and prompt-injection tests worth running alongside your evals are each their own piece; this one is about the CI wiring that ties all of them into a single pipeline. Add [Autonoma](https://getautonoma.com) when that pipeline also needs to verify the user-visible action and application state a passing model response produced.

## Frequently Asked Questions

## Frequently Asked Questions

### How do you run evals in CI/CD?

Split the pipeline into two lanes. Deterministic tests (prompt building, response parsing, retries, schema checks) run on every commit and pull request because they are free and fast. The LLM eval suite runs on merge to main plus a nightly cron, since each case costs paid model tokens and seconds. Each eval case runs N times (five is a common default), the scores are averaged, and the average is compared against a stored baseline within a tolerance band rather than failing on any single low run.

### What are LLM evals?

LLM evals are automated tests that score a model's output against a quality bar, such as correctness, faithfulness to a source document, or tone, using a scoring function like semantic similarity or LLM-as-judge instead of an exact-match assertion. They differ from unit tests because the thing being checked is a graded quality, not a fixed, reproducible output.

### How do you build custom evals for an AI product?

A minimal eval framework needs four pieces: a versioned dataset of input/reference-answer pairs stored as reviewable files, a scoring function that grades a fresh response against the reference (semantic similarity, faithfulness, or an LLM-as-judge call), a runner that executes each case multiple times and averages the score, and a CI job that gates a threshold check on merges and a nightly schedule rather than every commit.

### How do you make AI testing reproducible if the model's output changes every run?

You don't force the output itself to be reproducible. You run each test case multiple times (five is a common default), average the score across those runs, and compare the average against a baseline within a tolerance band. A single run is not a reliable signal; an averaged score absorbs normal sampling noise while still catching a genuine, consistent regression.

### How do you score LLM responses automatically?

Replace exact string matching with a scoring function: embedding-based semantic similarity against a reference answer, a faithfulness or groundedness check against retrieved context, or an LLM-as-judge call that rates the response against a rubric. The score is compared to a threshold rather than to an exact string, since correct answers can be worded many different ways.

### Should LLM eval tests run on every commit like unit tests?

No. Eval tests call a paid model and take seconds per case, so running the full suite on every commit is slow and expensive. Run deterministic tests (parsing, retries, schema checks) on every commit, and run the LLM eval suite on merge to main plus a nightly cron, which catches both deliberate prompt or model changes and silent provider-side model updates.

---

This is the markdown variant of <https://getautonoma.com/blog/how-to-run-llm-evals-in-ci-cd>, served by content negotiation (`Accept: text/markdown`) and also available directly at <https://getautonoma.com/md/blog/how-to-run-llm-evals-in-ci-cd>.

Other agent surfaces: [llms.txt](https://getautonoma.com/llms.txt), [resource catalog](https://getautonoma.com/.well-known/ai-catalog.json), [developer portal](https://getautonoma.com/developers), [sitemap](https://getautonoma.com/sitemap.xml).
