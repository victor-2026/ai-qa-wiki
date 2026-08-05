# ISO 14971 — Risk Management for Medical Devices

Source: ISO 14971:2019 (EN ISO 14971:2019 + A11:2021)
Purpose: Interview prep for BostonGene — Senior Software Quality Manager (Yerevan)
Keywords: ISO 14971, risk management, medical device, IEC 62304, FMEA, hazard analysis

---

ISO 14971 is the international standard for risk management of medical devices, including software as a medical device (SaMD) and software in a medical device (SiMD). It defines a systematic process for identifying hazards, estimating risks, controlling them, and monitoring their effectiveness throughout the product lifecycle.

When combined with IEC 62304 (software lifecycle) and ISO 13485 (quality management), it forms the regulatory foundation for medical device software development.

---

## 1. Key Terms

| Term | Definition | Example |
|------|-----------|---------|
| **Hazard** | Potential source of harm | Software crash during patient data upload |
| **Hazardous situation** | Circumstance where people/property are exposed to a hazard | Lab technician using crashed software, unaware data was lost |
| **Harm** | Injury or damage to health | Misdiagnosis due to lost/missing data |
| **Risk** | Combination of probability of harm and severity of that harm | High probability × high severity = unacceptable risk |
| **Severity** | Measure of harm's potential impact | Negligible / Minor / Serious / Critical / Catastrophic |
| **Probability** | Likelihood of harm occurring | Frequent / Probable / Occasional / Remote / Improbable |
| **Risk control** | Action to reduce risk to an acceptable level | Add auto-save every 30 seconds + data integrity check |
| **Residual risk** | Risk remaining after controls are applied | Auto-save might fail if disk is full — monitor and alert |

---

## 2. Risk Management Process (6 Steps)

ISO 14971 defines a continuous, iterative process:

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Risk Analysis                                            │
│    Identify intended use → Identify hazards → Estimate risk │
└─────────────────────────┬───────────────────────────────────┘
                          ↓
┌─────────────────────────┬───────────────────────────────────┐
│ 2. Risk Evaluation                                          │
│    Compare estimated risk against acceptable criteria       │
└─────────────────────────┬───────────────────────────────────┘
                          ↓
┌─────────────────────────┬───────────────────────────────────┐
│ 3. Risk Control                                           │
│    Identify control measures → Implement → Verify          │
└─────────────────────────┬───────────────────────────────────┘
                          ↓
┌─────────────────────────┬───────────────────────────────────┐
│ 4. Residual Risk Evaluation                                 │
│    Is residual risk acceptable? If not → more controls      │
└─────────────────────────┬───────────────────────────────────┘
                          ↓
┌─────────────────────────┬───────────────────────────────────┐
│ 5. Risk Management Report                                   │
│    Document the entire process for audit                    │
└─────────────────────────┬───────────────────────────────────┘
                          ↓
┌─────────────────────────┬───────────────────────────────────┐
│ 6. Post-Market Surveillance                                 │
│    Monitor real-world use, update risk assessment           │
└─────────────────────────┬───────────────────────────────────┘
```

---

## 3. Risk Analysis Methods

### FMEA (Failure Mode and Effects Analysis)
- Bottom-up: for each component, ask "what could fail?"
- RPN = Severity × Occurrence × Detection
- Used for: software modules, data pipelines, UI components

### Fault Tree Analysis (FTA)
- Top-down: start with the harm, trace back to root causes
- Used for: investigating incidents, compliance

### HAZOP (Hazard and Operability Study)
- Guide-word based: "what if data is missing?", "what if the system is slow?"
- Used for: complex workflows, AI/ML systems

### SWIFT (Structured What-If Technique)
- Brainstorming-based: team asks "what if..." questions
- Used for: early-stage design review

---

## 4. Software-Specific Risk (IEC 62304 + ISO 14971)

IEC 62304 classifies software safety classes:

| Class | Description | Example | Risk Management Effort |
|-------|-------------|---------|----------------------|
| **Class A** | No injury possible | Patient appointment scheduler | Minimal |
| **Class B** | Non-serious injury possible | Drug interaction checker | Moderate |
| **Class C** | Death or serious injury possible | Radiation therapy planning software | Full |

For AI/ML-based software (bioinformatics pipelines):
- **Data quality risk:** training data bias → incorrect prediction
- **Model drift risk:** model degrades over time → outputs become unreliable
- **Explainability risk:** black-box model → can't audit decisions
- **Reproducibility risk:** non-deterministic output → can't validate

**Risk controls for AI/ML:**
- Golden dataset regression tests
- LLM-as-a-Judge for output quality
- Human-in-the-loop for critical decisions
- Continuous monitoring (model drift detection)

---

## 5. Documentation Requirements (for Audit)

| Document | Content | When |
|----------|---------|------|
| **Risk Management Plan** | Scope, criteria, methods, roles | Start of project |
| **Hazard Analysis / FMEA** | List of hazards, risk estimation, controls | During development |
| **Risk Control Verification** | Evidence that controls work | After implementation |
| **Risk Management Report** | Summary, residual risks, conclusions | Before release |
| **Post-Market Surveillance Plan** | How to monitor in production | Before release |
| **Post-Market Surveillance Report** | Real-world data, risk updates | Ongoing |

### What auditors look for:
- Traceability: every hazard → risk control → verification
- Logic: "why did you decide this risk is acceptable?"
- Completeness: all intended uses and foreseeable misuse considered
- Updates: risk file is maintained, not a one-time exercise

---

## 6. Connection to Other Standards

| Standard | Role | How it connects |
|----------|------|-----------------|
| **ISO 13485** | QMS for medical devices | Risk management is a required process |
| **IEC 62304** | Software lifecycle | Software safety classification drives risk effort |
| **ISO 14971** | Risk management | This standard (the core process) |
| **21 CFR Part 820** | US FDA QSR | US equivalent, harmonised with ISO 13485 |
| **IEC 62366** | Usability engineering | Use errors → hazards → risk control |

---

## 7. Interview Questions (BostonGene)

**"What is your experience with risk management for medical devices?"**
→ Honest answer: "I have deep experience with risk-based testing and quality risk management in non-regulated environments (Wimark, OrangeHRM). I understand ISO 14971 principles and have studied them in preparation for this role. My AI/ML validation expertise is directly transferable to regulated software."

**"How would you implement risk management for an AI-based bioinformatics pipeline?"**
→ Key points: data quality gates, model drift monitoring, golden dataset regression, human validation loop for critical outputs, explainability layer

**"What's the difference between risk management per ISO 14971 and risk-based testing?"**
→ ISO 14971: formal, documented, auditable, covers patient safety
→ Risk-based testing: informal, QA-focused, covers product quality
→ Both identify hazards/high-risk areas and prioritise controls

---

## Sources

- [ISO 14971:2019 — Medical devices — Application of risk management](https://www.iso.org/standard/72704.html)
- [IEC 62304:2006 + AMD1:2015 — Medical device software lifecycle processes](https://www.iso.org/standard/59378.html)
- [FDA Guidance — Content of Premarket Submissions for Software](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/content-premarket-submissions-management-cybersecurity-medical-devices)
- [ISO/TR 24971:2020 — Guidance on ISO 14971](https://www.iso.org/standard/74437.html)
