# Postman Blog — Complete Publications Catalog

**Source:** https://blog.postman.com/ (All Things API: News, Tutorials & More)
**Total articles:** ~1,127 (sitemap: post-sitemap.xml 992 + post-sitemap2.xml 135, filtered; excludes page-sitemap; lastmod 2026-08-31)
**Last updated:** 2026-08-31
**Feed:** https://blog.postman.com/feed/
**Focus for QA/QE:** API lifecycle, QE platform, AI agents & API discovery, governance, spec/collection/server drift

---

## Legend

- **Relevance:** HIGH / MEDIUM / LOW (for QA/QE automation engineer, API+AI focus)
- **Category:** API Design | Testing & QE | AI | Engineering | Product
- **Action:** FULL READ / SKIM / SKIP

---

## TOP 15 Must-Read for AI-QA / API-QA (2026 Highlights)

### QE Platform & Structural Problems (HIGH — Rick Crawford series)

| # | Title | URL | Date | Relevance |
|---|-------|-----|------|-----------|
| 1 | [Your QE Program Has a Structural Problem, and AI Just Made It Visible](https://blog.postman.com/your-qe-program-has-a-structural-problem-and-ai-just-made-it-visible/) | 2026-08-12 | **HIGH** |
| 2 | [5 QE Pipeline Metrics That Show Where Quality Is Leaking](https://blog.postman.com/5-qe-pipeline-metrics-that-show-where-quality-is-leaking/) | 2026-08-21 | **HIGH** |
| 3 | [QE Platform Strategy: 3 Paths and Where Each Hides Its Cost](https://blog.postman.com/qe-platform-strategy-3-paths-and-where-each-hides-its-cost/) | 2026-08-31 | **HIGH** |

*Series: 6 structural gaps → 5 metrics (Design/Gate/Validate/Monitor/Improve) → 3 paths + 90-day plan. Part 1 is your UTM link with `?utm_source=softwaretestingweekly` — same content.*

### AI, Agents & API Discovery (HIGH)

| # | Title | URL | Date | Relevance |
|---|-------|-----|------|-----------|
| 4 | [How AI Agents Discover and Integrate Public APIs](https://blog.postman.com/how-ai-agents-discover-and-integrate-public-apis/) — Anthony Viard, Orbit | 2026-08 | **HIGH** |
| 5 | [Finding three-way API drift with the AI Engineer](https://blog.postman.com/finding-three-way-api-drift-with-the-ai-engineer/) — Talia Kohan | 2026-08 | **HIGH** |
| 6 | [Why AI coding agents need context graphs](https://blog.postman.com/why-ai-coding-agents-need-context-graphs/) — Talia Kohan | 2026-08 | **HIGH** |
| 7 | [Introducing Orbit: Turn Any Task Into the Right API Calls](https://blog.postman.com/introducing-orbit-turn-any-task-into-the-right-api-calls/) — Abhinav Asthana | 2026-08 | **HIGH** |
| 8 | [Computing is changing, so is Postman – Introducing Postman.ai](https://blog.postman.com/introducing-postman-ai/) — Abhinav Asthana | 2026-08 | **HIGH** |
| 9 | [How Postman Passport keeps API secrets inside your network](https://blog.postman.com/how-postman-passport-keeps-api-secrets-inside-your-network/) | 2026-08 | **HIGH** |

### API Governance & Design

| # | Title | URL | Date | Relevance |
|---|-------|-----|------|-----------|
| 10 | [Why API Governance Programs Break Down, and What the Successful Ones Do Differently](https://blog.postman.com/why-api-governance-programs-break-down-and-what-the-successful-ones-do-differently/) — Rick Crawford | 2026-07 | **HIGH** |
| 11 | [API-First Strategy](https://blog.postman.com/tag/api-first/) (tag) | 2025-2026 | MEDIUM |
| 12 | [Tutorials: Spec Hub, Mock Servers, Collection Runner](https://blog.postman.com/tag/tutorials/) | 2026 | MEDIUM |

### Product & Engineering (SKIM)

| # | Title | URL | Date | Relevance |
|---|-------|-----|------|-----------|
| 13 | [Postman Product Updates July/August/November 2025-2026](https://blog.postman.com/tag/product-updates/) | 2026 | MEDIUM |
| 14 | [Engineering Spotlights](https://blog.postman.com/engineering/) | 2025-2026 | LOW |
| 15 | [Company News](https://blog.postman.com/tag/company-news/) | 2025-2026 | LOW |

*Full tag list at /tag/ — AI, API-First, Product Updates, Engineering, Company News, Tutorials (6 main + 20+ sub-tags).*

---

## Category Breakdown (Sampled — Estimates)

| Category / Tag | Example URL Pattern | Est. Count | HIGH | Action |
|----------------|---------------------|------------|------|--------|
| AI — AI agents, Orbit, Context Graphs, Postman.ai, Passport | /tag/ai/ | ~40 | ~15 | FULL READ |
| QE Platform / API Lifecycle / Governance | /your-qe-program..., /why-api-governance... | ~25 | ~10 | FULL READ |
| API Design & Spec Hub / Mock / Collection Runner | /tag/api-first/, /tag/tutorials/ | ~200 | ~20 | SKIM |
| Engineering (spotlights, architecture) | /engineering/ | ~150 | ~5 | SKIM |
| Product Updates | /tag/product-updates/ | ~300 | ~5 | SKIM |
| Company News / Culture | /tag/company-news/ | ~200 | — | SKIP |
| Tutorials | /tag/tutorials/ | ~250 | ~10 | SKIM |
| **TOTAL** | sitemap 992+135 | **~1,127** | **~65** |  |

*Counts estimated from sitemap (992+135) + index pagination + tag samples (2026-09-03). Use as order-of-magnitude.*

---

## Summary Statistics

| Tier | Count (est.) | % | Action |
|------|--------------|---|--------|
| HIGH relevance (read first) | ~65 | ~6% | FULL READ |
| MEDIUM relevance (skim) | ~200 | ~18% | SKIM |
| LOW relevance (skip) | ~862 | ~76% | SKIP |

---

## Key Strengths & Gaps (for QA/QE)

**Strengths:**
- Authoritative on QE platform as system (6 gaps → 5 metrics → 3 paths) — complements Zalando's risk-based PR gate with pipeline-wide view.
- AI×API discovery (Orbit, three-way drift, context graphs, Passport) — directly maps to API testing, spec/collection/server drift detection, secret management.
- Governance lens (API governance breakdown, successful programs) — parallels Martin Fowler's data-contracts/governance.

**Gaps / Watch-outs:**
- Product-led blog — signal/noise ~6% HIGH; many release notes, spotlights, company news.
- QE series is opinion + field anecdotes (fintech 160 incidents, pharma hand-collated evidence) — strong narrative, limited peer-reviewed data like Kiro's 1.5M convos or Autonoma's 4-metric RAG framework.

---

## Methodology

- **Discovery:** `sitemap.xml` → `post-sitemap.xml` 992 + `post-sitemap2.xml` 135 (lastmod 2026-08-31) + `feed/` (hourly); `/` index (6 latest posts) + deep fetch of Part 1 article (UTM alias) via webfetch (2026-09-03).
- **Relevance rubric:** HIGH = QE structural gaps/QE metrics/QE platform, AI agent API discovery & drift, context graphs, governance — directly actionable for QA/QE platform design; MEDIUM = useful API design/tutorial; LOW = company news/product spotlights.
- **Analogous to:** [Kiro catalog](kiro-blog-catalog-all-publications-2025-2026.md), [Autonoma catalog](autonoma-blog-catalog-all-publications-2026.md), [testRigor catalog](testrigor-blog-catalog-all-publications-2026.md), [TestMu AI catalog](testmuai-blog-catalog-all-publications-2026.md), [Zalando catalog](zalando-blog-catalog-all-publications-2026.md), [Martin Fowler catalog](martinfowler-blog-catalog-all-publications-2026.md), [Julia Pottinger catalog](juliapottinger-blog-catalog-all-publications-2026.md)

---

*Compiled: 2026-09-03 · Base page for https://blog.postman.com/ + detailed wiki for QE structural problem (your UTM link is alias of Part 1)*
