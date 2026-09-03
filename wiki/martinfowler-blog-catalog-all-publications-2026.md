# Martin Fowler — Complete Publications Catalog

**Source:** https://martinfowler.com (feed.atom)
**Total articles:** ~600+ (Content Index /tags: 50+ tags; feed shows 100 latest; testing guide alone 40+ entries; exploring-gen-ai series 10+ in 2026)
**Last updated:** 2026-09-02
**Feed:** https://martinfowler.com/feed.atom
**Focus for QA/QE:** Architecture, Refactoring, Agile, Data, Testing, Delivery, Microservices, DSL, GenAI

---

## Legend

- **Relevance:** HIGH / MEDIUM / LOW (for QA/QE automation engineer, AI-augmented testing focus)
- **Category:** Core Tech | Testing | Data | Architecture | AI/GenAI
- **Action:** FULL READ / SKIM / SKIP

---

## TOP 15 Must-Read for AI-QA (2026 Highlights + Classics)

### AI & Agentic Engineering (HIGH)

| # | Title | URL | Date | Relevance |
|---|-------|-----|------|-----------|
| 1 | [Making Your Data Ready for Agentic AI](https://martinfowler.com/articles/making-data-ready-for-agentic-ai.html) | 2026-08-27 | **HIGH** |
| 2 | [An Accidental Blackboard](https://martinfowler.com/articles/exploring-gen-ai/an-accidental-blackboard.html) | 2026-09-02 | **HIGH** |
| 3 | [Maybe We Shouldn't Be Reviewing All This Code](https://martinfowler.com/rachels-ramblings/code-review.html) — Rachel Laycock | 2026-09-02 | **HIGH** |
| 4 | [TDD inside the agent loop - theater or actual value?](https://martinfowler.com/articles/exploring-gen-ai/tdd-in-the-agent-loop.html) — Birgitta Böckeler | 2026-08 | **HIGH** |
| 5 | [Building Reliable Agentic AI Systems](https://martinfowler.com/articles/exploring-gen-ai/building-reliable-agentic-ai-systems.html) | 2026 | **HIGH** |
| 6 | [Citizens Build, Agents Execute, Experts Govern](https://martinfowler.com/articles/citizens-build-agents-execute.html) | 2026-08 | **HIGH** |
| 7 | [The Conductor Developer](https://martinfowler.com/articles/the-conductor-developer.html) | 2026-08 | MEDIUM |
| 8 | [DSLs Enable Reliable Use of LLMs](https://martinfowler.com/articles/dsls-enable-llms.html) | 2026-07 | **HIGH** |

### Testing & Quality Foundations (HIGH — Classics Still Relevant)

| # | Title | URL | Date | Relevance |
|---|-------|-----|------|-----------|
| 9 | [The test suite as a regression sensor](https://martinfowler.com/articles/sensors-for-coding-agents.html#TheTestSuiteAsARegressionSensor) | 2026 | **HIGH** |
| 10 | [Test Pyramid](https://martinfowler.com/bliki/TestPyramid.html) | 2012-05-01 | **HIGH** |
| 11 | [The Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html) — Ham Vocke | 2018-02-26 | **HIGH** |
| 12 | [On the Diverse And Fantastical Shapes of Testing](https://martinfowler.com/articles/2021-test-shapes.html) | 2021-06-02 | **HIGH** |
| 13 | [Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html) | 2007-01-02 | **HIGH** |
| 14 | [Self Testing Code](https://martinfowler.com/bliki/SelfTestingCode.html) | 2014-05-01 | **HIGH** |
| 15 | [Eradicating Non-Determinism in Tests](https://martinfowler.com/articles/nonDeterminism.html) | 2011-04-14 | **HIGH** |

*Full exploring-gen-ai series at https://martinfowler.com/articles/exploring-gen-ai.html (10+ articles in 2026).*

---

## Category Breakdown (Sampled)

| Category / Tag | Example URL | Est. Count | HIGH | Action |
|----------------|-------------|------------|------|--------|
| Testing Guide (/testing) — SelfTestingCode, Pyramid, etc. | /bliki/TestPyramid.html | ~45 | ~20 | FULL READ |
| Architecture / Data / Delivery / Microservices | /architecture | ~200 | ~10 | SKIM |
| Exploring Gen AI series | /articles/exploring-gen-ai/ | ~12 | ~8 | FULL READ |
| Refactoring (refactoring.com) | /books/refactoring.html | ~50 | ~5 | SKIM |
| Bliki (Paracelsus Maxim etc.) | /bliki/ParacelsusMaxim.html | ~150 | ~2 | SKIM |
| Fragments (weekly notes) | /tags (fragments) | ~100 | — | SKIP |
| **TOTAL** | martinfowler.com | **~600+** | **~45** |  |

*Counts estimated from feed (100 latest) + content index /tags (50+ tags) and testing guide structure; HIGH = directly actionable for AI-QA harness design.*

---

## Summary Statistics

| Tier | Count (est.) | % | Action |
|------|--------------|---|--------|
| HIGH relevance (read first) | ~45 | ~7% | FULL READ |
| MEDIUM relevance (skim) | ~100 | ~16% | SKIM |
| LOW relevance (skip) | ~455 | ~76% | SKIP |

---

## Key Strengths & Gaps (for QA/QE)

**Strengths:**
- Authoritative on test design (Pyramid, Practical Pyramid, mocks, self-testing code) — directly counters AI-generated test theater.
- GenAI series provides empirically grounded agentic practices (data contracts, TDD theater, conductor/orchestrator, DSLs for LLMs, regression sensor via mutation).
- Thoughtworks pedigree — data governance, traceability, and delivery lens beyond tool hype.

**Gaps / Watch-outs:**
- Not a QA blog per se — AI-QA specifics (LLM evals, prompt injection, MCP) scattered vs Autonoma's dedicated testing focus.
- Many entries are bliki/fragments — signal/noise ~7% HIGH; use curated TOP list above.

---

## Methodology

- **Discovery:** `feed.atom` (100 latest, updated 2026-09-02) + `/testing` guide + `/articles/exploring-gen-ai/` + direct fetches (making-data-ready 2026-08-27, tdd-in-agent-loop, accidental-blackboard, rachels-ramblings).
- **Relevance rubric:** HIGH = agentic AI data readiness, test design, regression sensing, TDD theater, review process — directly maps to mutation/MCP/evals and verification layer; MEDIUM = useful context; LOW = culture/bliki.
- **Analogous to:** [Kiro catalog](kiro-blog-catalog-all-publications-2025-2026.md), [Autonoma catalog](autonoma-blog-catalog-all-publications-2026.md), [testRigor catalog](testrigor-blog-catalog-all-publications-2026.md), [Zalando catalog](zalando-blog-catalog-all-publications-2026.md) (Zalando snapshot).

---

*Compiled: 2026-09-02 · Base page for https://martinfowler.com + detailed wiki for making-data-ready (90-120 lines)*
