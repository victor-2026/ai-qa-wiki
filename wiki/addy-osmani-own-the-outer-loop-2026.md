# Addy Osmani — Own the Outer Loop (2026)

**Source:** https://addyo.substack.com/p/own-the-outer-loop
**Author:** Addy Osmani (Member of Technical Staff, Anthropic)
**Date:** 2026-07-09
**Engagement:** 109 likes, 19 comments, 16 restacks

---

## Core Thesis

> Engineers need to own the outer loop — the accountability for agentic systems. The agent runs the inner execution loop. Engineers own the outer loop.

---

## Three Pillars

| Pillar | Definition |
|--------|-----------|
| **Quality** | All checks installed before letting the system loose. Produces evidence. |
| **Verdict** | Final decision before work enters dependent system. "The model may write the line, but the Verdict is mine." |
| **Answerability** | The guarantee that if someone asks, you can explain why. |

---

## Inner Loop vs Outer Loop

- **Inner loop** (agent): investigate → implement → verify → repeat
- **Outer loop** (human): decide if right way, verify diagnosis + implementation, approve, carry consequences
- **Boundary**: evidence (diffs, tests, logs, brief explanation)

> "Inside the system: capability. Outside the system: agency."

---

## Three Hidden Costs

### 1. Cognitive Surrender
Blindly accepting AI output. Wharton study: when AI was wrong, ~75% accepted it anyway and felt MORE confident.

### 2. Cognitive Debt
Erosion of understanding. Anthropic RCT: engineers using AI scored 17 percentage points lower on comprehension (50% vs 67%). Gap compounds exponentially with longer agent horizons.

### 3. Orchestration Tax
Easy to spin up agents, but cognitive bandwidth doesn't parallelize. Steering, sorting, verifying = un-automatable work.

---

## Four Loops Humans Must Own

1. **Constraints loop** — what inputs, architectures, instructions, invariants?
2. **Sampling loop** — how much output to sample and review?
3. **Audit loop** — what evidence to keep, how to make audit log effective?
4. **Ownership loop** — what part of the production boundary to own?

---

## Accountability Contract

Every codebase change should include:
- Checklist understood when change was accepted
- Evidence that went into decision
- Who was accountable
- System status after change

> "Without accountability, there are no rules. If nobody owns the consequence of a decision, high agency can only bring chaos."

---

## Alpha, Decay, Taste

- **Alpha** — lead taken by highest achiever when playing highest-value move
- **Decay** — established patterns everyone learns through repetition
- **Taste** — earliest sense of alpha/change before evidence. "Making high-quality qualitative judgments where no objective metric exists yet" (Mitchell Hashimoto).

> "The half-life of an edge is one release, but the half-life of a signature is a career."

---

## Twelve Pillars (Brownfield)

Brownfield = frontier for factories. Must: turn implicit knowledge into explicit constraints, keep coherent across teams, formalize into test procedures, tie to objective evidence, ratchet failure into learning.

---

## Key Quotes

- "Build the factory; keep the lights on; make work legible, verifiable, owned."
- "An agent can write it. But before it reaches users, someone must explain why it should exist, why it's safe, and what they will do when it is wrong."
- "The bottleneck moves from 'can we build this?' to 'should this exist, can we answer for it?'"
- "Only people can choose. Only people inherit consequence."
- "Skills get you leverage; accountability turns leverage into trust."

---

## Connections to Our Work

- **Verdict = our attestor role:** "The model may write the line, but the Verdict is mine." This IS the QA governance thesis.
- **Answerability = per-risk-tier evidence chain:** every tier produces evidence for the verdict. Without it, no answerability.
- **Cognitive debt (50% vs 67%)** = strongest external evidence for Article 27. AI-assisted engineers understand less.
- **Four loops** = our operating model constraints: AGENTS.md (constraints), sampling (B-tier review), audit (evidence chain), ownership (attestor signature).
- **Twelve pillars** = brownfield attestation requirements. Our per-risk-tier framework addresses these.
- **"Should this exist?"** = VerdictGate question. Not "does it pass?" but "should it ship?"

---

## Related Wiki

- `wiki/addy-osmani-human-judgment-software-factory-2026.md` — factory setup, verification budget
- `wiki/addy-osmani-software-factories-light-and-dark-2026.md` — dark factory, comprehension debt
- `wiki/addy-osmani-agentic-autonomy-levels-2026.md` — six levels of autonomy
- `wiki/comprehension-debt.md` — the debt itself

## See also

- [Addy Osmani — Agentic Autonomy Levels (2026)](wiki/addy-osmani-agentic-autonomy-levels-2026.md)
- [Addy Osmani — Human Judgment Doesn't Leave. It Relocates. (2026)](wiki/addy-osmani-human-judgment-software-factory-2026.md)
- [Addy Osmani — Software Factories, Light and Dark (2026)](wiki/addy-osmani-software-factories-light-and-dark-2026.md)
