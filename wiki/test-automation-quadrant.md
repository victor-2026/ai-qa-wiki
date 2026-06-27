# The Test Automation Quadrant

**Author:** Bas Dijkstra
**Source:** [ontestautomation.com](https://www.ontestautomation.com/the-test-automation-quadrant/)
**Date:** December 11, 2024

---

## Overview

A different way to classify automated tests using two axes: **information value** and **efficiency**.

---

## Why a Different Model?

The test automation pyramid misses:

1. **Value** — Pyramid doesn't represent the *value* of a test
2. **Definitions** — "What is a unit test?" has 6+ different answers
3. **Ratios** — Nobody cares about ratios (pyramid, hourglass, ice cream cone)

---

## The Quadrant

```
        HIGH VALUE          LOW VALUE
           │                    │
FAST    ────────────────────────►
           │      top right     │
           │  valuable+fast    │  fast but low value
SPEED/    │                   │
EFFICIENCY │  top left        │  top left
           │  fast+val珍贵的   │  fast+low value
           │                   │
           ▼                   ▼
SLOW    ────────────────────────
           │                  bottom left
           │   valuable      │  slow + low value
           │   but slow      │  (DELETE THESE!)
           │                   │
           │                  bottom right
           │   valuable     │  slow + high value
           │   but slow     │  (keep, optimize later)
```

---

## Quadrants Summary

| Quadrant | What to Do |
|----------|------------|
| **Top Right** ✅ | Keep — valuable + efficient |
| **Top Left** | Lower priority, only if time |
| **Bottom Right** | Keep — valuable (but optimize) |
| **Bottom Left** ❌ | DELETE — no value, slow |

---

## Key Insights

1. **Value = Risk** — High-risk problems = high-value information
2. **Scope doesn't matter** — E2E can be efficient, unit tests can be slow
3. **Reliability matters** — Unreliable tests = no value

---

## How to Use

1. **Assess** — Place tests in quadrants
2. **Move** — Improve:
   - **Up** → Make more efficient
   - **Right** → Make info more valuable
3. **Delete** — Bottom left tests

---

## Examples to Improve

### Move Up (More Efficient)
- Break down E2E tests into smaller focused tests
- Use mocks instead of real dependencies
- Refactor hard-to-test code

### Move Right (More Valuable)
- Fix flaky tests
- Use mutation testing to find false negatives
- Improve reporting

---

## Related

- [[Risk-Based-Testing-Skill]] — CodeScene skill for risk-based testing
- [[wiki/testing-strategies]] — Testing strategies
- [[wiki/ai-testing-frameworks-complete]] — AI testing approaches

---

*Extracted from Bas Dijkstra's blog via groq_qa.py*
*RSS: https://www.ontestautomation.com/feed.xml*