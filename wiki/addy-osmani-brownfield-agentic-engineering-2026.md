# Addy Osmani — Brownfield Agentic Engineering (2026)

**Source:** https://addyo.substack.com/p/brownfield-agentic-engineering
**Author:** Addy Osmani (Member of Technical Staff, Anthropic)
**Date:** 2026-09-14
**Engagement:** 68 likes, 10 comments, 6 restacks

---

## Core Thesis

> Agentic engineering in an old codebase is about making hidden constraints visible and cheap changes trustworthy.

Brownfield = repository is no longer a complete description of how the thing actually behaves. Institutional knowledge, duct tape, legacy services, and expectations other teams depend on live outside the tree.

---

## Key Patterns

### 1. Zones (Green / Yellow / Red)

Agent autonomy mapped to codebase risk:

- **Green** — safe, good tests, isolated. Agents work in tight loop.
- **Yellow** — mixed quality. Agents change code only after characterization tests written.
- **Red** — sensitive (auth, billing, permissions). Human pairing on every step or work doesn't happen.

**Three rules make zones an operating procedure:**
1. A person draws the map, not the agent (agents start in scariest file because it has most interesting names).
2. Zones only move when earned: yellow → green once characterization tests exist + module owner reviewed first agent changes.
3. Zone sets the verbs: green = tight loop, yellow = tests first, red = human pairing or no-go.

### 2. Write Down What the Code Can't Say

Agents infer a lot from code itself. What they CAN'T infer:
- Business/team-specific nuance
- Trade-offs explaining WHY the system is structured a certain way
- Guidelines not enforced by static analysis
- Domain-specific rules
- External constraints and historical context behind counter-intuitive implementations

**Rule:** Write down what the code can't say, and nothing else.

### 3. Make Research Survive the Session

If agent's exploration produces no durable artifact, next agent pays for same archaeology again.

**Pattern:** Separate read-only pass that produces a short comprehension memo:
- Entry points, owners, callers
- Existing abstractions, tests
- Production signals, relevant history
- Open questions

Claims should cite a file, issue, ownership record, or dashboard.

After research → plan with clean context → human picks path → implementation stops if map was wrong.

### 4. Characterization Tests (Lock Before You Leap)

> Characterization tests are automated tests used to document a system's actual current behavior so you can safely refactor or change legacy code.

- Pin what the module does today, ugly parts included (some ugly behavior is what the business runs on).
- Agent will happily "fix" it behind a green suite.
- Netflix: replay + shadow traffic against old and new paths, diff payloads, promote only when they match.
- Don't let same session be only author of tests + implementation. Pin behavior first (separate pass or by person), then let agent work.

### 5. Migration Blindness

SWE Refactor Bench: 520 agent runs → only 28 passed migration audit + behavioral tests + independent verification.

Half-finished migrations are particularly confusing to agents: search returns old approach in 40 files, replacement in 12, shim presenting both as current → contradictory precedent.

**Rule:** Finish one route end to end, including removing old path. If deletion is a future cleanup ticket, migration unit is not complete.

### 6. Parallelize Last

Software factories can run many changes at once. Copy that part only after one unit has:
- Dependable judge
- Recovery path
- Review format people can absorb

> Parallelism multiplies the bottleneck you already have. Automated verification can handle five checked changes. One senior reading every line gets a queue, fragmented attention, and eventually ceremonial approval.

### 7. Agents Put a Price on Ambiguity

> Lines generated don't tell you whether the codebase improved.

Track: lead time, review minutes, human interventions, escaped defects, rollbacks, oracle mismatches, suppressions left behind.

> Tribal conventions become recurring review comments. That cost was always there, paid during onboarding, review, and incident recovery. Agents make more of it countable.

---

## Case Studies Referenced

| Company | Migration | Key Insight |
|---------|-----------|-------------|
| Netflix | GraphQL cutover | Replay + shadow traffic, diff payloads, promote on match |
| Stripe | 3.7M lines to TypeScript | Months of codemod, no agents, durable migration machine |
| Bun | Zig-to-Rust (535K LOC) | 50 workflows / 11 days, porting guide BEFORE agents, adversarial reviewers |
| Anthropic | Internal migration | Stress-test rulebook on disposable mini-migration, throw trial output away |
| Asana | Enzyme → modern | Multi-year backlog cleared in 2 weeks, ~$12K model cost |
| Shopify | RN → native Swift/Kotlin | 12 weeks, agent-gated screen-sized checkpoints |
| VB6 → C# study | Controlled experiment | 92% behavioral equivalence on simple, 47% on complex — unit size is the lever |
| Spotify | Backstage | 650+ agent PRs/month on rails built years earlier |

---

## Key Quotes

- "Agentic engineering in an old codebase is about making hidden constraints visible and cheap changes trustworthy."
- "What transfers between companies is the structure around the agents."
- "Agents have changed the price of trying several plausible implementations. They haven't changed the evidence required to choose one."
- "A green suite with all traffic still taking the old path is busywork."
- "The next time an agent works on the homepage equivalent, I would want it to leave behind more than the repair: a synthetic user journey, an ownership record, and a regression test."

---

## Connections to Our Work

- **Zones (Green/Yellow/Red) ≈ Per-risk-tier gates (B0–B3):** same principle — autonomy scales with confidence earned through verification, not assumed.
- **Characterization tests = Phase 0 of any pilot:** lock current behavior before mutation/seeding. Validates our staged ramp (trivial → realistic → industry pool).
- **Write down what code can't say ≈ AGENTS.md + memory architecture:** tribal knowledge codified, not assumed.
- **Migration blindness ≈ VerdictGate vendor evaluation:** score without context = contradictory precedent. Tiered evidence prevents false confidence.
- **"Agents put a price on ambiguity" ≈ Article 27 thesis:** QA role shifts from running tests to governing the evidence system.
- **Parallelize last ≈ staged ramp §8 v0.3:** earn autonomy through single-unit dependability first.

---

## Related Wiki Pages

- `wiki/comprehension-debt.md` — comprehension debt (origination: Addy's substack). Brownfield patterns are the mitigation: zones + characterization tests prevent comprehension debt from accumulating.
- `wiki/addy-osmani-anthropic-verification-floor-skill-decay-2026.md` — skill decay. Brownfield zones answer "where can agents work safely" while skill decay answers "why human verification still matters."
- `wiki/addy-osmani-month-digest-verification-gates-2026-09.md` — month digest with tiered gates, config rot, loop engineering. Zones are the practical implementation of those tiered gates.




















<!-- backlinks-start -->
### Backlinks
- [Codescene Deterministic Code Health Gate 2026](wiki/codescene-deterministic-code-health-gate-2026.md)
- [Qodo Introducing Qodo 2 4 The Next Layer Of Code Quality Governance](wiki/qodo-introducing-qodo-2-4-the-next-layer-of-code-quality-governance.md)
- [Qodo Software Map Risk Across Repos 2026](wiki/qodo-software-map-risk-across-repos-2026.md)
- [Qodo: Contract Verification Across Repositories – Catching Breaking Changes at AI Velocity](wiki/qodo-contract-verification-across-repos-catching-breaking-changes-at-ai-velocity.md)
- [Qualitymax Independent Verifier Profile 2026](wiki/qualitymax-independent-verifier-profile-2026.md)
<!-- backlinks-end -->
