# Test Management & Traceability

**Last Updated:** 2026-04-17
**Sources:** raw/rtm-matrix-habr.md

---

## Requirements Traceability Matrix (RTM)

RTM is a document (usually table) that establishes and tracks relationships between:
- Requirements
- Test cases
- Defects

### Three Key Questions

| Question | RTM Answer |
|----------|------------|
| **What did we test?** | Requirements with test cases |
| **What did we NOT test?** | Gaps in coverage |
| **Why are we testing this?** | Test → Requirement link |

> **Without RTM** — testing is less manageable. **With RTM** — conscious and measurable testing.

## Types of Traceability

| Type | Direction | Purpose |
|------|-----------|---------|
| **Forward** | Requirement → Test Case | Verify coverage |
| **Backward** | Test Case → Requirement | Understand test purpose |
| **Bidirectional** | Requirement ⇄ Test Case | Complete traceability |
| **Vertical** | Requirement → Design → Code → Test | End-to-end trace |
| **Horizontal** | Test → Bug → Fix → Retest | Trace within phase |

## RTM Structure

| Column | Description | Example |
|--------|-------------|---------|
| Requirement ID | Unique requirement ID | REQ-AUTH-01 |
| Requirement Description | Brief description | Email/password login |
| Test Case ID | Covering test cases | TC-LOGIN-01, TC-LOGIN-02 |
| Test Status | Pass / Fail / Blocked / Not Run | Pass |
| Defect ID | Related bugs | BUG-101 |
| Defect Status | Open / Fixed / Closed | Fixed |
| Coverage Status | Covered / Not Covered / Partial | Covered |
| Coverage % | Coverage percentage | 100% |

## RTM Example

| REQ ID | Requirement | Priority | Test Cases | Status | Defects | Coverage |
|--------|------------|----------|------------|--------|---------|----------|
| REQ-01 | User login | High | TC-LOGIN-01, TC-LOGIN-02, TC-LOGIN-03 | Pass, Pass, Fail | BUG-101 | 100% |
| REQ-02 | Password recovery | Medium | TC-REC-01, TC-REC-02 | Pass, Not Run | — | 50% |
| REQ-03 | Product search | High | TC-SEARCH-01, TC-SEARCH-02 | Pass, Pass | — | 100% |
| REQ-04 | Price filter | Low | — | — | — | **0% (GAP!)** |

## Impact Analysis

```
CHANGED REQ-01 (Login)
                    │
                    ▼
┌─────────────────────────────────────────────────┐
│  RTM shows:                                     │
│  • TC-LOGIN-01 (Pass)     → Rerun needed      │
│  • TC-LOGIN-02 (Pass)     → Rerun needed      │
│  • TC-LOGIN-03 (Fail)     → BUG-101 needs     │
│                              retest             │
│                                                 │
│  REQ-01 also affects REQ-02                    │
└─────────────────────────────────────────────────┘
```

## Coverage Statistics

| Metric | Value |
|--------|-------|
| Total requirements | 50 |
| Requirements with tests | 45 |
| Requirements WITHOUT tests | 5 |
| **Coverage %** | **90%** |
| Requirements with defects | 12 |
| Total test cases | 180 |

## Common Mistakes

| Mistake | Consequence |
|---------|-------------|
| RTM not updated | Quickly becomes outdated |
| Formal linking | False sense of coverage |
| No defect linkage | Hard to analyze problem areas |
| Test duplication | Distorts metrics |
| No backward traceability | "Hanging" tests without purpose |

## QA Checklist

- [ ] Each requirement has at least 1 test case?
- [ ] Any "hanging" test cases without requirement link?
- [ ] Tests updated when requirement changed?
- [ ] Each defect linked to specific requirement?
- [ ] Can answer "Why was this test not passed?" via RTM?
- [ ] RTM updated after each release/sprint?

## Tools

| Tool | Type | Feature |
|------|------|---------|
| Jira + Xray/Zephyr | Plugin | Built-in traceability |
| TestRail | TMS | Native RTM support |
| Qase | TMS | Simple requirement linking |
| Excel/Google Sheets | Manual | Free but labor-intensive |
| Polarion | ALM | Enterprise solution |
| Azure DevOps | ALM | Built-in traceability |

## When RTM is NOT Needed

| Situation | Alternative |
|-----------|-------------|
| Startup with 5-10 requirements | Trello / Notion / Google Sheets |
| Project 1-2 weeks | RTM won't pay off |
| Team of 1-2 people | All traceability in your head |
| Ad-hoc testing | No clear requirements |
| Prototype / MVP | Requirements change daily |

### Rule of Thumb

> **>20 requirements + team from 3 people = RTM pays off**

## Pre-Implementation Checklist

- [ ] More than 20 requirements in project?
- [ ] Team larger than 3 people?
- [ ] Requirements don't change daily?
- [ ] Someone to maintain the matrix?
- [ ] Ready to spend 15-30 min per sprint on RTM?

**3+ "yes" answers → implement RTM**

## Key Takeaways

1. **RTM is a tool, not a goal.** Value in answers it provides.
2. **Start small.** Simple table: Requirement → Test Case.
3. **Actuality is key.** Dead matrix worse than no matrix.
4. **>20 reqs + team 3+ = RTM saves nerves.**

> **RTM is not bureaucracy, it's the QA navigator.**

## Related

- [[wiki/testing-strategies]] — Testing approaches
- [[wiki/ai-testing-metrics]] — Measuring quality

## Sources

- raw/rtm-matrix-habr.md
