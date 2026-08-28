# MCP + UCP: Two Protocols for Agentic QA (2026)

## Summary

Two complementary open protocols define how AI agents interact in 2026:
- **MCP (Model Context Protocol)** — model ↔ tools/data (Anthropic, Nov 2024, industry standard by 2025)
- **UCP (Universal Chat Protocol)** — agent ↔ agent across vendors (Microsoft, announced Sep 2025, open-standard proposal)

For QA: MCP is how an agent drives a browser/framework; UCP is how teams of agents from different vendors coordinate.

## MCP — Model Context Protocol

- **What:** Open protocol (Anthropic, Nov 2024) connecting LLMs to tools and data sources.
- **Architecture:**
  - MCP **server** — exposes tools/resources (browser, files, APIs, DBs)
  - MCP **client** — the app/agent calling them (Claude Code, Playwright MCP, etc.)
- **Adoption:** accepted by OpenAI, Google, Microsoft during 2025 — de-facto industry standard for agent tool access.
- **QA use cases:**
  - Playwright MCP — agent controls the browser directly (navigation, clicks, assertions)
  - Claude Code + MCP servers in CI/CD — agent runs test-bench checks on demand
  - Local QA: MCP server wrapping test frameworks, Allure, DBs → agent calls them like tools

## UCP — Universal Chat Protocol

- **What:** Microsoft's protocol (announced Sep 2025) for agent-to-agent communication **between different vendors** — Copilot ↔ ChatGPT ↔ Claude agents talking directly.
- **Relationship to MCP:** UCP is the layer above MCP:
  - MCP answers "how does an agent use tools"
  - UCP answers "how do agents talk to each other"
- **Status:** proposed by Microsoft as an open standard; adoption still maturing.

## MCP + UCP for Agentic QA

| Layer | Protocol | QA example |
|-------|----------|------------|
| Model ↔ tools | MCP | Playwright MCP: agent opens browser, clicks, asserts |
| Agent ↔ agent | UCP | Orchestrating Planner / Generator / Healer agents from different vendors |

- Today: "agent + MCP tools" is the standard stack (Playwright Agents, Claude Code, DevAssure O2 use MCP-class tool access).
- Tomorrow: "agent teams over UCP" — cross-vendor interoperability; e.g., a vendor-neutral QA agent calling vendor-specific tool agents.
- Implication for QA teams evaluating agent tools: MCP support is now a checkbox; UCP support will become the interop checkbox as teams run multi-agent pipelines.

## Sources

- Anthropic MCP announcement: modelcontextprotocol.io
- Microsoft UCP announcement: Sep 2025, Microsoft blog (agent interop initiative)
- Related wiki: claude-code-ci-cd-mcp-2026.md, fullstack-verification-mcp-habr.md

*Ingested: 2026-08-17*
