# Boris Cherny — Claude Code Practical Tips (Anthropic, 2026)

**Source:** https://www.youtube.com/watch?v=XFYUKBPfUMw
**Speaker:** Boris Cherny (Member of Technical Staff, Anthropic; creator of Claude Code)
**Event:** Anthropic internal/conference talk
**Duration:** ~27 minutes

---

## What Is Claude Code

- Fully agentic (not line-by-line completion)
- For building features, writing entire functions/files, fixing entire bugs
- Works with all IDEs (VS Code, Xcode, JetBrains, Vim, Emacs), all terminals, SSH, tmux
- General purpose — no forced workflow
- **CLI was chosen because:** (1) common denominator across IDEs, (2) models improving so fast that "by end of year people aren't using IDEs anymore"

---

## Setup Tips

1. Run `/terminal-setup` (shift+enter for newlines)
2. `/theme` for light/dark mode
3. `/install-github-app` (at-mention Claude on any GitHub issue/PR)
4. Customize allowed tools (don't get prompted every time)
5. Enable macOS dictation (speak prompts instead of typing)

---

## Tip 1: Start with Codebase Q&A

> "Onboarding used to take about two or three weeks for technical hires. It's now about two or three days."

- Ask questions about the codebase first (don't start by editing)
- No indexing — code stays local, no upload, no training on your code
- Claude goes deeper than text search (finds usage examples, git history, issues)
- Teaches boundaries: what can be one-shotted, what needs iteration

---

## Tip 2: Let It Brainstorm Before Coding

> "Before you write code, make a plan. That's it."

- Ask for brainstorming/planning before implementation
- Avoids "3000 line feature that isn't what you wanted"
- No special tools needed — just ask

---

## Tip 3: Give It Self-Check Tools

> "When Claude has some way to check its work, it can iterate. And this is incredible."

- Unit tests, screenshots (Puppeteer), iOS simulator screenshots
- Give it a mock → it builds UI → iterates 2-3 times → nearly perfect
- **Key insight:** "Give it some sort of tool that it can use for feedback to check its work, and then based on that it will iterate by itself"

---

## CLAUDE.md = Team Configuration

- **Project CLAUDE.md:** checked into source control, shared with team
- **Local CLAUDE.md:** personal, not checked in
- **Nested CLAUDE.md:** auto-loaded when working in subdirectories
- **Enterprise CLAUDE.md:** rolled out to all employees
- Contains: common commands, style guide, core files, architectural decisions
- Keep it short (too long = wasted context)
- **`/memory` command** to view/edit all memory files

---

## Permission System (Tiered)

- Read-only bash commands: auto-approved
- Static analysis determines safe command combinations
- Allow-list and block-list at different levels
- **Block URLs** that should never be fetched (enterprise policy)
- **Auto-approve safe commands** for all employees (enterprise policy)

> "The hardest part of implementation... making bash commands safe. Bash is inherently dangerous, but manual approval of every command is annoying."

---

## Claude Code SDK

- `claude -p` flag = SDK = CLI
- Pass prompt, allowed tools, output format (JSON, streaming JSON)
- "Super intelligent Unix utility" — pipe in, pipe out
- Used in CI, incident response, pipelines
- Git status → pipe → claude → JQ → result

---

## Power Users

- Multiple parallel sessions (SSH, tmux, Git worktrees)
- 80% of Anthropic technical staff use Claude Code daily
- Researchers use notebook tool for ML work

---

## Key Quotes

- "It's a power tool. You can use it for a lot of things."
- "Onboarding used to take about two or three weeks... now about two or three days."
- "When Claude has some way to check its work, it can iterate."
- "Give it some sort of tool for feedback... it will iterate by itself."
- "CLAUDE.md... automatically read into context at the start of every session."
- "The hardest part... making bash commands safe. Bash is inherently dangerous."
- "I think there's a good chance that by the end of year people aren't using IDEs anymore."

---

## Connections to Our Work

- **CLAUDE.md = our AGENTS.md pattern** — team-shared, hierarchical, version-controlled configuration
- **"Give it self-check tools" = Article 27:** verification loop = agent writes code, agent checks work (via tests), human governs the system
- **Tiered permissions = B0-B3 gates:** read-only = auto, dangerous = manual approval, enterprise block-list
- **Onboarding 2-3 weeks → 2-3 days** = codebase Q&A as the killer app (not code generation)
- **SDK as Unix utility** = VerdictGate design (CLI tool, pipe in, pipe out, JSON verdict)
- **"People won't use IDEs anymore"** = shift to CLI-first, verification-first workflows
- **80% adoption internally** = dogfooding as quality signal

---

## Related Wiki

- `wiki/tornhill-farewell-tdd-agents-2026.md` — same shift (TDD → e2e boundaries)
- `raw/adamtornhill-practices-abandoned-agents-2026.md` — code for machine consumption
- `raw/testmuai-llm-evaluation-vs-e2e-agent-testing-2026.md` — eval vs test
- Article 27: "QA Didn't Get Replaced. It Got Promoted."
