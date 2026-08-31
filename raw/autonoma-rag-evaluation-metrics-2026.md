# Source: https://getautonoma.com/blog/rag-evaluation-metrics

---
title: "How to Build a RAG Evaluation Framework in 4 Metrics"
description: "A RAG evaluation framework for app builders: the four metrics that actually matter, runnable Ragas and DeepEval code, and a CI gate that fails the build."
date: "2026-07-28"
canonical: "https://getautonoma.com/blog/rag-evaluation-metrics"
authors:
  - "Tom Piaggio"
tags:
  - "AI"
  - "Testing"
  - "RAG Evaluation"
---

# How to Build a RAG Evaluation Framework in 4 Metrics

> **A RAG evaluation framework** is the set of metrics, benchmark data, and pass/fail thresholds you run against a retrieval-augmented generation system to catch regressions before they reach users. For an app builder, that means four metrics computed on your own questions and documents, not the twenty-metric catalog built for ML research teams, wired into CI so a regression fails the build instead of sitting on a dashboard nobody checks.

> Everything in this article as a runnable Python project: the four metrics scored with both Ragas and DeepEval, a heuristic miner that pulls candidate benchmark questions out of exported support logs, a versioned benchmark fixture with ground-truth chunk IDs, and a pytest CI gate with per-metric thresholds and a repeated-run pass rate, wired to a GitHub Actions workflow. Clone it and point it at your own pipeline. [Source on GitHub](https://github.com/Autonoma-Tools/rag-evaluation-metrics).

The demo went fine. It always does. Feed the RAG feature the three questions everyone asks in a demo and it answers cleanly, cites the right page, looks finished. Then a real user asks something one degree off-script, and the answer comes back fluent, confident, and wrong: a citation pointing at a document that never said what the model just claimed it said. Someone tweaks the prompt, or swaps the embedding model, or bumps the chunk size, and ships the change anyway. Did that change make the RAG feature better or worse? Nobody on the team can answer that with a number. Just a shrug and "it seemed fine when I tried it."

That shrug is the whole problem this post exists to fix. Not by pointing you at a bigger metric catalog, you already have one open in another tab, but by narrowing it down to the four numbers that actually change a ship decision, showing the code that computes them, and walking through the part almost nobody covers: building a benchmark out of your own documents instead of someone else's leaderboard.

## Why the Twenty-Metric Catalog Fails an App Builder

Search for RAG evaluation metrics and you land in one of a handful of comprehensive catalogs. [Evidently's metric library](https://docs.evidentlyai.com), the docs behind Confident-AI's DeepEval, Weights & Biases's eval guides: all three are thorough, all three are correct, and all three are written for an ML team standing up a general-purpose evaluation pipeline across many models and many use cases. That's a different job from shipping one RAG feature into one product. Read those docs as an app builder and you walk away with a list of eighteen to twenty-something metrics and zero guidance on which four to actually gate a merge on.

Platform vendors make the same gap worse in a different direction. Databricks and similar tooling frame RAG evaluation around their own managed pipeline, which is fine advice if you're already on that stack and useless if you're not, because the tooling doesn't transfer. None of this is a knock on any of it. Evidently, DeepEval, and Weights & Biases all show up later in this post as the actual libraries doing the scoring. The problem is scope, not quality: a catalog built to cover every case leaves you to do the hard part, deciding which four matter for yours, entirely on your own.

Here's the answer for a RAG feature that retrieves documents and generates an answer from them: faithfulness, answer relevancy, context precision, and context recall. Everything else in the standard catalogs is either a variant of one of those four, or a metric that matters for a narrower case than most app builders have. Start there. Add a fifth metric only when a specific, observed failure in your own product demands it, never because a blog post listed it.

## The Four RAG Evaluation Metrics That Matter (and What Each One Catches)

Split the four down the middle by which half of the pipeline they watch. Context precision and context recall are retrieval-side: they judge what your retriever handed to the generator, before a single token of the answer got written. Faithfulness and answer relevancy are generation-side: they judge what the model did with what it was given, after retrieval already happened. That split matters in practice, because a metric that flags a generation problem tells you nothing about whether the real fault sits in your retriever, and chasing the wrong half of the pipeline based on the wrong metric wastes an afternoon.

**Context recall** catches a retriever that missed the point of the question entirely. It's computed by checking whether the chunk that actually contains the ground-truth answer shows up anywhere in what the retriever returned. Score it low and no amount of prompt tuning on the generation side fixes anything, because the model was never handed the piece it needed. **Context precision** catches the opposite failure: the right chunk is in there, but it's buried under three or four irrelevant ones, forcing the generator to sort signal from noise instead of answering cleanly off a clean set. High recall paired with low precision describes a retriever that grabs everything vaguely related and lets the model sort it out, which works until an unlucky chunk ordering makes it not work. For the mechanics of actually computing precision and recall against your retriever's real output, [how to test RAG retrieval](/blog/how-to-test-rag-retrieval) goes a layer deeper into the retrieval step specifically.

**Faithfulness** catches a model inventing a fact that isn't anywhere in the chunks it actually received: the classic hallucination-on-top-of-retrieval failure, where the retriever did its job correctly and the generation step still made something up. **Answer relevancy** catches the failure faithfulness is structurally blind to: an answer that is completely grounded in the retrieved chunks, cites them accurately, and still doesn't answer the question the user actually asked. A technically faithful non-answer passes faithfulness and fails relevancy, which is exactly why gating on faithfulness alone lets an entire category of real user complaints straight through the gate.

> **Diagram:** A RAG pipeline flow from question to retrieve to chunks to generate to answer, with context precision and context recall watching the retrieval half and faithfulness and answer relevancy watching the generation half.

*The four metrics split cleanly by which half of the pipeline they're actually watching, which is also how to know which half to go fix.*

> **Metrics score the answer. Test the app.** Autonoma runs agentic end-to-end tests on every pull request. [Try Autonoma](https://autonoma.app).

## Computing the Four Metrics With Ragas and DeepEval

You don't hand-roll claim decomposition and entailment checks for four metrics when two well-maintained libraries already do it. [Ragas](https://docs.ragas.io) scores at the dataset level, a batch of question, answer, retrieved-context, and ground-truth-answer rows scored all at once, which is the shape you want once you have more than a handful of examples. Here's a small worked example, three rows, all four metrics, in about fifteen lines once the dataset is built:

[ragas_eval.py](https://github.com/Autonoma-Tools/rag-evaluation-metrics/blob/main/ragas_eval.py)

[DeepEval](https://docs.confident-ai.com) scores per test case instead of per dataset, which is the shape you want when you're asserting on one scenario at a time inside a normal pytest run rather than scoring a batch offline. Same four metrics, same underlying idea, different unit of work:

[deepeval_eval.py](https://github.com/Autonoma-Tools/rag-evaluation-metrics/blob/main/deepeval_eval.py)

Both are computing the same thing under the hood: an LLM judge decomposing the answer into claims and checking each one against the retrieved chunks, or checking whether the ground-truth chunk shows up in what was retrieved. The choice between the two comes down to whether your workflow is dataset-first (Ragas) or test-case-first (DeepEval), not which one is more "correct." Pick one, wire it into the benchmark set below, and move on. Switching between them later costs you an afternoon, not a rewrite.

## Building a RAG Benchmark Set From Your Own Documents

This is the part every metric catalog skips, and it's the part that actually decides whether your evaluation numbers mean anything. A metric computed against a public leaderboard or an academic benchmark tells you how a model performs on someone else's documents and someone else's questions. It tells you nothing about whether your users get good answers about your product's refund policy, your API's rate limits, or your onboarding flow, because none of those exist in any public dataset. The only benchmark that predicts whether your RAG feature works is one built from your own corpus and your own users' actual questions.

Start smaller than feels responsible. Thirty to fifty question-and-answer pairs, built from your real documents, beats a hundred you're still debating six weeks from now, and it beats zero while you wait for a "proper" dataset that never quite gets prioritized. A benchmark that small already catches the regressions that matter: did the last prompt change break the three questions that come up in every sales call, did swapping embedding models drop recall on the ten questions your top customers actually ask. You extend it as real gaps show up, not before.

Source the questions from where your users already are, not from your own imagination. Support tickets, sales call transcripts, and product chat logs are full of exactly the phrasing real users use, which is reliably weirder, shorter, and more ambiguous than the clean questions a team invents while staring at its own documentation. Mining a week of support tickets for lines that end in a question mark, then de-duplicating and skimming the results, produces a stronger seed set in an afternoon than a team brainstorming session produces in a week, because it's grounded in what people actually asked instead of what a team assumes they'd ask.

Writing the ground-truth answer is the part that takes the most care and the least code. For each sourced question, find the actual chunk (or chunks) in your corpus that contain the answer, write the correct answer in your own words, and record which chunk IDs support it. That chunk-ID record is what makes context precision and recall computable later; skip it and you can still score faithfulness and answer relevancy, but you lose the retrieval-side half of the evaluation entirely.

Your corpus changes, so the benchmark has to version alongside it, not sit frozen next to a wiki page from three months ago. Commit the benchmark file into the same repository as your RAG pipeline code, bump its version when a source document it depends on is edited or removed, and treat a stale ground-truth answer (correct against last quarter's docs, wrong against this quarter's) as a bug in the benchmark, not a mysterious drop in your metric scores.

That versioning discipline is manual by necessity here, because only a human knows what the corpus is supposed to say. It's worth naming what the equivalent looks like when the artifact is derived from code instead of documents, since it's the same rot with a different fix: on the behavioral side, [Autonoma](https://getautonoma.com)'s Diffs Agent reads each pull request's diff and adds, updates, or deprecates the end-to-end cases that change affects, so the suite tracks the application without a scheduled review. Your ground-truth answers still need your judgment. The cases that assert on what the app did with those answers don't.

> **Diagram:** Building a benchmark from source documents and real user questions through ground-truth answers to a versioned benchmark set that feeds the CI gate, contrasted with public leaderboards which do not predict performance on your own documents.

*The benchmark that matters is the one built from what your users actually asked about your actual documents, not a public leaderboard.*

Here's a starting point for mining candidate questions out of exported support logs, heuristic-based, meant for a human to review before anything becomes a graded benchmark entry:

[scripts/extract_questions.py](https://github.com/Autonoma-Tools/rag-evaluation-metrics/blob/main/scripts/extract_questions.py)

And here's the shape a versioned benchmark entry actually takes once a human has reviewed and written the ground truth for it:

[benchmark/rag_benchmark_v3.jsonl](https://github.com/Autonoma-Tools/rag-evaluation-metrics/blob/main/benchmark/rag_benchmark_v3.jsonl)

## Turning Your RAG Evaluation Framework Into a Pass/Fail CI Gate

A metric score that lives on a dashboard nobody opens is not an evaluation framework, it's a chart. The whole point of the four metrics and the benchmark set is to fail a build automatically when a change makes the RAG feature worse, the same way a broken unit test fails a build, without anyone having to remember to go look.

Set thresholds per metric, not one aggregate score for all four blended together. An aggregate hides exactly the information you need: a feature that's 95% faithful and 60% relevant to the question asked can average out to a number that looks fine while actively failing users on relevancy. Gate faithfulness and context recall higher and stricter, since an invented fact or a missed chunk is usually the worse failure to ship, and give answer relevancy and context precision a little more room, since a slightly over-broad retrieval or a technically-adjacent answer is a rougher edge, not a wrong one.

The judge scoring your metrics is itself a non-deterministic model, and pretending otherwise is how a gate becomes untrustworthy within a month. Run each benchmark question through the pipeline and the judge multiple times, not once, and gate on a pass rate across those runs rather than a single verdict. Four-of-five passing is a defensible floor for most teams; a question that drops from five-of-five to two-of-five over a week is a real signal, not noise, the kind a single-run gate would never surface. A gate that fails on normal judge variance gets disabled by the team within a sprint, and a disabled gate is worse than no gate, because everyone still believes it's running.

[tests/test_rag_gate.py](https://github.com/Autonoma-Tools/rag-evaluation-metrics/blob/main/tests/test_rag_gate.py)

Wire that gate into the pull request path itself, not a script someone is supposed to remember to run before a release:

[.github/workflows/rag-eval-gate.yml](https://github.com/Autonoma-Tools/rag-evaluation-metrics/blob/main/.github/workflows/rag-eval-gate.yml)

None of these four metrics, however carefully thresholded, tell you whether the citation link the model just generated actually opens the right document when a real user clicks it, or whether a grounded, relevant answer got wired into the right field on the next screen. Verifying what your application actually does with a response that already passed every metric is a behavioral layer above eval scores, and it's closer to what Autonoma tests for inside a running app than anything Ragas or DeepEval measure.

## Shipping a RAG Feature You Can Actually Trust

Four metrics, split cleanly across retrieval and generation. A benchmark built from your own documents and your own users' real questions, thirty to fifty entries to start, versioned alongside the code instead of frozen next to a stale wiki page. Thresholds set per metric instead of blended into one misleading average, gated on a repeated-run pass rate instead of a single lucky or unlucky judge call. That's the whole RAG evaluation framework. It fits in a CI job, it runs on every pull request, and it turns "it seemed fine when I tried it" into a number that either goes up or goes down when someone changes the prompt. If the retrieval half of that pipeline is where you suspect the real problem lives, [how to test a RAG pipeline](/blog/how-to-test-a-rag-pipeline) is the broader end-to-end guide this metrics work sits inside.

Then stop, because the framework is finished and the temptation at this point is to add a fifth metric instead of the layer above. Four scores tell you the pipeline returned a grounded, relevant answer. They cannot tell you the citation rendered as a working link, the answer landed in the right field on the next screen, or the refusal path drew the fallback state instead of an empty div, because none of those are properties of the text. Autonoma is what we built for that layer, and it's deliberately not a fifth metric: it computes no score and grades no model output. Our Planner derives end-to-end cases from the application code around the RAG feature, the Executor drives them against the running app, and the assertion is whether the product ended up in the right state. Keep the four metrics as your pipeline gate. Add a behavioral gate above them for the failures a perfect score is structurally blind to.

## Frequently Asked Questions

## Frequently Asked Questions

### What is a RAG evaluation framework?

A RAG evaluation framework is the combination of metrics, a benchmark dataset, and pass/fail thresholds used to score a retrieval-augmented generation system and catch regressions before they ship. For an app builder, the practical version narrows to four metrics (faithfulness, answer relevancy, context precision, context recall) computed against a benchmark built from the product's own documents and real user questions, wired into CI rather than left as a one-off report.

### Which RAG evaluation metrics actually matter?

Faithfulness (does the answer stay grounded in the retrieved chunks), answer relevancy (does the answer address the question asked), context precision (is the retrieved set free of irrelevant noise), and context recall (did retrieval include the chunk that actually contains the answer). Public metric catalogs list fifteen to twenty additional metrics, most of which are variants of these four or matter only for narrower use cases than a typical product feature.

### How do you benchmark a RAG system?

Build a small set, thirty to fifty question-and-answer pairs is a reasonable start, sourced from real user questions in support tickets or chat logs rather than invented by the team. Write a ground-truth answer and record the supporting chunk IDs for each question, version the set alongside the RAG pipeline code, and re-score it on every change instead of relying on a public leaderboard, which reflects someone else's documents and never predicts performance on your own.

### Should I use Ragas or DeepEval for RAG evaluation?

Both compute the same four core metrics using the same underlying claim-decomposition and entailment approach. Ragas scores at the dataset level, which fits a batch-first workflow with many rows scored at once. DeepEval scores per test case, which fits a pytest-style workflow asserting on one scenario at a time. The choice is about workflow shape, not accuracy, and switching later is a small change, not a rewrite.

### How do you set thresholds for a RAG CI gate without it becoming flaky?

Set a separate threshold per metric instead of one blended average, since an aggregate hides exactly the failure you need to see. Because the LLM judge scoring each metric is non-deterministic, run each benchmark question multiple times and gate on a pass rate, such as four-of-five, rather than a single verdict. A gate that fails on normal judge variance gets disabled by the team within a sprint, which defeats the entire point of having one.

---

This is the markdown variant of <https://getautonoma.com/blog/rag-evaluation-metrics>, served by content negotiation (`Accept: text/markdown`) and also available directly at <https://getautonoma.com/md/blog/rag-evaluation-metrics>.

Other agent surfaces: [llms.txt](https://getautonoma.com/llms.txt), [resource catalog](https://getautonoma.com/.well-known/ai-catalog.json), [developer portal](https://getautonoma.com/developers), [sitemap](https://getautonoma.com/sitemap.xml).
