# Agentic Engineering at Zalando: a snapshot

**Author:** Bartosz Ocytko (Executive Principal Engineer)
**Published:** 2026-08-14
**Source:** https://engineering.zalando.com/posts/2026/08/agentic-engineering-at-zalando-a-snapshot.html
**Fetched:** 2026-09-01

---

Zalando snapshot 2.5 years agentic engineering, 250+ teams.

## LLM proxy for API-based LLM access from day 1

GitHub Copilot from early days. Jan 2024 LiteLLM-based API proxy (OpenAI, AWS Bedrock, Google Vertex). Single point to measure adoption via MAU, WAU, model, User-Agent. Extensibility: post-call hooks for anonymized cost tracking, pre-call hooks for enforcing client version upgrades via User-Agent header, auto-injection of prompt caching checkpoints, restart after 20k requests (--max_requests_before_restart) → 2k MAU with six small pods (2 CPU, 4GB). Rust rewrite expected.

### Beyond the API: Chat UI and CLI

Chat UI (fork OSS) still high adoption. CLI (custom pydantic-ai, hackathon Aug 2024): generating images, interactive multi-turn, agent mode with MCP support and automatic Bearer token injection, http to stdio MCP proxy, built-in MCP config, coding agent config command (claude code, opencode, pi + plugins for autodiscovery). Token injection avoids hardcoding secrets.

### Challenges

Generic User-Agent makes client identification hard → require name/repo/version in User-Agent for own apps, request upstream. Tools lack custom auth commands → local proxy injects auth headers, plugins for model discovery, TUI for costs/cache.

## Vendor independence

Never centrally mandated single tool. Users choose (Copilot/opencode/pi). Open tools allow mixing Copilot subscription + API. Psychological inertia to switch despite low switching costs. Reference configs via git + CLI command.

## Identifying the impact of AI coding

PRs: increase in sizes [100,500), growth in [500,1k) and [1k,2k) since Sonnet 4 Q2/2025. Teams limit PR sizes via agreements.

Code complexity: CCN inflection when agents appear. 4 codebases tracked (go-agentic-only new full, go-reference 10y+ OSS, java-with-agents 4y from commit>1600, java-reference 12y+ none). Commit message size bloat (~5k chars, extreme: full test log in commit) → pre-commit hook candidate.

## Risk-based PR approval

Bot at PR creation evaluates rollout risk low/medium/high. 33% low-risk auto-approved → lead time -20-40%. Rules from prod incident analysis: typos in config = high, breaking backwards-compat = medium + human judge, docs only = low. Behavior: engineers split PRs to get low-risk auto-approve.

## Learning from session data

Spot non-essential traffic (plan names, recaps), low cache hit ratio (<30% vs 80%+ expected) via parser, agentsview.io and codeburn for analysis.

## Agent skills

Centralized collection grouped into plugins, CI validation, separation concerns, inspiration via agent-skills-eval.

## Governance

Tech Radar AI section, Sunrise (Backstage), legal per use-case, auto-detect AI model usage via Docker image scan + portal registration.

## Knowledge sharing

LLM guild weekly 1h (20-min slots), hackathons guided experimentation (4-6 people, 2-3 days, predefined goals), GenAI Labs → monthly trainings (MCP, pydantic-ai, coding agents, skills, loops). Balance with Engineering Fundamentals track.

## Getting to the next level

Scanner AI readiness per repo, fleet transformations via coding agent CLI, platform from OSS (kagent runtime, Identity Broker for delegation chains/on-behalf-of, token vault). Next: device management, local sandboxing, auto-routing models, Shopify Quick-inspired prototype sharing for non-engineers.

## What's next?

AI amplifies good and bad practices — large PRs discourage reviewers. Investments pay off: web monorepo per-PR deployment wired to live data enables agents + non-engineers to prompt changes. Agent platform composing OSS.

*Related: Search QA with LLM-as-judge, product data enrichment, frontend migrations linked in post.*

