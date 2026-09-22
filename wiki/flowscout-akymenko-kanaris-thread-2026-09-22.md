---
source: "flowscout-akymenko-kanaris-thread-2026-09-22.md"
ingested: "2026-09-22"
---

## FlowScout – An Honest‑AI Browser‑Crawling Assistant  

**What is it?**  
FlowScout is an open‑source (Apache‑2.0) autonomous browser agent built on Playwright.  
Its purpose is to **discover the actual user flows that exist in a web application** and to **compare those flows with the test cases you already maintain** (TestRail, Zephyr, Xray, qTest, CSV, etc.).  
Unlike many “AI‑testing” tools that generate tests and ask you to trust their predictions, FlowScout only reports **what it can verify by interacting with the UI** – which pages can be reached, which actions are possible, and which of those are already covered by your test suite.

---

### Key Concepts  

| Concept | Explanation |
|---|---|
| **Real‑flow discovery** | The crawler follows links, forms, and navigation exactly as a human would, respecting the current user identity, feature‑flag state, and configuration. |
| **Risk‑aware crawling** | Destructive actions (logout, external redirects) are skipped by default; mutating actions (checkout, delete) run only when the user opts‑in. |
| **Three‑way deduplication** | Near‑identical paths are merged, delivering a concise set of distinct flows instead of dozens of redundant traces. |
| **Gap analysis** | FlowScout cross‑references discovered flows with existing test‑case repositories, highlighting uncovered flows and auto‑generating draft pytest‑Playwright specs. |
| **Multi‑persona support** | Separate runs can be seeded with different user roles, feature‑flag configurations, or sitemap entries, producing persona‑specific coverage reports. |
| **Transparent failure handling** | CAPTCHA or challenge pages are reported as “unresolved” rather than silently bypassed, preserving honesty about what the tool could not verify. |
| **Residue awareness** | The author identifies three classes of **unsolved** problems: <br>1. **Multi‑actor handoffs** – workflows that require sequential actions by different users. <br>2. **One‑shot irreversible transitions** – actions that consume a token or change state permanently. <br>3. **Time‑dependent flows** – processes gated by schedulers or long waiting periods. |

---

### Practical Applications  

| Scenario | How FlowScout Helps |
|---|---|
| **Regression‑ready coverage reporting** | Generate a baseline map of reachable flows for a given release; quickly spot newly introduced gaps after a feature flag change or UI redesign. |
| **Test‑suite audit** | Import your existing test case export (CSV, TestRail, etc.) and let FlowScout tell you which real flows are already exercised and which are missing. |
| **On‑boarding of new QA engineers** | The visual flow map and automatically generated pytest‑Playwright skeletons give newcomers a concrete starting point without guessing the UI structure. |
| **Compliance & security reviews** | By explicitly avoiding destructive actions unless approved, the tool can be run against production‑like environments without risking data loss. |
| **Continuous‑integration pipelines** | Integrate the CLI to run nightly on a staging build; the diff report highlights newly added or removed flows, alerting teams to unintended UI changes. |
| **Bug discovery** | As demonstrated by a user who uncovered a hidden overlay that blocked navigation, FlowScout surfaces real UI defects that might be invisible to static analysis. |

---

### Limitations & Open Challenges  

* **Undiscovered vs. uncovered behavior** – FlowScout reports only what it can reach under the supplied identity and configuration. If a workflow is hidden behind a permission or a data condition that wasn’t part of the run, the tool will correctly label it “not found,” but the analyst must recognise that this does not guarantee completeness.  
* **Multi‑actor handoffs, irreversible actions, and time‑gated flows** remain outside the current automation scope; addressing them will require coordinated multi‑session orchestration or state‑snapshot techniques.  

---

### Getting Started  

1. Clone the repo: `git clone https://github.com/igorakymenko-create/FlowScout.git`  
2. Install dependencies (`pip install -r requirements.txt`).  
3. Provide a Playwright‑compatible config, a user credential set, and optionally a `sitemap.xml`.  
4. Run `flowscout crawl --role employee --opt‑in‑mutations`.  
5. Review the generated HTML report and the pytest‑Playwright drafts.  

Community contributions are encouraged, especially around the three “genuine residue” problems.

---

### See also  

- [Bolton & Bach: LLM Sandwich Test и ментальная гигиена против антропоморфизации](wiki/bolton-bach-llm-sandwich-hygiene-protocol-2026.md)  
- [AI Testing Tools Landscape — Hands‑On Pilots & Verdicts (2026‑09‑09)](wiki/ai-testing-tools-landscape-hands-on-2026-09.md)  
- [How to Test if RAG Is Retrieving the Right Context](wiki/autonoma-rag-retrieval-2026.md)  
- [Rotation Without Relevance: Why Mutants Must Be Filtered Before Seeding](wiki/rotation-without-relevance-preseed-mutant-filtering-2026.md)  
- [BrowserStack Blog — Breakpoint 2026 & Test Companion](wiki/browserstack-blog-breakpoint-2026-test-companion.md)

---
*Source: [raw/flowscout-akymenko-kanaris-thread-2026-09-22.md](../raw/flowscout-akymenko-kanaris-thread-2026-09-22.md) · Generated by wiki_llm.py (Groq)*


<!-- backlinks-start -->
### Backlinks
- [AI Testing Tools Landscape — Hands-On Pilots & Verdicts (2026-09-09)](wiki/ai-testing-tools-landscape-hands-on-2026-09.md)
- [Bolton & Bach: LLM Sandwich Test (2026-09-19)](wiki/bolton-bach-llm-sandwich-hygiene-protocol-2026.md)
- [BrowserStack Blog — Breakpoint 2026 & Test Companion](wiki/browserstack-blog-breakpoint-2026-test-companion.md)
- [How to Test if RAG Is Retrieving the Right Context](wiki/autonoma-rag-retrieval-2026.md)
- [Rotation Without Relevance: Why Mutants Must Be Filtered Before Seeding](wiki/rotation-without-relevance-preseed-mutant-filtering-2026.md)
<!-- backlinks-end -->
