# 21 CFR Part 11 — Electronic Records and Electronic Signatures

Source: FDA 21 CFR Part 11
Purpose: Interview prep for BostonGene
Keywords: 21 CFR Part 11, FDA, electronic records, audit trail, electronic signature, validation

---

## What is 21 CFR Part 11?

US FDA regulation that defines criteria under which electronic records and electronic signatures are considered **trustworthy, reliable, and equivalent to paper records**. Applies to all FDA-regulated industries: pharmaceuticals, medical devices, biotech, clinical trials.

### When it applies:
- Records required by FDA regulations (e.g., batch records, lab data, clinical data)
- Signatures required by FDA regulations
- Systems that create, modify, maintain, archive, retrieve, or transmit electronic records

### When it does NOT apply:
- Paper records (obviously)
- Internal records not submitted to FDA

---

## Core Requirements

### 11.10 — Controls for Closed Systems

| # | Requirement | Implementation Example |
|---|-------------|----------------------|
| (a) | **Validation** — system validated for accuracy, reliability, consistent performance | IQ/OQ/PQ for LIMS or QMS software |
| (b) | **Audit trail** — computer-generated, time-stamped, secure record of who did what and when | Database triggers, immutable logs |
| (c) | **Authority checks** — ensure only authorised users can access the system | Role-based access, AD/LDAP |
| (d) | **Device checks** — verify source of data input (e.g., instrument ID) | Laboratory equipment integration |
| (e) | **Training** — ensure developers, maintainers, and users are trained | Training records, competency assessment |
| (f) | **Written policies** — hold individuals accountable for actions in e-records | User acknowledgement, incident policy |
| (g) | **Authority checks on devices** — sequential or event-based login | Badge + PIN, biometric |
| (h) | **Documentation** — system documentation, operational manuals, policies | SOPs, system specification, test scripts |
| (i) | **Record retention** — readily retrievable throughout retention period | Backup, archive, restore testing |
| (j) | **Limit checks** — system checks for valid data entry, sequence, processing | Input validation, sequence enforcement |

### 11.30 — Controls for Open Systems
Same as 11.10 plus additional controls (encryption, digital signatures) for systems accessible by unauthorised persons.

### 11.50 — Signature Manifestations
- Signed electronic record must contain:
  - Printed name of signer
  - Date and time of signature
  - Meaning of signature (e.g., "Reviewed", "Approved")
- These must be **included in any human-readable form** (display, printout, export)

### 11.70 — Signature/Record Linking
- Electronic signature must be linked to the record to **detect alteration or falsification**
- Cannot be copied, deleted, or reassigned

### 11.100 — Electronic Signatures
- Must be **unique to one individual** (no shared accounts)
- Identity verification before creation
- Must use at least two distinct components (e.g., user ID + password)
- If biometric: device design ensures non-reusable

### 11.200 — Electronic Signature Components
- **Non-biometric:** at least two identification components (ID + password)
- **Biometric:** measurement of physical/behavioural characteristic

### 11.300 — Controls for Identification Codes/Passwords
- Maintain uniqueness
- Periodic check/recall
- Loss management (deactivation, reporting)
- Attempt limits (lockout after N failed attempts)
- Periodic password changes
- Encryption when transmitted

---

## Validation Requirements (11.10(a))

Validation per 21 CFR Part 11 is **risk-based and documented**:

```
Validation Plan → Risk Assessment → Requirements → Scripts → Execution → Report
```

| Phase | What | Output |
|-------|------|--------|
| IQ | Installation Qualification | System installed correctly |
| OQ | Operational Qualification | System operates per specs |
| PQ | Performance Qualification | System performs in production |
| CSV | Computer System Validation | All of the above for regulated systems |

### What auditors check:
- Validation scope (all systems that handle regulated data)
- Evidence of testing (scripts with expected results, signed off)
- Change control (any change → revalidation assessment)
- Training records (users trained on validated system)

---

## Audit Trail Requirements (11.10(b))

Audit trail must be:
- **Computer-generated** (not manual)
- **Time-stamped** (date + time, NTP-synced)
- **Secure** (cannot be modified, deleted, or overwritten by users)
- **Chronological** (sequential record of events)
- **Complete** (who, what, when, why for create/edit/delete)

### What auditors look for:
- Audit trail reviewed periodically
- Audit trail included in backup/archive
- No shared admin accounts
- Admin actions also tracked

---

## Common Inspection Findings (483s)

| Finding | Root Cause |
|---------|------------|
| No validation for spreadsheet used for clinical data | Excel ≠ validated system |
| Shared login accounts | No unique user identification |
| Audit trail disabled in production | Performance concern → no compliance check |
| No password policy | 11.300 requirements not implemented |
| Backup not tested for restoration | Procedural gap |
| Deleted records not tracked | Audit trail not covering delete operations |

---

## Relation to Other Standards

| Standard | Connection |
|----------|------------|
| **ISO 13485** | QMS that must validate systems per Part 11 requirements |
| **GxP** | Good Practices (GMP, GCP, GLP) all require Part 11 compliance |
| **EU Annex 11** | European equivalent of 21 CFR Part 11 |
| **ICH E6 R2** | Clinical trial data integrity |

---

## Interview Questions (BostonGene)

**"How would you ensure 21 CFR Part 11 compliance for a laboratory system?"**
→ Validate system (IQ/OQ/PQ), enable audit trail, enforce unique logins + password policy, document in SOP, test backup/restore, train users

**"What makes an audit trail compliant?"**
→ Computer-generated, time-stamped, secure (no user edits), chronological, covers all CRUD operations

**"How do you validate a system under Part 11?"**
→ Risk-based approach: validation plan → requirements → IQ/OQ/PQ scripts → execution → deviation handling → validation report

---

## Sources

- [21 CFR Part 11 (ecfr.gov)](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-A/part-11)
- [FDA Guidance — Part 11 Electronic Records (2003)](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/part-11-electronic-records-electronic-signatures-scope-and-application)
- [FDA Data Integrity Guidance (2018)](https://www.fda.gov/media/119267/download)
