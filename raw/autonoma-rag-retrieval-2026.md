# Source: https://getautonoma.com/blog/how-to-test-rag-retrieval

---
title: "How to Test if RAG Is Retrieving the Right Context"
description: "How to test if RAG is retrieving the right context: isolate retrieval, build a labeled test set, and gate hit rate, MRR, and context precision in CI."
date: "2026-07-28"
canonical: "https://getautonoma.com/blog/how-to-test-rag-retrieval"
authors:
  - "Tom Piaggio"
tags:
  - "AI"
  - "Testing"
  - "RAG"
  - "LLM Testing"
---

# How to Test if RAG Is Retrieving the Right Context

> **To test if RAG is retrieving the right context**, isolate retrieval from generation and test it as its own step: build a labeled set of query-to-expected-chunk-ID pairs, run only the retriever against it (no LLM call involved), and assert on hit rate/recall@k, MRR, and context precision/recall. Gate these metrics in CI so a regression in retrieval fails the build before it ever reaches a user as a confidently wrong answer.

> A runnable Python and pytest project that tests RAG retrieval on its own, with no LLM in the loop: a thin retriever wrapper that returns ranked chunk IDs, hit rate and recall@k, MRR, and context precision and recall each with their own assertions, a 44-query labeled fixture pairing queries with the chunk IDs known to answer them, a regression suite that gates on aggregate thresholds, and a GitHub Actions workflow that fails the build when retrieval regresses. Runs offline on a clean checkout with no API key. [Source on GitHub](https://github.com/Autonoma-Tools/how-to-test-rag-retrieval).

Somewhere on your team right now, someone is tuning a prompt that doesn't need tuning. The RAG feature gave a wrong answer, the eval flagged it, and the fix everyone reaches for is prompt engineering: rewrite the system message, add a stricter instruction, try a different model. Three iterations later the answer is still wrong, because the prompt was never the problem. The retriever pulled the wrong chunk, handed it to the generator, and the generator did exactly what it was asked: summarize the document it was given, faithfully, confidently, and completely irrelevantly.

This is the failure mode almost nobody isolates. Teams test the RAG pipeline end to end, watch a bad answer come out, and start debugging three layers too high. The generation step passed its own quiet test the whole time: given garbage in, it produced a fluent, on-topic-sounding summary of garbage. The actual defect lives in the vector search, and it will keep producing wrong answers no matter how many times you rewrite the prompt around it.

## Isolate Retrieval From Generation

The fix starts with a reframe most teams never make: retrieval is not a language model problem. It is a classic information-retrieval problem, the same one search engines have been testing for decades, with metrics that were established long before anyone put an LLM on top of a vector index. You do not need an LLM in the loop to test whether your retriever found the right document. You need the retriever, a set of queries with known-correct answers, and a way to compare a ranked list of chunk IDs against the ones you expected.

Strip the generator out and retrieval testing turns fast, cheap, and deterministic: no model call, no LLM-as-judge grading a summary. A test that once cost seconds and cents now runs in milliseconds, on every commit, without a second thought.

> **Diagram:** A RAG pipeline split into retrieval and generation, with a query flowing into the retriever, which returns ranked chunk IDs, an assertion checkpoint comparing those IDs against a labeled expected set before the generator ever runs, and the generator shown as a separate downstream step.

*Cut the pipeline at the retriever's output. Everything left of the checkpoint is a fast, deterministic information-retrieval test. Everything right of it is a different problem with a different testing discipline.*

A thin wrapper is all this requires: a function that takes a query string and returns a ranked list of chunk IDs, nothing else. No prompt template, no generator call, no output parsing. Here's that wrapper, built to sit in front of whatever vector store you're actually using:

[src/retriever.py](https://github.com/Autonoma-Tools/how-to-test-rag-retrieval/blob/main/src/retriever.py)

## How to Evaluate RAG Retrieval Quality: 4 Metrics That Catch Real Bugs

Retrieval has a small set of metrics that have been tested against exactly this kind of problem for decades, and each one catches a distinct failure a naive "did it work" check misses.

### Hit Rate (Recall@k)

Hit rate, also called recall@k, asks the bluntest possible question: is the chunk you actually needed anywhere in the top-k results at all? It's a binary pass or fail per query, averaged across the test set. A hit rate of 0.65 at k=5 means over a third of your queries never surface the right document, no matter how good the generator's writing is. It's the first gate, and the one most teams stop at, which is a mistake: a chunk buried at rank 9 still counts as a "hit" at k=10 while being functionally invisible to a generator's context window.

[src/metrics/hit_rate.py](https://github.com/Autonoma-Tools/how-to-test-rag-retrieval/blob/main/src/metrics/hit_rate.py)

### Mean Reciprocal Rank (MRR)

Mean Reciprocal Rank fixes exactly that blind spot. MRR was standardized in [the TREC question-answering track](https://trec.nist.gov/data/qamain.html) long before RAG existed, further evidence that retrieval is a decades-old IR problem, not a new one invented by LLMs. MRR doesn't just ask whether the right chunk showed up, it asks how high up: it's the average of one over the rank of the first relevant result, so a chunk at rank 1 scores a full point and one limping in at rank 9 scores barely a tenth of a point. This is the metric that catches "technically in top-10, so hit rate called it a pass, but ranked ninth and the generator's context window only fits the top 3." Hit rate tells you the chunk existed. MRR tells you whether it mattered.

[src/metrics/mrr.py](https://github.com/Autonoma-Tools/how-to-test-rag-retrieval/blob/main/src/metrics/mrr.py)

### Context Precision and Recall

[Context precision](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/context_precision/) measures the opposite kind of waste: of everything you retrieved, how much of it was actually relevant? Retrieve 10 chunks and only 2 are on-topic, and you've diluted the generator's context with 8 chunks of noise, exactly the situation where a model starts blending irrelevant details into an answer that reads confident and is quietly wrong. Context recall asks the complementary question: did you retrieve everything needed to answer the query fully, or just part of it? A retriever that finds one relevant paragraph out of three needed for a complete answer will produce a partial, misleadingly confident response, and neither hit rate nor MRR will flag it, because technically, a relevant chunk did show up.

[src/metrics/context_precision_recall.py](https://github.com/Autonoma-Tools/how-to-test-rag-retrieval/blob/main/src/metrics/context_precision_recall.py)

Be honest about what each one is actually telling you, because conflating them is how teams end up chasing the wrong fix. A low hit rate means your retriever isn't finding the right document at all: check your embedding model, your chunking, your index. A low MRR with a decent hit rate means the right document is in there but buried: check your ranking or reranking step. Low precision with a fine recall means you're retrieving too much noise: tighten k or add a reranker. Low recall with fine precision means you're retrieving too little: the chunk boundaries may be splitting an answer across pieces you're only grabbing one of.

## How to Test Vector Search Accuracy Directly

Underneath all four metrics sits one direct question: for a given query, does the top-k set from your vector search actually contain the chunk you know is relevant? That's a narrower, more mechanical test than the aggregate metrics above, and it's worth running on its own because the failure modes at this layer are specific and not that hard to catch once you know where to look.

An embedding model mismatch between index-time and query-time is the most common one: someone bumps the model version for new documents without re-indexing the old ones, and now half the index lives in a different vector space than the other half, with similarity scores meaningless across the split. Chunk boundaries are the second: a chunking strategy that splits one answer across two chunks means neither scores high enough to surface alone. An ANN index like [HNSW](https://arxiv.org/abs/1603.09320) or IVF is deliberately approximate, trading recall for speed, so accuracy has a ceiling below 100% by design, not by bug. Metadata filters are a quieter failure: a filter meant to narrow results to the right tenant can silently exclude the correct chunk if tagged wrong at ingestion, leaving the query looking like it had no good match.

The blind spot worth calling out on its own: vector search is built to match semantic meaning, and it's famously bad at exact-identifier lookups. Ask it to find "the invoice for order 48291" and a dense retriever may confidently return three different invoices, because "order," "invoice," and a nearby-looking number cluster close together in embedding space while the literal string `48291` carries almost no semantic weight. If your application needs exact-ID lookups, that's a job for a keyword or hybrid search layer, not a pure semantic retriever, and testing for this means including exact-match queries in your labeled set on purpose, not assuming semantic similarity covers them.

## Building a Labeled Retrieval Test Set

None of the metrics above mean anything without a labeled set: queries paired with the chunk ID (or IDs) you already know are the right answer. This is the part almost nothing written about RAG evaluation actually walks through, because most teams assume they need a dedicated labeling effort before they can start, and then never start.

You don't need a labeling team, you need to mine data you already have. Real user queries pulled from production logs are the highest-signal source: the actual distribution of questions, not a set someone imagined in a meeting. Support tickets are the second source, the ticket is the query and the document the agent linked is the expected chunk, a free label. The third source works when the first two are thin: ask an LLM to generate a couple of plausible questions per chunk, then have a human spend thirty seconds confirming or rejecting each pair before it enters the set. That confirmation step matters, an unverified LLM-generated set just tests whether your retriever agrees with the model that wrote the questions, which is circular.

Thirty to fifty labeled queries is enough to start gating a build on. It won't cover every edge case in your domain, but it's enough to catch the regressions that matter: an index rebuild that silently drops documents, an embedding model swap that reshuffles the neighborhood, a chunking change that splits answers differently than before.

[tests/fixtures/labeled_queries.json](https://github.com/Autonoma-Tools/how-to-test-rag-retrieval/blob/main/tests/fixtures/labeled_queries.json)

> **Diagram:** Six labeled queries against a vector index, showing at what rank each one.

*Hit rate treats rank 1 and rank 9 as equal passes. MRR does not. The exact-identifier query (invoice #48291, buried at rank 9) is exactly the failure MRR is built to surface and hit rate alone would hide.*

## Gating the CI Build on Retrieval Metrics

A labeled set only earns its keep once it's wired into a build that fails when retrieval regresses. The pattern that works is a full pytest suite that loads the labeled fixture, runs every query through the retriever, computes the aggregate metrics across the whole set, and asserts each one against a threshold.

[tests/test_retrieval_regression.py](https://github.com/Autonoma-Tools/how-to-test-rag-retrieval/blob/main/tests/test_retrieval_regression.py)

Set thresholds on regression, not on an imagined ideal. A brand-new retriever rarely starts at a hit rate of 0.95, and gating the very first CI run at a number nobody has actually hit yet just means the build never goes green and the check gets disabled within a month. Measure your current baseline honestly, set the threshold a few points below it as a floor, and ratchet the floor up over time as the system improves. The goal of the gate is "did this change make retrieval worse," not "is retrieval perfect," and those are different bars with very different failure costs if you confuse them. The same ratchet-the-floor pattern applies to generation-side evals, covered in [how to run LLM evals in CI/CD](/blog/how-to-run-llm-evals-in-ci-cd).

[.github/workflows/retrieval-regression.yml](https://github.com/Autonoma-Tools/how-to-test-rag-retrieval/blob/main/.github/workflows/retrieval-regression.yml)

The other way a gate gets disabled within a month is quieter than a threshold nobody can hit: it stops matching the code. Chunking moves, the retriever is swapped, the feature around it is rewritten, and the labeled set keeps asserting against a shape the system no longer has. On the behavioral half of this problem that upkeep is automated rather than scheduled: [Autonoma](https://getautonoma.com)'s Diffs Agent reads each pull request's diff and adds, updates, or deprecates the end-to-end cases the change affects, which is the same instinct as ratcheting a floor applied to the tests themselves instead of the numbers. Your labeled fixture still needs a human. The cases above it don't.

When the gate fails, resist the reflex to touch the prompt. A retrieval-metric failure means the problem is upstream of the generator: check whether the index was rebuilt, whether the embedding model version changed, whether a chunking change shifted boundaries, or whether new documents landed with the wrong metadata tags. Fix the retrieval layer, rerun the labeled set, and only then look at generation if the retrieval metrics are back to baseline and the answer is still wrong.

## How Autonoma Catches the Failure Retrieval Metrics Miss

Here's what a broken retriever looks like from the outside, because it never looks broken. The user asks a specific question. The retriever, silently, hands the generator the wrong chunk, close enough in embedding space to seem plausible, wrong enough to make the answer false. The generator does its job faithfully: it summarizes what it was given, fluently, in well-formed sentences, often citing a source. No exception fires. Nothing appears in an error log. The response looks, by every surface signal, like a good answer. It is confidently, cleanly wrong, and the one metric that would have caught it (hit rate on a labeled set, computed before this query ever reached a real user) was simply never run.

That failure mode has a second layer most retrieval metrics can't see at all: even a retriever that scores perfectly on hit rate and MRR only proves the right chunk was returned, not that the user actually got the right experience in the product. The retrieved chunk can be exactly correct and the feature can still be broken, because the answer renders in the wrong panel, the citation link 404s, the streaming response cuts off mid-sentence, or the "no results found" empty state never fires when it should have. That gap between "retrieval was correct" and "the user's screen showed the correct thing" is behavioral, not a retrieval metric at all, and it's the layer Autonoma tests directly. Our Planner reads the application code around the retrieval feature and plans end-to-end cases from it, including the database state each case needs, and the Executor drives the real UI to confirm the retrieval win actually showed up where the user was looking.

> **Retrieval metrics pass. Does the feature work?** Autonoma runs agentic end-to-end tests on every pull request. [Try Autonoma](https://autonoma.app).

## Retrieval Metrics at a Glance

| Metric | What it measures | Bug it catches | Starting threshold |
| --- | --- | --- | --- |
| Hit rate / recall@k | Is the chunk in top-k at all | Retriever misses the doc entirely | 0.80+ at k=5 |
| MRR | How high the chunk ranked | Buried at rank 8-9, unused by generator | 0.60+ |
| Context precision | Share of retrieved chunks that are relevant | Noisy context diluting the prompt | 0.70+ |
| Context recall | Share of needed info actually retrieved | Partial, incomplete answers | 0.75+ |

These starting thresholds are opinionated defaults, not an industry standard. Treat them as a floor to beat on day one, then replace them with your own measured baseline.

Retrieval is, if anything, more deterministic than generation, which is why it's worth asserting on this hard. Same query, same index, same chunks, no sampling temperature to shrug off. The real non-determinism has three sources: re-indexing changes what's in the store, an approximate ANN index trades exactness for speed by design, and an embedding model version bump silently reshuffles the neighborhood since old and new vectors aren't comparable. Handle all three the same way: assert on chunk IDs with exact equality where a query has one correct answer, use threshold assertions on the aggregate metrics rather than expecting every query to pass in isolation, and pin the embedding model version in your test config so an upstream upgrade shows up as a CI failure instead of a support ticket.

If retrieval is solid but you're still seeing bad answers, the fault likely sits one layer over: our guide to [testing for AI hallucinations](/blog/how-to-test-for-ai-hallucinations) covers faithfulness checks for when the generator drifts from even a correctly retrieved chunk. Once retrieval is gated, [testing a full RAG pipeline](/blog/how-to-test-a-rag-pipeline) covers the end-to-end layer above this one, and [RAG evaluation metrics](/blog/rag-evaluation-metrics) goes deeper on the broader metric set.

Put in order, the whole method is short enough to hold in your head. Isolate retrieval from generation so a failure has one address instead of two. Label a small set of real queries with the chunks that should answer them. Compute hit rate and MRR on that set, add context precision and recall when partial answers are the complaint, and gate the aggregate rather than any single query. Set the threshold below your measured baseline and ratchet it, pin the embedding model version, and treat a red build as an index or chunking problem until the metrics say otherwise. That gets you a retriever you can trust to return the right chunk.

What it does not get you is a feature you can trust, and the difference is worth being blunt about because it decides where Autonoma belongs. Every number above is computed on what the retriever handed back, never on what the user saw. Autonoma sits above that boundary: it computes no retrieval metric and ranks no chunks, it drives the running application and asserts the retrieved answer rendered, linked, and fell back the way it was supposed to. Keep the labeled set as your retrieval gate. Add a behavioral gate above it, because a perfect hit rate and a broken feature are entirely compatible.

## Frequently Asked Questions

## Frequently Asked Questions

### How many labeled queries do I need to test RAG retrieval?

Thirty to fifty labeled query-to-chunk pairs is enough to start gating a CI build on. It won't cover every edge case, but it's enough to catch real regressions: an index rebuild that drops documents, an embedding model swap that reshuffles rankings, or a chunking change that splits answers differently. Grow the set over time by adding a case every time a real production query fails.

### What's a good hit rate for RAG retrieval?

There's no universal number, because it depends on your document set and query difficulty, but 0.80 or higher at k=5 is a reasonable starting bar for most applications. More important than hitting an absolute number is measuring your own baseline honestly and gating on regression from that baseline, not on an imagined ideal you haven't actually achieved yet.

### Should I test retrieval separately or test the whole RAG pipeline?

Both, but test retrieval separately first. Isolating retrieval from generation turns a slow, expensive, LLM-in-the-loop test into a fast, deterministic, information-retrieval test that runs on every commit. Once retrieval is solid and gated in CI, layer end-to-end pipeline tests on top to catch faithfulness and answer-quality issues that only show up when generation is involved.

### Does vector search work for exact-ID or keyword queries?

Not reliably. Dense vector search is built to match semantic meaning, not literal strings, so a query for a specific ID or exact term can return semantically similar but factually wrong results, because the surrounding language clusters closely in embedding space even when the specific identifier doesn't match. If your application needs exact lookups, add a keyword or hybrid search layer, and include exact-match queries in your labeled test set specifically to catch this.

### How do I test retrieval without a labeled dataset?

Mine one instead of waiting for someone to build it. Real user queries from production logs paired with the documents users ultimately engaged with are the highest-signal source. Support tickets are a second source, the ticket is the query and whatever document resolved it is the label. A third option is generating candidate questions per chunk with an LLM and having a human spend a few seconds confirming or rejecting each one before it enters the set, which keeps the labels honest instead of circular.

### What causes a RAG retriever to return the wrong chunk?

The most common causes are an embedding model mismatch between when documents were indexed and when queries are run, chunk boundaries that split a single answer across pieces, an approximate ANN index trading recall for speed, metadata filters silently excluding the correct document, and semantic search's known weakness on exact-identifier or keyword-style queries.

---

This is the markdown variant of <https://getautonoma.com/blog/how-to-test-rag-retrieval>, served by content negotiation (`Accept: text/markdown`) and also available directly at <https://getautonoma.com/md/blog/how-to-test-rag-retrieval>.

Other agent surfaces: [llms.txt](https://getautonoma.com/llms.txt), [resource catalog](https://getautonoma.com/.well-known/ai-catalog.json), [developer portal](https://getautonoma.com/developers), [sitemap](https://getautonoma.com/sitemap.xml).
