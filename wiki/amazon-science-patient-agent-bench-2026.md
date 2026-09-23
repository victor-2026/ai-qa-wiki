---
source: "amazon-science-patient-agent-bench-2026.md"
ingested: "2026-09-24"
---

## PatientAgentBench – A Benchmark for Patient‑Facing Health AI Agents  

**Published:** Amazon Science, 29 July 2026  

### Summary  
PatientAgentBench is a reproducible, clinician‑vetted evaluation suite that measures how well AI agents interact with patients in realistic, multi‑turn conversations. Unlike traditional medical‑knowledge tests or provider‑centric tool benchmarks, it focuses on the *agentic* behavior required when an AI acts on a patient’s behalf—gathering information, navigating clinical workflows, triaging safely, and escalating when needed. The benchmark creates synthetic patient charts, generates a corresponding clinical vignette, and runs a dialogue between a “patient agent” (which presents the case) and the health‑AI system under test. An LLM‑as‑jury panel scores each interaction across six safety‑oriented dimensions, providing both numeric grades and explanatory feedback. Because the scenarios are generated on‑the‑fly and no fixed answer key exists, the benchmark resists training‑data contamination while remaining extensible to new domains and patient populations.

### Key Concepts  

| Concept | What it means for the benchmark |
|---------|---------------------------------|
| **Synthetic patient record** | A fully artificial health record (demographics, meds, history) that serves as the ground truth for the conversation. |
| **Stateful healthcare sandbox** | A simulated environment containing tools (e.g., appointment scheduler, prescription manager) that the evaluated agent can invoke, mirroring real‑world clinical systems. |
| **LLM‑as‑jury panel** | A set of large language models prompted with over 100 clinician‑validated criteria, organized into six rubric dimensions: |
| • Clinical safety | Detects omissions (e.g., missing suicide‑hotline info) and fabricated facts. |
| • Triage quality | Assesses whether the agent correctly escalates or de‑escalates based on risk. |
| • Workflow accuracy | Checks proper use of tools and adherence to care pathways. |
| • Task completion | Verifies that the patient’s request (e.g., refill, appointment) is fulfilled. |
| • Clinical helpfulness | Measures educational value without overstepping into diagnosis. |
| • Conversational quality | Evaluates empathy, clarity, and coherence. |
| **Reusable rubrics** | The same criteria apply to any conversation, eliminating per‑conversation bespoke scoring and enabling fair comparison across models. |
| **Conservative safety bias** | The jury is tuned to flag potential safety issues more readily than to miss them, mirroring regulatory expectations. |
| **Contamination‑proof design** | Dynamic scenario generation prevents models from memorizing answers, ensuring that scores reflect reasoning rather than recall. |

### Practical Applications  

1. **Model selection for healthcare products** – Developers can run multiple foundation‑model families through PatientAgentBench and compare per‑dimension scores to choose a base model that meets safety thresholds before fine‑tuning.  
2. **Iterative agent design** – The rubric’s explanatory feedback pinpoints exact failure modes (e.g., crisis‑resource omission, information fabrication), guiding targeted improvements in tool‑integration logic or prompt engineering.  
3. **Regulatory readiness** – Because the benchmark mirrors real clinical workflows and enforces a conservative safety stance, results can be incorporated into compliance dossiers for FDA or other health‑authority submissions.  
4. **Academic research** – Researchers studying multi‑turn clinical reasoning, tool‑using agents, or LLM‑based evaluation can use the open‑source pipeline to generate custom scenarios or extend the rubric to specialty domains.  
5. **Education & training** – Medical schools or health‑tech bootcamps can employ the sandbox to teach safe AI‑assisted patient interaction, exposing trainees to common pitfalls highlighted by the benchmark.  

### Getting Started  
The full framework—including the synthetic‑scenario generator, sandbox tools, dual‑agent conversation runner, and LLM‑as‑jury evaluation scripts—is available on GitHub. Users can run predefined seed distributions or define custom patient‑population profiles to stress‑test specific clinical pathways.  

---

### See also  
- [Cige An Agentic Ai Test Case Standard 2026](wiki/cige-an-agentic-ai-test-case-standard-2026.md)  
- [SOP‑Bench: Benchmarking AI Agents on Real‑World Business Procedures 2026](wiki/amazon-science-sop-bench-agents-business-procedures-2026.md)  
- [ICLR 2026 Agent Benchmarking Self Improvement](wiki/iclr-2026-agent-benchmarking-self-improvement.md)  
- [Arxiv Rebuild Dossier Mechanically Enforced Specs 2026](wiki/arxiv-rebuild-dossier-mechanically-enforced-specs-2026.md)  
- [Continuous Prompt Evaluation: LLM Judges and Live Signals (Kiro 2026)](wiki/kiro-continuous-prompt-evaluation-llm-judges-2026.md)

---
*Source: [raw/amazon-science-patient-agent-bench-2026.md](../raw/amazon-science-patient-agent-bench-2026.md) · Generated by wiki_llm.py (Groq)*





<!-- backlinks-start -->
### Backlinks
- [Amazon Science Blog: Catalog for AI-QA (2026)](wiki/amazon-science-blog-catalog-2026.md)
- [Arxiv Rebuild Dossier Mechanically Enforced Specs 2026](wiki/arxiv-rebuild-dossier-mechanically-enforced-specs-2026.md)
- [Cige An Agentic Ai Test Case Standard 2026](wiki/cige-an-agentic-ai-test-case-standard-2026.md)
- [Continuous Prompt Evaluation: LLM Judges and Live Signals](wiki/kiro-continuous-prompt-evaluation-llm-judges-2026.md)
- [Iclr 2026 Agent Benchmarking Self Improvement](wiki/iclr-2026-agent-benchmarking-self-improvement.md)
- [SOP‑Bench: Benchmarking AI Agents on Real‑World Business Procedures](wiki/amazon-science-sop-bench-agents-business-procedures-2026.md)
<!-- backlinks-end -->
