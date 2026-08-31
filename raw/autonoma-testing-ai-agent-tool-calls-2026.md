# Source: https://getautonoma.com/blog/testing-ai-agent-tool-calls
# Fetched: 2026-08-31

---
title: "How to Test AI Agents That Take Actions (Tool Calls)"
description: "A runnable guide to testing tool-calling agents: right tool, right order, right arguments, mocked vs live calls, failure handling, and non-determinism."
date: "2026-07-24"
canonical: "https://getautonoma.com/blog/testing-ai-agent-tool-calls"
authors:
  - "Tom Piaggio"
tags:
  - "AI"
  - "Testing"
---

# How to Test AI Agents That Take Actions (Tool Calls)

> **Testing tool calling agents** means verifying the trajectory an agent produces when it acts: the ordered list of tool calls it made, with what arguments, captured and inspected after the fact. This is trajectory evaluation, a white-box check on tool selection, call order, and argument accuracy. An agent can pass all three and still be wrong, because none of them confirm the tool's effect on the running application was correct.

> A framework-neutral Python harness for testing tool-calling agents, plus one pytest file per assertion type: right tool, right order, right arguments, mocked vs live execution, failure handling, and non-determinism. Every test passes as written. [Source on GitHub](https://github.com/Autonoma-Tools/testing-ai-agent-tool-calls).

Search "trajectory evaluation" right now and you'll get the concept explained cleanly, in a vendor glossary, a framework doc, a conference talk transcript. What you won't get, in almost every case, is a test file. The term is well-covered. The assertions are not, and that gap is exactly where a team with a tool-calling agent in production gets stuck: they know what to check, they don't have anything to paste into their CI config.

This is that code. Every check below is real Python against a small harness in the companion repo, no SDK, no platform sign-up. The throughline: an agent can select the correct tool and still be wrong, because the argument it passed was wrong, and the two failures look identical from far away and completely different once you write the assertion.

## What Is Trajectory Evaluation?

A trajectory is just the list your agent produces as it works: which tools it called, in what order, with what arguments, and what came back. Trajectory evaluation is the practice of capturing that list and asserting against it after the run, instead of eyeballing a transcript or trusting that "it seemed to work."

That distinction matters because a tool-calling agent has a failure surface a plain function call doesn't. A function returns the right value or it doesn't. An agent decides which function to call, in what order relative to others, and what to pass it: three decisions that fail independently, usually in this order of frequency: wrong arguments most often, wrong order less often, wrong tool rarest once a system has real usage behind it.

> **Diagram:** An agent trajectory shown as a horizontal flow: user request, LLM decides, Tool A, Tool B, final response, with checkpoints for right tool, right order, right arguments, and right outcome.

*Trajectory evaluation covers tool selection, sequence, and arguments, the first three checkpoints. It stops at the boundary of the call. It never sees whether the tool's effect on the running application was actually correct.*

If your agent talks to tools over MCP rather than in-process function calls, the protocol and handshake layer underneath these checkpoints is its own testing surface, covered in our guide to [testing an MCP server](/blog/how-to-test-an-mcp-server). LangGraph formalizes a version of this same idea as a first-class concept in its evaluation tooling; if you're on that framework specifically, our [LangGraph testing guide](/blog/langgraph-testing) covers the framework-specific plumbing. Everything below is intentionally framework-neutral: an OpenAI-style tool-calling shape, a generic agent loop, no SDK required to follow along.

## The Harness: A Framework-Neutral Agent Loop You Can Actually Test

Every assertion in this guide runs against the same small harness: an `Agent` class that loops until it decides it's done, calling real tool functions and recording each call, its arguments, its result, and any error, into a trajectory. The only seam is `llm_decide`, a callable that looks at the request and the trajectory so far and returns the next action. Swap it for a real model call in production. In tests, it's a scripted fake, which is what makes the trajectory fully deterministic and inspectable instead of a black box you're hoping behaved.

[agent.py](https://github.com/Autonoma-Tools/testing-ai-agent-tool-calls/blob/main/agent.py)

The fixtures underneath it are just as small: an in-memory `AppState` standing in for your real application (here, a toy booking system with a `bookings` dict), three tool functions (`search_flights`, `book_flight`, `get_weather`) that read and write that state, and a `ScriptedLLM` fake that plays back a fixed list of decisions so every test below is reproducible without a live model call:

[conftest.py](https://github.com/Autonoma-Tools/testing-ai-agent-tool-calls/blob/main/conftest.py)

`book_flight` writes to `AppState.bookings`, real application state, which is what lets the mocking-vs-live section later demonstrate the difference between asserting on a call and asserting on an effect.

## Assertion One: Did the Agent Call the Right Tool

The cheapest and most common trajectory assertion, and the one nearly every existing write-up stops at: given a booking request, does `book_flight` show up in the trajectory at all, and does an irrelevant tool like `get_weather` stay out of it.

[test_right_tool.py](https://github.com/Autonoma-Tools/testing-ai-agent-tool-calls/blob/main/test_right_tool.py)

This test is worth having. It catches an agent that reaches for entirely the wrong capability, which does happen, especially as the tool list grows and tool descriptions start overlapping. It's also the least informative check in this guide, because it says nothing about whether the call that did happen was actually useful. That's the next two sections.

## Assertion Two: Did It Call Them in the Right Order

Tool selection can be perfect and the trajectory can still be broken if the sequence is wrong. Search-then-book is an obvious dependency (you can't book a flight ID you haven't looked up), but sequence assertions matter even without a strict data dependency: a weather check the user asked for before booking, if it runs after the booking already happened, is not the trajectory anyone asked for, even though every individual tool call, in isolation, looks fine.

[test_tool_order.py](https://github.com/Autonoma-Tools/testing-ai-agent-tool-calls/blob/main/test_tool_order.py)

The second test in that file uses a three-tool trajectory on purpose. Two-tool sequencing tests pass trivially once you've written one; three tools is where teams actually get bitten, usually by an agent that reorders steps under a slightly rephrased prompt.

## Assertion Three: Did It Call Them With the Right Arguments

This is the deepest section in this guide for a reason: argument accuracy is the highest-value trajectory assertion and the one almost every public write-up skips entirely. Tool selection and order both check that the right shape of thing happened. Argument accuracy checks whether it happened correctly, and it's where "the agent worked" and "the agent did what the user asked" stop being the same claim.

[test_argument_accuracy.py](https://github.com/Autonoma-Tools/testing-ai-agent-tool-calls/blob/main/test_argument_accuracy.py)

The third test in that file is deliberately the point of this whole guide: it books a flight one day off from what the user asked for, confirms tool selection passed, then confirms the argument-accuracy check correctly fails. If you only ship the first assertion type from this guide, ship this one instead. "It called `book_flight()`" is not a finding. "It called `book_flight()` with the date the user actually asked for" is.

## Right Tool, Right Order, Right Arguments: Still Not the Same as Right Outcome

Run every assertion above and get green across all of them, and here's what you actually know: the agent picked the correct tool, in the correct sequence, with arguments that match what the user asked for. Here's what you still don't know: whether that tool call changed anything correctly in the running application the user is looking at. The trajectory tests in this guide are white-box, they inspect the call. None of them touch the app itself.

That gap is easy to miss because it's invisible from inside the trajectory. A `book_flight()` call with the exactly right arguments can still fail if the booking service silently drops the write, if a downstream queue never processes it, or if the UI the user actually checks afterward never reflects the new state. Trajectory assertions have no way to see any of that, because by design they stop at the boundary of the call.

> **Diagram:** A diagram showing the agent correctly selecting book_flight, marked as the right tool, but passing the wrong date argument, which produces a passing trajectory assertion alongside a wrong outcome in the application.

*The agent picked the right tool. A tool-selection-only test passes here. The argument is still wrong, and so is the outcome in the running application, which only an argument-accuracy assertion catches.*

> **E2E coverage for your AI features.** Autonoma runs agentic end-to-end tests on every pull request. [Try Autonoma](https://autonoma.app).

## How Autonoma Verifies What the Tool Call Actually Did

Every test in this guide answers a version of the same question: did the agent fire the right call, in the right order, with the right arguments. None of them answer whether the call's effect showed up correctly where the user would actually look for it, a booking in the itinerary, a record in a dashboard, a state change reflected back in the UI. That's a different layer of testing, and it's the one [Autonoma](https://getautonoma.com) covers.

We built Autonoma to run behavioral, end-to-end tests directly against a running application rather than against a captured trajectory. Our Planner reads the codebase, the routes, the components, the flows a tool call is supposed to trigger, and plans test cases (including the database state each scenario needs) around what should actually happen after an action fires. The Execution Agent then drives the real UI in a live environment to confirm it: where a trajectory test in this guide asserts `book_flight()` was called with `{'{'}date: '2026-08-01'{'}'}`, the behavioral test asserts the booking actually appears in the itinerary screen with that date. The Diffs Agent keeps that coverage current as the codebase changes, so it doesn't quietly rot the next time a tool's downstream behavior shifts.

Mapped against this guide directly: the six assertion types above tell you the call was well-formed. Autonoma tells you the thing the call was supposed to do actually happened, correctly, where a user would see it. A tool-calling agent worth shipping needs both. Trajectory tests alone can't tell you the second half, and outcome tests alone would tell you something broke without narrowing down whether it was tool selection, ordering, or an argument, which is exactly what the trajectory layer is for.

## Mocking the Tool vs Exercising It Live

There are two legitimate ways to test a tool call, and they're not interchangeable, they check different things. Mock the tool and assert on the call: fast, no external dependency, and it isolates the agent's decision logic from whether the tool implementation happens to work today. Let the tool run for real and assert on the effect: slower, sometimes requiring test infrastructure, and it's the only way to know the action actually landed.

[test_mocking_vs_live.py](https://github.com/Autonoma-Tools/testing-ai-agent-tool-calls/blob/main/test_mocking_vs_live.py)

The mocked test proves the agent tried to book the right thing. The live test proves a booking record with the right passenger name actually exists afterward. Use the mock in tight, fast unit-style loops where you're iterating on the agent's decision logic itself. Use the live call whenever you need to know the action actually changed something, which is most of the time you care about tool calls at all.

## What Happens When the Tool Call Fails

Tools fail. Timeouts, rate limits, a downstream service returning a transient 5xx, none of that is exotic, it's Tuesday. What separates a production-ready agent from a demo isn't that its tools never error, it's what the agent does the moment one does: retry, fall back to a different approach, or surface the failure cleanly instead of swallowing it and reporting success anyway.

[test_failure_handling.py](https://github.com/Autonoma-Tools/testing-ai-agent-tool-calls/blob/main/test_failure_handling.py)

The first test injects exactly one transient failure and confirms the trajectory shows a failed attempt followed by a successful retry, with the booking actually present afterward. The second test injects a permanent failure and confirms the opposite: the trajectory has to show the error explicitly, and no booking should exist in application state. That second assertion catches a specific, ugly failure mode: an agent that catches the exception internally, says something reassuring to the user, and never actually completes the action. A trajectory test that only checks "did it crash" would miss that completely.

## Handling Non-Determinism Explicitly

A real tool-calling model, given the identical prompt twice, can produce two different, equally valid trajectories. Treat that like a normal deterministic unit test, one run, exact match, pass or fail, and you get a suite that's either flaky for reasons nobody can explain or so loose it stops catching anything real. Both failure modes come from the same root cause: applying single-run, exact-match thinking to a system that isn't single-run or exact.

The fix has two parts. First, run the scenario N times, not once, and require K of N to pass rather than treating any single failure as a verdict. Second, and this is the part teams get wrong even after adopting K-of-N: assert on the invariant, the tool name and the argument's shape or type, not the literal string. `date == '2026-08-01'` breaks the moment the model reformats a functionally identical date as `08/01/2026`. A check for "is this a date-shaped string" doesn't.

[test_non_determinism.py](https://github.com/Autonoma-Tools/testing-ai-agent-tool-calls/blob/main/test_non_determinism.py)

When a scenario in a suite like this fails intermittently, resist the instinct to conclude "the model is unreliable" and move on. Flakiness in a K-of-N eval is a signal about the test, not a verdict on the model: either the assertion is stricter than the tool actually requires, or the tool's description and the prompt are ambiguous enough that two reasonable interpretations exist. Loosen the assertion to the real invariant, or tighten the tool description, then re-run before you touch the pass threshold.

## Wiring This Into CI

The deterministic assertions (right tool, right order, right arguments, mocking, failure handling) behave like any other pytest suite: they run on every push, they either pass or they don't, and a red build blocks the merge. The non-determinism suite needs one adjustment: it's still a hard gate, but it's evaluating a pass rate over N runs rather than a single boolean, so it belongs in the same job, not a separate "best-effort" pipeline that nobody actually watches.

[.github/workflows/test.yml](https://github.com/Autonoma-Tools/testing-ai-agent-tool-calls/blob/main/.github/workflows/test.yml)

Keep both in the same required check. A K-of-N gate that lives outside your required checks is a gate nobody enforces, which is functionally the same as not having one. Report the pass rate in the job summary too (17/20, not just a green checkmark), so a slow decline from 20/20 to 17/20 over a few weeks shows up as a trend someone can act on, instead of quietly riding just above the threshold until it doesn't.

## Putting the Layers Together

None of the six checks in this guide replace each other, and none of them replace a behavioral check on the app itself. Tool-selection tests catch an agent reaching for the wrong capability. Order tests catch a sequence that's individually correct and collectively wrong. Argument-accuracy tests, the one to prioritize if you only have time for one, catch the failure mode that looks identical to success from a distance. Mocking and live-execution tests answer two different questions about the same call. Failure-handling tests confirm the agent doesn't quietly lose an action when a tool errors. Non-determinism handling keeps all of the above from becoming either flaky noise or a check so loose it stops meaning anything.

Run all six against your own tool-calling agent, wire the deterministic ones and the K-of-N gate into the same required CI check, and you have a trajectory suite that catches real regressions instead of producing green builds that don't mean anything. None of it requires a platform, a new vendor relationship, or a rewrite of how your agent is built: it's pytest, a handful of fixtures, and the discipline to assert on arguments and not just on tool names. The only thing left uncovered is the one this guide has flagged repeatedly, whether the call's effect actually landed where a user would see it, which is a different test, running against a different target, and worth building deliberately rather than assuming your trajectory suite already implies it. Autonoma supplies that last layer by testing the running application after the tool call and maintaining that behavioral coverage as the code changes, so a correct-looking trajectory and a correct user-visible outcome are verified separately.

## Frequently Asked Questions

## Frequently Asked Questions

### What is trajectory evaluation?

Trajectory evaluation is the practice of capturing the ordered list of tool calls an agent makes (the trajectory: tool names, arguments, and results) and asserting against it after the run. It typically checks three things independently: whether the agent selected the right tool, whether it called tools in the right order, and whether it passed the right arguments. It's a white-box check on the call itself, not on the effect that call had on the running application.

### Can an agent pick the right tool and still be wrong?

Yes, and it's the most common real-world failure mode. An agent can correctly select book_flight() and still book the wrong date, the wrong recipient, or the wrong quantity if the arguments are off. A tool-selection-only test passes in that case. An argument-accuracy assertion, which checks the actual values passed to the tool, is what catches it.

### How do you test something non-deterministic, like an LLM's tool choice?

Run the same scenario N times instead of once, and require K of N runs to pass rather than treating a single failure as a verdict. Assert on the invariant (the tool name, and the shape or type of each argument) rather than an exact string match, since a functionally identical value (a reformatted date, for example) will fail a strict equality check without being wrong. Wire the K-of-N check into the same required CI gate as your deterministic tests, not a separate best-effort pipeline.

### What's the difference between mocking a tool call and testing it live?

Mocking a tool and asserting on the call verifies the agent's decision logic: did it try to call the right tool with the right arguments. It's fast and has no external dependency, but it never touches real application state. Testing a tool live and asserting on the effect verifies the outcome: does a record with the expected values actually exist afterward. Both are legitimate; they answer different questions about the same call.

### How do you test what happens when a tool call fails?

Inject a tool error deliberately (a mocked timeout or exception) and assert on what the trajectory shows afterward, not just that the process didn't crash. For a transient failure, assert the agent retried and the retry succeeded. For a permanent failure, assert the trajectory shows the error explicitly and that no partial or false-success state exists in the application, since an agent that swallows the exception and reports success anyway is a worse failure than one that visibly errors.

---

This is the markdown variant of <https://getautonoma.com/blog/testing-ai-agent-tool-calls>, served by content negotiation (`Accept: text/markdown`) and also available directly at <https://getautonoma.com/md/blog/testing-ai-agent-tool-calls>.

Other agent surfaces: [llms.txt](https://getautonoma.com/llms.txt), [resource catalog](https://getautonoma.com/.well-known/ai-catalog.json), [developer portal](https://getautonoma.com/developers), [sitemap](https://getautonoma.com/sitemap.xml).
