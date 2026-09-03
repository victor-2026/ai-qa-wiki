# Pi ↔ OpenCode Integration

**Source:** https://github.com/nicobailon/pi-subagents + https://opencode.ai/docs + Zalando agentic snapshot (MCP proxy/Bearer injection)
**Date:** 2026-09-03
**Tags:** #pi #opencode #MCP #AGENTS.md #subagents
**Raw:** [pi-subagents-2026.md](../raw/pi-subagents-2026.md) + [ruvnet-agentic-stack-2026.md](ruvnet-agentic-stack-2026.md)

---

## What It Is

Pi (Pi extension `pi-subagents`) and OpenCode (AI coding agent, `opencode.ai`) are both terminal-native harnesses. No native `pi ↔ opencode` wire, but **3 integration layers** make them composable without code: **files as contract** (`AGENTS.md`), **MCP as shared tool bus**, and **CLI as subagent**.

## Layer 1: Files as Contract — AGENTS.md

Both read `AGENTS.md` (OpenCode also reads `CLAUDE.md` via import) in repo root. Single source of truth:

```md
# AGENTS.md
## Build & Test
- build: npm run build
- test: npx playwright test
- lint: npx eslint .

## Rules (for Pi scout/worker/reviewer and OpenCode)
- Use data-testid where present, fallback to ARIA role
- Never hardcode secrets — use Bearer injection via MCP proxy
- PR must include AI-assisted block: Accountable owner, Risk, Evidence
```

Pi `scout`/`worker`/`reviewer` and OpenCode `worker` obey same rules. Handoff is filesystem/git — Pi writes, OpenCode reads, no API. Zalando pattern: reference configs via `git` + `CLI command` installing symlinks (opencode does `plugin marketplaces` via symlinks).

## Layer 2: MCP as Shared Bus

Both speak Model Context Protocol. One `mcp.json` serves both:

```json
{
  "mcpServers": {
    "playwright": {"command": "npx", "args": ["@playwright/mcp@latest"]},
    "github": {"command": "npx", "args": ["@modelcontextprotocol/server-github"]},
    "zalando-proxy": {"command": "npx", "args": ["zalando-mcp-proxy"], "env": {"MCP_BEARER_CMD": "zalando-auth refresh"}}
  }
}
```

Example flow: Pi `scout` → Playwright MCP → finds `data-testid="invoice-total"` + ARIA boxes → writes recon brief → OpenCode `worker` consumes same MCP for real locators (no hallucination). Same proxy injection Zalando uses to avoid hardcoding secrets in `mcp.json`.

## Layer 3: CLI as Subagent (Recommended Loop)

OpenCode can spawn Pi via `bash` tool; Pi can spawn OpenCode. Use Pi-subagents as specialized reviewers/oracles:

**Recommended loop:** `clarify (human) → scout (Pi) → worker (OpenCode) → fresh reviewers (Pi parallel) → worker (OpenCode) → FleetView check`

OpenCode prompt (or `opencode.json` skill):

```text
When you finish implementing, run a Pi reviewer subagent before summarizing:
bash: pi "Use reviewer to review this diff. Check tests would fail on real bug."
```

Pi plain-language triggers (no slash needed):

```text
Use reviewer to review this diff.
Ask oracle for second opinion on my plan. Challenge assumptions.
Run parallel reviewers: correctness, tests, unnecessary complexity.
Use scout to inspect auth flow before planning.
Run this in background.
```

Pi-subagents details: `pi install npm:pi-subagents` (only step), `maxSubagentSpawnsPerRun=64` (bounded tree, separate from concurrency), FleetView below editor + `/subagents-fleet` inspector + machine-readable artifacts (`docs/observability.md`). Installing gives delegation tool, not auto-reviewer — add to project instructions if you want every implementation reviewed.

## Bounded Orchestration

- **Master:** OpenCode (main harness, owns build/test, owns AGENTS.md)
- **Specialists:** Pi `oracle` (challenge assumptions — Julia Pottinger), `scout` (fast recon), `reviewer` (check tests would fail), `researcher` (web/docs with sources)
- **Observability:** FleetView streams foreground; background keeps working; `/subagents-fleet` to steer/stop; artifacts for audit (EU AI Act Art 12 lineage).

## Minimal Setup (5 Minutes)

1. **AGENTS.md** in repo root with build/test + 3 rules you care about (even corrections from last week).
2. **mcp.json** with `playwright` + `github` + your `MCP proxy`; point both harnesses at it.
3. **Install:** `pi install npm:pi-subagents` + `opencode` (already).
4. **Prompt:** In OpenCode project instructions: "When you finish implementing, run a Pi reviewer subagent before summarizing."
5. **Try:** `Use scout to understand this code based on our discussion, then ask me clarification questions.` — Pi decides tool/agent/composition.

## Relevance to QA/QE

| Pattern | QA Application |
|---------|----------------|
| AGENTS.md as contract | Single definition of done, test conventions, risk/PR template — both harnesses obey |
| MCP shared bus | Real locators/timing, no invented selectors — fixes Playwright 80% flakiness at auth |
| Pi parallel reviewers | Mirrors staged autonomy: worker → reviewer (tests) / reviewer (correctness) / reviewer (cleanup) bounded to 3 rounds |
| Oracle second opinion | Implements "challenge assumptions" gate before high-risk merge |

## Critical Analysis

**Strengths:**
- No custom code — files + MCP + CLI, additive, Zalando-proven (MCP proxy + Bearer injection).
- Pi-subagents zero-config start (plain language) but composable (`/council`, `/review-loop`, `/parallel-review`) — progressive disclosure.
- Bounded (64) + FleetView — traceability for audit.

**Gaps:**
- Pi-specific (`pi-subagents` not portable to Kiro/Claude without adaptation); model volatility of TDD-like prompts across models.
- Requires you to write the PR block / CODEOWNERS rule — tool won't invent accountability.

## Cross-links

- Related: [pi-subagents](pi-subagents-2026.md) (scout/reviewer/oracle, FleetView)
- Related: [ruvnet agentic stack](ruvnet-agentic-stack-2026.md) (Ruflo/MetaHarness swarm — alternative harness)
- Related: [Zalando agentic snapshot](zalando-agentic-engineering-snapshot-2026.md) (MCP proxy, risk-based gate, Identity Broker)
- Related: [Julia Pottinger who-validates](julia-pottinger-who-validates-ai-generated-code-2026.md) (RACI + PR block — what reviewer checks)

---

*Ingested: 2026-09-03 · Via pi-subagents README + opencode.ai/docs + Zalando MCP proxy pattern; no native pi↔opencode wire, integration via files/MCP/CLI*
