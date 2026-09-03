---
source: "milko-slavov-two-doors-mcp-2026.md"
ingested: "2026-09-01"
---

## Milko Slavov - AI SaaS Needs Two Doors (MCP vs Native Agent)

**Summary**
Milko Slavov (AI-native SDLC, 1d, PostHog example) argues: `I already pay for an agent. I don't want every SaaS selling me another one through credits.` User's agent already has model choices, context, workflows. When SaaS puts accessible models behind its own agent and credit wallet, user pays more to get less. PostHog showed better model: has native agent but also exposes PostHog through MCP. Team connected own agent, asked it to design dashboards, agent built them in PostHog keeping own models/workflow. Value came from `analytics data and actions`, not chat.

**Thesis:** AI SaaS needs two doors:
1. Native agent for ready-made experience
2. Scoped MCP or API for people who already have an agent

Moat isn't another chat box or credit wallet. It's data, workflows, permissions, reliable execution. `Build your agent. Just let mine use your product too.`

**Comments:** David Breunig (retavi) - same in industrial automation via MCP; Gabriel dos Santos - MCP valuable, one agent with context + preferred models beats maintaining workflow/credit per product.

---

## Our analysis (for Victor)

1. **Maps to QAEverest MCP + PostHog MCP.** QAEverest offers MCP server + JetBrains plugin putting generation/execution inside editor where code is - same two-doors. Forrester-style moat: not chat, but `Figma/Postman/Jira -> test suites + self-healing + Time-Travel + traceability` that agent can call.

2. **For Victor's pilot:** The value Victor verified (findings persistence, drift weakly-anchored, scorecard) is the `data, workflows, permissions, reliable execution` Slavov names - not the chat box. That is the attestation layer that makes MCP useful.

3. **For Appfire/HTEC QA leadership:** Build vs buy decision for AI QA - native agent for teams wanting ready-made, MCP for teams with existing Claude Code / Cursor. The two-doors model explains why acquisition-led growth (Appfire) needs both doors to keep 800+ remote teams on different stacks.

4. **Connects to Boris Cherny loop:** Cherny's 388 PRs via Slack channel is door 1 (native). Door 2 is exposing the same routines via MCP so user's own agent can trigger them without leaving its workflow - the scalability Slavov describes.

---

## Cross-links
- [Boris Cherny - Claude Maintains Apps](wiki/boris-cherny-claude-maintains-apps-2026.md) — native agent loop, 388 PRs
- [QAEverest Verification 7.1.1](../../Positions-CV-CL/company/pilots/DevQaExpert/index.md) — MCP + reliability layer as moat
- [Ilya Kabanov - Hygiene vs Hype](wiki/ilya-kabanov-cybersecurity-ai-cost-2026.md) — moat is boring reliable execution, not hype

---

*Source: Milko Slavov LinkedIn (1d) via PostHog MCP example · Ingested 2026-09-01*
