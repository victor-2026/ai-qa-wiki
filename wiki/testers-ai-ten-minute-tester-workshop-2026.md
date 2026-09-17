# testers.ai — Ten Minute Tester Workshop (2026)

**Source:** https://testers.ai/workshop/#startForm
**Date:** 2026-09-16 (Victor's session)
**Type:** Human + AI field study

---

## Setup

- 10-minute timed testing session on a "Buggy" kanban board app
- Intentional bugs included in the app under test
- Comparison against pooled results from 2 separate AI coding-agent sessions (16 deduplicated defect families)
- $25/hour conservative rate → $4.17 cost per 10-minute session

---

## Victor's Results

| Metric | Value |
|--------|-------|
| Reports filed | 1 |
| Defect families matched | 1 (Usability) |
| Unmatched candidates | 0 |
| AI families not matched by Victor | 15 |
| Categories Victor explored | Usability only |
| AI categories covered | Security, Privacy, Data integrity, Reliability, Functionality, Usability, Accessibility (7) |

---

## Victor's Report

**REPORT 01 (6:05 into session):** "The titles of cards are not shown full on the cards"

Matched to AI baseline B14 (clipped card titles). Correct finding, confirmed by AI collection.

---

## AI Collection: 15 Unmatched Defect Families

| # | Defect | Category |
|---|--------|----------|
| 1 | Stored JavaScript in notes — private notes render HTML and execute scripts | Security |
| 2 | Public export includes private fields — JSON exposes owner emails/notes | Privacy |
| 3 | Stale tab overwrites newer work | Data integrity |
| 4 | Storage failure says saved — failed writes claim success | Reliability |
| 5 | Done without approval — unapproved cards move to Done | Functionality |
| 6 | In progress exceeds three — 4th card enters despite limit | Functionality |
| 7 | Recovery exports samples and overwrites originals | Data integrity |
| 8 | Card 501 breaks reload | Functionality |
| 9 | Recording opt-out ignored | Privacy |
| 10 | Erase retains activity history | Privacy |
| 11 | CSV quoting broken | Functionality |
| 12 | Legacy import loses assignee | Data integrity |
| 13 | Numeric IDs break card controls | Functionality |
| 14 | Card text too faint — low contrast | Accessibility |
| 15 | Keyboard focus lost | Accessibility |

---

## Analysis

### Coverage Gap
- **Human (10 min):** 1 dimension (Usability), 1 finding
- **AI (2 runs pooled):** 7 dimensions, 16 findings
- **Overlap:** 1 family (Usability/ clipped titles)

### What AI Found That Human Didn't
- Security (JS injection in notes)
- Privacy (export data exposure, opt-out ignored, erase retains history)
- Data integrity (stale overwrites, recovery corruption, import data loss)
- Reliability (silent storage failures)
- Functionality (approval bypass, limit violation, 501 edge case, CSV/ID bugs)
- Accessibility (contrast, keyboard focus)

### What Human Found That AI Didn't
- Nothing unmatched (0 candidates)

### Key Observations
1. **10 minutes ≠ comprehensive testing.** Even focused testers miss 94% of defect families.
2. **AI excels at breadth** — systematic coverage across security/privacy/reliability/accessibility in parallel.
3. **Human excels at Usability** — observed experience, not just functional breakage.
4. **The matched finding validates both:** human noticed the same thing AI did (card titles clipped).
5. **Cost comparison:** $4.17 human for 10 min vs unknown AI cost. Not a competition — complementary signals.
6. **15/16 unmatched** = the gap that QA governance must address. Neither human nor AI alone covers everything.

---

## Connections to Our Work

- **Article 27 thesis validated:** Human testing is narrow (usability), AI testing is broad (security/privacy/reliability/accessibility). The "Guided QA Engineer" role = directing BOTH, not replacing either.
- **Per-risk-tier evidence:** AI findings need human review before they count as confirmed defects. testers.ai: "Unmatched candidates need review."
- **VerdictGate:** AI generates findings, attestor makes the verdict. Same pattern.
- **10-minute cost ($4.17)** = economic framing for Article 27. "What does your QA hire req list as core today?" ← breadth vs depth trade-off.
- **Complementary signals:** Human = taste/experience. AI = systematic coverage. Together = governance.

---

## Related Wiki

- `wiki/addy-osmani-own-the-outer-loop-2026.md` — answerability, verdict, quality
- `wiki/addy-osmani-agentic-code-quality-2026.md` — constraints as quality
- `wiki/comprehension-debt.md` — human understanding gap
