# Source: https://getautonoma.com/blog/how-to-qa-an-ai-feature

---
title: "How to QA a Generative AI Feature Before You Ship"
description: "How to QA a generative AI feature before shipping: risk tiers, real eval sets, a red-team pass, behavioral E2E, staged rollout, and production monitoring."
date: "2026-07-27"
canonical: "https://getautonoma.com/blog/how-to-qa-an-ai-feature"
authors:
  - "Tom Piaggio"
tags:
  - "AI"
  - "Testing"
  - "QA Strategy"
---

# How to QA a Generative AI Feature Before You Ship

> **How to QA a generative AI feature** before shipping it comes down to a six-step gate: tier the feature by what a wrong output actually costs, build an eval set from real user inputs instead of invented prompts, run a guardrail and red-team pass, verify the feature's actions inside the running app rather than just its response, ship it behind a flag with a real rollback trigger, and monitor production for drift that feeds back into the eval set.

> A Python reference implementation of the pre-ship QA gate in this article: an eval-set runner with pass-rate thresholds across repeated runs, a red-team/guardrail subset runner, a composed ship-gate script that exits non-zero below threshold, and the GitHub Actions workflow that wires it into CI. [Source on GitHub](https://github.com/Autonoma-Tools/how-to-qa-an-ai-feature).

Someone on your team just merged a PR that drops a generative AI feature into the product. A support assistant, a smart search box, an autofill that drafts replies. The Slack message says something like "looks good, ready to test?" You open it, type a few messages, it looks fine. Then what? A regression suite built for deterministic software has nothing useful to say about a component that can give a different answer to the same input twice.

This is the ship-gate problem: a sequence for finding out, with actual evidence, whether an AI feature is safe to release before real users touch it. Not a taxonomy of testing types. Not a philosophy of "AI risk." A sequence, ordered, gated, with a runnable artifact behind each step you can point to when someone asks how you know it works.

> **Diagram:** The six-step pre-ship QA gate for an AI feature. Six connected stages in two rows of three: risk tier, eval set, and guardrail/red-team on top, then behavioral E2E, staged rollout, and production monitoring on the bottom, with behavioral E2E highlighted in lime as the step most teams skip.

*Six gated steps, not six independent checklists. A cosmetic feature can reasonably stop after step 2; an irreversible feature does not get to skip steps 4 through 6.*

The behavioral E2E step needs a check on the running product, not another score on the model's sentence. That is the layer [Autonoma](https://getautonoma.com) covers: it verifies the state and side effect the feature actually produced in the UI.

## Tier the Feature by What a Wrong Output Actually Costs

Start here, before writing a single test case, because the tier decides how much of the rest of this playbook is mandatory. A wrong output from a marketing-copy generator and a wrong output from a refund assistant are not the same category of problem. Treating them the same either wastes weeks over-testing a blurb generator or ships an under-tested feature that moves money.

Four tiers cover most of what ships. Cosmetic: the AI generates copy or content a human reviews before it goes anywhere, so a wrong tone or an awkward phrase gets caught before publishing. Advisory: the AI recommends, but a person still decides. A wrong suggestion here costs someone a few minutes, not a broken outcome. Actionable: the AI's output directly changes what the product does next, an auto-sent reply, an updated ticket, with no human checkpoint in between. Irreversible: the output triggers something that is expensive or impossible to undo, a refund, a deleted record, a message sent to a customer that can't be unsent.

| Tier | Example | Mandatory before ship |
| --- | --- | --- |
| Cosmetic | Marketing blurb tone | Eval set only |
| Advisory | Search ranking suggestion | Eval set + red-team |
| Actionable | Auto-sent ticket reply | + Behavioral E2E |
| Irreversible | Refund amount assistant | + Rollout + kill switch |

The tier is a gate, not a suggestion. A cosmetic feature that never touches a system of record can reasonably ship after step two. An irreversible feature does not get to skip steps four through six no matter how good the eval-set numbers look, because an eval set never watched the feature run against your actual application.

## Build the Eval Set From What Users Actually Typed

The single most common mistake in this step is writing twenty synthetic prompts by hand and calling it an eval set. Real inputs are uglier: typos, half-finished sentences, a wall of pasted text, one message that combines three intents at once, the edge case where someone asks a refund assistant about a return that already happened. Mine the eval set from actual sources, support tickets, transcript logs from a beta, sales-call summaries, whatever real usage already exists. If the feature is new enough that no usage exists yet, borrow adjacent data from an existing support queue in the same domain before inventing prompts from imagination.

Then comes the part a written eval set alone doesn't solve. The same case can pass on Monday and fail on Tuesday against the identical input, because the model draws from a distribution, not a lookup table. Run every case `N` times instead of once, and assert against a pass-rate threshold, "passes at least four of five runs," instead of a single boolean. Exact match still works for structured fields: a refund amount, a status code, an extracted date either match or they don't. For free text, exact match fails correct answers just for using different words, so score those with semantic similarity or an LLM-judge rubric instead, and sample the judge's own score across a few runs too, since it has the same non-determinism the feature does.

When a case flakes under this setup, there are exactly two honest explanations, and the fix is different for each. Either the assertion is too strict for a task with more than one correct phrasing, in which case loosen it to semantic similarity instead of exact match, or the prompt itself is ambiguous enough that a reasonable person could answer it two different ways, in which case the prompt needs fixing, not the test. Treating a flaky AI test as "just rerun it" without deciding which of those two is true is how eval sets rot into noise nobody trusts.

Here's a minimal runner that applies all three rules at once: repeated runs, a configurable pass-rate threshold, and a semantic-similarity check for free-text fields alongside exact match for structured ones.

[eval_suite/eval_runner.py](https://github.com/Autonoma-Tools/how-to-qa-an-ai-feature/blob/main/eval_suite/eval_runner.py)

## Run the Guardrail and Red-Team Pass

An eval set tells you the feature answers correctly under normal use. It says nothing about what happens when someone deliberately tries to break it, and in a shipped product, someone will. This step is adversarial by design: injection attempts that try to override the system prompt, jailbreak phrasing that tries to get the feature to ignore its own guardrails, and probes that fish for data the feature shouldn't disclose.

The specific techniques here deserve their own treatment rather than a rushed summary. For the injection side, [how to test for prompt injection](/blog/how-to-test-for-prompt-injection) covers building the adversarial payload set itself, and [how to test AI guardrails](/blog/how-to-test-ai-guardrails) covers verifying the guardrail blocks what it should without over-blocking legitimate requests. What belongs here is the sequencing: this pass runs after the eval set, because a feature that fails on cooperative inputs has no business being red-teamed yet, and it runs before behavioral E2E, because an injection payload that reaches the running application is a worse problem than one caught at the response layer.

One more failure mode belongs in this pass even though it isn't adversarial in the usual sense: faithfulness. Does the answer stay grounded in whatever context it was given, or does it confidently state something nobody fed it? A confident, wrong answer is worse than an obviously broken one, because nothing about it signals "check this." [How to test for AI hallucinations](/blog/how-to-test-for-ai-hallucinations) covers the faithfulness checks in depth; the short version for this gate is that a red-team subset without at least a few groundedness cases is testing adversarial inputs while ignoring the failure mode most likely to reach production quietly.

The red-team runner reuses the same pass-rate machinery as the eval runner, pointed at an adversarial payload set instead of normal-use cases, and fails the gate on any critical payload that gets through:

[eval_suite/redteam_runner.py](https://github.com/Autonoma-Tools/how-to-qa-an-ai-feature/blob/main/eval_suite/redteam_runner.py)

## Test the Feature Inside the Running App, Not Just the Response

Every step so far scores the response: does the eval set case pass, does the red-team payload get blocked, is the answer grounded in context. None of them confirm the feature actually did the right thing inside the product. An assistant can generate a perfectly worded confirmation, "your ticket has been escalated," and never actually update the ticket. A refund assistant can state the correct amount in its response and post a different amount to the database, or post nothing at all, because the tool call it was supposed to make failed silently. The eval set graded the sentence. Nobody checked the side effect.

Behavioral E2E closes that gap by testing the feature the way a user actually encounters it, in the running application, checking the state that resulted rather than the words that were generated. Did the ticket's status field actually change. Did the refund amount that landed in the database match the number in the assistant's message. Did the UI advance to the screen the response implied it would. None of that is visible from an eval set's scorecard, because an eval set was never looking at the application in the first place.

> An eval set tells you the response scored well. It cannot tell you the feature did the right thing in the app the response was supposed to trigger.

This is also where a single feature's testing surface connects back to the broader question of testing a generative AI application end to end. Eval sets and behavioral E2E aren't competing approaches, they're two layers of the same pipeline, covered in full in [testing generative AI applications](/blog/testing-generative-ai-applications).

## How Autonoma Verifies the Feature's Actual Action

The gap this playbook keeps circling back to is the same one every eval-set-only approach has: a response can read correctly while the action behind it is wrong, missing, or never happened, and nothing at the response layer would ever catch it.

That's the layer we built [Autonoma](https://getautonoma.com) to run. Instead of grading a transcript, Autonoma's Planner reads your application's actual code, the routes, the components, the flows a feature's output is supposed to trigger, and plans test cases against the real running app on a live preview environment. The Executor drives that UI the way a user would and confirms the resulting state, not just the resulting sentence: the ticket status, the refund amount, the screen the app actually landed on. When the feature's code changes, the Diffs Agent updates the affected test cases from the diff itself, so this layer doesn't quietly go stale the way a hand-written E2E suite does. It's worth being precise about what this replaces and what it doesn't: Autonoma isn't an eval framework and it doesn't score model outputs. It's the layer above the eval set, confirming that a response which scored well also produced the right outcome in the product.

Mapped onto this playbook: steps one through three are entirely about the response, is it correct, is it safe, is it grounded. Step four is where behavioral E2E, and specifically this layer, takes over, checking the application state a response is supposed to produce. Steps five and six are about how safely you expose all of that to real traffic.

> **The answer looked right. Did the action?** Autonoma runs agentic end-to-end tests on every pull request. [Try Autonoma](https://autonoma.app).

## Ship Behind a Flag You Can Actually Kill at 2am

Nothing in steps one through four replaces a staged rollout, because the eval set, the red-team payloads, and the behavioral E2E suite are all necessarily a sample of the input space, not the whole of it. A staged rollout is how you contain whatever that sample missed.

Put the feature behind a flag from day one, not as an afterthought once something breaks. Ramp it as a percentage rather than a binary: five percent of traffic, then twenty five, then everyone, with a dwell time at each stage long enough to notice a problem before the next ramp. Decide the rollback trigger before you need it, not while staring at a spike: a hard-failure rate on actionable or irreversible outputs past some threshold, a support-ticket spike tagged to the feature, a specific metric moving the wrong direction.

The switch has to be something a human can flip without a deploy. A config flag in a feature-flag service, not a boolean buried in application code that needs a build and a release to change, because the moment you need the kill switch is the worst possible moment to also need an engineer awake, a PR, a review, and a deploy pipeline to run cleanly. If the rollback plan requires all of that, there is no kill switch, only a plan to eventually recover.

## Monitor Production and Feed Failures Back Into the Eval Set

The gate doesn't end at rollout. What gets logged, what gets sampled for human review, and what alerts on drift together decide whether a regression is caught in hours or discovered from a support queue three weeks later.

Log enough to reconstruct what happened without re-running anything: the input, the model version and prompt version that produced the response, the full response, and, critically, the resulting action or state change if the feature is actionable or irreversible. Sample a meaningful slice of production traffic for a human to actually read, not just the flagged failures, because the failures nobody thought to flag are exactly what a review pass exists to catch.

Alert on drift, not just on errors: an actionable feature's tool-call success rate dropping, response length or tone shifting after a silent model update behind the same API alias, a rise in the rate of refusals or "I don't know" responses. Close the loop deliberately. Every real failure a human confirms in production becomes a new eval-set case, so the eval set from step two keeps growing from what actually happened instead of staying frozen at whatever you could imagine before launch.

## The Ship Gate: One Script, One Threshold, One Decision

Everything above is a sequence a human can reason through. What a CI pipeline needs is a single script with a single exit code: did this change clear the bar or not.

Before wiring that up, here's what actually blocks a release once all six steps are in place:

> **Diagram:** The pre-ship gate checklist. A vertical checklist of six items, each with a checkmark in a lime circle: eval set pass rate at or above threshold, red-team subset clean, behavioral E2E green on staging, rollback trigger defined and tested, kill switch reachable without a deploy, and monitoring wired before rollout.

*The last two items are the ones teams skip under deadline pressure, right before the release that needed them.*

The gate script composes the eval runner and the red-team runner, computes a combined pass rate, and exits non-zero the moment either drops below its configured threshold:

[ship_gate.py](https://github.com/Autonoma-Tools/how-to-qa-an-ai-feature/blob/main/ship_gate.py)

Wire that exit code into whatever already gates your other merges. The gate doesn't need to be smarter than your CI system, it just needs to be a script CI can call and trust the exit code of. Here's the workflow that runs it on every pull request touching the feature, failing the check the same way a failing unit test would:

[.github/workflows/ai-feature-gate.yml](https://github.com/Autonoma-Tools/how-to-qa-an-ai-feature/blob/main/.github/workflows/ai-feature-gate.yml)

None of this replaces judgment. It turns "do we know it works" into a script with an exit code, an eval set built from real cases behind it, a red-team pass that actually ran, and a check on the feature's real actions in the app, the layer [Autonoma](https://getautonoma.com) exists to verify, confirming the outcome matched what the response said it would be.

## Frequently Asked Questions

## Frequently Asked Questions

### How do you QA a generative AI feature before shipping it?

Run it through a six-step gate: tier the feature by what a wrong output actually costs, build an eval set from real user inputs and run each case multiple times against a pass-rate threshold, run a guardrail and red-team pass for injection and faithfulness failures, verify the feature's actions in the running app rather than just its response, ship behind a flag with a defined rollback trigger, and monitor production for drift that feeds new cases back into the eval set.

### What goes in an AI feature testing checklist?

At minimum: an eval set pass rate at or above a defined threshold across repeated runs, a red-team subset with zero critical failures, behavioral E2E passing on a staging or preview environment (checking application state, not just the response text), a rollback trigger that's defined and tested before launch, a kill switch reachable without a deploy, and monitoring or drift alerts wired in before rollout rather than added after the first incident.

### How do you handle non-determinism when testing AI features?

Run every eval case multiple times instead of once and assert against a pass-rate threshold instead of a single pass or fail. Use exact match for structured fields like amounts or status codes, and semantic similarity or an LLM-judge rubric for free text, since exact match will fail correct answers that are simply phrased differently. When a case flakes, the fix is either loosening an overly strict assertion or fixing an ambiguous prompt, not just rerunning the test.

### What's the difference between an eval set and behavioral E2E testing for AI features?

An eval set scores the AI's response in isolation: is the text correct, safe, and grounded in context. Behavioral E2E tests the feature inside the running application and checks what actually happened as a result, whether a database record updated, whether a ticket status changed, whether the UI advanced correctly. A response can score well on an eval set and still correspond to an action that failed or never happened, which is the gap behavioral E2E exists to close.

### What's a kill switch for an AI feature rollout?

A kill switch is a way to disable or roll back an AI feature that a human can flip immediately, without a code deploy, typically a feature flag in a flag-management service rather than a boolean buried in application code. It's paired with a rollback trigger defined ahead of time, a specific failure rate or metric threshold, so the decision to flip it doesn't have to be made under pressure during an incident.

---

This is the markdown variant of <https://getautonoma.com/blog/how-to-qa-an-ai-feature>, served by content negotiation (`Accept: text/markdown`) and also available directly at <https://getautonoma.com/md/blog/how-to-qa-an-ai-feature>.

Other agent surfaces: [llms.txt](https://getautonoma.com/llms.txt), [resource catalog](https://getautonoma.com/.well-known/ai-catalog.json), [developer portal](https://getautonoma.com/developers), [sitemap](https://getautonoma.com/sitemap.xml).
