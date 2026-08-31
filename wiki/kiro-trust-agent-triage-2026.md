# How We Learned to Trust an AI Agent to Triage Production Incidents

**Source:** https://kiro.dev/blog/trust-agent-triage/
**Date:** August 21, 2026
**Author:** Sai Srinivas Somarouthu
**Tags:** #incident-response #triage #kiro-cli #mcp #skills #trust
**Raw:** [kiro-trust-agent-triage-2026.md](../raw/kiro-trust-agent-triage-2026.md)

---

## What It Is

Frontier team (AWS) runs Kiro data plane (IDE/CLI/Web/iOS/Crew → fleet of models via Bedrock, multi-region) and lets Kiro CLI agent triage production tickets autonomously. Story: 2:33 AM Sunday availability alarm (model responses stalling mid-stream) → 2:46 AM (13m35s later) defensible diagnosis on ticket: silent stream stalls from prod bug or capacity scaling, customers affected, competing hypotheses ruled out, next action with evidence. On-call typed: `file escalation` / `fix bug` — job became reviewing brief, not starting investigation.

Triage = hypothesis search across 500 possible questions, picking right 5 first. Agent built for it: read-heavy (96.9% reads, parallelizable), repeatable, compounds knowledge; human at 3 AM can't.

## System: Markdown + MCP Around Stock Kiro Harness

No custom orchestration, no fine-tuned model — stock Kiro CLI pointed at own ops with 3 plain-file layers (reviewed like code):

- **Agent config** — model + tools + markdown steering file (operational rules = human judgment once, applied thereafter)
- **MCP servers** — ReadOnly AWS accounts, logs, tickets, pipelines, code review, Slack
- **Skills + knowledge** — progressive disclosure: agent holds index of 107 skills; loads full playbook for matching alarm only (vs stuffing all runbooks into prompt → fails at ~10). Example: rate-limiting skill excerpt. Knowledge layered: always-needed facts loaded, playbooks on demand, archive of past investigations searchable.

One long-running dispatcher watches queues, spawns one headless CLI session per ticket. Model = runtime param: lead investigator = strongest model, fan-out = swarm subagents on cheap fast models, ambiguous calls = council of 3 providers, disagreement → gather more evidence.

## Anatomy of One Investigation

13m35s pipeline: Orient → Measure → Classify → Rule out → Publish. Every step logged, every claim links to query. Value of work nobody does manually: prior alarm looked like model-wide capacity event; agent joined every stream error to routing record by request ID → 96.5% errors from 2 of isolated serving cells, rest zero → hypothesis "uneven per-cell quotas" checked ReadOnly → latent bug in upstream dependency. Engineer could, but not weekend night across dozens of accounts.

## The Flywheel (Built by Humans, Run by Agents)

Investigate → Record → Compile → Evolve → Skill library (next identical alarm starts where last left off):

- **Corrections → lessons** — stored once, injected into every future session (hundreds corrections vs thousands runs), agent patches doc that misled it (prompt bug = doc bug)
- **Investigations → knowledge** — closed tickets distilled to searchable archive (future sessions query first)
- **Agent drafts skills, humans review** — per-cell step added same night; library curated like codebase + nightly job
- **Shared state** — conditional-write escalation tracker → 10 parallel agents observing same incident file one upstream ticket, not ten

Failure mode: lesson-capture once accepted raw ticket comments verbatim from interrupted sessions as "wisdom" → future sessions studied garbage. Fix: schema validation before write + nightly prune. Learning pipeline compounds garbage as efficiently as knowledge.

## Cost / Scale

~250 investigations/month, median 13.6 min, unattended. Spend bounded by structure (timeouts, stuck-detection, concurrency cap, cheap fan-out), not restraint. Cost ~9 top-tier subscriptions. Reclaimed hours → reviewing briefs, correcting agent, fixing roots.

## What Went Wrong (Lessons)

- **Agents inherit doc bugs at machine speed** — one stale line propagated to multiple tickets. Fix: correct + ask "what misled it?" → fix doc (5 min once beats 5 min weekly).
- **Confident half-answers > wrong answers** — steering rule: test & rule out competing hypotheses before concluding + automated checks (arithmetic, alarm state, duplicates).
- **Conciseness builds trust** — early full worklogs in customer-visible threads noisy; now one short post to visible thread, full to worklog. Judged by worst comment.
- **No single autonomy setting** — `stop asking to draft review` vs `never resolve ticket/change severity; humans only`. Every action needs its own rule in steering file.
- **Security via infrastructure, not prompts** — default ReadOnly via role allowlist, Admin request returns error, per-session scoped credentials minted for declared task only.

## Where It Goes

Agent does triage today; increasingly repairs (drafting code reviews for fixes behind mandatory human review). Whole system is markdown + MCP + stock CLI → improvements are product-relevant. On-call becomes decision queue for work already done. Swami's frontier teams post: "invest in agent context" = first step; this queue is that.

## Relevance to QA/QE

| Pattern | QA Application |
|---------|----------------|
| 96.9% reads, gated writes | QA agent: read logs/metrics freely, gate state-changing actions (merge, deploy) |
| Progressive disclosure (107 skills) | Don't stuff all runbooks into prompt; index + load on demand |
| Flywheel (corrections → skills) | Retrospective → steering update + skill draft, not just postmortem doc |
| Rule out competing hypotheses | Require agent to disprove alternatives before concluding RC |
| Conciseness (short visible + full worklog) | PR comment = summary + link to full evidence |

## Cross-links

- Related: [Continuous prompt evaluation](kiro-continuous-prompt-evaluation-llm-judges-2026.md) — evaluation for prompt changes
- Related: [Root cause 33s](kiro-root-cause-33s-2026.md) — same CLI, perf vs incident domain
- Concept: [AI QA evidence layer](ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md)

---


## Single vs Multi-Model Roles (Cost/Quality)
- **Lead investigator:** strongest model (accuracy matters for synthesis).
- **Fan-out swarm:** cheap fast models for parallel log queries (volume, not depth).
- **Council:** 3 providers debate ambiguous calls; disagreement = signal to fetch more evidence, not vote.
- This mirrors QA: lead reviewer + parallel checkers + adjudication. Structure bounds spend vs letting single agent loop expensively.
- Headroom: 250 tickets/mo at 13.6m median → cost ~9 subscriptions. Structure (timeouts, concurrency cap) controls bill, not ad-hoc restraint.


## QA Parallels
- Triage agent = flaky-test triage agent: 96% reads, hypothesis search over logs, posts evidence-linked diagnosis.
- Skills library = runbook wiki that agent actually executes — keep as markdown in repo.
- Corrections → lessons mirrors mutation-matrix learned_patterns.json — curated, not auto-appended.

*Ingested: 2026-08-30*
