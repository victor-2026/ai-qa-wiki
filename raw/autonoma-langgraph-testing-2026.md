# Source: https://getautonoma.com/blog/langgraph-testing
Fetched: 2026-08-31

---
title: "LangGraph Testing and Debugging: A Practical Guide"
description: "LangGraph testing means node-level unit tests, trajectory verification, multi-turn simulation, and time-travel debugging, in one runnable pytest guide."
date: "2026-07-24"
canonical: "https://getautonoma.com/blog/langgraph-testing"
authors:
  - "Tom Piaggio"
tags:
  - "AI"
  - "Testing"
  - "LangGraph"
  - "Agent Testing"
---

# LangGraph Testing and Debugging: A Practical Guide

> **LangGraph testing** covers a compiled agent graph at three levels: node-level unit tests that invoke a single node in isolation through the checkpointer, trajectory tests that assert the graph took the expected path through nodes and tools, and multi-turn simulations that drive several turns over one thread and check the accumulated state. Paired with LangGraph's built-in state inspection and time-travel replay, it is also the fastest way to debug why an agent went down the wrong branch.

> A runnable LangGraph support-ticket triage agent plus a full pytest suite: node-level unit tests via checkpointer isolation, trajectory/route assertions from get_state_history, multi-turn simulation over one thread_id, and a standalone time-travel debugging script that forks a replay from an earlier checkpoint. Everything runs with zero API keys because the graph's nodes are deterministic stand-ins for real model calls. [Source on GitHub](https://github.com/Autonoma-Tools/langgraph-testing).

Search "LangGraph testing" today and the official docs give you a few paragraphs on node tests and a mention of the checkpointer, then stop. The rest of what you need is scattered across four or five posts written at different times against different LangGraph versions: one on unit-testing nodes with `interrupt_before` and `update_state`, one on trajectory evaluation, one on multi-turn conversation testing, one on time-travel debugging with `get_state_history`. Each is fine on its own. None treats these as one connected workflow, which means every team shipping a LangGraph agent ends up rebuilding the connective tissue between them from scratch.

This is that connective tissue, built once. Everything below runs against a current LangGraph install, verified against the current docs rather than copied from whichever post happened to rank first. We'll build a small support-ticket triage agent (classify the ticket, pull account context, draft a reply, then escalate or resolve) and test it the way a LangGraph agent actually needs to be tested: one node at a time, the path the graph takes through those nodes, and the outcome accumulated across a multi-turn thread. Then we'll reuse the same checkpointer to debug it when a run goes sideways.

> **Diagram:** LangGraph test pyramid: node-level unit tests at the base, trajectory and route verification in the middle, multi-turn simulation at the top.

*Each layer verifies something the one below it cannot: a single node's logic, the route the graph took to get there, and the outcome accumulated across a whole conversation.*

## Unit Testing a Single LangGraph Node in Isolation

The graph under test is a `StateGraph` with four nodes: `classify_ticket`, `fetch_account_context`, `draft_response`, and a conditional split into `escalate` or `resolve`. Each node is a plain function that reads the graph's state and returns the fields it changes, which is the point: nothing about testing that logic requires a real model call. Here's the graph, compiled once with a checkpointer so every invocation is tied to a `thread_id`:

[src/graph.py](https://github.com/Autonoma-Tools/langgraph-testing/blob/main/src/graph.py)

To unit test `fetch_account_context` on its own, you do not need to run `classify_ticket` first. Compile the graph once with `interrupt_after` set to `["fetch_account_context"]`, a static setting passed to `.compile()`, not something you flip per invocation. Then call `update_state` with `as_node` set to `classify_ticket`, seeding the state exactly as if that node had already run and `fetch_account_context` were next in line. Resuming with `graph.invoke(None, config)` runs exactly that one node and then stops, because the compiled interrupt fires right after it, so nothing downstream executes by accident.

The test itself has three moves: compile with `interrupt_after` set to the node under test, seed state via `update_state` with `as_node` pointing at the node upstream of it, then resume with `graph.invoke(None, config)` and call `graph.get_state(config)` to assert on the fields that node is supposed to add, `account_context` in this case. Nothing about that assertion cares what `classify_ticket` or `draft_response` do; it is a true unit test of one function, with the checkpointer standing in for the setup code you would otherwise write by hand.

[tests/test_node_isolation.py](https://github.com/Autonoma-Tools/langgraph-testing/blob/main/tests/test_node_isolation.py)

## Verifying the Trajectory: Did the Graph Take the Right Path?

A node-level test tells you `fetch_account_context` handles one input correctly. It says nothing about whether the graph actually calls that node, in that order, for a given ticket. That's a routing problem, and `add_conditional_edges` is exactly where routing bugs hide: a comparison flipped, a threshold off by one category, a boolean the model hands back as a string instead of an actual bool. Node tests never catch it, because the node itself was correct. What you need is a trajectory assertion: run the full graph once, then check the sequence of nodes it actually visited against the sequence you expected.

LangGraph makes the executed sequence cheap to recover. Call `graph.stream` with `stream_mode="updates"` and read the node name off each yielded update, or call `graph.get_state_history(config)` after the run and walk the checkpoints in order (they come back most-recent-first, so reverse the list). Either way you get a list of node names, and the assertion is a plain list comparison: for a high-priority billing dispute, the expected path is `classify_ticket`, `fetch_account_context`, `draft_response`, `escalate`; for a routine ticket it's the same first three nodes followed by `resolve` instead.

> **Diagram:** Trajectory diagram of the support-ticket triage graph. The executed path, classify_ticket, fetch_account_context, draft_response, escalate, is highlighted in lime. The resolve branch, not taken on this input, is shown in gray.

*The trajectory test reads this exact sequence back out of `get_state_history` and asserts it against the expected path for a high-priority billing ticket.*

This is the same idea our companion piece on [testing AI agent tool calls](/blog/testing-ai-agent-tool-calls) covers in general terms: the sequence of steps an agent chooses matters as much as its final answer. Applied to LangGraph specifically, the sequence is nodes and edges instead of an abstract tool-call log, and `get_state_history` hands it to you for free, because the checkpointer was already recording it for durability, not for testing.

[tests/test_trajectory.py](https://github.com/Autonoma-Tools/langgraph-testing/blob/main/tests/test_trajectory.py)

## How Autonoma Covers What LangGraph's Own Tests Can't See

Node and trajectory tests both run entirely inside the graph. A node test confirms `fetch_account_context` transforms state correctly. A trajectory test confirms `escalate` ran instead of `resolve`, in the right order. Neither confirms that escalating the ticket did anything to the product wrapped around the graph: that the support queue a human agent looks at actually shows the ticket as high-priority, that the customer's status widget updated, that the on-call alert actually fired. The graph can be exactly right and the feature can still be broken, because the code wiring the graph's decision to the rest of the application is something no graph-level test ever touches.

That's the layer we built [Autonoma](https://getautonoma.com) to cover. It's an open-source, codebase-first testing product that runs behavioral end-to-end tests against your running application, not against the graph in isolation. Our Planner agent reads the actual routes, components, and schema your ticket-triage feature touches (the queue page, the status widget, the alert handler) and plans test cases against what the product is supposed to do once that graph decision fires. Our Execution Agent drives the real UI in a live preview environment the way a support engineer would, checking that the escalated ticket actually landed in the queue instead of reading a state dict that claims it did. Our GenerationReviewer separates a genuine regression from a flaky run, and our Diffs Agent keeps that suite aligned every time someone reworks the escalation endpoint, so the coverage doesn't rot the week after you write it.

Think of it as a layer sitting above everything a graph-level test can see. Node tests, trajectory tests, and the multi-turn simulation below all verify the graph produced the right decision. Autonoma verifies the rest of the product actually acted on it, which is the part a passing pytest run has no way to check.

> **Verify the app, not just the graph.** Autonoma runs agentic end-to-end tests on every pull request. [Try Autonoma](https://autonoma.app).

## Multi-Turn Simulation Over a Compiled Graph

Node tests and trajectory tests both run the graph once, start to finish. Production traffic rarely looks like that. A real support ticket is a thread: the customer replies, the agent re-classifies, the account context gets re-fetched with new information, and the final `status` only makes sense in light of everything that came before it. Testing that means driving several turns through the *same* `thread_id`, not a fresh one each time, so the checkpointer accumulates state across calls the way it would in production.

The pattern is a loop: build one config with a fixed `thread_id`, call `graph.invoke` once per turn against that same config, and after the last turn call `graph.get_state(config)` to read the accumulated state. What you assert matters more than how. Exact wording is the wrong target, two runs of the same conversation can phrase a `draft` differently and both be correct, but an ID or a status is not: pin `temperature=0` on the underlying model call where you can to cut incidental variance, then assert on structure and invariants rather than text. The final `status` is one of `escalated` or `resolved`. Escalation happens at most once per thread. Every account fact the agent repeats back matches the fact it was given, exactly, every turn.

If a scenario genuinely needs to check that a reply *means* the right thing rather than contains the right token, that's the one case worth reaching for an LLM-as-judge, and only there. Save it for semantic equivalence checks specifically; using it as the default assertion for everything trades a fast, deterministic test for a slow, non-deterministic one grading another non-deterministic one.

[tests/test_multi_turn_simulation.py](https://github.com/Autonoma-Tools/langgraph-testing/blob/main/tests/test_multi_turn_simulation.py)

Put the three layers side by side and each one is catching a different class of bug, which is why none of them is optional once an agent ships:

| Layer | Catches | Needs an LLM call | Cost |
| --- | --- | --- | --- |
| Node isolation | Wrong output from one function | No | Milliseconds |
| Trajectory | Wrong routing decision | Only if the node calls one | One graph run |
| Multi-turn simulation | Wrong accumulated outcome | Yes, several per test | Seconds per turn |

## LangGraph Debugging: State Inspection and Time-Travel Replay

Testing catches the bugs you thought to check for. Debugging is what you need when a run does something you didn't anticipate, and the checkpointer is already recording everything required for it, whether or not you set out to test that particular run.

Start with `graph.get_state(config)`. It returns the graph's current snapshot for a `thread_id`: every state field, plus `next`, the node or nodes that would run on the next invocation. That single call answers the question you ask first when a run looks stuck or wrong: what does the graph currently believe, and what is it about to do next.

When the current snapshot isn't enough, `graph.get_state_history(config)` returns every checkpoint for that thread, most recent first, each carrying its own config with a `checkpoint_id`. That's a full audit trail of every node execution in order, and it's the same data the trajectory test earlier reads for its assertion, meaning the debugging tool and the test are, structurally, the same call pointed at a different question.

Time-travel is what turns that history from readable into actionable. Pick an earlier checkpoint (say, the one right before `draft_response` ran), pass its config straight into `graph.invoke(None, config)`, and the graph resumes from exactly that point: every node before it is skipped, everything after re-executes. Pair that with `update_state` on the earlier checkpoint, changing `category` before resuming, for instance, and the replay forks into a new timeline built from the corrected input, without re-running the parts of the graph that were never in question.

One detail that trips people up the first time: if any node in your graph is itself a compiled subgraph, `get_state` only returns the parent graph's fields by default. Pass `subgraphs=True` and the returned snapshot's `tasks` include each subgraph's own state and its own config, so you can drill into a subgraph's checkpoint history the same way you'd drill into the parent's. Skipping that flag is the usual reason a debugging session stalls on "the state looks right, so why did the subgraph node behave differently," when the subgraph's internal state was never inspected in the first place.

[scripts/debug_replay.py](https://github.com/Autonoma-Tools/langgraph-testing/blob/main/scripts/debug_replay.py)

## Wiring the Three Layers Into CI

Node tests are cheap enough to run on every commit: a few hundred milliseconds each, no LLM calls if the nodes are pure functions. Trajectory tests cost one graph run and belong on every pull request. Multi-turn simulations are the expensive ones, several LLM calls per test, so they belong on a slower cadence: a one-scenario smoke pass on every PR, the full multi-turn suite nightly, and a failing nightly run treated as an incident to triage that day rather than a stat to note in passing.

None of the three layers above touches the product the graph is embedded in, and that is deliberate scope, not an oversight. Catching whether the right decision actually reached the customer's screen is a job for the layer above the graph, which is where Autonoma and behavioral end-to-end testing come in, not where LangGraph's own testing surface was ever trying to compete.

If your stack is CrewAI instead of LangGraph, the same three-layer arc applies almost unchanged: isolate a single agent's role logic, verify the crew's task routing, then simulate a multi-turn run. The specifics of how you seed and inspect state differ enough to matter, and [our CrewAI evaluation guide](/blog/crewai-evaluation) walks through those specifics end to end.

## Frequently Asked Questions

## Frequently Asked Questions

### What is LangGraph testing?

LangGraph testing means verifying a compiled agent graph at three levels: node-level unit tests that exercise a single node in isolation via the checkpointer, trajectory tests that assert the graph visited the expected sequence of nodes and tools, and multi-turn simulations that drive several turns over one thread and check the accumulated state. It also includes debugging with state inspection and time-travel replay, since both rely on the same checkpointer data the tests already use.

### How do I unit test a single LangGraph node?

Compile the graph with an InMemorySaver checkpointer and interrupt_after set to the node under test, a static setting passed to compile(), not invoke(). Use update_state with as_node set to the upstream node's name to seed the state as if that node had already run. Resume with invoke(None, config); the graph runs exactly that one node and stops, because the compiled interrupt fires right after it. Then call get_state and assert on the fields the node is supposed to have added.

### How do I check that a LangGraph agent followed the expected path?

Run the graph once, then recover the executed node sequence either by streaming with stream_mode="updates" and reading the node name off each update, or by calling get_state_history after the run and reversing the most-recent-first list of checkpoints. Compare that sequence to the list of node names you expected for the given input.

### How do I debug a LangGraph agent that went down the wrong branch?

Call get_state to see the graph's current snapshot and what it will run next. If that is not enough, call get_state_history to see every checkpoint for the thread in order. Pick the checkpoint right before the point things went wrong, pass its config into invoke to replay from there, and optionally call update_state first to fork the replay with corrected input.

### Should I use InMemorySaver in production?

No. InMemorySaver keeps checkpoints in process memory, so state disappears on restart and never shares across processes. It is meant for tests and local development. Production deployments need a durable checkpointer, such as a Postgres or SQLite-backed saver, so a thread's state survives restarts and scales across multiple workers.

---

This is the markdown variant of <https://getautonoma.com/blog/langgraph-testing>, served by content negotiation (`Accept: text/markdown`) and also available directly at <https://getautonoma.com/md/blog/langgraph-testing>.

Other agent surfaces: [llms.txt](https://getautonoma.com/llms.txt), [resource catalog](https://getautonoma.com/.well-known/ai-catalog.json), [developer portal](https://getautonoma.com/developers), [sitemap](https://getautonoma.com/sitemap.xml).
