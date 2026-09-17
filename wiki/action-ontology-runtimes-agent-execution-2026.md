---
title: "Action Ontology Runtimes: Constraining Agent Execution with State Machines"
source: https://www.linkedin.com/feed/update/urn:li:activity:7506204110497435648/
author: Radik Zagirov (Agentiqa, TUM.ai)
date: 2026-09-16
created: 2026-09-17
tags: [agentiqa, action-ontology, palantir, runtime-verification, state-machine, enterprise-agents, architectural-patterns]
aliases: [Action Ontology, Agent Runtime, Guarded State Transitions]
---

# Action Ontology Runtimes: Constraining Agent Execution with State Machines

**Source:** Radik Zagirov (Agentiqa) — LinkedIn post 2026-09-16
**Context:** Agentiqa's runtime architecture for autonomous agents in enterprise systems (ERPs, multi-role platforms)

## Problem

Tool-calling loop (LLM + API definitions + history) works for linear, stateless tasks. In stateful enterprise systems it breaks:
- Long trajectories → compounding errors from token-probability-based decisions
- Prompted rules ("never approve invoice before checking line items") work 90% — in production = failing daily
- Business invariants cannot be enforced by prompting alone

## Palantir Action Ontology Pattern

In Palantir Foundry, an **Action** is not an API wrapper. It is a formal, guarded state transition:
- Preconditions must pass on the object graph before action is valid
- Mutations run deterministically
- Post-conditions verified against reality

## Three Architectural Shifts

### 1. Dynamic Action Spaces (over tool dumps)
- Instead of 40 tools in prompt → runtime evaluates current state first
- If order isn't approved, `SubmitOrder` physically does not exist in prompt context
- **Model cannot attempt illegal transition** — action space constrained by code before token generation

### 2. Decoupling Intent from Mutation
- **Model** = resolves intent (interprets messy inputs, UI layouts, selects action primitive)
- **Ontology** = handles parameter validation, idempotency, execution deterministically
- Clear boundary: model reasons, runtime executes

### 3. Verification External to the Model
- Action never marked successful because agent asserts it succeeded
- Runtime independently monitors ground truth: network response codes, database changefeeds, DOM state via CDP
- If expected state diff isn't observed → transition rejected

## Key Insight

> "Language models shouldn't be treated as the operating system."
> "Reliability in enterprise autonomy isn't about finding models that hallucinate less — it's about building runtimes where hallucinations cannot mutate state."

## Cross-Links

- **Article 27** — guided QA engineer, harness as state machine
- **Article 22** — external boundaries, vendor/platform constraints
- **Agentiqa** — Radik's company, AI quality engineering
- **Palantir Foundry** — Action Ontology origin
- **Per-risk-tier framework** — risk classification determines runtime constraints
- **Greiler SCOPE** — agent tests signal safety where there is none (complementary: runtime verification solves this)
- **Tornhill "tooling enforces what you don't inspect"** — same principle, different framing
- **Bansal "harness configuration is a file"** — configuration as deterministic gate
