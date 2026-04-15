**Source:** [Qase Blog](https://qase.io/blog/canary-testing/)
**Date:** 2024-07-09
**Author:** Vitaly Sharovatov

---

# A Complete Guide to Canary Testing

## What is Canary Testing

Named after canaries in coal mines (sensitive to toxic gases), canary testing deploys new functionality to a **small subset of users** before full rollout to mitigate risk.

## The Process

### Step 1: Select Canary Group
- Small enough to limit risk
- Large enough for statistical significance
- **1-5%** of user base typical
- Without making users aware (Hawthorne effect)

### Step 2: Setup Environment
- Parallel environment with new release
- Route canary users via load balancer

### Step 3: Monitor
- Error rates, response times, latency
- CPU, memory, I/O utilization
- If issues detected → rollback

### Step 4: Evaluate & Rollout
- Meets benchmarks → full rollout
- Doubt → route more users to canary
- No issues → deploy to all, shut down canary

## Canary vs A/B Testing

| Aspect | Canary | A/B |
|--------|--------|-----|
| **Goal** | Stability, no critical issues | Which version performs better |
| **Focus** | Operational metrics | User behavior metrics |
| **Groups** | Small representative | Statistically representative |
| **Selection** | Non-random | Random, demographic balance |

## Canary vs Blue-Green

- **Blue-Green** — two identical environments, all-or-nothing switch
- **Canary** — same setup but **gradual** user routing

## Benefits

- Early warning system
- Issues affect only small group
- Real user feedback > pre-prod testing
- Quick rollback if needed
- Build confidence in release

## Challenges

### 1. Representative Group Selection
- Must include varied users, locations, devices
- Random selection might miss edge cases

### 2. Granular Monitoring
- General metrics might miss specific issues
- Add metrics specific to new release

### 3. Seamless Rollback
Two methods:
- **Feature flags** — IF conditions separating new/old code
- **Routing changes** — reroute traffic back to production

Rule: Use rerouting if it can be done quickly.

## When to Use

- Major architectural changes
- Core functionality overhauls
- New features for feedback
- **Any release** with proper investment

Examples:
- Google Chrome Canary builds
- Facebook: daily canary releases

## Real Example: WebSocket Chat Migration

Problem: XMLHttpRequest polling → WebSockets

Approach:
1. Selected 1-5% users from 10 countries
2. Two mainstream browsers only
3. Monitored: connection stability, message delivery, drop rate
4. Gradual rollout over 2 months
5. Removed old code completely

Result: Better responsiveness, improved user satisfaction

## Key Takeaway

> "Canary testing offers a balanced approach to innovation and reliability."

## Related

- Blue-Green Deployment
- A/B Testing
- Feature Flags
- ODD (Observability-Driven Development)
- Progressive Delivery
