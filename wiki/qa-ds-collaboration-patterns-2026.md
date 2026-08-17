---
title: "QA + Data Science Collaboration Patterns"
type: article
updated: "2026-08-17"
tags: [qa]
---

# QA + Data Science Collaboration Patterns

## Summary

QA and Data Science teams operate with different mindsets: DS optimizes for model quality (accuracy, AUC), QA for system reliability (defects, coverage, risk). Effective collaboration bridges this gap through shared processes, metrics, and ownership models.

## Ownership Model

| Activity | Owner | QA Role |
|----------|-------|---------|
| Model development | DS | — |
| Property-based tests | QA + DS | Write and maintain PBT |
| Experiment design | PM + DS | Validate guard-rails and metrics |
| Golden dataset | QA | Curate, maintain, automate runs |
| Drift monitoring | DS + Infra | Setup alerts, thresholds, dashboards |
| Release decision | PM + QA + DS | QA provides risk assessment, DS provides model readiness |
| Quality dashboard | QA Lead | Unified view of QA + DS + product metrics |

## When QA Should Engage

| Phase | What QA Does |
|-------|-------------|
| **Before experiment** | Review hypotheses, define success criteria, design evaluation harness |
| **During experiment** | Monitor data quality, validate experiment setup, track guard-rail metrics |
| **Pre-release** | Golden dataset regression, bias check, risk register, release readiness assessment |
| **Post-release** | Monitor drift, track false positives/negatives, feed findings back to retrain cycle |

## Common Friction Points

| Friction | Root Cause | Resolution |
|----------|-----------|------------|
| "DS says model is good, QA says not ready" | No shared release criteria | Define joint go/no-go gates upfront |
| "QA doesn't understand ML metrics" | Different vocabularies | QA learns key ML metrics (precision, recall, F1, PSI), DS explains business impact |
| "DS experiments without QA" | QA seen as bottleneck | Shift-left: embed QA in experiment design, not just release validation |
| "No one owns data quality" | Gap between DS and engineering | QA steps in as data quality guardian for test/training datasets |
| "Model passes metrics but fails in production" | Offline-online gap | Add golden dataset + A/B gate as mandatory pre-release steps |

## Shared Artifacts

- **Joint release readiness checklist** — gates that both QA and DS must sign off
- **Unified dashboard** — QA metrics (defect escape rate, coverage) + DS metrics (drift, accuracy, PSI) in one view
- **Risk register** — known limitations, confidence levels, edge cases for each model version
- **Incident post-mortem** — joint QA+DS RCA for production issues involving AI/ML components

## Regular Cadence

| Meeting | Frequency | Participants | Agenda |
|---------|-----------|-------------|--------|
| Model review | Per release | QA + DS | Metrics, regression, risk |
| Experiment sync | Weekly | QA + DS + PM | Pipeline, blockers, results |
| Quality review | Monthly | All | Trends, incidents, process improvements |

## Communication Principles

- **Translate metrics to business impact:** "4% false positives" → "1 in 25 users sees incorrect output"
- **Acknowledge uncertainty:** For probabilistic systems, communicate confidence levels, not binary pass/fail
- **Document assumptions:** Every model version ships with documented known limitations, edge cases not covered, and confidence thresholds
- **Joint sign-off:** Release decision requires both QA risk assessment and DS model readiness

## Related

- `wiki/ds-ml-quality-testing-2026.md` — 4-level testing model
- `wiki/ai-testing-metrics.md` — Metrics for AI systems
- `wiki/quality-characteristics.md` — AI quality attributes (ISO 25010)
