# Amazon Science: When LLM Judges Agree, Should We Believe Them? (2026-08-26)

**Authors:** Krishna Balasubramanian (UC Davis, Amazon Scholar), Sasha Podkopaev (AWS applied scientist); coauthor Shiva Kasiviswanathan (acknowledged)
**Source:** https://www.amazon.science/blog/when-llm-judges-agree-should-we-believe-them
**Paper:** "Dependence-aware label aggregation for LLM-as-a-judge via Ising models", ICML 2026 - https://www.amazon.science/publications/dependence-aware-label-aggregation-for-llm-as-a-judge-via-ising-models
**Context:** LLM-as-a-judge methodology. Thesis: agreement count overstates evidence when judges share training lineage, prompts, model family, or blind spots. Solution: treat panel as a network, learn pairwise dependence (Ising model) + per-judge reliability, unsupervised (true labels latent, no human labels for training). Two variants: label-independent dependence (interpretable adjusted weights) and class-dependent (expressive, needs more data). Direct hit for our "author can't be examiner" / silent-false-negative thesis and verdict-layer eval design.
**Fetched:** 2026-09-23 via webfetch, verbatim substance below (nav/footer stripped).

---

## Core problem

RAG relevance check with 10 judges: 8 say relevant. Convincing - unless the 8 share a prompt template, training lineage, model family, or blind spot. Vote count then inflates evidence. Majority vote and weighted-majority vote both assume errors are independent - too optimistic for LLM judges (shared rubric interpretation, shared few-shot examples, same phrasing sensitivity).

## Method: panel as a network (Ising model)

Each judge keeps a reliability profile; PAIRS get relationship parameters (agree more than reliability predicts, incl. on shared mistakes; or complementary). Learns judge skill + judge similarity jointly, unsupervised: alternate between estimating per-item positive probability (soft, current best guess) and re-estimating reliability/dependence. Human labels used only afterward for measuring accuracy. Bonus use: learned network audits redundancy - which judges duplicate bias, which tasks split into clusters, whether adding a judge helps or duplicates bias.

## Evaluation

Three binary tasks (relevance classification, toxicity, summarization assessment), 10 judges at temperature zero. Dependence-aware vs weighted/uniform majority vote, max data: relevance 0.912 vs 0.820/0.804; toxicity 0.792 vs 0.694/0.695; summarization 0.806 vs 0.737/0.561. Gains 9-14% over best baseline once enough items and judges to estimate relationships.

## Best practices (for LLM-as-a-judge pipelines)

1. Evaluate the PANEL, not just individual judges - strong individuals can fail identically.
2. Model diversity = statistical diversity - mixing families helps only if error patterns change.
3. Inspect agreement structure - clusters reveal shared rubrics/behavior/task ambiguity, valuable even when labels don't change.
4. Report uncertainty with dependence in mind - 10 correlated votes != 10 independent votes.

Closing: when judges agree, ask why - independent evidence or shared blind spot. Aggregation must tell the difference.

## Use for us

- Formal backing for K-of-N / multi-judge design in verdict layer: votes must be dependence-discounted, not counted.
- Panel-diversity audit procedure maps to our attestation evidence (agreement-clustering as artifact).
- Pairs with Qodo "author can't be examiner" and CIGE evidence rules: independent EVIDENCE requirement is the same problem one layer up.
