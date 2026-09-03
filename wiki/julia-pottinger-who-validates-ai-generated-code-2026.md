# Who Validates AI-Generated Code? — Who Is Accountable (Julia Pottinger)

**Source:** https://juliapottinger.com/who-validates-ai-generated-code/?utm_source=softwaretestingweekly&utm_medium=email&utm_campaign=issue-325 (redirects to Who Is Accountable for AI-Generated Code?)
**Canonical:** https://juliapottinger.com/who-validates-ai-generated-code/ (same content as Who Is Accountable, 25 Aug 2026) — Issue #325 link is UTM alias
**Author:** Julia Pottinger (QA, JPott Studios, QA since 2015)
**Date:** August 25, 2026, 10 min
**Tags:** #accountability #AI-generated-code #sign-off #QA-control-layer #PR-template
**Raw:** [julia-pottinger-who-validates-ai-generated-code-2026.md](../raw/julia-pottinger-who-validates-ai-generated-code-2026.md)

---

## What It Is

Follow-up to "QA is the control layer" — answers *who validates* when AI writes code: not the tool, never a committee, exactly one **Accountable** human per change. On solo game (Tropic Tumble) accountability is clear: author accepts, ships broken → only author to blame. On team, chain `Agent Generates → Developer Accepts (glance) → Reviewer Approves (fast) → Production Breaks (nobody answers)` — gap is ownership, not testing.

This piece is *underneath* gates: gates work only if named person owns outcome. Without owner, green pipeline = nobody who can answer.

## Generating ≠ Owning

Hand-writing: authorship and accountability arrive together (understand because built line by line). Agent-writing: they split:
- Authorship moves to tool (developer authored prompt, not logic)
- Reading is optional (may not have read every branch)
- Author gone at failure time

> A tool can produce code. A tool cannot be accountable for it. — Accountability needs someone to hold responsible, model cannot be held.

Accepting = click. Owning = you can answer what it does, decided correct, team comes to you when not. Real question: *which human stands behind this change?* Honest answer often "nobody in particular."

## Why "Developers Will Catch It" Fails

Spreads responsibility across everyone → lands on no one. Social psychology: **diffusion of responsibility** — more who *could* act, less any *must*. AI worsens: author assumes agent right, reviewer assumes author checked. Two believe code has owner, has none.

Sharper: what approval even meant? Under pressure, reviewer approves `looks right` not `is right`. Generated code excels at looking right — fluency lowers scrutiny. Thumbs-up conflates:
- "I read and stand behind it"
- "Looked fine and tests passed"

If approval rested on suite, ownership rested on tests — and AI-written tests confirm what code does, not challenge ([green suite confirming defect](https://juliapottinger.com/is-that-green-checkmark-real/)).

Fix: make ownership **named, recorded** thing, not assumption.

## Name an Accountable Owner (RACI per Change)

Exactly one **Accountable** per change, never tool/committee. Plenty can be Responsible.

| Activity | Developer (prompter) | Reviewer | QA | Tech Lead |
|----------|---------------------|----------|----|-----------|
| Generate and accept code | R | · | · | · |
| Understand what change does | **A** | C | C | · |
| Confirm solved right problem | **A** | C | C | · |
| Verify tests would fail on real bug | C | C | **A** | · |
| Sign off risk acceptable to ship | C | R | **A** | I |
| Own rollback if breaks | **A** | · | C | I |
| Own policy for AI use | C | · | C | **A** |

- Developer = accountable for understanding; acceptance without understanding = original sin
- QA = accountable for risk sign-off (judgment no one else positioned to make)
- Agent = nowhere — cannot hold letter

Role names less important than discipline: one accountable human who can pass honest test.

## The "Can I Sign Off" Test (5 Questions)

Before putting name on AI-assisted change, need yes to each — else not owner yet:

1. Can I explain what change does in one honest paragraph, without re-reading agent summary?
2. Do I know what problem it was meant to solve, and why this solves it not plausible neighbour?
3. If breaks at 2am, am I called and could I start debugging?
4. Is there at least one test that would actually go **red** if behaviour were wrong?
5. If teammate asked "are you sure," would answer be **evidence, or shrug**? (most weight)

If most honest answer is "agent seemed confident and build green," change has hopeful bystander, not owner. Diff that looks right backed by nothing you checked is not evidence.

## Record Sign-Off Where Change Lives

Ownership in head evaporates on leave. Put in artifact — short required PR block:

```md
## AI-assisted change
- Generated with: <agent / tool>
- Accountable owner: @name  (understands, owns rollback)
- What it does (my own words): ...
- Risk if wrong, who it affects: ...
- Evidence it works: <link to test that would fail on real bug>
- QA sign-off (risk acceptable): @name
- If unverifiable before release: monitor + owner + rollback plan
```

Why earns place:
- Makes owner write in own words → cheapest understand test
- Separates developer accountability from QA risk sign-off → green pipeline can't stand for either
- Leaves record → postmortem reads name+paragraph, not guessing commit hash; turns witch hunt into "sign-off missed this risk, tighten it"

## Ownership Scales to Volume, Not Line

Objection: 10× code → bottleneck if every change needs deep owner reading. Right → answer is risk-sizing:

- **Low** (copy, styling, internal tooling): developer owner only, no second sign-off — speed right
- **Medium** (new feature path, changed query, user-facing): named developer owner + real review (reviewer must also pass can-I-sign-off test)
- **High** (auth, payments, data integrity, money/trust loss): named developer owner **AND** explicit QA sign-off recorded before merge

Use **GitHub CODEOWNERS** to route high-risk dirs to owners mechanically — accountability stops depending on remembering to add reviewer. Volume can climb; number of high-risk changes shipping without name cannot.

## Where This Leaves You

AI changed writer, not answerer. Teams generating most code aren't trouble; teams letting authorship move to tool and forgetting to hand accountability to person are. Keep explicit: one accountable name per change, sign-off sized to risk, record where change lives.

**One move this week:** add AI-assisted block to PR template and require named accountable owner on anything touching auth/payments/data. Costs almost nothing; turns "someone approved it" into "this person owns it."

## Relevance to QA/QE

| Pattern | QA Action |
|---------|-----------|
| Diffusion of responsibility | Require one Accountable per AI-assisted PR; never tool/committee |
| Thumbs-up conflation | Separate "looks fine" from "stand behind it" — require paragraph + evidence |
| Agent owns generation | QA owns risk sign-off — explicit gate before merge |
| Volume vs risk | Risk-sized sign-off via CODEOWNERS, not uniform bottleneck |
| Green ≠ proof | Demand test that would go red on real bug, not just passing suite |

## Critical Analysis

**Strengths:**
- Concrete PR template + 5-question test + RACI — immediately implementable, not policy doc.
- Directly addresses fluency bias and diffusion — names mechanism, not just "review harder."

**Gaps:**
- Light on tooling to enforce (CODEOWNERS is hint; needs CI check that block present).
- Doesn't deep-dive on assertion quality — pairs with companion "6 Checks Before You Trust a Green Checkmark."

## Cross-links

- Related: [julia-pottinger-accountable-ai-code-2026.md](julia-pottinger-accountable-ai-code-2026.md) — earlier 10-min version from Weekly #325 #3 (same theme, shorter)
- Related: [QA Is the Control Layer](https://juliapottinger.com/qa-control-layer-for-ai-assisted-development/) — gates that need owner
- Related: [Testing AI-Generated Code: 6 Checks](https://juliapottinger.com/is-that-green-checkmark-real/) — evidence before green
- Related: [Keith Klain Testing Mindset](keith-klain-testing-mindset-after-all-2026.md) — evaluator independence supports accountable sign-off
- Newsletter: [Software Testing Weekly #325](software-testing-weekly-newsletter-2026.md)

---

*Ingested: 2026-09-03 · Full fetch of UTM alias who-validates → Who Is Accountable; alias noted as same content*
