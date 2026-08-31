# Source: https://getautonoma.com/blog/crewai-evaluation
Fetched: 2026-08-31

---
title: "CrewAI Evaluation and Testing: How to Test CrewAI Agents"
description: "CrewAI evaluation and testing explained end to end: the crewai test CLI, DeepEval span-level assertions, and multi-agent delegation testing, with runnable code."
date: "2026-07-24"
canonical: "https://getautonoma.com/blog/crewai-evaluation"
authors:
  - "Tom Piaggio"
tags:
  - "Testing"
  - "AI"
  - "AI Agent Testing"
---

# CrewAI Evaluation and Testing: How to Test CrewAI Agents

> **CrewAI evaluation** means verifying that a crew of agents does the right thing, not just that its final reply reads correctly: scoring the crew's overall output with the `crewai test` CLI, inspecting what each agent and tool actually did with DeepEval's span-level tracing, and asserting that one crew member correctly delegates a task to another with the right context intact. Each layer catches a different class of bug, and none of them require abandoning CrewAI's native APIs.

> A two-agent CrewAI support crew tested three ways: crewai test CLI baseline scoring, DeepEval span-level tool-call assertions, and LangWatch Scenario delegation testing, plus a CI workflow and AutoGen / OpenAI Agents SDK delegation equivalents. [Source on GitHub](https://github.com/Autonoma-Tools/crewai-evaluation).

Run `crewai test` on a two-agent crew and it prints a clean number: 8.2 out of 10, averaged over five iterations. Ship it, or dig deeper? The score doesn't say whether the billing agent actually got asked about the right order, or whether the triage agent quietly answered a billing question itself and got lucky on the wording. A passing score and a correctly behaving crew are not the same claim.

That gap is exactly where the public CrewAI-testing advice runs out. The framework's own testing docs cover the `crewai test` command and stop there. Everything past it is scattered: a Promptfoo red-teaming guide here, a DeepEval integration page there, a LangWatch Scenario tutorial, a Patronus unit-testing post, a Google Cloud notebook, none of them building on each other. Multi-agent delegation, the part where a crew actually earns the word "crew," is barely covered anywhere. This piece builds the missing progression: baseline score, then span-level detail, then delegation correctness, as one runnable path instead of four disconnected tabs.

## The Crew You're Testing

Everything below runs against the same small crew, so the layers build on each other instead of describing three unrelated toy examples. It's a two-agent support crew: a triage agent that classifies incoming requests and a billing resolver that actually answers them, using a tool that looks up an order's status.

The one design choice that matters for testing: the triage agent has `allow_delegation=True` and is explicitly told never to answer billing questions itself. That single line is where most of this article's interesting bugs live, because delegation is a decision the model makes, not a function call you wrote.

[src/crew.py](https://github.com/Autonoma-Tools/crewai-evaluation/blob/main/src/crew.py)

> A `crewai test` score tells you the crew was probably fine. It does not tell you which agent did the work, or whether it delegated at all.

> **Diagram:** Three layers of CrewAI evaluation at increasing resolution: the crewai test CLI aggregate score, DeepEval span-level inspection, and Scenario delegation testing.

*Each layer subsumes less of the crew's actual behavior than the one after it. The CLI score is the least informative and the cheapest to run; delegation testing is the most informative and the most expensive.*

## Layer One: `crewai test` for a Baseline Score

The `crewai test` command is the fastest way to get any signal at all, and it deserves to be the first thing you run, not the only thing. From the root of a CrewAI project, it re-runs your crew a fixed number of times and has an LLM grade each run's output.

Two flags control it. `-n` (or `--n_iterations`) sets how many times the crew runs, defaulting to 3. `-m` (or `--model`) sets which model does the grading, defaulting to `gpt-4o-mini`. A higher iteration count buys you a more stable average at the cost of more LLM calls, which matters once this is wired into CI rather than run by hand on your laptop.

[scripts/baseline_eval.sh](https://github.com/Autonoma-Tools/crewai-evaluation/blob/main/scripts/baseline_eval.sh)

What you get back is an aggregate quality score across the iterations, and that's genuinely useful as a smoke check: did something obviously break after the last prompt edit. What you don't get is any visibility inside a single run. If the score drops from 8.4 to 6.1, `crewai test` cannot tell you whether the triage agent stopped delegating, the billing resolver started calling the lookup tool with the wrong order ID, or the drop is just this run's share of ordinary model variance. For that, you need to see inside the task, which is exactly what the CLI doesn't show you.

## Layer Two: DeepEval for Span-Level Inspection

DeepEval's CrewAI integration registers an event listener that turns every `crew.kickoff()` call, every agent execution, and every tool invocation into a span you can attach an assertion to. Instead of grading the crew's final answer as one opaque blob, you grade the pieces: did the billing resolver's tool call use the order ID the customer actually gave, or one it invented.

The setup is one line, `instrument_crewai()`, called once at the top of your test module. From there, `Agent` and `tool` accept a `metrics` argument the same way a `Task` accepts an `expected_output`, and DeepEval wires the metric to that specific span rather than to the whole crew.

[tests/test_deepeval_spans.py](https://github.com/Autonoma-Tools/crewai-evaluation/blob/main/tests/test_deepeval_spans.py)

This is also where the non-determinism problem stops being abstract. The billing resolver can phrase "your order is pending cancellation" a dozen different correct ways, and an exact-match assertion on the final string will flake between them for no real reason. The fix isn't a looser threshold, it's matching the assertion to the thing you're actually checking: use a semantic or LLM-graded metric (DeepEval's `GEval` or a similarity score) for anything the model is free to phrase, and reserve exact-match for hard facts like the order ID and the status value itself. If a span-level test is flaky across runs, the almost-always-correct diagnosis is that the criteria is too loose, or the agent's instructions leave room for two genuinely different valid behaviors, not that the crew is randomly broken.

The same discipline applies to how many times you trust a single run. A `GEval` score of 0.78 on one execution tells you almost nothing about whether 0.78 is normal variance or a real regression, because the grading model itself has some spread. Running the same span assertion three or five times and gating on a pass rate, rather than a single pass or fail, absorbs that spread the same way the `crewai test` CLI's own `-n` flag does at the aggregate level. If the pass rate drifts across a week of CI runs instead of staying flat, that's the signal worth investigating, not a single red run in isolation.

The `crewai test` CLI and a DeepEval span assertion will both tell you the billing resolver's response was correct. Neither one tells you whether that response is attached to a feature real users touch, where a correct-sounding reply and a correct outcome are two different claims, a gap [Autonoma](https://getautonoma.com) was built to close.

## How Autonoma Complements CrewAI Evaluation and Testing

Every layer in this article, the CLI score, the span assertion, and the delegation judge you're about to see, grades something the crew said or decided. None of them grade what the crew's tool call actually did to the application it's wired into. A DeepEval span can confirm the billing resolver called `look_up_order` with the exact order ID from the customer's message and got back "pending_cancellation." It cannot confirm that a real cancellation flow behind that crew ever flips a database row, that the support team's dashboard now shows the ticket as resolved, or that a downstream inventory table doesn't have a stale entry the crew's tool call never touched. Saying the right thing and changing the right state in a running application are two different verification problems, and every layer above only ever tests the first one.

That's the layer Autonoma covers, and it's a different kind of testing, not a bigger judge. Autonoma's Planner reads your codebase, including the routes, the database schema, and the actual endpoints a tool like `look_up_order` or `cancel_order` calls, and plans behavioral end-to-end tests against what the application really does, generating the database state each scenario needs. The Execution Agent drives the real UI in a live preview environment, the same way a support engineer would, clicking through the actual "cancel this order" flow instead of reading a transcript about it. The GenerationReviewer classifies what it finds (a real bug, a flaky run, or a stale test), and the Diffs Agent keeps the suite aligned to the codebase as that flow evolves. None of that scores a delegation handoff or grades a tool span. It verifies that the crew's decision, once it left the conversation, actually happened.

> **E2E coverage for your AI features.** Autonoma runs agentic end-to-end tests on every pull request. [Try Autonoma](https://autonoma.app).

## Layer Three: Multi-Agent Delegation Testing with Scenario

This is the layer almost nothing online covers, and it's the one that actually tests the "multi" in multi-agent. A span-level assertion can confirm the billing resolver's tool call was correct. It cannot confirm the triage agent chose to delegate at all, or that what it handed off included the customer's exact order ID instead of a summary that dropped it.

LangWatch's Scenario framework tests exactly that boundary. You wrap the crew behind an `AgentAdapter`, the same adapter-boundary pattern used for testing agents built on any framework, so the test doesn't care that two CrewAI agents are cooperating underneath it. A `UserSimulatorAgent` sends the request, the adapter runs the crew, and a `JudgeAgent` grades the full transcript against explicit, checkable criteria, not a vague "did this go well."

[tests/test_delegation_scenario.py](https://github.com/Autonoma-Tools/crewai-evaluation/blob/main/tests/test_delegation_scenario.py)

Notice what the criteria check for. Not "the response was helpful," but three specific, verifiable claims: the triage agent delegated instead of answering the billing question itself, the delegated task carried the exact order ID from the original message, and the final answer reflects that order's real status. That middle criterion is the one every simpler test in this article misses. An agent that delegates but drops the order ID along the way will still often produce a plausible-looking final answer, because the billing resolver just asks a clarifying question or guesses instead, and a test that only checks the last message would never catch it.

> **Diagram:** CrewAI multi-agent delegation test checkpoints: right agent chosen, context complete with the order ID intact, and the handoff not dropped.

*A passing final answer can hide a broken handoff. The three checkpoints above are what the judge's criteria actually check, not just whatever the last message said.*

The same three-actor pattern (a simulated user, the crew under test, and a judge) generalizes past CrewAI entirely; [our guide to agent simulation testing](/blog/agent-simulation-testing) builds it from raw Python with no framework dependency at all, worth reading once you need the same delegation check against an agent that isn't a CrewAI crew.

## What Each Layer Catches (and Misses)

| Layer | Catches | Misses |
| --- | --- | --- |
| crewai test | Overall quality drift, N-run average | Which agent, which tool, which args |
| DeepEval spans | Wrong tool args, wrong agent behavior | Whether delegation happened at all |
| Scenario delegation | Right agent, full context, clean handoff | Real app state after the crew runs |

Read top to bottom, each row costs more to run and catches something the row above it structurally cannot see. Running only the top row is common and it is why "the score looked fine" and "the crew was broken" keep showing up in the same incident report.

## Wiring the Full Suite Into CI

Not every layer belongs on every commit. `crewai test` and the DeepEval span assertions are cheap enough to run on every pull request as a smoke check. The Scenario delegation suite, run five times for a stable pass rate rather than a single trusted run, is slower and pricier, so a nightly schedule catches a genuine regression within a day without blocking every commit behind a slow, LLM-heavy job.

[.github/workflows/agent-tests.yml](https://github.com/Autonoma-Tools/crewai-evaluation/blob/main/.github/workflows/agent-tests.yml)

Treat a failing nightly delegation run as an incident to triage the same day, not a badge to eventually get to. A flaky delegation test almost always means the judge's criteria is under-specified or the user simulator's goal text is ambiguous, the same discipline as the span-level layer: tighten the assertion before you loosen the pass threshold.

## Testing AutoGen and the OpenAI Agents SDK

The delegation-correctness problem isn't unique to CrewAI. Every framework that lets one agent hand work to another needs the same three checks: right agent, complete context, clean handoff. If your stack leans on graph-based orchestration instead, [our LangGraph testing guide](/blog/langgraph-testing) covers the same delegation problem for node-to-node routing. Here, the two worth naming briefly are AutoGen and the OpenAI Agents SDK.

AutoGen's `RoundRobinGroupChat` exposes the conversation as a list of messages tagged with their source agent, so the equivalent assertion checks which agents actually spoke rather than inspecting a delegation object directly. If the billing agent's name never shows up in the message sources, the handoff never happened, regardless of what the final message claims.

[examples/autogen_groupchat_test.py](https://github.com/Autonoma-Tools/crewai-evaluation/blob/main/examples/autogen_groupchat_test.py)

The OpenAI Agents SDK surfaces the handoff more explicitly, as a first-class event: `Runner.run()` returns a result whose `new_items` list includes a `HandoffOutputItem` whenever control passes between agents, so the assertion checks for that item directly instead of inferring it from who spoke.

[examples/openai_agents_sdk_test.py](https://github.com/Autonoma-Tools/crewai-evaluation/blob/main/examples/openai_agents_sdk_test.py)

Three frameworks, three different APIs for the same underlying event. Once you've built the "did control and the right context move to the correct agent" assertion for CrewAI, porting it to AutoGen or the Agents SDK is a matter of finding where that framework exposes the handoff, not relearning the pattern.

## When One Layer Is Enough

If you're the only person touching a single crew, `crewai test` in CI plus a handful of DeepEval span assertions on the tools that matter is a reasonable stopping point. The delegation layer earns its cost once a crew grows past two agents, or once a silent bad handoff is a customer-facing mistake rather than an internal inconvenience, which is exactly the kind of bug a `crewai test` score cannot see by construction.

None of the three layers here, run together, tell you whether the crew's work landed anywhere real. They confirm the crew reasoned and handed off correctly. Whether `cancel_order` actually flipped a database row is a claim about the running application, not the conversation, and it needs a different kind of test to check.

## Frequently Asked Questions

## Frequently Asked Questions

### What does crewai evaluation mean?

CrewAI evaluation means verifying that a crew of agents behaves correctly, not just that its final output reads well. In practice it spans three layers: an aggregate quality score from the crewai test CLI, span-level assertions on individual agent and tool behavior with a tool like DeepEval, and multi-agent delegation testing that checks whether one crew member correctly hands a task to another with the right context intact.

### How do I use the crewai test command?

Run crewai test from the root of a CrewAI project. The -n flag (default 3) sets how many iterations to run, and the -m flag (default gpt-4o-mini) sets which model grades each run. It returns an aggregate quality score averaged across iterations, but it does not show which agent or tool produced a given result inside any single run.

### What is span-level testing for CrewAI agents?

Span-level testing means attaching assertions to individual steps inside a crew's execution, such as a specific agent's reasoning or a specific tool call, rather than grading only the crew's final output. DeepEval's CrewAI integration does this by instrumenting crew.kickoff(), each agent execution, and each tool call as an inspectable span, so a metric can catch a wrong tool argument even when the final answer still reads correctly.

### How do you test multi-agent delegation in CrewAI?

Wrap the crew behind an AgentAdapter so a testing framework can drive it like any other agent, then run a simulated user against it while a judge grades the transcript against explicit criteria: did the right agent get the task, did the delegated task carry the necessary context (like an order ID), and does the final answer reflect that context correctly. LangWatch's Scenario framework implements this pattern directly against CrewAI.

### Is CrewAI testing different from testing AutoGen or the OpenAI Agents SDK?

The underlying question is the same across all three: did control and the right context move to the correct agent. The mechanics differ. CrewAI's delegation shows up through its Process and allow_delegation configuration, AutoGen's GroupChat exposes it as a sequence of messages tagged by source agent, and the OpenAI Agents SDK surfaces it as an explicit HandoffOutputItem in a run's result. Once the assertion pattern is built for one framework, adapting it to another is mostly a matter of locating where that framework exposes the handoff event.

---

This is the markdown variant of <https://getautonoma.com/blog/crewai-evaluation>, served by content negotiation (`Accept: text/markdown`) and also available directly at <https://getautonoma.com/md/blog/crewai-evaluation>.

Other agent surfaces: [llms.txt](https://getautonoma.com/llms.txt), [resource catalog](https://getautonoma.com/.well-known/ai-catalog.json), [developer portal](https://getautonoma.com/developers), [sitemap](https://getautonoma.com/sitemap.xml).
