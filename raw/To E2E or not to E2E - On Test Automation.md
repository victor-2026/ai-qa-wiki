# To E2E or not to E2E? — On Test Automation

**Source:** Email / Newsletter — On Test Automation (Bas Dijkstra / OnTestAutomation)
**Address:** Veenslagen 16, 3825 RV Amersfoort, Netherlands
**Topic:** When (not) to write an end-to-end test
**Date received:** 2026-08-24 (forwarded during holiday)

---

## Summary (gist of forwarded email, not verbatim full copy)

A manager/tech lead believes a feature *only* works if covered by an E2E test. The system has many moving parts; building/running/maintaining E2E will be Herculean, value unclear, while unit/integration coverage is already decent. How to handle?

Author's 20+ year heuristic — three sequential questions:

### 1) What is the information that we are looking for?
Define *what* "this" is and *why* it must be known before deploy. Does it directly impact customer or revenue? If no clear reason, case for a test — especially expensive E2E — is weak.

### 2) Is an E2E test the most efficient (or even the only) way to get that information?
Which components/layers actually produce that information? Which can be skipped? Often few pieces of info truly need true E2E; a combination of lower-level tests finds it cheaper/faster/more reliably. See linked blog post exercise (context differs but principle same).

### 3) Is automating that test worth the effort?
Cost = writing + running + maintaining. Benefit vs cost; the closer to "true" E2E, the harder the business case, especially as complexity grows.

General thought process only; specifics depend on context. No assumptions beyond that.

**Closing:** How do you decide when (not) to write an E2E test?

---

## Original excerpt (key paragraphs, preserved for citation)

> To E2E or not to E2E? That's a good question. During my holiday, someone in my network sent me an email with a very good question. I won't paste the entire email in here verbatim, but the gist of their question was [...]
> "My manager / tech lead / only believes that a particular feature of our system really works when there is an end-to-end test covering it. However, there are so many moving parts in the system that building, running and maintaining these tests will be a Herculean task, and I'm not sure that these end-to-end tests will add enough value. Also, we have a decent coverage on lower-level unit and integration tests in place already. How do I deal with this situation?"
> [...]
> What is the information that we are looking for? [...] What do they really need to know about your product before you deploy? And why is that information important? Does it directly impact the customer? Does it directly impact your revenue stream?
> Is an E2E test the most efficient (or maybe even the only) way to get that information? [...] Which components and layers can you skip?
> Is automating that test worth the effort? What's the cost of automating the test (including writing, running and maintaining it)? Do the benefits outweigh those costs?

---

## Why this matters for this wiki

- Complements `regression-suite-museum` (5 Questions Delete vs Keep) and `agentic-regression-testing` (what to delegate vs verify)
- Gives a negotiation frame for "manager demands E2E" without resorting to dogma
- Reinforces evidence-based QA: information need → cheapest reliable source → automation ROI

## Capture note
Saved verbatim excerpt + summarized framework for wiki ingestion. Full original available in email archive; do not republish entire newsletter verbatim beyond fair excerpt.
