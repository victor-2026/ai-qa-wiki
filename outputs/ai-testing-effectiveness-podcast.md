# AI Testing Effectiveness: What the Research Shows (2026)

## Podcast Outline

**Topic:** Measuring and improving AI testing effectiveness in enterprise
**Duration:** 25-30 min
**Audience:** QA leads, engineering managers, test automation engineers

---

## Segment 1: The Big Picture (5 min)

### Hook
- "Can AI actually test software better than humans? The answer is more nuanced than you think."

### Key Research Findings
- **PersonaTester** (FSE 2026): LLM agents improve testing by 117-126% with persona-based approach
- **c-CRAB benchmark**: Current code review agents solve only 40% of tasks
- **AI Code Debt study**: 24.2% of AI-introduced issues persist long-term in production

### Transition
"But before you replace your QA team, let's understand what actually works."

---

## Segment 2: What Works - Agentic Testing (7 min)

### Persona-Based Testing
- 100+ crashes, 11 functional bugs discovered
- Simulates diverse human behaviors via 3 dimensions:
  - Testing mindset
  - Exploration strategy
  - Interaction habits

### Multi-Agent Systems
- SWEAgent shows multi-agent > single agent
- Chain-of-Verification (ConVerTest):
  - +39% test validity
  - +28% coverage
  - +18% mutation scores

### Few-Shot Prompting
- Human-written examples best for coverage
- Combined similarity (problem + code) yields best prompts

### Practical Takeaway
"Start with persona prompts for GUI testing, use multi-agent for complex scenarios."

---

## Segment 3: The Hidden Cost - Technical Debt (5 min)

### The Numbers
- 304,362 AI-authored commits studied
- 484,606 distinct issues identified
- 89.1% are code smells
- Every AI assistant introduces issues in 15%+ of commits

### What This Means for QA
- AI-generated code needs MORE testing, not less
- 24% of issues survive to production
- Need stronger quality gates for AI-assisted development

### Quote
"Cheaper generation does not mean cheaper review" — GenAI Governance study

---

## Segment 4: Measuring Effectiveness (6 min)

### SPACE Framework (from Agile productivity study)
- **S**atisfaction — How do developers feel?
- **P**erformance — Outcomes delivered
- **A**ctivity — Volume of work
- **C**ommunication — Team collaboration
- **E**fficiency — Speed/effort ratio

### Key Insight
GenAI increases **value density** of work, not volume. Performance + efficiency up, activity flat.

### Metrics to Track
| Metric | What It Measures |
|--------|-------------------|
| F2P (Failures to Pass) | Bug discovery rate |
| Coverage | Code coverage from AI tests |
| Validity | Test quality without ground truth |
| Mutation Scores | Test effectiveness |
| SPACE composite | Multi-dimensional productivity |

---

## Segment 5: Industry Reality Check (5 min)

### Case Study: Logistics Company (Belgium)
- Production microservice, security-sensitive
- LLM-based test amplification practical
- Increased coverage, revealed anomalies

### REST API Testing
- 67% of sites have redundant API calls
- 67% missing cache headers
- Third-party overhead >20% on 72% of sites

### Education
- Prompt scaffolding critical for students
- Missing context = failed tests
- One-shot prompting insufficient

---

## Segment 6: Action Items & Recommendations (4 min)

### For QA Leads
1. Implement persona-based testing for GUI
2. Add technical debt monitoring for AI code
3. Use SPACE framework for productivity measurement

### For Engineers
1. Use few-shot prompting with human examples
2. Implement multi-stage verification (ConVerTest approach)
3. Track coverage + validity metrics

### Future Trends
- GenAI governance beyond banning (12 strategies)
- IDEs abstraction level changing
- More benchmarks coming (c-CRAB, TestExplora)

### Close
"The research is clear: AI testing works, but needs guardrails. Start small, measure results, iterate."

---

## Guest Suggestions

1. **Academic:** Shengcheng Yu (PersonaTester) or Fitash Ul Haq (ISTQB study)
2. **Industry:** Rafael Tomaz (Agile productivity study)
3. **Practical:** Author of REST API test amplification paper

---

## Show Notes / References

- [2603.24160] PersonaTester - FSE 2026
- [2603.23448] Code Review Agent Benchmark (c-CRAB)
- [2603.28592] AI Code Debt - Large-scale study
- [2603.26487] GenAI Governance OSS - 12 strategies
- [2602.13766] GenAI Agile Productivity - SPACE framework
- [2602.10522] ConVerTest - Verification without ground truth
- [2601.17903] REST API Test Amplification - Industry case

---

## Related Wiki Entries

- [[wiki/ai-testing-metrics]] — Metrics deep dive
- [[wiki/testing-strategies]] — Testing strategies
- [[wiki/agentic-patterns]] — Agent patterns
- [[wiki/vibe-wipe-coding-guide]] — AI-assisted development