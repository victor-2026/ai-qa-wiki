---
source: "jeff-nyman-ai-testing-catalog-2026.md"
ingested: "2026-09-01"
---

## Jeff Nyman - AI and Testing (Category)

**Source:** https://testerstories.com/category/ai/ai-and-testing/ - 20+ posts Feb-May 2026, plus 2026-09-01 Testing Knowledge. All by Jeff Nyman. Focus: testing AI via DeepEval, RAG evaluation, DSPy, ontologies, local model pipelines.

---

## TOP 6 Most Useful for Victor

| Post | Date | Why useful |
|------|------|------------|
| **Evaluation Synthesis** | 2026-04-19 | Synthesis of 8 metrics across 2 paradigms (retrieval + generation) on 4 diverse docs (warp drive, mass extinction, colliders, time travel). Shows how full metric set reveals system-level weaknesses vs single metric. Direct template for holistic LLM eval. |
| **Evaluating Conversations** | 2026-04-12 | Moves from single-turn RAG metrics (Faithfulness etc.) to multi-turn conversational evaluation. Key for testing AI agents with memory - single-turn pass can be conversation fail. |
| **Faithfulness / Contextual Precision / Recall, Relevancy, G-Eval** | 2026-02-11 to 04-08 | DeepEval diagnostic kit: Faithfulness (is answer faithful to context?), Precision (is retrieved context precise?), Recall/Relevancy. How retrieval failures cascade to generation. Core for RAG pipeline eval - Victor's wiki already has RAG pipeline failure modes. |
| **Using Local Models for Testing / Using Model Pipelines** | 2026-02-26 / 03-02 | Local model looks at web app HTML, generates test cases + Playwright scripts, then pipeline of models with source of truth. Practical pattern for Claude Code + Playwright Agents - model generates, another evaluates, DeepEval sneaked in. |
| **Testing Knowledge Isn't (Just) a Testing Skill** | 2026-09-01 | Testability as cooperation: dev already carries tester discipline (sleep/rng seam), tester carries algorithm literacy (exact formula). Example is the seam design pattern for Fragility Index. |
| **DSPy and RAG: Grounding Answers in Documents** | 2026-05-03 | Applies DSPy pipelines to RAG grounding - wiring steps without writing prompts. Contrasts with raw prompting (Ishan's sensitivity trap). Useful for prompt durability discussion. |

**Read last:** The Last Useful Animal (philosophical, Thomist indictment of techno-oligarchy) - low QA utility.

---

## Full List (Feb-May 2026, page 1)

- 2026-05-03 DSPy and RAG: Grounding Answers in Documents
- 2026-04-19 AI and Testing: Evaluation Synthesis
- 2026-04-12 Evaluating Conversations
- 2026-04-08 Recall, Relevancy, and Richer Evaluation
- 2026-04-03 The Last Useful Animal
- 2026-03-30 Testing the "Yes-Man" in Your Pocket (psychological/behavioral impacts)
- 2026-03-25 From Specification to Story (ontology -> code -> LLM plays game)
- 2026-03-19 From Ontology to Implementation
- 2026-03-14 From Specification to Ontology
- 2026-03-10 Auditing a Knowledge Graph Pipeline
- 2026-03-07 A Knowledge Graph Pipeline in Practice
- 2026-03-05 Knowledge Graphs and Ontologies
- 2026-03-02 Using Model Pipelines for Testing
- 2026-02-26 Using Local Models for Testing
- 2026-02-23 Improving Retrieval Quality Part 4
- 2026-02-19 Part 3
- 2026-02-17 Part 2
- 2026-02-16 Part 1
- 2026-02-13 Contextual Precision
- 2026-02-11 Faithfulness
- + older page 2 (not fetched)

---

## How to use

- **For RAG eval:** Start with Faithfulness -> Precision -> Recall/Relevancy -> Synthesis. This is the DeepEval path Victor can mirror with mutation matrix (retrieval vs generation failures).
- **For agent testing:** Evaluating Conversations + Using Model Pipelines (multi-turn, pipeline of models, source of truth).
- **For testability:** Testing Knowledge post (sleep/rng seam) -> link to QAEverest Fragility (position-based selectors) and Victor's confirm/dismiss gate.

---

## Cross-links
- [Jeff Nyman - Testing Knowledge](wiki/jeff-nyman-testing-knowledge-not-just-testing-skill-2026.md)
- [Ishan Anand - Persona Failure Modes](wiki/ishan-anand-llm-persona-feedback-failure-modes-2026.md) — prompt sensitivity vs DeepEval
- [AI QA Evidence Layer](wiki/ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md)

---

*Source: https://testerstories.com/category/ai/ai-and-testing/ and page 2 · Ingested 2026-09-01*
