# Source: https://getautonoma.com/blog/how-to-test-an-mcp-server

---
title: "How to Test an MCP Server: 3 Layers That Actually Work"
description: "A complete, runnable guide to testing an MCP server: protocol tests, pytest unit tests, tool-selection evals, transport tests, and auth checks."
date: "2026-07-22"
canonical: "https://getautonoma.com/blog/how-to-test-an-mcp-server"
authors:
  - "Tom Piaggio"
tags:
  - "Testing"
  - "API"
  - "AI"
---

# How to Test an MCP Server: 3 Layers That Actually Work

> **Testing an MCP server** means verifying three independent layers: that the protocol handshake and tool listings are well-formed, that each tool's underlying function returns correct values and handles errors deterministically, and that a calling LLM actually selects the right tool with the right arguments given a natural-language prompt. Model Context Protocol testing also has to account for transport (stdio, HTTP, SSE) and auth, each of which fails in its own way.

> A runnable companion repo for testing an MCP server: a minimal two-tool MCP Python server, MCP Inspector CLI protocol checks, deterministic pytest unit tests on the tool functions, a Claude-based tool-selection eval harness with semantic assertions across N runs, and transport-specific (stdio/HTTP/SSE) and auth/authorization pytest suites. [Source on GitHub](https://github.com/Autonoma-Tools/how-to-test-an-mcp-server).

Search "how to test an MCP server" today and you'll find a listicle naming three tools, a paragraph of prose describing test categories, and not one runnable command. You will not find a single assertion, a single pytest file, or a single test that accounts for the fact that an MCP server has to survive three different transports and an authorization boundary that most write-ups never get to.

That gap is what this guide closes. Every layer below is something you can run in the next twenty minutes: the MCP Inspector CLI commands, the pytest suite against the tool functions, the tool-selection eval harness, the transport tests, and the auth tests. None of it is prose describing what testing "should" look like.

## Why Testing an MCP Server Is Different From Testing a Normal API

A normal API has one boundary to test: does the request produce the right response. An MCP server has that same boundary, but it sits behind a second one that didn't exist in traditional API testing at all. Before your tool's code ever runs, an LLM has to read a natural-language request, decide which of your exposed tools applies, and construct arguments for it. Get the response contract right and the tool selection wrong, and the user still gets a broken experience, even though every individual function returned exactly what it was supposed to.

That second boundary is genuinely new, and it's genuinely probabilistic. You cannot unit test "did the model pick the right tool" the way you unit test "did the discount function apply the right percentage," because the same prompt, run twice, can produce two different tool calls. Treating it like a normal deterministic test (one run, exact match, pass or fail) produces a suite that's either flaky for no diagnosable reason or so loose it never catches a real regression.

The fix is to stop treating MCP testing as one layer and start treating it as three, each with a different failure mode and a different testing technique.

> **Diagram:** A three-layer test pyramid for an MCP server: protocol and handshake tests at the base, deterministic tool-function unit tests in the middle, and non-deterministic tool-selection evaluation at the top.

*Each layer needs a different testing technique, because each layer fails in a different way. Running all three the same way is how MCP test suites end up either flaky or useless.*

| Layer | What It Tests | Tooling | Failure Signal |
| --- | --- | --- | --- |
| Protocol &amp; handshake | Message shape, tool listing | MCP Inspector CLI | Malformed JSON-RPC, missing fields |
| Deterministic units | Tool function logic | pytest | Wrong return value, unhandled edge case |
| Tool selection | LLM picks tool + args | Eval harness, N runs | Wrong tool, wrong arguments, flakiness |

## Layer 1: Protocol and Handshake Tests With the MCP Inspector CLI

The first layer doesn't touch an LLM at all. It asks a narrower question: does your server speak MCP correctly. Can a client complete the initialize handshake, list your tools, call one, and get back a well-formed JSON-RPC response with the fields a client actually needs.

Here's a minimal MCP server exposing two tools, a weather lookup and a ticket-creation tool, that the rest of this guide tests against:

[src/server.py](https://github.com/Autonoma-Tools/how-to-test-an-mcp-server/blob/main/src/server.py)

The [MCP Inspector](https://github.com/modelcontextprotocol/inspector) ships a CLI mode built for exactly this, no browser UI required, which makes it scriptable in CI. Here's a runnable check script that starts the server over stdio, lists its tools, calls one, and asserts on the JSON-RPC shape with `jq`:

[scripts/inspector_checks.sh](https://github.com/Autonoma-Tools/how-to-test-an-mcp-server/blob/main/scripts/inspector_checks.sh)

Run it and you get a real pass or fail, not a visual inspection. If `tools/list` comes back missing a schema field, or `tools/call` returns a result without a `content` array, the script exits non-zero and names the field that broke. That's the whole point of testing this layer separately: a broken handshake produces the exact same symptom to an end user as a bad tool-selection decision ("nothing happened"), but the fix is completely different, so you want to be able to rule this layer out in seconds.

> **E2E coverage for your AI features.** Autonoma runs agentic end-to-end tests on every pull request. [Try Autonoma](https://autonoma.app).

## Layer 2: Deterministic Unit Tests on the Tool Functions

Once the protocol layer is confirmed sound, the next question has nothing to do with MCP at all: does the tool's underlying function do the right thing. This is the layer most teams already know how to write, and the mistake most MCP guides make is skipping straight past it to talk about "testing the AI," as if the plain old function underneath weren't there.

Here are the two tool functions themselves, written so they can be imported and called directly, independent of any MCP framing:

[src/tools.py](https://github.com/Autonoma-Tools/how-to-test-an-mcp-server/blob/main/src/tools.py)

And here's the pytest suite against them, calling the functions directly and asserting on return values, error handling, and edge cases, with no LLM and no protocol layer anywhere in the loop:

[tests/test_tools_unit.py](https://github.com/Autonoma-Tools/how-to-test-an-mcp-server/blob/main/tests/test_tools_unit.py)

This suite runs in milliseconds and belongs in your normal CI pipeline, not in some separate "AI testing" track. If `create_ticket` silently accepts an empty title, or `get_weather` throws an unhandled exception on an unrecognized city instead of returning a structured error, this is where that gets caught, before you've spent any time wondering whether the model picked the wrong tool.

## Layer 3: Does the LLM Actually Pick the Right Tool

This is the layer that doesn't exist in traditional API testing, and it's the one most guides either skip or wave at with a sentence. Given a natural-language prompt, does the model select the correct tool, with correct arguments, reliably enough to trust in production.

"Reliably enough" is the operative phrase, because a single run tells you almost nothing. A tool-selection test that asserts once and calls itself done is really just checking that the happy path is possible, not that it's dependable. The pattern that actually works: run the same scenario N times (10 to 20 is a reasonable floor), and assert on semantic or property-based conditions rather than an exact match, because "the model called `create_ticket` with a title containing the word 'refund'" is a testable property, while "the model's arguments exactly equal this hardcoded dict" is a test that breaks the moment the model rephrases a field for no functional reason.

Here's an eval harness that does exactly this against the two tools from Layer 2, calling the model directly, running each scenario N times, and asserting on tool name plus argument properties instead of exact values:

[eval/eval_tool_selection.py](https://github.com/Autonoma-Tools/how-to-test-an-mcp-server/blob/main/eval/eval_tool_selection.py)

When a scenario in this harness fails intermittently, resist the urge to read that as "the model is unreliable" and move on. Flakiness here is a signal about your test, not a verdict on the model: either the assertion is stricter than the tool actually needs to be (you're checking an exact phrase where a substring or a type check would do), or the tool's description and the prompt are ambiguous enough that a reasonable model could go either way. Tighten the tool description or loosen the assertion, then re-run. This same category of problem, testing whether an agent picks the right tool out of several plausible ones in the first place, is worth its own dedicated pass if your server exposes more than a couple of tools.

A suite that's green across all three of these layers tells you something real: the handshake works, the functions are correct in isolation, and the model reliably picks the right one. It does not tell you the one thing your users actually experience, which is whether calling that tool changed anything correctly inside the application it was supposed to act on.

## How Autonoma Verifies What MCP Tool Calls Actually Do

Every layer above stops at the same boundary: it confirms that a tool call was well-formed and that the response looked valid. A `create_ticket` call that returns `{'{'}"status": "success", "id": "T-4821"{'}'}` passes Layer 1 (valid JSON-RPC), Layer 2 (the function returned the shape it's supposed to), and Layer 3 (the model picked the right tool with the right arguments). None of that confirms a ticket actually exists in the system a user will look at next, with the right title, assigned to the right queue, visible to the right account. Testing the tool call is not the same as testing the outcome.

That's the layer [Autonoma](https://getautonoma.com) covers, and it's deliberately outside the three layers above rather than a fourth version of them. Autonoma's Planner reads your codebase (routes, components, the flows a tool call is supposed to trigger) and plans end-to-end test cases around what should happen in the running application, including generating the database state each scenario needs. The Executor runs those planned tests against a live [PreviewKit](https://getautonoma.com) preview environment per PR, driving the actual UI the way a user would after that tool call fired. The Reviewer then classifies what it finds, a real bug in the resulting application state, an agent execution error, or a mismatch between the plan and what changed, and decides whether the plan needs to adapt or whether the failure is real. Diffs Agent keeps the whole suite current as the codebase evolves, so the coverage doesn't quietly rot the next time a tool's behavior changes.

Mapped against the structure of this guide: Layers 1 through 3 answer "did the MCP layer behave correctly." Autonoma answers the question none of them can, which is "did the thing the tool call was supposed to do actually happen, correctly, inside the application." Both answers matter. Neither one substitutes for the other.

## Testing Transport-Specific Behavior: stdio, HTTP, and SSE

Everything so far has been transport-agnostic on the surface, but the transport your MCP server runs over changes what can actually go wrong, and almost nothing published on MCP testing addresses this directly. A test suite that only exercises stdio locally and never touches an HTTP or SSE deployment is missing entire categories of production failure.

> **Diagram:** Test flow for three MCP transports: stdio process lifecycle, HTTP request and auth checks, and SSE event-stream and reconnection checks.

*Same tool call, three different ways to break: a zombie process on stdio, a missing 401 on HTTP, a connection that never resumes on SSE.*

| Transport | Lifecycle Model | Auth Mechanism | Failure Mode |
| --- | --- | --- | --- |
| stdio | Parent-spawned subprocess | Process-level trust | Zombie process, no exit check |
| HTTP | Stateless request/response | Bearer token per request | Missing 401, stale token accepted |
| SSE | Long-lived event stream | Token at connect, per-event checks | No reconnect, missed events |

### stdio: Process Lifecycle Tests

For stdio, the server is a subprocess your client owns. The failure modes are process failure modes: does the process actually start and complete the handshake, does a tool call over stdio return before the process itself is killed, and critically, does the process exit cleanly when the client disconnects instead of leaking a zombie that slowly exhausts file descriptors in a long-running host.

[tests/test_transport_stdio.py](https://github.com/Autonoma-Tools/how-to-test-an-mcp-server/blob/main/tests/test_transport_stdio.py)

### HTTP: Request, Response, and Auth Header Tests

Over HTTP the server is stateless per request, which means every single request needs to independently prove it's authorized. The tests that matter here check the boundary conditions your happy-path integration test never touches: a request with no `Authorization` header, a request with an expired token, a request with a token that's valid but scoped to fewer tools than it's asking for.

[tests/test_transport_http.py](https://github.com/Autonoma-Tools/how-to-test-an-mcp-server/blob/main/tests/test_transport_http.py)

### SSE: Event-Stream Parsing and Reconnection Tests

SSE looks like HTTP until the connection drops. The two things worth testing directly: that your client correctly parses incremental `data:` frames as they arrive rather than waiting for the stream to close, and that a dropped connection actually reconnects and resumes rather than silently going quiet. This second one is the failure mode that never shows up in local development and always shows up in production behind a load balancer.

[tests/test_transport_sse.py](https://github.com/Autonoma-Tools/how-to-test-an-mcp-server/blob/main/tests/test_transport_sse.py)

## Testing Authorization and Token Handling

The last gap almost nothing covers: does your MCP server actually enforce who's allowed to call what. Three patterns matter, and they're distinct enough to need separate tests.

First, rejection: a tool call with no credential, or an invalid one, should be refused before any tool logic runs, not caught by a downstream error handler. Second, scoping: two valid credentials with different permissions should see different tool lists and different results, not the same tools with a client-side filter that a slightly different request could bypass. Third, expiry and refresh: a token that was valid when the connection opened but expires mid-session should cause the next call to fail cleanly, and a refreshed token should be picked up without requiring a full reconnect.

[tests/test_auth.py](https://github.com/Autonoma-Tools/how-to-test-an-mcp-server/blob/main/tests/test_auth.py)

Notice what these tests are not checking: whether the tool call worked. They're checking whether it was allowed to be attempted at all, which is a separate question a lot of MCP servers answer with "we trust whatever's inside the network perimeter," right up until the perimeter has a gap.

## Putting the Layers Together

None of these five categories replace each other. Protocol tests catch a broken handshake in seconds without needing a model call. Deterministic unit tests catch a logic bug in the function itself, independent of whether the LLM ever picks it correctly. Tool-selection evals catch the case where everything downstream is correct but the model reaches for the wrong tool, and they're the one layer where a single run is worthless and a stable pass rate across N runs is the actual signal. Transport tests catch the failure modes specific to how your server is actually deployed, not how it behaves on localhost over stdio. Auth tests catch the boundary a working demo never exercises.

Run all five, and you know your MCP server speaks the protocol correctly, does the right thing internally, gets picked correctly by the model calling it, survives its actual transport, and enforces who's allowed to call it. What you still don't know, and what none of these layers can tell you, is whether the actual application behind that tool call ended up in the state your user needed it to be in. Autonoma supplies that final behavioral E2E check against the deployed application, so a green MCP suite can be paired with proof that the user-facing outcome occurred.

## Frequently Asked Questions

## Frequently Asked Questions

### What is MCP testing?

MCP testing is the practice of verifying a Model Context Protocol server across three layers: the protocol and handshake layer (is the JSON-RPC message shape correct, are tools listed properly), the deterministic layer (do the underlying tool functions return correct values and handle errors), and the tool-selection layer (does a calling LLM pick the right tool with the right arguments given a natural-language prompt). It also covers transport-specific behavior (stdio, HTTP, SSE) and authorization.

### How do you validate MCP responses?

Validate MCP responses at the protocol layer with the MCP Inspector CLI, checking that tools/list and tools/call return well-formed JSON-RPC results with the expected fields present. Then validate the same responses at the function layer with deterministic unit tests that call the tool's underlying implementation directly, bypassing the LLM, and assert on exact return values and error handling.

### How do you test MCP tools without involving an LLM?

Import the tool's underlying function directly in a unit test and call it with the same arguments an LLM would pass. This tests the deterministic logic (validation, error handling, edge cases) in isolation from tool selection, and it runs in milliseconds instead of requiring a live model call.

### How many times should you run a tool-selection eval?

Run each tool-selection scenario at least 10 to 20 times before trusting the pass rate, since a single run tells you nothing about consistency. If a scenario fails intermittently, treat that as a signal to loosen an overly strict assertion or clarify an ambiguous tool description and prompt, rather than assuming the model is simply unreliable.

### Do stdio, HTTP, and SSE transports need separate tests?

Yes. Each transport fails differently. stdio tests need to check process lifecycle (clean spawn, clean exit, no zombie processes). HTTP tests need to check request and response semantics including auth headers and status codes. SSE tests need to check event-stream parsing and reconnection behavior after a dropped connection. A test suite that only covers one transport will miss failure modes specific to the others.

---

This is the markdown variant of <https://getautonoma.com/blog/how-to-test-an-mcp-server>, served by content negotiation (`Accept: text/markdown`) and also available directly at <https://getautonoma.com/md/blog/how-to-test-an-mcp-server>.

Other agent surfaces: [llms.txt](https://getautonoma.com/llms.txt), [resource catalog](https://getautonoma.com/.well-known/ai-catalog.json), [developer portal](https://getautonoma.com/developers), [sitemap](https://getautonoma.com/sitemap.xml).
