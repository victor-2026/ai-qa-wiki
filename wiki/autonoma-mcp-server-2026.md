# How to Test an MCP Server: 3 Layers That Actually Work

**Source:** https://getautonoma.com/blog/how-to-test-an-mcp-server
**Date:** 2026-07-22
**Tags:** #autonoma #mcp #tool-calls #api-testing #transport
**Raw:** [autonoma-mcp-server-2026.md](../raw/autonoma-mcp-server-2026.md)

---

## What It Is (3-5 bullets)

- **Three-layer MCP test pyramid**: protocol/handshake (JSON-RPC shape), deterministic tool-function units (logic correctness), and non-deterministic tool-selection eval (LLM picks right tool + args) — each fails differently, each needs different technique (Tom Piaggio, Autonoma, 2026-07-22, repo `Autonoma-Tools/how-to-test-an-mcp-server`).
- **Runnable two-tool server**: `src/server.py` (weather + ticket) plus Inspector CLI script `scripts/inspector_checks.sh`, pytest unit suite `tests/test_tools_unit.py`, and Claude-based eval harness `eval/eval_tool_selection.py` all executable in ~20 minutes.
- **Transport and auth as separate surfaces**: stdio (process lifecycle/zombie), HTTP (per-request bearer, 401, scoping), SSE (event-stream parsing, reconnect behind LB) — each with dedicated pytest suite; auth tests scoping, rejection, expiry/refresh (beyond "trust inside perimeter").
- **Tool-call vs outcome boundary explicit**: Layers 1-3 prove call well-formed and function correct; Autonoma behavioral E2E (Planner → live PreviewKit → Reviewer/Diffs Agent) proves ticket actually exists with right title/queue/visibility — both required, neither substitutes.

## Key Patterns / Techniques (table or bullets)

| Pattern | How it works (from raw) | File in repo |
|---------|-------------------------|--------------|
| **Layer 1 — Protocol/handshake** | MCP Inspector CLI: `initialize`, `tools/list`, `tools/call` over stdio, assert JSON-RPC with `jq` shape (`content` array, schema fields) | `scripts/inspector_checks.sh`, `src/server.py` |
| **Layer 2 — Deterministic units** | Import tool function directly, no LLM/protocol; assert return value, error handling, edge cases; ms, every commit | `src/tools.py`, `tests/test_tools_unit.py` |
| **Layer 3 — Tool selection eval** | N=10-20 runs per scenario, semantic/property assertion (title contains "refund", not exact dict equality); model direct call | `eval/eval_tool_selection.py` |
| **Flake routing rule** | Intermittent fail → assertion too strict (loosen to substring/type) OR description/prompt ambiguous (tighten description) — never "model unreliable" | Harness note |
| **stdio transport tests** | Spawn, handshake, call, clean exit on disconnect — zombie leak fails suite | `tests/test_transport_stdio.py` |
| **HTTP transport tests** | No auth → 401, expired token → 401, valid but under-scoped → filtered tool list / 403; per-request bearer validated | `tests/test_transport_http.py` |
| **SSE transport tests** | Incremental `data:` frame parsing, dropped connection reconnect + resume — the prod-behind-LB failure local never shows | `tests/test_transport_sse.py` |
| **Auth/authorization tests** | Rejection before tool logic, scoping (two creds see different lists), expiry mid-session + refresh without reconnect | `tests/test_auth.py` |

> Each layer needs a different discipline: Inspector for shape, pytest for logic, N-run semantic eval for selection — running all three the same way yields flaky-or-useless.

## Relevance to QA/QE (table QA Action)

| QA Concern | Action |
|------------|--------|
| **"How to test MCP server" = prose, zero asserts** | Clone repo and run 5 categories: Inspector script + unit suite + tool-selection harness + transport suites + auth suite — paste-ready |
| **Same prompt, different tool call** | N=10-20 + property assertion (contains/type) not exact dict; 17/20 in required CI job, trend logged, not single-run pass/fail |
| **Happy-path only, prod transport skipped** | Cover all three transports; do not ship stdio-only suite to HTTP/SSE prod — each fails differently |
| **Zombie process / silent disconnect** | Add stdio exit-on-disconnect check and SSE reconnect+resume test — LB-induced quiet failure is the expensive one |
| **Auth = perimeter trust** | Enforce rejection + scoping + expiry/refresh in dedicated suite; valid but under-scoped cred must not see same tools via client filter bypass |
| **Tool response 200 ≠ app state correct** | Pair MCP suite (well-formed call) with behavioral E2E (ticket exists where user looks, correct fields) — Autonoma Planner/Executor on live preview |
| **Intermittent harness red** | Route to test strictness vs description ambiguity first; tighten tool description and prompt before threshold loosening |

## Critical Analysis (Strengths/Gaps)

**Strengths:**
- Three-layer pyramid is the cleanest MCP framing published — maps failure signal to tooling and shows why uniform technique fails; Table "Layer / What / Tooling / Failure Signal" is immediately gate-able.
- Runnable minimal server (2 tools) keeps example tractable while transport × auth matrix shows where real prod complexity lives — no hand-waving.
- Property-based N-run eval is the transferable pattern: same prompt 10-20x + semantic/contains check generalizes to any tool server, avoids exact-dict brittleness.
- Auth depth beyond typical "check 401" — scoping (different creds see different tool lists) and mid-session expiry/refresh are the gaps managed demos never exercise.

**Gaps:**
- 10-20 N-run floor asserted without cost/power trade-off; no guidance on full-set per PR vs sampled/scheduled subset for large tool catalogs.
- MCP Inspector CLI asserted via `jq` but response schema evolution (new required fields) and version pinning not addressed.
- Two-tool domain scales poorly to 20+ tools with overlapping descriptions — no tool-ranking/disambiguation harness or embedding-based description deduplication shown.
- SSE reconnect "behind LB" noted as key failure but LB timeout / idle-connection tuning (the usual root cause) not linked to test configuration.

## Worked Example (from raw)

- **Minimal server**: `src/server.py` exposes `get_weather` + `create_ticket` — protocol tests `tools/list` and `tools/call` validate JSON-RPC shape before LLM involved.
- **Unit isolation**: `src/tools.py` functions called directly; empty title or unknown city → structured error, not unhandled exception — caught in `tests/test_tools_unit.py` before model-pick question.
- **Selection harness**: scenario "refund request" → assert `create_ticket` called with title containing "refund" across N=15 runs; exact-phrase assertion would break on harmless rephrase.
- **Transport failures**: stdio zombie after client disconnect (exhausts FDs), HTTP stale token accepted, SSE never resumes after drop — each caught by transport-specific suite, missed by localhost stdio-only run.
- **Auth**: token valid but scoped to weather only → asking for ticket tool must see filtered list / refused call; expiry mid-session → next call fails cleanly, refresh picked up without reconnect.
- **Outcome gap**: `{"status":"success","id":"T-4821"}` passes all 3 layers yet ticket may not exist in DB with right queue — behavioral E2E drives UI/DB to confirm.

## FAQ Highlights (from raw)

- MCP testing = 3 layers: protocol shape + deterministic function + LLM tool-selection with N-run; plus transport (stdio/HTTP/SSE) and auth.
- Validate MCP responses via Inspector (`tools/list`, `tools/call` shape) then validate functions via direct unit import — shape ≠ logic.
- Test tool logic without LLM: import underlying function, call with intended args, assert values/errors — ms, deterministic.
- Run tool-selection 10-20 times per scenario; intermittent = tighten description or loosen assertion, not "model unreliable".
- Each transport needs separate tests: stdio lifecycle, HTTP headers/status/auth, SSE parsing/reconnect — one-transport suite misses whole categories.

## Reuse Checklist

- Clone `Autonoma-Tools/how-to-test-an-mcp-server`; run `scripts/inspector_checks.sh` and `pytest tests/test_tools_unit.py` to baseline green.
- Add `eval/eval_tool_selection.py` for own tools; write property assertions (`"refund" in title.lower()`, type checks) and wrap N=15; gate 13/15 in required CI job.
- Implement `tests/test_transport_stdio.py`, `test_transport_http.py`, `test_transport_sse.py` for deployed transports; make HTTP 401/scoping and SSE reconnect required.
- Implement `tests/test_auth.py`: unauthenticated rejection, two-credential scoping, mid-session expiry + refresh; gate before tool logic.
- Keep MCP suite (call correct) plus one behavioral probe (DB row / UI state correct) — map Layers 1-3 to "behaved correctly" and behavioral to "happened correctly" in gate.

## Cross-links

- Trajectory: [Testing Tool Calls](autonoma-testing-tool-calls-2026.md) — K-of-N, argument-accuracy, mock vs live — MCP harness is transport+auth extension
- Non-determinism: [Non-Deterministic Outputs](autonoma-non-deterministic-outputs-2026.md) — N-run sampling, threshold, practitioner rule for harness flakes
- Tool-call eval: [LLM Unit Testing](autonoma-llm-unit-testing-2026.md) — schema/string → similarity → judge ladder beneath selection eval
- Agent E2E: [How to Test an AI Agent E2E](autonoma-how-to-test-ai-agent-e2e-2026.md) — trajectory vs behavioral outcome distinction at feature level
- MCP/UCP: [MCP + UCP Protocols](mcp-ucp-protocols-2026.md) — open protocols for agentic QA, versioning context
- Streaming: [Streaming Responses](autonoma-streaming-responses-2026.md) — SSE-adjacent lifecycle/state-machine testing
- Guardrails: [AI Guardrails](https://getautonoma.com/blog/how-to-test-ai-guardrails) + [Prompt Injection](https://getautonoma.com/blog/how-to-test-for-prompt-injection) — auth-adjacent boundary testing
- Evidence: [AI QA Evidence Layer](ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md) — tool call = eval, DB/UI state = downstream validation
- Repo: [Autonoma-Tools/how-to-test-an-mcp-server](https://github.com/Autonoma-Tools/how-to-test-an-mcp-server)

## Reuse Notes

- Version-lock tool descriptions alongside tests — when selection flakes, diff description first; ambiguous overlap between tools is the cheapest fix.

---
*Ingested: 2026-08-31*
