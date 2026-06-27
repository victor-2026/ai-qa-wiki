# Rinat Abdullin (ЛЛМ Под Капотом) — LLM Engineering

## Profile
- **Role:** LLM engineer, benchmark creator, AI-native development thinker
- **Channel:** @llm_under_hood — "LLM под капотом"
- **Notable:** Creator of **BitGN** benchmark (used in PAC1 competition)

## Key Ideas

### BitGN Benchmark
- Blind prod benchmark (~104 tasks)
- Tests agent on realistic non-trivial scenarios: prompt injection, hidden conflicts, dirty data with randomization
- PAC1 competition: 3-winner system (Accuracy, Ultimate)

### BDD > SDD for AI-Native Development
- **Thesis:** SDD (Spec-Driven Development) produces dead specs — can't verify code matches without expensive audits
- **Solution:** BDD with Given-When-Then as AI-Native Harness
- Agents generate BDD scenarios from requirements, implement code, and harness stays executable
- Any violation = build error (not stale document)
- Prefers event-driven specs over Gherkin for 10k+ scale

### Harness Engineering (OpenAI)
- Specs must be verifiable (not just documents)
- Harness should validate, not just describe

## Relationship to our work
- Directly validates our BDD skill + executable spec approach
- BitGN benchmark shows what breaks agents in prod — applies to QA agent testing
- BDD-as-harness = next step for our test framework (beyond Cucumber/Gherkin)
- Event-driven specs at scale → relevant for enterprise test suites

## Last updated
2026-06-18 — initial profile
