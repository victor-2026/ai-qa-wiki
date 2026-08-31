# Source: https://getautonoma.com/blog/how-to-test-multi-turn-conversations
Fetched: 2026-08-31

---
title: "How to Test Multi-Turn Conversations and Context Retention"
description: "How to test multi-turn conversations: catch topic-switch coreference breaks, context-window overflow, and long-conversation drift with a runnable pytest harness."
date: "2026-07-29"
canonical: "https://getautonoma.com/blog/how-to-test-multi-turn-conversations"
authors:
  - "Tom Piaggio"
tags:
  - "Testing"
  - "AI"
  - "Context Retention Testing"
  - "LLM Testing"
---

# How to Test Multi-Turn Conversations and Context Retention

> **Testing multi-turn conversations** means verifying that a chatbot or AI agent holds state correctly across many turns in a single session, not just that any one reply is correct in isolation. It covers three separate failure modes: losing a fact after the topic changes and comes back (coreference), forgetting or confabulating once the conversation crosses the context window's truncation boundary, and drifting persona, instructions, or consistency over twenty or more turns. Test each one with a scripted three-actor harness, a user simulator, the system under test, and a judge, asserting on invariants and pass rates, never on exact wording.

> [Source on GitHub](https://github.com/Autonoma-Tools/how-to-test-multi-turn-conversations).

Turn fourteen was where it broke. On turn two, a user setting up a booking said, "I'm booking for my daughter Maya, she's 7." Turns three through eleven wandered into refund windows, baggage limits, and seat selection, none of it about Maya. On turn fourteen the user circled back: "ok so can she bring a friend?" The bot answered as if "she" referred to nobody in particular, and quoted the policy for an unaccompanied adult passenger.

Graded turn by turn, every reply in that transcript was defensible. The refund answer was correct. The baggage answer was correct. Turn fourteen's answer, read alone with no history attached, was even coherent. The failure only exists at the level of the conversation, and a test suite that scores replies one at a time will never see it.

That's the gap this piece fills. Response-level evals, the kind most teams already have, check whether a reply is good given the transcript up to that point. They say nothing about whether the transcript itself survived the trip. What follows are three specific ways a conversation degrades that a single-turn eval structurally cannot catch, plus a runnable pattern for testing each one.

It's worth naming the second gap up front, because it shapes where these tests stop. Everything below reads the conversation. None of it touches the product the conversation is driving, and a booking bot that holds Maya's name perfectly across fourteen turns can still leave the reservation unchanged. That distinction, between a coherent transcript and a correct application, is the one [Autonoma](https://getautonoma.com) was built around, and it comes back at the end of this piece with a concrete example.

## Context Retention Is Not Memory, and Testing Them the Same Way Is a Mistake

Two very different things get called "the bot remembered." In-window context retention is whatever the model can still see inside the current conversation's token window. It lives entirely inside one session and dies the moment that session ends: test it by scripting turns inside a single conversation and asserting on what survives from one turn to the next. Persistent memory is whatever the system deliberately wrote to a durable store and retrieves later, in a separate session starting from zero context: test that by closing the first session, opening a second, and asserting the system pulls the right fact back out.

Conflating the two is a common mistake. A bot can pass every multi-turn test here and still have zero persistent memory, holding a fact across turn six of one conversation says nothing about whether it wrote anything down for next Tuesday. The reverse is just as real: a working long-term memory store doesn't stop a bot from losing the plot by turn six of a single session, since retrieval-from-storage and holding-state-in-context run through entirely different code paths.

| Property | In-Window Context Retention | Persistent Memory |
| --- | --- | --- |
| Where it lives | Current session's token window | A durable store (DB, vector index) |
| Survives session end? | No | Yes, by design |
| How you test it | Script turns in one conversation | Close session, open a new one, probe |
| Common break | Coreference lost after topic switch | Fact never written, or wrong one retrieved |
| Failure looks like | "Who is she?" mid-session | Bot re-asks something from last week |

This piece covers the first column only. For the store-and-retrieve-later layer, [how to test AI agent memory](/blog/how-to-test-ai-agent-memory) is the sibling piece, and it's worth reading both if your bot claims to do either.

## The Harness: A Scripted User, a System Under Test, and a Judge

Every pattern below reuses the same three-actor shape: a scripted user actor, the system under test, and a judge layer that asserts on the conversation rather than on any one reply's wording. If you haven't built that harness yet, [agent simulation testing](/blog/agent-simulation-testing) is the full derivation, three actors, a tool-failure scenario, and why a judge beats exact match. This piece extends that shape for multi-turn state specifically.

The seam worth naming up front is `send(conversation, message)`: it appends a user turn, calls your chat client with the full history, appends the reply, and returns it. Every pattern below is written against that seam so it drops into whatever you're running, your own agent server, a hosted API, a wrapped SDK, without rewriting the tests. If you haven't covered single-turn correctness yet, [how to test a chatbot](/blog/how-to-test-a-chatbot) is the fundamentals piece to start from; what follows is about what changes once turns start accumulating.

Here's the shared fixture layer every test file below builds on, the `Conversation` object, the `send()` seam, and a `pinned_facts` fixture for the facts a session establishes early and needs to keep:

[lib/harness.py](https://github.com/Autonoma-Tools/how-to-test-multi-turn-conversations/blob/main/lib/harness.py)

The fixtures themselves stay thin, two of them, wrapping the harness above so every test file gets a fresh conversation and the facts it pins at the start:

[tests/conftest.py](https://github.com/Autonoma-Tools/how-to-test-multi-turn-conversations/blob/main/tests/conftest.py)

## Failure Mode 1: Topic-Switch-Then-Return

This is the turn-fourteen story from the top of this piece, and it's the single most common real-world multi-turn break, precisely because almost nobody tests for it directly. The shape is always the same: establish a fact, spend several turns on something else entirely, then refer back with a pronoun instead of restating it. A human conversation partner does this constantly and never notices. A bot with weak context handling drops the referent the moment the topic moves on.

The assertion is not on the words of the final reply. It's on whether the reply's meaning still resolves the pronoun to the right referent, which is exactly why this needs a judge instead of a string match: "she can bring a friend if the friend is also a listed passenger" and "yes, one additional passenger is allowed on Maya's booking" are both correct and share almost no words.

> **Diagram:** A six-turn conversation timeline showing a fact established at turns one and two, an unrelated intervening topic spanning turns three through five, and a pronoun reference at turn six where the test asserts the reply still resolves back to the fact established at the start.

*The assertion isn't on turn six's wording. It's on whether the pronoun still points back to the fact established before the intervening topic ever came up.*

Here's the test: establish the fact, insert three unrelated turns, then probe the referent, and assert the judge sees it survive:

[tests/test_topic_switch_return.py](https://github.com/Autonoma-Tools/how-to-test-multi-turn-conversations/blob/main/tests/test_topic_switch_return.py)

## Failure Mode 2: Context-Window Overflow

Every model, and every wrapper around one, has a token budget, and every long enough conversation eventually crosses it. The wrong question is whether the bot breaks once that happens. Something always changes past the window, older turns get dropped, summarized, or both. The right question is whether it degrades gracefully. Acknowledging the gap, re-asking, or falling back to a summary that preserved the facts you pinned is an acceptable failure. Silently forgetting and then confidently inventing a replacement is the dangerous one, since it looks identical to a correct answer until someone checks it against reality.

Most teams discover their truncation strategy the hard way: it's "drop the oldest messages first," which quietly drops the most important turn in the conversation, the one where the user stated what they actually wanted. The fix most mature systems converge on is a pinned-facts layer, a short summary of the handful of facts that must never drop, refreshed and re-injected on every turn regardless of what else gets truncated.

Test the boundary on purpose. Pad a conversation with filler turns past your system's actual truncation threshold, then probe for a fact you pinned at the start, and assert one of two allowed outcomes, remembered, or acknowledged as gone, never a confidently invented substitute.

> **Diagram:** A conversation growing left to right toward a truncation threshold. Before the threshold pinned facts are retained. After it, two outcomes diverge: graceful degradation, which acknowledges the gap or relies on a preserved summary, and silent confabulation, which forgets and confidently invents a replacement fact.

*Crossing the truncation boundary isn't the failure by itself. Which of the two branches the bot lands on is what the test actually needs to gate.*

[tests/test_context_window_overflow.py](https://github.com/Autonoma-Tools/how-to-test-multi-turn-conversations/blob/main/tests/test_context_window_overflow.py)

> **The reply was right. Was the app?** Autonoma runs agentic end-to-end tests on every pull request. [Try Autonoma](https://autonoma.app).

## Failure Mode 3: Long-Conversation Degradation

The first two failure modes happen at a specific turn. This one is a trend, and it needs a different assertion. Over twenty, forty, sixty turns, even comfortably inside the context window, quality decays: the bot drifts off its persona, repeats phrasing, stops following an instruction given early ("stop using bullet points" quietly stops holding by turn thirty), or contradicts a commitment it made turns ago.

The version of this that costs real money is the one where the drift is in the actions, not the prose. A bot forty turns into a support session that quietly stops applying a constraint the user set at turn three keeps writing perfectly reasonable replies while issuing credits it shouldn't. A transcript-level judge scores those replies as fine, because as sentences they are fine. Catching it needs an assertion on the account, not the answer, which is the layer Autonoma drives: the same long conversation replayed against the running product, with the invariant checked on what the product ended up in rather than on what the bot said about it.

A single assertion at the end misses this entirely, since the failure is gradual, not a step function. Score every turn against the same invariant, track the trend, and assert the score doesn't regress past a threshold as the conversation gets longer, plus a separate check for direct self-contradiction against anything said earlier in the session:

[tests/test_long_conversation_degradation.py](https://github.com/Autonoma-Tools/how-to-test-multi-turn-conversations/blob/main/tests/test_long_conversation_degradation.py)

## Why Multi-Turn Tests Are the Flakiest Tests You'll Write

Failure probability compounds per turn. A test with a 98% pass rate on any single assertion, run six times across a scripted conversation, has roughly an 89% chance all six hold, and every failure mode above needs several chained assertions, not one. Multi-turn tests will flake more than anything else in your suite, and that's expected.

Handle it like any genuinely probabilistic system. Assert on invariants, never exact wording, since two correct replies can use completely different words. Run each test N times and require a pass rate, not a single one-out-of-one pass; five runs with four clearing the bar is a defensible floor. Prefer a judge or embedding similarity over string comparison, and treat `temperature=0` as a start, not a guarantee: retrieval order, summarization, and tool results can still vary between identical-looking runs even at zero temperature.

The heuristic worth pinning above your desk: a flaky multi-turn test means one of three things. Your assertion is too strict for normal variance, your prompt or script is ambiguous enough to have more than one right answer, or your context strategy actually is non-deterministic and the flake is real signal, not noise to average away. Here's the judge helper every test above calls into, boolean and scored questions instead of text comparison:

[lib/judge.py](https://github.com/Autonoma-Tools/how-to-test-multi-turn-conversations/blob/main/lib/judge.py)

## Running This in CI Without Drowning in Flaky Reruns

Not every one of these belongs on every pull request. The topic-switch and overflow tests are cheap, a handful of turns each, so they run fine per PR with a couple of automatic reruns for the compounding-flake problem above. The long-conversation suite is expensive, forty-plus turns times however many judge calls per turn, and belongs on a nightly schedule instead, where a slower, fuller run is affordable.

Budget for judge calls specifically: a forty-turn conversation scored on one invariant per turn is forty extra model calls beyond the conversation itself, and that adds up fast running nightly. Gate on pass rate at the suite level the same way you gate on it per test, and treat a regressed rate, not any single flake, as the signal worth blocking a merge over:

[.github/workflows/multi-turn-tests.yml](https://github.com/Autonoma-Tools/how-to-test-multi-turn-conversations/blob/main/.github/workflows/multi-turn-tests.yml)

## The Practitioner Takeaway

Every test pattern above proves the same narrow thing: the conversation, as text, held together. That's real and worth proving, and it's also not the whole application. A booking bot can pass all three failure-mode tests here, hold Maya's name across the topic switch, degrade gracefully past the window, stay in persona for sixty turns, and still leave the booking showing two passengers after the reply said "okay, removed." The transcript was coherent. The app state wasn't, and no test that only reads the conversation catches that gap.

We built [Autonoma](https://getautonoma.com) for exactly that layer. It runs behavioral end-to-end tests against the running application in a preview environment on the pull request, driving the conversation the way a user would and then asserting on what the product actually holds: the passenger count on the booking, the credit on the account, the ticket's owner. Every claim a reply makes about the world becomes checkable against the world. The bot saying "okay, removed" stops being evidence of anything, which is the correct amount of weight to give it.

The maintenance side matters as much as the assertion for a conversational feature, because prompts and flows change weekly. Autonoma's Diffs Agent reads each pull request's diff and updates the suite alongside the code, so a scripted conversation that no longer matches the product gets revised rather than quietly asserting last month's flow. A stale multi-turn suite is a particularly expensive kind of stale, since each scenario is long, hand-built, and easy to trust on reputation alone.

So script the three failure modes above into your suite and gate on pass rate instead of a single run. That catches the class of bug turn-by-turn evals were never built to see. Then put [Autonoma](https://getautonoma.com) underneath it, because the conversation holding together and the application doing what it said are two separate claims, and only one of them has a user's money attached. Turn fourteen is worth catching. The booking that never changed is worth catching more.

## Frequently Asked Questions

## Frequently Asked Questions

### How do you test multi-turn conversations in a chatbot?

Script a conversation with a user simulator, run it against your system, and assert on invariants using a judge rather than exact-match text. Test three failure modes separately: whether a fact survives an intervening, unrelated topic (coreference), whether pinned facts survive crossing the context window's truncation boundary, and whether quality holds steady across twenty or more turns instead of drifting.

### What is context window testing?

Context window testing means deliberately padding a conversation with filler turns until it crosses your system's actual truncation or summarization threshold, then probing whether a fact pinned earlier in the conversation survives. The acceptable outcomes are remembering the fact or acknowledging it's gone; the failure worth blocking on is confidently inventing a replacement instead of admitting the gap.

### How do you test context loss in long conversations?

Run a long scripted conversation, score every turn against the same invariant (an instruction, a persona trait, a prior commitment), and assert the score doesn't regress past a threshold as the conversation gets longer. A single check at the end misses this, since the decay is gradual, not a single failure point.

### Is context retention the same as long-term memory in AI chatbots?

No. Context retention is whatever the model can see inside the current session's token window, and it disappears when the session ends. Long-term memory is whatever the system deliberately writes to a durable store and retrieves in a later, separate session. A bot can pass every multi-turn test and still have no persistent memory, and the reverse is just as possible.

### My multi-turn tests pass, but users still say the bot didn't do what it said. What am I missing?

Almost certainly the application layer. Every pattern in this article reads the conversation, so it can prove a fact survived a topic switch, that the bot degraded gracefully past the truncation boundary, and that it held its persona for sixty turns, and none of it looks at what the product actually holds afterward. A booking bot can reply 'okay, removed' inside a perfectly coherent transcript while the reservation still shows two passengers, and a transcript-level judge scores that reply as correct, because as a sentence it is. Catching it means driving the running application and asserting on its state, which is the layer Autonoma runs: the same scripted conversation against the real app, with the assertion on the passenger count rather than on the reply describing it.

---

This is the markdown variant of <https://getautonoma.com/blog/how-to-test-multi-turn-conversations>, served by content negotiation (`Accept: text/markdown`) and also available directly at <https://getautonoma.com/md/blog/how-to-test-multi-turn-conversations>.

Other agent surfaces: [llms.txt](https://getautonoma.com/llms.txt), [resource catalog](https://getautonoma.com/.well-known/ai-catalog.json), [developer portal](https://getautonoma.com/developers), [sitemap](https://getautonoma.com/sitemap.xml).
