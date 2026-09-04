# Andrew Ng: AI Engineering Skills Map — Using Coding Agents

**Source:** https://www.linkedin.com/pulse/ai-engineering-skills-map-using-coding-agents-andrew-ng-h8yxc/ (Andrew Ng, DeepLearning.AI)
**Date:** September 4, 2026 (1,991 reactions, 76 comments at fetch)
**Tags:** #ai-engineering #coding-agents #spec #verification #AGENTS.md #MCP
**Raw:** [AI Engineering Skills Map - Using coding agents.md](../raw/AI%20Engineering%20Skills%20Map%20-%20Using%20coding%20agents.md)
**Series:** (1) Map m479c Aug 14 → (2) Building/Deploying gyn5e Aug 21 → (3) Fundamentals 7lnac Aug 28 (ingested) → (4) this article

---

## What It Is

Fourth installment of Skills Map series: the skill of steering coding agents for code + non-code tasks (data analysis, ops). Agents evolve fastest of all top-level skills — proprietary (Claude Code, Codex, Cursor) + open (OpenCode, Pi) via harness + model improvements. Keeping up = continuous experimentation, building, learning. Based on dozens of top-AI-engineer interviews + own team practice.

## Workflow: Plan → Execute → Deploy/Monitor

Same shape as pre-agent software, focus shifted from code to decisions:

1. **Planning** — (i) brainstorm (research, experiments, codebase understanding), (ii) spec (requirements, technical design, architecture) + execution plan; review plan vs assumptions, security, overengineering.
2. **Execution** — build with calibrated autonomy + verify via automated/human checks.
3. **Deployment + monitoring** — deploy via CI/CD/human gates; agents watch logs, surface issues, propose/execute improvements.

Highly iterative, steps omittable (greenfield prototype = loose prompt-spec; brownfield with users = heavy spec). Skilled devs loop back: verification fail → steer rebuild; monitoring → update + redeploy.

## Five Skills

### 1. Directing the Workflow
Navigate each step: human vs agent effort per step, when to iterate back. Tradeoffs speed/cost/risk/effort: how much to research up front, when to retain human ownership of critical work, architecture choice, spec detail level, decomposition into verifiable steps.

### 2. Enabling Agent Autonomy
Choose level: interactive back-and-forth vs delegated chunk vs loop-until-success. Manage context: capture learnings, feedback, changed assumptions downstream. Parallel agents (human- or agent-orchestrated) + human attention management. Run safely: permissions, gating (leaks, data loss).

### 3. Reviewing the Work
Output uncertain — review redirects. Behavioral + functional verification matched to task; user flows (agent screenshots as evidence); eval sets + LLM-as-a-judge for qualitative. Decide automation level: full-auto so agent self-checks; evaluate tests against aims, evolve them. Agentic code review + AI security/architecture audits; human reviews of behavior (rarely code); deployment verification; agent-operated monitoring/incidents.

### 4. Customizing Agent + Environment
Skills, plugins, MCP servers (prune when model obviates); hooks for repeatable parts (auto-review, CI/CD); standing context (`AGENTS.md`/`CLAUDE.md`: codebase, architecture, style, data access); state across sessions/parallel agents; retrospectives accumulating learnings; navigable conventions; clearing agent-generated debt; team context coordination.

### 5. Coding Agent Foundations
How agents work: search/retrieval, context windows, effect of tool calls/MCP on context, agents/subagents interaction, harness-around-LLM. Less black box → recognize failure modes: overengineering simple solutions, rigor loss without verification, stopping short, destructive actions. Reason about state, prescribe context, spot off-track runs.

## Key Warning

Social media overhypes long-horizon autonomous runs (hours, millions of tokens). Practical utility vs cost amplified beyond reality. Effective use = complex, highly iterative + high-skill intervention.

## Notable Comments

- **Elijah Billian:** add "evidence discipline" — durable record (changes, assumptions, checks, failures, unresolved); speed compounds safely only with verification + restart state.
- **Tom Mooney:** security for agents is different; deterministic controls vs probability posture.
- **Ram Ramanathan:** decomposition has no playbook; platform + requirements + context + multiple agents + iterative + human intelligence.

## Relevance to QA/QE

| Ng Skill | QA Application |
|----------|----------------|
| Directing workflow | Decide human-owned gates (auth/payment) vs agent-delegated; decompose into verifiable steps |
| Enabling autonomy | Calibrated levels: scout (interactive) → worker (delegated) → review-loop (until green); permissions per risk |
| Reviewing work | Behavioral + functional verification; screenshots as evidence; evals + LLM-judge; tests must match aims |
| Customizing env | AGENTS.md standing context; MCP servers; hooks for auto-review/CI; prune stale skills |
| Foundations | Recognize failure modes (overengineering, rigor loss, short-stop, destructive) — same as mutation blind spots |

## Critical Analysis

**Strengths:**
- Names open agents (OpenCode, Pi) alongside proprietary — legitimizes OSS harness stack.
- Verification as first-class skill with evidence (screenshots, evals, audits) — directly QA-compatible.

**Gaps:**
- No numbers (eval precision, cost per loop) — qualitative, unlike Kiro's 406K diagnostics or Zalando's 122 behaviors.
- Long-horizon skepticism stated but not quantified — no token-cost curve.

## Worked Example (Your Stack)

Greenfield prototype: loose prompt-spec + `worker` builds + `reviewer` checks + deploy; 30 min loop. Brownfield with users: full spec (requirements, design, architecture) + `scout` recon + `oracle` challenges assumptions + `reviewer` 3-round + human gate on auth/payment + CI/CD + agent monitoring of logs. Same workflow, different spec weight and gate strictness — exactly Ng's greenfield/brownfield split.

## Checklist (Per Build)

- Spec written before build? (detail matched to greenfield vs brownfield)
- Autonomy level chosen + permissions gated? (leaks, data loss, prod DB)
- Verification designed before generation? (behavioral + functional, screenshots, evals)
- Tests correspond to aims? (evolve if not; screenshots as evidence)
- AGENTS.md updated with learnings? (retrospective → standing context)
- Monitoring wired? (agents watch logs, propose improvements)

## Cross-links

- Related: [Fundamentals map](aiengineeringskillsmap-softwareengineeringfundamentals.md) (part 3, tradeoffs language)
- Related: [Ng loop engineering](andrew-ng-loop-engineering-2026.md) (3 nested loops, developer-as-QA)
- Related: [Pi ↔ OpenCode integration](../wiki/pi-opencode-integration-2026.md) (AGENTS.md/MCP/CLI loop)
- QA evidence layer: [ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md](ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md)

---

*Ingested: 2026-09-04 · Full text via webfetch (LinkedIn login wall bypassed for body)*
