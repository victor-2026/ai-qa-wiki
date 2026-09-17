# Michaela Greiler — SCOPE Model: From Code Review to Code Oversight (2026)

**Source:** https://www.ministryoftesting.com/media-sessions/from-code-review-to-code-oversight-michaela-greiler-s-scope-model
**Speaker:** Dr Michaela Greiler (ex-Microsoft Research, ex-DX Head of Research, now independent)
**Interviewer:** Rosie Sherry (MoT CEO)
**Date:** 2026-09-16

---

## Core Thesis

> "Reviewing test code, long the lowest priority on most teams, now matters more than ever, because agent-generated tests can signal safety where there is none."

Code review needs to evolve into **code oversight** as agentic development changes the review dynamics.

---

## Two Failure Modes

### 1. Code Review Exploitation
Verification work gets shifted onto a peer reviewer who never had the mental model in the first place. Agent generates code → reviewer can't evaluate it → approves blindly.

### 2. Code Review Surrender
Reviewers simply can't keep up with the volume and things get waved through. Agent generates 10x more PRs → reviewer overwhelmed → everything gets approved.

---

## SCOPE Model

**Staged Code Oversight with Proportional Escalation**

Key principles:
- Code review needs to **start in the planning phase**, not at the pull request
- Escalation proportional to risk (similar to our B0-B3 tiers)
- Reviewing test code matters MORE than reviewing app code (agent-generated tests can be false assurance)

---

## Key Quotes

- "Agent-generated tests can signal safety where there is none."
- "Code review needs to start in the planning phase rather than at the pull request."
- "Reviewing test code, long the lowest priority on most teams, now matters more than ever."

---

## Connections to Our Work

- **"Agent-generated tests can signal safety where there is none"** = mutation testing thesis (tests must be verified independently)
- **"Start in planning, not at PR"** = Article 27's per-risk-tier (gate BEFORE code, not after)
- **"Proportional escalation"** = B0-B3 tiers (critical = more oversight, cosmetic = less)
- **"Code review exploitation"** = our "author ≠ examiner" (Pettersson) — if reviewer can't evaluate, review is theater
- **"Code review surrender"** = Bach's "market forces don't optimize for safety" — volume overwhelms oversight
- **Test code matters more** = Tornhill's "double-entry bookkeeping" — tests are the verification boundary

---

## Related

- `raw/keithklain-death-by-thousand-prompts-2026.md` — same problem (more tests ≠ better testing)
- `raw/adamtornhill-practices-abandoned-agents-2026.md` — e2e tests as boundary
- `raw/testmuai-finance-ai-agent-compliance-testing-2026.md` — compliance = staged oversight
- Article 27: "QA Didn't Get Replaced. It Got Promoted." — oversight role
