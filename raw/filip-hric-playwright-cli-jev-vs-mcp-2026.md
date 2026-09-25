# Filip Hric: Playwright CLI + Jev vs Playwright MCP (2026-09-25)

**Author:** Filip Hric ("I help developers make AI-written software reliable"; Playwright educator). LinkedIn post pasted by user 2026-09-25 (~1h old). Video referenced, not fetched (LinkedIn gate).
**Source:** user-pasted post verbatim substance below. Post-level claims (his measurements), not independently verified.
**Context:** Independent practitioner evidence for judgment-model economics: Jev+CLI beats MCP agent loop 98% cheaper + 2x faster on fuzzy instruction. Pattern = snapshot → judgment-model decides element (no LLM tool-call loop). Directly relevant: locator-decision via verdict model (cf. FlowScout Admin/PIM locator problem, testRigor/QAEverest drift); tier-model cost axis; W3 Jev track.
**Captured:** 2026-09-25 from user paste.

---

## Post substance

- Setup: Trello playground app; fuzzy instruction "Create new board, list and card".
- Playwright MCP path (baseline): snapshots → decisions thrown to LLM → execution with tool calls (Astra model). Standard agent loop.
- Jev path: hand Playwright CLI snapshot to Jev → Jev decides which element to interact with. Author notes further optimizable ("could be optimized even better").
- Result: 98% cheaper, 2x faster. Author "quite impressed".

## Use for us

- Judgment-as-locator-resolver: fuzzy instruction → element choice WITHOUT tool-call loop = the exact pattern our locator-drift cases need (FlowScout deep-nav, QAEverest id-drift). Cite as independent existence proof.
- 98%/2x figures: vendor-independent cost/latency datapoint for tier-model economics (judge-vs-loop); mark as single-task n=1, author-measured.
- MCP-loop cost anatomy (snapshot + LLM decision + tool calls per step) vs one-shot verdict = structural explanation transferable to our gate design.
- Follow-up: video details (task breakdown, token counts) if retrievable; Filip Hric = practitioner node worth watching (Playwright educator audience).
