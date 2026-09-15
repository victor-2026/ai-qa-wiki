# From AI Agent Demo to Production

> InfoQ (Jul 2026). Authors: Bernardo Aceituno, Maxime Lagrange, Adil Zinebi. URL: https://www.infoq.com/articles/ai-agent-demo-production/

Conference talk and article covering the gap between AI agent demos (RAG chatbots, LLM demos, agentic coding assistants) and production-ready systems.

## The Demo-to-Production Gap
Demos are typically:
- Tightly scoped to happy path
- No error handling
- No observability
- No security audit
- No cost control
- No human-in-the-loop fallback

## Production Requirements
- **Observability**: trace LLM calls, tool invocations, cost per request
- **Guardrails**: content filtering, output validation, rate limiting
- **Fallback**: graceful degradation when LLM fails or hallucinates
- **Cost control**: token budgets, caching, model tiering
- **Security**: prompt injection defense, PII handling
- **Human-in-the-loop**: escalation paths for ambiguous or high-risk decisions

## Patterns
- **Demo**: "Look, it works!"
- **Production**: "It works, AND here's what happens when it doesn't."

## Key Insight for QA
The gap between demo and production is where QA lives. A tester's job is to find the scenarios the demo didn't cover — the edge cases, the failure modes, the cost blowouts.

## Source
- URL: https://www.infoq.com/articles/ai-agent-demo-production/
- Tags: #ai-agents, #production-readiness, #demo-to-prod, #guardrails, #observability, #infoq-2026
- See also: [[known_patterns|Pattern: human_review_loop]], [[llm-testing]], [[Test-Reliability]]
