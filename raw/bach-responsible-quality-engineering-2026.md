# Responsible Quality Engineering — James Bach (Satisfice, 2026-09-22)

**Author:** James Bach
**Source:** https://www.satisfice.com/blog/archives/488069
**Context:** Satisfice blog (Software Testing for Serious People). Published 22 Sep 2026. Categories: Process Dynamics, Quality, Rapid Software Testing Methodology, RST. Fetched via webfetch. Digest candidate (satisfice.com добавлен в digest-config 2026-09-23).

---
**Дата:** 2026-09-22, James Bach

Quality engineering is not testing, although it may require testing. Also, most "quality engineers" don't do quality engineering. The people who do quality engineering are developers. Testers support that process by analyzing the quality of the product and providing feedback to developers as *part* of the quality engineering process.

**First principles:**
- **Quality is value to some person (who matters).** Always a judgment made in context — an assessment, not a measurement. A relationship between a person and a product. Without people, no quality.
- **Quality engineering = the systematic process of "creating quality"**: systematically satisfying someone who matters (other than yourself) + engineering a reliable and economical process by which the product comes into being. In complex systems, quality doesn't happen automatically.
- **A responsible process is a process for which some competent human is accountable** — a natural person with capacity, commitment, skills, reasonably prepared to explain, defend, and answer for the quality of that process. **Since an AI tool cannot be accountable for anything, it cannot enact or embody a responsible process.**
- Provider + receiver: at least one person creates the quality product, at least one person experiences it. If provider = receiver, you don't need quality engineering discipline.

**Quality Engineering Tetrad (Venn diagram):** product has four aspects that must be intentionally aligned (in the judgment of people who matter):
1. **Imagination** — conceiving what is good, understanding the product (both provider and receiver)
2. **Specification** — communicating/describing what will be built (provider) and explanation received (receiver)
3. **Delivery** — making it real
4. **Experience** — the receiver feels its effects

Where all four overlap = engineered quality (green zone, vs accidental quality). Testing = the process of assessing that alignment. All subsets can overlap without meaning quality is good — you still must validate idea-of-good matches what the client wants. And all of it must be done **reliably and at a reasonable cost**.

**Responsibility concepts (law & ethics):** Duty of care; Reasonable; Responsible; Contract (mutual assent, consideration, capacity, legality); Representation. Quality engineering is the opposite of mere trust — trust means you don't need to engineer quality; you need it when you want to *compel* quality into existence and *know* it is there. **"This matters in a world where people use AI tools... A tool cannot be held accountable... fault lies with the operator or the provider of the tool."**

**Mismatch analysis (when pairs don't overlap):**
- **Imagination ≠ Specification** — we aren't saying what we mean (or all we mean); often not a problem, but quality engineering depends on knowing minds and developing ideas/specs over time.
- **Imagination ≠ Delivery/Experience** — even fully/perfectly specified and delivered, may not fulfill needs/desires; needs evolve (Agile iteration), world changes, compromises across people. Product matches spec but not wants → enhancement request.
- **Specification ≠ Delivery/Experience** — ordinary bug; when definitely wrong vs claims → **defect** (RST: bug = threatens value; defect = direct contradiction of claims).
- **Delivery ≠ Experience** — correct product but user doesn't receive intended experience: platform/hardware problems outside developer control, user environment/attributes unanticipated, foreseeable misuse. Iterative+incremental delivery + strong feedback loop + configurability help.

QA relevance (digest): RST/context-driven lineage — systematic model (tetrad) for "engineered vs accidental quality"; AI cannot embody a responsible process (accountable human required); quality engineering = opposite of mere trust — verification-first; four mismatch classes as a coverage/eval rubric. Maps to Prachi/Bach RST wiki, Bolton/Bach sandwich protocol, Mutation Matrix human gate, Articles 21/26/27.