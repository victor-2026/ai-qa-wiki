# Testing AI Systems Across All Four Layers — Testkube (2026-08-28)

**Source:** Atulpriya Sharma (Sr Dev Advocate, Testkube) https://testkube.io/blog/testing-ai-systems-four-layers — companion to delivery-pipelines piece. Honest vendor content (admits limits, flags Promptfoo acquisition by OpenAI Mar 2026).
**Use for us:** layer map for LLM-eval work; threshold references; demo repos.

## The 4 layers (tool per layer, outputs)

| Layer | Tests | Tool | Output / gate |
|-------|-------|------|---------------|
| Infrastructure | GPU allocated, model loaded, latency in bounds | NVIDIA Device Plugin checks in TestWorkflow | node/pod counters, pass/fail |
| Model | grounded + relevant (not just running) | RAGAS (faithfulness, answer relevancy) | mean/min/max per metric; fail < 0.80 |
| Orchestration/Agent | whole chain held (errors compound silently mid-chain) | DeepEval (faithfulness, contextual recall 0.75, relevancy 0.80) | results JSON, merge blocked on fail |
| Application | YOUR prompts/guardrails vs attackers (not abstract safety) | Promptfoo red-team (OWASP LLM Top 10) | attack report per vuln category |

## Key points (vendor-honest)

- Four tools, four formats, four dashboards by default — Testkube's pitch is orchestration (one catalog, one history), not evaluation. Right scoping, no overclaim.
- Cross-layer RCA admitted NOT proven yet ("natural next step", not shipped). Centralized visibility = precondition, not afterthought.
- Scope argument for Layer 4: model can pass general safety while YOUR app leaks system prompt — test the app, not the model.
- Failure compounding mid-chain (Layer 3) = same mechanism as our M4 duplicate diagnosis gap: symptom looks nothing like cause.

## Links

- Demo repos: RAG gate (DeepEval), Ragas example, Promptfoo example (all github.com/kubeshop/testkube-examples)
- Sibling pieces: delivery-pipelines (thresholds), quality-gates, four-layers part 1 (skipped layers)
- Our mapping: eval-threshold design (per-risk-tier), LLM-testing skill (6 approaches), Gulin thresholds-before-numbers

## See also

- [Smart Suites: AI-Driven Test Selection — Testkube (2026-04-22)](wiki/testkube-smart-suites-test-selection-2026-04.md)
