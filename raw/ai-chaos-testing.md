**Source:** [Qase Blog](https://qase.io/blog/ai-for-chaos-testing/)
**Date:** 2024-06-03
**Author:** Vitaly Sharovatov

---

# How to Leverage AI for Chaos Testing

## Why Testing Is Limited

**Hardware isn't fully deterministic:**
- Temperature, power fluctuations
- Clock speed variations
- Network delays

**Software isn't fully deterministic:**
- OS scheduler determines process/thread order
- Garbage collectors run unpredictably
- Multithreading introduces execution variability
- I/O has variable latency

**Humans can't predict all user behaviors.**

> "Functional specifications are incomplete; they do not fully characterize the behavior of the system for all possible inputs."

## What Chaos Testing Does

Chaos testing introduces **unexpected events** to assess system behavior.

Instead of: "Does implementation match specification?"
We ask: "Does everything seem to be working properly?"

## AI's Role in Chaos Testing

| Step | AI Can Help? | Human Should Do? |
|------|--------------|-----------------|
| 1. Generate hypotheses | ✅ Yes | Filter ideas |
| 2. Plan chaos scenarios | ✅ Yes | Review plans |
| 3. Review & approve | ❌ | ✅ Yes |
| 4. Execute & observe | ❌ | ✅ Yes |

## Why AI Works for Step 1

1. **Good at analyzing graphs** — service architecture diagrams
2. **Trained on huge dataset** — provides more diversity than humans
3. **No context blindness** — not influenced by prior knowledge
4. **Hallucinations are useful** — provides diverse options to filter

## Prompt Example

```
Given the graph of services in the picture I uploaded, 
please come up with all the potential ways to perform 
chaos testing for each link of the graph. Please consider 
at least these ways where it makes sense:
- Latency injection
- Random server outages
- Resource exhaustion
- Simulated DDoS attacks
- Database failures
- Dependency failures
- Disk space exhaustion
```

## Chaos Testing Methods by Component

### Network (AWS VPC)
- Latency injection
- Random server outages
- Bandwidth exhaustion

### Ingress Controllers (Nginx)
- Latency in request routing
- Terminate controllers
- DDoS simulation
- Resource exhaustion

### Application Layer (Services)
- Service communication latency
- Individual service outages
- CPU/memory/disk exhaustion
- Disable dependencies (e.g., auth)

### Database Layer
- Unavailability, slow queries, corruption
- Redis crash, data loss
- Connection limit exhaustion
- Disk space exhaustion

### API Gateway
- Request processing latency
- Gateway downtime
- DDoS simulation
- CPU/memory exhaustion

### External Services (S3, SQS/SNS)
- Read/write latency
- Bucket/service unavailability
- Burst traffic
- Message duplication

## Tools for Chaos Testing

| Tool | Purpose |
|------|---------|
| Chaos Monkey | Random server outages |
| tc (Linux), Chaos Mesh | Latency injection |
| stress-ng, Chaos Toolkit | Resource exhaustion |
| Locust, Vegeta | DDoS simulation |
| Pumba | Container chaos |

## Key Principle

> "With this approach to chaos testing, one can save plenty of time and mental effort on generating the diverse set of testing scenarios while at the same time using the pros and cons of AI to the tester's benefit."

**AI generates diversity. Humans validate and execute.**

## Related

- Canary Testing
- ODD (Observability-Driven Development)
- Progressive Delivery
- Testing AI Systems Overview (ISTQB)
