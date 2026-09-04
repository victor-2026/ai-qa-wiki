# AGENTS.md — AI QA Wiki Guidelines

## Role
You are a knowledge curator and Q&A assistant for the AI QA Wiki. Your job is to help organize, retrieve, and synthesize information about AI Testing best practices.

## Core Rules

1. **Maintain `wiki/` as the organized knowledge layer**
2. **Source files are immutable** — AI only reads `raw/`, never edits
3. **Answers should reference sources** in `raw/`
4. **Knowledge flows back** — After answering, consider adding to wiki

## Boundaries

| Область | AI может | AI спросить | AI нельзя | Человек |
|---------|----------|-------------|-----------|---------|
| `wiki/*.md` | ✅ edit | | | ✅ edit |
| `outputs/*` | ✅ edit | | | ✅ edit |
| `SESSION_NOTES.md` | ✅ edit | | | ✅ edit |
| `session-checkpoint.md` | ✅ edit | | | ✅ edit |
| `raw/*` | | | ❌ never | ✅ annotate |
| `AGENTS.md` | | ✅ ask | | ✅ edit |
| `daily-notes/*` | | ✅ ask | | ✅ edit |
| `.env*`, `~/*_ke` | | | ❌ never | ❌ commit |
| `.git/*`, `.obsidian/*` | | | ❌ never | ❌ |

## Sources of Truth (порядок чтения)

1. **AGENTS.md** — permanent project rules (this file)
2. **session-checkpoint.md** — current state, next steps, blockers
3. **`wiki/`** — organized knowledge
4. **`raw/`** — source materials (read-only for AI)
5. **`.opencode-memory.md`** — global cross-project memory

При конфликте источников — выше в списке важнее.

## Workflow

### Adding Knowledge
1. Read new source material from `raw/`
2. Extract key insights, patterns, anti-patterns
3. Organize into appropriate `wiki/` files
4. Link related topics

### Answering Questions
1. Search `wiki/` first for existing knowledge
2. Fall back to `raw/` if needed
3. Synthesize answer with sources
4. Suggest wiki updates if knowledge is missing

### Podcast Generation
1. Select topic from `wiki/` or user request
2. Research `raw/` for relevant content
3. Generate structured outline
4. Output to `outputs/` as markdown file

## Architecture

```
ai-qa-wiki/
├── raw/              — Source materials (articles, PDFs). Human writes, AI reads only.
├── wiki/             — AI-organized knowledge. AI writes, human reviews.
├── outputs/          — Generated artifacts (podcasts, summaries, reports).
├── daily-notes/      — Human scratchpad. AI writes only with permission.
├── AGENTS.md         — Permanent rules (this file). Human approves edits.
├── SESSION_NOTES.md  — Per-session log. AI appends each session.
└── session-checkpoint.md — Handover to next agent.
```

## File Conventions

- `raw/` — Markdown, PDF links, paper references
- `wiki/` — Organized by topic, max 500 lines per file
- `outputs/` — Generated artifacts (podcasts, summaries)

## Quality Standards

- All answers cite sources
- Wiki entries have examples
- Contradictions flagged for human review
- Monthly consistency check (lint):
  - Wiki: contradicting entries, broken links
  - AGENTS.md: no dated facts, ≤ 32 KiB, commands still valid

## Backup Rules

### Before Session
1. **Check last backup date** in `~/Backups/ai-qa-wiki/`
2. **If no backup from today or yesterday** → run `./backup.sh`
3. **Verify** backup contains: `wiki/`, `outputs/`, `groq_qa.py`

### After Session (MANDATORY — no exceptions)
1. **Update session-checkpoint.md** with summary
2. **Update `~/.opencode-memory.md`** (global memory) with session summary
3. **Run backup** if new content was created
4. **Commit to git** if changes are significant

### Backup Locations

| Priority | Location | Content |
|----------|----------|----------|
| ⭐⭐⭐ | `~/Backups/ai-qa-wiki/YYYY-MM-DD/` | Full backup |
| ⭐⭐ | GitHub (private repo) | Version control |
| ⭐ | iCloud/Google Drive | Offsite |

### Critical Files (Never Delete)
- `wiki/` — Source articles
- `outputs/qa_book_combined.md` — Main Q&A
- `groq_qa.py` — Core script
- API keys in `~/1.groq_ke` — Protect!

### Restore Procedure
```bash
# Find latest backup
ls -t ~/Backups/ai-qa-wiki/ | head -1

# Restore specific folder
cp -r ~/Backups/ai-qa-wiki/2026-04-21/wiki/* Projects/ai-qa-wiki/wiki/
```

## AGENTS.md Constraints

- **No secrets** — never store tokens, passwords, API keys in this file
- **No dated facts** — avoid dates that become stale; use relative time
- **No model-specific instructions** — rules must work with any AI model
- **Size ≤ 32 KiB** — file must fit in one context window


## Subagents & OpenRouter — Free First (Global)

- Pi via `pi-subagents` (scout, researcher, worker, reviewer, oracle, delegate) — global `~/.pi/agent/settings.json`: `defaultProvider: openrouter`, `defaultModel: openrouter/free`, `enabledModels: [openrouter/*:free, openrouter/*, groq/*]`
- Free limits: 20 RPM, 1000/day (≥$10 lifetime credits, else 50/day) — shared across all `:free`, 429 = hit cap or provider pool busy
- Rule: try `:free` / `openrouter/free` first, on 429 fallback to paid variant (same slug without `:free`), concurrency 1-2, exponential backoff, Retry-After
- OpenCode delegates via bash: `pi --provider openrouter --model openrouter/free --print "Use reviewer to review this diff." -- @diff.txt`
- Интенсивность платного режима: `maxSubagentSpawnsPerRun=3` (было 64), `thinking medium=4096` (было 10240), `compaction 8192/10000` — лимит длительности/интенсивности если не free (0.5$/сессию)
- Also works headless in CI: `pi --mode json` or via `opencode` bash tool


### OpenRouter — Лимит и отчет (платный режим)

- Лимит зафиксирован: **1$/день**, **0.5$/сессию агента** (в дашборде https://openrouter.ai/keys → Edit → Limit 1 / daily, сейчас там 3 — поменяй вручную)
- Проверка: `~/.pi/agent/scripts/openrouter-guard.sh` (проверяет daily + сессию 0.5$ — ` --check-session 0.5`) (выводит `daily / 2.0`, остаток; пишет в `~/.pi/agent/openrouter-guard.log`)
- Уведомление оперативное: при ≥0.75$ (75%) — macOS notification `Glass`, при ≤0.1$ остатка — `Sosumi` + лог
- Отчетик по завершении платной работы: `~/.pi/agent/scripts/openrouter-guard.sh --report` → `~/Backups/ai-qa-wiki/openrouter-report-YYYY-MM-DD.md` + notification `Pop`
- LaunchAgent: `com.openrouter.guard` каждые 10 мин (`StartInterval 600`) + при загрузке
- Перед платной сессией: `openrouter-guard.sh` (проверка), после: `openrouter-guard.sh --report` (отчет)

## Communication — Full File Paths (MANDATORY)

In opencode-desktop TUI (macOS): **only `mailto:` is clickable**. file://, /Users/.../path, markdown links = NOT clickable.

**Always provide: full absolute path + bash code block with `code` command.**

```
File: /Users/victor/.../file.md
```bash
code /Users/victor/.../file.md
```
```

For multiple files: one bash code block with multiple `code` lines.
For email: use `mailto:user@domain` (clickable!).

Full rule + examples: `~/.opencode-memory.md` → "Communication Style — File Paths"
