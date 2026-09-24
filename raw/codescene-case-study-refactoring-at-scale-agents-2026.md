# CodeScene: Case Study Refactoring at Scale with Agents - Street Fighter III 300K Lines (2026-09-24)

**Author:** Adam Tornhill (Founder/CTO CodeScene); execution credit: Daniel Webb, Markus Borg; contact NeoSee for enterprise delivery
**Source:** https://codescene.com/blog/case-study-refactoring-at-scale-with-agents
**Context:** CodeScene = behavioral code analysis, Code Health metric (validated proxy: healthy code 10x faster to evolve, 15x fewer defects per Code Red papers). Vendor case study (numbers directional, single codebase). Core relevance: (1) objective deterministic quality signal as agentic feedback loop (MCP server); (2) replay-trace harness as behavioral-equivalence evidence (frame-by-frame rollback hash); (3) iterative playbook with documented failures; (4) AI-discovered domain-specific rules structurally unlike human ones; (5) economics ($4K tokens vs 12-18 months experts). Lund University follow-up study planned (students implement features in healthy vs unhealthy versions).
**Fetched:** 2026-09-24 via webfetch, substance below (nav/footer stripped).

---

## Setup

- Codebase: Street Fighter III: 3rd Strike, 300K lines of C (open-source 3S decomp).
- Goal: eradicate application-code technical debt → Code Health 10.0, level where new features addable safely with AI.
- Correctness evidence: replay-trace harness comparing rollback state hash frame by frame; game still playable identically.
- Quality signal: CodeHealth MCP Server as objective signal + agentic feedback loop.

## Process in numbers (3 weeks part-time)

- 2,903 commits; 252,055 lines modified; 726 files touched; 22 refactoring recipes + 82 notes.
- Model trajectory: experimented, settled on Claude Opus (better at capturing/documenting playbook patterns); Sonnet/Terra plateaued at local optima, stuck on remaining smells.
- Playbook mechanics: agents iteratively build refactoring playbook (preconditions per recipe, evaluated, successes added back); documented FAILURES included (attempts that moved nothing or degraded health).

## AI-discovered rules (domain-specific, non-Fowler)

Shared Index Range (loops differing only in ranges); Action Parameter (duplicated control differing in invoked function); Uniform Step Table (heterogeneous calls → table-driven dispatch). Emerged from codebase patterns under CodeHealth-MCP feedback. Familiar base (Extract Function, Guard Clauses, Parameter Object) + novel shapes.

## Why trust the metric (their argument)

Give an agent any metric + tokens and it optimizes it - so target must be validated: Code Red (productivity/defects), AI-Ready-Code whitepaper (health improves AI correctness), token-efficiency data (healthy code cuts iteration churn). Business translation of 5.6 → 10.0 uplift: ~70% fewer AI-induced defects + ~45% less token waste on future features vs $4K token spend.

## Thesis

Technical debt is NOT solved - naive AI adoption adds to it. But economics flipped: use AI to make code AI-suitable, with deterministic quality feedback (where to improve + objective judge) and automated tests/equivalence checks as behavior safeguards. Large-scale remediation becomes economically viable.

## Use for us

- Deterministic gate doctrine: independent objective signal (Code Health) steering generation loop = same shape as our verdict-layer argument (judge ≠ generator); cross-link judges-agree, Qodo examiner pieces.
- Replay-trace equivalence harness = behavioral-evidence template (frame-hash ≈ golden-trajectory diff in autonoma-agent-reliability).
- Playbook-with-failures = mutation-matrix analog (documented kills AND survivals both feed the loop).
- Lund follow-up (healthy vs unhealthy student study) = radar for controlled human+AI evidence.
- Caveat: single vendor codebase, game code (deterministic replay available - not every domain has frame-hash equivalence); $4K excludes human design time.
