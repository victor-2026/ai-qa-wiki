---
source: https://www.linkedin.com/feed/update/urn:li:activity:7506204110497435648/
author: Radik Zagirov
role: Co-Founder & Builder, Agentiqa. AI Quality Engineering. TUM.ai
date: 2026-09-16
fetched: 2026-09-17
tags: [agentiqa, action-ontology, palantir, runtime-verification, state-machine, enterprise-agents]
---

# Radik Zagirov — Action Ontology Runtimes for Agent Execution

The standard mental model for AI agents is still the tool-calling loop: give an LLM a set of API definitions, append history to context, and let the model probabilistically decide what to invoke next.

This works for linear, stateless tasks. But in stateful enterprise systems (ERPs, multi-role platforms, complex web apps), it breaks down quickly. In long trajectories, relying on token probabilities to respect business invariants leads to compounding errors. Prompting an agent with rules like "never approve an invoice before checking line items" works 90% of the time, which in production means failing almost daily.

The shift for how we build runtimes at Agentiqa came from studying Palantir's Action Ontology.

In Palantir Foundry, an Action isn't an API wrapper. It is a formal, guarded state transition: preconditions must pass on the object graph before an action is even valid, mutations run deterministically, and post-conditions are verified against reality.

Adapting this to autonomous agent execution led to three architectural shifts:

1. Dynamic action spaces over tool dumps
Instead of putting 40 tools in the prompt, the runtime evaluates the current state first. If an order isn't approved, SubmitOrder physically does not exist in the prompt context. The model cannot attempt an illegal transition because the action space is constrained by code before token generation.

2. Decoupling intent from mutation
The model is responsible for resolving intent within the active state (interpreting messy inputs, UI layouts, and selecting the action primitive). The ontology handles parameter validation, idempotency, and the actual execution deterministically.

3. Verification external to the model
An action is never marked successful because the agent asserts it succeeded. The runtime independently monitors ground truth—network response codes, database changefeeds, and DOM state via CDP. If the expected state diff isn't observed, the transition is rejected.

The core realization was that language models shouldn't be treated as the operating system.

LLMs are brilliant at navigating ambiguity and unstructured inputs. But the execution layer must remain a deterministic state machine. Reliability in enterprise autonomy isn't about finding models that hallucinate less—it's about building runtimes where hallucinations cannot mutate state.
