---
title: "QA and Evolutionary Architecture (Tiago Gomes, Thoughtworks)"
type: article
updated: "2026-09-22"
tags: [fitness-functions, evolutionary-architecture, qa-role, verification]
---

# QA and Evolutionary Architecture (Tiago Gomes, Thoughtworks 2026-09-20)

**Source:** https://www.linkedin.com/pulse/qa-evolutionary-architecture-tiago-gomes-hhf5f/ (Tiago Gomes, Lead Consultant @ Thoughtworks; revisits his 2024 "QA as a Key Driver in Evolutionary Architecture")
**Lineage:** Building Evolutionary Architectures — Neal Ford, Rebecca Parsons, Patrick Kua, Pramod Sadalage (Thoughtworks). Also "Sensible Defaults" at Thoughtworks.

## Thesis
Architecture is not a blueprint to protect from change — it should be designed to support change while preserving the qualities that matter. QA is not the gatekeeper of quality; it can be the facilitator of better conversations, clearer signals, and faster learning. Fitness functions make architectural intent visible, measurable, continuously actionable.

## Key Concepts
- **Fitness function** — automated, measurable check of whether the system still meets an architectural expectation. Gives feedback: is architecture moving toward intent, or quietly drifting?
- **Architectural drift** — slow erosion via "small shortcut here, urgent integration there," individually invisible, accumulating into costly unchangeable systems.
- **Examples of fitness functions:** performance test protecting a critical journey, contract test for service evolution, architectural test preventing cross-module dependencies, security checks, observability checks (structured logs, metrics, traceability).

## QA Angle (why relevant)
- QA professionals are well-positioned to ask risk/feedback/evidence questions: what could go wrong, what assumptions, how do we know it still works under pressure, what does "good" look like.
- These are architectural questions, not just feature-testing questions.
- Some architectural characteristics are only learnable in production (real traffic, actual diagnosability, actual availability) → quality and operability are joined.

## Key Principles
1. **Value = few meaningful signals, not long checklists.** Pipelines produce information, not insight. A fitness function must answer a meaningful question and produce an actionable decision, or teams learn to ignore it.
2. **Staged gating.** Not every fitness function starts as a strict gate — visibility first (measure deployment duration, response time, coupling, cloud cost, accessibility, log quality), then baseline + team agreement on "acceptable," then act.
3. **Quality is contextual.** No universal threshold; the question is "which qualities are essential for this product, these users, this business moment?" (payment platform vs internal reporting app differ).
4. **Fitness-Function-driven Development** expresses architectural intent as code, measures continuously, improves trade-off decisions with evidence — does not replace human judgement.

## Convergences with Our Work
- Staged gating (visibility → baseline → gate) = **per-risk-tier B0-B3 ramp** (independent convergence with QAEverest framework).
- Contextual thresholds = per-risk-tier rationale: critical (payment/auth) vs cosmetic cannot share one bar.
- "Pipelines produce info not insight" = mutation-matrix "assertion matters, not coverage count" + Klain "more tests ≠ better testing".
- Production-only characteristics = our "content must die to be validated"/live-evidence angle + DORA observability.
- QA as facilitator vs our attestation-gate: complementary — they make quality visible, we make it independently verifiable ("author can't be examiner").
- Fitness functions = governance harness = Tornhill "tooling enforces what you don't inspect" + Dhruv Bansal "harness configuration is a file".

## Uses
- Article 26/29: quality as system property, continuous verification; architecture guardrails framing.
- Article 27: noise-free evidence, meaningful-signal selection.
- Counter-example note: Tiago's own example of coupling = contract seams = Qodo Software Map "contract tracking" (risk heat map across repos).

## Related
- [[wiki/101-beginner-rag-architecture]] (skill stack)
- [[wiki/martinfowler-making-data-ready-agentic-ai-2026]] (Thoughtworks affiliate? separate — Fowler is ThoughtWorks; cross-company lineage)
- [[wiki/vector-databases-fintech-2026]]
- per-risk-tier (QAEverest) — see outreach/active/Rupesh in Positions-CV-CL