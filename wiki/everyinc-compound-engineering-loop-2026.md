---
title: "EveryInc: Compound Engineering Loop (brainstorm → plan → work → simplify → review → compound)"
source: https://github.com/EveryInc/compound-engineering-plugin (MIT, 25.2k stars)
date: 2026-09-21
tags: [compound-engineering, knowledge-compounding, review-against-plan, skills, opencode, pi]
---

# EveryInc: Compound Engineering Loop

**Source:** https://github.com/EveryInc/compound-engineering-plugin (MIT, 25.2k stars, Kieran Klaassen/Trevin Chow) — Compound Engineering for AI agents

## The Loop

**brainstorm → plan → work → simplify → review → compound**

Knowledge from each cycle written to `docs/solutions/` so next agent starts smarter. 36 skills, works on 14 hosts (including OpenCode, Pi).

- `/ce-code-review` — report-only multi-agent review against plan
- `/lfg` — full autopilot
- `/ce-brainstorm`, `/ce-plan` — structured phases

## Why It Matters for Victor

- **Compound knowledge** = our `raw → wiki → outputs` + `session-checkpoints` + `.opencode-memory.md` — same principle, different path (`docs/solutions/` vs `wiki/`).
- **Forced lesson documentation** = wiki-ability — every pilot writes to wiki, not just code.
- **Review-against-plan** = variant of per-risk-tier gate (evidence vs plan, not vs tier). Could add as gate in VerdictGate: "does evidence match the plan's stated scope?"

## What to Adopt

1. **`/ce-code-review` report-only** — already have Pi reviewer, but make it plan-vs-evidence (not just code style). Our `window-discipline.md` + `per-risk-tier` already is plan, but review step is ad-hoc. Formalize: every feature branch gets `review-against-plan` before merge.
2. **`docs/solutions/` compounding** — we compound via wiki + checkpoints, but not via `docs/solutions/` per-feature knowledge. Could add `verdictgate/docs/solutions/` for each scorer version's lessons (we already do `reviews/` — close).
3. **Simplify phase** — explicit refactor pass after work, before review. We tend to skip this.

## Links
- Repo: https://github.com/EveryInc/compound-engineering-plugin
- Six-layer: https://github.com/rmorison/engineering-standards
