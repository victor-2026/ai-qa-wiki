# ISO 13485 — Quality Management System for Medical Devices

Source: ISO 13485:2016
Purpose: Interview prep for BostonGene
Keywords: ISO 13485, QMS, medical device, quality management system, audit, CAPA

---

## What is ISO 13485?

ISO 13485 is the international standard for Quality Management Systems (QMS) for medical device manufacturers. It is based on ISO 9001 but with medical-device-specific additions: regulatory compliance, risk management, traceability, and post-market surveillance.

It is **mandatory** for CE marking under EU MDR and accepted by FDA (21 CFR 820 harmonised).

### Key difference from ISO 9001:

| Aspect | ISO 9001 | ISO 13485 |
|--------|----------|-----------|
| Focus | Customer satisfaction | Safety + regulatory compliance |
| Risk | General | ISO 14971 integrated |
| Traceability | Recommended | Mandatory (all records) |
| Validation | General | Specific: process, software, design |
| CAPA | Recommended | Mandatory |

---

## Core Clauses

### Clause 4: QMS
- Documented quality policy and objectives
- Quality Manual (controlled document)
- Document and record control
- **4.2.4 Records:** one of the most audited clauses — every record must be identifiable, legible, stored, retained, and retrievable

### Clause 5: Management Responsibility
- Top management must demonstrate commitment
- Quality policy communicated throughout organisation
- Management review at planned intervals
- **5.6 Management Review:** input includes audit results, customer feedback, process performance, CAPA status

### Clause 6: Resource Management
- Competence, training, and awareness
- Infrastructure (buildings, equipment, IT systems)
- Work environment (cleanroom, lab conditions)

### Clause 7: Product Realisation (Core)
- **7.1 Planning:** plan quality, resources, verification, validation
- **7.2 Customer-related processes:** requirements review, communication
- **7.3 Design and Development:**
  - Design and development planning
  - Design inputs → outputs → review → verification → validation → transfer
  - **Design History File (DHF):** complete record of design activities
- **7.4 Purchasing:** supplier evaluation and control
- **7.5 Production and Service Provision:**
  - **7.5.6 Validation of processes:** when output cannot be verified by monitoring (e.g., sterilisation)
  - **7.5.7 Sterilisation specifics**
- **7.6 Control of Monitoring and Measuring Equipment:** calibration

### Clause 8: Measurement, Analysis, Improvement
- **8.2 Monitoring and Measurement:**
  - Customer feedback (mandatory)
  - Internal audit (at planned intervals)
  - Measurement and monitoring of processes and product
- **8.3 Nonconforming Product:** identify, segregate, evaluate, disposition
- **8.4 Analysis of Data:** statistical techniques, trends, CAPA effectiveness
- **8.5 Improvement:**
  - **CAPA (Corrective and Preventive Action):** root cause analysis, effectiveness verification
  - Preventive action: proactive, before issues occur

---

## Most Audited Records

| Record | Clause | Auditor Checks |
|--------|--------|----------------|
| Quality Manual | 4.2.2 | Complete, controlled, current |
| Design History File (DHF) | 7.3 | All design phases documented |
| Design Reviews | 7.3.4 | Participants, decisions, action items |
| Design Verification | 7.3.6 | Did it meet specs? Evidence? |
| Design Validation | 7.3.7 | Does it meet user needs? Clinical? |
| Risk Management File | ISO 14971 | Traceability: hazard → control → verification |
| CAPA Records | 8.5.2 | Root cause, correction, effectiveness check |
| Internal Audit Reports | 8.2.4 | Nonconformities, follow-up |
| Management Review Minutes | 5.6 | Inputs, outputs, decisions |
| Training Records | 6.2 | Competency matrix, training plans |
| Supplier Audits | 7.4 | Approved supplier list, evaluation criteria |
| Calibration Records | 7.6 | Equipment list, certificates, schedules |

---

## Integration with Other Standards

| Standard | Role in ISO 13485 |
|----------|-------------------|
| ISO 14971 | Risk management is a required process |
| IEC 62304 | Software lifecycle conformity |
| IEC 62366 | Usability engineering |
| 21 CFR Part 820 | US equivalent (harmonised 2026) |
| EU MDR | EU Medical Device Regulation |

---

## Interview Questions (BostonGene)

**"How would you implement QMS per ISO 13485 for a bioinformatics platform?"**
→ Establish DHF for software components, integrate ISO 14971 risk file, implement CAPA for AI model drift, ensure audit trail for all data transformations

**"What's the difference between verification and validation?"**
→ Verification: "did we build it right?" (specs met). Validation: "did we build the right thing?" (user needs met)

**"How do you ensure audit readiness?"**
→ Continuous compliance (not checkbox before audit). Document control, training matrix, CAPA trend analysis, management review minutes

---

## Sources

- [ISO 13485:2016](https://www.iso.org/standard/59752.html)
- [FDA 21 CFR Part 820 QSR](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-820)
- [MDR 2017/745 Annex IX](https://eur-lex.europa.eu/eli/reg/2017/745/oj)
