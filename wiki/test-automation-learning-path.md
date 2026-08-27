---
title: "Test Automation Learning Path — E-book Summary"
type: article
updated: "2026-08-17"
tags: [qa]
---

# Test Automation Learning Path — E-book Summary

**Author:** Bas Dijkstra  
**Source:** [EuroSTAR Huddle](https://huddle.eurostarsoftwaretesting.com/resources/test-automation/a-test-automation-learning-path/)  
**File:** raw/Bas-Dijkstra-A-Test-Automation-Learning-Path-EuroSTAR-Huddle.pdf

---

## The 5 Pillars of Test Automation

| # | Pillar | What It Covers |
|---|--------|----------------|
| 1 | **Software Testing** | Testing fundamentals, QA mindset |
| 2 | **Software Development** | Programming, clean code |
| 3 | **Test Automation Strategy** | 5W1H, what/when/how to automate |
| 4 | **Test Automation Tools** | Frameworks, libraries |
| 5 | **Test Automation Engineering** | CI/CD, infrastructure |

---

## 1. Software Testing

**Why it matters:** Test automation supports testing — you need to know what good testing looks like.

**Key concepts:**
- Test design techniques (equivalence partitioning, boundary value analysis)
- Black-box vs white-box testing
- Test levels (unit, integration, system, acceptance)
- Heuristics and oracles

---

## 2. Software Development

**Focus:** Programming skills for test automation

**Key skills:**
- Clean code principles
- Design patterns (Page Object, Factory, Builder)
- Version control (Git)
- Debugging skills

**Languages for test automation:**
- Java (popular in enterprise)
- Python (fast growth)
- JavaScript/TypeScript (web)

---

## 3. Test Automation Strategy

### The 5W1H Method

| Question | Purpose |
|----------|----------|
| **Why** automate? | ROI, feedback speed |
| **What** to automate? | Risk-based selection |
| **Where** in the pyramid? | Unit/Integration/E2E |
| **When** to run? | CI/CD pipeline |
| **Who** writes tests? | Skills distribution |
| **How** to implement? | Tool selection |

### Pyramid for Automation

```
        /\
       /  \     E2E (few)
      /----\    Integration (some)
     /      \   Unit (many)
    ----------
```

---

## 4. Test Automation Tools

### Categories

| Category | Tools |
|---------|-------|
| **Web UI** | Playwright, Cypress, Selenium, WebdriverIO |
| **API** | REST Assured, Postman, SoapUI |
| **Mobile** | Appium, Espresso, XCUITest |
| **Unit** | JUnit, TestNG, pytest, NUnit |
| **BDD** | Cucumber, SpecFlow, Behave |
| **Visual** | Percy, Applitools, BackstopJS |

### Selection Criteria

- Community support
- Documentation quality
- Learning curve
- Integration with existing stack

---

## 5. Test Automation Engineering

### CI/CD Pipeline

**Stages:**
1. **Commit** — Unit tests
2. **Build** — Integration tests
3. **Deploy** — E2E tests
4. **Monitor** — Production metrics

### Infrastructure

- **Version Control** — Git, branching strategies
- **Containers** — Docker for consistent environments
- **Cloud** — AWS, GCP, Azure for scaling
- **Reporting** — Allure, Extent Reports

---

## Learning Path Recommendations

### Beginner (1-3 months)
1. Learn a programming language (Java or Python)
2. Understand testing fundamentals
3. Master one automation tool (Selenium or Playwright)
4. Build first simple test suite

### Intermediate (3-6 months)
1. Learn API testing (REST Assured)
2. Understand CI/CD pipelines
3. Learn version control (Git)
4. Build test framework from scratch

### Advanced (6-12 months)
1. Learn BDD frameworks (Cucumber)
2. Master containerization (Docker)
3. Learn cloud platforms
4. Build scalable test architecture

---

## Related

- [[Test-Automation-Quadrant]] — Value vs Efficiency
- [[Test-Automation-Fundamentals-Revisited]] — Updated for AI era
- [[wiki/testing-strategies]] — Testing strategies
- [[wiki/ai-testing-frameworks-complete]] — AI testing approaches

---

*E-book summary created from PDF via groq_qa.py*




<!-- backlinks-start -->
### Backlinks
- [Devqaexpert Qaeverestimport2000Cypresstests Confidencescore 2026 08 22](wiki/devqaexpert-qaeverestimport2000cypresstests-confidencescore-2026-08-22.md)
- [Devqaexpert Qaeverestmaintenancetax Intentresolvesatruntime 2026 08 22](wiki/devqaexpert-qaeverestmaintenancetax-intentresolvesatruntime-2026-08-22.md)
<!-- backlinks-end -->
