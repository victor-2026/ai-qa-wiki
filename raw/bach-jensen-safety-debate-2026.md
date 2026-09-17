# Bach vs Jensen: AI Safety as Engineering vs Market Failure (2026)

**Source:** LinkedIn post by Linas Beliūnas (Dreamforce commentary) + James Bach response
**Date:** 2026-09-17
**Context:** Jensen Huang spoke at Dreamforce about AI safety regulation

---

## Jensen Huang's Position (NVIDIA CEO)

> "Safety is an engineering problem, not a legal one."

- If your model isn't safe, don't ship it
- Not confident in safety? Don't release it
- Not confident in capability? Keep testing
- Confident in product? "Run as fast as you can"
- New AI laws? Market forces already give companies reason not to ship unsafe products
- Rejects the idea that safety requires the entire industry to move at the speed of its most cautious lab

**Commercial incentive:** NVIDIA sells compute powering the AI race. More training = more NVIDIA infrastructure.

---

## James Bach's Response

> "What he's saying is beside the point. The companies know how to test. But market forces do NOT optimize for safety."

Key insight: "if you FEEL that things are out of control" doesn't work in an environment where everyone is taking big risks because they believe a tiger is chasing them.

**Translation:** Market creates urgency (tiger chasing). Urgency overrides safety. "Feeling safe" ≠ "being safe."

---

## The Debate Framing

| Position | Jensen | Bach | Our Position (Article 27) |
|----------|--------|------|---------------------------|
| Safety is | Engineering problem | Market failure | Structured verification |
| Solution | Ship when confident | Cannot self-regulate | Per-risk-tier gates |
| Mechanism | Test more | External oversight | Evidence-based attestation |
| Speed | Fast when ready | Market too fast | Structured gates at each tier |
| Who decides | Engineer | Market + regulation | Attestor (evidence) + human (approval) |

---

## Connection to Our Work

- **Article 22 (seams):** external boundaries = where market forces fail. Market optimizes for speed, not safety at integration points.
- **Article 27 (governance):** QA role = structured evidence gates, not "feeling" safe. B0-B3 tiers are the practical answer to Jensen's "ship when confident" AND Bach's "market doesn't optimize for safety."
- **Per-risk-tier framework:** neither pure engineering (Jensen) nor pure regulation (Bach). Structured verification = the middle path that actually works.
- **Tornhill's "tooling enforces what you don't inspect":** same principle — safety through architecture, not through market incentives or feelings.
- **TestMu AI verdict (Green/Yellow/Red):** production-readiness = decision, not number. Jensen's "confident" needs a framework, not a feeling.
- **FinRA compliance (TestMu):** regulated industries already have this pattern. Agent output = communication = supervised record. The rest of the industry needs the same structure.

---

## Why This Matters for Article 27

The Jensen/Bach debate is the EXTERNAL CONTEXT for Article 27's thesis:
- Jensen is right: safety IS an engineering problem (testing, verification)
- Bach is right: market forces alone DON'T solve it (urgency overrides safety)
- Article 27's answer: structured verification gates (B0-B3) = engineering + governance. Not regulation, not market forces. Evidence.
