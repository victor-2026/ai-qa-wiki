# Source: https://getautonoma.com/blog/agent-regression-testing
Fetched: 2026-08-31

---
title: "Agent Regression Testing: When Your Agent Breaks Without a Deploy"
description: "Agent regression testing catches silent AI regressions after a model update: golden trajectories, N-run averaging, and CI threshold gating, with runnable code."
date: "2026-07-24"
canonical: "https://getautonoma.com/blog/agent-regression-testing"
authors:
  - "Tom Piaggio"
tags:
  - "Testing"
  - "AI"
  - "Regression Testing"
---

# Agent Regression Testing: When Your Agent Breaks Without a Deploy

> **Agent regression testing** is the practice of re-running a fixed set of known-good agent trajectories against every new model version, prompt, or knowledge-base update, then flagging any drop in an aggregated score, because an AI agent has no code deploy a normal regression suite can hook into. It differs from traditional regression testing in one critical way: since a single run is non-deterministic, you run each case N times and compare the averaged score, not one pass or fail, against a baseline within a tolerance band.

> The full runnable harness from this article: golden-trajectory capture, a structural-plus-similarity scorer, an N-run averaging pytest suite, and the nightly-plus-on-change CI gate. Clone it and swap in your own agent. [Source on GitHub](https://github.com/Autonoma-Tools/agent-regression-testing).

Tuesday's dashboard read 93% routing accuracy, the number our support agent had held steady for six weeks. Thursday it read 71%. Nobody had opened a pull request. Nobody had merged anything. The deploy log for that window was empty.

The model provider had swapped the LLM behind the API endpoint we called, quietly, mid-week, with no changelog entry any QA process would think to watch. Same prompt. Same tools. Same "test suite," if you could call it that, a handful of exact-string assertions against old transcripts, and every one of those assertions still passed, because the agent still replied in English and still called a tool. It just called the wrong one, more often, in ways a string match will never see.

That's the failure mode this piece is about: a regression with nothing to do with your code.

## The Silent Model Update That Cost 22 Points of Accuracy

The setup was mundane, which is exactly why it's worth using as the example. A support-routing agent read an incoming ticket and decided which of four downstream queues it belonged in, billing, technical, account access, or escalate-to-human, then called the matching tool. We measured it the only way that matters: run a labeled set of past tickets through the agent, check whether the tool call it picked matches the human-labeled correct queue, average the hits. That number sat at 93% for six weeks, comfortably above the 90% floor the support team had agreed was acceptable.

Then it dropped to 71%, and the drop showed up as a wave of mis-routed billing tickets landing in the technical queue, not in any dashboard we were watching. When we went looking for what shipped, the answer was nothing. Our prompt hadn't changed. Our tool definitions hadn't changed. Our knowledge base hadn't changed. The one thing that had changed, invisibly, was the model sitting behind the API endpoint the agent called. The provider rolled a new version into the same model name, the routing behavior it had learned to imitate shifted underneath it, and every regression gate we had, all of them keyed to code changes, had nothing to trigger on.

> **Diagram:** The regression with no deploy to blame. A timeline showing routing accuracy flat at 93 percent, a silent model provider update, an empty deploy log, and accuracy dropping to 71 percent.

*The deploy log was empty. The regression wasn't.*

## Why Traditional Regression Testing Doesn't Catch This

Traditional regression testing rests on three assumptions that quietly stop holding once an LLM sits inside the loop. It assumes a change worth testing is a change your team made, so it wires itself to a merge or a deploy hook. It assumes the same input produces the same output, so a snapshot diff or an exact string match is a valid pass or fail signal. And it assumes "correct" is a property of the text itself, checkable by comparing it to a stored answer.

None of those hold for an agent built on a model whose weights you don't control. The provider can update the model behind an API name with no changelog entry your CI would ever parse, which means llm regression testing has to run on a schedule, not a hook, because there is no commit to trigger it. The same prompt against the same model produces different phrasing on every call, so an exact-match assertion will fail constantly on entirely correct output, training every engineer on the team to ignore the test within a month. And correctness for an agent usually lives in the decision, which tool it called, which record it touched, not in the words wrapped around that decision, so grading the text alone misses exactly the kind of regression that took our routing accuracy from 93 to 71.

The 2026 arXiv paper on AgentAssay (arXiv 2603.02601) frames this precisely: token-efficient regression testing for non-deterministic agent workflows means comparing structured execution traces, not raw text, and doing it cheaply enough to run continuously instead of as a one-off audit. That's the right instinct. The rest of this piece is a runnable, vendor-neutral version of it.

## Golden Trajectories: Recording What "Good" Looked Like

A golden trajectory is a recording of one input run through the agent at a moment when a human checked the result and confirmed it was correct. Not just the final reply, the whole path: which tools got called, in what order, with what arguments, and what the agent said at the end. Capture the input, the tool-call sequence, and the final output together, and you have a baseline artifact every future run gets compared against, model update or not.

The discipline that matters here is capturing the trajectory, not just the outcome. "The ticket got routed to billing" is one bit of information. "The agent read the ticket, called `classify_intent`, got back billing at 0.94 confidence, then called `route_to_queue("billing")`" is the actual shape of the decision, and it's the shape that breaks first when a model update shifts behavior, often before the final label changes at all.

Here's a capture script that wraps a single agent invocation and writes exactly that shape to a baseline file, using a plain callable so it works against any agent framework underneath:

[src/capture_baseline.py](https://github.com/Autonoma-Tools/agent-regression-testing/blob/main/src/capture_baseline.py)

Run this once against every case in a labeled set, while the agent is behaving the way you want it to, and check the resulting JSON files into the repo next to the test suite. That directory, not a fresh model call, is what everything downstream compares against.

## Scoring a Fresh Run Against the Golden Baseline

Comparing a fresh run to a golden trajectory needs two different measurements, because the two halves of a trajectory fail in different ways. The tool-call sequence is a hard fact: either the agent called `classify_intent` then `route_to_queue("billing")`, or it didn't, and that half of the comparison should be an exact structural match, not a fuzzy one. The final text reply is not a hard fact. "Routed to billing" and "I've sent this over to the billing team" are both correct, and scoring them with an exact match manufactures regressions out of nothing. That half needs a similarity score, an embedding comparison, a string-similarity ratio, or an LLM-as-judge call, folded into one number alongside the structural half.

Here's a scorer that combines both into a single float between 0 and 1, so a threshold check downstream has one value to compare against the baseline:

[src/scorer.py](https://github.com/Autonoma-Tools/agent-regression-testing/blob/main/src/scorer.py)

That single score is what feeds the drift check. It's also, and this matters for what comes later, a score about the conversation, not about the application the agent's tool calls are supposed to affect. A perfect score here confirms the agent said the right thing and, per the structural half, called the right tool. It does not confirm that `route_to_queue("billing")` actually moved the ticket in the system the support team looks at, or that the technical queue's dashboard reflects the change. Those are two different verification problems, and it's entirely possible to grade the first one perfectly while the second one silently breaks underneath it, which is exactly the gap [Autonoma](https://getautonoma.com) exists to close, a point worth coming back to once the regression suite itself is built.

> **Catch the regression the model bump slipped past.** Autonoma runs agentic end-to-end tests on every pull request. [Try Autonoma](https://autonoma.app).

## Averaging N Runs So Noise Isn't Mistaken for Regression

Every agent invocation in this harness is an LLM call, which means a single fresh run can score lower than the golden baseline for reasons that have nothing to do with a real regression. The model phrased something slightly differently. The similarity function scored a correct paraphrase a little harshly. None of that is the 93-to-71 drop from earlier. It's noise, and treating one low-scoring run as a failed test teaches the team to ignore the test within a week, the same trap as the exact-match assertion from two sections ago.

The fix is to run each golden case N times, average the score across those N runs, and compare the average, not any individual run, against the baseline minus a tolerance threshold. Five runs and a 0.05 tolerance band is a reasonable starting point: run the case five times, average the five scores, and only fail if that average drops more than 0.05 below what the baseline scored. A single bad run out of five barely moves the average. A genuine regression, the kind that would have caught our routing agent's provider swap, drags every one of the five runs down together, and the average reflects that unambiguously.

Here's the pytest suite that does exactly this, one test per golden case, N invocations per test, one averaged assertion:

[tests/test_regression.py](https://github.com/Autonoma-Tools/agent-regression-testing/blob/main/tests/test_regression.py)

Notice what this test does not do: it does not assert that any single run matches the baseline exactly, and it does not treat a below-baseline outlier as a failure on its own. Non-determinism gets absorbed by the average. A real regression, model-wide and consistent across every run, still gets caught, because there's nowhere for it to hide once you're comparing five averaged numbers instead of one noisy one.

## How Autonoma Tests What the Model Change Actually Did

Everything above answers one question well: did the agent's decision and its wording hold up against a known-good baseline. It answers a different question not at all: did the thing the agent's tool call was supposed to do actually happen in the application your users and your support team look at. A perfect regression score on `route_to_queue("billing")` confirms the agent chose to call that function. It does not confirm the ticket's status actually flipped in the admin dashboard, that the technical team's queue count actually went down, or that a stale row didn't get left behind in a table the tool call never touched. That gap is invisible from inside a trajectory, because a trajectory only ever records what the agent claims it did.

That's the layer we built [Autonoma](https://getautonoma.com) to cover, and it runs on a different verification path entirely, not a bigger scorer. The Planner reads your codebase, the routes, the queue tables, the admin screens a support lead actually opens, and plans behavioral end-to-end test cases against what the application really does, including generating the database state each scenario needs before it runs. The Execution Agent drives the UI in an isolated PreviewKit environment, Autonoma's managed preview-environments layer, clicking through the actual routing flow instead of reading a transcript about it. The GenerationReviewer classifies what it finds, a real bug, an agent error, or a plan that no longer matches the current app. And the Diffs Agent keeps the whole suite aligned to the codebase on every pull request, adding, deprecating, and maintaining test cases as the code evolves, so these tests don't silently rot the next time someone reworks the queue-routing endpoint.

Put the two side by side on the exact scenario from earlier: the pytest suite from the sections above proves the agent still picks the right tool and phrases the outcome correctly after a model update, averaged across five runs to rule out noise. Autonoma's behavioral layer proves the ticket's status genuinely changed to "routed: billing" in the dashboard the support team is staring at, that the technical queue's count actually dropped, and that a regression introduced next month, someone reworks the queue-routing endpoint and nobody touches the agent's prompt, gets caught even though the trajectory-level score never moves. Neither one substitutes for the other. A response-level score and a behavioral check on the running app are answering two different questions, and the 93-to-71 drop this piece opened with is a response-level problem. The application-state problem is just as real, and it's the one a trajectory diff will never see.

## Wiring the Threshold Gate Into CI

The pytest suite above is only useful if something actually runs it and someone actually finds out when it fails. That's a CI job, and the trigger for that job is the part that looks different from every other regression gate on the team, because there's no deploy or merge to hook it to. The model can change underneath you on a Tuesday afternoon with no pull request attached.

> **Diagram:** The baseline-comparison gate. A fresh run is run N times, scores are averaged and compared with a golden baseline, then the pipeline passes or fails.

*One averaged number, one threshold, one gate. No individual run decides the outcome alone.*

Here's the GitHub Actions workflow: it runs the regression suite, fails the job if the threshold assertion trips, and posts an alert on failure so drift surfaces the same day instead of sitting quietly in a log nobody opens:

[.github/workflows/agent-regression.yml](https://github.com/Autonoma-Tools/agent-regression-testing/blob/main/.github/workflows/agent-regression.yml)

## Scheduling: Nightly, and On Every Model, Prompt, or KB Change

Since there is no deploy event to hook a regression gate to, the schedule has to do the work a merge trigger normally would. Two triggers cover the failure modes that actually happen. The first is a nightly cron run, which exists purely to catch a silent provider-side model update, the exact failure that opened this piece, where nothing in your own repository changed at all. The second is a path-filtered trigger on anything your team does control: the model or provider config file, the prompt templates, the knowledge-base documents the agent retrieves from. Any of those is a real, deliberate change, and it deserves the same gate a code merge would get.

Skipping either trigger leaves a real gap. Schedule only the path-filtered run, and a silent model swap goes unnoticed until someone notices the support queue backing up, the way ours did. Schedule only the nightly run, and a genuinely bad prompt edit sits in the codebase for up to 24 hours before anyone finds out, instead of failing the same pull request that introduced it. Running both costs a few extra minutes of CI time a day. It's the cheapest insurance in this whole setup.

## Building the Habit: Regression Testing as a Standing Practice

None of this is a one-time setup. A golden trajectory captured today reflects what "good" meant against today's model, today's prompt, and today's knowledge base. Add a new intent the agent needs to route, and it needs its own golden case. Change the prompt in a way that deliberately shifts behavior, and the old baselines need a human to re-check them before they get trusted again, or the suite will flag a deliberate improvement as a regression and nobody will believe the gate the next time it fires for real.

The teams that keep this running treat the golden set the way they'd treat a schema migration: reviewed in a pull request, not edited silently. When someone adds a case or updates a baseline, that's a diff a teammate looks at, the same scrutiny a change to a database migration would get, because a badly captured golden trajectory is worse than no regression suite at all. It teaches everyone to distrust the gate, and a gate nobody trusts is a gate nobody checks before merging.

The pattern in this piece, golden trajectories captured from known-good runs, a structural-plus-similarity scorer, N-run averaging to separate signal from noise, and a nightly-plus-on-change CI gate, is the foundation for testing an agent's decisions. It has a natural neighbor one layer up: [how to test an AI agent](/blog/how-to-test-an-ai-agent) covers the broader test pyramid an agent needs beyond regression alone, and [AI agent reliability testing](/blog/ai-agent-reliability-testing) covers what happens once that agent is live and the questions shift from "did it regress" to "can I trust it in production." Autonoma adds the complementary application-state check: it verifies that a model decision produced the right visible result in the running product, on the isolated PR environment where the change will be reviewed. For running the eval layer this regression suite builds on top of inside your existing pipeline, how to run LLM evals in CI/CD is the next piece in this series.

## Frequently Asked Questions

## Frequently Asked Questions

### What is agent regression testing?

Agent regression testing is the practice of re-running a fixed set of known-good agent trajectories, inputs, tool-call sequences, and outputs captured from prior correct runs, against every new model version, prompt change, or knowledge-base update, and flagging a drop in an aggregated score. Unlike traditional regression testing, it has no deploy event to hook into, since the underlying model can change on the provider's side with no code change on your end.

### Why did my agent's accuracy drop without a deploy?

The most common cause is a silent model update on the provider's side: the same API model name now points at a newer model version, and its behavior shifted even though your prompt, tools, and code are unchanged. Because nothing in your repository changed, a deploy-triggered regression gate never fires. Catching this requires a regression suite that runs on a schedule (nightly) and on any change to model config, prompts, or knowledge-base files, not one wired to a merge or release.

### What is a golden trajectory in AI agent testing?

A golden trajectory is a recorded baseline of one agent run, captured when a human confirmed the result was correct: the input, the full sequence of tool calls with their arguments and results, and the final output text. It's the artifact every future run gets compared against, and it captures the decision path, not just the final answer, which is what breaks first when a model update shifts behavior.

### How do you do regression testing on non-deterministic AI outputs?

Run each golden case multiple times (five is a reasonable starting point), score each run against the baseline using a structural comparison of the tool-call sequence plus a similarity score for the free-text output, average the scores across the N runs, and assert the average stays within a tolerance band of the baseline. A single low-scoring run should not fail the test on its own; only a drop in the averaged score across all runs indicates a real regression rather than run-to-run noise.

### How often should I run agent regression tests if there's no deploy trigger?

Run the full suite on a nightly schedule to catch silent model updates the provider ships without any code change on your end, and also trigger it on any pull request that touches model configuration, prompt templates, or knowledge-base files, since those are deliberate changes your team controls and deserve the same gate a code merge would get. Running only one of the two leaves a real gap: nightly alone misses a bad prompt edit until the next day, and change-triggered alone misses a silent provider-side model swap entirely.

---

This is the markdown variant of <https://getautonoma.com/blog/agent-regression-testing>, served by content negotiation (`Accept: text/markdown`) and also available directly at <https://getautonoma.com/md/blog/agent-regression-testing>.

Other agent surfaces: [llms.txt](https://getautonoma.com/llms.txt), [resource catalog](https://getautonoma.com/.well-known/ai-catalog.json), [developer portal](https://getautonoma.com/developers), [sitemap](https://getautonoma.com/sitemap.xml).
