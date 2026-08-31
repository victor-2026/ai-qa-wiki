# Source: https://getautonoma.com/blog/how-to-test-for-ai-hallucinations

---
title: "How to Test for AI Hallucinations: A Code-First Guide"
description: "How to test for AI hallucinations with runnable checks: reference-based and reference-free assertions, RAG faithfulness, LLM-as-judge, and a CI regression set."
date: "2026-07-27"
canonical: "https://getautonoma.com/blog/how-to-test-for-ai-hallucinations"
authors:
  - "Tom Piaggio"
tags:
  - "AI"
  - "Testing"
  - "Hallucination Testing"
---

# How to Test for AI Hallucinations: A Code-First Guide

> **How to test for AI hallucinations** means running two complementary kinds of checks: a reference-based check that compares an answer against a labeled, known-good response for a curated regression set, and a reference-free check that verifies an answer is grounded in whatever context it was actually given, the kind that scales to live production traffic. Both need runnable assertions, not just metric names, to catch a hallucination before it reaches a user.

> A runnable pytest project implementing every check in this guide: reference-based and reference-free assertions, a claim-decomposition faithfulness harness with DeepEval and Ragas equivalents, an LLM-as-judge factuality rubric, a repeat-and-threshold wrapper for non-deterministic scores, a hallucination regression set built from real incidents, and the CI workflow that gates merges on all of it. [Source on GitHub](https://github.com/Autonoma-Tools/how-to-test-for-ai-hallucinations).

The support bot answered in under a second. It quoted the refund policy correctly, structured the response cleanly, and closed with a friendly line about being happy to help further. It also stated, with the same even confidence as everything else in the message, that a $10 restocking fee applies. No restocking fee exists in the company's policy, in the context the model was given, or anywhere in reality. Every test the team had passed: the response answered the question asked, the tone matched the brand voice, latency was fine, the JSON parsed. Nothing about the failure looked like a bug, because by the standards of a conventional test suite, it wasn't one. It was a hallucination, and the suite that would have caught it did not exist yet.

## What Counts as a Hallucination (and What Doesn't)

"Hallucination" gets used as a catch-all for "the AI said something wrong," which is too loose a definition to test against. Three distinct failure modes hide inside that one word, and they need different checks.

An **ungrounded claim** is a statement the model was not given any basis for, regardless of whether it happens to be true in the world. The restocking fee above is ungrounded: nothing in the retrieved policy text supports it, whether or not some other store somewhere charges one. A **factually false claim** is wrong independent of context, the kind of error a reference-based check against a known-good answer catches even without a retrieval step: a wrong date, a wrong formula, a wrong version number. An **unsupported extrapolation** is subtler than both. The model takes something the context actually says and reasons one step past it, inferring a general policy from a specific example, or assuming a rule applies to a case the context never covered. It often sounds the most reasonable of the three, which is exactly why it is the easiest one to ship by accident.

The distinction matters because it decides which check catches which failure. Groundedness and faithfulness checks are built to catch ungrounded claims and, with more care in the rubric, unsupported extrapolation. They are not built to catch a factually false claim that happens to match the given context, because a groundedness check only ever asks "does the context support this," never "is the context itself correct." Keep that boundary explicit before writing a single assertion, or you'll end up debugging a faithfulness score that was doing exactly what you asked it to do. If you're still mapping out the wider surface a genAI feature needs covered, [testing generative AI applications](/blog/testing-generative-ai-applications) is the broader guide this hallucination work sits inside.

## Reference-Based vs Reference-Free Checks

The first fork in the road is whether you have a labeled, known-good answer for the input you're testing. If you do, a reference-based check compares the new answer against that golden reference, usually with semantic similarity rather than exact string match, since two correct answers can be worded completely differently. That comparison is precise and cheap to compute, but it only exists for the inputs someone bothered to label, which means it lives entirely inside a curated regression set. It has nothing to say about the live traffic your users are actually sending, because none of that traffic has a labeled answer waiting for it.

A reference-free check drops the labeled-answer requirement entirely. Instead of asking "does this match the known-good answer," it asks "is this answer supported by whatever context the model was actually given." That reframing is what makes it viable on open-ended, unlabeled production traffic: it needs the retrieved context (which you always have, by construction) and the answer (which you always have too), and nothing else. The tradeoff is real: a reference-free check can tell you an answer is well-grounded in its context and still have no opinion on whether that grounded answer was the *right* one to give, since it never compares against what a correct answer should have said.

> **Diagram:** Two paths for hallucination testing: reference-based checks need a labeled known-good answer and only scale to a curated regression set, while reference-free checks need only the retrieved context and scale to live production traffic.

*Neither path is strictly better. Reference-based checks need labels and don't scale; reference-free checks scale but can't tell you if the grounded answer was the one you wanted.*

| Dimension | Reference-Based | Reference-Free |
| --- | --- | --- |
| Ground truth needed | Yes, a labeled answer | No, only given context |
| Scalability | Limited to the labeled set | Scales to any input |
| Prod-traffic viability | Not viable, no labels exist | Viable, runs on live traffic |
| What it catches | Drift from the golden answer | Claims unsupported by context |
| What it misses | Anything outside the golden set | Whether it's the answer you wanted |

Here's the reference-based version, semantic similarity against a golden set instead of exact match, gated with a threshold and margin rather than exact equality:

[tests/test_reference_based_check.py](https://github.com/Autonoma-Tools/how-to-test-for-ai-hallucinations/blob/main/tests/test_reference_based_check.py)

And here's the reference-free version, a groundedness check that needs no labeled answer at all, only the context the model was actually given:

[tests/test_reference_free_groundedness.py](https://github.com/Autonoma-Tools/how-to-test-for-ai-hallucinations/blob/main/tests/test_reference_free_groundedness.py)

Most teams end up running both. The reference-based suite guards a curated set of high-stakes, known scenarios (the ones a human already wrote a correct answer for). The reference-free suite runs continuously against everything else, since it's the only check of the two that doesn't need someone to have labeled the input first.

> **Passed the eval. Broke the app anyway.** Autonoma runs agentic end-to-end tests on every pull request. [Try Autonoma](https://autonoma.app).

## RAG Faithfulness: Keeping the Answer Grounded in Retrieved Context

Faithfulness is the reference-free check applied specifically to retrieval-augmented generation: given the chunks your retriever pulled back, does the generated answer stay inside what those chunks actually support? The metric name shows up everywhere in the current SERP. The runnable version of it does not, which is the actual gap this section closes.

The mechanism that makes faithfulness testable is claim decomposition. You don't score an entire answer as one grounded-or-not unit, because a single answer routinely mixes a grounded sentence with an invented one, and scoring the whole thing at once hides exactly which part failed. Instead, split the answer into atomic, independently-checkable claims (no pronouns pointing at an earlier claim, no compound "and" statements), then check each claim against the retrieved chunks individually. Here's the decomposition and per-claim entailment logic, written against a generic `llm_call` so it works with whichever model client you're already using:

[lib/faithfulness.py](https://github.com/Autonoma-Tools/how-to-test-for-ai-hallucinations/blob/main/lib/faithfulness.py)

> **Diagram:** The RAG faithfulness assertion pipeline: a question with retrieved chunks produces an answer, the answer is decomposed into atomic claims, each claim is checked for entailment against the retrieved chunks, and the aggregate result passes or fails a threshold.

*Claim decomposition turns "is this answer faithful" into a series of small, checkable questions instead of one fuzzy judgment call.*

Here's the assertion that ties it together, decomposing an answer, checking each claim against the retrieved context, and gating on the fraction entailed rather than requiring every claim to pass:

[tests/test_rag_faithfulness.py](https://github.com/Autonoma-Tools/how-to-test-for-ai-hallucinations/blob/main/tests/test_rag_faithfulness.py)

You don't have to hand-roll this. [DeepEval](https://docs.confident-ai.com) ships a `FaithfulnessMetric` that does the same claim-level entailment check behind a single call, and the config surface (a threshold, the retrieved context, the actual output) maps directly onto the pieces above:

[tests/test_faithfulness_deepeval.py](https://github.com/Autonoma-Tools/how-to-test-for-ai-hallucinations/blob/main/tests/test_faithfulness_deepeval.py)

[Ragas](https://docs.ragas.io) does the same thing at the dataset level rather than one test case at a time, which is the shape you want once you're scoring a batch of question-answer-context triples instead of asserting on a single example:

[tests/test_faithfulness_ragas.py](https://github.com/Autonoma-Tools/how-to-test-for-ai-hallucinations/blob/main/tests/test_faithfulness_ragas.py)

All three versions, the hand-rolled one and both library equivalents, are computing the same thing: what fraction of the atomic claims in this answer are actually supported by what the model was given. If your RAG pipeline's retrieval step itself is the thing under suspicion (wrong chunk, not wrong claim), [how to test a RAG pipeline](/blog/how-to-test-a-rag-pipeline) goes one layer deeper, into testing retrieval quality separately from generation quality.

## How Autonoma Closes the Gap Faithfulness Scores Can't See

Every check above, hand-rolled or via DeepEval or Ragas, scores the same thing: the text of the answer against the text of the retrieved context. That's the right thing to score, and it's still only half the failure mode that actually reaches users. A faithfulness score can come back clean, every claim entailed, threshold cleared, and the application the AI feature is wired into can still do the wrong thing with that grounded answer: prefill the wrong field, route the user to the wrong screen, trigger a side effect the grounded text never implied. The score tells you the words were honest. It has no visibility into what happened after the words were generated.

That's the layer [Autonoma](https://getautonoma.com) operates in, and it's deliberately not another eval framework: it never scores a faithfulness metric or grades a model's output. Autonoma's Planner reads your codebase, the routes, components, and flows a genAI feature actually touches, and plans behavioral end-to-end test cases around what should happen inside the running application after that feature responds, including generating the database state each scenario needs. Executor drives those tests against the real UI in a live preview environment, the same environment a deploy would use, so the assertion is "did the app end up in the right state," not "was the text grounded." Reviewer classifies what it finds, a genuine bug in how the feature's output got wired into the app, an agent error, or a plan-to-code mismatch, and Diffs Agent keeps that coverage current on every pull request by reading the code diff instead of letting the suite quietly rot. A hallucination test tells you the claim wasn't supported. A behavioral test tells you whether the unsupported claim still made it into a database row or a rendered screen, which is the outcome that actually reaches a user.

## LLM-as-Judge for Factuality

Once you're past exact-match and semantic similarity, most factuality checks end up leaning on a judge model to read the answer and the context and decide whether the claims hold up. The failure mode here isn't the concept, it's the rubric. A prompt that asks "is this answer accurate, rate 1 to 5" produces a number that drifts run to run and means something slightly different every time you use it, because "accurate" was never defined as a criterion. A rubric that forces a binary entailment verdict per claim, and forces the judge to cite which retrieved chunk supports (or fails to support) that verdict, produces something you can actually threshold and trust.

[lib/factuality_judge.py](https://github.com/Autonoma-Tools/how-to-test-for-ai-hallucinations/blob/main/lib/factuality_judge.py)

Here's the assertion built on that rubric, gating on the fraction of claims the judge marks entailed rather than trusting a single overall verdict:

[tests/test_llm_judge_factuality.py](https://github.com/Autonoma-Tools/how-to-test-for-ai-hallucinations/blob/main/tests/test_llm_judge_factuality.py)

### Where Does the Judge Get It Wrong?

A judge with a good rubric is still a probabilistic system judging another probabilistic system, and pretending otherwise is how a factuality suite quietly becomes untrustworthy. The judge call is itself non-deterministic: run the same claim through it twice and you can get two different verdicts, especially near the entailment boundary. It carries known biases, toward longer and more confident-sounding answers, and toward outputs that resemble its own training distribution, which matters most when your judge and your generator are the same model family and share the same blind spots. A judge tuned on someone else's rubric needs its own calibration against a small set of human-labeled examples before you trust its threshold in CI, the same way you'd never trust a new hire's bug triage without checking their first few calls against a senior engineer's. None of that makes LLM-as-judge unusable. It makes it a component you calibrate and monitor, not a ground truth you accept on the first output.

## Why Does the Same Faithfulness Check Pass One Run and Fail the Next?

A faithfulness or judge score is a sampled measurement, not a fixed property of the answer, because both the generator and the judge are non-deterministic. Gating on a single run conflates three genuinely different problems: the assertion threshold is too strict for normal variance, the prompt is ambiguous enough that the model reasonably answers two different ways, or the retrieval is actually wrong and something real changed. Treating all three as "the test is flaky" and loosening the threshold until it stops complaining fixes none of them and hides all three.

The fix is the same one that shows up across every check in this cluster: run the scenario N times and gate on a pass rate with margin, not on unanimous agreement. Five runs with four passing is a defensible floor for most factuality checks; a scenario that drops from 5-of-5 to 2-of-5 over a week is a real signal (a prompt edit, a model version bump, retrieved context that quietly got worse), the exact kind of signal a single-run assertion would never surface. For a deeper look at the broader pattern behind this, including semantic-similarity assertions and the general "is my test too strict or is the model actually wrong" decision tree, see [how to test non-deterministic AI outputs](/blog/how-to-test-non-deterministic-ai-outputs).

[lib/repeat_and_threshold.py](https://github.com/Autonoma-Tools/how-to-test-for-ai-hallucinations/blob/main/lib/repeat_and_threshold.py)

## Building a Hallucination Regression Set From Real Incidents

Every check above is aimed at catching a hallucination before it ships. The most durable one is aimed at making sure the same hallucination never ships twice. Every hallucination that reaches a real user is a gift, in the specific sense that it's a concrete, verified failure mode you now know how to describe precisely: the question, the context that was retrieved, the exact wrong claim, and why it happened. Turn that into a permanent test case, and a recurrence of that specific failure fails the build instead of reaching a user a second time.

[fixtures/hallucination_incidents.json](https://github.com/Autonoma-Tools/how-to-test-for-ai-hallucinations/blob/main/fixtures/hallucination_incidents.json)

[tests/test_hallucination_regression.py](https://github.com/Autonoma-Tools/how-to-test-for-ai-hallucinations/blob/main/tests/test_hallucination_regression.py)

None of this protects anything if it only runs on a laptop before a release someone remembers to trigger manually. Wire it into CI so a recurrence blocks the merge automatically, the same way any other regression suite does:

[.github/workflows/hallucination-tests.yml](https://github.com/Autonoma-Tools/how-to-test-for-ai-hallucinations/blob/main/.github/workflows/hallucination-tests.yml)

A regression set built this way compounds in a way a static eval set never does. Every incident makes the next release a little harder to break the same way twice, and after a few months of real production traffic feeding it, the regression set becomes a more accurate map of your actual failure modes than any golden set someone wrote up front ever could be.

## Catching the Next One Before It Ships

Stack these checks in the order they earn their keep. Reference-based checks are cheap and precise but only exist where someone labeled an answer, so they belong on your highest-stakes, curated scenarios. Reference-free and faithfulness checks are what actually runs on everything else, since they need no ground truth, only the context the model was given. LLM-as-judge fills in wherever a rule-based check can't reach, provided the rubric forces per-claim citations instead of a vague overall score, and provided you never forget the judge itself needs calibration. Run all of it N times, not once, so a threshold gate reflects an actual pattern instead of a single lucky or unlucky sample. Then feed every real production miss back into a regression set that makes the specific failure impossible to ship a second time.

Faithfulness and factuality checks answer whether the words were honest. For the rarer but sharper case, a grounded, honest-sounding answer that still drove the application to do the wrong thing, that's the layer [Autonoma](https://getautonoma.com)'s behavioral testing covers, above and separate from anything a hallucination score can measure.

## Frequently Asked Questions

## Frequently Asked Questions

### How do you test for AI hallucinations?

Run two complementary checks: a reference-based check that compares the answer to a labeled, known-good answer using semantic similarity, and a reference-free check that verifies the answer is grounded in whatever context the model was actually given. For RAG systems, decompose the answer into atomic claims and check each one for entailment against the retrieved chunks, gating on the fraction supported rather than requiring every claim to pass.

### What are the best hallucination testing tools?

DeepEval and Ragas are the two most commonly used, and both implement claim-level faithfulness scoring behind a single metric call rather than requiring you to hand-roll the decomposition and entailment logic yourself. The choice of tool matters less than the rubric: a claim-by-claim entailment check with forced chunk citation catches far more than a vague 'is this accurate, 1 to 5' judge prompt.

### How do you test RAG hallucinations specifically?

Test faithfulness (does the answer stay grounded in the retrieved chunks) separately from retrieval quality (did the retriever pull back the right chunks in the first place). A faithful answer built on the wrong retrieved chunk is still a real production failure, just a different one, which is why testing a RAG pipeline needs both a faithfulness check on the generation step and a separate check on what the retriever returned.

### How do you catch AI hallucinations before they reach production?

Run reference-free faithfulness and groundedness checks continuously in CI, since they need no labeled ground truth and can run against realistic inputs before a release ships. Repeat non-deterministic checks multiple times and gate on a pass rate instead of a single run, and turn every hallucination that does slip through into a permanent regression test case so the same failure can't reach production a second time.

### Is LLM-as-judge reliable for detecting hallucinations?

It's reliable when the rubric forces a binary entailment verdict per atomic claim with a cited supporting chunk, and unreliable when it asks for a vague overall accuracy score. Even with a good rubric, the judge itself is non-deterministic and biased toward verbose, confident-sounding answers, so it needs its own calibration against human-labeled examples and should be run multiple times with a pass-rate threshold rather than trusted on a single call.

---

This is the markdown variant of <https://getautonoma.com/blog/how-to-test-for-ai-hallucinations>, served by content negotiation (`Accept: text/markdown`) and also available directly at <https://getautonoma.com/md/blog/how-to-test-for-ai-hallucinations>.

Other agent surfaces: [llms.txt](https://getautonoma.com/llms.txt), [resource catalog](https://getautonoma.com/.well-known/ai-catalog.json), [developer portal](https://getautonoma.com/developers), [sitemap](https://getautonoma.com/sitemap.xml).
