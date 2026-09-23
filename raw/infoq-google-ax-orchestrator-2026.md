# Google Open-Sources AX — Kubernetes-Style Orchestrator for Autonomous AI Agents (2026-09-22)

**Author:** Olimpiu Pop (InfoQ)
**Source:** https://www.infoq.com/news/2026/09/google-ax-orchestrator/
**Context:** InfoQ news. AX hosted at agentexecutor.io, GitHub google/ax, Apache 2.0. Runs on Agent Substrate. Digest 23.09 candidate.

---
Google introduced AX: open-source, Apache 2.0 orchestrator and declarative runtime to execute and scale autonomous AI agent workloads. Running on Agent Substrate, AX treats agents as **stateful actors** rather than microservices or batch jobs, offering sub-second task suspension/resumption + four declarative primitives: Task, Workspace, Gateway, Model.

Problem: modern AI agents are stateful, bursty, long-running — intensive compute during reasoning/tool execution/local code eval, interspersed with prolonged idle periods awaiting model responses, external API feedback, or HITL intervention. In conventional K8s/containers: keeping dedicated sandboxes active during idle = compute underutilization; cold starts introduce latency that degrades interactive agent loops.

Architecture (systems research from Google + Google DeepMind): each agent session = isolated actor sandbox with strict CPU/memory boundaries. On idle (waiting for inference provider/tool call): platform checkpoints execution state and suspends. Resumes in sub-second intervals, zero cold-start delay, multiplexing dozens of tasks onto shared host workers.

**Four Kubernetes-style primitives (ax.io/v1alpha1):**
- **Task** — execution lifecycle, sandbox resource constraints, references to supporting infra.
- **Workspace** — pre-execution environment assembly: declaratively mount Git repos, configure MCP servers, install skill bundles, or provide natural-language goals that an initialisation agent executes to bootstrap toolchains/dependencies before task start.
- **Gateway** — outbound network security policies: restrict sandboxed agents to explicit allowlists of hostnames/ports; credential injection into outbound requests.
- **Model** — unified control point for LLM provider parameters, runtime configs, secrets stored in Kubernetes.

CLI (`ax`, written in Go): `ax apply` (register manifests), `ax watch` (stream task phase/condition changes), `ax ssh` (interactive sandbox debugging), `ax suspend`/`ax resume` (manual task execution control). Control plane deployed to K8s via ko + Redis into ax-system namespace.

Positioned for production agent deployment and research (sandboxed trajectories, RL loops, agent benchmark evals at scale).

Community split (HN/Reddit): infrastructure engineers praise it for solving prohibitive cloud costs of idle agents; developers criticize "ergonomic workflows" marketing given heavy K8s/cluster/CRD overhead (ko). Practitioner notes: AX = foundational execution runtime, NOT a high-level app orchestrator (vs LangGraph/CrewAI); gVisor-isolated sandboxes contain blast radius; early issues — egress proxy dropped connections, rudimentary secrets management. Not a quick-start for solo hackers; an essential compute primitive for large long-running agentic fleets.

QA relevance (digest): K8s-like runtime with state management → QA can test suspend/resume and resource allocation of AI agents.