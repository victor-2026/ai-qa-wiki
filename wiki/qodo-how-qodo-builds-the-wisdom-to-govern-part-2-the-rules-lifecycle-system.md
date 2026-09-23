---
source: "qodo-how-qodo-builds-the-wisdom-to-govern-part-2-the-rules-lifecycle-system.md"
ingested: "2026-09-23"
---

## Qodo: The Rules Lifecycle System – Turning Scattered Standards into Governable Policies  

**Source:** Qodo blog, “How Qodo Builds the Wisdom to Govern – Part 2: The Rules Lifecycle System” (2026‑09‑23)  

### Summary  
Qodo’s Rules Lifecycle System is the governance layer that converts informal, repository‑level guidance into structured, traceable standards that can be automatically enforced across an organization. While the Context Engine (Part 1) supplies *what exists* in a codebase, the Rules system supplies *what must exist*—the policies, severities, scopes, and ownership that drive reliable code‑quality reviews. Rules are first‑class objects stored in the Qodo portal under **Review Standards**, each carrying metadata, examples, and a full lifecycle (creation → activation → deprecation).  

### Key Concepts  

| Concept | What it means | Why it matters |
|---------|---------------|----------------|
| **Rule record** | A fixed‑shape entity containing: name, enforcement text, compliant/non‑compliant examples, **Category**, **Severity**, **Scope**, and **Source type**. | Provides a machine‑readable, auditable definition that can be displayed to developers during a review. |
| **Category** | High‑level bucket (Security, Correctness, Quality, Reliability, Performance, Testability, Compliance, Accessibility, Observability, Architecture). | Enables reporting, prioritisation, and alignment with organisational risk models. |
| **Severity** | `Error` → must comply, `Warning` → default compliance, `Recommendation` → optional. | Distinguishes mandatory policies from best‑practice suggestions. |
| **Scope** | Path‑based boundary (global, repo‑wide, sub‑directory). | Guarantees a rule only applies where it is relevant (e.g., payments code). |
| **Source type** | Origin of the rule: *Authored*, *Extracted* (from repo files), *Mined* (from review history), *Library*, or *Compliance file*. | Tracks provenance for governance, change‑impact analysis, and de‑duplication. |
| **Rule lifecycle** | **Draft → Active → Deprecated → Retired**. Each transition records owner, timestamp, and rationale. | Prevents rule drift, supports audit trails, and lets organisations retire obsolete standards. |
| **Rule Miner** | Engine that analyses recent merged PRs, weighting reviewer ownership, recurrence, concentration, and dismissal signals to propose candidate rules. | Leverages existing human decisions to surface implicit standards without manual effort. |
| **Skill‑derived rules** | Skills (`SKILL.md` + assets) are treated as rule inputs; findings are attributed back to the skill name. | Guarantees traceability from enforcement back to the documented multi‑step process. |
| **Duplicate/conflict handling** | When multiple inputs generate the same rule, Qodo deduplicates and merges metadata, preserving the most authoritative source. | Avoids contradictory policies and reduces noise. |

### How Rules Enter the System  

1. **Authoring** – An admin writes a natural‑language policy; an AI assistant drafts a full rule record for review.  
2. **Import from repository files** – Qodo scans all files (e.g., `AGENTS.md`, `CLAUDE.md`, `RULE.md`, docs, ADRs) to locate enforceable statements, extracts them, and enriches with metadata. The rule’s scope defaults to the containing folder.  
3. **Mining from review history** – The Rule Miner processes the latest ~1 000 merged PRs per repo, surfacing repeated, ownership‑weighted feedback as candidate rules. Dismissed suggestions decay over time.  
4. **Extraction from Skills** – Skills that encode multi‑step processes become rule sources; any violation discovered via a skill is reported with a citation to that skill.  

All rules retain a pointer to their originating file or comment, enabling “where did this rule come from?” queries in the portal.

### Practical Applications  

| Use‑case | How the Rules Lifecycle System helps |
|----------|--------------------------------------|
| **Enterprise governance** | Provides auditable, severity‑aware policies that can be demonstrated to regulators or internal auditors. |
| **Consistent enforcement** | Scope‑based application prevents a rule from leaking into unrelated code (e.g., payments‑only checks). |
| **Continuous improvement** | Mining from PR feedback surfaces emerging standards, turning “tribal knowledge” into codified rules. |
| **Developer experience** | When a rule fires, developers see concrete compliant/non‑compliant snippets, reducing friction and education time. |
| **Risk management** | Categorisation and severity enable risk dashboards that highlight high‑impact violations (e.g., security errors). |
| **Policy deprecation** | Lifecycle tracking flags stale rules that have not triggered any violations for a configurable period, prompting review. |
| **Cross‑repo consistency** | Centralised rule definitions avoid the 500‑copy problem of per‑repo instruction files, ensuring uniform standards. |

### Summary of Benefits  

- **Scalability:** One rule can govern thousands of repositories without duplication.  
- **Traceability:** Every rule knows its source, owner, and change history.  
- **Governance‑ready:** Severity and lifecycle make rules suitable for compliance evidence.  
- **Automation‑friendly:** Structured format lets review agents evaluate code automatically and surface actionable feedback.  

---

### See also  
- [

---
*Source: [raw/qodo-how-qodo-builds-the-wisdom-to-govern-part-2-the-rules-lifecycle-system.md](../raw/qodo-how-qodo-builds-the-wisdom-to-govern-part-2-the-rules-lifecycle-system.md) · Generated by wiki_llm.py (Groq)*
