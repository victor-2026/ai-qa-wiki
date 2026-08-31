# How to Test Streaming AI Responses

**Source:** https://getautonoma.com/blog/how-to-test-streaming-ai-responses
**Date:** 2026-07-29
**Tags:** #autonoma #streaming #sse #typing-indicator #playwright
**Raw:** [autonoma-streaming-ai-responses-2026.md](../raw/autonoma-streaming-ai-responses-2026.md)

---

## What It Is (3-5 bullets)

- **Streaming as a lifecycle, not a value**: test the sequence idle → requested → first token → streaming → complete with an error branch off streaming, not just the finished string — most bugs (stuck indicator, wiped partial, missing retry) live mid-stream, not at the end (Tom Piaggio, Autonoma, 2026-07-29, repo `Autonoma-Tools/how-to-test-streaming-ai-responses`).
- **Runnable two-level harness**: `fake_stream_server.py` (FastAPI deterministic fake SSE with terminator/withhold and mid-stream cut params) serving minimal chat HTML, plus `tests/test_stream_protocol.py` (chunk/buffer/terminator), `tests/test_stream_failure.py` (mid-stream drop), `playwright/streaming-ui.spec.ts` (indicator + partial + retry), `.github/workflows/stream-tests.yml` on every commit.
- **Five assertion targets mapped to transitions**: every chunk must parse and buffer must only grow; terminator `data: [DONE]` or `finish_reason` must arrive inside a timeout; mid-stream drop must retain partial text and clear loading with retry; typing indicator on at request/off at first token (or completion) never stuck; final assembled output checked via intent/semantic invariant across N runs, never exact chunk text.
- **Two-level complement**: Level 1 fake-server tests catch what evals and finished-string checks structurally cannot; Level 2 real-browser behavioral tests catch what Level 1 cannot (detached listener, re-render wipe, scroll anchor fight) — Autonoma positioned as that Level 2 layer running behavioral checks against PreviewKit on each PR with Diffs Agent updating selectors.

## Key Patterns / Techniques (table or bullets)

| Target | Assertion (from raw) | Where exercised |
|--------|----------------------|-----------------|
| **Partial-response correctness** | Every delta parses, safely renderable (no unescaped fragment rewriting bubble), running `buffer.length` after chunk ≥ before — catches malformed delta or replacement-instead-of-append | `tests/test_stream_protocol.py` |
| **Stream completion** | Terminator must arrive within bounded timeout; client must leave streaming state once it does; hanging stream = broken, not paused; assert elapsed time per run, not once in debugger | `tests/test_stream_protocol.py` — timeout threshold per suite |
| **Error mid-stream recovery** | Deliberately abort at chunk ~6 or fulfill with truncated body; assert independently: partial text stays on screen, indicator clears (no forever spinner), retry control appears | `tests/test_stream_failure.py` + Playwright route interception |
| **Typing indicator state** | On at request, off at first token (or at completion — declare convention), off after error; DOM assertion, not protocol; most common bug is error-path forget to clear | `playwright/streaming-ui.spec.ts` — real DOM check |
| **Final assembled output** | Concatenated buffer checked via invariants (contains required fact, ends complete sentence, length bound) + semantic similarity across N runs; never assert on chunk content or count — both accidents of network timing and model sampling | `tests/test_stream_protocol.py` — run-it-five-times semantic assert |
| **Fake-server fixture** | FastAPI SSE streaming scripted tokens, params `cut_at_chunk`, `omit_terminator`; serves HTML with Ask/Response/Indicator/Retry — single fixture backs protocol + browser tests | `fake_stream_server.py` |
| **CI wiring without flake** | Run fake-server suite on every commit (no live model, localhost only); job-level timeout a few minutes to catch hang; keep per-test timeouts short; never retry a streaming test — fix wait condition instead | `.github/workflows/stream-tests.yml` |

> Evals score finished response; finished response exists only after every interesting failure has already happened — and a stuck spinner has no representation in the text stream, requiring DOM-level assertion.

## Relevance to QA/QE (table QA Action)

| QA Concern | Action |
|------------|--------|
| **Tests wait for full string and miss spinner bug** | Map lifecycle states explicitly and add assertions at each transition; include error-branch assertions — not just final text |
| **Streaming flakes in CI (30s timeout locally passed)** | Assert lifecycle transitions with bounded waits, not timing; give server boot delay, keep per-test timeout short; treat any test needing retry as assertion bug |
| **Chunk boundaries assumed stable** | Never assert on chunk content or count; assert on monotonic buffer growth and final-buffer invariants/semantic across N runs |
| **Indicator stuck 40s while text complete** | Drive real UI in Playwright; assert visible at request, hidden at first token, hidden after injected drop — error-path is the one nobody tests |
| **Mid-stream drop wipes partial or freezes** | Force drop at 60%: assert partial text retained + indicator cleared + retry shown — three independent DOM checks, not one protocol log |
| **Selector rots when chat component moves** | Split Level 1 (protocol you own, hermetic) from Level 2 (behavioral on deployed preview); use Diffs Agent or fixture-scoped selectors updated from diff |

## Critical Analysis (Strengths/Gaps)

**Strengths:**
- Lifecycle-as-state-machine makes a flaking-prone category tractable; five named transitions give failures a nameable reason instead of vague timing.
- Two-level harness cleanly separates hermetic protocol checks (cheap, runs every commit) from DOM behavioral checks (finds stuck indicator, wiped text) with the same fake fixture.
- Explicitly warns that chunk boundaries + live-model wording are both non-deterministic — correctly pushes final output to invariants/semantic across N runs.

**Gaps:**
- Terminator form (`data: [DONE]` vs `finish_reason`) left as "literal or field" — no guidance on abstracting over both or handling chunked terminator split across frames.
- No guidance on setting completion timeout per model/payload size or on distinguishing slow-first-token from slow-every-token.
- Scroll/anchor and re-render bugs named but only indicator/partial/retry are asserted in excerpted tests — broader UI jank surface not shown.
- No load or interleaving case (multiple concurrent streams, user sending second message mid-stream) and no auth/rate-limit path for SSE.

## Worked Example (from raw)

- **Stuck indicator report:** response finished in <2s, indicator spun 40s with complete text in DOM; suite that waited for full response never watched indicator state.
- **Protocol violation:** malformed delta with unescaped fragment rewrites bubble mid-stream — caught by per-chunk parse check; finished-string check would pass.
- **Cut at 60%:** `?cut_at_chunk=6` truncates stream; correct recovery = partial text visible, indicator cleared, retry button appears — vs broken = spinner forever + partial wiped.
- **Buffer monotonicity:** chunk 1 "Hello" (5) → chunk 2 "Hello world" (11) vs bug "world" (5) would be caught by `len(buffer_after) >= len(buffer_before)`.
- **CI hang:** stream withholds terminator; per-test timeout fails fast, job-level timeout prevents pipeline block — no retry added, wait condition fixed.

## FAQ Highlights (from raw)

- Test lifecycle: chunk parse + monotonic buffer, terminator inside timeout, mid-stream drop recovery, indicator transitions, final intent/semantic — not finished string.
- Use deterministic fake SSE server to force normal, no-terminator, and mid-drop; pair with small real-browser suite for DOM-only bugs.
- Flake is almost always timing-check or hidden retry papering over buffer/indicator/network race — fix wait, do not retry.
- Evals/judges cannot catch stuck indicator or wiped partial — they score text after all streaming bugs already happened; need live UI drive (Autonoma layer).

## Reuse Checklist

- Copy `fake_stream_server.py` into `fixtures/`; expose `GET /stream?script=hello&cut_at=6&omit_done=1` and serve `static/chat.html` with selectors `data-testid="indicator|response|retry"`.
- Add `tests/test_stream_protocol.py` patterns: loop deltas, `assert parses_jsonl(chunk)` and `assert len(buf_after) >= len(buf_before)`; bound terminator with `pytest-timeout 3s`.
- Add `tests/test_stream_failure.py`: start stream, `await page.route('**/stream', route => route.fulfill(truncated))`, then three DOM asserts on retry flow.
- Keep `playwright/streaming-ui.spec.ts` to three checks: `expect(indicator).toBeVisible()` at request, `toBeHidden()` at first-token event, `toBeHidden()+retry` after error injection.
- Wire `.github/workflows/stream-tests.yml` on every commit: boot fake server step with health wait, `pytest tests/test_stream* -m "not live"` with job `timeout-minutes: 5`; never add `retries:`.

## Cross-links

- Non-determinism: [Non-Deterministic Outputs](autonoma-non-deterministic-outputs-2026.md) — N-run semantic for final assembled buffer
- Prompt unit: [LLM Unit Testing](autonoma-llm-unit-testing-2026.md) — mocked vs live split mirrored by fake-server vs browser split here
- Evals pipeline: [LLM Evals in CI/CD](autonoma-llm-evals-cicd-2026.md) — deterministic every-commit lane is exactly this fake-server suite
- Feature gate: [QA a Generative AI Feature](autonoma-qa-ai-feature-2026.md) — streaming chat is an Actionable feature inside that six-step gate
- Agent trajectories: [Testing Tool Calls](autonoma-testing-tool-calls-2026.md) — indicator state machine parallels tool-call sequence assert; [Agent Memory](autonoma-agent-memory-2026.md) — carryover across streamed turns
- E2E & reliability: [How to Test an AI Agent E2E](autonoma-how-to-test-ai-agent-e2e-2026.md) — behavioral Stage 5; [Agent Reliability](autonoma-agent-reliability-2026.md) — canary on streaming regression
- Evidence: [AI QA Evidence Layer](ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md) — protocol = validation, indicator/partial = behavioral evidence
- Repo: [Autonoma-Tools/how-to-test-streaming-ai-responses](https://github.com/Autonoma-Tools/how-to-test-streaming-ai-responses)

## Reuse Notes

- Name indicator convention in code (`INDICATOR_OFF_ON=FIRST_TOKEN`) and assert that convention in the test name.

---
*Ingested: 2026-08-31*
