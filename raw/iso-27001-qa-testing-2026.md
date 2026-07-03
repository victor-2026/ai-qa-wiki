# ISO 27001 and QA/Testing

## Overview

ISO/IEC 27001 is the international standard for Information Security Management Systems (ISMS). It specifies requirements for establishing, implementing, maintaining, and continually improving an ISMS within the context of the organization's overall business risks.

For QA professionals, ISO 27001 is relevant because:
1. Testing is a key control in the ISMS (A.8.29 — Testing in development/acquisition)
2. QA processes must themselves be secure (test data protection, access control)
3. Security testing is often a compliance requirement, not just a quality practice
4. QA teams may be audited as part of ISMS certification

## Key ISO 27001 Clauses Relevant to QA

### A.8.25 — Secure development lifecycle
- Security requirements defined at the requirements stage
- Security testing integrated into SDLC
- Regression testing for security controls

### A.8.26 — Application security testing
- Vulnerability scanning
- Penetration testing
- Code review for security issues
- Acceptance criteria include security requirements

### A.8.27 — Secure system architecture and design
- Architecture review includes security considerations
- Threat modeling (STRIDE, PASTA)
- Design principles: least privilege, defense in depth

### A.8.28 — Secure coding
- Coding standards include security rules
- Static code analysis
- Peer review for security-critical code

### A.8.29 — Testing in development/acquisition
- Test plans include security test cases
- Test environments isolated from production
- Test data protection (anonymization, masking)
- Acceptance testing includes security validation

### A.8.30 — Outsourced development
- Security requirements in contracts
- Vendor security assessment
- Third-party testing

### A.8.31 — Separation of test and production environments
- No production data in test without anonymization
- Access controls on test environments
- Clear separation of duties

### A.8.32 — Change management
- Change control process
- Testing before production deployment
- Rollback procedures tested

## QA Implications

### What Changes for QA under ISO 27001

1. **Test data management** — Must be anonymized/pseudonymized. Production data cannot be used directly.
2. **Environment isolation** — Test environments must be separate from production. Access controls required.
3. **Evidence collection** — All testing must produce auditable evidence (test cases executed, results, defect reports).
4. **Security requirements in acceptance criteria** — Every user story should have security acceptance criteria.
5. **Penetration testing schedule** — Regular pentests (typically annual or after major changes).
6. **Vulnerability management** — QA may own or participate in vulnerability tracking and retesting.
7. **Access control testing** — Verify RBAC, authentication, session management.

### Testing Types that Support ISO 27001

| Testing Type | ISO 27001 Relevance |
|-------------|---------------------|
| **Vulnerability scanning** | A.8.26 — Regular automated scanning |
| **Penetration testing** | A.8.26 — Deep manual security testing |
| **SAST (Static Analysis)** | A.8.28 — Code-level security checks |
| **DAST (Dynamic Analysis)** | A.8.26 — Runtime security testing |
| **Fuzz testing** | A.8.26 — Input validation robustness |
| **API security testing** | A.8.26 — Endpoint security validation |
| **Authentication testing** | A.9 — Access control verification |
| **Authorization testing** | A.9 — Privilege escalation testing |
| **Session management testing** | A.9 — Token/session security |
| **Data validation testing** | A.8.26 — Input/output validation |
| **Configuration testing** | A.12 — Secure configuration verification |
| **Backup/restore testing** | A.12.3 — DR testing |

## ISO 27001 in the SDLC

```
Requirements → Design → Development → Testing → Release → Operations
    |            |           |            |         |           |
    v            v           v            v         v           v
 Security     Threat      SAST +       Security   Penetration  Continuous
 Stories      Modeling    Secrets      Testing    Testing      Monitoring
                         Scanning     (DAST)
```

## QA's Role in ISO 27001 Audit

1. **Provide evidence** of testing activities (test plans, executed test cases, defect reports)
2. **Demonstrate test environment isolation** (separate from production)
3. **Show test data protection** (anonymization process, no PII in test data)
4. **Prove security testing is performed** (vulnerability scans, pentest reports)
5. **Exhibit change management** (all changes tested before production)

## Common Findings (Non-Conformities) in QA

1. No security testing in acceptance criteria
2. Test environments not isolated from production
3. Production data used in testing without anonymization
4. No evidence of regression testing for security fixes
5. Penetration testing not performed or outdated
6. No vulnerability retesting after fixes

## How to Prepare QA for ISO 27001

1. **Document test processes** — Test strategy, test plans, test case templates
2. **Implement test data management** — Anonymization scripts, synthetic data generation
3. **Separate environments** — Test, staging, production with clear access controls
4. **Integrate security testing** — SAST/DAST in CI/CD pipeline
5. **Create audit evidence** — Traceability from requirements to test cases to results
6. **Train team** — Security awareness, secure coding, testing for security

## Practical Experience Notes

- ISO 27001 certification typically takes 6-12 months for the initial audit
- QA involvement should start from the gap analysis phase
- The biggest QA impact is test data management (most orgs fail here first)
- Automated security testing (SAST/DAST in CI) significantly reduces audit burden
- Vulnerability management process (triage → fix → retest) is a common QA responsibility

## References

- ISO/IEC 27001:2022 — Information security, cybersecurity and privacy protection
- ISO/IEC 27002:2022 — Code of practice for information security controls
- ISO/IEC 27005:2022 — Information security risk management
- OWASP Testing Guide — Security testing methodology
- BSIMM — Building Security In Maturity Model
