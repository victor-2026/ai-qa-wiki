# Adam Tornhill — Practices I Abandoned with Agents (2026)

**Source:** https://adamtornhill.substack.com/p/practices-i-abandoned-with-agents
**Author:** Adam Tornhill (Founder CodeScene, "Your Code as a Crime Scene", "Your Brain on Code")
**Date:** 2026-09-03
**Engagement:** 43 likes, 4 comments

---

## Core Thesis

> After 25 years with TDD, we are now parting ways. The incremental TDD steps were great for human cognition, but didn't survive the transition to agentic coding.

TDD = design technique optimized for human cognition (small increments, visible progress). Agents take larger steps — one agentic iteration = tens of red-green-refactor cycles. Forcing agents through human-optimized increments negates benefits.

---

## TDD Backstory

- Practiced TDD for 25 years (early 2000s → 2026)
- TDD = design technique with verification as side effect (not "testing")
- Key win: radar simulation project — shipped early, "it just worked" on integration
- TDD took him from "decent to good developer"

## Shift 1: Functional Programming (Clojure)

- Clojure REPL → faster feedback than TDD's red-green cycle
- Experiment in REPL, copy to tests for iteration
- TDD still used for maintenance/extensions, but not novel work
- Lesson: don't cling to old patterns when new paradigm offers better feedback

## Shift 2: Agentic Coding (Sep 2025)

- Started with TDD + agents (familiar, but not effective)
- 6-8 months to find new process
- **Key insight: agents iterate at feature level, not building-block level**

---

## The Abandonment

### What Changed

| TDD (Human) | Agentic (Machine) |
|-------------|-------------------|
| Small increments | Large steps (feature-level) |
| Human reads code | Machine is primary audience |
| Unit tests as design | E2e tests as boundary |
| Manual inspection | Tooling enforces what you don't inspect |
| Red = "I have work to do" | Red = "test suite validates changes" |
| Human refactors | Machine refactors via MCP servers |

### What Survived

1. **Double-entry bookkeeping** — always drive via failing test (prevents AI from deleting test or changing condition to match erroneous code)
2. **Red-green principle** — but different meaning: red = confidence test suite can validate delegated changes
3. **Refactoring step** — left to machine, driven by MCP server feedback

### Code is No Longer for Human Consumption

> "My AI code doesn't look like what I would have written myself. And I had to accept that. What matters is that the code supports machine reasoning and change."

Enforce via tooling, not manual inspection.

---

## Key Quotes

- "Forcing an agent through increments optimized for human cognition negates many of the benefits."
- "Code is no longer for my consumption. The machine is the primary audience."
- "I always drive any change to the codebase via a failing test. The difference is that those tests can typically be at a higher level than unit tests."
- "In TDD, red verified that I had implementation work to do. With agents, red gives me confidence that my test suite is capable of validating the changes I delegate to agents."
- "Tooling enforces what you don't inspect."

---

## Connections to Our Work

- **E2e as human/agent boundary = per-risk-tier:** human defines evidence (what to check), agent implements, attestor verifies (red = test suite validates)
- **"Double-entry bookkeeping" = mutation testing thesis:** tests must survive independent verification (mutants), not just pass. Same principle: don't let the thing being tested control the test.
- **"Tooling enforces what you don't inspect" = B0-B3 gates:** automated constraints, not manual review. Quality through architecture, not reading.
- **"Code supports machine reasoning"** = our VerdictGate design: machine-readable evidence chains, not human-readable summaries.
- **Article 27:** QA role shifts from reading code (TDD-era) to governing the evidence system (agentic-era). Tornhill confirms this from engineering perspective.
- **Config rot / skill hygiene (Osmani)** — Tornhill's shift parallels: adapt workflows to new paradigm, don't force old patterns.

---

## Related Wiki

- `wiki/addy-osmani-agentic-autonomy-levels-2026.md` — autonomy levels require different verification
- `wiki/addy-osmani-human-judgment-software-factory-2026.md` — judgment relocated, not removed
- `wiki/addy-osmani-brownfield-agentic-engineering-2026.md` — characterization tests as Phase 0 (Tornhill's failing tests = characterization tests)
- `wiki/comprehension-debt.md` — understanding gap when code is for machines
