# Addy Osmani — Human Judgment Doesn't Leave. It Relocates. (2026)

**Source:** https://addyo.substack.com/p/human-judgment-doesnt-leave-the-software
**Author:** Addy Osmani (Member of Technical Staff, Anthropic)
**Date:** 2026-08-21
**Engagement:** 58 likes, 5 comments, 5 restacks

---

## Core Thesis

> Human judgment is being relocated. Remove people from parts of the loop where machines produce stronger signals. Concentrate people where context, taste, risk, and long-term ownership matter most.

---

## Key Ideas

### Do You Need a Factory?
You can get surprisingly far with stock coding harness (Claude Code / Codex, multiple sessions, good SPECs with verification baked in). Factory needed when: repeatable + event-driven + isolated cloud + triage/implementation/testing with explicit human babysitting.

### Verification Budget
Think like performance budgets: fast checks early (lint, type), full tests near draft PR (mutation, browser, security). Don't replace with summaries — real tests, budgeted in right places.

### When Green is Misleading
AI can change the test to pass instead of changing the code. "Just because a factory shows everything is green doesn't mean it's actually green."

### Cognitive Bandwidth Doesn't Scale
5-10 parallel sessions = 5-10 mental models going cold. Parallel work amplifies comprehension debt. Store trajectory/lessons outside session (repo, local, shared).

### 82-Manute Factory Run
- Quick finder (no rejections): 7 min
- Favorites (2 rejections + human decision): 56 min
- Same factory, 8x difference = verification cost
- Verifiers caught real problems; overhead vs useful delay

### Ownership Doesn't Disappear
Someone still: chooses the problem, chooses architecture, sets quality bar, decides which verification signals deserve trust, decides when evidence is sufficient to ship.

### Runs That Don't Ship (Vercel taxonomy)
- **Success** → ships
- **Flawed** → wrong implementation, needs fix
- **Blocked** → missing credential/env
- **Manual** → boundary factory can't cross

Pair with per-stage timing; a manual run isn't finished when the factory stops but when the human knows what to do next.

---

## Key Quotes

- "Human judgment is being relocated."
- "The best software factories will not be defined by how completely they eliminate human involvement. They will be defined by how intelligently they place it."
- "Consider optimising the software factory for your reviewer."
- "Code good enough to ship still starts with a human."

---

## Connections to Our Work

- **"Judgment relocated" = Article 27 thesis:** QA moves from running tests to governing evidence.
- **Verification budget ≈ staged ramp:** fast checks early (B0), heavier verification later (B3 trend-only).
- **82-minute factory ≈ VerdictGate MVP:** verification takes 8x longer than generation; that's the point.
- **"Green is misleading" ≈ mutation testing thesis:** passing tests ≠ correct implementation.
- **Comprehension debt** = our gotcha #4 (count from full file, not truncation). Parallel sessions amplify.

---

## Related Wiki

- `wiki/addy-osmani-own-the-outer-loop-2026.md` — deeper on accountability/answerability
- `wiki/addy-osmani-software-factories-light-and-dark-2026.md` — dark factory = comprehension debt accelerator
- `wiki/comprehension-debt.md` — the debt itself
