# AI Risk Communication for QA Leaders

## Summary

Testing AI/ML systems is not just about metrics — it's about explaining uncertainty, limitations, and confidence levels to stakeholders in language they understand. This article provides patterns for communicating AI quality and risk to non-technical audiences.

## Why Traditional Pass/Fail Doesn't Work

Classical QA communicates in binary terms: test passed, test failed, bug found, bug fixed. AI/ML systems are probabilistic — there is no single "right answer." A model can be 94% accurate but still cause business-critical failures in 6% of cases.

The QA leader's job is to translate probabilistic quality into actionable business information.

## Communication Framework: Health / Risks / Actions

### 1. Health

The current state of quality at a glance.

| Metric | What It Tells Business |
|--------|----------------------|
| **Model accuracy: 94%** | System performs correctly in 94 of 100 cases |
| **False positive rate: 4%** | 4 of 100 alerts require manual review |
| **Drift: stable** | Model behavior hasn't changed since last release |
| **Coverage: 89%** | 89% of known scenarios are tested |

**Format:** Single dashboard number with a trend arrow (↑/→/↓), not a table.

### 2. Risks

Where the system can fail and what it means.

| Risk | Business Impact | Mitigation |
|------|----------------|------------|
| High false negatives in edge case X | Customer sees incorrect recommendation | Manual review for this scenario |
| Model degrades on unseen data distributions | Accuracy drops after peak season | Retrain scheduled, monitoring active |
| Bias in demographic group Y | Regulatory risk, reputational harm | Fairness testing added, data augmentation planned |

**Format:** Risk register with business impact, not technical metrics.

### 3. Actions

What we're doing about it.

- Short-term: monitoring, manual gates, known workarounds
- Medium-term: retrain cycle, additional data collection, evaluation harness improvements
- Long-term: process changes, tooling, team upskilling

## Translating Metrics for Business

| Instead of Saying | Say |
|------------------|-----|
| "F1 score is 0.87" | "The system is reliable in most cases, but we've identified 3 scenarios where it needs human oversight" |
| "False positive rate is 4%" | "1 in 25 outputs needs manual review — here are the patterns we see" |
| "PSI is 0.15" | "User behavior has shifted since training — we're monitoring and have a retrain scheduled" |
| "Accuracy is 94%" | "The system works well for standard cases; we have identified these edge cases" |
| "Drift detected" | "The model's environment has changed — we need to validate before the next release" |

## Release Decision Communication

**Don't say:** "The model passed all tests" or "The model failed."

**Say:** "The model meets release criteria for 6 of 8 gates. The two remaining risks are: (1) false positive rate for edge case X is above target, (2) drift detection shows minor shift in demographic Y. Both are documented with mitigation plans. Our recommendation is conditional go with monitoring."

## Common Anti-Patterns

| Anti-Pattern | Why It Fails | Better Approach |
|-------------|-------------|-----------------|
| Lead with accuracy | Hides failure modes | Lead with risks, use accuracy as context |
| Binary pass/fail for AI | Doesn't capture probabilistic nature | Use confidence levels with documented exceptions |
| Technical deep-dive | Stakeholders disengage | Start with business impact, offer depth on request |
| "The model is 94% accurate" | Ignores 6% failure impact | "94% accurate overall, but these 3 scenarios need attention" |

## Template: 5-Minute Quality Update

```
1. Overall: [green/yellow/red]
2. Key metric: [one number + trend]
3. Top risk: [one sentence business impact]
4. Action: [what we're doing about it]
5. Need from you: [decision needed]
```

## Related

- `wiki/ds-ml-quality-testing-2026.md` — 4-level testing model for ML
- `wiki/ai-testing-metrics.md` — Metrics for AI systems
- `wiki/quality-characteristics.md` — AI quality attributes
- `wiki/qa-ds-collaboration-patterns-2026.md` — How QA and DS work together
