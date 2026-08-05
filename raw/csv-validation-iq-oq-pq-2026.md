# CSV Validation Protocols — IQ/OQ/PQ

Source: GAMP 5, FDA Guidance
Purpose: Interview prep for BostonGene
Keywords: IQ, OQ, PQ, CSV, Computer System Validation, validation protocol, GAMP 5

---

## What is CSV?

Computer System Validation (CSV) is the documented process of ensuring that a computerised system does what it is intended to do **consistently, accurately, and in compliance** with regulatory requirements (21 CFR Part 11, EU Annex 11, GxP).

### Core principle:
**"If it isn't documented, it didn't happen."** — Everything in CSV is documented and auditable.

---

## Validation Lifecycle (GAMP 5)

```
Concept → Requirements → Design → Build → Test → Release → Operation → Retirement
                                          ↓
                                     IQ / OQ / PQ
```

GAMP 5 (Good Automated Manufacturing Practice) is the industry standard for CSV. It defines a risk-based approach to validation — not all systems need the same level of validation.

### GAMP 5 Software Categories

| Category | Type | Validation Effort | Example |
|----------|------|-------------------|---------|
| **1** | Infrastructure software | Minimal | OS, database, network |
| **2** | Not used (removed in GAMP 5) | — | — |
| **3** | Standard (off-the-shelf) | OQ only | Excel, Jira, Confluence |
| **4** | Configured product | IQ + OQ + PQ | LIMS, QMS, ERP |
| **5** | Custom application | Full lifecycle (IQ+OQ+PQ+design specs) | Bioinformatics pipeline, AI model |

---

## IQ — Installation Qualification

**Goal:** Prove that the system is installed correctly per manufacturer specs.

### What is checked:
- Hardware: correct model, specs, network connectivity
- Software: correct version, installed per procedure, patches applied
- Environment: server room conditions, power, cooling
- Documentation: manuals received, installation records complete
- Security: physical access, user accounts

### IQ Document Template:
```
1. System identification (name, version, serial)
2. Installation checklist (component → installed? → verified by → date)
3. Environment verification (temperature, humidity, power)
4. Software version verification (checksum, installer log)
5. Configuration baseline (settings, parameters)
6. Deviations (any issues, resolutions)
7. Approval signatures
```

---

## OQ — Operational Qualification

**Goal:** Prove that the system operates according to defined functional requirements under normal and boundary conditions.

### What is tested:
- All functions work per specification
- Boundary conditions (max users, max data volume)
- Error handling (what happens when inputs are invalid?)
- Security (access controls, permissions, audit trail)
- Interfaces (data exchange with other systems)
- Alarms/warnings function correctly

### OQ Document Template:
```
1. Test objective
2. Test environment (hardware, software, configuration)
3. Test cases (pass/fail, each linked to requirement)
4. Expected vs actual results
5. Deviations and resolution
6. Traceability matrix (test → requirement)
7. Approval signatures
```

### Example OQ Test Case:

| ID | Requirement | Test Step | Expected Result | Actual | Pass/Fail |
|----|-------------|-----------|-----------------|--------|-----------|
| OQ-01 | System authenticates user | Enter valid credentials | Dashboard loads | Dashboard loaded | ✅ Pass |
| OQ-02 | System rejects invalid user | Enter wrong password | Error message | Error "Invalid credentials" | ✅ Pass |
| OQ-03 | Audit trail captures login | Login, then check audit log | Entry with user, time, action | Entry found | ✅ Pass |

---

## PQ — Performance Qualification

**Goal:** Prove that the system performs reliably in the production environment with real-world workloads.

### What is tested:
- End-to-end business scenarios
- Load/stress testing (peak usage)
- Data integrity (data flows correctly end-to-end)
- Backup and restore
- Business continuity / disaster recovery
- Integration with production systems

### PQ Document Template:
```
1. Business process description
2. Real-world scenarios (not just unit tests)
3. Duration (e.g., 7 days continuous operation)
4. Performance metrics (response time, throughput)
5. Data integrity verification
6. Backup/restore testing
7. Deviations and resolution
8. Approval signatures
```

---

## Validation Documentation Package (for Audit)

```
Validation Plan (VP)
├── Requirements (URS — User Requirements Spec)
├── Functional Specifications (FS)
├── Design Specifications (DS)
├── Risk Assessment (RA)
├── IQ Protocol + Report
├── OQ Protocol + Report
├── PQ Protocol + Report
├── Traceability Matrix (requirements → tests)
├── Validation Summary Report (VSR)
├── SOPs (Standard Operating Procedures)
└── Training Records
```

---

## Key Concepts

### 4-Eyes Principle
All validation documents must be **prepared by one person, reviewed and approved by another** (independent reviewer).

### Deviation Handling
When a test fails:
1. Record the deviation
2. Investigate root cause
3. Determine impact
4. Implement corrective action
5. Re-test
6. Close deviation

### Change Control
After validation, ANY change to the system triggers change control:
- Assess impact (major/minor)
- Determine revalidation needed
- Document change
- Test and approve

### Periodic Review
Validated systems must be **periodically reviewed** (annually or per schedule):
- Is the system still validated?
- Have processes changed?
- Are SOPs current?
- Training up to date?

---

## Risk-Based Validation (GAMP 5 Approach)

Not all systems need full IQ/OQ/PQ. GAMP 5 says:
- **Category 3** (standard): OQ only
- **Category 4** (configured): IQ + OQ + PQ
- **Category 5** (custom): full lifecycle

### Risk factors to consider:
- Patient safety impact
- Data integrity impact
- System complexity
- Vendor reliability
- History of failures

---

## Interview Questions (BostonGene)

**"Explain the difference between IQ, OQ, and PQ."**
→ IQ: installed correctly. OQ: operates correctly. PQ: works in production

**"When would you reduce validation effort?"**
→ Low-risk, standard software (e.g., Jira for non-regulated tasks). Risk-based per GAMP 5

**"How do you handle a failing OQ test?"**
→ Document deviation, investigate root cause, fix, re-test. If spec is wrong → update requirement. If system bug → vendor fix. All documented

**"What's in a Validation Summary Report?"**
→ Summary of all activities, deviations, conclusion: "system is validated and ready for production use"

---

## Sources

- [GAMP 5 — A Risk-Based Approach to Compliant GxP Computerized Systems (ISPE)](https://ispe.org/publications/guidance-documents/gamp-5)
- [FDA — General Principles of Software Validation (2002)](https://www.fda.gov/media/73141/download)
- [21 CFR Part 11 — Electronic Records](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-A/part-11)
- [WHO — Validation of Computerized Systems](https://www.who.int/publications/m/item/validation-of-computerized-systems)
