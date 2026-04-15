# ML Functional Performance Metrics

**Last Updated:** 2025-04-15
**Sources:** User research + industry best practices

---

## Three Levels of ML Metrics

| Level | Focus | Audience |
|-------|-------|----------|
| **Model Performance** | Mathematical accuracy | Data Scientists |
| **System Performance** | MLOps health | Engineers |
| **Business Metrics** | Revenue & Impact | Executives |

---

## 1. Model Performance (Mathematical Level)

Classic metrics showing how well algorithm works "in vacuum".

### Classification Metrics

| Metric | Formula | When to Use |
|--------|---------|-------------|
| **Precision** | TP / (TP + FP) | High cost of False Positive (e.g., banning users) |
| **Recall** | TP / (TP + FN) | Need to find all positives (e.g., anomaly detection) |
| **F1-Score** | 2 × (P × R) / (P + R) | Balanced view for imbalanced data |
| **ROC-AUC** | Area under ROC curve | Overall separability regardless of threshold |

### Confusion Matrix

|  | Predicted Positive | Predicted Negative |
|--|-------------------|-------------------|
| **Actual Positive** | TP (True Positive) | FN (False Negative) |
| **Actual Negative** | FP (False Positive) | TN (True Negative) |

### Regression Metrics

| Metric | Description | Use Case |
|--------|-------------|----------|
| **MAE** | Mean Absolute Error | Same units as target, outlier-robust |
| **RMSE** | Root Mean Square Error | Penalizes large errors more |
| **MAPE** | Mean Absolute Percentage Error | Normalized for comparison |
| **R²** | Coefficient of Determination | How much variance is explained |

### Clustering Metrics

| Metric | Description |
|--------|-------------|
| **Silhouette Score** | How similar objects are to own cluster vs others |
| **Davies-Bouldin Index** | Lower = better clustering |
| **Adjusted Rand Index** | Compares clustering to ground truth |

### Limitations of ML Metrics

1. **Metrics ≠ Business Value** — 99% accuracy on spam detection may be useless if false positives block real emails
2. **Single metric insufficient** — Need multi-dimensional evaluation
3. **Goodhart's Law** — When a measure becomes a target, it ceases to be a good measure
4. **Proxy metrics fail** — Optimizing for proxy (clicks) may hurt real goal (satisfaction)

---

## 2. System Performance (MLOps Level)

Critical for operating 4500+ microservices. Shows "health" of ML system.

| Metric | Description | SLA Target |
|--------|-------------|------------|
| **Model Drift** | Distribution shift from training data | Monitor daily |
| **Inference Latency** | Time from request to prediction | < 100ms for real-time |
| **Training Time** | Duration of model retraining | Track for capacity planning |
| **Throughput (RPS)** | Predictions per second | Match expected load |
| **Model Size** | MB/GB of model | Affects deployment feasibility |
| **Memory Usage** | RAM/GPU consumption | Cost optimization |

### Drift Detection

| Type | What Changes | Detection |
|------|--------------|-----------|
| **Data Drift** | Input distribution | Population Stability Index (PSI) |
| **Concept Drift** | Relationship X→Y | Performance drop monitoring |
| **Feature Drift** | Individual feature distribution | Statistical tests per feature |

---

## 3. Product & Business Metrics

Most important for defending project to executives. Model can have 99% accuracy but not generate revenue.

| Metric | Description | Why It Matters |
|--------|-------------|----------------|
| **CTR** | Click-through rate on recommendations | Engagement proxy |
| **Conversion Rate** | Recommendations → action | Direct business impact |
| **Revenue per User** | Financial effect of ML | Executive reporting |
| **Fairness/Bias** | Non-discrimination in output | Legal/compliance risk |
| **Customer Lifetime Value** | Long-term user value from ML | Strategic impact |
| **Churn Rate** | User retention from better recommendations | Loyalty metric |

---

## DORA Metrics for ML Teams

Special considerations when applying DORA to ML teams:

| DORA Metric | ML-Specific Nuance |
|------------|-------------------|
| **Lead Time for Changes** | Includes Data Pipeline → not just code |
| **Deployment Frequency** | Model retraining cycles |
| **Change Failure Rate** | Model regression (accuracy drop) ≠ just 500 errors |
| **Time to Restore** | Rollback model vs rollback code |

### ML Failure Modes

- **Model Regression** — Accuracy drops after new deployment
- **Data Pipeline Break** — Training data becomes corrupted
- **Feature Drift** — Input distribution shifts
- **Concept Drift** — X→Y relationship changes over time

---

## Selecting Metrics

### Decision Framework

```
1. Start with business goal
   ↓
2. Map to product metric
   ↓
3. Choose proxy ML metric
   ↓
4. Validate proxy correlates with product metric
   ↓
5. Monitor both
```

### Common Mistakes

| Mistake | Why It Happens | Solution |
|---------|---------------|----------|
| Optimizing accuracy on imbalanced data | Easier to measure | Use F1, AUC |
| Ignoring latency | Focus only on accuracy | Set SLA, monitor P99 |
| No baseline | "Perfect" accuracy | Compare to random/heuristic |
| Metric gaming | Goodhart's Law | Multi-metric guardrails |

---

## Related

- [[wiki/istqb/testing-ai-systems]] — Test levels for AI
- [[wiki/ai-testing-metrics]] — Ragas, TrickCatcher metrics
- [[wiki/quality-characteristics]] — AI-specific quality

## Resources

- Google ML Crash Course: Classification Metrics
- Chip Huyen "Designing Machine Learning Systems"
- Fiddler AI / Arize: Model Monitoring blogs
- Arize: ML Observability

## Sources

- User research on ML metrics evolution
- DORA principles for ML teams
- Industry best practices for 4500+ microservices
