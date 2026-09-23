---
source: "arxiv-rebuild-dossier-mechanically-enforced-specs-2026.md"
ingested: "2026-09-23"
---

## Rebuild Dossier – Mechanically‑Enforced Specifications for Agentic App Rebuilds  
*Parker Fawcett – arXiv:2608.23616 (v3, 20 Sep 2026)*  

### Summary  
`rebuild‑dossier` is an open‑source framework that **locks an application’s public interface** (exact input‑output contract) before any source code is generated, and then **forces a one‑test‑at‑a‑time development loop** through automated checks. By separating the specification from the implementation, the tool prevents agents from “gaming” a static test suite and makes the rebuild process auditable. Empirical evaluation on two models and three benchmark apps shows:

1. A rule‑compliant agent can still miss a hidden test that a rule‑breaking agent passes, demonstrating that a passing test suite is not a guarantee of correctness.  
2. When compared with the baseline “source + one instruction” (AgentModernize), `rebuild‑dossier` ties on a tiny app but loses on a larger one only because the automated check was disabled, confirming that the **checking mechanism**, not the interface lock, drives the performance gap.  
3. A three‑level verification (agent report → automated log → final files) uncovers real defects—including a bug in the authors’ own logging code—that single‑level validation would miss.  

A stronger model repeated the full process three times without failure, whereas a weaker model could not complete a single run, highlighting the importance of model capability in following mechanically‑enforced specifications.

### Key Concepts  

| Concept | Description |
|---------|-------------|
| **Interface‑Locking** | The real API (function signatures, data types, I/O formats) is recorded and immutable before code generation. Agents must produce code that conforms exactly to this contract. |
| **One‑Test‑At‑A‑Time Building** | After each code edit, an automated checker runs a single, newly‑exposed test. The agent proceeds only when the test passes, preventing batch‑submission of many hidden tests. |
| **Three‑Level Evidence** | 1️⃣ Agent’s self‑generated report, 2️⃣ Machine‑generated execution log, 3️⃣ The actual source files. Cross‑checking these layers catches inconsistencies and hidden bugs. |
| **Gaming Resistance** | By withholding a subset of tests until after the agent’s submission, the framework eliminates the possibility of over‑fitting to a static suite. |
| **Model‑Dependent Process Fidelity** | Stronger LLMs can reliably follow the enforced workflow; weaker models tend to diverge, leading to incomplete rebuilds. |

### Practical Applications  

- **Software QA for AI‑Generated Code** – Integrate `rebuild‑dossier` into CI pipelines to ensure that any AI‑produced patch respects the declared API and passes incremental tests, reducing regression risk.  
- **Regulatory Auditing** – The three‑level evidence trail satisfies emerging standards that require transparent provenance for AI‑generated artifacts.  
- **Benchmarking Agent Capabilities** – Use the framework as a stress test for new LLMs or multi‑agent orchestrators, measuring not just final correctness but adherence to a mechanically‑enforced process.  
- **Educational Tooling** – Teach developers how to structure specifications before coding, reinforcing best practices in contract‑first design.  
- **Safety‑Critical Systems** – In domains where hidden failures are catastrophic (e.g., medical devices, autonomous control), the incremental test‑driven approach limits exposure to undiscovered bugs.  

### Limitations & Open Questions  

- The approach assumes the existence of a reliable test generator; poorly designed tests could still mask defects.  
- Scaling to large codebases may increase the number of incremental steps, potentially inflating compute cost.  
- Interaction with existing multi‑agent pipelines needs further study to determine how `rebuild‑dossier` can be combined with higher‑level planning modules.  

---

### See also  

- [`wiki/rotation-without-relevance-preseed-mutant-filtering-2026.md`](wiki/rotation-without-relevance-preseed-mutant-filtering-2026.md) – Rotation Without Relevance: Why Mutants Must Be Filtered Before Seeding  
- [`wiki/iclr-2026-agent-benchmarking-self-improvement.md`](wiki/iclr-2026-agent-benchmarking-self-improvement.md) – ICLR 2026 Agent Benchmarking Self‑Improvement  
- [`wiki/ai-agents-replace-team-entrepreneurs-mogilko-yampolskiy-2026.md`](wiki/ai-agents-replace-team-entrepreneurs-mogilko-yampolskiy-2026.md) – AI Agents Replace Team Roles: The 35‑Agent Startup Model  
- [`wiki/prompt-tips-and-skills.md`](wiki/prompt-tips-and-skills.md) – Prompt Tips & Agent Skills Architecture  
- [`wiki/autonoma-multi-turn-conversations-2026.md`](wiki/autonoma-multi-turn-conversations-2026.md) – How to Test Multi‑Turn Conversations and Context Retention  

---
*Source: [raw/arxiv-rebuild-dossier-mechanically-enforced-specs-2026.md](../raw/arxiv-rebuild-dossier-mechanically-enforced-specs-2026.md) · Generated by wiki_llm.py (Groq)*





<!-- backlinks-start -->
### Backlinks
- [AI Agents Replace Team Roles: The 35-Agent Startup Model](wiki/ai-agents-replace-team-entrepreneurs-mogilko-yampolskiy-2026.md)
- [Amazon Science Patient Agent Bench 2026](wiki/amazon-science-patient-agent-bench-2026.md)
- [How to Test Multi-Turn Conversations and Context Retention](wiki/autonoma-multi-turn-conversations-2026.md)
- [Iclr 2026 Agent Benchmarking Self Improvement](wiki/iclr-2026-agent-benchmarking-self-improvement.md)
- [Prompt Tips & Agent Skills Architecture](wiki/prompt-tips-and-skills.md)
- [Rotation Without Relevance: Why Mutants Must Be Filtered Before Seeding](wiki/rotation-without-relevance-preseed-mutant-filtering-2026.md)
- [Verge Rabbit Os3 Agent 2026](wiki/verge-rabbit-os3-agent-2026.md)
<!-- backlinks-end -->
