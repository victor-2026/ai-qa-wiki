# Source: https://getautonoma.com/blog/how-to-test-ai-agent-memory
# Fetched: 2026-08-31

---
title: "How to Test AI Agent Memory (Short- and Long-Term)"
description: "How to test AI agent memory: within-session recall, cross-session persistence, retrieval accuracy against decoys, staleness, and a runnable pytest suite."
date: "2026-07-29"
canonical: "https://getautonoma.com/blog/how-to-test-ai-agent-memory"
authors:
  - "Tom Piaggio"
tags:
  - "Testing"
  - "AI"
  - "AI Agent Testing"
---

# How to Test AI Agent Memory (Short- and Long-Term)

> **How to test AI memory** starts with one definition: verify that an agent stores, retrieves, and correctly applies information from earlier in the same session and from entirely separate sessions, not just that it writes a plausible-sounding reply. That means testing four things directly: recall across distractor turns, persistence into a brand-new thread, retrieval accuracy against decoy memories, and whether a newer fact correctly overrides an older, conflicting one.

> A vendor-neutral, runnable Python and pytest suite for testing AI agent memory: within-session recall past distractors, cross-session persistence, retrieval accuracy against decoy memories, staleness, and a CI gate that splits unit-level checks from the cross-session integration job. [Source on GitHub](https://github.com/Autonoma-Tools/how-to-test-ai-agent-memory).

A support agent we watched during a review call greeted a returning user by name: "Hey Priya, welcome back." Two days later, same user, a brand-new conversation: "I don't have your name on file, who am I speaking with?" The test suite was green the whole time: every test opened a fresh conversation, asked one question, checked the reply, and never asked the agent to remember something and come back later.

That gap is invisible from inside a single conversation. A multi-turn test catches the agent losing track of something said three messages ago. It doesn't catch it losing track of something said three days ago in a different thread: a different mechanism failing, not the context window, the memory store behind it.

Memory is also where AI-native testing stops resembling model evaluation and starts resembling application testing. Nothing about the greeting above is a language problem. The reply was well-formed both times; a row was written or it wasn't, a query matched or it didn't. That's a stateful application bug wearing a chatbot's clothes, which is why the coverage that actually catches it looks like end-to-end testing rather than scoring. It's the reasoning behind how we built [Autonoma](https://getautonoma.com), and it shapes every assertion in this piece.

## Memory Is Not Context

Context retention is what survives inside the model's context window during one conversation: the last several turns, still visible when it replies. Memory is persistent storage that outlives the window and the session: written once, retrievable in a conversation that hasn't even started yet.

Conflating the two is exactly why memory bugs slip past context-focused test suites. A context-window failure is a truncation or eviction problem: something got pushed out of the prompt before the model needed it again. A memory failure is a write-or-retrieve problem: either the fact never made it into storage, or it did, and the retrieval query never matched it.

> A context bug loses something the model could technically still see. A memory bug loses something the model was never given a chance to see again.

Recall inside one conversation and recall across two separate ones are not the same test. This piece covers the second: within-session recall past distractors, cross-session persistence, retrieval accuracy against near-miss memories, and staleness. For the context-window layer itself, truncation and how far a long conversation degrades before the model loses the thread, see [how to test multi-turn conversations](/blog/how-to-test-multi-turn-conversations).

## Testing Within-Session Recall

Within-session recall tests AI memory retention inside one conversation: does the agent still have a fact once it's no longer the topic on screen? State a fact, inject a handful of unrelated turns, then ask something answerable only using the fact from several turns back.

If you already run a multi-turn harness (a user simulator, an agent, a judge scoring the transcript), memory assertions bolt onto the same loop. See [agent simulation testing](/blog/agent-simulation-testing) for that harness in raw Python.

Don't assert on exact wording: "the deploy window is Tuesdays 2 to 4pm" and "you're set for Tuesday afternoon, 2 to 4" are both correct, and an exact-match assertion will flake between them for reasons that have nothing to do with memory. Assert on the fact's presence semantically instead.

Here's the memory client and agent interface every test in this piece shares: a persistent store, a fresh-namespace helper for test isolation, and an agent that writes and retrieves against it.

[memory_client.py](https://github.com/Autonoma-Tools/how-to-test-ai-agent-memory/blob/main/memory_client.py)

And the within-session recall test itself: state the fact, inject three distractor turns, then assert the reply carries the fact semantically.

[test_within_session_recall.py](https://github.com/Autonoma-Tools/how-to-test-ai-agent-memory/blob/main/test_within_session_recall.py)

> **Diagram:** Diagram contrasting within-session memory, which lives in one conversation.

*Within-session recall reads from the same context window the fact was stated in. Cross-session memory has to survive that window being discarded entirely.*

## Testing Cross-Session Memory

Cross-session memory, the core of how to test long-term memory in AI agents, asks a different question: does the fact survive into a conversation that hasn't started yet, with a completely fresh context window? This is where most implementations fail silently. The write step succeeds, but the read-side retrieval query at the start of the next session never matches it, because it was phrased differently or scoped to the wrong session id instead of the wrong user id.

The test pattern: session A writes a fact. Tear the conversation down completely, no shared object, a genuinely new agent instance. Session B, same user id, reads. If the assertion only passes because session B reuses session A's in-memory state, the test is lying to you; the point is that nothing from session A survives except what made it into the persistent store.

The teardown is the assertion, which is worth stating plainly because it's also the thing hardest to fake at the harness level. A fresh Python object is a weaker teardown than a fresh process, and a fresh process is weaker than a fresh browser session against the deployed app with a real database behind it. Each step up closes a class of false pass. The strongest version of this test is the one Autonoma runs: drive the product through a real session, close it, come back in a new one, and check what the agent knows against what the application actually stored. At that level there is no shared state left to accidentally pass on, because the only thing connecting the two sessions is the user id and the database.

Here's that test, plus a case that looks like a memory bug and usually isn't: a query with no overlap returns the correct "I don't know" fallback, while the fact itself is still sitting untouched in the store.

[test_cross_session_memory.py](https://github.com/Autonoma-Tools/how-to-test-ai-agent-memory/blob/main/test_cross_session_memory.py)

## Retrieval Accuracy: The Decoy Problem

Persistence isn't the hard part. Getting the right memory back is. An agent with three stored addresses needs to retrieve the one matching the question, not a plausible neighbor or a hallucinated one. This dimension gets the least attention, because it only shows up once the store holds more than one similar fact.

Seed similar-but-distinct memories, query for one, and assert two things at once: the correct value is present, and the decoy values are absent. Most teams write the first assertion and skip the second, and the second is what actually catches a retrieval bug: a reply with the right address that also lists the wrong ones isn't passing, it's an agent that dumped its whole memory into the prompt and got lucky.

The same pattern covers the no-memory case: ask about something never stored, and the agent should say it doesn't know, not invent a plausible answer from whatever else is in context.

[test_retrieval_accuracy.py](https://github.com/Autonoma-Tools/how-to-test-ai-agent-memory/blob/main/test_retrieval_accuracy.py)

> **Diagram:** Diagram of a retrieval-accuracy assertion: a query hits a memory store holding one correct memory and two decoy memories, and the assertion checks that the correct value is present and both decoy values are absent.

*The positive assertion is the easy half. The negative assertion, that the decoys never leak into the reply, is the one most memory tests skip.*

## Context Carryover: When Memory Changes Behavior

The hardest dimension isn't a string check at all. A user says "I'm on the Free plan" in one session; the test that matters isn't whether a later reply contains the word "free," it's whether that fact changes what the agent does: does it still offer an enterprise-only action to a user who said, sessions ago, they're not on that plan?

That's a behavioral assertion, not a text-match, and it needs an LLM-as-judge or an explicit rubric rather than a substring check, because the phrasing of a denial varies every run while the underlying decision doesn't. Write the criteria as something checkable: does the response withhold the action, does the reason reference the stored plan tier.

A green suite hides the most expensive bug right here: the reply reads fine while the underlying action is wrong, a Free-plan user routed into an enterprise-only workflow because the check only looked at words, never the state change behind them. That's the same gap [Autonoma](https://getautonoma.com) exists to close on the application side: our agents run behavioral end-to-end tests against the real running app, so a wrong action shows up as a wrong outcome in the product, not just a sentence that reads fine.

[test_context_carryover.py](https://github.com/Autonoma-Tools/how-to-test-ai-agent-memory/blob/main/test_context_carryover.py)

> **Test that your agent remembers, not just replies.** Autonoma runs agentic end-to-end tests on every pull request. [Try Autonoma](https://autonoma.app).

## Staleness: The Newer Fact Has to Win

A memory system that stores every version of a fact without resolving conflicts produces an agent that's technically correct and practically useless. The user said "I live in Lisbon" in March, "I moved to Berlin" in June. Query in July, and the answer has to be Berlin, not both, and not the older one because it got retrieved first.

Test this directly: write the same key twice with a conflicting value, assert the reply carries only the newer one. The retrieval-accuracy suite above already exercises this, since the store overwrites by key rather than appending, but it's worth asserting on by name: staleness bugs are usually a storage-layer decision made months before anyone writes a test for it.

## Handling Non-Determinism in Memory Assertions

Every assertion here rides on a model call, and the same input produces different words each run. That's a different flavor of flaky than a brittle CSS selector, and loosening the assertion until it stops complaining is almost always the wrong fix.

Use semantic containment for anything the model is free to phrase. Reserve exact-match for hard values that must appear verbatim: an order id, a dollar figure. For the harder behavioral checks, use an LLM-as-judge graded against an explicit rubric. For anything genuinely variance-sensitive, run it five times and gate on a threshold, four out of five, rather than a single pass.

> A flaky memory test almost always means one of two things: the assertion is stricter than the thing it's checking, or the memory prompt itself is ambiguous enough that the model has room to interpret it differently each run. Find out which before you "fix" it by loosening the pass bar.

Loosening a threshold hides a real bug behind a statistic. Tightening the persona or the judge's rubric fixes the actual ambiguity, and that's almost always where the fix belongs.

## How Do You Wire Memory Tests Into CI?

Unit-level memory tests (within-session recall, retrieval accuracy, staleness) run against an in-memory store and belong in your normal CI job, on every pull request. Cross-session tests need a real persistence backend, since the point is confirming state survives a teardown, and an in-memory stub survives everything trivially, including bugs you'd want caught.

Give cross-session tests their own integration job against a disposable, per-run instance of that backend, and give every run a fresh, unique user id. Two runs sharing a user id pollute each other's memories: a test can pass because a previous run's leftover fact is still sitting there, worse than a red build.

Here's the gate: unit-level tests in the main job, cross-session tests split into a job that documents the real-backend requirement.

[.github/workflows/memory-tests.yml](https://github.com/Autonoma-Tools/how-to-test-ai-agent-memory/blob/main/.github/workflows/memory-tests.yml)

### Memory vs. Context Retention, at a Glance

| Dimension | Memory | Context Retention |
| --- | --- | --- |
| What it is | Facts stored outside the model, across sessions | What survives inside one active context window |
| Where it lives | A database, cache, or vector store | The live prompt, this conversation only |
| How it fails | Write succeeds, retrieval query never matches | Older turns get truncated or evicted |
| How you test it | Cross-session read after a full teardown | Recall mid-conversation, before truncation |
| Which article covers it | This article | [Multi-turn conversations testing](/blog/how-to-test-multi-turn-conversations) |

Testing whether an AI remembers previous conversations comes down to one discipline: write in one session, tear down, read in a genuinely new one, and assert semantically. Pair that with retrieval accuracy against decoys and a staleness check, and the memory layer gets the same coverage the rest of your application already has. For the multi-turn harness these tests can run inside of, see [agent simulation testing](/blog/agent-simulation-testing); for the context-window layer itself, see [how to test multi-turn conversations](/blog/how-to-test-multi-turn-conversations).

## Where a Memory Suite Stops, and What Picks It Up

Every test above answers the same question: does the agent say the right thing given what it should remember. That's the correct question for a memory layer and the wrong question for the product wrapped around it. The Free-plan case from earlier is the tell. What matters isn't that the agent mentions the plan tier, it's whether the enterprise-only action stayed unavailable, whether the upgrade path rendered, whether the audit record shows what actually happened. Those live in the application, and a suite that reads replies can't reach any of them.

That's the layer [Autonoma](https://getautonoma.com) covers. It runs behavioral end-to-end tests against the real running application in a preview environment on the pull request, so a stored fact is verified by its effect on the product rather than by its appearance in a sentence. The two suites fit together cleanly: the pytest suite above pins the memory client's contract fast and offline on every commit, and the behavioral layer proves that contract still means something once the rest of the app is in the picture.

The maintenance argument is the one that usually decides it, though. Memory tests are unusually brittle for a reason that has nothing to do with models: they encode assumptions about storage keys, user scoping, and retrieval phrasing, and all three get refactored without anyone thinking of them as behavior changes. Autonoma's Diffs Agent updates the suite from each pull request's diff, which is what keeps a scoping change from turning a memory test into a test of nothing at all. That failure is quiet, and a quiet memory test is worse than none, because it reads as proof the Priya bug can't happen again.

## Frequently Asked Questions

## Frequently Asked Questions

### How do you test AI agent memory?

Test AI agent memory across four dimensions: within-session recall (does the agent still have a fact after several unrelated turns), cross-session persistence (does the fact survive into a brand-new thread with a fresh context window), retrieval accuracy (does the agent retrieve the right memory instead of a similar decoy or a hallucinated one), and staleness (does a newer, conflicting fact correctly override an older one). Assert on the fact's presence semantically rather than exact wording, since the model phrases the same correct answer differently every run.

### What's the difference between memory and context in an AI agent?

Context is what survives inside the model's context window during one active conversation: recent turns still visible to the model when it replies. Memory is persistent storage that outlives both the window and the session: written once and retrievable in a conversation that hasn't started yet. A context failure is a truncation or eviction problem. A memory failure is a write-or-retrieve problem, and the two need different tests.

### How do I test if an AI remembers previous conversations?

Write a fact in one session using a fresh, isolated user id, then tear that session down completely and start a genuinely new session, a new agent instance with no shared in-memory state, using the same user id. Ask a question in the new session that can only be answered correctly using the earlier fact. If the reply carries that fact semantically, cross-session memory is working. If it doesn't, check whether the write actually reached persistent storage before assuming the retrieval query is at fault.

### What is AI session persistence testing?

AI session persistence testing verifies that information a user shared in one conversation is available and correctly applied in a later, unrelated session, not just recalled within the same conversation. It requires a genuine teardown between sessions, no shared context window or in-memory object, and a shared, stable user identifier so the read-side session can find what the write-side session stored.

### Why does a memory test fail intermittently?

An intermittent memory test failure usually means one of two things: the assertion is stricter than what it's actually checking, such as an exact-match assertion against a model's freely-phrased reply, or the underlying prompt or persona is ambiguous enough that the model has room to answer differently each run. Loosening the pass threshold hides the problem rather than fixing it. Tighten the wording of the stored fact, the query, or the judge's rubric first, and only add run-N-times gating for genuinely borderline behavioral checks.

### How do you test long-term memory in an AI agent?

Long-term memory testing is cross-session testing plus a time dimension. Write a fact in one session, tear the session down completely, and read it back in a genuinely new session using the same stable user id. Then add two assertions the short-term case does not need: that a newer conflicting fact overrides the older one rather than both being returned, and that the correct memory is still retrievable once the store holds many similar facts, not just the one you seeded. Run these against a real persistence backend, since an in-memory stub survives a teardown trivially and will pass even when the write never reached storage.

### My memory tests pass, but a user still got an action they shouldn't have. What's the gap?

The suite is checking what the agent said rather than what the product did. A test can confirm the agent correctly recalls that someone is on the Free plan and still miss that the enterprise-only action stayed available, that the upgrade path never rendered, or that the audit record shows something different from the reply. Those outcomes live in the application, not in the sentence, so the assertion has to land there too. It's also why the teardown in a cross-session test matters: a fresh Python object is a weaker teardown than a fresh session against the deployed app with a real database behind it. Autonoma runs behavioral end-to-end tests against that real running application, so a stored fact gets verified by its effect on the product rather than by its appearance in a reply.

---

This is the markdown variant of <https://getautonoma.com/blog/how-to-test-ai-agent-memory>, served by content negotiation (`Accept: text/markdown`) and also available directly at <https://getautonoma.com/md/blog/how-to-test-ai-agent-memory>.

Other agent surfaces: [llms.txt](https://getautonoma.com/llms.txt), [resource catalog](https://getautonoma.com/.well-known/ai-catalog.json), [developer portal](https://getautonoma.com/developers), [sitemap](https://getautonoma.com/sitemap.xml).
