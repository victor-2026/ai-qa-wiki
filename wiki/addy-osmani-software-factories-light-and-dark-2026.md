# Addy Osmani — Software Factories, Light and Dark (2026)

**Source:** https://addyo.substack.com/p/software-factories-light-and-dark
**Author:** Addy Osmani (Member of Technical Staff, Anthropic)
**Date:** 2026-07-22
**Engagement:** 113 likes, 7 comments, 10 restacks

---

## Core Thesis

> A software factory is harnessing loops at scale. Light factory = humans in the loop. Dark factory = code ships that no human has read, verified only by machines.

---

## The Stack: Loop → Harness → Factory

| Concept | Definition |
|---------|-----------|
| **Loop** | One agent doing one job on repeat: gather → act → check → repeat. Smallest unit of agentic work. |
| **Harness** | Walls around a loop: sandbox, tools, memory, gates. Loop = behavior; harness = environment. |
| **Factory** | Many harnessed loops at once, fed by queue, drained through review gate into production. "An org chart made of loops." |

---

## Dark Factory

- Borrowed from FANUC (Japan, lights-out manufacturing since 2001)
- Code ships that no human has read, verified only by machines
- Easy to do at first (removes review bottleneck → feels like broken sound barrier)
- **Fatal flaw: comprehension debt** — 3-6 months → drowning in unread code
- HumanLayer's Dex Horthy: 4 months fully automated → painstaking manual debugging to find problems
- Tests stay green the whole time → reckoning is quiet and late

> "Comprehension debt is the widening gap between how much code exists and how much any human still understands. A dark factory doesn't pay it down; it takes it on as fast as it can."

---

## Lit Factory

Same pipeline with lights on where judgment lives:
- Human judgment moves **upstream** (product, design, architecture) before agent starts
- Upfront hour → fewer implementation hours (review 200-line plan vs 2000-line diff)
- Safety net = ordinary architectural practices: types, test seams, short call stacks, component boundaries, DI

---

## What Earns a Loop the Dark

Loop can go dark ONLY if:
1. Check is cheap
2. Runs at high frequency
3. Relies on something that can't be easily faked
4. Oracle answers immediately, doesn't drift

**Stays lit if:** wrong answer is expensive, only person can catch it, subtle production bugs, large blast radius, long-lived decisions.

> "Back pressure is the rule that you can only hand a loop as much autonomy as you can cheaply and reliably verify, and not one inch more."

---

## Human Goes in the Outer Loop

Engineers own: decide whether it's the right way, verify diagnosis + implementation, approve change, carry consequences of being wrong. Inner loop = agent execution. Outer loop = human accountability.

> "You're not down on the line writing changes any more; you're up at the end of the production line designing it and guarding the gate."

---

## Key Quotes

- "Verification, not generation, is the real constraint on a factory."
- "The bottleneck was never generation."
- "If people stop reading, they'll stop understanding your software."
- "The hardest job now is knowing which checks to build and how much autonomy to delegate."

---

## Connections to Our Work

- **Dark factory = Article 27 warning:** "QA Didn't Get Replaced" because dark factories fail at 3-6 months.
- **Light factory = our operating model:** human owns outer loop (attestor/governor), agents do inner loop.
- **Back pressure = per-risk-tier:** autonomy bounded by verification capacity, not generation speed.
- **"What earns the dark" = our staged ramp:** B0 (always lit) → B2/B3 (can go dark with cheap oracle).
- **Comprehension debt** links directly to `wiki/comprehension-debt.md`.
- **"Safety net = ordinary architecture"** = our AGENTS.md + memory architecture. Not new; now doing second job.

---

## Related Wiki

- `wiki/addy-osmani-human-judgment-software-factory-2026.md` — factory setup, verification budget, runs taxonomy
- `wiki/addy-osmani-own-the-outer-loop-2026.md` — accountability, answerability, 12 pillars
- `wiki/addy-osmani-brownfield-agentic-engineering-2026.md` — brownfield = lit factory territory
- `wiki/comprehension-debt.md` — the debt dark factories accumulate
