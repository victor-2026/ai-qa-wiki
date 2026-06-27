# Self-Healing Tests — Why It's a Bad Idea

**Author:** Bas Dijkstra  
**Source:** [ontestautomation.com](https://www.ontestautomation.com/my-thoughts-on-self-healing-in-test-automation/)
**Date:** April 9, 2026

---

## Overview

Bas argues against "self-healing" test frameworks — they are band-aids hiding the real problem.

---

## The Problem

GUI tests fail because:
- Button text changes (Submit → Apply)
- ID attributes change after framework update
- Asynchronous processing in browsers

Tests fail to locate elements — even when behavior is correct.

---

## Why Self-Healing Is a Bad Idea

### What self-healing does:
- Uses "AI" to find alternative element locators
-consults training database
- Probabilistic — can make mistakes

### Bas's argument:

> "The biggest problem I have with 'self-healing' is that they are nothing more than band-aids, hiding the real problem that is underneath."

**The real problem:**
1. Who changed the button text?
2. Why didn't they update the test?
3. Or inform the team?
4. Or know about the framework update?

---

## Bas's Advice

> "Close the communication and collaboration gaps in our teams, instead of trying to patch them up with an algorithm."

**Instead of self-healing:**
- Update locators proactively
- Communicate changes in the team
- Use stable locators (data-testid)

---

## The Alternative

| Self-Healing | Better Approach |
|--------------|------------------|
| Hides problems | Exposes problems |
| Probabilistic | Deterministic |
| Band-aid | Fix root cause |

---

## Related

- [[Claude-Code-Tests-Part1]] — AI-written tests need mutation testing
- [[Test-Automation-Quadrant]] — Value vs Efficiency model
- [[wiki/testing-stability]] — Anti-flakiness strategies

---

*From RSS: https://www.ontestautomation.com/feed.xml*