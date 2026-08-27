# Testing AI by Jason Arbon: Wiki Index

**Book:** *Testing AI: Engineering Confidence in Non-Deterministic Systems*  
**Author:** Jason Arbon  
**Primary theme:** confidence engineering for AI-generated code, agents, models and products.

This wiki organizes the publicly available Knowledge Edition, the author's legal draft preview and the official chapter carousels. It is a reference map, not a replacement for the final book. Chapter summaries are a synthesis of the author's public briefs plus a QA interpretation for this wiki.

## Legal Access

- **Official book site:** https://www.testingaibook.com/
- **Full author draft preview:** https://icebergqa.com/book/draft.html
- **Public Knowledge Edition:** https://www.testingaibook.com/knowledge/index.html
- **Free copy request for QA and engineering leaders:** https://icebergqa.com/
- **Final print and Kindle edition:** https://www.amazon.com/dp/B0H8J9GCK1
- **Test Guild interview with Jason Arbon:** https://testguild.com/podcast/a600-jason
- **Public coding-agent skills:** https://github.com/jarbon/testing-ai-skills

The Knowledge Edition contains 21 chapter maps and 194 short, citable concept briefs. The IcebergQA page is a draft for comments and exposes the complete working manuscript in the browser. It is not an unofficial copy and should not be repackaged or redistributed.

## Local Wiki Sections

- [Chapters 1-8: Evidence Foundations](testing-ai-book-evidence-foundations.md)
- [Chapters 9-11: Generated Code and the Confidence Engineer](testing-ai-book-generated-code-confidence-engineer.md)
- [Chapters 12-18: Data, Security and Dynamic Systems](testing-ai-book-security-dynamic-systems.md)
- [Chapters 19-21 and Appendices: Governance, Playbook and Future](testing-ai-book-playbook-future.md)

## Recommended Reading Paths

### QA and Engineering Leadership

1. Chapter 1 - move beyond one-run demos.
2. Chapter 2 - turn tests into release evidence.
3. Chapter 7 - define release readiness and escalation.
4. Chapter 10 - identify false-confidence patterns.
5. Chapter 11 - connect evidence to decisions and ownership.
6. Chapter 20 - build the minimum viable AI quality system.

### AI Testing and Evaluation

1. Chapters 1-4 - variance, sampling and statistical reasoning.
2. Chapter 5 - human and LLM judges.
3. Chapter 6 - product-specific evals and benchmark blind spots.
4. Chapter 8 - tracing, RAG, cost and production operations.
5. Chapter 13 - threat models, prompt injection and tool permissions.

### AI-Generated Code and Agents

1. Chapter 2 - evidence and release gates.
2. Chapter 7 - tool trajectories and human escalation.
3. Chapter 9 - generated code, generated tests and review loops.
4. Chapter 10 - anti-overfit and false-confidence traps.
5. Chapter 11 - the Confidence Engineer role.
6. Appendix: Testing AI Review Loops With Coding Agents.

## Complete Chapter Map

### Chapter 1 - The End of One-Run Testing

Replace brittle exact assertions with criteria, repeated runs and variance-aware scoring. The important question is not whether one output was good, but what behavior distribution the system produces.

[Official chapter](https://www.testingaibook.com/knowledge/chapter-01.html) · [PDF carousel](https://www.testingaibook.com/carousels/testing-ai-chapter-1-linkedin-carousel.pdf)

### Chapter 2 - From Tests to Release Evidence

Turn cases into evidence packets containing samples, slices, traces, reviewer decisions and explicit gates. Metamorphic testing, risk-based sampling and replayable logs make release decisions defensible.

[Official chapter](https://www.testingaibook.com/knowledge/chapter-02.html) · [PDF carousel](https://www.testingaibook.com/carousels/testing-ai-chapter-2-linkedin-carousel.pdf)

### Chapter 3 - Sampling and Uncertainty

Treat one run as an anecdote. Report sample counts, confidence intervals, repeat-run distributions and the difference between model-reported confidence and measured statistical confidence.

[Official chapter](https://www.testingaibook.com/knowledge/chapter-03.html) · [PDF carousel](https://www.testingaibook.com/carousels/testing-ai-chapter-3-linkedin-carousel.pdf)

### Chapter 4 - Statistical Tests for AI Quality

Choose tests based on data shape, state the null hypothesis, report effect size and practical risk, and control false discoveries when comparing many prompts, models or slices.

[Official chapter](https://www.testingaibook.com/knowledge/chapter-04.html) · [PDF carousel](https://www.testingaibook.com/carousels/testing-ai-chapter-4-linkedin-carousel.pdf)

### Chapter 5 - Judges, Humans, and Disagreement

Treat raters and LLM judges as measurement systems. Define rubrics, calibrate against trusted humans, measure disagreement and allow the judge to abstain when it is weak.

[Official chapter](https://www.testingaibook.com/knowledge/chapter-05.html) · [PDF carousel](https://www.testingaibook.com/carousels/testing-ai-chapter-5-linkedin-carousel.pdf)

### Chapter 6 - Building Evals That Matter

Define the behavior, user value and oracle before choosing a benchmark. Product-specific evals, risk-weighted metrics and blind-spot analysis matter more than inherited leaderboard numbers.

[Official chapter](https://www.testingaibook.com/knowledge/chapter-06.html) · [PDF carousel](https://www.testingaibook.com/carousels/testing-ai-chapter-6-linkedin-carousel.pdf)

### Chapter 7 - Release Readiness for AI Systems

Release is the start of production measurement, not the end of testing. Evaluate agent trajectories, tool calls, side effects, cost, latency and human escalation rules.

[Official chapter](https://www.testingaibook.com/knowledge/chapter-07.html) · [PDF carousel](https://www.testingaibook.com/carousels/testing-ai-chapter-7-linkedin-carousel.pdf)

### Chapter 8 - Operating AI: Observability, Relevance, and Economics

Trace input, prompt assembly, retrieval, model calls, tools, filters and user-visible output. Separate retrieval from generation failures and treat cost, latency and rollback as quality outcomes.

[Official chapter](https://www.testingaibook.com/knowledge/chapter-08.html) · [PDF carousel](https://www.testingaibook.com/carousels/testing-ai-chapter-8-linkedin-carousel.pdf)

### Chapter 9 - Generated Code Changes the Job

Generated code can compile and still be wrong in integration, security, privacy, permissions or deployment. AI-generated tests can inflate coverage without protecting behavior, so independent review and execution evidence are required.

[Official chapter](https://www.testingaibook.com/knowledge/chapter-09.html) · [PDF carousel](https://www.testingaibook.com/carousels/testing-ai-chapter-9-linkedin-carousel.pdf)

### Chapter 10 - Anti-Patterns That Create False Confidence

Name the confidence trap before proposing a fix. Replace green/red theater, aggregate scores, one-run demos and prompt whack-a-mole with distributions, blockers, slices and evidence.

[Official chapter](https://www.testingaibook.com/knowledge/chapter-10.html) · [PDF carousel](https://www.testingaibook.com/carousels/testing-ai-chapter-10-linkedin-carousel.pdf)

### Chapter 11 - The Confidence Engineer

The Confidence Engineer connects product intent, code, tests, evals, traces, rollout and business consequences. The role combines builder, tester, product thinker and evidence owner.

[Official chapter](https://www.testingaibook.com/knowledge/chapter-11.html) · [PDF carousel](https://www.testingaibook.com/carousels/testing-ai-chapter-11-linkedin-carousel.pdf)

### Chapter 12 - Data, Bias, Raters, and Incentives

Quality is shaped by data sources, labels, raters, incentives and deployment feedback. Use slices, counterfactuals and train/test audits to expose gaps hidden by averages.

[Official chapter](https://www.testingaibook.com/knowledge/chapter-12.html) · [PDF carousel](https://www.testingaibook.com/carousels/testing-ai-chapter-12-linkedin-carousel.pdf)

### Chapter 13 - AI Security and Guardrails

Threat-model every untrusted channel, including retrieved pages, tool output, files, OCR, images and external APIs. Convert prompt injection, MCP permissions and guardrail failures into replayable release-blocking evals.

[Official chapter](https://www.testingaibook.com/knowledge/chapter-13.html) · [PDF carousel](https://www.testingaibook.com/carousels/testing-ai-chapter-13-linkedin-carousel.pdf)

### Chapter 14 - Frontier Safety and Containment

Separate frontier safety from ordinary product bugs. Test dangerous capabilities, deception, evaluation awareness, tool misuse and containment without turning the test into a capability tutorial.

[Official chapter](https://www.testingaibook.com/knowledge/chapter-14.html) · [PDF carousel](https://www.testingaibook.com/carousels/testing-ai-chapter-14-linkedin-carousel.pdf)

### Chapter 15 - How Models Work

Model mechanics create test surfaces: tokenization, context, sampling, reward tuning, multimodal processing and fine-tuning. A task improvement can regress unrelated capabilities.

[Official chapter](https://www.testingaibook.com/knowledge/chapter-15.html) · [PDF carousel](https://www.testingaibook.com/carousels/testing-ai-chapter-15-linkedin-carousel.pdf)

### Chapter 16 - Introspection: White-Box Testing Networks

Use attention, activations, probes and sparse autoencoders as triage evidence, not proof of correctness. Validate the internal measurement system against known-good, known-bad and ambiguous cases.

[Official chapter](https://www.testingaibook.com/knowledge/chapter-16.html) · [PDF carousel](https://www.testingaibook.com/carousels/testing-ai-chapter-16-linkedin-carousel.pdf)

### Chapter 17 - Personalized and Dynamic AI Products

Test at N=1. Dynamic UI, memory, ranking, tone, privacy and accessibility become behavior surfaces that need real traces, representative raters and portability checks.

[Official chapter](https://www.testingaibook.com/knowledge/chapter-17.html) · [PDF carousel](https://www.testingaibook.com/carousels/testing-ai-chapter-17-linkedin-carousel.pdf)

### Chapter 18 - Embodied and Long-Running AI Systems

Use simulation for breadth and safety, then validate critical cases physically. Test safe inaction, recovery, permissions, drift, long-run memory, cost growth and human operators.

[Official chapter](https://www.testingaibook.com/knowledge/chapter-18.html) · [PDF carousel](https://www.testingaibook.com/carousels/testing-ai-chapter-18-linkedin-carousel.pdf)

### Chapter 19 - Governance, Regulation, and Moral Futures

Turn governance and ethics into test inputs, evidence requirements, ownership and monitoring. Keep changeable legal facts separate from durable quality principles.

[Official chapter](https://www.testingaibook.com/knowledge/chapter-19.html) · [PDF carousel](https://www.testingaibook.com/carousels/testing-ai-chapter-19-linkedin-carousel.pdf)

### Chapter 20 - The Practical Playbook

Start with a small operating system: cases, repeated runs, traces, rubrics, slices, gates, monitoring and incident promotion. Make failures visible and reusable as future eval cases.

[Official chapter](https://www.testingaibook.com/knowledge/chapter-20.html) · [PDF carousel](https://www.testingaibook.com/carousels/testing-ai-chapter-20-linkedin-carousel.pdf)

### Chapter 21 - Predictions for the Tokenized Product Future

As generation becomes cheap, validation becomes the compute sink. The future quality layer will independently test AI-generated variants, dynamic products and systems that continuously update themselves.

[Official chapter](https://www.testingaibook.com/knowledge/chapter-21.html) · [PDF carousel](https://www.testingaibook.com/carousels/testing-ai-chapter-21-linkedin-carousel.pdf)

## High-Value Appendices

- [AI Quality Release Checklist](https://www.testingaibook.com/knowledge/ch183-quality-release-checklist.html)
- [How to Read an AI Eval Report](https://www.testingaibook.com/knowledge/ch184-read-eval-report.html)
- [Templates for AI Quality Work](https://www.testingaibook.com/knowledge/ch185-templates-quality-work.html)
- [Testing MCP Integrations](https://www.testingaibook.com/knowledge/ch189-mcp-integrations.html)
- [Testing SKILL.md](https://www.testingaibook.com/knowledge/ch191-skill-md.html)
- [Testing AI Review Loops with Coding Agents](https://www.testingaibook.com/knowledge/ch192-review-loops-coding-agents.html)
- [Modern EvalOps and AI Quality Platforms](https://www.testingaibook.com/knowledge/ch193-modern-evalops-quality-platforms.html)

## Related Wiki Topics

- [AI QA evidence layer](ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md)
- [AI Productivity Paradox and verification layer](ai-productivity-paradox-verification-layer-2026.md)
- [Offline evaluation trajectories](offline-evaluation-trajectories-2026.md)
- [Testing AI agent tool calls](testing-ai-agent-tool-calls-autonoma.md)
- [Mutation testing and anti-overfit](Mutation-testing-advanced-playwright.md)
- [Monitoring and observability](monitoring-observability.md)
- [AI testing map](ai-testing-map.md)

## Source Boundary

The official Knowledge Edition is a set of short, citable briefs, not the complete manuscript. The IcebergQA draft is explicitly a draft for comments. Claims in this wiki are therefore attributed to the public source and should not be treated as independent empirical validation of the book's arguments.





<!-- backlinks-start -->
### Backlinks
- [Modeloptimizingagainstqualitygateinsteadofactualproblem](wiki/modeloptimizingagainstqualitygateinsteadofactualproblem.md)
<!-- backlinks-end -->
