# AI in QA Issue #17 — Butch Mayhew (Jul 6, 2026)

**Raw:** `raw/ai-in-qa-issue-17-butch-mayhew-2026-07-06.md`

## Key Takeaways

### 1. Tests That Pass for Wrong Reasons
Claude Code generates E2E tests that look correct and pass green — but survive UI changes without failing. Ankur Tyagi + Rishi Raj Jain reproduced this on an Airbnb clone.

**Maps to:** Article 7 (Skills Reliability Experiment) — 0% lift because tests wrote tests that confirmed existing assumptions. Article 8 thesis: skills as behavior blueprints, not code gen.

### 2. AI Agents > Framework Debate
Dmitry Shyshkin: "Selenium vs Playwright is a distraction. AI agents are the real change." The skill shift is from writing selectors to reading agent output.

### 3. Safari MCP Server (Apple)
Apple shipped Safari MCP server — AI agents can now inspect live browsers natively. New vector for cross-browser agentic testing.

### 4. Other Resources
- Andrew Knight: 4-hour LinkedIn Learning course "Playwright + AI"
- Julia Pottinger: CLAUDE.md files for test suites guide
- Alan Richardson: Playwright screencast API for defect evidence videos

## Relevance
- Confirms the "tests pass for wrong reasons" risk identified in Articles 7-8
- Safari MCP = new capability for Playwright Agents comparison
- CLAUDE.md for test suites = spec-first test approach (matches BDD harness in Article 8)

**Newsletter:** https://aiinqa.com/ai-in-qa-issue-17/








<!-- backlinks-start -->
### Backlinks
- [Ai In Qa Issue 17 Butch Mayhew 2026 07 06](wiki/ai-in-qa-issue-17-butch-mayhew-2026-07-06.md)
<!-- backlinks-end -->
