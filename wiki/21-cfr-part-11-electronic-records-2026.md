---
source: "21-cfr-part-11-electronic-records-2026.md"
ingested: "2026-07-24"
---

## 21 CFR Part 11 – Electronic Records & Signatures  

**Summary**  
21 CFR Part 11 is the FDA’s rule that makes electronic records and signatures legally equivalent to paper documents. It applies to any system that creates, modifies, stores, retrieves, or transmits data required by FDA‑regulated activities (pharma, medical devices, biotech, clinical trials). Compliance is achieved by demonstrating that the system is trustworthy, reliable, and protected against unauthorized alteration.

---

### Key Concepts  

| Area | What it means | Typical controls |
|------|---------------|------------------|
| **Closed‑system controls (§11.10)** | Systems used only by authorized personnel must be validated and auditable. | Validation (IQ/OQ/PQ), immutable audit trail, role‑based access, device identification, training records, SOPs, retention strategy, input limits. |
| **Open‑system controls (§11.30)** | Adds encryption and digital‑signature safeguards for systems that could be accessed by outsiders. |
| **Signature Manifestation (§11.50)** | Every electronic signature must display the signer’s name, date/time, and purpose in a human‑readable format. |
| **Linkage (§11.70)** | The signature is cryptographically bound to the specific record; any later change breaks the link and is flagged. |
| **Electronic Signature Requirements (§11.100‑§11.200)** | Each signature is unique to one individual, requires at least two authentication factors (e.g., ID + password) or a biometric measure, and must be non‑transferable. |
| **Identification/Password Controls (§11.300)** | Unique IDs, periodic password changes, lock‑out after failed attempts, encrypted transmission, and formal loss/deactivation procedures. |
| **Validation (Risk‑based)** | Validation plan → risk assessment → functional requirements → test scripts → execution → validation report. Includes Installation Qualification (IQ), Operational Qualification (OQ), Performance Qualification (PQ), and overall Computer System Validation (CSV). |
| **Audit Trail** | Computer‑generated, time‑stamped, immutable, chronological log of who did what (create, edit, delete, view). Must be included in backups and reviewed regularly. |
| **Common Findings** | Unvalidated spreadsheets, shared logins, disabled audit trails, weak password policies, untested backups, missing delete‑event logging. |

---

### Practical Applications  

1. **Laboratory Information Management System (LIMS)**  
   * Validate the LIMS (IQ/OQ/PQ) against a risk‑based plan.  
   * Enable immutable audit logs for every sample entry, result edit, and report generation.  
   * Enforce unique user IDs with strong password rules and two‑factor login.  
   * Configure electronic signatures that embed the analyst’s name, timestamp, and “Reviewed/Approved” status on each report.  

2. **Clinical Trial Data Capture**  
   * Use a validated eCRF platform that encrypts data in transit and at rest (open‑system controls).  
   * Link investigator signatures to each case report form; any post‑signoff change triggers an alert.  
   * Maintain SOPs describing backup, restoration, and periodic audit‑trail review.  

3. **Manufacturing Batch Records**  
   * Integrate instrument IDs to satisfy device checks; the system records the source of each measurement.  
   * Implement sequential login (badge + PIN) for operators to satisfy authority‑check requirements.  
   * Archive records for the statutory retention period and verify restore capability quarterly.  

4. **Change Management**  
   * Any software update or configuration change triggers a re‑assessment of risk and, where needed, a partial re‑validation.  
   * Document all changes in a controlled change‑control log that itself is auditable.  

5. **Audit Preparation**  
   * Keep validation documentation, SOPs, training logs, and audit‑trail extracts readily accessible.  
   * Conduct internal mock inspections focusing on the 483‑type findings listed above.  

---

### Interview‑Ready Nuggets (BostonGene)

* **Ensuring compliance** – “Validate the system, enable a secure audit trail, enforce unique logins with two‑factor authentication, document everything in SOPs, and verify backup/restore.”  
* **Audit‑trail compliance** – “Computer‑generated, time‑stamped, immutable, chronological, covering all create/read/update/delete actions.”  
* **Validation workflow** – “Risk‑based plan → requirements → IQ/OQ/PQ scripts → execution → deviation handling → final report.”  

---

### See also  

- [ISO 27001 and QA/Testing](wiki/iso-27001-qa-testing-2026.md)  
- [Test Stability & Anti‑Flakiness](wiki/testing-stability.md)  
- [Transition from Vibe to Wipe Coding](wiki/wipe-coding-transition-en.md)  
- [30 AI‑Focused Interview Questions for Manual QA](wiki/30-ai-questions-manual-qa-2026.md)  
- [Vector Databases in Fintech](wiki/vector-databases-fintech-2026.md)  











<!-- backlinks-start -->
### Backlinks
- [30 AI-Focused Interview Questions for Manual QA](wiki/30-ai-questions-manual-qa-2026.md)
- [ISO 27001 and QA/Testing](wiki/iso-27001-qa-testing-2026.md)
- [Test Stability & Anti-Flakiness](wiki/testing-stability.md)
- [Transition from Vibe to Wipe Coding: Benefits, Challenges and Risks](wiki/wipe-coding-transition-en.md)
- [Vector Databases in Fintech](wiki/vector-databases-fintech-2026.md)
<!-- backlinks-end -->

---
*Generated by wiki_llm.py (Groq) — ingested from `raw/21-cfr-part-11-electronic-records-2026.md`*
