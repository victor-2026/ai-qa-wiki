# AI Testing Metrics

**Last Updated:** 2025-04-15
**Sources:** raw/rag-evaluation-ragas, raw/trickcatcher, raw/ai-roi-regression-testing

---

## RAG Evaluation Metrics (Ragas)

### Core Metrics

| Metric | What It Measures | Ideal |
|--------|------------------|-------|
| **Answer Relevance** | Is response relevant to prompt? | High |
| **Faithfulness** | Is model faithful to context? | High |
| **Context Relevance** | Is retrieved context relevant? | High |

**Method:** LLM-as-judge (use another LLM to evaluate)

### Why Traditional Metrics Fail

- Bleu/Rouge — measure surface similarity, not meaning
- Exact match — too strict for generative AI
- Human evaluation — slow and expensive

## TrickCatcher Metrics

For detecting bugs in plausible programs:

| Metric | Score |
|--------|-------|
| **Precision** | 2.65× improvement vs baseline |
| **Recall** | 1.80× improvement vs baseline |
| **F1** | 41-51% (vs 25-36% baseline) |
| **False Positives** | 16× fewer |

## AI Regression Testing ROI

### Pre-release Metrics

| Metric | Description |
|--------|-------------|
| Test cycle time reduction | % decrease in execution time |
| Automation coverage | % of tests automated |
| Maintenance effort | Hours fixing broken scripts |

### Post-release Metrics

| Metric | Description |
|--------|-------------|
| Defect leakage | % of bugs found in production |
| Defect detection efficiency | % of total bugs caught in testing |
| Escaped defect severity | Severity mix of production bugs |

### Cumulative Metrics

| Metric | Description |
|--------|-------------|
| Cost of Quality (CoQ) | Total QA + production defect cost |
| Release velocity | Change in release frequency |
| QA labor hours saved | Time saved through AI |

### Proven Results

| Use Case | Improvement |
|----------|-------------|
| Test case generation | 1-3 hrs vs 16-24 hrs manually |
| Test prioritization (Launchable) | 50% machine hours, 90% faster |
| Coverage gap analysis | 10× improvement |
| Script maintenance | 70% time reduction |
| Flakiness detection | 22% → 0.6% flaky rate |
| Root cause analysis | 80% faster troubleshooting |
| Meta predictive selection | 60% fewer test runs |

## WebTestBench F1 Scores

| Model | F1 | Precision | Recall |
|-------|-----|-----------|--------|
| GPT-5.1 | 26.4% | 25.8% | 33.3% |
| Claude Sonnet 4.5 | 21.9% | 32.1% | 19.7% |
| Claude Opus 4.5 | 20.2% | 33.0% | 16.5% |

**Oracle (human checklist):** 46-49% F1

## Quality Dimensions (WebTestBench)

| Dimension | Difficulty | Example |
|-----------|------------|---------|
| Functionality | Easiest | Core features work |
| Constraint | Hard | Implicit logical rules |
| Content | Hardest | Visual + domain reasoning |

## Key Insight

> "Single metric is insufficient — use multiple evaluation metrics"

**For any AI system:**
1. Define objective metrics (automated)
2. Define subjective criteria (human judgment)
3. Track both over time
4. Watch for drift

## When Metrics Deceive

1. **Accuracy alone** — ignores false positives
2. **Speed alone** — ignores quality
3. **Coverage alone** — ignores relevance
4. **Human preference alone** — not scalable

**Balance:** Speed + Quality + Cost + Coverage

## Related

- [[wiki/testing-strategies]] — How to apply these metrics
- [[wiki/quality-characteristics]] — What to measure beyond accuracy
- [[wiki/agentic-patterns]] — Testing agentic workflows

## Sources

- raw/rag-evaluation-ragas.md
- raw/trickcatcher-bug-detection.md
- raw/ai-roi-regression-testing.md
- raw/webtestbench-ai-web-testing.md
