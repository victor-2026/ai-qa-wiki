# NIST AI RMF 1.0 (AI 100-1, Jan 2023)

**Source:** NIST AI 100-1 (48pp). Raw: `raw/NIST.AI.100-1.pdf` (full text read 10.10). Status note (Brijesh): under revision — foundation, not final word. Successor watch: TEVV-Athlon draft (AI 200-2, 4 stages).

## Core: Govern / Map / Measure / Manage

- **Govern** (cross-cutting, infused everywhere): risk culture, policies, risk tolerance, roles, inventory + safe decommissioning (GOVERN 1.6/1.7), transparency. Senior leadership sets tone; documentation enhances review + accountability.
- **Map:** establish context to frame risks. Lifecycle actors lack full visibility into other parts; early purpose decisions alter behavior; deployment dynamics reshape impacts. MAP outputs feed Measure + Manage; MAP 3.5 = human-oversight processes defined and assessed.
- **Measure:** analyze, assess, benchmark, monitor risk (tools, metrics, red-teaming implied in subcategories).
- **Manage:** prioritize, respond, recover, decommission; decide appropriateness of the AI solution itself.

## Trustworthy characteristics (7; Valid & Reliable is the base)

Valid & Reliable (necessary condition) · Safe · Secure & Resilient · Accountable & Transparent (vertical — touches all) · Explainable & Interpretable · Privacy-Enhanced · Fair (bias managed).

## AI risks ≠ traditional SW risks (Appendix B)

Data-trained behavior, emergent capabilities, lifecycle-spanning actors, measurement difficulty — risk management differs in kind, not just degree.

## Human-AI interaction (Appendix C + Brijesh bridge)

Framework: roles, documented oversight processes, accountability for AI risk decisions, competence of overseers. Brijesh's 6-question test (who/when/info/understand/authority/stop-in-time) operationalizes it; APPROVE-button without evidence/authority/intervention = observation, not oversight. "Human oversight should itself be testable."

## QA interpretation

- **Map-before-Measure** is our relevance-gate + context-first doctrine (no measurement without framed risk).
- **Govern-as-cross-cutting** matches per-risk-tier (policy infused into every gate, not a separate gate).
- **Valid & Reliable as base** = our reliability floor: no trustworthiness claim stands on an unreliable system.
- **Decommissioning (GOVERN 1.7)** is the sunset half nobody tests — pairs with model-swap re-runs (scorecard discipline).
- **Actor separation best practice** (builders ≠ verifiers, Fig. 3) = examiner-author split, standards-stated.

## See also

- [[kenhuang-maestro-google-control-roadmap-2026]] — control mapping (MAESTRO/TRAIT&R)
- [[anthropic-demystifying-evals-agents-2026]] — Measure-layer method
- [[durability-curve-seven-checks-kit-2026]] — practitioner checks
- [[rotation-without-relevance-preseed-mutant-filtering-2026]] — relevance gate
