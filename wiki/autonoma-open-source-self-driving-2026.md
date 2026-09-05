---
title: "Autonoma Open Source & Architecture (June 2026)"
type: article
updated: "2026-08-17"
tags: [autonoma]
---

# Autonoma Open Source & Architecture (June 2026)

## Announcement

April 2026: Autonoma went source-available (BSL 1.1) and announced a new "self-driving testing" architecture. The previous pipeline (used in our Phase 3 experiments) was acknowledged as deprecated.

**Source:** [Introducing Open-Source AI Self-Driving Testing](https://getautonoma.com/blog/introducing-open-source-ai-self-driving-testing)

## License

| Что | Статья (ошибочно) | Реальность |
|-----|-------------------|------------|
| License | Apache 2.0 (fully open source) | **BSL 1.1** — source-available. Apache 2.0 only from **March 23, 2028** |
| Status | Free alpha | **Stable**. Free tier, pay-as-you-go, self-hosted |
| Docs URL | `docs.agent.autonoma.app` | **`docs.autonoma.app`** |

## Claude / Anthropic Integration

**Autonoma's Test Planner is a Claude Code plugin.** This is their primary integration channel:

- Installation: `/plugin marketplace add Autonoma-AI/test-planner-plugin`
- Runs as: `/autonoma-test-planner:generate-tests`
- Internal: uses `claude -p --output-format json` for subagent calls
- Plans: OpenAI Codex (coming soon), OpenCode (coming soon)

**Implication:** Autonoma's cloud pipeline runs on Anthropic Claude models. Requesting API credits for Claude from Autonoma is valid — their service depends on it.

## Architecture

### Test Planner (Claude Code Plugin) — 6-step pipeline

The current Test Planner is a **Claude Code plugin** with 6 deterministic steps, each gated by shell-script validators (not LLM checks):

| Step | What it does | Produces |
|------|-------------|----------|
| 1. Knowledge Base | Analyzes frontend codebase — pages, flows, UI patterns | `AUTONOMA.md` + `features.json` |
| 2. Entity Audit | Inspects backend codebase for model creation functions | `entity-audit.md` (factory vs raw SQL) |
| 3. Scenarios | Reads DB schema, designs 3 test data environments (standard/empty/large) | `scenarios.md` |
| 4. Env Factory | Installs Autonoma SDK, registers factories calling real service code | Working endpoint + `.endpoint-implemented` |
| 5. Validate | Runs discover→up→down lifecycle, iterates up to 5x on failures | `scenario-recipes.json` + `.endpoint-validated` |
| 6. E2E Tests | Generates markdown test files distributed by priority (core flows 50-60%) | `qa-tests/` + `INDEX.md` |

Validation gates: PostToolUse hooks, cross-file consistency checks, preflight on `scenario-recipes.json`. Step 6 blocked until `.endpoint-validated` exists.

Review checkpoints after each step — not optional, determines test quality.

### Self-Driving Architecture (4 components)

Separate from the Test Planner — the cloud platform's architectural vision:

1. **Test user generation & management** — automatic data seeding, adapts to schema changes
2. **Test plan generation, editing, deprecation, execution** — scales with codebase
3. **Test preview environments** — auto-provisioned per branch/PR
4. **Parallel test infrastructure** — Web (Playwright) + Android (Appium) + iOS (Appium)

### Execution Agent

Vision-based AI agent. Loop: Screenshot → LLM → Command → Record.

- Uses **PointDetector** — LLM sees screenshot, identifies elements visually (not CSS selectors)
- Self-healing: if element changes, vision adapts naturally
- Runs on real browsers and devices

## Technology Stack

| Component | Tech |
|-----------|------|
| Runtime | Node.js 24 (ESM-only) |
| TypeScript | strictest config |
| Frontend | React 19, Tailwind CSS v4 |
| Database | PostgreSQL 18 |
| Orchestration | Temporal |
| Infra | Kubernetes |
| AI Models | Gemini, Groq, OpenRouter (configurable) |

## Pricing (as of June 2026)

| Tier | Cost | Details |
|------|------|---------|
| Free | $0 | 100K credits |
| Pay-as-you-go | $100 | 150K credits |
| Self-hosted | Free | Requires K8s + Temporal (not trivial) |

## Market Data

| Metric | Value | Source |
|--------|-------|--------|
| SOC 2 Type II | Certified (Feb 2026) | trust.delve.co/autonoma |
| GitHub stars | ~118 | github.com/autonoma-ai/autonoma |
| Forks | ~27 | github.com/autonoma-ai/autonoma |
| ARR | $11.1M | Bootstrapped |
| Team | 101–169 employees | LinkedIn |
| Enterprise clients | 20+ (fintech, retail, tech) | Groq case study |

### Groq Case Study (their data)

| Metric | Value |
|--------|-------|
| Regression testing | 3 days → single-digit minutes |
| Tests/week | Hundreds of thousands |
| Inference | GroqCloud (time-to-first-token: seconds → ms) |
| Team origin | 4 ex-Google engineers |
| Test creation | Plain English → real-time execution |

**Note:** The Groq numbers are **vendor case study claims**, not independently verified.

## Our Experience vs Their Marketing

### Their landing page demo output
```
$ npx @autonoma-ai/planner@latest
✓ 23 routes · 48 components · 12 APIs
✓ 156 test cases ready
│ 42 happy paths
│ 38 edge cases
└ 47 state transitions
```
**Source:** `getautonoma.com` — fictional demo animation, not measured.

### Our Phase 3 experiment (OrangeHRM, old pipeline)
| Metric | Our result |
|--------|-----------|
| Routes discovered | 13 POM routes |
| Entities audited | 14 models, 6 factory stubs |
| Tests generated | 28 .md descriptions |
| Pipeline cost | ~$4.99 (2 sessions) |
| Context overflow | Confirmed at entityAudit (~274K > 131K) |
| Model auto-switching | Yes — deepseek → kimi → gpt without asking |

### Key differences
- Their demo: fictional numbers for a perfect scenario
- Our experience: real constraints (context limits, auto-switching, incomplete stubs)
- Their new Test Planner (Claude Code plugin) may address some issues but we have not tested it

## What Changed: Old Pipeline vs Current

| Aspect | Old pipeline (we tested) | Current Test Planner |
|--------|-------------------------|---------------------|
| Count | 6 steps (different) | 6 steps (different) |
| Sequence | pagesFinder → KB → entityAudit → scenarioRecipe → testGenerator → environmentFactory | KB → Entity Audit → Scenarios → Env Factory → Validate → E2E Tests |
| Validator | None (accumulative context) | Deterministic shell-script per step |
| Claude | Plugin for Claude Code | Plugin for Claude Code (same) |
| Architecture | "Test generation" | "Test generation + isolated data seeding" |
| Data seeding | Not integrated | Environment Factory SDK |
| Status | Deprecated by CEO | Current |

**Flag (human review):** the observed Phase 3 run log (`autonoma-orangehrm-setup-notes.md`, 2026-06-10) shows an intermediate step `recipeBuilder` between `scenarioRecipe` and `testGenerator` (5/7 steps, paused). GitHub sources (`test-planner-plugin`, `test-planner`) document `testGenerator → environmentFactory` as steps 5–6. The row above follows the GitHub source per `raw/Autonoma - шаги в пайплайне.md` (ingested 2026-08-17); the observed run may predate the rename.

## Open Source Commitments

- **Quality for everyone** — democratizing shipping confidence
- **Your code, our code** — transparent engine
- **No lock-in** — deploy, extend, fork

## Links

- GitHub: https://github.com/autonoma-ai/autonoma
- Test Planner Plugin: https://github.com/Autonoma-AI/test-planner-plugin
- Test Planner (4-step skill): https://github.com/Autonoma-AI/test-planner
- Discord: https://discord.com/invite/nsYQExXTsQ
- Cloud: https://agent.autonoma.app/
- Docs: https://docs.autonoma.app/
- Blog: https://getautonoma.com/blog/

## Implications

- The old pipeline (tested in Phase 3 at ~$4.99) is deprecated by the vendor
- New Test Planner (Claude Code plugin) may address context overflow with per-step validation gates
- Self-hosting is free but requires K8s + Temporal — not a simple `docker compose up`
- Autonoma's real differentiator is the **Environment Factory** (real data seeding through your own service functions), not test generation
- The "pipeline vs point tool" framework (Article 4) remains valid for the version tested; current Autonoma may shift the comparison
- Worth re-evaluating once Claude Code plugin is tested on OrangeHRM

## Positioning (from getautonoma.com FAQ, Jul 2026)

| Question | Answer |
|----------|--------|
| **vs Playwright/Appium?** | "Playwright/Appium = kernel (low-level). Autonoma = OS on top. AI agents understand your app, generate tests, adapt. Same reliability, zero test code." |
| **vs Claude + Playwright scripts?** | "Claude generates scripts — 10% of the problem. Still need: isolated environments, seed data, parallel execution, flaky handling, validation that tests actually test the right thing." |
| **Replaces QA?** | "Yes. QA was a bottleneck. No human team multiplexes across 7 features. Autonoma runs thousands of tests in parallel, no backlog." |
| **Handles UI changes?** | "AI agents understand what your app does, not just where buttons are. Tests adapt automatically." |
| **Open source?** | "Fully open source. Self-hosted free forever, no feature limits." |

## Related

- [Autonoma OrangeHRM Setup Notes](./autonoma-orangehrm-setup-notes.md) — old pipeline experience
- [AI Testing Platform Comparison 2026](./ai-testing-platform-comparison-2026.md) — competitive landscape





























<!-- backlinks-start -->
### Backlinks
- [AI in QA Issue #17 — Butch Mayhew (Jul 6, 2026)](wiki/ai-in-qa-issue-17-butch-mayhew-2026.md)
- [Ai Productivity Paradox Verification Layer 2026](wiki/ai-productivity-paradox-verification-layer-2026.md)
- [Autonoma Шагивпайплайне](wiki/autonoma-шагивпайплайне.md)
- [Claude Code Ci Cd Mcp 2026](wiki/claude-code-ci-cd-mcp-2026.md)
- [Claude Code Skill Examples 2026](wiki/claude-code-skill-examples-2026.md)
- [Iso 14971 Risk Management 2026](wiki/iso-14971-risk-management-2026.md)
- [MCP + UCP: Open Protocols for Agentic QA (2026)](wiki/mcp-ucp-protocols-2026.md)
- [Modeloptimizingagainstqualitygateinsteadofactualproblem](wiki/modeloptimizingagainstqualitygateinsteadofactualproblem.md)
- [Десктопные AI-агенты для кода (2026)](wiki/desktop-ai-agents-2026.md)
<!-- backlinks-end -->
