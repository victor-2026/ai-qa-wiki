---
source: "iso-14971-risk-management-2026.md"
ingested: "2026-07-24"
title: "ISO 14971 – Risk Management for Medical Devices"
type: article
updated: "2026-07-24"
tags: [compliance]
---

## ISO 14971 – Risk Management for Medical Devices  

**Purpose** – Provides a systematic, auditable framework for identifying hazards, estimating and controlling risks, and monitoring their effectiveness throughout a medical device’s lifecycle (including SaMD and SiMD). When paired with IEC 62304 (software lifecycle) and ISO 13485 (QMS), it becomes the regulatory backbone for safe medical‑device software development.  

---

### Summary  
ISO 14971 requires a continuous, six‑step process that starts at concept design and ends with post‑market surveillance. Risks are expressed as the product of **severity** (impact of possible harm) and **probability** (likelihood of occurrence). Controls are implemented to lower the risk to an *acceptable* level; any remaining *residual risk* must be justified and documented. The standard emphasizes traceability—from each identified hazard to its control, verification evidence, and final risk‑management report—so auditors can verify completeness and logical decision‑making.  

---

### Key Concepts  

| Concept | What it means | Typical example |
|---------|---------------|-----------------|
| **Hazard** | Potential source of harm | Software crash during patient‑data upload |
| **Hazardous situation** | Condition exposing users to a hazard | Technician continues work after crash, unaware data loss |
| **Harm** | Injury or health damage | Misdiagnosis caused by missing data |
| **Risk** | Severity × Probability | High probability + catastrophic outcome = unacceptable |
| **Risk control** | Action that reduces risk | Auto‑save every 30 s + integrity check |
| **Residual risk** | Remaining risk after controls | Auto‑save may fail if storage is full – requires monitoring |
| **Acceptability criteria** | Pre‑defined thresholds for severity and probability that define “acceptable” | E.g., “Catastrophic risk must be improbable or eliminated” |

**Risk‑management process (6 steps)**  

1. **Risk analysis** – Define intended use, list hazards, estimate risk.  
2. **Risk evaluation** – Compare each risk with acceptability criteria.  
3. **Risk control** – Select, implement, and verify mitigation measures.  
4. **Residual‑risk evaluation** – Confirm that remaining risk is acceptable; otherwise iterate.  
5. **Risk‑management report** – Consolidate findings for regulatory review.  
6. **Post‑market surveillance** – Collect field data, reassess risks, and update the risk file.  

**Common analysis techniques**  

- **FMEA** – Bottom‑up, calculates a Risk Priority Number (Severity × Occurrence × Detection).  
- **Fault Tree Analysis** – Top‑down, traces a harm back to root causes.  
- **HAZOP** – Uses guide words (“missing”, “slow”) to explore process deviations.  
- **SWIFT** – Structured brainstorming of “what‑if” scenarios, useful early in design.  

**Software‑specific considerations (IEC 62304)**  

| Safety class | Typical function | Required effort |
|--------------|------------------|-----------------|
| **A** | Scheduling | Minimal documentation |
| **B** | Drug‑interaction check | Moderate verification |
| **C** | Radiation‑therapy planning | Full risk‑control lifecycle |

AI/ML pipelines add extra risk vectors: data‑bias, model drift, lack of explainability, and nondeterministic outputs. Controls include golden‑dataset regression, continuous drift detection, human‑in‑the‑loop review, and automated quality judges.  

**Documentation checklist for audit**  

- **Risk Management Plan** – Scope, criteria, methods, responsibilities.  
- **Hazard analysis / FMEA** – Detailed hazard list, risk estimates, proposed controls.  
- **Control verification** – Test evidence that mitigations work.  
- **Risk Management Report** – Summary of all activities, residual risk justification.  
- **Post‑Market Surveillance Plan & Report** – Ongoing monitoring strategy and findings.  

Auditors focus on **traceability**, **logical justification of acceptability**, **coverage of intended use and foreseeable misuse**, and **maintenance of the risk file** throughout the product’s life.  

---

### Practical Applications  

- **Design‑phase risk workshops** – Use SWIFT or HAZOP to surface early hazards before code is written.  
- **Iterative FMEA during sprints** – Update the risk register as new features are added, keeping the RPN current.  
- **AI/ML validation pipeline** – Combine golden‑dataset tests with drift alerts; document each as a risk control.  
- **Release gate** – Require a signed Risk Management Report before any regulatory submission or market launch.  
- **Post‑market monitoring** – Integrate field‑incident logs into the risk file; trigger re‑analysis when a new hazardous situation emerges.  

---

### See also  

- [AI Testing Frameworks — Complete Technical Reference](wiki/ai-testing-frameworks-complete.md)  
- [ISO/IEC 25000 (SQuaRE) – Software Quality Standards](wiki/iso-25000-square-quality-2026.md)  
- [Autonoma Open Source & Architecture (June 2026)](wiki/autonoma-open-source-self-driving-2026.md)  
- [AI Quality Characteristics](wiki/quality-characteristics.md)  
-











<!-- backlinks-start -->
### Backlinks
- [AI Quality Characteristics](wiki/quality-characteristics.md)
- [AI Testing Frameworks — Complete Technical Reference](wiki/ai-testing-frameworks-complete.md)
- [Autonoma Open Source & Architecture (June 2026)](wiki/autonoma-open-source-self-driving-2026.md)
- [ISO/IEC 25000 (SQuaRE) — Software Quality Standards](wiki/iso-25000-square-quality-2026.md)
<!-- backlinks-end -->

---
*Source: [raw/iso-14971-risk-management-2026.md](../raw/iso-14971-risk-management-2026.md) · Generated by wiki_llm.py (Groq)*
