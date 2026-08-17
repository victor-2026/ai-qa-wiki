---
title: "Monitoring & Observability for AI Systems"
type: article
updated: "2026-08-17"
tags: [llm]
---

# Monitoring & Observability for AI Systems

**Last Updated:** 2025-04-15
**Sources:** raw/monitoring-vibe-coded-apps, raw/llms-observability-driven-development, raw/splunk-odd-explained

---

## The Problem

AI systems are fundamentally different from traditional software:

| Traditional Software | AI/LLM Systems |
|---------------------|----------------|
| Same input → same output | Same input → may differ |
| Testable, reproducible | Not fully testable |
| TDD works | TDD doesn't fully work |

> "LLMs are black boxes that produce nondeterministic outputs and cannot be debugged using traditional techniques."

## Why Traditional Debugging Fails

- **Natural language is infinitely expressive** — infinite possible outputs
- **Long tail of edge cases** — impossible to enumerate
- **High randomness in edge cases** — different each time
- **User expectations** — meaningful results everywhere

## Observability-Driven Development (ODD)

Shift from **TDD** to **ODD**:

```
TDD: Write tests → Build code → Ship
ODD: Ship sooner → Observe → Feedback → Improve
```

### Why ODD is Necessary

1. Systems are increasingly complex
2. Nondeterministic outputs are the norm
3. Only way to understand: instrument + observe

### What ODD Requires

1. **Wide events** — arbitrary high-cardinality dimensions
2. **Traces** — ordered in time
3. **Ability to break down** — by any dimension

## Three Layers of Monitoring

### Layer 1: Uptime Monitoring
**Question:** Is your app reachable?

Tools: UptimeRobot, Better Stack, Pingdom
Setup: ~5 minutes

### Layer 2: Error Tracking
**Question:** Is your app working correctly?

Tools: Sentry, Datadog
Captures: exceptions, failed API calls, affected users

### Layer 3: Performance & Health
**Question:** Is your app fast?

Tools: Grafana, APM solutions
Metrics: response times, resource usage, throughput

## AI-Specific Monitoring

### For LLMs

| What to Monitor | Why |
|----------------|-----|
| Response latency | User experience |
| Token usage | Cost control |
| Error rates | System health |
| Output quality | User satisfaction |
| Prompt injection attempts | Security |

### For RAG Systems

| What to Monitor | Why |
|----------------|-----|
| Retrieval relevance | Answer accuracy |
| Context truncation | Missing information |
| Hallucination rates | Factuality |
| Citation accuracy | Trustworthiness |

## Model and Tool Telemetry

Allure-style test evidence and delivery metrics are not the same as model or tool telemetry. Model telemetry records how an inference ran: provider, model and version, correlation IDs, input/output or template hashes, token usage, latency, finish reason, retries, fallbacks, safety result, and estimated cost.

Tool telemetry records what the agent did outside the model: tool name and version, call sequence, redacted arguments, target resource, authorization decision, human approval, result status, latency, retries, errors, and side-effect identifiers such as commits, tickets, database transactions, or deployments.

Agent telemetry joins these events into a trace: planner and subagent transitions, retrieval sources, memory reads/writes, generated artifacts, file changes, approvals, escalations, and final outcome. Do not store raw secrets or unrestricted prompts by default; use redaction, hashing, access control, retention limits, and sampling.

The [OpenTelemetry GenAI Semantic Conventions](https://github.com/open-telemetry/semantic-conventions-genai) provide a vendor-neutral starting point for GenAI spans, metrics, events, and MCP instrumentation. For the distinction between runtime telemetry, downstream validation, and model evals, see [AI QA Evidence Layer: Validation, Evals, Guardrails, and Telemetry](ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md).

## 8 Steps to Implement ODD

1. **Audit** — map microservices, key flows
2. **Define metrics** — logs, metrics, traces
3. **Instrument code** — set up loggers, APM
4. **Choose tools** — align with needs/budget
5. **Analyze data** — look for patterns
6. **Create alerts** — threshold-based
7. **Iterate** — ODD is not "set and forget"
8. **Foster culture** — team-wide observability mindset

## Vibe-Coded Apps Need Monitoring Too

AI coding tools generate application code, NOT operational infrastructure:
- Won't set up Sentry
- Won't configure uptime alerts
- Won't create Grafana dashboards

**Setup cost:** Negligible (free tiers available)
**Setup time:** An afternoon
**Alternative:** Angry users, lost transactions, churn

## Key Quotes

> "Your vibe-coded app got you to launch. Monitoring is what keeps you running after launch."

> "The days when you could predict how your system would behave simply by reading lines of code are long, long gone."

> "LLMs might be the Trojan Horse that drags teams into modern best practices."

## Common Mistakes

1. **No monitoring** — discover problems from users
2. **Too many alerts** — alert fatigue
3. **No action on alerts** — cry wolf effect
4. **Monitoring but not observing** — data without insight
5. **Only reactive** — not proactive

## Related

- [[wiki/vibe-wipe-coding-guide]] — Monitoring for vibe-coded apps
- [[wiki/quality-characteristics]] — AI-specific quality attributes
- [[wiki/testing-strategies]] — Testing + observability together

## Sources

- raw/monitoring-vibe-coded-apps.md
- raw/llms-observability-driven-development.md
- raw/splunk-odd-explained.md
