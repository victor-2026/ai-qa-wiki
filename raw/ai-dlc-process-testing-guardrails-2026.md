AI-DLC (AI-Driven Development Lifecycle) — process-oriented review focusing on testing methods, guardrails, and parallelization.

Source: Google AI response synthesizing IBM Think, Microsoft/GitHub Spec Kit, ResearchGate (May 2026), QA Bible, and critical Medium review.

## 1. Methods for verifying AI results

- **Dual-Agent Cross-Checking:** Model A generates code, isolated Model B writes tests from business requirements only. Auto-debug loop if tests fail.
- **Differential Testing:** Run old (human) and new (AI) code in parallel on production data, compare outputs. Divergences = bugs.
- **Property-Based Testing:** AI generates tests for invariants (e.g., "account balance never negative") not specific values. Catches edge-case hallucinations.
- **AST/Semantic Analysis:** AI validators build call graphs, verify architectural compliance (e.g., Layered Architecture not violated).

## 2. Guardrails & Constraints

- **Agent Constitutions (SKILL.md):** Hard rules — no external libraries without architect approval, mutation coverage ≥ 80%.
- **Token & Cost Budgets:** Max 5 debug iterations or $2 per task → escalate to human.
- **Sandboxing:** Tests run in ephemeral Docker/K8s containers. No direct access to staging/production data.
- **Human Gatekeeping:** AI can write code + tests + run pipeline, but Merge PR always requires human approval.

## 3. Process Flow & Parallelization

```
[Business Requirements] → [Spec (Markdown/Spec Kit)]
                              │
              ┌───────────────┴───────────────┐
              ▼                               ▼
   [Agent-Developer]               [Agent-Tester]
   (Feature generation)            (Test plan + auto-tests)
              │                               │
              └───────────────┬───────────────┘
                              ▼
                  [Sandbox: Run tests]
                              │
           ┌──────────────────┴──────────────────┐
    (Tests failed)                        (Tests passed)
           ▼                                     ▼
[Auto-debug by agent]              [Human Code Review / Approve]
                                             │
                                             ▼
                                        [Auto-CI/CD]
```

Phases:
1. **Specification (Shift-Left):** Human describes feature → AI converts to strict spec. AI checks spec for logical contradictions before code.
2. **Parallel Generation:** Two streams — Agent A writes code, Agent B writes integration/E2E tests from same spec.
3. **Merge & Auto-Verification:** Code + tests meet in sandbox. If tests fail, Agent-Developer gets logs and fixes. Fully autonomous, seconds.
4. **Human-in-the-loop:** Human gets PR with AI report: what was done, how tested, edge cases covered.

Parallelization:
- Fleet of agents runs 1000+ isolated scenarios in cloud simultaneously
- Mutation testing runs in parallel — AI creates mutants, checks if colleague's tests catch them

## 4. FinTech-specific (VS Code + GitHub Copilot + MCP)

Stack: VS Code/VSCodium + DevContainers + GitHub Copilot Enterprise (Data Exclusion) or Continue.dev with local LLM + MCP protocol.

Three verification phases:
1. **Pre-validation in IDE:** Block API keys/PII in LLM context (Trufflehog), architectural linting (SonarQube/Checkmarx)
2. **Autonomous dual-agent in CI/CD:** Synthetic data generation + parallel test design + stress testing edge cases (rounding, zero amounts, race conditions)
3. **Human Gatekeeping:** AI cannot auto-merge. Human reviews Semantic Diff — AI explains financial risks in plain language.

Key insight: mutation testing as quality gate for AI-generated tests — if mutants pass, tests are unreliable.
