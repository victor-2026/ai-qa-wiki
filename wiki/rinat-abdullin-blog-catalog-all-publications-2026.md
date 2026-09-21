# Rinat Abdullin Blog: Complete Publications Catalog

**Source:** https://abdullin.com (with full-site index at `/search-index.jsonl`, search at `/_api/search?q=terms`)
**Author:** Rinat Abdullin — technical advisor ("help ship LLM-driven products faster"), works from Vienna 🇦🇹. Known for [LLM Product Benchmarks](https://abdullin.com/llm-benchmarks), [Schema-Guided Reasoning](https://abdullin.com/schema-guided-reasoning/), [Enterprise RAG Challenge](https://abdullin.com/erc/). Founder of [BitGN](https://bitgn.com) — platform for agent benchmarks & challenges. Head of ML and Innovation at TIMETOACT GROUP Austria. Newsletter: "ML Under the Hood". Blog language: mostly EN, some RU (archived course pages).
**Total articles:** 15 AIQA-relevant posts (5 AI Coding + 2 ERC + 6 SGR + 2 Evals) + 6 LLM-product guides + 1 course landing
**Last updated:** 2026-09-21

---

## Legend

- **Relevance:** HIGH / MEDIUM / LOW (for QA/QE automation engineer + agent/LLM testing focus)
- **Action:** FULL READ / SKIM / SKIP

---

## Connecting threads (why this catalog)

- **Agentiqa link:** Rinat Abdullin is associated/author figure of Agentiqa (agentic QA). Cross-reference: Positions-CV-CL vault → `company/pilots/Agentiqa/index.md` (verified in pilot runs, contact Radik Zagirov CEO). His "credit the verifier" / benchmark-methodology thesis is the conceptual backbone of the Agentiqa gap analysis.
- **`boring-code` = master thesis:** "We never wanted human code" — humans always wanted boring code, AI just writes more of it. Directly supports Victor's "suite green ≠ correctness": the 200K-line pipeline was validated by a test suite that took ~70% of human effort — verification was the bottleneck, not generation.
- **SGR = structured-output testing angle:** constrained decoding (Pydantic/JSON Schema) as a *controllability* mechanism — relevant to "arbitrary-agent-output" testing (llm-testing skill: contract-based checks).
- **Existing wiki file:** [Rinat Abdullin SDD vs BDD AI-Native Harness](../wiki/rinat-abdullin-bdd-vs-sdd-ai-native-harness.md) — "BDD as AI-Native harness" = executable requirements. Recruit from catalog below.

---

## TOP 10 Must-Read Articles (Tier 1)

### AI Coding Agents (5 articles total)

| # | Title | URL | Date | Relevance | Саммари |
|---|-------|-----|------|-----------|---------|
| 1 | [We never wanted human code](https://abdullin.com/ai-coding/boring-code/) | 2026 | **HIGH** | 200K lines boring AI code, 99.6% accuracy, ~2¢/component, ~70% human effort went into test suite → verification defines correctness. Master thesis for AI-QA. [→ wiki](rinat-boring-code-2026.md) |
| 2 | [AI+Coding Kata (2025)](https://abdullin.com/ai-coding/kata-1/) | 2025-04-06 | **HIGH** | Self-contained "BizDocumentAI" spec = its own test suite; parser kata for any tool/lang; tests-as-spec thinking. [→ wiki](rinat-ai-coding-kata-2026.md) |
| 3 | [AI Coding (series hub)](https://abdullin.com/ai-coding/) | 2026 | MEDIUM | "Building maintainable software with agents" — how to make intent clear, verify behavior (current thinking). |
| 4 | [ChatGPT quickstart for developers (2023)](https://abdullin.com/ai-coding/chatgpt-quickstart/) | 2023 | LOW | Beginner prompt-engineering primer (few-shot = function definition). |
| 5 | [How to get into ML for a developer? (2023)](https://abdullin.com/ai-coding/how-to-get-into-ml/) | 2023 | LOW | Legacy roadmap, not testing-relevant. |

### Enterprise RAG Challenge (2 articles total)

| # | Title | URL | Date | Relevance | Саммари |
|---|-------|-----|------|-----------|---------|
| 6 | [Enterprise RAG Challenge](https://abdullin.com/erc/) | 2025-03-13 | **HIGH** | 43-team RAG benchmark (annual reports QA): winners detail phase — eval-first experimentation framework, router+reranking+SO CoT, self-consistency. Real-world evals-by-competition. [→ wiki](rinat-erc-2026.md) |
| 7 | [Ilya Rice: How I Won the Enterprise RAG Challenge](https://abdullin.com/ilya/how-to-build-best-rag/) | 2025 | **HIGH** | Winning deep-dive: dense+router+LLM rerank+SO, majority vote; "what didn't work" log = honest eval loop. [→ wiki](rinat-ERC-winner-deep-dive-2026.md) |

### Schema-Guided Reasoning (6 articles total)

| # | Title | URL | Date | Relevance | Саммари |
|---|-------|-----|------|-----------|---------|
| 8 | [Schema-Guided Reasoning (SGR)](https://abdullin.com/schema-guided-reasoning/) | 2025-07 | **HIGH** | Technique hub: enforce reasoning steps via Pydantic schemas + constrained decoding. Accuracy boost 5-10%; makes weak local models usable. Auditability = testability. [→ wiki](rinat-sgr-2026.md) |
| 9 | [SGR Adaptive Planning](https://abdullin.com/schema-guided-reasoning/adaptive-planning) | 2025 | **HIGH** | Fresh-plan-per-step agent: `plan_remaining_steps_brief` planned then discarded; adapts to new facts at runtime. Deterministic envelope around agent behavior. [→ wiki](rinat-sgr-adaptive-planning-2026.md) |
| 10 | [SGR Patterns](https://abdullin.com/schema-guided-reasoning/patterns) | 2025 | MEDIUM | Cascade, Routing, Cycle — reusable schema topologies. |
| 11 | [SGR Examples](https://abdullin.com/schema-guided-reasoning/examples) | 2025 | MEDIUM | math, text-to-sql, doc classification, compliance analysis. |
| 12 | [SGR Demo (Business Assistant)](https://abdullin.com/schema-guided-reasoning/demo) | 2025 | MEDIUM | 160-line reasoning business assistant with tool use + self-memories. |
| 13 | [Structured Output](https://abdullin.com/structured-output/) | 2025 | MEDIUM | Constrained decoding (grammar/JSON Schema) — SGR foundation. |

### LLM Evals & Benchmarks (2 topics)

| # | Title | URL | Date | Relevance | Саммари |
|---|-------|-----|------|-----------|---------|
| 14 | [Evaluating LLM in business workloads](https://abdullin.com/llm-benchmarks) | Aug 2023 – Summer 2025 | **HIGH** | Flagship evals page: business-workload benchmark, FAQ, full monthly report index, SGR-powered benchmark v2. Cross-link to `testing-agents.md` / `llm-testing`. [→ wiki](rinat-llm-benchmarks-2026.md) |
| 15 | ML Under the Hood (newsletter) | ongoing | LOW | Announcements/essays hub (stub page; real content via newsletter). |

### LLM-product FAQ (guides — mostly SKIP for QA angle, keep as reference)

| # | Title | URL | Relevance |
|---|-------|-----|-----------|
| 16 | [Shipping products with LLMs and ChatGPT (FAQ hub)](https://abdullin.com/llm/) | MEDIUM |
| 17 | [My team has no experience with ML/GPT. How do we proceed?](https://abdullin.com/llm/engineering-team-advice/) | LOW |
| 18 | [ChatGPT is unpredictable in text analysis. Can this be fixed?](https://abdullin.com/llm/faq-chat-gpt-text-analysis-prompts/) | LOW |
| 19 | [How to segment texts for embeddings?](https://abdullin.com/llm/how-to-segment-text-for-embeddings/) | MEDIUM |
| 20 | [How to talk to your knowledge base?](https://abdullin.com/llm/talk-to-your-knowledge-base/) | MEDIUM |
| 21 | [Building Reliable AI Assistants course (Apr 2026, EN)](https://abdullin.com/building-ai-assistants-course) | MEDIUM |
| 22 | [SDD vs BDD AI-Native Harness (Telegram)](https://abdullin.com) — existing wiki | HIGH | [rinat-abdullin-bdd-vs-sdd-ai-native-harness.md](rinat-abdullin-bdd-vs-sdd-ai-native-harness.md) |

---

## Category Breakdown

| Category | Count | TOP picks |
|----------|-------|-----------|
| AI Coding agents (`/ai-coding/`) | 5 | boring-code, kata-1 |
| Enterprise RAG Challenge (`/erc/`) | 2 | ERC hub, Ilya Rice deep-dive |
| Schema-Guided Reasoning (`/schema-guided-reasoning/`, `/structured-output/`) | 6 | SGR hub, Adaptive Planning |
| LLM Evals / benchmarks (`/llm-benchmarks`) | 2 | Evaluating LLM in business workloads |
| LLM-product guides (`/llm/`) | 5 | — (reference) |
| Course (EN, 2026) | 1 | Building Reliable AI Assistants |
| **AIQA-relevant total** | **15 + 1 (SDD/BDD)** | **8 HIGH** |

## Structure notes (for crawler reuse)

- Full-text index: `https://abdullin.com/search-index.jsonl` (JSONL, 315 lines, `url` + `title` + `text`).
- Search: `https://abdullin.com/_api/search?q=terms`.
- Nav sections: ERC · SGR · LLM Evals · News · Courses. Blog sections: AI Coding, SGR, Shipping products with LLMs, Event Sourcing (legacy), Opinionated Tech, Simulation, Robotics, SkuVault, HappyPancake, Being the Worst (podcast).
- Legacy/non-LLM (skip for QA): simulation, robotics, event sourcing/CQRS, SkuVault, HappyPancake, `/post/*` pre-2016.
- LLM-evals nav item does NOT map to `/llm-evals/` (404) — real page is `/llm-benchmarks`.
- SGR-based benchmark v2 exists on `/llm-benchmarks` (references external interactive reports on TimeToAct/Trustbit).

---

*Generated by curator (2026-09-21) from full-site index. Author association with Agentiqa per Victor; official Agentiqa contact is Radik Zagirov (CEO), see Agentiqa pilot catalog.*