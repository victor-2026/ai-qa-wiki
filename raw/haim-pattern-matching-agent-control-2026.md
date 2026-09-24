# Haim Michael: AI Agent Control Logic with Pattern Matching (AI Agents Conference, 2026-04-27)

**Author:** Haim Michael (Founder & CEO Zindell Technologies; life michael blog; Kiro day-1 user; meetup organizer). 1st connection.
**Sources:** talk post https://lifemichael.com/en/reflections-from-ai-agents-conference-my-talk-on-ai-agent-systems-and-control-logic/ (video https://www.youtube.com/watch?v=U2ko01b4jow, slides on SlideShare); follow-up same thesis at Conf42 AI Agents 2026-09-24 "Orchestrating AI Agents with Pattern Matching" (materials pending, https://www.conf42.com/agents2026); earlier variant JDConf 2026-04-09 (Java pattern matching).
**Context:** Deterministic control layer over probabilistic agents via Java pattern matching on sealed interfaces (LangChain4j AiServices). Directly our control-plane/guardrail territory: typed verdicts, reviewer score gates, bounded retries, judge selection. Practitioner code, not theory - all four orchestrators package-visible for direct unit testing with mocked agents.
**Fetched:** 2026-09-24 via webfetch, substance below (site nav stripped; Java code condensed to signatures + logic).

---

## Thesis

Agents produce probabilistic outputs; the orchestrating system must not be unpredictable. Pattern matching on sealed types gives structure, predictability, maintainability: routing, delegation, retries, fallbacks, termination as exhaustive, compiler-checked decision logic.

## Pattern 1 - Pipeline orchestrator (Planner → Coder → Reviewer)

`step()` switches on sealed AgentMessage (PlanRequest/CodeRequest/ReviewRequest/FinalResult); main loop runs until FinalResult, logs agent per step, try/catch per delegation. Exhaustiveness: every message type handled, no silent fallthrough.

## Pattern 2 - Branching delegation (Router)

RouterAgent classifies input to enum (LangChain4j can't deserialize sealed interfaces - enum bridge documented as limitation workaround); orchestrator maps enum → sealed TaskClassification (TranslateTask/SummarizeTask) and dispatches. Type-based routing replaces fragile if-chains.

## Pattern 3 - Retry / feedback loop (MOST RELEVANT FOR US)

Bounded loop (MAX_ATTEMPTS = 3): coder codes → reviewer returns Approved(code, score) | Rejected(feedback); guarded pattern `Approved a when a.score() > 7` (high-score fast path, plain Approved fallback); rejection re-invokes coder WITH feedback appended; exhaustion returns last attempt with WARNING log. This is a verdict-gate in miniature: score threshold + feedback routing + bounded cost + explicit give-up signal.

## Pattern 4 - Fan-out / fan-in with JudgeAgent

Two solvers on virtual threads (StructuredTaskScope), JudgeAgent picks winner with reason (PickedA/PickedB sealed JudgeVerdict); selection logic pure and separately testable. Parallel-agent verdict pattern.

## Use for us

- Retry-loop shape (score gate + feedback + bound + give-up log) = template for verdict-gate loop design; guarded-pattern idiom maps to per-risk-tier thresholds.
- Sealed-verdict types (AgentResult Answer/Clarification/Error; JudgeVerdict PickedA/PickedB) = typed-verdict precedent for our evidence artifacts.
- Testability note (package-visible orchestrators, mocked agents) = same testability demand we place on verdict tooling.
- Enum-bridge limitation = honest engineering constraint worth remembering when designing typed handoffs.
- Cross-links: CIGE guardrails (control layer), AgentSpec (runtime enforcement), Qodo examiner pieces, judges-agree (judge dependence applies to his JudgeAgent too - single judge, no diversity).
- Watch: Conf42 2026-09-24 talk materials (video/slides/post) when published on lifemichael.com/en/talks/.
