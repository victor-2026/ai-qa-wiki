# DevQAExpert Blog: Evaluation

**Source:** https://devqaexpert.com/blog/
**Checked:** 2026-09-03
**Sitemap:** https://devqaexpert.com/sitemap.xml → sitemap-blog.xml (not paginated like testmuai; blog pagination: 14 pages × 4 posts = ~50-56 articles, 2015-2026)
**Total articles:** ~50-56 (vs TestMu AI ~2,380, testRigor ~3,013, Autonoma 581, Zalando ~430, Kiro 92, Martin Fowler ~600)
**Last sampled:** 2026-09-03 (p1 fetch + deep fetch of 90× article)

---

## Sampled Content (p1, 4 visible)

| # | Title | URL | Date | Note |
|---|-------|-----|------|------|
| 1 | [How QAeverest.ai Turned My Automation Pipeline Into a 90× Speed Machine](https://devqaexpert.com/2025/07/15/how-qaeverest-ai-turned-my-automation-pipeline-into-a-90x-speed-machine/) | 2025-07-15 | Product anecdote: Jira 200 words + 2 Figma PNG → 47 functional +12 API +8 security +5 perf in <3 min, 8h→25min/story, 3w→1w release, 22→5 prod defects |
| 2 | [QAEverest.ai, A True Friend to Software Testers](https://devqaexpert.com/2025/07/03/qaeverest-ai-a-true-friend-to-software-testers/) | 2025-07-03 | Overview platform (functional/API/perf/security in one run) |
| 3 | [Why AI + API Testing is the Future](https://devqaexpert.com/2025/07/02/why-ai-api-testing-is-the-future/) | 2025-07-02 | Generic AI+API hype, no harness/code |
| 4 | [From Manual to Magical: How AI Transformed Testing Journey](https://devqaexpert.com/2025/01/30/from-manual-to-magical-how-ai-transformed-testing-journey/) | 2025-01-30 | Personal journey, no metrics |

Deep fetch #1 detail:
- **Before/With table:** test design 90× faster (manual Gherkin → AI from stories/mock-ups), edge coverage 88% auto, maintenance 30%→~0 broken via self-healing, security/perf shift-left (OWASP+load same run)
- **6 weeks numbers:** 8h→25min/story, release 3w→1w, prod defects 22→5 (critical caught by AI security tests), cost/story ~40% lower
- **Features:** multi-format ingestion (whiteboard image→cases), one-click Jira sync, risk-based prioritization (5% tests most likely to fail)
- **Gaps:** no dependency graph, no recall on skipped tests, no mutation score, no MCP detail, no peer-reviewed eval — anecdotal speed, not methodology like TestMu AI Facebook 99.9% or Kiro 15 dims.

---

## Assessment for AI QA Wiki

**Relevance:** LOW for wiki ingestion.

- **Signal/noise:** ~5% HIGH (2-3 posts with limited depth) — lower than Autonoma ~6% HIGH (38/581 with code/harness), Kiro ~24% HIGH (22/92), testRigor ~5% (165/3013) but with broader coverage, Martin Fowler ~7% (45/600) authoritative, Zalando (~430) high density for governance.
- **Depth:** No architecture like TestMu AI's 4-level ladder + recall metric, no Kiro's 406K diagnostics/15-dim judge, no Autonoma's RAG/mutation depth. Content is product marketing for QAEverest (sales funnel), not engineering blog.
- **Value vs direct pilot:** Pilot with Rupesh (M2-M9 mutations, Trust Scorecard 78% sensitivity, floor suite, nightly recall) gives **private, verifiable signal** far beyond blog anecdotes. Blog adds no new verifiable method.

**Strengths (if cataloging):**
- Shows vendor's positioning: 90× speed, Jira+Figma ingestion, risk-based 5%, Zephyr export — useful as vendor claims to cross-check against live pilot findings (text-based search, label-rename fragility).
- Indicates where blog would be HIGH if deeper: codeless ingestion + risk-based prioritization map to QA control layer.

**Gaps / Watch-outs:**
- Anecdotal 90× without dependency graph or escaped-fault measurement — risk of "faster but not verified."
- 50-post scale too small for comprehensive catalog like Kiro/Autonoma; SEO duplication risk if treated as independent source.

---

## Decision

**Do NOT build full catalog** analogous to Kiro/Autonoma/testRigor (not worth 125-line page + 50 raw fetches + 5-10 wiki pages). Keep this **evaluation page as lightweight catalog** (this file) — records sampling, scale, and why not ingested further.

If later vendor publishes technical deep dives (graph-based selection, recall measurement, mutation harness), re-evaluate and ingest as individual wiki pages (e.g., risk-based prioritization deep dive).

---

*Compiled: 2026-09-03 · Analogous to [Kiro catalog](kiro-blog-catalog-all-publications-2025-2026.md), [Autonoma catalog](autonoma-blog-catalog-all-publications-2026.md), [testRigor catalog](testrigor-blog-catalog-all-publications-2026.md), [Zalando catalog](zalando-blog-catalog-all-publications-2026.md), [Martin Fowler catalog](martinfowler-blog-catalog-all-publications-2026.md) — but evaluation only, not full ingestion.*
