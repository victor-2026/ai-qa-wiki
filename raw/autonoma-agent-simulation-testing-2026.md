# Source: https://getautonoma.com/blog/agent-simulation-testing
Fetched: 2026-08-31

---
title: "What Is Agent Simulation Testing? A 3-Actor Harness"
description: "Agent simulation testing explained and built in raw Python: a three-actor harness (user simulator, agent, judge) with a tool-failure recovery scenario."
date: "2026-07-22"
canonical: "https://getautonoma.com/blog/agent-simulation-testing"
authors:
  - "Tom Piaggio"
tags:
  - "Testing"
  - "AI"
  - "AI Agent Testing"
---

# What Is Agent Simulation Testing? A 3-Actor Harness

> **Agent simulation testing** runs a synthetic user, driven by an LLM playing a persona and a goal, against your AI agent across multiple turns, then scores the resulting transcript against explicit pass/fail criteria. It is the multi-turn counterpart to a single-shot eval: instead of grading one reply, it validates a whole conversation, including whether the agent recovers when a tool call fails partway through. The pattern needs three actors, a user simulator, the agent under test, and a judge, and none of them require a vendor SDK to build.

> A raw-Python, vendor-neutral three-actor agent simulation harness (user simulator, agent-under-test adapter, and LLM judge) with a worked order-cancellation scenario that injects a mid-conversation tool failure and asserts recovery, plus a pytest suite demonstrating the run-N-times and semantic-similarity patterns for handling LLM non-determinism. [Source on GitHub](https://github.com/Autonoma-Tools/agent-simulation-testing).

LangWatch calls its version Scenario testing, and their docs are, honestly, the best public artifact of this pattern anywhere. The pytest harness ships an `AgentAdapter`, a `UserSimulatorAgent`, and a `JudgeAgent`, and the six-turn order-cancellation example in their guide simulates a tool call failing mid-conversation and asserts the agent recovers from it. It is a genuinely good piece of work. The catch: every part of it only runs inside LangWatch's SDK. If you are not already on their platform, the pattern is not portable, even though nothing about the pattern itself is proprietary. Three LLM calls, a loop, and an assertion. This piece builds the same harness in raw Python, so it works with whatever agent framework, whatever model provider, and whatever CI system you already run, and it stays the reference the rest of this agent-testing series links back to.

## The Three-Actor Pattern, Explained Generically

A single-shot eval answers one question: is this one reply good? That is enough for a classifier or a summarizer, but an agent's failures rarely show up in a single reply. They show up three turns in, after the user has pushed back once, right after a tool call comes back with an error the agent has to react to. Testing that requires a conversation, not a prompt-response pair, and a conversation needs someone to have it with.

The pattern that works is three actors, each doing one job.

The `UserSimulatorAgent` is an LLM given a persona and a goal, not a script. It generates the next user message given the conversation so far, and it decides on its own when the goal has been reached (or when to give up), the same way a real user would. Because it is a model reasoning about intent rather than a fixed list of inputs, it can push back, get confused, or rephrase, which is exactly the behavior that breaks agents in production and never shows up in a scripted test.

The `AgentAdapter` wraps the agent under test behind one interface: take the conversation history, return a reply and whatever tool calls the agent made. It does not care if the agent underneath is LangGraph, CrewAI, an OpenAI Assistants thread, or code you wrote yourself. That adapter boundary is what makes the harness reusable across every agent you own, instead of one test file per framework.

The `JudgeAgent` is a third, independent LLM call, graded against criteria written as an explicit, checkable rubric, not a vague "was this a good response." A criteria string like "PASS only if the order status changed to cancelled AND the agent acknowledged the failed attempt before retrying" gives the judge something it can actually check line by line. A criteria string like "PASS if the response was helpful" gives it nothing to check, and you will get a different verdict every run for reasons that have nothing to do with your agent.

A `SimulationRunner` ties the three together: it alternates user and agent turns up to a turn limit, stops early if the simulator signals the goal is done, and always hands the full transcript to the judge at the end, even if the conversation ended early. That last detail matters. An agent that gives up after turn two should fail the judge's rubric just as loudly as one that runs all eight turns and gets the answer wrong.

![Diagram of the three-actor simulation harness: UserSimulatorAgent and AgentAdapter exchange user turns and agent replies for N turns, orchestrated by a SimulationRunner, then the full transcript is sent to a JudgeAgent which returns a pass or fail verdict with reasoning](/img/blog/agent-simulation-testing/three-actor-harness.svg)

*Three LLM-backed roles, one loop, one verdict. Nothing here is vendor-specific.*

Here's the harness itself, as a single, provider-agnostic module. It only touches the OpenAI SDK in one place (`LLMClient`), so swapping providers means changing one class, not rewriting the pattern:

[src/harness.py](https://github.com/Autonoma-Tools/agent-simulation-testing/blob/main/src/harness.py)

## A Worked Scenario: The Order-Cancellation Tool Failure

The happy path is not where agents fail. They fail when a downstream call times out, a third-party API returns a 500, or a database write silently doesn't land, and the agent has to notice, tell the user, and try again instead of pretending nothing happened or looping the same failing call forever. That is the scenario worth building a simulation test around, and it is close to the one LangWatch demonstrates: a customer wants order A1092 cancelled, and the `cancel_order` tool fails on the first attempt.

The scenario injects a real failure mode: the first call to `cancel_order` raises a timeout, the second call (on retry) succeeds. The user simulator's persona is written to push back once if the agent seems to give up, which is the behavior most scripted tests never exercise because nobody writes a fixture for "the user gets annoyed." The judge's criteria are explicit and checkable: the order's status actually changed to cancelled by the end of the conversation, the transcript shows the agent acknowledging the failed attempt before it retries, and the agent never repeats the same failing action more than twice without telling the user.

That middle criterion is the one that separates a simulation test from a plain success check. An agent that silently retries and eventually succeeds looks fine if you only check the final state. It is not fine. A support agent that goes quiet for three tool calls and then reports success has a UX bug even though the outcome is technically correct, and a bug like that is invisible to any assertion that only checks whether `cancel_order` eventually returned 200.

![Timeline of the order-cancellation scenario across five turns: the user asks to cancel order A1092, the agent calls cancel_order, the tool call fails on the first attempt, the agent acknowledges the failure and retries, the retry succeeds, and a recovery assertion checks that the failure was acknowledged before the retry, not silently swallowed](/img/blog/agent-simulation-testing/scenario-timeline.svg)

*The failure and the recovery are both part of the transcript the judge scores. A test that only checks the final "cancelled" state would miss the silent-retry bug entirely.*

Here's the scenario built on top of the harness, including a second, deterministic recovery check that does not rely on the judge alone:

[src/order_cancellation_scenario.py](https://github.com/Autonoma-Tools/agent-simulation-testing/blob/main/src/order_cancellation_scenario.py)

## Handling Non-Determinism: Run It More Than Once

Every actor in this harness is an LLM call. The user simulator can phrase its request differently each run. The agent can word its acknowledgment differently each run. The judge can, in rare cases, misread a transcript. That is a different kind of flakiness than a brittle CSS selector, and it needs a different fix, not a `sleep()` and a retry.

The first discipline is running the scenario more than once and gating on a threshold, not a single boolean. Five runs, four-out-of-five required to pass, is a reasonable starting point. What matters more is what you do when the pass rate is inconsistent: the instinct is to loosen the threshold further, and that is almost always the wrong move. Check the user simulator's persona and goal text first. If the goal is underspecified, the model has room to interpret it a different way each run, and that variance is not a bug in your agent, it is ambiguity in your test. Tighten the persona and the judge's criteria before you tighten the pass bar. A flaky simulation test is telling you the assertion is too strict or the prompt is too ambiguous, almost never that your agent is randomly broken.

The second discipline is matching the assertion to the thing you are actually checking. The order id `A1092` and the word `cancelled` are hard facts, worth asserting on exactly. The sentence around them is not: "Your order has been cancelled" and "I've gone ahead and cancelled order A1092 for you" are both correct, and an exact-match assertion will flake between them for no real reason. Use semantic similarity (an embedding-based comparison, or the judge itself) for anything the model is free to phrase, and reserve exact-match for the facts that must appear verbatim.

Here's both patterns together, run-N-times gating and semantic-similarity assertions, as a real pytest file:

[tests/test_non_determinism.py](https://github.com/Autonoma-Tools/agent-simulation-testing/blob/main/tests/test_non_determinism.py)

## Tools That Productize This

Building the harness above takes an afternoon and teaches you exactly where your agent's failure modes live. Once you are running it against a dozen agents instead of one, a hosted platform starts pulling its weight: a dashboard instead of a spreadsheet of pass rates, historical trend lines, and a UI for writing new personas without touching Python. Here is what each of the three vendors most often named alongside this pattern actually wraps.

| Tool | Wraps | Best for | Lock-in |
| --- | --- | --- | --- |
| LangWatch | Full 3-actor harness, pytest-native | Teams already tracing with LangWatch | SDK-locked scenario format |
| Maxim | Simulation plus a metrics dashboard | Managed metrics, less code ownership | Platform-hosted, less control |
| Retell | Simulated callers for voice agents | Voice agents specifically | Voice-only, not general-purpose |

None of these are wrong choices. They are the right choice once the harness itself stops being the interesting part of your job. What none of them do, and what the three-actor pattern above does not do either, is tell you whether the agent's action actually changed anything in the application it is wired into.

## How Autonoma Complements Agent Simulation Testing

The judge's verdict in the scenario above only tells you the conversation was correct. It confirms the agent said the right words, acknowledged the failure, and reported success. It does not confirm that `cancel_order()` actually flipped order A1092's status in the real database, that the support team's dashboard now shows "Cancelled," or that a stale row didn't get left behind in an inventory table the agent's tool call never touched. Saying the right thing and doing the right thing to the running application are two different verification problems, and simulation testing, by construction, only tests the first one. That gap is invisible from inside the transcript, because the transcript only ever shows you what the agent claimed happened.

That is the layer we built Autonoma to cover, and it is a different kind of testing entirely, not a bigger judge. Autonoma's agents run behavioral end-to-end tests directly against a running application. The Planner reads your codebase, the routes, the components, the order-management screens, and the database schema the cancellation actually touches, and plans test cases against what the application really does, including generating the DB state each scenario needs. The Executor drives the UI in a live PreviewKit environment, Autonoma's managed preview-environments layer, the same way a support engineer would, clicking through the actual cancellation flow instead of reading a transcript about it. The Reviewer classifies what it finds: a real bug, a flaky run, or a mismatch between the test and the current app behavior. The Diffs Agent keeps the suite aligned to the codebase on every pull request, so the tests don't rot the next time someone reworks the cancellation endpoint. None of that scores a conversation or computes a similarity threshold. It verifies that the tool call your agent made actually produced the state your users and your support team see.

Put the two side by side on the exact scenario above: agent simulation testing proves the agent chose the right tool, recovered out loud instead of silently retrying, and told the user the truth. [Autonoma](https://getautonoma.com)'s behavioral E2E layer proves the order's status genuinely changed to cancelled in the admin dashboard your support team actually looks at, that inventory was actually released, and that a regression introduced next month, someone reworks the cancellation endpoint and nobody touches the agent's prompt, gets caught even though the conversation layer never changes. You need both. Neither one substitutes for the other.

> **Test what your agent does, not just what it says.** Autonoma runs agentic end-to-end tests on every pull request. [Try Autonoma](https://autonoma.app).

## When to Build the Harness vs Adopt a Platform

If you are testing one agent end to end for the first time, build the raw harness above. It is a few hundred lines, it teaches you your agent's actual failure modes instead of a vendor's abstraction of them, and it runs in whatever CI you already have.

Three signals tell you it's time to look at a platform instead of maintaining more Python. The first is agent count. Once you are running this harness against five or six different agents, each with its own personas and criteria, the maintenance burden shifts from "understand your agents" to "maintain a small test framework," and that second job is exactly what LangWatch, Maxim, and similar tools are built to take off your plate. The second is who is writing the personas. Personas and criteria strings are prose, not code, and once someone on your product or support team wants to add a new scenario without touching a Python file, a hosted UI earns its cost. The third is history. A pass or fail printed to a CI log tells you today's result. A platform that stores every run gives you a trend line, so a pass rate that drifts from 96% down to 84% over two weeks shows up as a graph instead of a mystery someone has to happen to notice.

None of that means the raw harness was wasted effort. The vendor products above are, at their core, a hosted version of the same three actors this article builds from scratch, plus a UI and a database in front of them. Understanding the pattern first means you know exactly what you are paying for when you adopt one, and you can tell the difference between a platform limitation and a bug in your own agent, a distinction that is much harder to make when the harness has always been someone else's black box.

Wiring this into CI is worth doing deliberately, not by accident. Every run is a handful of real LLM calls, on the user simulator side, the agent side, and the judge, which makes it slower and more expensive than a typical unit test. Running the full non-determinism suite (five repetitions of every scenario) on every commit gets expensive fast once you have more than a handful of scenarios. A more sustainable pattern: run one repetition per scenario on every pull request as a smoke check, and run the full five-repetition, threshold-gated suite on a nightly schedule, so a genuine regression surfaces within a day instead of blocking every commit with a slow, LLM-heavy test run. Treat a failing nightly run as an incident to triage that same day, not a red badge to get to eventually. For the action-level check that a transcript cannot provide, Autonoma can run the behavioral journey against the PR's running application as that code evolves. The version of this pattern that never turns into technical debt is the version someone is actually looking at.

The three-actor pattern here is the foundation the rest of this batch builds on. For the protocol and tool-function layers beneath an agent's conversation, [how to test an MCP server](/blog/how-to-test-an-mcp-server) separates handshake, deterministic tool, and tool-selection checks. For the broader application layer, [testing generative AI applications](/blog/testing-generative-ai-applications) maps prompt tests, eval sets, behavioral E2E, and production monitoring. And [chatbot automation testing](/blog/chatbot-automation-testing) shows how to make non-deterministic response assertions a repeatable CI gate.

## Frequently Asked Questions

## Frequently Asked Questions

### What is agent simulation testing?

Agent simulation testing runs a synthetic user, driven by an LLM playing a persona with a goal, against an AI agent across multiple conversation turns, then scores the full transcript against explicit pass/fail criteria using a separate judge model. It validates the whole conversation, including how the agent recovers from a mid-conversation tool failure, rather than grading a single reply in isolation.

### How is agent simulation testing different from an LLM eval?

A single-shot eval grades one input-output pair: is this one response accurate, relevant, or safe. Agent simulation testing validates a multi-turn journey: does the agent handle a user pushing back, recover when a tool call fails, and reach the correct outcome across several turns. Evals check a point. Simulation checks a path.

### Do I need a vendor SDK to run agent simulation testing?

No. The pattern is three LLM-backed roles, a user simulator, the agent under test, and a judge, orchestrated in a loop. It can be built in raw Python against any LLM provider's API and any agent framework. Vendor products like LangWatch, Maxim, and Retell productize pieces of this pattern with dashboards and managed infrastructure, but the underlying pattern has no proprietary dependency.

### How many times should I run a simulation test before trusting the result?

Run it multiple times (five is a reasonable starting point) and gate on a pass threshold like four-out-of-five, rather than treating a single run as ground truth. If the pass rate is inconsistent across runs, tighten the user simulator's persona and the judge's criteria before loosening the threshold. Inconsistent results usually mean the prompt is ambiguous, not that the agent is randomly broken.

### Should I use LangWatch, Maxim, or Retell instead of building my own harness?

Build the raw harness first if you are testing one or a few agents; it takes an afternoon and teaches you your agent's real failure modes. Adopt a platform once you are running this pattern across many agents and a dashboard, historical trends, and non-engineer persona editing start paying for themselves. LangWatch wraps the fullest version of the pattern for teams already on their tracing stack. Maxim trades code ownership for a managed metrics dashboard. Retell is scoped specifically to voice agents.

---

This is the markdown variant of <https://getautonoma.com/blog/agent-simulation-testing>, served by content negotiation (`Accept: text/markdown`) and also available directly at <https://getautonoma.com/md/blog/agent-simulation-testing>.

Other agent surfaces: [llms.txt](https://getautonoma.com/llms.txt), [resource catalog](https://getautonoma.com/.well-known/ai-catalog.json), [developer portal](https://getautonoma.com/developers), [sitemap](https://getautonoma.com/sitemap.xml).
