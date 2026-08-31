# Kiro Crew: Multi-Agent Orchestration Platform (Open Source)

**Source:** https://kiro.dev/blog/introducing-kiro-crew/
**Date:** August 4, 2026
**Authors:** Bolin Chen, Zejiang (Joe) Guo, Zezhen Xu (Amazon/Kiro)
**Tags:** #multi-agent #orchestration #open-source #k8s #aws #ACP

---

## What It Is

Kiro Crew is an **open-source multi-agent orchestration platform** built on Kiro CLI. Originally internal Amazon tool called **MeshClaw**, now open-sourced. 39,000+ Amazon builders, 500+ contributors, 597 updates, 143 weekly commits in <6 months.

**Key value:** Run multiple AI agents across sessions, tools, and repos with human oversight. Agents work while you sleep.

## Origin Story

- Started as side project "MeshClaw" inside Amazon
- 3 engineers wanted: kick off task, walk away, come back to something worth reviewing
- Inspired by OpenClaw + self-learning agent tools, but needed Amazon security compliance
- Built on Kiro CLI harness
- Community grew organically: engineers across roles (not just devs) extended it for their workflows
- "Narrow edge cases and quality-of-life fixes that only the person living in that workflow would think to add"

## Architecture

### Core Components

1. **Agent Client Protocol (ACP)** - orchestration standard (from Zed Industries)
   - Every step observable live via Activity view
   - One card per agent on dashboard
   - Tool calls, reasoning, results visible in real-time

2. **Defense-in-Depth Security**
   - OS-level sandbox
   - Denied-by-default commands
   - Suspicious-pattern blocking
   - Input validation
   - Sensitive-path blocking
   - Credential redaction
   - Signed audit log of every action

3. **Self-Learning Memory**
   - Preferences carry into new sessions (no cold starts)
   - Corrections become durable lessons
   - Repeated patterns become reusable skills
   - Memory/lessons/skills visible and editable

4. **Multi-Agent Coordination**
   - Multiple concurrent conversations (isolated context)
   - Subagents return results to parent
   - Parallel research + implementation

5. **Scheduling + Automation**
   - Recurring jobs on user-defined schedules
   - Morning digests, PR monitoring, deployment watching
   - Authenticated webhooks trigger on external events
   - Checkpoints + validation + retries

6. **Apps (Purpose-Built Interfaces)**
   - Custom UI + agents + skills + schedules + integrations
   - App SDK for custom builds
   - Launch Apps: DevFleets, Task Runner, Issue Radar
   - MCP Apps for data/actions

### Surfaces

- Desktop app
- Web dashboard
- TUI (terminal)
- Slack, Telegram, Discord integrations
- Local or remote machine

## Open Source Governance

- Steering committee in MAINTAINERS.md
- Minimal governance model
- Proposals as PRs, debated in repository
- Roadmap = conversation, not decree
- Supports integrations with other AI coding tools/providers
- Kiro + AWS engineers maintain core; trusted external maintainers can join

## Integration With Existing Kiro

- Reads `.kiro` config out of the box
- Steering files, skills, custom agents carry over
- Same configuration, different runtime

## Key Patterns for QA/QE

| Pattern | Relevance |
|---------|-----------|
| Self-learning memory | Agents learn from corrections, build domain knowledge |
| Cross-session continuity | Incidents/migrations span days, agents keep state |
| Observable orchestration | Every agent action auditable (antithesis to black-box) |
| Defense-in-depth security | Production-grade controls for AI agents |
| Apps as interfaces | Issue triage, monitoring dashboards, not just chat |
| Schedule + webhook triggers | Automated regression, PR monitoring, deployment checks |

## Relevance to Articles

- **Article 21 (Conway):** Kiro Crew = federation of specialized agents (identity per agent, delegation chain)
- **Article 26 (Testing AI Testing Tools):** Open-source = auditable; security layers = how you verify agent behavior
- **Article 27 (Guided QA):** Self-learning memory + corrections = QA-as-supervisor pattern
- **Article 20 (False Positives):** Observable orchestration = understanding agent reasoning

## Critical Analysis

**Strengths:**
- Open source with real production use (39K Amazon builders)
- Security-first design (defense in depth)
- ACP standard = vendor-neutral orchestration
- Self-learning = compounds value over time

**Gaps:**
- Built on Kiro ecosystem (vendor coupling at platform level)
- Amazon-scale governance may not fit smaller teams
- No mention of evaluation/benchmarking framework for agent quality
- "597 updates" = velocity, but quality signal unclear

---

*Ingested: 2026-08-30*
