# Apparently We Need a Testing Mindset After All — Keith Klain (2026)

**Source:** LinkedIn — Keith Klain, Technology Leader | AI Assurance, Quality Engineering and Operational Risk — 1d • Edited
**Canonical:** https://qualityremarks.com/apparently-we-need-a-testing-mindset-after-all/ (24.08.2026, with links to papers and image)
**RSS:** https://qualityremarks.com/feed/
**Title:** Apparently We Need a Testing Mindset After All
**Hashtags:** #testing
**Capture date:** 2026-08-25

## Full excerpt (as posted)

For years, those of us who view #testing as skilled knowledge work were told there's no such thing as a "testing mindset." We've also endured criticism that independent testing is just self-interested consultants preserving a business model.

Their argument was simple: developers can learn testing skills. Creation and critical evaluation don't require fundamentally different mindsets. Anything other than that was a "myth" designed to create silos and stop knowledge from being distributed across teams and in fact, dedicated testing specialists might not be necessary at all.

Then AI became the developer and suddenly, everyone is worried about who evaluates the work.

And the research is explaining why LLM-as-a-Judge, generator/evaluator architectures, judge calibration and using multiple evaluators is the new "independent testing".

A 2024 paper on LLM Evaluators found that LLM evaluators can "recognize and favor their own generations". When the same LLM acts as both evaluator and evaluatee, self-preference can compromise what appears to be neutral evaluation.

And research published in 2026 described "preference leakage" when generators and judges are the same model, inherit from one another, or belong to the same model family. They found judges systematically biased toward related models and the problem wasn't bad prompting, but relatedness between creator and evaluator.

And to top it all off, a June 2026 survey of LLM-as-a-Judge identifies reliability and bias mitigation as fundamental problems in constructing trustworthy evaluation systems. Simply appointing an LLM as judge doesn't make its judgment reliable.

I guess having the creator evaluate its own work might introduce blind spots after all.

It might sound petty (I don't really care), but I can't help remembering at the time this mythology nonsense was being pushed that James Bach disputed the straw man directly when it was published. Years later, AI researchers may not be using his terminology, but they are describing the same problem.

And credit where credit is due, my friend Michael Bolton has been making a similar argument for nearly twenty years: the problem isn't whether a developer can test, it's whether a creator can achieve sufficient critical distance from their own work.

But as with all things in the era of Testing with #AI, everything old has become new again as we watch the AI Testing Bros discover skilled testing. "Critical distance" has become "evaluator independence". "Builders perspective" has become "generator". "Tester perspective" has become "judge/evaluator". "Mindset" has become "self-evaluation bias", and on and on it goes.

But until they find a Testing Mindset neuron inside Claude, the value of independent testing has always been the same: someone deliberately occupying a different epistemic position, making different assumptions, and using different models of risk and purpose.

And that's not a myth.

## Key claims to preserve for wiki

- Historical debate: "testing mindset" dismissed as myth to justify distributing testing skills to developers and questioning need for dedicated testers.
- Shift with AI: same organizations now worry about who evaluates AI-generated work.
- Research mapping:
  - 2024 paper: LLM evaluators recognize and favor own generations (self-preference, self-bias)
  - 2026 paper: preference leakage when generator and judge are same / related model family — not prompt issue but relatedness bias
  - June 2026 survey: reliability and bias mitigation are fundamental problems for LLM-as-a-Judge; appointing a judge does not guarantee reliability
- Lineage: James Bach disputed straw man early; Michael Bolton — nearly 20 years arguing creator vs critical distance.
- Translation to AI terms: critical distance → evaluator independence, builder perspective → generator, tester perspective → judge/evaluator, mindset → self-evaluation bias.
- Core value: independent testing = different epistemic position, different assumptions, different risk/purpose models — not a myth.

## Why save this for this wiki
- Directly supports: LLM-as-a-Judge, generator/evaluator architectures, judge calibration, multi-evaluator, independence, anti-overfit, QAEverest/Rupesh two-gate discussion, StatusNeo AI QA strategy (human gate)
- Bridges classic testing theory (Bach/Bolton critical distance) and current AI evaluation research (self-preference, preference leakage)
- Complements: Testing AI book (judges, disagreement, evals), Goodhart's Law, evidence layer, AI QA transformation
- Captures terminology shift useful for interviews: explain why AI makes independent testing more, not less, important

## Capture note
Saved as fair excerpt for wiki ingestion. Full post is public LinkedIn. Do not republish as own content without attribution.
