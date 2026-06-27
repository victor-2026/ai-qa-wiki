# Hack'n'Vibe — AI Agent Builder

## Profile
- **Role:** AI agent builder, coder
- **Notable:** BitGN PAC1 — 3rd Accuracy, 5th Ultimate (April 2026, blind prod)
- **Telegram:** @hack_n_vibe — про AI-кодинг и доставку продукта в прод

## Product: BitGN PAC1 Agent
**Architecture:** Thin Python transport + Claude Code CLI as brain (no API keys in code)

**Key innovation:** 11 VM-native operations (tree, find, search, read, write, etc.) instead of a single `execute_code` — each maps 1:1 to gRPC. No sandbox, no middle layer.

**RULES.md:** Accumulated pattern dictionary — 9 stop-rules + 13 task patterns. Agent self-learns via `learn "..."` mechanism. Same concept as AGENTS.md + learned_patterns.json from MAS.

**Parallel execution:** `/solve-pac1` orchestrator spawns 10 subagents per batch, all 104 tasks solved simultaneously.

## Key Insights
- **Thin transport pattern:** Python never makes decisions — only Claude Code does
- **RULES.md as memory:** Growing checklist reusable across runs
- **Stop-rules are more valuable than do-rules:** Knowing what breaks is the real skill
- **Subagent parallelism over retry:** One precise parallel run > retries
- **Recon cycle:** tree 3 + read all → agent sees full context first

## Weaknesses Found (all documented in stop-list)
1. Context.time dates vs file dates
2. Recon truncation miscounts
3. Partial file scanning (manager lookup)
4. Conflicting instructions — Claude chooses instead of asking

## Relationship to our work
- **RULES.md** directly validates the AGENTS.md + checkpoint approach
- **Thin transport** = same separation we use (OpenCode decides, scripts execute)
- **Stop-rules** = useful pattern to borrow for QA skill self-evaluation
- **Subagent parallelism** = confirms our multi-agent Task approach

## Last updated
2026-06-18 — initial profile
