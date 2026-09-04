# QBurst: Quality Engineering Framework for Validating Agent Behavior

**Source:** https://www.qburst.com/blog/2026/09/a-quality-engineering-framework-for-validating-agent-behavior/ (Milan Thomas, QBurst)
**Date:** September 2026
**Tags:** #qe-framework #agent-behavior #execution-tracing #decision-validation #llm-as-judge #langsmith
**Raw:** [qburst-quality-engineering-framework-validating-agent-behavior-2026.md](../raw/qburst-quality-engineering-framework-validating-agent-behavior-2026.md)

---

## What It Is

QBurst's AI Quality Engineering Framework for enterprise agentic AI (case: leasing platform coordinating multiple agents + backend tools for property data). Thesis: non-deterministic agents need behavior validation, not just output validation — generated response may look correct while agent selected wrong API, omitted parameters, or hallucinated. Final-output-only testing creates false confidence.

Principle: **observable → evaluable → trustworthy.** Every interaction assessed at 3 layers before release-ready.

## Layer 1: Execution Tracing (What Happened)

LangSmith instrumentation captures every turn as structured runtime trace: agent routing, tool calls, arguments, outputs, intermediate reasoning checkpoints, final response metadata. Trace-first pipeline: events → normalized single schema → chronological trace persisted. Standardized traces enable replay, build-to-build comparison, divergence pinpoint.

## Layer 2: Decision Validation (Was It Right)

On top of traces: did system make right operational choices for intent?
- Standard evaluators: hallucination, toxicity, bias, fairness
- Custom task evaluators: e.g., tool-correctness (selected tool, parameters, invocation order for property questions)

Leasing case: failures were decision-quality errors, not crashes — fluent response via wrong tool path or incomplete params → inaccurate info. Checklist: correct agent routed? Appropriate tools selected? Parameters accurate? Response grounded or hallucinated?

## Layer 3: LLM-as-a-Judge (How Good)

Inputs: (1) conversation context from trace history, (2) tool-output evidence, (3) final response. Judge scores every turn on fixed rubric: factual accuracy, contextual relevance, data grounding, hallucination risk, overall usefulness. Turn + conversation aggregation → comparable metrics → conversational quality becomes regression-testable: model/prompt/toolchain drift detected pre-release.

## QE Impact

Failures isolated to exact layer: routing, tool choice, params, retrieval-vs-generation mismatch, low-quality response despite success. Shift:
- Pass/fail conversation checks → decision-level validation
- Manual transcript inspection → repeatable evaluator scoring
- "Looks reasonable" → evidence-backed grounding
- Post-release drift → pre-release regression detection

Stakeholders: QE gets deterministic diagnostics + reproducible evidence; app engineers see which decision failed; product gets release signals; clients get grounded correctness, not fluency.

## Production Governance

Functional testing stays but is one part. Behavior as testable engineering concern: same signals across model/prompt/toolchain changes; earlier regressions; evidence-backed releases. Shift: from "acceptable answer?" to "behaved appropriately to produce it?"

## Relevance to QA/QE

| QBurst Layer | QA Action |
|--------------|-----------|
| Execution tracing (LangSmith) | Require traces as evidence: routing, tool calls, args, outputs, checkpoints — replayable artifact |
| Decision validation (custom evaluators) | Add tool-correctness evaluator per workflow: right tool, right params, right order — catches fluent-but-wrong |
| LLM-as-judge (fixed rubric) | Score factuality, relevance, grounding, hallucination, usefulness per turn; aggregate for release gate |
| Three-layer gate | Block release unless all 3 pass; isolate failures to layer (routing vs tool vs response) |

## Critical Analysis

**Strengths:**
- Concrete enterprise case (leasing: pricing, availability, property) with exact failure taxonomy, not generic.
- Trace-first + fixed rubric + regression-testable quality — directly maps to evidence layer and per-risk-tier gate.

**Gaps:**
- LangSmith-centric; open-source alternative (OpenTelemetry + Jaeger) not discussed — vendor coupling risk.
- No numbers (precision/recall, cost per eval) — efficacy vs manual transcript review unquantified.

## Worked Example (Leasing Flow)

User asks: "3-bed near airport under $2k?" Trace shows: routed to property-search agent → called `searchListings` with `{beds:3}` but omitted `max_price` and `airport_radius` → returned 5-bed $3k listings → judge scores grounding low, hallucination risk high. Layer 2 catches wrong params even though response is fluent; fix is param mapping, not prompt.

## Checklist for Your Harness

- Emit trace per turn (routing, tool, args, outputs, checkpoints) in one schema.
- Add one custom evaluator per workflow (tool-correctness for your domain).
- Score every turn on 5 fixed dims; aggregate turn + conversation.
- Gate release on all 3 layers; file failures by layer (routing vs tool vs response).
- Re-run same suite on model/prompt/tool change; diff quality metrics for drift.

## FAQ Highlights

- "Isn't observability enough?" No — trace confirms invocation, not appropriateness for intent or correctness of decision.
- "Who uses the signals?" QE (diagnostics), app engineers (which decision failed), product (release), clients (grounded confidence).
- "Where to start?" One workflow, trace-first, one custom evaluator, fixed rubric — then expand.

## Cross-links

- Related: [Zalando agentic snapshot](zalando-agentic-engineering-snapshot-2026.md) (risk-based gate, Identity Broker)
- Related: [Martin Fowler making-data-ready](martinfowler-making-data-ready-agentic-ai-2026.md) (traceability, lineage)
- Related: [TestMu AI agentic regression](testmuai-agentic-regression-testing-2026.md) (4-level ladder, recall on skipped)
- QA evidence layer: [ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md](ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md)

---

*Ingested: 2026-09-04 · Via qburst.com fetch 2026-09-04*
