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

## 2026-09-28 — event-sourcing recipe + HUGSED (W5 intake from feed paste, paste only ⚠️)

Post "How I do event sourcing in 2026, the easy way" (4h): SQLite/Postgres/FoundationDB ACID + read-your-writes + views-replay on startup + HUGSED stack (HTMX + Unix + Go + SQLite + Event-Driven). Tagline on profile: "Founder @ BitGN | Verifying agents" — lane adjacency confirmed.
QA-relevant points: (5) transient events for non-DB systems used in Given-When-Then specs; (6) full-stack flattening — specs setup events → HTTP calls → assert UI semantic anchors. Deterministic fixtures + semantic assertions, same family as QA Wolf `toSatisfy` and our fixture patterns. No card opened (digest source + wiki-covered; Following, no thread).
