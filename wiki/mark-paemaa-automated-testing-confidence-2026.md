---
source: "mark-paemaa-automated-testing-confidence-2026.md"
ingested: "2026-09-01"
---

## Mark Paemaa - Automated Testing Isn't About Finding Bugs (Confidence)

**Summary**
Engineering Team Lead Mark Paemaa (2026-08-27, https://www.linkedin.com/pulse/automated-testing-isnt-finding-bugs-mark-paemaa-akphc/) reframes automated testing: real value is not bug hunting but confidence to change. Question is not "Did we find every bug?" but "How confident are we that we haven't broken something important?" As systems grow with integrations and business rules, confidence decays without good automation. Best teams see automation as engineering, not QA activity.

---

## Key Concepts

| Paemaa point | Essence | Maps to |
|--------------|---------|---------|
| **Confidence, not bugs** | Automation reduces uncertainty per release, not guarantee of zero bugs | Trust Scorecard / ship-confidence score; mutation sensitivity as confidence measure |
| **Engineering, not QA activity** | Developers get faster feedback, QA investigates risks vs re-running same cases, product gets predictable releases | DORA + shift-left; QA-as-supervisor (Article 27) |
| **Not everything** | Goal is not biggest suite, but automating areas that reduce risk and provide confidence | Risk-based testing; per-risk-tier gate; 0 of 10 positional vs meaningful coverage |
| **Trade-offs** | Some tests worth automating, others better explored by humans | Automation pyramid + exploratory; human review of findings |
| **Tests as production code** | Slow, unreliable suites are ignored because nobody trusts results - bad automation creates friction, good removes it | Flakiness quarantine, Self-Heals, Fragility Index; treat tests as code (clean, deterministic) |

---

## Our analysis (for Victor)

1. **Confidence = 1 - Risk.** Paemaa's "confidence to change" is exactly Victor's `Trust Scorecard` and `Quality Centre ship-confidence score`. Paemaa says confidence decays with complexity; the Scorecard measures that decay via Sensitivity (do we catch seeded defects?), Fragility (are selectors brittle?), Flakiness (do we trust the signal?).

2. **Finding vs confidence split.** Paemaa: "I've also learned automating everything is rarely the answer." This is Article 20's false discovery vs confidence: finding 5 bugs at 80% FDR hurts confidence, finding 1 true regression builds it. Gate must be on confidence, not count.

3. **Tests as production code = the fix for Paemaa's friction.** Slow/unreliable suites ignored by devs is the problem QAEverest's Time-Travel + quarantine + self-heals and Victor's mutation matrix address: treat automation with the same quality bar as production (deterministic, reviewable, evidence-backed).

4. **Supports Article 27 Guided QA Engineer.** "QA can spend more time investigating risks instead of repeatedly executing same test cases" - exactly the promotion Paemaa describes and Ng's loop engineering: agent/ automation handles checking, QA engineers handle risk investigation and trade-off decisions.

---

## Cross-links
- [QAEverest Verification 7.1.1 Trust Scorecard](../../Positions-CV-CL/company/pilots/DevQaExpert/index.md) — confidence as gate, not green tick
- [Ilya Kabanov - Hygiene vs AI Hype](wiki/ilya-kabanov-cybersecurity-ai-cost-2026.md) — boring hygiene that builds confidence vs vendor hype
- [Boris Cherny - Claude Maintains Apps](wiki/boris-cherny-claude-maintains-apps-2026.md) — tests as production code at scale (388 PRs)
- [Article 27 - Guided QA Engineer](../../Articles/linkedin-posts/Quality-Operating-Model/27-guided-qa-engineer.md) — QA investigates risks, not re-runs checks

---

*Source: Mark Paemaa LinkedIn Pulse 2026-08-27 via https://www.linkedin.com/pulse/automated-testing-isnt-finding-bugs-mark-paemaa-akphc/ · Ingested 2026-09-01*
