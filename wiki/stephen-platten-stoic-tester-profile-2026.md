---
source: "stephen-platten-stoic-tester-profile-2026.md"
ingested: "2026-08-17"
title: "Stephen Platten — The Stoic Tester (AI Testing & Assurance)"
type: people
updated: "2026-08-17"
tags: ["qa", "ai-testing", "people", "inbound-contact"]
---

## Stephen Platten – “The Stoic Tester”

**Location:** Kingston upon Hull, England  
**Current role:** Principal Consultant, Inspired Testing (since Apr 2024)  
**Community presence:** Ministry of Testing Ambassador, Head of Accreditation (UKITB), AI Advisor (GSDC)  
**Followers:** 13 319 on LinkedIn; newsletter “The Stoic Tester” – ~3 000 weekly readers  

---

### Summary  

Stephen Platten blends a military‑grade engineering background with a modern focus on AI‑enabled software quality. After serving as an RAF fast‑jet engineer, where software assurance had direct safety implications, he moved into commercial QA, eventually becoming a recognized thought‑leader on AI testing, risk‑based testing, and TMMi‑driven maturity. His LinkedIn persona “The Stoic Tester” promotes evidence‑based decision‑making, critical thinking, and a stoic mindset that keeps anxiety and ego out of the testing process. Through consulting, standards work, and a weekly newsletter, he influences both practice and policy for AI‑centric quality assurance.

---

### Key Concepts  

| Concept | Description | Why it matters for AI‑QA |
|---------|-------------|--------------------------|
| **AI Evaluation & Goodhart’s Law** | Metrics become targets and lose diagnostic power. Platten illustrates this with hallucination‑rate testing: a model can “cheat” by answering less or staying overly literal, reducing the measured error without becoming more useful. | Highlights the need for *holistic* evaluation—beyond surface metrics—to ensure AI delivers trustworthy, complete answers. |
| **Stoic Critical Thinking** | Borrowing from Stoicism, he stresses logical rigor, awareness of cognitive biases, and emotional detachment when confronting test failures or stakeholder pressure. | In the AI era, rapid model updates and opaque behavior demand disciplined reasoning to avoid knee‑jerk fixes. |
| **Risk‑Based & Evidence‑Based Testing** | Prioritise tests that mitigate the highest business or safety risks, and back decisions with measurable evidence rather than intuition. | Aligns AI testing budgets with impact, ensuring resources target the most damaging failure modes (e.g., policy‑drift hallucinations). |
| **QA Maturity (TMMi)** | Uses the Test Maturity Model integration framework to assess organisational readiness for AI testing, from ad‑hoc to optimised processes. | Provides a roadmap for enterprises transitioning from manual QA to AI‑centric pipelines. |
| **Accreditation & Standards Governance** | Leads UKITB accreditation for testing training providers, ensuring curricula cover emerging AI topics and maintain rigor. | Guarantees a pipeline of professionals equipped with up‑to‑date AI‑testing skills. |

---

### Practical Applications  

1. **Designing Robust AI Evaluation Suites**  
   - Combine quantitative metrics (hallucination rate, latency) with qualitative checks (usefulness, completeness).  
   - Apply “metric‑target” awareness: rotate or augment metrics to prevent models from gaming a single score.

2. **Implementing a Stoic Test Culture**  
   - Conduct post‑mortems that focus on *facts* and *process* rather than blame.  
   - Use Platten’s newsletter prompts (“Overcoming Anxiety in the Age of AI”) as team‑wide reflection exercises.

3. **Risk‑Based Test Planning for AI Products**  
   - Map AI use‑cases to potential failure impacts (regulatory, financial, safety).  
   - Allocate testing effort proportionally, using TMMi levels to gauge current capability and identify gaps.

4. **Building AI‑Ready QA Teams**  
   - Leverage UKITB‑accredited courses to upskill testers in prompt engineering, model interpretability, and AI governance.  
   - Foster Communities of Practice (as done at Inspired Testing) to share tooling PoCs, automation frameworks, and evaluation dashboards.

5. **Strategic Consulting Deliverables**  
   - Produce maturity assessment reports, AI‑testing roadmaps, and governance models for enterprises adopting LLMs or decision‑support systems.  
   - Provide white‑papers on AI assurance, covering topics from data provenance to continuous monitoring (telemetry).

---

### Engagement with Victor Ematin (2026-08)

**Signal type:** 🔵 **INBOUND** — Stephen approached Victor after Victor's Article 12 (AI testing agents field report, ~Aug 14). Strong network signal: published field reports attract senior peers.

**Thread (structured output validation):**
- Victor asked: "How are you validating the structured output today: schema-first contracts, LLM-as-a-judge, or both?" (context: CRM data + conversations → structured docs; what matters = schema contracts on output, per-field traceability to source record, golden set to catch drift)
- Stephen replied: "A combination of them plus human evaluation against set metrics"
- Alignment: combination (contracts catch structural drift, judge catches semantic drift, human eval catches business-context drift) + versioned golden set with mutation-style checks on contracts = anti-overfit guardrail

**Follow-up:** reply SENT (2026-08-17): 3-level drift framing (structural/semantic/business) + versioned golden set with mutation-style checks on contracts + question on golden-set versioning and human-eval re-runs as CRM data changes. Awaiting response.

---

### Community Impact  

- **Ministry of Testing Ambassador** – hosts webinars on AI risk, critical thinking, and quality leadership.  
- **AI Advisor, GSDC** – shapes national AI‑testing curricula and outreach programs.  
- **Newsletter “The Stoic Tester”** – disseminates concise, philosophy‑infused insights to a growing audience of QA professionals.

---

### See also  

- [`30 AI-Focused Interview Questions for Manual QA`](wiki/30-ai-questions-manual-qa-2026.md)  
- [`Vector Databases in Fintech`](wiki/vector-databases-fintech-2026.md)  
- [`AI/QA Testing Topics Map`](wiki/topics-map.md)  
- [`QA Skills → AI Roles Transition Guide`](wiki/qa-ai-transition-guide.md)  
- [`AI QA Evidence Layer: Validation, Evals, Guardrails, and Telemetry`](wiki/ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md)  

---
*Source: [raw/stephen-platten-stoic-tester-profile-2026.md](../raw/stephen-platten-stoic-tester-profile-2026.md) · Generated by wiki_llm.py (Groq)*

















<!-- backlinks-start -->
### Backlinks
- [30 AI-Focused Interview Questions for Manual QA](wiki/30-ai-questions-manual-qa-2026.md)
- [AI QA Evidence Layer: Validation, Evals, Guardrails, and Telemetry](wiki/ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md)
- [AI/QA Testing Topics Map](wiki/topics-map.md)
- [Agent Skills – Google/Kaggle Whitepaper (May 2026)](wiki/google-kaggle-agent-skills-whitepaper-2026.md)
- [Apparently We Need a Testing Mindset After All (Klain)](wiki/keith-klain-testing-mindset-after-all-2026.md)
- [QA Skills → AI Roles Transition Guide](wiki/qa-ai-transition-guide.md)
- [Stoic Tester Goodharts Law Ai Evaluation 2026](wiki/stoic-tester-goodharts-law-ai-evaluation-2026.md)
- [Vector Databases in Fintech](wiki/vector-databases-fintech-2026.md)
- [Wayne Roseberry Testers Do More Than Users 2026](wiki/wayne-roseberry-testers-do-more-than-users-2026.md)
<!-- backlinks-end -->
