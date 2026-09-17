# TestMu AI — Finance AI Agent Compliance Testing (2026)

**Source:** https://www.testmuai.com/blog/finance-ai-agent-compliance-testing/
**Author:** Brian Corkery (MD Banking & Financial Services), Sirajuddin Khan (Reviewer)
**Date:** 2026-09-14
**Regulation:** FINRA Rule 2210 (not SEC-registered advisers — they fall under Advisers Act Marketing Rule 17 CFR 275.206(4)-1)

---

## Core Thesis

> For a FINRA member firm, agent output is a communication with the public. Duties attach to what a firm distributes.

Agent compliance testing = treating output as a regulated record, not just a quality score.

---

## Key Patterns

### 1. Classification Is an INPUT, Not an Output

- **Correspondence:** ≤25 retail investors in 30 calendar days (Rule 2210(a)(2))
- **Retail communication:** >25 retail investors (Rule 2210(a)(5))
- Same byte-identical text can land in different categories based on recipient count
- **Suite cannot derive category from transcript** — must be declared in fixture

### 2. Required Qualifications List (Before the Run)

- Omission = absence. You can't pattern-match against nothing.
- Each topic the agent discusses needs a list of required qualifications
- **Owned by product disclosure owner**, not QA
- Goes stale when product changes, not when agent changes
- Versioned with review date

### 3. Phrasing ≠ Facts (Separate Graders)

- **Pass 1 (facts):** assertions against fixture values + knowledge source
- **Pass 2 (phrasing):** exaggeration, unwarranted certainty, promissory construction
- Calibration pairs: acceptable + unacceptable phrasings of the SAME true fact
- Compliance writes pairs, engineering wires them in

### 4. Approval = Supervisory Act (Not Test Result)

- Rule 2210(b)(1)(A): registered principal approves BEFORE use
- Agent composes each answer fresh — no fixed artifact
- **Approved object** (firm decides): prompt+constrained output, template library, or bounded response set
- Test run evidences constraint held ≠ principal approval

### 5. Evidence a Run Must Carry

| Rule Field | Run Already Emits | Harness Must Add |
|------------|-------------------|------------------|
| First/last use dates | Annotated transcripts | Stamped at release |
| Approving principal + date | Nothing | Read from sign-off |
| Preparer/distributor | CI actor (build log only) | Promoted into artifact |

---

## CI Gate Policy

| Gate Type | Rule Reference | Action |
|-----------|---------------|--------|
| Missing qualification | 2210(d)(1)(A) | Hard gate (build red) |
| Promissory phrasing | 2210(d)(1)(B) | Hard gate |
| Category mismatch | 2210(a)(5) | Hard gate |
| Tone/flow movement | — | Report only |

---

## Connections to Our Work

- **Classification as INPUT = per-risk-tier:** deployment context determines obligations, not the code itself
- **Qualifications list = mutation matrix:** required elements defined before the run, verified during
- **Phrasing ≠ facts = our split:** behavior (does it work?) vs. presentation (is it clear?)
- **Approval ≠ test = attestation boundary:** test evidence supports but doesn't replace human judgment
- **Evidence retention = Article 27:** "keep the evidence from gating runs"
- **FINRA compliance = real-world attestation pattern** (not just QA theory)

---

## Related

- `wiki/testmuai-llm-evaluation-vs-e2e-agent-testing-2026.md` — eval vs test distinction
- Article 27: "QA Didn't Get Replaced. It Got Promoted." — attestation role
- VerdictGate: evidence chain + audit trail
