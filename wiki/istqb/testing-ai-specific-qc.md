# Testing AI-Specific Quality Characteristics

**Last Updated:** 2025-04-15
**Sources:** Industry trends 2026, ISO standards, QE practices

---

## From QA to Quality Engineering (QE)

| Traditional QA | AI-Specific QC |
|---------------|----------------|
| Processes | Artifacts (data, models, agent responses) |
| Pre-release testing | Continuous monitoring |
| Deterministic assertions | Probabilistic/fuzzy validation |
| Code coverage | Behavior coverage |

**2026 Paradigm Shift:** Self-Healing Automation — AI writes and maintains its own tests.

---

## 1. Runtime QC (Control "On the Fly")

Unlike traditional software, AI services produce different results on identical queries.

### Prompt Regression Suites

Test sets verifying that model responses haven't degraded after prompt or LLM version update.

| What to Test | How |
|--------------|-----|
| Response quality trends | Automated scoring over time |
| Hallucination rate | Cross-reference with known facts |
| Latency changes | P50/P95/P99 monitoring |
| Output format stability | Schema validation |

### Confidence & Correctness Trends

Monitoring model confidence. If average confidence drops → route to human review (Human-in-the-Loop).

```
High Confidence → Auto-approve
Low Confidence → Human review
Novel Input → Canary deployment
```

### Fuzzy/Probabilistic Assertions

Using AI tools to validate other AI responses:
- Semantic matching (not keyword search)
- Business rule compliance checking
- Contextual relevance scoring

---

## 2. Standards & Frameworks (Compliance & Governance)

Critical for enterprise-scale deployments.

### ISO/IEC 42001 (AIMS) — AI Management Systems

First international standard for AI management systems.

| Requirement | Purpose |
|------------|---------|
| Risk documentation | Link risks to control points |
| Impact assessments | Pre-deployment evaluation |
| Continuous monitoring | Ongoing compliance |
| Incident response | AI-specific failure handling |

### ISO/IEC 5259 — Data Quality for ML

Standards for data quality in machine learning:
- Completeness, accuracy, consistency
- Timeliness, accessibility
- Data lineage tracking

### Model Explainability (XAI)

Using SHAP, LIME for QC:
- Verify not just result, but decision logic
- Detect bias in feature attribution
- Audit trail for regulatory compliance

---

## 3. Shift-Right Strategy

Validate model behavior on live production data.

### Why Traditional Testing Fails for AI

| Problem | Reason |
|---------|--------|
| Infinite input space | Can't enumerate all possibilities |
| Non-deterministic outputs | Same input → different output |
| Context-dependent | Meaning changes with conversation |
| Emergent behaviors | New capabilities appear unexpectedly |

### Production Validation Techniques

| Technique | Description |
|----------|-------------|
| **Shadow Testing** | Run new model in parallel, compare outputs |
| **Canary Deployment** | 1-5% traffic to new model |
| **A/B Testing** | Compare business metrics |
| **Champion/Challenger** | Gradually replace champion model |
| **Phased Rollout** | Slow traffic increase with monitoring |

---

## 4. Testing Specific Quality Characteristics

### Testing Self-Learning Systems

Challenge: Model continuously learns, behavior changes.

**Approach:**
1. Establish performance baseline
2. Monitor for regression
3. Define acceptable drift threshold
4. Automated rollback if exceeded

### Testing Autonomous AI-Based Systems

Challenge: System makes decisions without human intervention.

**Key Tests:**
- Decision boundary verification
- Fail-safe behavior under uncertainty
- Escalation to human review
- Audit trail completeness

### Testing for Bias

| Type | Description | Test Method |
|------|-------------|-------------|
| **Algorithmic** | Flawed hyperparameters | Statistical parity tests |
| **Sample** | Non-representative training data | Demographic analysis |
| **Inappropriate** | Gender/race/economic bias | Fairness metrics |

**Metrics:** Equalized Odds, Demographic Parity, Counterfactual Fairness

### Testing Probabilistic/Non-Deterministic AI

Challenge: Traditional assert-based testing doesn't work.

**Approach:**
- Metamorphic testing (define relationships)
- Statistical assertions (within confidence interval)
- Distribution testing (output distribution matches expected)
- Ensemble voting (multiple runs, majority wins)

### Testing Complex AI Systems

Challenge: Multiple AI components interact.

**Approach:**
- Component-level isolation testing
- Integration testing with mocks
- End-to-end behavioral testing
- Chaos testing for resilience

### Testing XAI (Explainability)

Challenge: Verify that explanations are accurate and understandable.

**Tests:**
- Feature attribution sanity checks
- Counterfactual explanation validity
- Explanation stability (same input → similar explanation)
- Human-interpretability evaluation

---

## 5. Test Oracles for AI-Based Systems

An "oracle" determines if test passed or failed.

| Oracle Type | Use Case | Limitation |
|-------------|----------|------------|
| **Specification** | Clear rules exist | Often doesn't exist for AI |
| **Reference Implementation** | Golden model comparison | Expensive to maintain |
| **Metamorphic Relations** | Define input-output relationships | Requires domain knowledge |
| **Statistical** | Output distribution expected | May miss individual failures |
| **Human Judgment** | Subjective quality | Slow, inconsistent |
| **AI-as-Oracle** | LLM validates LLM | Risk of correlated errors |

---

## 6. Test Objectives and Acceptance Criteria

### AI-Specific Acceptance Criteria

| Criterion | Measurement |
|-----------|-------------|
| Accuracy meets threshold | F1/AUC on test set |
| Fairness metrics within bounds | Demographic parity |
| Latency SLA | P99 < 100ms |
| Drift detection | PSI < 0.2 |
| Explainability coverage | > 95% of decisions explained |
| Hallucination rate | < 1% verified hallucinations |

### Documenting AI Components

For each AI component, document:

```
1. Purpose & scope
2. Training data (source, volume, date)
3. Model architecture
4. Performance metrics (baseline vs current)
5. Known limitations & edge cases
6. Monitoring plan
7. Update/retrain procedures
8. Fallback behavior
```

---

## 7. Tools 2026

| Tool | Purpose | Scale |
|------|---------|-------|
| **Arize** | ML Observability, drift detection | Enterprise |
| **Fiddler** | Model monitoring, explainability | Enterprise |
| **DeepUnit/Parasoft** | Auto-generate unit tests | Code |
| **Virtuoso/ACCELQ** | Low-code testing with NLP/CV | E2E |
| **Great Expectations** | Data quality validation | Pipeline |
| **Seldon/Alibi** | Model explainability | Deployment |

---

## Key Recommendations

1. **Standardize Prompt Ops & Model Versioning**
   - Treat prompts as code (version control, review, CI/CD)
   - Without versioning, no QC can identify cause of quality drop

2. **Separate AI QC as distinct stream**
   - Teams working on recommendations/search need dedicated QC
   - Different metrics than traditional software

3. **Build feedback loops**
   - Production signals → training data improvements
   - Human review → model updates

4. **Automate regression suites**
   - Prompt regression tests in CI/CD
   - Automated drift alerts

---

## Related

- [[wiki/istqb/ml-performance-metrics]] — Metrics for ML systems
- [[wiki/testing-strategies]] — Testing approaches
- [[wiki/monitoring-observability]] — Production monitoring

## Sources

- ISO/IEC 42001 (AIMS) Standard
- ISO/IEC 5259 Data Quality Standard
- Chip Huyen "Designing Machine Learning Systems"
- Industry trends 2026 for AI QC
