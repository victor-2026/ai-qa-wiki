# ISO 27001 and QA/Testing

## Overview

ISO/IEC 27001 is the international standard for Information Security Management Systems (ISMS). For QA professionals, this standard is relevant because testing is both a control (A.8.29) and a process that must itself be secure.

## Key Clauses Relevant to QA

| Clause | Topic | QA Implication |
|--------|-------|----------------|
| **A.8.25** | Secure development lifecycle | Security requirements at requirements stage, security testing in SDLC |
| **A.8.26** | Application security testing | Vulnerability scanning, penetration testing, code review |
| **A.8.27** | Secure architecture | Threat modeling, design review |
| **A.8.28** | Secure coding | SAST, code review, secure coding standards |
| **A.8.29** | Testing in development/acquisition | Test plans include security, environment isolation, test data protection |
| **A.8.31** | Separation of environments | No production data in test, access controls |
| **A.8.32** | Change management | Testing before production, rollback testing |

## QA Implications

### What Changes

1. **Test data management** — Anonymization/pseudonymization required. No production PII in test.
2. **Environment isolation** — Test environments must be separate from production.
3. **Audit evidence** — All testing must produce auditable results.
4. **Security in acceptance criteria** — Every user story should include security AC.
5. **Vulnerability management** — QA may own triage → fix → retest cycle.

### Testing Types for ISO 27001

| Testing Type | Relevance |
|-------------|-----------|
| Vulnerability scanning | A.8.26 — automated |
| Penetration testing | A.8.26 — manual deep testing |
| SAST (Static Analysis) | A.8.28 — code-level |
| DAST (Dynamic Analysis) | A.8.26 — runtime |
| Fuzz testing | A.8.26 — input validation |
| API security testing | A.8.26 — endpoint security |
| Auth/Authz testing | A.9 — access control |
| Backup/restore testing | A.12.3 — DR |

## QA Role in Audit

- Provide evidence of testing (plans, cases, results)
- Demonstrate test environment isolation
- Show test data protection process
- Prove security testing is performed (scans, pentests)
- Exhibit change management compliance

## Practical Takeaways

- Biggest failure point: test data management (production data without anonymization)
- Automated security testing in CI/CD significantly reduces audit burden
- ISO 27001 certification typically takes 6-12 months for initial audit
- QA involvement should start from gap analysis phase

## References

- ISO/IEC 27001:2022 — Information security, cybersecurity and privacy protection
- ISO/IEC 27002:2022 — Code of practice
- OWASP Testing Guide
- ENFINT Flametree.ai — ISO 27001:2022 certified (TÜV AUSTRIA)


<!-- backlinks-start -->
### Backlinks
- [21 Cfr Part 11 Electronic Records 2026](wiki/21-cfr-part-11-electronic-records-2026.md)
<!-- backlinks-end -->
