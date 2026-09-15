# Smart Suites: AI-Driven Test Selection — Testkube (2026-04-22)

**Source:** Sarvani Yallapragada (Dev Advocate, Testkube) https://testkube.io/blog/ai-driven-test-selection-smart-suites — demo with code (payment-service, GitHub MCP + Testkube MCP).
**Use for us:** third independent implementation of diff→test-selection (O2 blast radius, QAEverest sensitivity, now Testkube agent). Dual-mode pattern mirrors our x1 + periodic-deep runs.

## Mechanism

Agent reads latest commit diff via GitHub MCP, classifies every changed line (functional: logic/config/routes/schema/auth vs non-functional: comments/whitespace/docs), queries Testkube history (labels, pass rates, flakiness), runs best-fit labeled workflows via Testkube MCP, reports (what changed → why these tests → execution IDs).
- All-non-functional → run NOTHING (with SHA + explanation). Same shape as our M2-trivial expectation (no-op → green, stay silent).
- Prompt quality called out as THE critical factor (vague prompt → wrong selection). Matches our hint-engineering experience (Agentiqa credential-name confusion).

## Dual mode (maps to our protocol)

- **Smart suites (fast feedback):** selection per change.
- **Scheduled full runs (safety net):** cron, off-CI-path, catches what selection missed.
- = our shape: x1 mutants in flow + deeper 3x/10x periodically. Independent convergence, citable.

## Links

- Four-layers piece (orchestration context), delivery-pipelines (thresholds), quality-gates post
- Our mapping: per-risk-tier framework (selection by risk), QAEverest sensitivity (14/18), Agentiqa M2 (trivial → silent PASS)
