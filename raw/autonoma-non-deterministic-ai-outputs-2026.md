# Source: https://getautonoma.com/blog/how-to-test-non-deterministic-ai-outputs

---
title: "How to Test Non-Deterministic AI Outputs"
description: "How to test non-deterministic AI outputs: invariant assertions, semantic similarity, n-run sampling, and threshold gating, all runnable."
date: "2026-07-27"
canonical: "https://getautonoma.com/blog/how-to-test-non-deterministic-ai-outputs"
authors:
  - "Tom Piaggio"
tags:
  - "Testing"
  - "AI"
  - "LLM Testing"
---

# How to Test Non-Deterministic AI Outputs

> **How to test non-deterministic AI outputs**: assert what must be true about the output instead of asserting what the output is, and measure a pass rate across several runs instead of trusting a single one. In practice that means four things: invariant and property-based assertions on structure and required content, semantic-similarity comparisons instead of string equality, n-run sampling that reports a pass rate rather than a verdict, and a suite-level threshold gate set from a measured baseline. A flaky AI test almost always means one of two things: the assertion is too strict, or the prompt is too ambiguous.

> A runnable pytest project for testing non-deterministic AI outputs: a stub model client, property-based invariant assertions, a semantic-similarity helper with a calibrated threshold, an n-run self-consistency sampler, and a suite-level threshold gate. [Source on GitHub](https://github.com/Autonoma-Tools/how-to-test-non-deterministic-ai-outputs).

Your CI run goes red. You rerun the job. It goes green. You ship. Two days later the exact same test fails on the exact same input, and this time nobody reruns it, because it's 4pm on a Friday and the failure looks like every other flaky test that's ever cried wolf in that pipeline.

That flake didn't come from a network blip or a race condition in your test runner. It came from the model. Somewhere in your suite, an assertion expects the exact string a language model returned the last time this test happened to run, and the fix everyone reaches for first, retrying until it goes green, is exactly backwards. Retrying a network timeout recovers a false negative. Retrying a non-deterministic AI test just hides the one signal you actually have: that the same input can produce a different, and sometimes wrong, output.

## Why Does My Chatbot Give Different Answers to the Same Question?

Ask a language model the same question twice and you'll often get two different, both defensible, answers. Four things cause that, and only one of them lives in a prompt file you control.

Sampling temperature and top-p are the obvious ones: the model doesn't always pick the single highest-probability next token, it samples from a distribution, so a higher temperature means more wording variation from one call to the next. Context and retrieval drift is the second, and it's the one teams miss most often: if your feature pulls in a RAG chunk, a tool result, or recent conversation history, and that upstream data shifted even slightly between two calls, the model is answering a subtly different question each time even though the user typed identical words. Prompt phrasing is the third: a system prompt edited last sprint, one extra sentence a teammate added "for clarity," and the model's behavior shifts in ways nobody flagged as a change. The fourth sits entirely outside your codebase: providers update the underlying model silently, behind the same model name and the same API contract, so your exact prompt now hits a different set of weights than it did last week, with no diff for you to review.

| Cause | What changes between calls | In your codebase? |
| --- | --- | --- |
| Temperature and top-p | Sampling distribution | Yes |
| Context and retrieval drift | Upstream RAG or tool data | Yes |
| Prompt phrasing changes | Wording of instructions | Yes |
| Provider model updates | Weights behind the API | No |
| Even at temperature=0 | Batching, GPU, MoE routing | No |

Here's the correction that trips up almost everyone building on this stack: `temperature=0` is not determinism.

> Temperature=0 reduces variance. It does not eliminate it. Batching, floating-point non-associativity, GPU kernel behavior, and mixture-of-experts routing all still move the output, and none of them show up in your prompt.

Batched inference means your request shares a hardware batch with other requests in flight, and floating-point operations aren't strictly associative, so the same input can produce different logits depending on what else happens to be in that batch. GPU kernels introduce their own non-determinism at the level of floating-point precision. Mixture-of-experts models route tokens to different experts based on load, and that routing can vary run to run even when temperature is pinned at zero. This [detailed teardown of batch invariance in LLM inference](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/) covers exactly why batch composition and floating-point non-associativity move outputs even when nothing about your request changed. And a silent provider-side model update changes output at temperature zero exactly as easily as it changes output at temperature 0.7. If your entire test strategy rests on `temperature=0` producing a fixed string, it will pass in your local run and flake in production the first time any one of those four things moves, and you won't have a stack trace that tells you which one.

## Testing Non-Deterministic Software: The Assertion Has to Change Shape

Deterministic software testing runs on an assumption so basic it's invisible: same input, same output, every time. You assert equality and move on with your day. Non-deterministic AI output breaks that assumption at the root, which means the fix isn't a looser number in the same kind of assertion, it's a different kind of assertion entirely.

The shift is this: instead of asserting that an output IS a particular value, you assert what must be TRUE about it. And instead of trusting a single run to represent the system, you trust a rate measured across several.

| What you assert | Deterministic software | Non-deterministic AI output |
| --- | --- | --- |
| Output equality | Exact match, every run | Rarely holds twice |
| Structure and schema | Often implicit | Must be asserted explicitly |
| A single failing run | Confirms a real bug | Could be noise or signal |
| What a retry tells you | Infra flake, not the code | Hides the real variance |
| What "passing" means | Binary pass or fail | Pass rate above a floor |

Every pattern below is one way of putting that shift into code. None of them require you to give up on assertions, or to accept that "AI is just fuzzy." They require you to assert the right thing.

> **Assert the outcome, not the wording.** Autonoma runs agentic end-to-end tests on every pull request. [Try Autonoma](https://autonoma.app).

## Pattern One: Property-Based and Invariant Assertions

The most reliable fix for a flaky exact-match assertion is usually to stop asserting an exact match. Instead, assert the properties that must hold no matter which acceptable phrasing the model lands on this run: the response is well-formed and non-empty, it's under a length bound, it contains the entities the answer actually depends on (an order ID, a confirmation number, a status the user asked about), and it does not contain content you've explicitly forbidden (a leaked system prompt, an unqualified promise the business can't back).

This is deliberately the cheapest pattern in this article to write and the first one you should reach for. It needs no embeddings, no second model call, and no judge. If your response fails a structural invariant, you have a real bug, and chasing it into a semantic-similarity check first only adds latency to finding what's already broken.

Here's a pytest module asserting structural invariants against a stub model client, including the case where `temperature=0` still has to hold across many draws, not just one:

[tests/test_invariants.py](https://github.com/Autonoma-Tools/how-to-test-non-deterministic-ai-outputs/blob/main/tests/test_invariants.py)

Notice what these assertions do not check: whether the wording is good, or whether the words match some reference answer. That's on purpose. Invariants are the floor every acceptable response has to clear, not the full definition of a correct one.

> **Diagram:** Exact match fails, semantic similarity passes.

*The same three responses fail an exact-match assertion two out of three times and pass a semantic-similarity assertion three out of three times. Only one of those assertions is telling you something true about the answer.*

## Pattern Two: Semantic Similarity Instead of Exact Match

Once your invariants pass, the remaining question is usually whether the free-text response means the right thing, not whether it's spelled the right way. Exact-match assertions can't answer that, because the same correct answer has effectively infinite valid phrasings. The standard fix is to embed both the response and a reference answer, compute cosine similarity between the two vectors, and assert the similarity clears a threshold.

The threshold is the part teams get wrong. Picking `0.8` because it sounds reasonable is a guess, not a measurement. The right way to set it: gather a sample of response pairs, label each pair "same meaning" or "different meaning" by hand, embed all of them, and pick the cutoff that separates your two labeled groups with the fewest misclassifications. That threshold is specific to your domain: a cutoff tuned on refund-status replies will not transfer cleanly to a domain where subtle wording differences change the actual claim being made, like medical or financial guidance.

Similarity also has a ceiling. It tells you two strings are close in meaning, not that either one is factually correct, or that a multi-step claim actually holds up. When correctness depends on more than paraphrase-level meaning, an LLM-as-judge scored against an explicit rubric is the right tool, not a tighter similarity threshold; that judge-based approach is exactly what our guide to [prompt-level unit testing](/blog/llm-unit-testing) covers in depth.

Here's a semantic-similarity helper with the threshold calibration documented directly in the code:

[lib/semantic_similarity.py](https://github.com/Autonoma-Tools/how-to-test-non-deterministic-ai-outputs/blob/main/lib/semantic_similarity.py)

Passing a similarity check only tells you the words are equivalent, not that the right thing happened inside your application, which is exactly the gap behavioral end-to-end testing closes: [Autonoma](https://getautonoma.com) checks what an AI feature actually caused in a running app (the right screen, the right record, the right side effect) instead of the exact words it produced, so wording-level variance never enters into it.

## How Autonoma Tests the Outcome Around a Non-Deterministic Response

Autonoma handles the product layer that a semantic score cannot see. Its Planner reads the routes, components, and flows in your codebase to plan behavioral tests for the running app, and its Executor drives the UI against a live preview environment to verify the state the response caused: the ticket moved, the refund amount changed, or the correct screen rendered. That keeps the assertion focused on a deterministic product outcome even when the model can phrase the response many valid ways. Diffs Agent then updates the affected coverage from the code diff, so a UI or flow change does not leave that behavioral check behind.

## Pattern Three: N-Run Sampling and Self-Consistency

Testing the consistency of LLM outputs starts with accepting that a single run is never enough evidence for a non-deterministic system, no matter which assertion you're using. The fix is to run the same input multiple times, score each run independently, and report a pass rate instead of a verdict. This generalizes the [self-consistency method introduced by Wang et al.](https://arxiv.org/abs/2203.11171), from raising model accuracy to measuring test reliability. Two ways to turn that rate into a boolean: majority vote, where you require some fraction of runs (5 runs with 4 passing is a common default) rather than unanimity, and mean-similarity, where you average the similarity score across every run and threshold the mean instead of thresholding each run in isolation.

Choosing how many runs to sample is a cost tradeoff, not a purity contest. Five runs catches a scenario that fails more than roughly one time in five without paying for twenty-plus model calls on every assertion in your suite. Raise the count for scenarios you've watched flip near the majority line; a scenario that's a clean 5-of-5 or 0-of-5 rarely needs a bigger sample to trust.

Here's a sampling runner that executes the same input N times and reports both a majority-vote verdict and a mean-similarity verdict, instead of collapsing five distinct outcomes into one line:

[lib/sampling.py](https://github.com/Autonoma-Tools/how-to-test-non-deterministic-ai-outputs/blob/main/lib/sampling.py)

The spread itself is the signal worth watching over time, not just the final pass or fail. A scenario that holds at 5-of-5 for three weeks and then drops to 3-of-5 overnight just told you something real changed upstream, a prompt edit, a model version bump, a newly ambiguous tool description, that a single run would have completely hidden.

> **Diagram:** The n-run sampling gate.

*Five independent runs, four passes, an 80% rate against a 75% floor. The gate reads the rate, not any single run.*

## Pattern Four: Threshold Gating at the Suite Level

Everything above produces a pass rate per scenario. Threshold gating is the last step: rolling those per-scenario rates up into a single suite-level gate with a floor, so a CI run has one clear answer instead of a wall of individual pass rates nobody reads.

The floor itself has to come from somewhere real. Run the suite repeatedly against a version of the system you already trust, look at the noise floor that shows up even when nothing is broken, and set your gate a few points below that measured baseline, not at a round number that looks tidy on a dashboard. A gate set at 95% when your trusted baseline naturally sits at 88% will fail on every run, trusted or not, and a team that lives with a permanently red gate stops looking at it within a month.

Here's a compact gate that rolls per-scenario pass rates into a suite-level pass or fail and returns a process exit code CI can act on:

[lib/threshold_gate.py](https://github.com/Autonoma-Tools/how-to-test-non-deterministic-ai-outputs/blob/main/lib/threshold_gate.py)

Wiring this specific gate into a scheduled or per-PR CI run, alongside the model calls that produce the pass rates in the first place, is its own topic with real cost and latency tradeoffs; our guide to [running LLM evals in CI/CD](/blog/how-to-run-llm-evals-in-ci-cd) covers that pipeline end to end.

## The Practitioner Rule: Too Strict or Too Ambiguous

Here's the rule that resolves almost every "flaky AI test" ticket, stated plainly enough to paste into a Slack thread:

> A flaky AI test means your assertion is too strict, or your prompt is too ambiguous. It is almost never a third thing.

Telling those two apart doesn't require guessing. Run the exact same input against the exact same prompt ten to twenty times and look at the spread of outputs directly, not just at the pass or fail column.

If the outputs agree in meaning but differ in wording (the refund amount is right, the tone is right, only the phrasing changes), your assertion is too strict. You're still checking for a specific string, or a similarity threshold set too high for the amount of legitimate paraphrasing your feature actually produces. The fix lives in the assertion: move from exact match to an invariant or a semantic-similarity check, or loosen the threshold to a number you've actually calibrated against labeled examples instead of guessed at.

If the outputs disagree in meaning or structure (one run confirms the refund, another asks a clarifying question, a third states the wrong amount), your prompt is too ambiguous. No assertion change fixes that, because the model is correctly reflecting an underinstructed prompt back at you in different valid ways. The fix lives upstream: add the missing constraint, specify the output format explicitly, or split an overloaded prompt into two narrower ones. Tightening the assertion around an ambiguous prompt just teaches your suite to accept whichever behavior happened to show up in your sample.

> **Diagram:** Too strict or too ambiguous.

*The spread across repeated runs is what tells the two diagnoses apart, and each one has a fix that lives in a different place. Tightening an assertion around an ambiguous prompt fixes neither.*

Traditional flaky-test advice (retry it, quarantine it, mark it skip) actively misleads here, because that advice assumes the variance is infrastructure noise sitting on top of a stable, correct system. With AI output, the variance often is the system telling you something true: that the assertion doesn't match what "correct" actually looks like, or that the prompt hasn't pinned down what correct means in the first place. Quarantining that test doesn't remove noise. It removes your only warning.

## Where to Go From Here

If you take one thing from this article, take the rule: strict assertion or ambiguous prompt, and the ten-to-twenty-run spread that tells you which one you're looking at. Everything else here, invariants, semantic similarity, sampling, threshold gates, is the tooling that rule needs to actually run in a suite instead of living as a mental checklist.

A reasonable order to build this in: start with invariant assertions on your highest-traffic scenarios, since they're the cheapest and catch the most obvious breakage. Add semantic-similarity checks once you have reference answers worth comparing against. Wrap flaky-by-nature scenarios in n-run sampling before you spend more time debugging a single red run that might not mean anything. Roll everything into a threshold-gated suite once you have enough scenarios that a wall of individual pass rates stops being readable.

None of these four patterns tell you whether the feature actually did the right thing inside your product, only whether its words held up. That's a different, narrower question than whether the right screen loaded, the right record got written, or the right side effect actually fired, which is the layer [Autonoma](https://getautonoma.com) runs against on every preview environment your team ships. This piece is a deep dive under our broader guide to [testing generative AI applications](/blog/testing-generative-ai-applications), and if the AI feature you're testing is specifically a conversational one, [how to test a chatbot](/blog/how-to-test-a-chatbot) covers the surrounding checklist this article's patterns plug into.

## Frequently Asked Questions

## Frequently Asked Questions

### How do you test non-deterministic AI outputs?

Replace exact-match assertions with checks that hold across every acceptable answer: invariant and property-based assertions on structure and required content, semantic-similarity comparisons instead of string equality, n-run sampling that measures a pass rate instead of trusting a single run, and a suite-level threshold gate set from a measured baseline rather than a guessed number.

### Why does my chatbot give different answers to the same question?

Four things cause it: sampling temperature and top-p, context or retrieval drift (a RAG chunk or tool result changed between calls), prompt phrasing changes, and silent provider-side model updates. Temperature=0 reduces this variance but does not eliminate it, because batching, GPU non-determinism, and mixture-of-experts routing can still change the output.

### Is temperature=0 deterministic?

No. Temperature=0 reduces output variance but does not guarantee an identical response every time. Batched inference, floating-point non-associativity, GPU kernel behavior, and mixture-of-experts routing can all still shift the output, and a silent model update from the provider can change results at temperature=0 exactly as easily as at any other temperature.

### What does it mean when an AI test is flaky?

A flaky AI test almost always means one of two things: the assertion is too strict (checking for exact wording when the meaning is what matters), or the prompt is too ambiguous (underinstructed enough that multiple different responses are all valid). Run the same input 10-20 times and look at the spread: if outputs agree in meaning but differ in wording, loosen the assertion; if they disagree in meaning, fix the prompt.

### How do you test the consistency of LLM outputs?

Run the same input multiple times (5-20 runs depending on cost tolerance) and measure a pass rate instead of trusting a single run. Score consistency with semantic similarity or an invariant check rather than exact match, and gate on a majority-vote or mean-similarity threshold calibrated from a labeled sample, not a guessed cutoff.

### Should you retry a failing AI test?

No, and this is the single most common mistake teams make. Retrying a network timeout recovers a false negative, because the underlying system was fine and the failure was infrastructure noise. Retrying a non-deterministic AI test hides your only signal, because the variance you just retried away might be the model behaving differently on a prompt that's still ambiguous or an assertion that's still too strict. Run the input 10-20 times deliberately instead, and gate on a measured pass rate rather than chasing a single green run.

### What similarity threshold should you use for LLM output testing?

Don't pick a number like 0.8 because it sounds reasonable, that's a guess, not a measurement. Gather a sample of response pairs, label each one by hand as 'same meaning' or 'different meaning', embed all of them, and choose the cutoff that separates your two labeled groups with the fewest misclassifications. Thresholds are domain-specific: a cutoff calibrated on customer-support replies won't transfer cleanly to a domain like medical or financial guidance, where subtle wording differences change the actual claim being made.

### How many times should you run an AI test?

Five runs is a reasonable default: it catches a scenario that fails more than roughly one time in five without paying for twenty-plus model calls per assertion. Raise the count for scenarios you've watched flip near the majority line, where the extra signal is worth the extra cost. A scenario that comes back a clean 5-of-5 or 0-of-5 rarely needs a bigger sample, since the result is already unambiguous.

---

This is the markdown variant of <https://getautonoma.com/blog/how-to-test-non-deterministic-ai-outputs>, served by content negotiation (`Accept: text/markdown`) and also available directly at <https://getautonoma.com/md/blog/how-to-test-non-deterministic-ai-outputs>.

Other agent surfaces: [llms.txt](https://getautonoma.com/llms.txt), [resource catalog](https://getautonoma.com/.well-known/ai-catalog.json), [developer portal](https://getautonoma.com/developers), [sitemap](https://getautonoma.com/sitemap.xml).
