**Source:** [Splunk Blog](https://www.splunk.com/en_us/blog/learn/odd-observability-driven-development.html)
**Date:** 2023-07-17
**Author:** Kayly Lange

---

# Observability-Driven Development (ODD): 8 Steps

## Definition

ODD = using tools and hands-on developers to observe behavior and state of a system to get insights, especially patterns of weakness.

> "Observability means you can understand how your systems are working on the inside just by asking questions from the outside." — Charity Majors

## Why ODD Matters

| Reason | Description |
|--------|-------------|
| **Modern complexity** | Distributed systems, microservices — traditional methods inefficient |
| **Proactive solutions** | Identify issues before they impact users |
| **Fast resolution** | Real-time visibility → quicker identification |
| **Continuous improvement** | Culture of learning and iteration |
| **User focused** | Smoother UX, faster issue mitigation |
| **DevOps/SRE alignment** | 83% of IT leaders embrace DevOps — ODD is critical |

## 8 Steps to Implement ODD

### Step 1: Comprehensive System Audit
- Map out microservices
- Key user flows
- Important transactions/functions

### Step 2: Define Key Metrics
Three pillars of observability data:
- **Logs** — records of events
- **Metrics** — quantitative measurements
- **Traces** — records of single operation across system

### Step 3: Instrument Your Code
- Set up loggers
- Integrate metrics libraries
- Implement distributed tracing

Balance: comprehensive data vs. instrumentation overhead

### Step 4: Choose Observability Tools
- Log aggregators
- APM tools
- Distributed tracing systems

Align with: observability needs, system complexity, budget

### Step 5: Aggregate and Analyze Data
- Look for patterns, anomalies, bottlenecks
- ML can help parse large datasets

### Step 6: Create Alerts and Dashboards
- Alerts for potential issues (e.g., response time exceeds threshold)
- Dashboards for real-time metrics visualization

### Step 7: Iterate and Refine
- ODD is not "set and forget"
- Revisit instrumentation, alerts, metrics, dashboards as system evolves

### Step 8: Foster a Culture of Observability
- Train team to use observability tools
- Encourage regular dashboard checking
- Workshops and ongoing education

## Key Insight

> "As software grows more complex, ODD presents a profound solution in how it shifts our approach to development and maintenance."

## Related

- Honeycomb: LLMs Demand Observability-Driven Development
- Monitoring for Vibe-Coded Apps (Diffian)
- Hidden Costs of Vibe-Coded Apps
