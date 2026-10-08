# Igor Goldshmidt: Trajectory vs Response + Model-Migration Acceptance (Oct 2026)

**Source:** owner-saved profile/activity dump (Goldshmidt.webarchive, /tmp/goldshmidt.txt), posts 2d/1w/1mo read in full. Author: Igor Goldshmidt, https://www.linkedin.com/in/igorgolds/ — Principal QE Architect (AI-Assisted Testing & Agentic Workflows), Fractional Head of QA, ex-Moovit/Via/Gett, works with Skipper Soft. Tier proposal: Tier 1 (reason: trajectory/response doctrine + migration matrix, both load-bearing; track: peer exchange, W1 decides outreach).

## 1. Refund eval: trajectory × response (1w post, strongest)

Agent returns correct refund amount, polite, 0.91 vs reference — GREEN. Trace: fetch order + issue refund, but the policy-required eligibility check never called; order 42 days old vs 30-day cutoff. Correct-looking answer walking around the exact rule. "The test was green because the test was looking at the text. That is not an agent failure. It is an oracle failure."

Doctrine: checking an agent = two independent axes (Trajectory: right tools/order/arguments; Response: right final answer). Four combinations; genuinely dangerous = trajectory-wrong/response-right ("Green in CI, incident in production"). Google ADK as specimen: trajectory threshold quietly lowered 1.0→0.8, response metric counts word overlap (blind to "not"), golden dataset captured from the agent's own behavior.

## 2. September-1 model migration (1mo post)

Pipeline green, no commit — but the model underneath changed (Copilot deprecations Sep 1). Replacement must preserve engineering OUTCOME, not words: detect same critical defect; generate tests proving business rules; right tools + permissions; report timeout/missing-source as incomplete (not confident success); stay in latency/cost/review budget. Requires acceptance portfolio: frozen tasks, seeded failures, hard gates, diagnostic measures, suggestion-only canaries, explicit rollback.

## 3. Threshold discount composite (2d post)

Agent PR: >= implemented as >; suite had 50/150, nothing at exactly 100; reviewer LGTM. "AI bugs" = old species (ODC 1992 wrong-condition), new escape profile (compiles, pretty, nothing ugly to snag). Four questions to keep apart: what is wrong / what surfaced it / where found / which check should have stopped it — only the last tells what to fix. (Rhymes Haim's > vs >= post same week — independent convergence.)

## QA interpretation

- Trajectory/response split = Hari's behavior-check + QBurst L2 in practitioner words; the dangerous quadrant is our seeded-break target (fluent wrong-path).
- Migration acceptance portfolio (seeded failures + hard gates + canaries + rollback) = our per-risk-tier gate + Spotify rollback-capacity, vendor-independent.
- "Golden dataset captured from the agent's own behavior" = examiner-author contamination, pairs with Jason's held-out validation demand.
- ProQuality '26 tip from same feed: Hidden Cost of AI-Assisted SDLC (Sobko, EPAM) — cost per ACCEPTED result vs per generated output (W2 ledger thesis, lead only).

## See also

- [[runtime-authorization-ai-agents-2026]] — permissions, eligibility enforcement
- [[breaklight-ai-testing-methodology-whitepaper-2026]] — held-out validation, judge blindness
- [[qburst-quality-engineering-framework-validating-agent-behavior-2026]] — L2 decision validation
- [[anthropic-spotify-quality-at-ai-speed-2026]] — rollback capacity, verification pacing
