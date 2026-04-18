# QA Topics - Comprehensive Guide

**Last Updated:** 2026-04-17  
**Coverage:** 12 categories, 50+ topics

---

## 1. AI in QA and Development

### AI-Driven Testing
- Test generation with LLMs
- Prompt engineering for QA
- AI as test oracle (LLM-as-judge)
- Synthetic data generation

### Agentic Development
- [[wiki/swe-tester-framework]] — SWE-Tester (confirmed!)
- [[wiki/mas-testing-framework]] — MAS-Testing (conceptual)
- [[wiki/agentic-patterns]] — Agentic engineering
- Autonomous test agents
- Multi-agent pipelines
- Self-healing tests

### Low-code/No-code
- codeless automation
- Visual test builders
- Configuration over code

### Vibe-coding
- AI-first development
- Spec-driven vs vibe-driven
- Hidden costs of AI-generated code

---

## 2. Infrastructure and Engineering

### Kubernetes + Docker
- Container orchestration
- Pod/deployment patterns
- Auto-scaling
- Service mesh basics

### Microservices Testing
- Contract testing (Pact)
- Service isolation
- Integration testing strategies

### Monitoring and Alerting
- Prometheus + Grafana
- Log aggregation
- SLO/SLI definitions

---

## 3. Culture and Education

### Empathy in Testing
- User perspective
- Accessibility testing
- Emotional journey mapping

### Process Control
- Shift-left testing
- CI/CD integration
- Quality gates

### Critical Thinking
- Risk-based testing
- Exploratory testing techniques

---

## 4. Future of QA Profession

### Evolving Roles
- QA → SDET → QA Engineer
- Test automation → AI-augmented
- Manual → strategic

### Skills Matrix
| Skill | Manual | Automated | AI-augmented |
|-------|--------|-----------|---------------|
| Execution | 80% | 20% | 5% |
| Analysis | 20% | 80% | 95% |

---

## 5. Current Trends

### Agentic AI
- Autonomous test creation
- Self-healing locators
- Dynamic test generation

### Quality at Speed
- Fast feedback loops
- Progressive delivery
- Canary deployments

---

## 6. Applications

### Test Case Generation
- Property-based testing (PBT)
- Metamorphic testing
- Combinatorial testing

### Code Quality
- Static analysis
- Linting automation
- Security scanning

---

## 7. Challenges

### AI Challenges
- Hallucinations: AI generates wrong tests
- Data leaks: NDA exposure via prompts
- High training costs
- Lack of context

### Testing Challenges
- Flaky tests
- Test data management
- Environment parity

---

## 8. System Reliability (SRE)

### Fault Tolerance
- Circuit breakers
- Retry patterns
- Fallback strategies

### Incident Response
- War-room protocols
- Post-mortem culture
- MTTR optimization

### Monitoring
- SLI/SLO definitions
- Error budgets
- Alerts threshold tuning

---

## 9. Data Architecture

### DWH (Vertica/ClickHouse)
- Columnar storage
- Partitioning strategies
- Data lake integration

### Clickstream Events
- Event collection
- Schema evolution
- Analytics pipeline

---

## 10. Highload Challenges

### Scaling Strategies
- Horizontal scaling
- Read replicas
- Write optimization

### Rate-limiting
- Token bucket
- Sliding window
- API quota management

### Caching Strategies
- Multi-level (L1-L3)
- Cache invalidation
- CDN patterns

---

## 11. Community

### Knowledge Sharing
- Internal tech talks
- Cross-team mentorship
- Open source contribution

### Best Practices
- Code reviews for tests
- Documentation culture
- Test automation templates

---

## 12. Quality Assurance Architect

### Architecture Patterns
- Test pyramid
- Testing quadrants
- Quality gates design

### Risk Assessment
- Impact analysis
- Prioritization matrices
- Coverage metrics

---

## Quick Reference

```
                     ┌─────────────────────────────────────┐
                     │      QA PROFESSION EVOLUTION         │
                     └─────────────────────────────────────┘
                                     │
          ┌──────────────┬──────────────┼──────────────┬──────────────┐
          ▼             ▼            ▼            ▼            ▼
    ┌──────────┐ ┌─────────┐ ┌──────────┐ ┌──────────┐ ┌─────────┐
    │ Manual   │ │  Test   │ │  AI-     │ │  Agentic │ │  QA     │
    │  QA     │ │Auto-    │ │augmented │ │  -dev   │ │Architect│
    └──────────┘ └─────────┘ └──────────┘ └──────────┘ └─────────┘
          │             │            │            │            │
          ▼             ▼            ▼            ▼            ▼
    • Exploratory • Regression• Synthesis• Self-heal• Architecture
    • Usability  • API tests • Prompt   • Autonomy  • Risk-based
    • Ad-hoc    • E2E      • Gen      • Agents  • Quality
```

## Quick Reference (Terms)

Смотри полный глоссарий: [[wiki/ai-testing-glossary]]

---

## Related Wiki Topics

- [[wiki/testing-strategies]] — Testing approaches
- [[wiki/testing-stability]] — Anti-flakiness
- [[wiki/agentic-patterns]] — Agentic engineering
- [[wiki/quality-characteristics]] — Quality metrics
- [[wiki/monitoring-observability]] — SRE basics

## Sources

- Session learnings
- Industry trends 2025-2026
- Best practices from projects