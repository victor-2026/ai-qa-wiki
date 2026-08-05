# Kiro.dev — AWS Agentic AI IDE

Source: https://kiro.dev (+ docs, blog, community articles)

## Overview

Kiro is an agentic AI IDE built by AWS, launched at AWS Summit NYC in July 2025. Built on Code OSS (VS Code fork). Available as IDE, CLI, Web, and Mobile (iOS early access 2026).

Notable: Kiro is a standalone product — no AWS account required (GitHub/Google sign-in works). AWS Builder ID / IAM SSO for enterprise.

## Key Concepts

### Spec-Driven Development
- Prompts → `requirements.md` + `design.md` + `tasks.md`
- AI asks clarifying questions before writing code
- Specs stay in sync with code as it evolves (via hooks)
- Specs check for contradictions/gaps via automated reasoning before code is written

### Agent Steering
- `.kiro/steering/` — coding standards, architectural patterns, naming conventions
- 3 files: `tech.md`, `structure.md`, `product.md`
- Enforced per-project, team-wide

### Hooks
- Event-driven automation: on save, commit, PR
- Examples: auto-update requirements.md on file change, run tests, lint, security scan
- Enforce consistency across teams

### ACP (Agent Client Protocol)
- Implemented Feb 2026
- Works with: Eclipse, Emacs, JetBrains IDEs, Neovim, Toad, Zed
- Allows using Kiro agent from any ACP-compatible editor

### Property-Based Testing (PBT)
- Built-in PBT checks (like fuzz testing)
- Catches edge cases unit tests miss
- Verifies code matches spec intent, not just example cases

### Multi-Agent: Parallel Sub-Agents
- Specs → sequenced tasks → parallel agents implement
- Tasks linked to requirements, include unit tests, integration tests, loading states, mobile responsiveness

### Models
- Auto mode (recommended): chooses best model per task complexity
- Claude Opus 4.8, Sonnet 4.6/4.5, Haiku 4.5
- DeepSeek v3.2, MiniMax M2.5
- Custom models via `.kiro/agents.yaml` (billed separately via AWS Bedrock)

### Enteprise
- SSO / IAM / identity provider
- Governance policies, cost management, usage dashboards
- IP indemnity
- SOC 2 Type II (via AWS compliance)
- Privacy: code stays on local machine (IDE/CLI), or in isolated cloud sandboxes (Web)

## Pricing (Credit-Based)
- Free tier available
- No daily/weekly rate limits
- Pre-paid overages (cap, no surprise bills)
- Credits per model: Auto = 1x, Claude Opus = 2.2x, Sonnet = 1.3x, Haiku = 0.4x, DeepSeek = 0.25x

## Competitive Positioning

### vs Cursor
- Cursor: better for rapid prototyping, GitHub-native, advanced context navigation
- Kiro: structured dev flow, spec-first, hooks, infra-as-code, enterprise governance

### vs Copilot
- Copilot: integrated in GitHub/VS Code, agile teams
- Kiro: full IDE replacement, spec lifecycle, parallel agents, hooks

### vs Cline / Claude Code / OpenCode
- Kiro: full IDE (not just CLI/agent), spec lifecycle, hooks, enterprise
- Others: lighter, CLI-first, more flexible for custom workflows

## Kiro from QA Perspective

1. **Spec-First = Testable Specs**: Specs include test requirements (unit, integration, loading states, mobile responsiveness) — testability is built-in, not afterthought
2. **PBT Built-In**: Property-based tests catch what unit tests miss — aligns with Victor's PBT + fast-check approach
3. **Hooks = Quality Gates**: Event-driven hooks can enforce test automation, lint, security scan at every save/commit — aligns with Anton Gulin's 6 gates
4. **Specs as Golden Dataset**: Specs can serve as golden dataset for LLM testing — verify generated code against spec
5. **ACP = Any Editor**: Can use Kiro agent from JetBrains, Zed, Neovim — not locked into Kiro IDE
6. **No QA-specific features**: Kiro is dev tool, not QA/test tool. No test management, no Allure integration, no test analytics
7. **PBT ≠ Mutation Testing**: Kiro's PBT checks correctness against spec invariants, doesn't kill mutants or measure test quality

## Key People
- **Haim Michael** — Zindell Technologies CEO, uses Kiro since day 1, builds AI-aligned ventures
- **Brian Beach** — Tech Lead, ACP integration

## References
- https://kiro.dev
- https://kiro.dev/blog/kiro-adopts-acp (Feb 2026)
- https://dev.to/aws-builders/kiro-the-new-agentic-ai-ide-from-aws-5311
- https://devops.com/aws-previews-ai-ide-to-accelerate-software-development/
- https://agentmarketcap.ai/blog/2026/04/11/amazon-kiro-ai-ide-aws-2026
