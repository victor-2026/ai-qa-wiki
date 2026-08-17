# Goodhart's Law in AI Evaluation — hallucination rate example (Stephen Platten, "The Stoic Tester")

Source: LinkedIn post by Stephen Platten, Aug 2026 (~4d before 2026-08-17). Hashtags: #AI #AIEvaluation #AITesting.

## The argument

Metrics, KPIs and success criteria are important — they give a mechanism to assess whether the AI is doing the task "well". But they have limits and their own challenges. This leads to Goodhart's Law:

> "When a measure becomes a target, it ceases to be a good measure."

### Worked example: hallucination rate for a policy-Q&A AI

Setup: an AI that answers questions from company policies. Metric chosen: "How accurately does every statement in the answer reflect the source material?"

The easiest ways for the AI to improve that score:
1. Say less.
2. Stick closely to the wording of the document.
3. Avoid making connections between different parts of the source.
4. If any ambiguity is encountered — refuse to answer.

Result: hallucination rate goes down, accuracy against the source goes up. Looks like a win.

Question: have we actually built a better AI system? Maybe not — we may have built one that is better at passing the test. That is not the same thing.

The real question: can the AI give a useful, complete and trustworthy answer based on the information it has?

## Takeaways

- The metric we choose to measure matters, and how we measure it matters.
- Testers need to go further than the metric — that is where AI evaluation gets interesting.
- Classic Goodhart's Law pattern: optimizing the measured target degrades the unmeasured intent (usefulness, completeness, trustworthiness).

## Connection to existing wiki topics

- Anti-overfit guardrails: a metric being optimized by the system itself (or by the team) becomes a target — same trap as overfit assertions in mutation testing (surviving mutants = test optimizes for the assertion, not the behavior).
- LLM testing / evals: hallucination rate as a golden-dataset metric; boundary prompts; LLM-as-a-judge limits.
- Evidence-based QA: "better at passing the test vs better at the job" — downstream QA validation signals vs model evals (see evidence-layer article).
- Context engineering: refusal on ambiguity reduces coverage — the metric punishes useful synthesis.