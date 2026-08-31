# Source: https://getautonoma.com/blog/llm-unit-testing

---
title: "LLM Unit Testing: Writing Tests for Your Prompts"
description: "LLM unit testing with runnable code: schema and string assertions, semantic similarity thresholds, LLM-as-judge, prompt fixtures, and fast CI tiering."
date: "2026-07-27"
canonical: "https://getautonoma.com/blog/llm-unit-testing"
authors:
  - "Tom Piaggio"
tags:
  - "Testing"
  - "AI"
  - "LLM Testing"
---

# LLM Unit Testing: Writing Tests for Your Prompts

> **LLM unit testing** means writing fast, code-based tests against a single prompt's output: schema and string assertions where the contract is exact, semantic-similarity checks where a correct answer's wording varies, and an LLM-as-judge only for open-ended quality nothing cheaper can express. It differs from a full eval suite by living inside your existing test framework, running on every commit, and costing close to nothing once the model call itself is mocked for the logic tests.

> A runnable pytest project implementing every assertion type in this guide: a versioned prompt fixture with golden cases, Pydantic schema checks, must-contain and must-not-contain string assertions, a semantic-similarity test whose threshold is calibrated from data instead of guessed, an LLM-as-judge test with an explicit rubric at temperature 0, a mocked logic tier that runs in milliseconds with no network, side-by-side Promptfoo and DeepEval configs, and the three-tier CI workflow that ties them together. [Source on GitHub](https://github.com/Autonoma-Tools/llm-unit-testing).

A teammate tightened the system prompt on our ticket-summarizer three weeks ago. One sentence, meant to stop the model from padding summaries with a sign-off nobody asked for. It shipped clean: no linter complaint, no schema violation, nothing red in CI, because nothing in CI touched that prompt at all. Six days later a support engineer noticed the summarizer had quietly stopped extracting the account ID out of roughly half its inputs. The JSON was still valid. The output still read like a summary. It was just wrong, in the one field the rest of the pipeline actually depended on.

That gap wasn't a model problem. It was a test problem, and a solvable one. Most write-ups on "testing your prompts" stop at vague advice: version your prompts, write eval sets, watch for drift. Almost none of them show the actual test file. This one does. Every assertion type below runs as real code, checked into a repo, executed in CI, no platform sign-up required.

## What's Actually Testable in a Prompt (and What Isn't)

Treat an LLM call like a black box and every test becomes a vibe check: run it, read the output, decide if it looks right. That's not a test suite, it's code review with extra steps. The fix isn't giving up on assertions, it's matching the assertion to what the prompt's contract actually guarantees.

Ask a model for JSON with four required fields and you have a hard, deterministic contract: the response either has those four fields with the right types or it doesn't. That's schema validation, no fuzzier than testing any other API response. Ask it to explain a concept back in the user's own words and there's no single correct string, but there is a reference answer whose meaning the response has to land near: that's a semantic-similarity check with an explicit threshold. Ask it to write a comforting reply to an upset customer and there's no schema and no single reference answer worth measuring distance from: that's the narrow band of cases where an LLM-as-judge actually earns its cost.

Far more of a prompt's contract is deterministically testable than most teams assume. If you're reaching for an LLM judge on your very first test, you're probably testing the wrong thing, or you haven't looked hard enough for the hard constraint hiding inside a soft-looking prompt.

> **Diagram:** A decision tree for choosing a prompt assertion type: exact schema or substring leads to a deterministic check, a correct answer with varying wording leads to a semantic similarity check, and open-ended quality leads to an LLM-as-judge check.

*Most of a prompt's contract is deterministically testable. Reach for semantic similarity only when correct answers genuinely vary in wording, and for an LLM judge only when neither cheaper check can express what you're checking.*

## Deterministic Assertions First: Schema and String Checks

Start here, because it's the cheapest, fastest, and least contested assertion type available. If the prompt asks for JSON, validate the JSON: not with a loose `"id" in response`, with a real schema, required fields, correct types, no silently-optional field creeping in because the model omitted it and nothing complained.

Here's a [Pydantic](https://docs.pydantic.dev/latest/) model doing exactly that against a structured summarization response, plus the test that exercises it:

[tests/test_structured_output.py](https://github.com/Autonoma-Tools/llm-unit-testing/blob/main/tests/test_structured_output.py)

Schema checks alone won't catch every regression, though. A field can be present, correctly typed, and still wrong: an account ID that's an empty string, a summary that dropped a disclaimer it was required to keep. That's what must-contain and must-not-contain assertions are for: checking the raw text for markers cheaper than a schema and more specific than "looks fine to me," the field pattern you require, the boilerplate that was mistakenly reintroduced. This is, incidentally, the exact class of bug from the opening story. A must-contain assertion on the account-id pattern would have caught it on the very first commit, six days before a support engineer had to.

[tests/test_string_assertions.py](https://github.com/Autonoma-Tools/llm-unit-testing/blob/main/tests/test_string_assertions.py)

> **Test what the answer actually did.** Autonoma runs agentic end-to-end tests on every pull request. [Try Autonoma](https://autonoma.app).

## Semantic Assertions for When Wording Varies

Not every prompt has a fixed correct string. Ask a model to explain why a build failed in plain language and there are a dozen acceptable phrasings of the same correct answer. A must-contain check here is either too strict (it demands one phrasing) or too loose (it just checks for a keyword and lets nonsense through as long as the keyword shows up). What you want is a check on meaning: does the response land near a reference answer in embedding space, regardless of exact wording.

That means picking a similarity threshold, and picking it by guessing is how semantic tests turn into the flakiest tests in the suite. Do it empirically instead: run your known-good reference answers against your golden inputs, look at the actual score distribution you get back, and set the floor just below the worst true positive, not above some round number that felt safe.

[tests/test_semantic_similarity.py](https://github.com/Autonoma-Tools/llm-unit-testing/blob/main/tests/test_semantic_similarity.py)

Be honest about the ceiling here too. A fluent, confident, on-topic answer that's factually wrong will often score just as high on cosine similarity as a correct one, because similarity measures closeness in meaning-space, not truth. Semantic checks catch paraphrase drift and answers that wandered off-topic. They do not catch a wrong number stated with the same confidence as a right one. That's a faithfulness problem, not a phrasing problem, and it deserves its own dedicated testing pass.

## LLM-as-Judge for What Nothing Cheaper Can Catch

An LLM judge is the most expensive, slowest, and least deterministic assertion type available, and it should be your last choice on every test case, not your first. It adds a full model call, plus its own latency, plus its own token cost, plus a nonzero flakiness rate, since even a judge run at temperature zero can drift call to call on genuinely borderline cases. Reach for it only when the property you're checking has no schema and no single reference answer worth measuring distance from: tone, helpfulness, whether the response actually engaged with what the user asked instead of talking past it.

The decision rule in practice: if a deterministic or semantic check could express what you're testing, write that instead, every time. A judge earns its cost only on the residual, the handful of properties a schema can't encode and an embedding score can't distinguish. Budget for it accordingly. Most suites need a judge on a small fraction of their cases, not most of them.

When you do reach for a judge, treat judge hygiene as non-negotiable: pin the judge model explicitly by name and version, so it doesn't silently improve or regress underneath you the way the model you're testing might. Run it at temperature zero. And give it an actual rubric, explicit scoring criteria written into the prompt, not "rate this response 1 to 5," which is a request for a plausible-sounding number, not a measurement.

[tests/test_llm_judge.py](https://github.com/Autonoma-Tools/llm-unit-testing/blob/main/tests/test_llm_judge.py)

## How Autonoma Tests the Layer Above Your Prompt Tests

Every assertion above, schema, string, similarity, judge, checks one thing: what the model said. None of them can see whether that response actually did the right thing inside the running application, whether it triggered the correct UI state, the right navigation, the right downstream write. That's the moment a fully green test suite and a broken feature coexist, and it's a different layer of testing than anything in this guide.

[Autonoma](https://getautonoma.com) sits at exactly that layer. Its Planner reads the codebase to plan behavioral test cases against the running app, and its Executor drives the real UI to confirm the response actually produced the correct outcome, not just the correct text.

## Prompt Files as Versioned Test Fixtures

Everything above assumes a prompt file exists somewhere the test suite can load it from. That assumption does a lot of quiet work, and it's worth making explicit, because most teams don't actually structure it this way yet.

Prompts belong in version-controlled files, one file per version, not inlined as a string inside application code and not living only in a vendor's prompt-editing UI. Loaded as a fixture, a prompt edit becomes a reviewable diff in a pull request: the reviewer sees exactly what changed in the wording, and the test suite attached to that same file tells them, in the same CI run, whether the edit regressed anything.

Here's a versioned prompt fixture, structured as data rather than code, with its own golden case set traveling alongside it:

[prompts/summarize_ticket/v3.yaml](https://github.com/Autonoma-Tools/llm-unit-testing/blob/main/prompts/summarize_ticket/v3.yaml)

The golden cases inside that file aren't an afterthought, they're the whole point of putting the prompt in its own file at all. Bump the version, edit the wording, and the test suite parameterizes over the file automatically. If the golden cases still pass, the edit is safe. If a change is intentional, meaning the new prompt is supposed to produce a different kind of answer, update the golden cases in the same commit as the prompt edit. The pull request diff then shows both changes together, what the prompt now says and what "correct" now means, reviewed as one unit instead of a wording change nobody double-checked against behavior.

> **Diagram:** A versioning flow showing a prompt edit producing a git diff of wording and golden cases together, loaded by the test suite as a fixture, and shown in the pull request as a diff and a test result together.

*A prompt versioned as a fixture turns an edit into a reviewable diff with a test result attached, instead of a wording change nobody checked against behavior.*

## Prompt Testing Tools: Promptfoo vs DeepEval, Side by Side

Two tools cover most of this ground off the shelf, and they're built around different mental models, not different quality tiers. [Promptfoo](https://www.promptfoo.dev/docs/intro/) is config-first: you declare prompts, test cases, and assertions in YAML, and it's built to matrix-test many prompt variants against many inputs fast, without hand-writing a test harness. [DeepEval](https://docs.confident-ai.com) is pytest-native: prompt tests live as functions inside your existing Python test suite, with its metrics (answer relevancy, faithfulness, and others) used as assertions you call directly.

Neither replaces the assertion types above. Both are ways to run them with less boilerplate.

| Dimension | Promptfoo | DeepEval |
| --- | --- | --- |
| Config style | Declarative YAML | Python, pytest-native |
| Best for | Matrix-testing many variants fast | Living inside an existing test suite |
| Assertion style | Built-in graders in config | Metrics used as assertions |
| Test location | Separate from app code | Alongside other pytest files |
| CI integration | CLI eval command | Standard pytest run |

Here's a Promptfoo config running the same summarizer prompt across multiple test cases with built-in graders:

[promptfooconfig.yaml](https://github.com/Autonoma-Tools/llm-unit-testing/blob/main/promptfooconfig.yaml)

And here's the same idea from the DeepEval side, as a pytest file using its metrics directly as assertions:

[tests/test_deepeval_metrics.py](https://github.com/Autonoma-Tools/llm-unit-testing/blob/main/tests/test_deepeval_metrics.py)

Pick based on where your team already lives. A QA-heavy team running large prompt-variant matrices reaches for Promptfoo. A team that already has a Python test suite and wants prompt tests sitting next to everything else reaches for DeepEval. Both are worth trying against a single prompt before you commit either one across your whole suite.

## Keeping the Suite Fast Enough to Run in CI

None of this matters if the suite is too slow or too expensive to actually run. The fix is a strict split: mock the model for anything that's really testing your code, not the model, and only hit a real model for the small subset that's actually testing the prompt.

Template rendering, variable interpolation, token-budget checks, output parsing, error handling when the model returns malformed JSON: none of that needs a live API call. It needs a fake model response and an assertion on what your code did with it, and it should run in milliseconds:

[tests/test_prompt_logic_mocked.py](https://github.com/Autonoma-Tools/llm-unit-testing/blob/main/tests/test_prompt_logic_mocked.py)

That test never touches a real model and never will, which is exactly why it can run on every single commit without anyone thinking twice about cost.

The tiering that makes this sustainable in practice: mocked logic tests on every commit (free, instant, no excuse not to run them constantly), a small live-model eval subset on every pull request (the golden cases from the fixture file, a handful per prompt, real cost but bounded), and the full eval suite nightly on a schedule (broader coverage, paid once a day instead of on every push). Here's that split as a GitHub Actions workflow:

[.github/workflows/test.yml](https://github.com/Autonoma-Tools/llm-unit-testing/blob/main/.github/workflows/test.yml)

> **Diagram:** A three-tier CI split for prompt tests: mocked logic tests triggered on every commit with no model calls, a small set of live golden cases triggered on every pull request at bounded cost, and the full eval suite triggered on a nightly schedule for broad coverage.

*Three triggers, three costs. Mocked logic tests run free on every commit, a small live golden set gates every pull request, and the full eval suite runs once nightly instead of on every push.*

This is where a prompt unit test suite hands off to a full eval pipeline. This guide stops at "assert this prompt does X." A complete CI eval pipeline, test data management, scoring aggregation, regression thresholds across a whole suite, trend tracking over time, is its own discipline, covered in our guide to [running LLM evals in CI/CD](/blog/how-to-run-llm-evals-in-ci-cd). Wire that in once the unit layer here is solid, not before. If you're still hitting flaky results at this layer, our deep dive on [testing non-deterministic AI outputs](/blog/how-to-test-non-deterministic-ai-outputs) covers the K-of-N patterns these assertions rely on in more depth than this guide has room for, and our broader [guide to testing generative AI applications](/blog/testing-generative-ai-applications) is the pillar page this one hangs off of.

Three assertion types, in order of preference, and two practices that hold them together: schema and string checks first because they're cheap and stable, semantic similarity when wording genuinely varies, an LLM judge only for the residual nothing cheaper can express, all of it versioned as fixtures so a prompt edit is a diff with a test attached, and a CI tier that keeps the whole thing fast enough to run on every commit instead of once a week out of guilt. None of it proves the response did the right thing inside your actual application (that's the layer [Autonoma](https://getautonoma.com) tests directly), but it proves something upstream of that: the words the model produced were the words your contract required. Ship the two together and a bad prompt edit gets caught in CI, not by a support engineer six days later.

## Frequently Asked Questions

## Frequently Asked Questions

### Can you actually unit test a prompt, or is it always fuzzy?

Most of a prompt's contract is deterministically testable. If the prompt asks for structured output, a JSON schema check is a hard pass/fail, no fuzzier than testing any other API response. String presence and absence checks are just as deterministic. Only the genuinely open-ended part of a response, where wording legitimately varies or quality is subjective, needs a semantic or judge-based check.

### How do you test prompt engineering work, not just the prompt output?

Testing prompt engineering means testing the change, not the prompt in isolation. Keep each prompt version in its own version-controlled file with a golden case set attached, then treat every wording edit as a diff that has to pass those cases before it merges. That converts prompt engineering from a judgment call into a reviewable change with a pass or fail attached, which is the only way to know whether a tightened instruction actually improved the output or quietly broke a field the rest of your pipeline depended on.

### What's the difference between a prompt unit test and an eval?

A prompt unit test checks one prompt against a handful of cases, runs fast, and lives in your normal test suite next to everything else. An eval is a broader exercise: a larger test set, aggregated scoring across many cases, regression thresholds, and trend tracking over time, usually run as its own pipeline rather than inline with every commit. Unit tests are what you run constantly; evals are what you run to understand the whole system's quality over time.

### What does LLM output testing actually assert against?

LLM output testing asserts against whatever contract the prompt promised, and the contract determines the assertion. A structured response gets a schema check on required fields and types. A response with required or forbidden markers gets string presence and absence checks on the raw text. A response whose correct wording varies gets a semantic similarity score against a reference answer, with the threshold set just below your worst true positive rather than at a round number. Only open-ended quality, tone or whether the response engaged with the question, needs an LLM judge, and only after the cheaper checks have been ruled out.

### How do you test a prompt without spending money on every CI run?

Split your tests into two tiers. Mock the model entirely for anything testing your own code (template rendering, parsing, error handling), which costs nothing and runs in milliseconds on every commit. Reserve real model calls for a small golden case set, run on pull requests rather than every commit, with the full eval suite reserved for a nightly scheduled job.

### How many test cases per prompt is enough?

Enough to cover the prompt's distinct behaviors, not an arbitrary round number. A handful of golden cases per prompt version is typical: one or two happy-path cases, one edge case per known failure mode (empty input, ambiguous input, an input that previously broke the prompt), and one case per structural requirement in the schema. Add a case whenever a bug slips through, so the golden set grows in the direction your actual failures do.

### What happens when the model provider updates the model underneath you?

Your existing golden case suite is exactly what catches this. Re-run it against the new model version before adopting it in production, and treat any regression in your deterministic or semantic assertions as a blocker, the same way you'd treat a failing test after any other dependency upgrade. Pin your LLM-as-judge to a specific model version explicitly so the judge itself doesn't silently drift at the same time as the model you're testing.

---

This is the markdown variant of <https://getautonoma.com/blog/llm-unit-testing>, served by content negotiation (`Accept: text/markdown`) and also available directly at <https://getautonoma.com/md/blog/llm-unit-testing>.

Other agent surfaces: [llms.txt](https://getautonoma.com/llms.txt), [resource catalog](https://getautonoma.com/.well-known/ai-catalog.json), [developer portal](https://getautonoma.com/developers), [sitemap](https://getautonoma.com/sitemap.xml).
