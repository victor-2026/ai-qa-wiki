# CIGE: An Agentic AI Test Case Standard (Amazon, QRS 2026 Industry Track)

**Authors:** Vivek Krishna Choppa, Anusha Kovi (Amazon.com Services LLC, Washington, USA)
**Source PDF (immutable, in raw/):** raw/scipub-approval152129-48648126-cige-an-agentic-ai-test-case-standard.pdf (7 pages, uploaded 2026-09-23)
**Venue:** QRS 2026 Industry Track (acknowledgments thank QRS 2026 Industry Track reviewers)
**Context:** Test-case FORMAT standard for agentic execution: four fields {context, intent, guardrails, execution}. Storage-agnostic (JSON/YAML/TMS). Directly matches AWS summit session "Agentic Test Automation in Practice: An AWS Deep Dive into CIGE" (QA Leadership Summit Autumn 2026). Evidence grade: single-platform industry experience report (codeless agentic testing platform, enterprise workflows) - vendor-adjacent numbers, no control group described. Reported deltas: maintenance effort ~90% lower, false positives ~38% lower, avg execution time ~62% lower. Treat as directional, not independent.
**Extracted:** 2026-09-23 via pypdf, verbatim below.

---

## Abstract

Test automation is moving from fixed script replay to agent driven execution and judgement. An agent may read a goal, inspect product state, call tools, recover from small changes, and collect evidence before reporting a result. Existing test case formats do not give enough structure for this style of execution. Plain prompts mix setup, purpose, rules, and steps. Traditional scripts are repeatable, but they break when the product flow changes. This paper presents CIGE, a simple structure for agentic test cases with four fields: Context, Intent, Guardrails, and Execution. Context grounds the run. Intent captures the reason the test exists. Guardrails define what the agents must not do. Execution gives the first path to try and can be repaired when the product changes.

Keywords: Agentic Testing, Test Automation, Self-Healing Tests, Runtime Guardrails, Context Engineering.

## 1. Introduction (thesis)

Most automated tests assumed: the test case describes a path, the framework repeats it. That assumption weakens as UIs change, APIs evolve, auth moves, environments rebuild. Many failures are test drift or environment drift, not product defects. Agentic runners get a larger action space (less brittleness) but shift responsibility to the test case: it must state purpose, valid context, limits, and required evidence before a pass. A test case is no longer only steps.

## 2. Background and Related Work

CIGE is a layer for a different execution style, not a replacement. Positions vs: keyword-driven testing (ISO/IEC/IEEE 29119-5:2024), Page Object Model (Leotta et al. industrial Selenium study), BDD/Given-When-Then (mapping study notes evidence gaps), model-based testing, requirements-based generation, constrained combinatorial testing. Runtime safety: AgentSpec (customizable runtime enforcement, arXiv:2503.18666). Context engineering (Anthropic 2025): agents need the right information at the right time, not one mixed block. CIGE applies these at test-case level.

## 3. The CIGE Test Case Model

Four top-level fields: { context, intent, guardrails, execution }. Separation of concerns matters more than storage format.

- **Context:** operating ground; reusable prompts across tests; tool-search on demand instead of loading all tool definitions (progressive context disclosure + token optimization); skills-file per agent as lightweight capability index for routing, detailed tool contracts federated and loaded only at execution time.
- **Intent:** reason the test exists - capability under test, success criteria, failure criteria, evidence required for a pass. Intent is STABLE (a button can move, validation can move UI→API, reason stays). Intent is metadata for the whole case (blob-vs-DDB analogy): enables filtering, grouping, authoring new tests with optimal context. Every case uniquely identified by intent; intent rarely evolves; intent changes require human approval.
- **Guardrails (Runtime):** what agents must NOT do - block destructive actions, protect secrets, require approval before changing a test, require specific evidence before pass. Reduce false positives by stopping shortcuts that make final state look correct without validating. Shared control layer for multi-agent architectures, runtime-agnostic.
- **Execution:** first path to try; limits agent search space (UI steps, API calls, checks, expected observations). Steps are GUIDANCE, repairable when product changes as long as repair satisfies the same intent.

Example (workspace streaming flow): Context = staging, standard enterprise user, browser+screenshot+network-log tools, reveal policy (login notes first, diagnostics after connection failure). Intent = user can start streaming session; pass = connected state + first frame in latency window + no auth/policy error + screenshot + connection logs evidence. Guardrails = no resource deletion, no prod config change, no secrets in logs, no pass from UI text alone, no intent update without human approval. Execution = open client, sign in, start streaming, wait connected, capture evidence, validate.

## 4. Runtime Workflow

Agent treats fields differently. Flow: reveal minimal context → run execution with guardrails → on failure/FP: CLASSIFY first (product defect → bug report; environment drift → repair context; test drift → repair execution; false positive → stricter evidence rule/guardrail) → replay candidate repair in isolated environment → human-in-the-loop review → commit. Analyzer + self-healing agents cooperate; all auto-generated test-case updates reviewed by human.

## 5. Comparison (step fidelity → goal fidelity)

Step fidelity asks whether automation followed the expected path. Goal fidelity asks whether intended behavior was validated safely with enough evidence even if the path changed. Table vs formats: keyword-driven (+intent/guardrails/evidence/staged context around keywords); BDD (+separates behavior intent from repairable execution); POM (+vision-assisted execution, repair must not change purpose); model-based (+runtime structure, safety, evidence); requirements-based (+stable intent + approval boundaries, intent for coverage analysis); combinatorial (produces CIGE variants preserving context/guardrails/evidence).

## 6. Industry Experience

Applied in a codeless agentic testing platform (UI flows, service dependencies, env setup, business-rule validations). Stored: four fields + logs + evidence + failure categories + repair proposals + reviewer approvals. Reported: maintenance ~90% lower (changes limited to execution/context, purpose not rewritten); false positives ~38% lower (evidence rules + guardrails cut invalid pass paths); exec time ~62% lower (staged context cut prompt loading/exploration); self-healed updates validated before approval (isolated replay). Domain sketches: retail (intent "checkout with valid discount+tax" stable; guardrails block real orders/payments, require backend validation not UI-only); banking (guardrails encode compliance, audit trail, human approval for intent changes); healthcare (PHI protections, backend-service validation over UI).

## 7. Limitations and Future Work

Four next steps: (1) migration layers from BDD/keyword/POM/TMS records into CIGE; (2) schema for multi-agent execution (planner, executor, validator, guardrail-monitor roles); (3) evaluation under drift sources - selector changes, flaky envs, missing context, API contract changes, unavailable tools, prompt injection, changing business rules; (4) CIGE as portable artifact across workflows, infra, runtimes, validation tools.

## 8. Conclusion

Agentic automation needs cases more structured than prompts, less brittle than scripts. Separation of concerns reduces maintenance, FPs, exec time while giving humans and agents a reviewable artifact.

## References (selected)

ISO/IEC/IEEE 29119-5:2024 (keyword-driven); Leotta et al. 2013 (POM industrial study); Binamungu & Maro 2023 (BDD mapping); Schieferdecker 2012 (MBT); Yang et al. 2025 (requirements-based generation survey); Wu et al. 2019 (combinatorial); Rathnayake et al. 2026 (BDD+LLM); Wang et al. 2025 AgentSpec arXiv:2503.18666; Anthropic 2025 context engineering.
