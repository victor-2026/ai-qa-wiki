# Testing AI: Evidence Foundations

This page summarizes Chapters 1-8 of Jason Arbon's *Testing AI*. The summaries use the official public Knowledge Edition and are adapted for QA, AI-agent testing and engineering leadership.

## Chapter 1: The End of One-Run Testing

**Official source:** https://www.testingaibook.com/knowledge/chapter-01.html

### Core idea

A single green run is an anecdote, not evidence, when the system can vary. Replace exact-output assertions with criteria that distinguish harmless variation from harmful variation. Repeat runs, establish a deterministic baseline where possible, and report the distribution rather than the luckiest result.

### Practical QA interpretation

- Define behavior properties before running the AI system.
- Use anchored scores such as 10/7/4/0 only when each anchor has observable meaning.
- Compare a controlled baseline with production variance to isolate instability.
- Treat variance itself as a result that needs explanation.

### Useful artifacts

- Variance table by case and run.
- Criteria-based assertion set.
- Scoring rubric with examples.
- Baseline versus production-variance rerun plan.

### Link to current work

This is the measurement foundation for AI-agent evaluation, mutation testing and the Article 16 verification-layer thesis: generation can scale faster than proof.

## Chapter 2: From Tests to Release Evidence

**Official source:** https://www.testingaibook.com/knowledge/chapter-02.html

### Core idea

Tests become useful to leadership when they become a release evidence packet: cases, risk slices, traces, reviewer decisions and explicit gates. Metamorphic checks help when there is no single correct output but there are relationships that should remain true.

### Practical QA interpretation

- Keep golden cases and fresh live samples; they catch different failures.
- Weight samples by business and safety risk instead of counting every case equally.
- Report slices so easy traffic cannot hide a dangerous subgroup.
- Log enough context to replay a failure and explain a reviewer decision.

### Useful artifacts

- Risk-weighted eval plan.
- Metamorphic test catalog.
- Stratified report with rare-failure section.
- Release gate with hard blockers and escalation rules.

### Link to current work

This connects directly to the AI QA evidence layer, Allure/DORA evidence and the human-review boundary in AI-generated test workflows.

## Chapter 3: Sampling and Uncertainty

**Official source:** https://www.testingaibook.com/knowledge/chapter-03.html

### Core idea

Sampling estimates behavior; it does not reveal the whole future. Report sample count and uncertainty beside every score. Prefer paired comparisons when the same cases run through two versions. Model confidence is a claim from the system, while statistical confidence is evidence about the system.

### Practical QA interpretation

- Choose sample size as a risk decision, not a fixed ritual.
- Increase evidence for rare but severe failures.
- Use confidence intervals rather than false precision.
- Repeat the same build when measuring flakiness or model variance.

### Useful artifacts

- Sample-size plan.
- Confidence-interval report.
- Repeat-run distribution.
- Explicit uncertainty note beside each metric.

### Link to current work

This is the statistical guardrail for benchmark claims such as 7x/20%, METR's felt-versus-measured contrast and agent pass-rate comparisons.

## Chapter 4: Statistical Tests for AI Quality

**Official source:** https://www.testingaibook.com/knowledge/chapter-04.html

### Core idea

The test must match the data: paired versus independent, numeric versus categorical, ordinal versus binary. State the null hypothesis before inspecting results. A p-value is evidence about a comparison, not permission to ship. Effect size, practical impact and false-discovery control matter too.

### Practical QA interpretation

- Decide what improvement would matter before running the experiment.
- Report effect size and operational risk with significance.
- Use chi-squared-style reasoning for failure categories, not only average scores.
- Correct for the number of prompts, models, slices and metrics examined.

### Useful artifacts

- Test-selection note.
- Null hypothesis and alternative.
- P-value plus effect-size summary.
- Multiple-comparison warning.

### Link to current work

This supports DORA-style evidence discipline and prevents a single favorable AI benchmark from being presented as a universal productivity result.

## Chapter 5: Judges, Humans, and Disagreement

**Official source:** https://www.testingaibook.com/knowledge/chapter-05.html

### Core idea

An LLM judge is a measurement instrument, not an objective truth machine. Define the human rubric first, calibrate judges against trusted human decisions, measure disagreement and allow the judge to abstain when it is weak.

### Practical QA interpretation

- Write evidence requirements into the rubric.
- Use calibration examples before scaling an LLM judge.
- Treat disagreement as a signal of ambiguity, missing context or legitimate diversity.
- Keep adjudication and escalation paths visible.

### Useful artifacts

- Rater rubric.
- Human calibration set.
- Inter-rater agreement report.
- Judge confidence and abstention policy.
- Adjudication workflow.

### Link to current work

This aligns with the local LLM-as-judge work, the evidence-layer distinction between model evals and downstream QA validation, and the human review gate in QAEverest.

## Chapter 6: Building Evals That Matter

**Official source:** https://www.testingaibook.com/knowledge/chapter-06.html

### Core idea

An eval is only useful when its target behavior, user value and oracle are explicit. Public benchmarks provide signals, but their task shape and blind spots do not automatically match a product. Build weighted metrics around product risk rather than leaderboard theater.

### Practical QA interpretation

- Write an eval specification before choosing a dataset.
- Separate benchmark relevance from benchmark popularity.
- Add adversarial and real-world samples to normal random samples.
- Version prompts, datasets, labels, judges and model routes.
- Stop celebrating a high-water mark produced by repeated noisy reruns.

### Useful artifacts

- Eval specification.
- Benchmark-to-product gap analysis.
- Weighted quality metric formula.
- Blind-spot list.
- Adversarial sampling plan.

### Link to current work

This is directly applicable to Gaia2, OpenApps, SOP-Bench, Toloka Arena and any comparison of AI testing agents.

## Chapter 7: Release Readiness for AI Systems

**Official source:** https://www.testingaibook.com/knowledge/chapter-07.html

### Core idea

Release is the beginning of real-world measurement. Regression checks should protect invariants rather than fossilize exact wording. Tool-using agents must be evaluated on the trajectory: plan, tool calls, permissions, side effects, recovery and final outcome.

### Practical QA interpretation

- Define what may vary and what must never vary.
- Test tool permissions and side effects separately from final answers.
- Create a human escalation matrix before production.
- Monitor cost, latency, failure clusters and severe outcomes after launch.

### Useful artifacts

- Release-readiness checklist.
- Agent trajectory scorecard.
- Human escalation matrix.
- Post-release monitor plan.

### Link to current work

This is the bridge from downstream Playwright validation to agent trajectory testing and release governance.

## Chapter 8: Operating AI - Observability, Relevance, and Economics

**Official source:** https://www.testingaibook.com/knowledge/chapter-08.html

### Core idea

The final answer is not enough to debug an AI system. Capture the full path: input, prompt assembly, retrieval, model call, tool calls, filters and user-visible result. For RAG, separate retrieval failure from generation failure. Cost, p95/p99 latency, token use and rollback are quality outcomes.

### Practical QA interpretation

- Define a trace schema before debugging production failures.
- Version prompts, policies, retrievers and tools alongside model versions.
- Use shadow and canary modes before full traffic.
- Test rollback and data contracts, not only happy-path output.
- Mine production traces for future regression and eval cases.

### Useful artifacts

- Trace schema.
- RAG failure taxonomy.
- Canary/shadow/rollback plan.
- Token and latency budget report.
- Production-trace mining loop.

### Link to current work

This maps to Allure evidence, OpenTelemetry GenAI fields, DORA reliability signals, agent tool-call testing and the QAEverest time-travel RCA concept.

## Cross-Chapter Pattern

Chapters 1-8 move the team through one argument:

1. One run is not proof.
2. A score without a sample and risk slice is incomplete.
3. A test without trace and reviewer rationale is weak release evidence.
4. A released AI system needs continuous monitoring, not a final test ritual.

The practical output is a small evidence system, not a larger pile of tests.

## Sources

- [Official Knowledge Edition index](https://www.testingaibook.com/knowledge/index.html)
- [Full author draft preview](https://icebergqa.com/book/draft.html)
- [Testing AI book index in this wiki](testing-ai-book-index.md)

















<!-- backlinks-start -->
### Backlinks
- [Agent Skills – Google/Kaggle Whitepaper (May 2026)](wiki/google-kaggle-agent-skills-whitepaper-2026.md)
- [Devqaexpert Qaeverestimport2000Cypresstests Confidencescore 2026 08 22](wiki/devqaexpert-qaeverestimport2000cypresstests-confidencescore-2026-08-22.md)
- [Keithklain Testingmindsetafterall 2026](wiki/keithklain-testingmindsetafterall-2026.md)
- [Modeloptimizingagainstqualitygateinsteadofactualproblem](wiki/modeloptimizingagainstqualitygateinsteadofactualproblem.md)
- [Wayne Roseberry Testers Do More Than Users 2026](wiki/wayne-roseberry-testers-do-more-than-users-2026.md)
<!-- backlinks-end -->
