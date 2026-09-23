# InfoQ Podcast — Securing AI Agents: Identity, Authorization, and the DPACT Framework (2026-09-21)

**Guest:** Sahil Agarwal (area engineering leader, identity and authorization stack, cloud collaboration/content platform)
**Host:** Olimpiu Pop (InfoQ editor)
**Source:** https://www.infoq.com/podcasts/securing-ai-agents-identity-authorization/
**Context:** InfoQ podcast introducing DPACT framework (Delegation, Policy, Auditability, Context, Time) for governing AI agents. Full transcript on page. Date 2026-09-21.

---
## Key Takeaways (InfoQ box)
- AI agents are shifting from passive chat interfaces to unauthorized "delegated actors" requiring robust security models beyond traditional human authentication.
- DPACT (Delegation, Policy, Auditability, Context, Time) = blueprint for agents operating within defined, secure boundaries.
- Agents should act "on behalf of" a user rather than impersonating them (prevents unauthorized access, privilege escalation).
- Incremental governance (start with inventory, add visibility) is the most effective way to secure production agentic systems without stifling innovation.
- Future agentic infrastructure must treat bounded task grants as a first-class feature, moving away from long-lived API keys.

## Core ideas from transcript
**Shift:** from "can you write a good line of code" to "can you be the software orchestrator whose agents build it". Teams race to capability and forget identity, accountability and trust are the risky bits. Agents moved into operations and started gaining real world effects without corresponding identity and authorization.

**Acting on behalf of vs impersonating:** agents should always act on behalf of a human user, never impersonate the user. E.g., an army of agents works as a delegated autonomous actor, never "as Sahil". OpenClaw's first rendition is a case study in why delegation matters.

**Pre-AI era:** humans → apps → resources; humans always in the loop, permissions controlled, intent known. That theory breaks with autonomous delegated actors that chain tools, draw on info, make decisions.

**DPACT:**
- Delegation — clearly say on whose behalf the agent acts.
- Policy — the restriction; what it can do and most importantly what it absolutely cannot do.
- Auditability/explainability — today, 30 days later, be able to say why an agent took an action; audit logs feed a feedback loop (retrain the agent).
- Context — boundary drawn for the agent; draft an email but don't send it.
- Time — when does authority end; TTLs, task-based grants, explicit mechanisms to end authority.

It's a blueprint / positional framework (concept, no tool yet), not implementation-specific.

**Product mapping (customer service example):** autonomy tiers (proposed only / read-only / reversible / short-lived / escalated to human). A double-charge refund handled by an improperly-guarded agent can pull up 10 similar customers, refund all, email 60% coupons. Policy + context bound it: read/summarize only one ticket, escalate decisions to human.

**Incidents:** company autosorting hiring candidates — applicants prompt-injected the chat interface to write/execute Python scripts; engine bills went haywire, capabilities shut down. Food-ordering chatbot: people ask it to tell jokes or write Python (token maxing). End users will use the interface however they want; it's your responsibility to define what the agent can and cannot do.

**Incremental adoption (5 steps):** 1) inventory — which agents, what tools, what credentials, what data; 2) add visibility (agent ID, task ID, trace IDs, basic audit); 3) separate agent identity from human identity (never pass human tokens/API keys to agents); 4) add review for highest-impact effects (human in the loop for refunds); 5) continuous authorization — reevaluate policy at each step, downgrade/revoke on scope increase. First maturity step is not a perfect policy — it's knowing which agents can act and what authority they currently have.

**Ask for vendors:** first-class "agent on behalf of" grants (short-lived second-layer tokens, non-reusable, context-bound) + revocation strategy; tool providers should validate grants and emit structured audit events ("Why did the agent do what it did?" must be answerable — "it's AI and it just did it" loses trust). "The next platform perimeter should be delegated agent authority, not another place to paste a long-lived API key."

**Babysitter analogy:** we wouldn't hand a caretaker bank accounts, SSN, credit cards, house keys, full authority — so why hand agents full authority? Number one failure mode in production systems today isn't model quality, it's lack of identity systems; frontier models (Claude Mythos, Fable 5) can not only operate in a system, they can figure out what they can do and break it.

**Mentioned:** DPACT Research Paper https://doi.org/10.2139/ssrn.7307799 ; OpenClaw https://openclaw.ai/