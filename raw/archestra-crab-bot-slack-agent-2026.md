# Archestra: We Fix Small Bugs by Dropping a 🦀 in Slack (2026-09-10)

**Author:** Joey Orlando (Co-Founder, Archestra)
**Source:** https://archestra.ai/blog/fixing-small-bugs-from-a-slack-thread
**Context:** How their Crab Bot turns Slack bug reports into PRs, and how OpenAPPA controls where the agent can send the internal data it reads.

---

## TL;DR

A Slack bot + disposable GCP VM per task. Agent investigates bugs autonomously: provision VM, read Slack thread, fix, self-review with nitpicker, record demo video, post PR. Human only writes the report and clicks "Ship it". Security: OpenAPPA (Information Flow Control) blocks tool calls that would leak internal data to public destinations. Result: cost of a small bug fix ≈ cost of a bug report.

## The loop

1. Engineer drops a message ending with 🦀 in #task-feed Slack channel (one-liner + screenshot, no ticket/branch/repro).
2. Controller in cluster picks up request → provisions GCP VM pre-configured: archestra repo checked out, local k8s cluster, Tilt, headless Chromium, OpenAPPA, nitpicker.
3. Claude Code session starts pointing at the Slack thread ("read the thread first"), unmonitored.
4. Agent polls its own Slack thread — user can add follow-up messages mid-run; session gets a pointer to the thread and reads it itself (important for screenshots: agent inspects the actual image, not someone's description — excludes human factor).
5. Once PR open → session runs nitpicker (Arseny's tool): reviews diff with several models at once, merges verdicts, posts one comment. Session then treats that comment as review feedback on its own work: fixes valid issues, explains why it leaves the rest.
6. Session records its own demo: shot-scraper video (Playwright-powered, Simon Willison released Jun 2026) → posts video back into Slack thread.
7. Human watches video, types "Ship it", "Promote", reviews PR (#7371).

**Human actions in the whole loop:** describing bug, watching video, typing "Ship it", reviewing PR. Nobody set up env or pulled a branch.

## The uncomfortable part — why OpenAPPA

Tasks scale up: "our staging is slow, go figure out why" → agent needs read access to running system (pods, restarts, OOM kills, container logs, resource limits), call recordings, product analytics, Slack threads with prior diagnosis.

Setup: Claude session registered with MCP gateway, runs in their own Archestra deployment, can read staging k8s cluster, Slack, call recordings, analytics. Each tool read-only by construction, running with the credentials of the requester — session can't exceed its requester's access level.

**The lethal trifecta (Simon Willison) wired on purpose, unmonitored:** agent with read access to internal data (customer names, tenant data, cluster internals, prod screenshots) + network connection + web tools + pushing code to public GitHub. If a session decides to put a requester's name in a commit message, no human in loop catches it.

Prompt instructions (confidentiality section: neutral technical terms, never name customers) are "as reliable as the model's mood" — not direct control. References: Simon Willison's "challenger disaster for coding agents security" 2026 prediction.

## OpenAPPA — Information Flow Control policy engine

MIT-licensed, preview, RFC status (paper: arxiv 2607.24625, policy reference at openappa.com/contracts). Local policy engine: tracks restrictions on data the agent READ, checks each tool call BEFORE it runs.

Rules in their setup:
- Session starts unrestricted.
- Reading from an internal tool marks session as internal.
- Once internal → session can't publish to public destinations without authorized review (e.g., copying internal logs/config into a public GitHub issue). OpenAPPA blocks the tool call before it runs.

Covers MCP and CLI tools. Example: script checks which cluster a kubectl command reads; non-local cluster → output marked internal; cloud API reads marked internal; local dev left alone. LLM classifier as second line of defense for unrecognized commands.

"Giving it that access shouldn't also give it permission to publish the internal information it finds there."

## The verdict

Good at: small, well-described, self-contained fixes.
Not good at: anything requiring taste, architecture, argument — human stays in the loop. PRs open on private mirror, published to public repo only on human "Promote".
The tool didn't make them faster at hard work, but reduced cost of small bug fix to cost of a bug report. "an enormous amount of bugs are much more affordable and easier to fix than we've got used to thinking"

Open invitation to Simon Willison to try to break it — "It may be exactly the stress test this thing needs."

---

## Cross-references (in this wiki)

- `wiki/archestra-jev-100-agent-calls-benchmark-2026.md` — Jev benchmark (same company)
- Lethal trifecta / prompt injection: archestra blog what-is-a-prompt-injection, how-to-run-openclaw-securely
- nitpicker (arsenyinfo/nitpicker) — multi-model PR review, merges verdicts — same family as our mutation-matrix multi-judge pattern

## Relevance to VerdictGate / Article series

- **Agent self-review loop** (nitpicker → session treats review as feedback → fixes + explains) = "author reviews own work" BUT with an independent multi-model judge = externalizing the examiner. Direct example of "don't let a model grade its own homework" done right: judge is a separate tool, verified by 3+ models.
- **Info Flow Control (IFC) at the tool-call boundary** = real-world data-leak prevention that our Article 26/27 "silent false negative" talks about; leak = password = FN with no alarm.
- **Read-only-by-construction + credentials of requester** = least-privilege pattern for agents; mirrors attestation (evidence tied to requestor's scope).
- **"Cost of small fix → cost of report"** = delegation framing for Article 25 (delegating implementation not risk).
- OpenAPPA = potential to include in VerdictGate/vendor landscape as guardrail-layer reference (orchestration, not verdict layer on quality).