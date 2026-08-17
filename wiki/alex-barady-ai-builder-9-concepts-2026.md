# Alex Barády: 9 Concepts That Separate AI User from AI Builder

**Source:** Alex Barády (ENDGAME Founder) — LinkedIn post, Jul 6, 2026
**Raw:** `raw/alex-barady-9-concepts-ai-builder-2026.md`

## Framework

| # | Concept | Definition | Maturity Level |
|---|---------|------------|----------------|
| 1 | **Agentic Loops** | AI plans → acts → observes → reflects; loops until done | Builder |
| 2 | **MCP** | One interface connecting AI to tools (email, repos, DB, browser) | Builder |
| 3 | **Subagents** | Decompose → parallel execution → merge | Builder |
| 4 | **AI Gateway** | Single control plane: auth, routing, rate limits, logs | Infrastructure |
| 5 | **Inference Economics** | Token cost awareness, caching, model selection | Infrastructure |
| 6 | **Evals** | Measure before ship — benchmarks, golden datasets | Quality |
| 7 | **Guardrails** | Filter input/output — safety, brand protection | Quality |
| 8 | **Observability** | Traces, logs, metrics for production AI | Operations |
| 9 | **Context Engineering** | Feed right context from retrieval, memory, tools, history | Core Skill |

## Thesis

> "People spend months perfecting prompts and ignore the infrastructure, evaluation, and systems that power real AI products."

The biggest mistake: focusing on prompt engineering while skipping evals, guardrails, observability, and context infrastructure.

## Mapping to Existing Work

| Concept | Equivalent in Stack |
|---------|-------------------|
| Subagents | Playwright Agents (Planner → Generator → Healer), MAS pipeline |
| Context Engineering | `context-engineering` skill, `~/.opencode-memory.md`, session checkpoints |
| Agentic Loops | Autonoma pipeline, fault-injection cycles |
| Evals | `llm-testing` skill, offline-evaluation-trajectories, 4-axis self-evaluation |
| Observability | Allure TestOps, DORA metrics, Allure dashboards |
| Guardrails | Mutation testing, fault injection, boundary testing |
| MCP | Maestro MCP server, OpenCode MCP tools |
| Inference Economics | Model selection (Groq vs OpenRouter vs local), token budget management |
| AI Gateway | OpenRouter, model routing strategy documented in Articles |

### QA-Specific Interpretation

The mappings above are QA translations, not replacements for the original concepts. In particular, mutation testing is a downstream anti-overfit guardrail, not a complete AI safety guardrail; Allure and DORA provide test-run evidence and delivery metrics, not model/tool telemetry; and contract or E2E results are downstream QA validation, not general model eval scores. See [AI QA Evidence Layer: Validation, Evals, Guardrails, and Telemetry](ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md).

## Use Case

This framework can be used for:
1. **AI Engineering Maturity Model article** — map each concept to maturity levels (L1–L5)
2. **Self-assessment checklist** — which concepts are covered, which are gaps
3. **Job interview framing** — "I operate at builder level across all 9 concepts"
4. **Tool evaluation** — rate tools (Autonoma, Mabl, TestSigma) against this framework











<!-- backlinks-start -->
### Backlinks
- [Alex Barady 9 Concepts Ai Builder 2026](wiki/alex-barady-9-concepts-ai-builder-2026.md)
<!-- backlinks-end -->
