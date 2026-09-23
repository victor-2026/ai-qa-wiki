---
source: "bach-everyone-not-responsible-quality-2026.md"
ingested: "2026-09-23"
---

## Everyone is **NOT** Responsible for Quality  
*James Bach – Satisfice Blog (2026‑02‑01)*  

### Summary  
James Bach challenges the popular Agile mantra “quality is everyone’s responsibility.” He argues that quality is a **role**, not a generic task that any team member can claim. By dissecting four common interpretations of “everyone is responsible,” Bach shows how each either collapses into a weak, unaccountable system or is only viable for tiny, tightly‑coupled teams. The remedy is to **localize responsibility**: each person owns the part of the product they control, while dedicated testing roles focus on uncovering problems. Clear role definitions and personal accountability, rather than vague collectivism, produce higher‑quality outcomes and reduce conflict of interest.

### Key Concepts  

| Concept | Explanation |
|---|---|
| **Testing as a Role** | Testing is a specialized activity aimed at *finding* trouble, not guaranteeing quality. Testers cannot “own” quality because they lack control over all product decisions. |
| **Four Misreadings of “Everyone is Responsible”** | 1. **Chain Analogy** – each link only checks its own work; the whole product is never examined, leading to hidden defects. <br>2. **Total Redundancy** – every person tests everything; only works in 2‑3 person teams. <br>3. **Herd Responsibility** – “the team” becomes a scapegoat; no individual is ever held to account. <br>4. **Weak Redundancy / Shared Aspiration** – everyone *wants* quality but lacks a common standard, knowledge, or control, so commitment is superficial. |
| **Shallow‑Testing Cop‑out** | Teams without dedicated testers produce simple checklists, automate them, and declare the product “good” once those checks pass. This masks deeper quality problems. |
| **Personal Responsibility Model** | • Each member knows and excels at their own job.<br>• Roles are explicitly linked to the quality aspect they can influence.<br>• Unpopular or difficult tasks are assigned to defined roles, ensuring they are performed. |
| **Control‑Based Accountability** | Quality of the whole system belongs to those who *control* the project (e.g., product owners, architects). Quality of a component belongs to its builder. Systematic testing belongs to the testing function. |

### Practical Applications  

1. **Define Explicit Quality Roles**  
   - Create a *Testing* role (or team) whose sole purpose is to design, execute, and evaluate tests.  
   - Assign *Component Ownership* to developers; they are accountable for the quality of the code they produce.  

2. **Establish a Shared Quality Standard**  
   - Conduct regular, rigorous debates to converge on a concrete definition of “acceptable quality.”  
   - Document the standard and make it part of the team’s Definition of Done.  

3. **Separate Decision‑Making Authority**  
   - Ensure the people who can *stop* a release (e.g., QA lead, product manager) have the authority to enforce the quality standard.  
   - Avoid situations where developers can unilaterally override test findings.  

4. **Support Cross‑Functional Collaboration**  
   - Require every role to provide reasonable support to others (e.g., developers supplying test hooks, testers sharing defect trends).  
   - Use clear hand‑off points rather than “the team will figure it out.”  

5. **Guard Against Herd Responsibility**  
   - When a defect surfaces, trace it to the *specific* role that had control over that artifact.  
   - Use post‑mortems to reinforce personal accountability rather than blaming “the team.”  

6. **Avoid Shallow Automation**  
   - Complement UI‑level checks with deeper property‑based, mutation, or exploratory testing.  
   - Treat passing automated scripts as *evidence* of quality, not proof of it.  

### Take‑away  

Quality cannot be diffused into a vague collective slogan. By **localizing responsibility**, aligning it with control, and maintaining a dedicated testing role, teams can achieve a robust, conflict‑free quality culture.

---

### See also  

- [`wiki/satisfice-blog-catalog-2026.md`](wiki/satisfice-blog-catalog-2026.md) – Overview of Satisfice blog posts from 2026.  
- [`wiki/ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md`](wiki/ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md) – AI QA evidence layer concepts.  
- [`wiki/bach-responsible-quality-engineering-2026.md`](wiki/bach-responsible-quality-engineering-2026.md) – Bach’s view on responsible quality engineering.  
- [`wiki/julia-pottinger-who-validates-ai-generated-code-2026.md`](wiki/julia-pottinger-who-validates-ai-generated-code-2026.md) – Accountability for AI‑generated code.  
- [`wiki/ai-testing-tools-landscape-hands-on-2026-09.md`](wiki/ai-testing-tools-landscape-hands-on-2026-09.md) – Recent AI testing tool evaluations.  

---
*Source: [raw/bach-everyone-not-responsible-quality-2026.md](../raw/bach-everyone-not-responsible-quality-2026.md) · Generated by wiki_llm.py (Groq)*


<!-- backlinks-start -->
### Backlinks
- [Satisfice Blog Catalog 2026](wiki/satisfice-blog-catalog-2026.md)
<!-- backlinks-end -->
