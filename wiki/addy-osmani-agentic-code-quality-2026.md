# Addy Osmani — Agentic Code Quality (2026)

**Source:** https://addyo.substack.com/p/agentic-code-quality
**Author:** Addy Osmani (Member of Technical Staff, Anthropic)
**Date:** 2026-08-08
**Engagement:** 120 likes, 8 comments, 8 restacks

---

## Core Thesis

> Software quality now depends on the constraints you set around your agents.

Too much code for anyone to read → quality checks must happen in harness, environment, and OS around the agent. Quality = collection of signals of varying importance.

---

## Constraint Taxonomy

| Constraint Type | When | Examples |
|----------------|------|----------|
| **Pre-work** | Before agent begins | Architecture rules, scoped permissions, sandbox limits |
| **During work** | While agent is working | Type checks, linting, unit tests, live feedback |
| **Post-work** | Before production boundary | Mutation testing, security scanning, browser tests, full test suite |

**Back-pressure throughout the pipeline**, not just at the end. Push every deterministic signal early and continuously.

---

## Quality Signals (Not Just Tests)

- Type systems (compilers reject invalid code)
- Unit tests, property tests, acceptance tests
- Mutation testing (generate variations, run against same tests)
- Code quality metrics (cyclomatic complexity, line length)
- Architecture rules via linting (ESLint)
- Security scanning

> "Don't fall for volume of checks alone... tighten or relax constraints deliberately."

---

## Scaling Verification

When verification can't keep up with generation:
1. Scale verification system (more capacity)
2. Reduce agent change rate (slow down)
3. Lower quality bar (dangerous)
4. Or: un-constrain in low-risk directions, tighten where it matters

> "By providing tighter constraints where we care the most, we can maximize throughput without sacrificing quality."

---

## Human Code Review Changes

Correctness is one dimension. Also: maintainability, performance, security, efficiency, comprehensibility. Human attention → most nuanced problems requiring judgment. Downstream humans pulled in only when automated guardrails break.

> "For now, much of the difference between useful agent output and slop still comes down to the skill of the team operating the loop."

---

## Key Quotes

- "Software quality now depends on the constraints you set around your agents."
- "An agent can propose anything. Your constraints decide whether a proposal is safe enough to ship."
- "The environment we're after is one where an agent can do real work, get feedback it can trust, and fail without doing much damage."

---

## Connections to Our Work

- **Constraints = quality gates = B0–B3 tiers:** our tiers formalize what Osmani describes as constraint-driven quality.
- **"Back-pressure throughout"** = per-risk-tier step 0 (relevance gate) + mutation matrix gates. Not just end-of-pipeline.
- **Mutation testing explicitly named** as quality constraint (launch ammo for VerdictGate).
- **"Skill of the team operating the loop"** = Article 27 "Guided QA Engineer." Human skill at operating verification, not running tests.
- **Scaling verification** = our staged ramp: start with tight constraints (B0), loosen as trust earns (B2/B3).

---

## Related Wiki

- `wiki/addy-osmani-human-judgment-software-factory-2026.md` — verification budget, factory taxonomy
- `wiki/addy-osmani-agentic-autonomy-levels-2026.md` — autonomy levels mapped to verification
- `wiki/addy-osmani-brownfield-agentic-engineering-2026.md` — zones as constraint levels

## See also

- [Addy Osmani — Agentic Autonomy Levels (2026)](wiki/addy-osmani-agentic-autonomy-levels-2026.md)
