# Forms of LLM-Integrated Applications (Weber 2026, FLLM)

**Source:** Irene Weber (HS Kempten), "Forms of LLM-Integrated Applications from LLM-Chats to Autonomous AI Agent Systems", accepted FLLM2026 Barcelona. Raw: `raw/2610.11899v1.pdf` (8pp). Survey of 22 systems (vendor docs + own inspection + research). Single-author characterization, illustrative corpus (no frequency claims).

## Thesis: labels carry architecture

Vendor labels (chatbot, copilot, RAG, agent) are not pure branding — they denote structural forms. The copilot→agent shift marks a real move: from AI-selected single steps the user confirms to AI-planned multi-step execution of which the user sees only the outcome. Coding agents of four major providers share one architecture (reason-and-act loop delegating to subagents).

## Seven forms × four dimensions

Each form: architectural pattern + point of user intervention + agent calls per task + tool use.

| Form | Architecture | User control | Calls/task | Tools |
|---|---|---|---|---|
| LLM chats | multifunctional single agent | each answer | one–few | optional |
| Custom agents | monofunctional single agent | each answer | one | ≤1 |
| RAG narrow | monofunctional single agent (LLM only formulates answer from handed material — technically not tool use) | each answer | one | none |
| Agentic RAG | varies (single loop → hierarchical) | each answer | ? | retrieval tools |
| AI-enhanced workflows | workflow (RPA/BPMN blocks + agent steps) | optional checkpoints (critical/low-confidence) | fixed | fixed |
| Copilots | router-worker (intent detect → specialized workers operate host app) | each action result (keep/refine/undo) | two | host functions |
| Coding agents | ReAct loop → subagents | final result only | open, unbounded | extensive |

Plus: planner-executor example (Anthropic Research: lead plans, parallel subagents, interleaved planning/execution).

## Copilot anatomy (the paper's deepest case)

Router-worker at interaction level: user states goal → intent detection → monofunctional workers operate host-application functions → visible effect the user keeps or refines. Workers may themselves be orchestrator-workers internally (nesting rule: classify at the user-facing level, record nesting as worker property). GitHub-style: slash commands bypass intent detection; "copilot not autopilot" — generated code not compiled/executed before review.

## Limits (author-stated)

Single author, vendor sources disclose partial detail, corpus illustrative not representative, field moved during writing (copilots became agents). New forms emerging (local personal assistants reading/writing files). No mutual-exclusivity claim — nested hybrids are the norm.

## QA interpretation

- **Test strategy follows the form:** copilot = per-action assertion surface (each visible step checkable); coding agent = final-result-only (outcome evidence, not step inspection); workflow = checkpoint coverage (critical/low-confidence gates).
- **The label shift is a test-scope shift:** confirming single steps (copilot) vs validating planned multi-step outcomes (agent) — different oracles, different evidence packs.
- **Narrow RAG is not agentic:** no retrieval decisions by the LLM — eval it as answer-formulation, not as retrieval.
- Vendor-consistency finding (copilot used uniformly) supports treating vendor architecture docs as spec-grade input.

## See also

- [[anthropic-claude-code-expertise-2026]] — planning-execution division
- [[kiro-blog-catalog-all-publications-2025-2026]] — eval-driven development
- per-risk-tier framework (Positions-CV-CL vault) — gate strictness by risk tier
