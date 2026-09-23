---
source: "infoq-dpact-framework-ai-agents-2026.md"
ingested: "2026-09-23"
---

# Securing AI Agents – The DPACT Framework  

**Source:** InfoQ Podcast “Securing AI Agents: Identity, Authorization, and the DPACT Framework” (21 Sep 2026)  
**Guest:** Sahil Agarwal – Leader, Identity & Authorization Stack  

---

## Summary  

As AI agents move from chat‑only helpers to autonomous “delegated actors” that can orchestrate tools, provision resources, and affect real‑world outcomes, traditional human‑centric security models become insufficient. The DPACT framework (Delegation, Policy, Auditability, Context, Time) offers a conceptual blueprint for governing agents without stifling innovation. It stresses that agents must **act on behalf of** a human rather than impersonate them, and that authority should be granted as short‑lived, task‑specific tokens rather than permanent API keys. An incremental, inventory‑first approach is recommended for bringing production systems under control.

---

## Key Concepts  

| Component | What it means | Security impact |
|-----------|---------------|-----------------|
| **Delegation** | Explicitly record whose identity the agent represents. | Prevents impersonation and clarifies responsibility. |
| **Policy** | Define both allowed actions and absolute prohibitions. | Guarantees that an agent cannot overstep its mandate (e.g., “read‑only” vs “execute”). |
| **Auditability / Explainability** | Log enough metadata (agent ID, task ID, timestamps) to reconstruct decisions days later. | Enables post‑mortem analysis, compliance, and feedback loops for model retraining. |
| **Context** | Constrain the operational envelope (e.g., “draft email only, do not send”). | Limits the blast radius of mistakes or malicious use. |
| **Time** | Attach a TTL or task‑completion condition to every grant. | Guarantees that authority expires automatically, reducing lingering privileges. |

### Shift in Threat Landscape  
- **Pre‑AI era:** Humans → applications → resources, with clear permission boundaries.  
- **Agentic era:** Autonomous actors chain tools, infer intent, and act without a human in the loop, breaking the classic permission model.

### Incremental Adoption (5‑step maturity path)  

1. **Inventory** – Catalog agents, tools, credentials, and data they touch.  
2. **Visibility** – Emit identifiers (agent, task, trace) and basic audit records.  
3. **Identity Separation** – Never forward human tokens to agents; use distinct agent identities.  
4. **Human‑in‑the‑Loop Review** – Require manual approval for high‑impact actions (e.g., refunds).  
5. **Continuous Authorization** – Re‑evaluate policies at each step, revoking or downgrading rights as scope changes.

---

## Practical Applications  

| Domain | Typical Agent Activity | DPACT‑driven Controls |
|--------|-----------------------|-----------------------|
| **Customer Service** | Auto‑resolve tickets, issue refunds | Tiered autonomy (read‑only → reversible → human‑escalated); policy limits refunds to a single ticket; context forbids bulk email sends. |
| **Hiring Automation** | Parse resumes, schedule interviews | Delegation ties actions to recruiter; time‑boxed grants prevent agents from persisting after hiring cycle; audit logs capture why a candidate was shortlisted. |
| **Food‑ordering Chatbots** | Suggest meals, process payments | Context restricts agents to “suggest” mode; policy blocks code execution; time limits prevent prolonged payment authority. |
| **Infrastructure Ops** | Spin up VMs, apply patches | Delegated tokens with TTLs replace long‑lived API keys; audit trails feed into compliance dashboards. |

### Vendor Requirements  

- **First‑class “on‑behalf‑of” grants** – short‑lived, non‑reusable tokens bound to a user and a task.  
- **Structured audit events** – machine‑readable explanations (“why” an action was taken).  
- **Revocation mechanisms** – immediate invalidation of grants when policy changes.

The “babysitter” analogy underscores the absurdity of giving agents unrestricted access to bank accounts, SSNs, or house keys; the same discipline applied to humans should apply to agents.

---

### See also  

- [`wiki/martinfowler-making-data-ready-agentic-ai-2026.md`](wiki/martinfowler-making-data-ready-agentic-ai-2026.md) – Preparing data for agentic AI.  
- [`wiki/autonoma-multi-agent-handoffs-2026.md`](wiki/autonoma-multi-agent-handoffs-2026.md) – Testing handoffs and orchestration in multi‑agent systems.  
- [`wiki/kiro-crew-multi-agent-orchestration-open-source-2026.md`](wiki/kiro-crew-multi-agent-orchestration-open-source-2026.md) – Open‑source platform for multi‑agent orchestration.  
- [`wiki/autonoma-crewai-evaluation-2026.md`](wiki/autonoma-crewai-evaluation-2026.md) – Evaluation methodology for CrewAI agents.  
- [`wiki/ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md`](wiki/ai-qa-e

---
*Source: [raw/infoq-dpact-framework-ai-agents-2026.md](../raw/infoq-dpact-framework-ai-agents-2026.md) · Generated by wiki_llm.py (Groq)*
