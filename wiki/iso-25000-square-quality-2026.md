---
title: "ISO/IEC 25000 (SQuaRE) — Software Quality Standards"
type: article
updated: "2026-08-17"
tags: [evals, compliance]
---

# ISO/IEC 25000 (SQuaRE) — Software Quality Standards

## Overview

ISO/IEC 25000 (SQuaRE — Software product Quality Requirements and Evaluation) — международная система стандартов для оценки и обеспечения качества ПО и информационных систем. Стандартизирует весь жизненный цикл: от требований к качеству до методов измерения и тестирования.

## Core Model: ISO/IEC 25010

Ядро серии — модель качества, разделённая на две группы:

### Product Quality (8 characteristics)

| Characteristic | Sub-characteristics | QA Application |
|---------------|-------------------|----------------|
| **Functional Suitability** | Completeness, correctness, appropriateness | Functional testing, acceptance criteria, requirement traceability |
| **Performance Efficiency** | Time behaviour, resource utilization, capacity | Load testing, profiling, stress testing |
| **Compatibility** | Co-existence, interoperability | Integration testing, cross-platform testing |
| **Usability** | Learnability, operability, accessibility, user error protection | UX testing, accessibility audits |
| **Reliability** | Maturity, availability, fault tolerance, recoverability | Resilience testing, chaos engineering, failover tests |
| **Security** | Confidentiality, integrity, non-repudiation, accountability, authenticity | SAST/DAST, penetration testing, auth testing |
| **Maintainability** | Modularity, analyzability, modifiability, testability | Code review, static analysis, tech debt tracking |
| **Portability** | Adaptability, installability, replaceability | Cross-platform testing, deployment testing |

В версии 2023 года два последних переименованы: Portability → **Flexibility**, добавлена **Safety**.

### Quality in Use

Измеряет успех взаимодействия реального пользователя:
- Effectiveness, efficiency, satisfaction
- Freedom from risk (health, safety, environment)
- Context coverage (completeness, flexibility)

## Other SQuaRE Standards

| Standard | Purpose |
|----------|---------|
| **ISO/IEC 25020** | Quality measure framework — how to define measures |
| **ISO/IEC 25023** | Quality measures for product quality (quantitative formulas) |
| **ISO/IEC 25030** | Quality requirements framework — how to specify quality in TOR |
| **ISO/IEC 25040** | Quality evaluation framework — process for independent evaluators |
| **ISO/IEC 25045** | Evaluation module for recoverability |

## QA Implications

### Engineering Controls for 25010 Characteristics

| Characteristic | Engineering Controls |
|---------------|-------------------|
| Reliability | Automated tests, resilience testing, production monitoring, error budgets |
| Security | SCA, SAST, DAST, secret detection, vulnerability scanning |
| Maintainability | Static analysis, code review, linting, complexity checks, testability |
| Functional Suitability | Requirements validation, functional tests, acceptance tests |
| Compatibility | Integration tests, dependency management, interoperability tests |
| Usability | UX testing, accessibility evaluation, user feedback loops |
| Performance | Load testing, profiling, capacity planning |

### How to Implement

1. **Define quality objectives** aligned with business goals
2. **Gap analysis** of current processes vs SQuaRE
3. **Establish metrics** — KPIs for each characteristic
4. **Conduct evaluations** using SQuaRE guidelines
5. **Continuous monitoring** — treat as ongoing process

## SQuaRE vs Other Standards

| Standard | Focus | Relation |
|----------|-------|----------|
| **ISO 9126** | Predecessor | Replaced by 25010 |
| **ISO 9001** | Quality management | Organizational, not software-specific |
| **ISO 27001** | Information security | Overlaps on Security characteristic |
| **TMMi** | Test maturity | SQuaRE = what to test, TMMi = how mature is testing |

## Practical Value

- **For QA engineers**: checklist for what to test across all quality dimensions
- **For test leads**: framework for test strategy (covers functional + non-functional)
- **For managers**: objective criteria for acceptance, measurable quality gates
- **For auditors**: structured evaluation methodology (25040/25045)

## References

- ISO/IEC 25010:2023 — Systems and software Quality Requirements and Evaluation (SQuaRE)
- ISO/IEC 25023 — Quality measures for product quality
- ISO/IEC 25030 — Quality requirements framework
- ISO/IEC 25040 — Quality evaluation framework
- Codacy Blog: "An Exploration of the ISO/IEC 25010 Software Quality Model" (2026)
- arc42 quality model — ISO/IEC 25010 reference








<!-- backlinks-start -->
### Backlinks
- [Iso 14971 Risk Management 2026](wiki/iso-14971-risk-management-2026.md)
<!-- backlinks-end -->
