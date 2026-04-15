**Source:** [Habr - Pipeline Triad Pattern](https://habr.com/ru/articles/1023554/)
**Date:** 2026-04-15
**Author:** Егор Зиновьев

---

# Pipeline Triad Pattern: AI Agent Pipeline for SDLC

## Core Idea

Not one AI agent, but **pipeline of triads**: Creator + Critic + Arbiter.

Each triad closes its SDLC stage, human controls only at 4 checkpoints.

## The Triad

**Creator** — generates code/output
**Critic** — finds problems, validates
**Arbiter** — makes decisions (PASS/FAIL/PARTIAL)

Why three? LLM cannot self-correct reasoning (ICLR 2024). External critique needed.

## 14 Steps from Idea to Production

| Step | Role | Description |
|------|------|-------------|
| 0 | Human | Create task |
| 1 | Triad | Analytics — requirements → tech spec |
| 2 | Human Gate | Validate requirements |
| 3 | Triad | Development — code + review |
| 4 | Triad | Code review |
| 5 | Triad | Testing — unit, integration, property-based, fuzz |
| 6 | Triad | Regression |
| 7 | Triad | Security — SAST, DAST, dependency scan |
| 8 | Human Gate | Approve readiness |
| 9 | Triad | Artifacts — docs, release notes |
| 10 | Human Gate | Approve deployment |
| 11 | Auto | Deploy to staging |
| 12 | Human Gate | Verify staging |
| 13 | Auto | Deploy to production |

## Economics

- ~1 hour human time per task (vs 2-3 weeks traditionally)
- ~$6-12 per task via API
- Works best for: change requests, bugfixes, CRUD, integrations

## Key Patterns (from "Agentic Design Patterns" by Gulli)

1. **Prompt Chaining** — break into small steps
2. **Routing** — conditional logic
3. **Parallelization** — parallel execution where applicable
4. **Tool Use** — curl, git, scanners
5. **Memory Management** — short + long term
6. **Reflection** — self-critique

## QA Implications

1. **Testing triad** — Creator generates tests, Critic analyzes coverage, Arbiter decides
2. **Property-based testing** — can run boundary, mutation, property-based, fuzz tests in parallel
3. **Human gates** — cheapest place to catch bugs (hours vs days vs months)
4. **Artifact tracking** — full trace: who proposed, who rejected, why

## Limitations

- Hallucination of business logic
- Quality depends on prompt/skill descriptions
- Organizational processes remain
- Not for greenfield/R&D without formal specs

## Quality Metrics

- Lead time (target: hours, not days)
- Rework rate (% returns between steps)
- Defect escape rate (bugs in prod)
- Human touch time per task

## Security

- Least privilege for agents
- Read/write scope per repo
- No direct prod access
- Audit log all actions
- Policy engine over tool use
