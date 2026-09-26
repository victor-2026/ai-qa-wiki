# Graphify: Codebase → Queryable Knowledge Graph for Agents (InfoQ, 2026-09-23)

**Author:** Olimpiu Pop (InfoQ). Project: github.com/Graphify-Labs/graphify (OSS, MIT+Apache-2.0, since Apr 2026, weekly releases, thousands of stars in 10 days).
**Source:** https://www.infoq.com/news/2026/09/graphify-codebase-exploration/ (fetched 2026-09-25).
**Context:** Codebase context infrastructure for agentic coding: AST (tree-sitter) + docs + images → multimodal KG with community detection → queryable directly or via MCP. First-party benchmarks: LOCOMO recall@10 0.497, QA 45.3%, LongMemEval-S 76%, ERPNext key-fact 70.8%→82.0%. Community: strong concept, early-tool friction (brute-force/grep still faster on mid-size repos). Install: uv, macOS/Windows/Ubuntu.
**Captured:** 2026-09-25 from webfetch.

---

## Use for us

- Context-plane precedent: KG over repo (code + Markdown/PDF + images) queried by agents via MCP = the "define once, retrieve facts" economy (Seale rhyme: stop reconstructing business per call).
- Benchmark scaffold: LOCOMO recall@10 + QA accuracy + key-fact coverage as context-quality metrics (pairs with RAG eval pages; token-reduction claims need independent check).
- Maturity honesty (vendor-adjacent InfoQ piece admits grep-wins-mid-size) = quotable against hype.
- Cross-links: Qodo Software Map (risk map vs context map - complementary planes), VerdictGate context (what the judge must be handed), CIGE context-field design.
- Follow-up: version 2 with deeper parser intelligence; community verdict pending.
