# pi-subagents

**Source:** https://github.com/nicobailon/pi-subagents (Pi extension for async subagent delegation)
**Date:** Active 2026 (README banner, install `pi install npm:pi-subagents`)
**Author:** Nico Bailon (Pi ecosystem)
**Tags:** #pi #subagents #delegation #review #orchestration
**Raw:** [pi-subagents-2026.md](../raw/pi-subagents-2026.md)

---

## What It Is

Pi extension that gives Pi a `subagent` delegation tool. Pi = parent session; subagent = focused child Pi session with own job. After `pi install npm:pi-subagents` (only required step), you ask in plain language — Pi decides whether to call tool, which agent, how to compose. No config, no slash commands needed to start.

Example: `Use reviewer to review this diff.` / `Ask oracle for a second opinion on my plan. Challenge assumptions.` / `Run parallel reviewers: one for correctness, one for tests, one for complexity.` / `Use scout to understand this code, then ask clarification.`

Installing does NOT start automatic background reviewer — gives delegation tool. For every-implementation review, add to prompt/project instructions: `When you finish implementing, run a reviewer subagent before summarizing.`

## How It Works

- **Delegation:** Pi starts child, gives task, brings result back. Foreground streams in conversation; background keeps working, checkable later.
- **Truncation & artifacts:** child transcripts truncated, machine-readable run artifacts preserved.
- **Session sharing:** child inherits context as needed.
- **Bounded orchestration:** `maxSubagentSpawnsPerRun` defaults to 64 (logical children per run tree), separate from concurrency and session-wide budget.
- **Observability:** FleetView below editor in TUI keeps active work visible; `/subagents-fleet` inspector browses children, reads transcripts, steers/stops runs; or ask "Show active async runs." Details in `docs/observability.md`.

## Builtin Agents

| Agent | When to Use |
|-------|-------------|
| `scout` | Fast local codebase recon: relevant files, entry points, data flow, risks |
| `researcher` | Web/docs research with sources + concise brief |
| `worker` | Implementation: edits files, validates, escalates unapproved decisions vs guessing |
| `reviewer` | Code review + small fixes against task/plan, tests, edge cases, simplicity |
| `oracle` | Second opinion before acting: challenges assumptions without editing |
| `delegate` | Lightweight general delegate close to parent |

Rule of thumb: `scout` before understanding, `researcher` before trusting external facts, `worker` to implement, `reviewer` to check, `oracle` when decision risky.

## Common Workflows

- **Second opinion:** "Ask oracle to review this plan and challenge assumptions."
- **Hard problem:** "Use oracle to investigate this bug before we edit."
- **Diff review:** "Use reviewer to review this diff."
- **Parallel reviewers:** "Run reviewers for correctness, tests, and cleanup."
- **Council debate:** "Use `/council` with model-based advisors" (package includes `/council` + `council-mode` + documented `council-*` profiles you add in own agent directory)
- **Implement then review:** "Implement this, then review it."
- **Review loop:** "Run a review loop on this change with max 3 rounds." (`/review-loop`)
- **Scout before planning:** "Use scout to inspect auth flow before planning."
- **Background:** "Run this in the background."
- **Saved workflows:** "Run the review chain on this branch."

Recommended loop for implementation: `clarify → scout → worker → fresh reviewers → worker`. Packaged shortcuts `/parallel-review`, `/review-loop` make repeatable — see `docs/workflows.md`.

## Configuration & Fleet

- No automatic reviewer — delegation tool only.
- Builtin agents immediately usable; custom agents add in own directory.
- `maxSubagentSpawnsPerRun` =64, separate from concurrency.
- FleetView + `/subagents-fleet` + "Show fleet" for observability; machine-readable artifacts in `docs/observability.md`.

## Why It Matters (Relevance to QA/QE)

| Pattern | QA Application |
|---------|----------------|
| Scout before understanding | Use `scout` to map codebase before writing test plan — fast recon for impact analysis |
| Parallel reviewers (correctness/tests/cleanup) | Mirrors QA's 3-way review: correctness, test quality, simplicity — catches different faults |
| Review loop until clean | Implements staged autonomy: worker → reviewer → worker until green, bounded (max 3) |
| Oracle second opinion | Challenges assumptions before acting — same as Julia Pottinger's "challenge assumptions" + Kiro's 15-dim judge independence |
| Background runs + FleetView | Long investigations (like Kiro 13m35s, Zalando) visible and steerable; not lost in chat |

## Critical Analysis

**Strengths:**
- Zero-config start (plain language), but composable (parallel, council, review-loop) — progressive disclosure.
- Builtin agents map to real QA workflow (scout/researcher/worker/reviewer/oracle) — not generic.
- Observability first-class (FleetView, transcripts, artifacts) — traceability for audit (EU AI Act Art 12).
- Bounded (64 spawns) prevents runaway — governance by design.

**Gaps:**
- Pi-specific — not portable to other harnesses (Claude Code, Kiro) without adaptation; evaluation needed for Pi vs Pi vs other model.
- Review quality depends on prompt/project instructions you add — not automatic.

## Cross-links

- Related: [Zalando agentic snapshot](zalando-agentic-engineering-snapshot-2026.md) (agent harness + governance)
- Related: [Kiro trust agent triage](kiro-trust-agent-triage-2026.md) (13m triage, fleet, delegated access)
- Related: [Julia Pottinger who-validates](julia-pottinger-who-validates-ai-generated-code-2026.md) (RACI + PR block — reviewer subagent implements)
- Related: [ruvnet agentic stack](ruvnet-agentic-stack-2026.md) (Ruflo/MetaHarness swarm orchestration — alternative harness)

---

*Ingested: 2026-09-03 · Via GitHub README + banner + docs links; install `pi install npm:pi-subagents`*
