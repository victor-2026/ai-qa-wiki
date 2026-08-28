# Toloka Platform: LLM QA, Agent Plan Mode, OpenClaw adversarial testing (2026)

Source: LinkedIn posts reposted by Vladislav Davydkin (Technical Solutions Engineer, Toloka, Belgrade) - Olga Megorskaya (CEO), Toloka company posts, Aleksei Novikov (PM). ~2026.

---

## 1. Self-service platform + public pipeline API (beta)

- Everything built in the visual editor can now be operated programmatically via HTTP: feed data, launch runs, monitor progress, pull results
- **Agent Plan Mode**: instead of building the pipeline, the agent studies your brief, produces a structured plan, and WAITS FOR HUMAN APPROVAL before touching a single node. Review it, leave comments, the agent updates the plan before building
- Self-check: test individual nodes before a full run
- Pay-as-you-go billing with upfront cost estimates; pause and resume without losing progress

## 2. AI agent builds multi-stage pipeline automatically

- Describe your data goal once -> an AI agent builds the entire multi-stage pipeline (collection, annotation, evaluation, validation)
- Agent asks clarifying questions upfront: pipeline structure, workforce split, consent flows, regional storage - "real architectural decisions"
- Each stage fully configured: data structure, task UI, quality criteria, contributor guidelines, audience filters, QA method
- **Quality runs automatically throughout: LLM QA validates every output before results reach the pipeline. Human QA available when needed**
- Use cases: finance benchmarks, legal RAG validation, large-scale robotics datasets, multilingual content evaluation

## 3. Tendem by Toloka - universal human layer

- System to manage human efforts for unpredictable, one-of-a-kind tasks (vs repeatable data projects)
- AI agent decomposes and orchestrates the task; expert network handles parts needing real judgment; quality checks before anything reaches user
- **MCP so agent developers can call human expertise directly from their workflows** - a universal human layer callable by users or agents
- Launched on Product Hunt

## 4. OpenClaw adversarial testing (security evals for production agents) - KEY

Context: OpenClaw agents leaking credentials, executing unauthorized commands, being manipulated into ignoring their own system prompts. "Not edge cases - what happens when agents go into production without structured adversarial testing."

Key points:
- Granting an agent access to your environment introduces real risk; harder question: have you systematically tested how it responds to misuse across the channels where it operates
- **OpenClaw is a self-improving, self-evolving agent: behavior governed by SOUL.md and MEMORY.md files that adapt over time**
- **Adversarial testing isnt just diagnostic: each discovered attack pattern can be absorbed into these files as a new defensive boundary - every successful exploit becomes future protection against verbal attacks, social engineering, prompt manipulation**
- Toloka offers structured security evaluation for OpenClaw agents deployed on Telegram, Discord, WhatsApp, Slack
- Coverage: **access control, prompt injection, session isolation, memory poisoning, and four other defined attack vectors** with clear success criteria
- 300+ vetted specialists, results in 6-8 hours

## 5. New Toloka Platform - agent as primary interface

- AI agent isnt a feature on the side - it's the primary way to interact with the platform
- You bring the goal and domain knowledge; agent holds context of the entire task, understands each step, translates your language into a structured spec

---

## Why this matters for QA (analysis notes)

- **Agent Plan Mode = verify-before-execute gate**: human approval before the agent touches anything. Same pattern as Barady L1-L5 (plan gate), Shcherbinin verification layer. QA angle: the plan is a reviewable artifact - a testable checkpoint.
- **LLM QA validates every output before delivery** = verification layer inside the data pipeline; human QA as escalation tier.
- **OpenClaw taxonomy = practical adversarial checklist for LLM-testing skill**: 8 attack vectors (access control, prompt injection, session isolation, memory poisoning + 4), channel-aware (Telegram/Discord/WhatsApp/Slack), with success criteria.
- **SOUL.md/MEMORY.md mutation angle**: self-improving agents absorb exploit patterns into defensive boundaries - this is mutation testing applied to agent memory/prompt files. Anti-overfit pattern extension: mutate the agent's own memory files and see if defenses hold.
- **Tendem MCP**: human-in-the-loop as an API - the human layer is a callable service for agents, quality checks gated before output.