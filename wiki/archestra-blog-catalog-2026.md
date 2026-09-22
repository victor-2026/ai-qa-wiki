# Archestra Blog: Complete Publications Catalog with Annotations

**Source:** https://archestra.ai/blog
**Company:** Archestra.AI — open-source enterprise infrastructure for running AI agents + MCP across a company without losing control (agentic gateway, LLM proxy, MCP gateway, IFC-guardrails via OpenAPPA, code sandbox, access control). CNCF/Linux Foundation member. $3.3M pre-seed (Aug 2025), $10M seed led by 20VC (Jun 2026). Team: Matvey Kukuy (CEO, ex-Amixr/Grafana, ex-KeepHQ/Elastic), Ildar Iskhakov (CTO, ex-Principal Grafana), Joey Orlando (Co-founder), Arseny Kravchenko (Founding AI Engineer, author "ML System Design").
**Last updated:** 2026-09-22
**RSS:** none (Webflow) → manual digest source, follow via /blog + sitemap.xml

---

## Legend

- **Relevance:** HIGH / MEDIUM / LOW (for AI-QA / QE automation / VerdictGate)
- **Category:** Security | Agent Platform | MCP | Testing/Evals | Product Update | Tutorial | Community
- **Action:** FULL READ / SKIM / SKIP

---

## TIER 1: HIGH RELEVANCE (Read First)

| # | Date | Title | Category | Relevance | Action |
|---|------|-------|----------|-----------|--------|
| 1 | Sep 21, 2026 | [We Tested Jev on 100 Real Agent Calls](https://archestra.ai/blog/we-tested-jev-on-100-real-agent-calls) | Testing/Evals | HIGH | ✅ ingested → [wiki/archestra-jev-100-agent-calls-benchmark-2026.md](wiki/archestra-jev-100-agent-calls-benchmark-2026.md) + quotes.md |
| 2 | Sep 10, 2026 | [We Fix Small Bugs by Dropping a 🦀 in Slack](https://archestra.ai/blog/fixing-small-bugs-from-a-slack-thread) | Security | HIGH | ✅ ingested → [wiki/archestra-crab-bot-slack-agent-2026.md](wiki/archestra-crab-bot-slack-agent-2026.md) (agent self-review loop + OpenAPPA IFC) |
| 3 | Aug 12, 2026 | [Skills Aren't Prompts. They Can Run Code.](https://archestra.ai/blog/skills-arent-prompts-they-can-run-code) | Security | HIGH | ✅ ingested → [wiki/archestra-skills-aren-t-prompts-code-sandbox-2026.md](wiki/archestra-skills-aren-t-prompts-code-sandbox-2026.md) (log-as-truth sandbox, "skills carry the contract") |
| 4 | Jul 20, 2026 | [We Debug Our AI Harness on Weak Models on Purpose](https://archestra.ai/blog/we-debug-our-ai-harness-on-weak-models-on-purpose) | Testing/Evals | HIGH | ✅ ingested → [wiki/archestra-debug-harness-weak-models-2026.md](wiki/archestra-debug-harness-weak-models-2026.md) + quotes.md. Weak models as smoke-alarm; 26-task nightly bench; deterministic grader, hidden ground truth, full trajectory vs score; bugs found table; cost/capability cross-rank |
| 5 | Oct 13, 2025 | [The Archestra Dual LLM Pattern (Guess Who?)](https://archestra.ai/blog/dual-llm) | Security | HIGH | FULL READ (prompt-injection defense via dual-LLM; "author vs examiner" sister pattern) |

## TIER 2: MEDIUM RELEVANCE (Feature Covers)

### Security & Prompt Injection
| Date | Title | Action |
|------|-------|--------|
| Oct 13, 2025 | [What is a Prompt Injection?](https://archestra.ai/blog/what-is-a-prompt-injection) | SKIM |
| Feb 4, 2026 | [How to Run OpenClaw Securely](https://archestra.ai/blog/how-to-run-openclaw-securely) | SKIM (lethal trifecta ref) |
| Mar 30, 2026 | [Enterprise-Managed Authorization for MCP](https://archestra.ai/blog/enterprise-managed-authorization-mcp) | SKIM |
| — | [The lethal trifecta in one diagram](https://archestra.ai/blog/lethal-trifecta-definition) | SKIM |

### MCP Ecosystem (platform notes, no dates on /blog Notes tab)
| Title | Action |
|-------|--------|
| [MCP Security Checklist: 7 Pre-Install Checks](https://archestra.ai/blog/mcp-security-checklist) | SKIM |
| [How to test MCP servers: three layers](https://archestra.ai/blog/testing-mcp-servers) | SKIM |
| [Every 10th MCP server is one person (supply chain risk)](https://archestra.ai/blog/mcp-supply-chain-risk) | SKIM |
| [MCP tool description drift: how to detect](https://archestra.ai/blog/mcp-tool-description-drift) | FULL READ (drift = fragility, aligns locator-drift) |
| [MCP tool descriptions are prompts, not docs](https://archestra.ai/blog/mcp-tool-descriptions-as-prompts) | SKIM |
| [State of MCP, mid-2026 snapshot](https://archestra.ai/blog/state-of-mcp-2026) | SKIM |

### Evals / Agent Reliability
| Title | Action |
|-------|--------|
| [Why agents feel solid at first, then quietly get worse](https://archestra.ai/blog/why-agents-drift) | FULL READ (retain-on-failure, drift) |
| [Agent liability, the question nobody answers](https://archestra.ai/blog/who-is-liable-when-an-agent-acts) | FULL READ (attestation/accountability) |
| [The minimum agent observability stack](https://archestra.ai/blog/agent-observability-minimum) | SKIM |
| [Most AI governance is a doc on paper vs enforced](https://archestra.ai/blog/ai-governance-on-paper-vs-enforced) | FULL READ (governance vs enforced = attestation) |
| [Why "fully autonomous" is rarely the answer](https://archestra.ai/blog/autonomy-is-a-product-decision) | SKIM |

## TIER 3: LOW RELEVANCE (Skip)

- Product-обновления платформы (New: Apps, Migration Kit, Projects, 1.3 Lyra) — SKIP
- Funding/company news (seed, CNCF, welcome posts) — SKIP
- MCP brevidas (OAuth 2.1 quickref, JWKS, PKCE, spec history) — SKIP unless MCP-work starts
- Integration shout-outs (Helicone, Kong, OpenRouter, LiteLLM, etc.) — SKIP

---

## Category Breakdown

| Category | Posts | HIGH relevance |
|----------|-------|----------------|
| Security (IFC, OpenAPPA, sandbox, prompt injection) | ~25 | 4 |
| MCP protocols & gateway | ~45 | 1 (+2 drift/descr) |
| Testing & Evals (Jev, harness, benchmarks) | ~4 | 2 |
| Agent platform & product | ~20 | 0 |
| Agent reliability / governance | ~8 | 3 |
| **Total** | **~100+ (магазин + ~60 Notes)** | **~10** |

---

## Why This Blog Matters (для нашей серии)

1. **Jev benchmark (#1)** — 79% constant trap, stalls-vs-leaks, don't-grade-own-homework, labels-hold/probabilities-drift (SCORER_VERSION parallel). Всё в quotes.md.
2. **IFC / OpenAPPA (gov рабult) (#2)** — data-leak prevention at tool-call boundary = real-world "silent false negative" wiring. Read-by-construction + requester-credentials = least-privilege для агентов.
3. **Log-as-truth sandbox (#3)** — append-only command log outlives the container = репродуцибельность evidence pack. Threat-model honesty = risk-tiering без театра.
4. Company = открытая агентная инфраструктура (не AI-QA vendor). Для VerdictGate-ландшафта: **orchestration/guardrail-слой**, не verdict-слой (см. продукт-концепт §13 — Testkube precedent).

---

*Источники: [raw/archestra-jev-100-agent-calls-benchmark-2026.md](raw/archestra-jev-100-agent-calls-benchmark-2026.md), [raw/archestra-crab-bot-slack-agent-2026.md](raw/archestra-crab-bot-slack-agent-2026.md), [raw/archestra-skills-aren-t-prompts-code-sandbox-2026.md](raw/archestra-skills-aren-t-prompts-code-sandbox-2026.md)*




<!-- backlinks-start -->
### Backlinks
- [Archestra Crab Bot Slack Agent 2026](wiki/archestra-crab-bot-slack-agent-2026.md)
- [Archestra Jev 100 Agent Calls Benchmark 2026](wiki/archestra-jev-100-agent-calls-benchmark-2026.md)
- [Archestra Skills Aren T Prompts Code Sandbox 2026](wiki/archestra-skills-aren-t-prompts-code-sandbox-2026.md)
<!-- backlinks-end -->
