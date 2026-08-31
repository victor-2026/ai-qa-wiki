# Source: https://getautonoma.com/blog/how-to-test-a-rag-pipeline

---
title: "How to Test a RAG Pipeline: Two Surfaces, Not One Score"
description: "How to test a RAG pipeline: test retrieval and generation separately, ship a runnable Ragas or DeepEval harness, and build your eval set from your own docs."
date: "2026-07-28"
canonical: "https://getautonoma.com/blog/how-to-test-a-rag-pipeline"
authors:
  - "Tom Piaggio"
tags:
  - "AI"
  - "Testing"
  - "RAG Testing"
---

# How to Test a RAG Pipeline: Two Surfaces, Not One Score

> **How to test a RAG pipeline** starts with treating retrieval and generation as two separate test surfaces instead of scoring the whole answer at once: assert that the retriever pulled the right chunks, then separately assert that the generator's answer is faithful to those chunks and actually answers the question. Combine deterministic retrieval checks with threshold-gated generation metrics, faithfulness, answer relevancy, and context precision, computed with Ragas or DeepEval against an eval set built from your own documents, and gate the aggregate score in CI on every pull request.

> The full harness from this article: retrieval and generation tested as separate surfaces, Ragas and DeepEval suites gated on aggregate thresholds, and a script that builds an eval set from your own documents. [Source on GitHub](https://github.com/Autonoma-Tools/how-to-test-a-rag-pipeline).

Someone drops a screenshot in Slack. A user asked the "ask our docs" bot about the refund window, and the bot answered with total confidence. The answer is wrong. Not garbled, not a timeout, not a stack trace. Wrong, stated with the same even tone as everything else in the response.

Now you're staring at the two questions everyone stares at the first time this happens. Did the retriever pull the wrong chunk, so the generator was reasoning from garbage? Or did the retriever do its job, and the generator ignored the context, or quietly filled in a gap with something it half-remembered from pretraining? You cannot tell from the transcript alone. The retrieved chunks and the generated answer both read as plausible in isolation, and the only way to actually know which stage broke is to have already been asserting on both of them separately, before this ticket ever landed in your inbox.

## The Two Failure Surfaces an End-to-End Score Can't Localize

A RAG pipeline has exactly one job from the outside: take a question, return a grounded answer. That framing is exactly why an end-to-end pass or fail is the wrong metric to build a test suite around. It tells you the pipeline produced a bad answer. It has nothing to say about which of the two stages inside that pipeline produced it, and those two stages fail for completely different reasons, with completely different fixes.

A retrieval failure means the retriever handed the generator the wrong material. Right question, wrong chunks, and the generator is now confidently reasoning from context that never had the answer in it. The fix lives in chunking strategy, embedding model choice, top-k, or reranking, nowhere near the prompt. A generation failure means the retriever did its job. The right chunks were sitting right there in context, and the generator still produced a claim that isn't in them, either by embellishing past what the context supports or by quietly discounting it in favor of something the model already "knew." The fix for that lives in the prompt, the faithfulness threshold, or the refusal logic, and touching chunking or embeddings does nothing for it.

Score the whole answer as one unit and both failures look identical from the outside: a wrong answer. Split the assertion into two gates, one on what the retriever returned and one on what the generator did with it, and the failure tells you exactly which team meeting you need to have.

> **Diagram:** A RAG pipeline flowing from query through retriever to context to generator to answer, with a Retrieval Assertion Gate attached after the retriever checking context precision recall and hit-rate at k, and a Generation Assertion Gate attached after the generator checking faithfulness answer relevancy and refusal, showing the two independent test surfaces.

*Retrieval and generation fail for different reasons and need different fixes. Testing them as one pass or fail hides which one you actually have.*

| Signal | Retrieval Failure | Generation Failure |
| --- | --- | --- |
| Symptom | Right question, wrong chunks | Right chunks, unsupported claim |
| Root cause | Chunking, embeddings, low top-k | Model ignores or embellishes context |
| Fix lever | Chunking, embeddings, reranking | Prompt, threshold, refusal logic |
| Test surface | Context the retriever returned | Answer text given fixed context |
| Determinism | Deterministic given a fixed index | Non-deterministic, needs N-run gating |

If you're mapping the wider surface a shipped genAI feature needs covered, [testing generative AI applications](/blog/testing-generative-ai-applications) is the broader pillar this retrieval and generation split sits inside.

## Testing the Retrieval Layer

Retrieval is the deterministic half of a RAG pipeline, and that's exactly why it deserves its own test surface. Given a fixed index and a fixed query, the retriever returns the same chunks every time. There's no sampling, no temperature, no model deciding how to phrase anything. If a retrieval test flakes, it isn't the retriever being probabilistic, it's your index or your query changing underneath the test.

The core assertion is simple to state and easy to get wrong in practice: for a question with a known-correct chunk, is that chunk in the top-k results, and at what rank. Rank matters because "somewhere in the top 50" and "the first result" are very different production experiences once you factor in how many chunks actually make it into the generator's context window. Context precision asks what fraction of what you retrieved was actually relevant. Context recall asks what fraction of everything relevant you managed to retrieve, in app-builder terms: precision punishes a retriever that buries the right answer under noise, and recall punishes a retriever that leaves the right answer out of the top-k entirely.

The three fix levers, in the order most teams reach for them: chunk size and overlap first (chunks too large dilute the embedding, too small lose context), embedding model choice second (a domain mismatch between your embedding model and your actual content shows up here first), and top-k or reranking third (retrieving more candidates and reranking them is usually cheaper than re-chunking your entire index). If you're seeing a specific "confidently wrong answer" pattern and want to isolate whether it's a retrieval problem before touching generation at all, [how to test if your RAG pipeline is retrieving the right context](/blog/how-to-test-rag-retrieval) goes deeper into hit-rate, MRR, and vector search accuracy specifically.

## Testing the Generation Layer Given Retrieved Context

Once retrieval is asserted separately, generation testing gets to ask a narrower, more answerable question: given exactly this context, is this answer any good? Two metrics carry almost all of the weight here. Faithfulness asks whether every claim in the answer is actually supported by the retrieved context, the generation-side counterpart to the hallucination problem: an answer can be fluent, confident, and completely unsupported by anything the model was given. Answer relevancy asks the opposite failure mode: an answer that's fully grounded in the context but doesn't actually address what was asked, a faithful non-answer.

Both metrics need the same underlying mechanism to be trustworthy: don't score the whole answer as one grounded-or-not unit. Decompose it into atomic claims and check each one against the retrieved chunks individually, then aggregate. A single ungrounded sentence buried inside an otherwise solid answer is exactly the failure a whole-answer score is built to miss. [How to test for AI hallucinations](/blog/how-to-test-for-ai-hallucinations) covers that claim-decomposition mechanism in more depth if you want the generation-only version of this problem outside of a RAG context specifically.

There's a third case generation testing has to cover that faithfulness and relevancy alone don't: what happens when the context genuinely doesn't contain the answer. A well-behaved pipeline should refuse or hedge rather than generate a confident answer from insufficient context, and that refusal behavior is itself a testable assertion, not a hope. Build refusal test cases directly into your eval set, questions your corpus genuinely cannot answer, and assert the generator says so instead of inventing something plausible-sounding to fill the gap.

## Building Your Eval Set From Your Own Documents

None of the metrics above mean anything without an eval set, and this is the part almost every RAG testing guide skips straight past, as if a labeled dataset just appears once you've read enough about faithfulness. It doesn't. You have to build it, and the good news is it's a mechanical process once you know the shape of it.

Start by sampling real chunks out of your own index, not synthetic documents, not a public benchmark corpus. For each sampled chunk, generate a candidate question that chunk should be able to answer, plus the ground-truth answer, using an LLM to draft the pair and a human to review it before it goes in the set. That review step is not optional: an LLM-drafted question can accidentally be answerable from general knowledge rather than from the chunk specifically, which quietly breaks the point of the test. Layer in real user queries mined from your logs, deduplicated and sampled, because the questions your actual users ask are reliably weirder and more specific than anything an LLM generates from a chunk in isolation.

The subset everyone skips is the adversarial one: questions your corpus genuinely cannot answer. Deliberately write a handful of questions that sound reasonable but fall outside what your documents cover, and mark them so the expected behavior is a refusal, not an answer. Without that subset, you have no way to test whether your pipeline knows the difference between "I don't have this" and "I'll guess."

On size: twenty to fifty curated examples, each one reviewed and something you'd defend individually, will catch more real regressions than five hundred synthetic ones nobody has looked at. A small set you trust means every red result gets investigated. A large set nobody has reviewed means red results get shrugged off as noise, which defeats the entire point of having a test suite. Here's the script that handles the sampling, the LLM-assisted question generation, the log mining, and the adversarial subset:

[scripts/build_eval_set.py](https://github.com/Autonoma-Tools/how-to-test-a-rag-pipeline/blob/main/scripts/build_eval_set.py)

And here's the shape the resulting eval set takes once it's reviewed and merged, a corpus of chunks plus a list of examples, each one tagged standard or adversarial:

[eval_set/eval_set.json](https://github.com/Autonoma-Tools/how-to-test-a-rag-pipeline/blob/main/eval_set/eval_set.json)

> **Test what your RAG answer actually did.** Autonoma runs agentic end-to-end tests on every pull request. [Try Autonoma](https://autonoma.app).

## Shipping the Runnable Harness

With an eval set in hand, the harness is just pytest wired up to run both gates against it. Start with a shared fixture layer so every test file works off the same corpus, the same eval examples, and the same retriever instance instead of each test file re-loading its own copy:

[tests/conftest.py](https://github.com/Autonoma-Tools/how-to-test-a-rag-pipeline/blob/main/tests/conftest.py)

The retrieval tests run entirely offline against your fixed index, no LLM call, no API key, no non-determinism to manage. They compute hit-rate@k and mean reciprocal rank across the whole eval set and check the adversarial examples come back with low retrieval confidence rather than a false-positive match:

[tests/test_retrieval.py](https://github.com/Autonoma-Tools/how-to-test-a-rag-pipeline/blob/main/tests/test_retrieval.py)

The generation tests need an actual model call, and this is where the two dominant libraries earn their keep. [Ragas](https://github.com/explodinggradients/ragas) scores a batch of question, answer, and context triples at once, which is the shape you want once you're evaluating a full eval set instead of asserting on one example:

[tests/test_generation_ragas.py](https://github.com/Autonoma-Tools/how-to-test-a-rag-pipeline/blob/main/tests/test_generation_ragas.py)

[DeepEval](https://github.com/confident-ai/deepeval) scores case by case with the same metric names, faithfulness, answer relevancy, contextual precision, and plugs directly into pytest's assertion model if you prefer per-test-case granularity while still aggregating before you gate:

[tests/test_generation_deepeval.py](https://github.com/Autonoma-Tools/how-to-test-a-rag-pipeline/blob/main/tests/test_generation_deepeval.py)

Notice both generation test files compute a mean across the eval set and assert on that mean, never on any single example. That's deliberate, and it's the difference between a harness a team trusts and one they route around after the third false alarm.

> **Diagram:** The RAG eval harness flow: an eval set built from your own documents feeds into the pipeline, per-example metrics are computed with Ragas or DeepEval, scores are aggregated against thresholds, and the result gates CI pass or fail on the pull request.

*Eval set in, aggregate score out. The threshold gates on the mean across the set, which is what keeps the harness usable in CI instead of noisy.*

Wiring this into CI is the same shape as any other regression suite: run it on every pull request, fail the merge if the aggregate drops below threshold, and give the team a real signal instead of a manual step someone forgets before a release.

[.github/workflows/rag-tests.yml](https://github.com/Autonoma-Tools/how-to-test-a-rag-pipeline/blob/main/.github/workflows/rag-tests.yml)

Worth being clear about what that gate does and doesn't cover, because it's easy to read a green check as broader than it is: it gates the pipeline, not the feature. A pull request that changes the chat component, the citation link builder, or the fallback screen passes this suite untouched, because none of those files can move a faithfulness score. We built [Autonoma](https://getautonoma.com) for that other half: our Planner reads the application code around a RAG feature and plans end-to-end cases from it, including the database state each one needs, so the two gates cover the pipeline and the product surface separately instead of one standing in for the other.

## Why RAG Tests Flake (and the Fix)

Generation scores are sampled measurements, not fixed properties of an answer, because both the generator and, if you're using one, the judge model scoring it are non-deterministic. Exact-match assertions were never the right tool here: two correct answers can use completely different words, so assert on properties and score thresholds instead of string equality.

Run the eval set multiple times rather than once, and gate on the distribution instead of a single pass. Five runs with four clearing threshold is a defensible floor for most generation metrics, and it's the aggregate across the set that matters, never any single example, for the same reason a batting average means more than one at-bat. If you're relying on an LLM as the judge for faithfulness or relevancy, pin its model version, set temperature to zero where the provider allows it, and treat disagreement between repeated judge calls as signal about your rubric, not noise to average away.

The retrieval layer stays out of all of this. Given a fixed index and a fixed query, retrieval is reproducible, which is exactly why testing it as its own surface gives you a stable signal while generation stays fuzzy around it. The practitioner rule worth pinning above your desk: a flaky RAG test is either an assertion that's too strict for normal variance, or a prompt and query that are genuinely too ambiguous to have one right answer. It is never "the model is just being random today," and treating it as such is how thresholds quietly drift until the suite stops meaning anything.

[lib/repeat_and_threshold.py](https://github.com/Autonoma-Tools/how-to-test-a-rag-pipeline/blob/main/lib/repeat_and_threshold.py)

There's a slower failure mode hiding behind flake, and it's the more dangerous of the two: a suite that stops describing the system. Chunking changes, a document set gets restructured, a prompt is rewritten, and the eval set keeps passing against expectations that no longer match what the pipeline is for. Nothing goes red, which is exactly the problem. On the behavioral side we handed that upkeep to our Diffs Agent, which reads each pull request's code diff and adds, updates, or deprecates the affected end-to-end cases, so drift shows up as a changed test rather than as coverage that quietly stopped meaning anything.

## How Autonoma Fits Above the RAG Pipeline

Every check in this guide, retrieval, faithfulness, relevancy, refusal, answers the same underlying question: did the pipeline produce a grounded, relevant answer. Green scores across the board prove exactly that and nothing more. They don't prove the citation link under that answer actually resolved to the right document, that the streaming response didn't truncate mid-sentence in the UI, that the "I don't have enough information" path rendered the fallback screen instead of a blank div, or that a follow-up question kept the retrieved context instead of starting the conversation over. Those are failures your eval harness will never see, because they happen one layer up, in the running application the pipeline is wired into.

That's the layer Autonoma operates in, and it's worth being precise about the boundary: our platform runs behavioral end-to-end tests against the real, running app, it doesn't score a faithfulness metric or grade a model's output, that job belongs entirely to the harness above. Concretely, the Planner turns the routes and components around a RAG feature into test cases, the Executor drives those cases against the running application, and the Reviewer classifies each result as a real bug, an agent error, or a plan that no longer matches the code. Your eval set proves the pipeline returned a grounded answer; behavioral E2E on the feature the pipeline powers confirms the answer actually helped the user in the product they were using.

## The Practitioner Takeaway

Separate the two surfaces before you write a single assertion. Retrieval is deterministic and testable with hard thresholds today; generation is fuzzy and needs aggregate gating across a set, run more than once. Build that set from your own documents, not a benchmark, and keep it small enough that every red result gets a human's attention. This piece is the hub for testing the pipeline itself; if you want the metrics deep dive specifically, [RAG evaluation metrics that matter](/blog/rag-evaluation-metrics) covers the app-builder's practical subset in more depth, and if the failure you're chasing is specifically about what the retriever returned, [how to test RAG retrieval](/blog/how-to-test-rag-retrieval) is the layer below this one. Own the eval set, gate the aggregate, and the next confidently wrong answer will come with an answer to which stage actually broke.

That leaves one boundary worth naming plainly, since it decides what you build versus what you add. Everything above is the pipeline's own test surface, and it should stay yours: your documents, your thresholds, your judgment about what counts as grounded. Autonoma is what we'd put above it, not inside it. It scores no metric and grades no model output, it drives the feature the pipeline powers and asserts the application ended up in the right state, which is the one failure a perfect faithfulness score is structurally unable to report.

## Frequently Asked Questions

## Frequently Asked Questions

### How do you test a RAG pipeline?

Test retrieval and generation as two separate surfaces instead of one end-to-end score. Assert that the retriever returns the known-correct chunk within the top-k results, then separately assert that the generator's answer is faithful to whatever context it was given and actually answers the question, using threshold-gated metrics computed with Ragas or DeepEval against an eval set built from your own documents.

### What is the difference between testing RAG retrieval and RAG generation?

Retrieval testing checks whether the right chunks came back from the index, and it's deterministic: given a fixed index and query, you get the same result every time. Generation testing checks whether the answer produced from those chunks is faithful and relevant, and it's non-deterministic, since the same context can produce different wording on different runs. They fail for different reasons and need different fixes, which is why they need separate assertions.

### How many examples do you need in a RAG eval set?

Twenty to fifty curated examples, each reviewed by a human, catches more real regressions than several hundred synthetic ones nobody has looked at. A small, trusted set means every failure gets investigated. A large, unreviewed set means failures get dismissed as noise, which defeats the point of having the suite.

### Can you test a RAG pipeline without ground truth answers?

Yes, for the reference-free checks. Faithfulness only needs the retrieved context and the generated answer, no labeled ground truth required, which is why it scales to live traffic. Answer relevancy works the same way. Context precision and recall against a known-correct chunk do need a labeled eval set, which is why building one from your own documents is still worth doing even if you lean on reference-free checks elsewhere.

### How do you test a RAG pipeline in production?

An eval harness proves the pipeline returns a grounded, relevant answer given a fixed input. It doesn't prove the feature works for a user in the running app: whether a citation link resolves, whether a streaming answer renders without truncating, whether the fallback UI appears when context is insufficient, or whether a follow-up question keeps the retrieved context. That's a separate, behavioral test layer that sits above the pipeline and needs its own coverage in the actual application.

---

This is the markdown variant of <https://getautonoma.com/blog/how-to-test-a-rag-pipeline>, served by content negotiation (`Accept: text/markdown`) and also available directly at <https://getautonoma.com/md/blog/how-to-test-a-rag-pipeline>.

Other agent surfaces: [llms.txt](https://getautonoma.com/llms.txt), [resource catalog](https://getautonoma.com/.well-known/ai-catalog.json), [developer portal](https://getautonoma.com/developers), [sitemap](https://getautonoma.com/sitemap.xml).
