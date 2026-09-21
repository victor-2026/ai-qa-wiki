# Archestra: Skills Aren't Prompts. They Can Run Code. (2026-08-12)

**Author:** Arseny Kravchenko (Founding AI Engineer, Archestra)
**Source:** https://archestra.ai/blog/skills-arent-prompts-they-can-run-code
**Context:** Why agent skills are an execution packaging format, why scripts change what agents can deliver, and why production-grade skills require sandboxed code execution. Author initially rolled his eyes at Skills (thought it was "Nth way to inject a prompt") — turned out wrong.

---

## TL;DR

Skills = folder with SKILL.md (name, description, instructions) + optional scripts/docs/templates. Open convention (Anthropic, OpenAI, "roughly everyone else who shipped an agent product"). Not a prompt trick: it's a domain-knowledge + execution packaging format. Skills beat human-like role-agent teams via progressive disclosure (model sees only the one-line description, loads body only when relevant → hundred skills installed, pay context cost of the one you use). Scripts = the game changer (three lines of Python > a paragraph of tokens). Scripts force the sandbox question — sandbox is the precondition for shipping skills, not a bolt-on.

## Why skills beat "agent teams" (persona-routing)

Archestra leaned on specialized agents (frontend agent, reviewer agent, role prompts) and walked it back. Agentic teams lose to skills because of progressive disclosure: a swarm of role-prompted agents pays for every persona's context whether the task requires it or not, plus manual assignment of who talks to whom. Skills invert that — load only what the task needs.

Spicy take: "humans split by job titles because we don't share a pretrain; but agents do, so they should be routed by data and tasks, not by senior_frontend_dev."

## Why scripts are the game changer

A skill carrying scripts = the line between "nicer way to organize prompts" and "the agent can now deliver." Chat-only agent reasons in tokens; a skill with a script lets the agent run code. Some work is cheaper and more reliable as three lines of Python than as a paragraph of tokens hoping to compute the right number.

Skills are portable: folder format same across vendors — not a bet on a single model provider. "Versionable, transferable. That's a real property, not marketing."

## Evidence

Recent framework (arxiv 2606.17819) ~500 real open-source skills, two metrics: did the agent complete the job / follow the intended workflow. Goal-completion barely budged; relevant skills moved score 65 → 80, almost entirely instruction-following (agent used the right, current API/CLI instead of deprecated one). Example: agent defaulted to old huggingface-cli prefix switched to current hf commands once it had the skill — no model upgrade needed, skill carried the contract. Confirmation: SkillsBench (arxiv 2602.12670, 7,308 trajectories).

Caveat: skills only help when they encode real, targeted, versioned procedures. Generic/stale skills reduce gain to nothing; one study (arxiv 2603.15401) found a few stale skills made things worse by fighting the project's actual context. "This asymmetry is the whole reason why a skills platform is not at all similar to a skills folder."

## Sandbox: what scripts unlock + why it's mandatory

Scripts kill a class of bespoke tools (arithmetic → run code, fetch repo → curl, unzip sketchy archive → in the box). "Do the thing" replaces "integrate a tool for the thing."

Most real skills can shell out, hit a runtime, reach the network. "The model reads a file" becomes "the model writes and executes code on your infrastructure" — every prompt is a potential execution path.

Evidence of risk:
- Microsoft AutoJack (Jun 2026): single malicious webpage rendered by a browsing agent crossed a localhost boundary, spawned processes on the host. "Once an agent can read untrusted input and reach a privileged local service, localhost is no longer a trust boundary."
- Framework (arxiv 2509.22040) with 314 injection payloads got command-execution success rates 41-84% on coding agents.

## The one non-obvious decision: durable replay, ephemeral container

Naive approach: one long-lived container per chat, mutate in place. Archestra deliberately does NOT do that. Sandbox has no durable container. Source of truth = append-only command log in Postgres. Every command spins up a fresh container from a warm base image, replays the whole ordered history, then runs a new step and appends. **Container is a cache, the log is the truth.**

Properties: crash/restart resilience, exact ordering (on-disk order deterministically matches acceptance order), immutable inputs (skill bytes pinned to content hash at mount), cheap in typical cases (content-addressed layer cache hit). Uploads live in the log (else cold rebuild loses the file); artifacts (output bytes) stored separately, never replayed. The upload-vs-artifact split falls out of "what must survive a rebuild."

Not free: non-deterministic commands (network/clock/RNG) can diverge on cold replay (uv add without a pin). Original recorded stdout treated as canonical, called a v1 limitation — "failure modes written down, better than calling it elegant with them hidden away."

## The boundary and threat model

Isolation primitive: Dagger (programmatic container engine, superb caching). Threat model: NOT "sophisticated external attacker pivoting through sandbox into corporate network." It's "separate the vibe-coded script one of our own employees just had an agent generate from everyone else's — careless, not malicious." An OCI container with non-root execution (uid 1000), CPU/mem rlimits, wall-clock kill = proportionate measure. "Blast-radius boundary between coworkers' half-baked scripts, not a nation-state perimeter... pretending otherwise would just be security theatrics."

Stronger boundary = backend swap, not rewrite: same replay engine, different runtimeClassName (runc → gVisor → Kata/Firecracker).

Caveat: egress enabled inside the container (npm/uv need it) — network isolation rides on k8s NetworkPolicy on the engine pod. Without policy the engine can reach link-local + cloud-metadata endpoints. Documented in the limitations doc, "not buried."

## Bottom line

Skills move instruction-following, not raw completion — agent works the way you meant; role-play subagents only pretended to do that. Production-grade only when paired with a reproducible, disposable execution environment.

---

## Cross-references (in this wiki)

- `wiki/archestra-jev-100-agent-calls-benchmark-2026.md` — same author (Arseny Kravchenko)
- Skills as prompt-injection surface matches "Checking is not testing" / harness-discipline series
- progressive disclosure (archestra blog) — context cost control; matches reasoning-efficiency theses

## Relevance to VerdictGate / Article series

- **Skills = execution packaging** — parallels our skills approach (tech-writer, qa-automation-engineer); SKILL.md convention is what we use in ~/.config/opencode/skills.
- **"Log is the truth, container is disposable"** (append-only command log + replay) = reproducibility/auditability pattern directly applicable to VerdictGate/evidence packs — the *log* (evidence) outlives the run environment. Same principle as our SCORER_VERSION / frozen-bar.
- **Threat model honesty** ("careless not malicious", proportionate boundary) = our risk-tiering philosophy (proportionate controls per tier, not theater).
- **Skills can run code → sandbox mandatory** = article 26/27 ammo: agent proficiency = execution capability; evaluation must include the execution path, not just prompt compliance.
- Skills as data-driven (65→80 instruction-following) = "the harness/contract carries the quality, not the model" — supports our vendor-eval / harness-over-hype thesis.