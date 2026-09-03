# Your QE Program Has a Structural Problem, and AI Just Made It Visible

**Source:** https://blog.postman.com/your-qe-program-has-a-structural-problem-and-ai-just-made-it-visible/ (Rick Crawford, Field CTO, Postman)
**Alias:** https://blog.postman.com/your-qe-program-has-a-structural-problem-and-ai-just-made-it-visible/?utm_source=softwaretestingweekly&utm_medium=email&utm_campaign=issue-325 (same content, UTM alias from Software Testing Weekly #325)
**Date:** August 12, 2026
**Series:** 3-part (Part 2: 5 QE Pipeline Metrics, Part 3: 3 Paths + 90-day plan)
**Tags:** #QE-program #postman #pipeline-metrics #platform-strategy
**Raw:** [software-testing-weekly-newsletter-2026.md](software-testing-weekly-newsletter-2026.md) (#325 #2)

---

## What It Is

Postman Field CTO Rick Crawford's diagnosis: your QE program works by the standards it was built for, but those standards no longer match AI-accelerated delivery. AI multiplied PR velocity and API calls; gates, tests, audit processes sized for slower world. Gap widens monthly. Not a tool problem — structural.

6 structural problems exposed, none new but now impossible to defer.

## The Shape of the Problem

Classic QE: dev on one branch, quality on another. Tests after code, integration after services, perf/security pre-release, audits quarter-end. Pipeline moves at slowest branch speed. Held at human pace (1 dev, 1 PR, 1 review).

Build-time AI (Cursor, Claude Code, Copilot, Codex) lifts PR velocity per dev by multiples. Gates sized for 40-min suites, 5% flake, manual review become wall. Runtime AI agents consume prod APIs in unexpected ways (pick endpoints by name, infer params, fail creatively).

Headcount flat → asked to do more, faster, with same people, surface growing every direction.

## Six Compounding Problems

1. **Quality is structurally serial** — Dev and QE branches meet at release. QE becomes brake others route around.
2. **Tooling fragments by protocol/stage** — REST (Pact), GraphQL, gRPC, WebSocket, events each own tool (k6/JMeter, Karate/ReadyAPI, custom). Each own report/coverage/evidence → no single picture; seams leak coverage.
3. **Tests rot faster than maintained** — Flaky muted to keep green, spec/behavior drift, brittle scripts, ceiling well below real coverage needs. Fintech 160 major prod incidents despite "testing" — no automation/regression suite.
4. **Long tail undefended** — High-revenue/regulated flagships covered; rest thin. Defects cluster in underinvested surface, invisible to leadership until incident.
5. **Audit evidence is scramble, not system** — Hand-collated per release/protocol: env file → test plan → execution → attach → approve → repeat per protocol. Top-5 pharma: generate env, plan, execution, trigger by hand, attach by hand, mark done, route approval — per protocol, per release. SEC cyber materiality, DORA, FedRAMP continuous, PCI 4.0 make continuous evidence required.
6. **AI amplifies every gap** — Strong pipeline + AI = coverage compounds; thin pipeline + AI = more bugs, faster. Without specs, examples, mocks, known-good workflows, AI generates plausible tests missing real failures.

## Why Visible Now

Not new — AI just makes deferral impossible. Every slow release = unrealized revenue; every escaped defect = reputational; every audit scramble = capacity not building product. AI amplifies whatever pipeline you have, good or bad.

## What to Do Now (Part 1 Action)

Rate each of 6 red/yellow/green for one domain (3-10 services where pain visible). Reds = structural exposure, compound whether you act or not. Input to Part 2 (5 metrics).

Follow-up: **5 QE Pipeline Metrics That Show Where Quality Is Leaking** (Design, Gate, Validate, Monitor, Improve — one per stage) and **QE Platform Strategy: 3 Paths and Where Each Hides Its Cost**.

## Relevance to QA/QE

| Structural Gap | QA Action |
|----------------|-----------|
| Serial quality | Shift from end-gate to platform — quality as continuous output, not branch |
| Fragmented tools | Single coverage/evidence view across protocols; seams checklist |
| Test rot | Deduplicate, quarantine flaky, spec-derived tests; ceiling audit |
| Long tail | Risk-weighted coverage, not flagship-only |
| Audit scramble | Evidence as pipeline output (continuous), not quarterly project |
| AI amplification | Rich context for AI generation (specs, mocks, workflows, failure modes) |

## Critical Analysis

**Strengths:**
- Field-based (1,000+ employee fintech, financial services, top-5 pharma) not vendor pitch.
- Six gaps stack — useful diagnostic map before tooling choice.
- Ties to continuous compliance shift (FedRAMP/DORA/PCI 4.0, SEC).

**Gaps:**
- No single tool fixes — but diagnostic without prescription risks analysis paralysis; Part 2/3 needed for metrics/paths.
- Prioritizes platform view; may undervalue team-level test design fixes.

## Cross-links

- Related: [5 QE Pipeline Metrics](https://blog.postman.com/5-qe-pipeline-metrics-that-show-where-quality-is-leaking/) (Part 2)
- Related: [Postman QE Platform Strategy] (Part 3)
- Wiki: [QE Program Structural Problem → Anton Gulin regression museum](anton-gulin-regression-suite-museum-2026.md) — museum tests are symptom of #3
- Newsletter: [Software Testing Weekly #325](software-testing-weekly-newsletter-2026.md)

---


## The 5 Metrics (Part 2 Preview)
- **Gate:** Coverage of PRs that run blocking suite + flake rate.
- **Validate:** Escaped defects % (prod vs pre-prod).
- **Monitor:** Synthetic journey coverage + mean time to detect.
- **Improve:** Change failure rate (rollback/hotfix).
- **Design:** Package adoption — metrics you can't measure are stages you can't manage.


## Red/Yellow/Green Exercise
For domain 3-10 services, score six gaps now. Reds compound; map is input to Part 2 metrics. No tool fixes all six — start with one.

Note: Testing mindset ≠ gatekeeping — it's deliberately occupying different epistemic position.

Additional takeaway: independent testing = different assumptions, risk models, purpose — not just different person.

Additional takeaway: independent testing = different assumptions, risk models, purpose — not just different person.

Additional takeaway: independent testing = different assumptions, risk models, purpose — not just different person.

*Ingested: 2026-09-01*
