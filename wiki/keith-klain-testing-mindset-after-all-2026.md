# Apparently We Need a Testing Mindset After All

**Source:** https://qualityremarks.com/apparently-we-need-a-testing-mindset-after-all/ (Keith Klain, Quality Remarks)
**Alias:** https://qualityremarks.com/apparently-we-need-a-testing-mindset-after-all/?utm_source=softwaretestingweekly&utm_medium=email&utm_campaign=issue-325 (same content, UTM alias from Software Testing Weekly #325)
**Date:** August 24, 2026
**Tags:** #testing-mindset #llm-as-judge #critical-distance #AI-testing
**Raw:** [software-testing-weekly-newsletter-2026.md](software-testing-weekly-newsletter-2026.md) (via Software Testing Weekly #325)

---

## What It Is

Keith Klain's rebuttal to the "no testing mindset" myth. For years, critics argued developers can learn testing skills and independent testers are consultants preserving a business model. AI becoming the developer suddenly made everyone worry about who evaluates the work — and research now proves the mindset matters.

## Core Argument

For years: "developers can learn testing skills; creation and critical evaluation don't need different mindsets; dedicated testers not necessary."

Then AI became the developer → question: who evaluates AI-generated work?

Research answers:
- **2024 paper on LLM Evaluators:** LLM evaluators "recognize and favour their own generations" — when same LLM is evaluator and evaluatee, self-preference compromises neutrality.
- **2026 research on preference leakage:** when generator and judge are same model, inherit, or same family, judges systematically biased toward related models — not bad prompting, but relatedness.
- **June 2026 survey of LLM-as-a-Judge:** reliability and bias mitigation are fundamental problems; appointing LLM as judge doesn't make it reliable.

Quote: "I guess having the creator evaluate its own work might introduce blind spots after all."

Credit to Michael Bolton (20 years arguing): problem isn't whether developer *can* test, but whether creator can achieve sufficient **critical distance** from own work.

## New Vocabulary, Old Idea

AI Testing Bros rediscovered skilled testing:
- Critical distance → evaluator independence
- Builder's perspective → generator
- Tester perspective → judge/evaluator
- Mindset → self-evaluation bias

Value of independent testing: someone deliberately occupying a **different epistemic position**, making different assumptions, using different models of risk and purpose. Not a myth — until they find a "Testing Mindset neuron inside Claude," it's the difference.

## Why It Matters Now

- LLM-as-a-Judge, generator/evaluator architectures, judge calibration, multiple evaluators = new "independent testing."
- Confirmation bias: creators seek validation ("does it work"), testers seek failure ("what if it goes wrong").
- Developer testing study (2000+ engineers, 2.5 years, 4 IDEs, 2019): developers overestimate how much they test, misjudge scope.

## Relevance to QA/QE

| Pattern | QA Application |
|---------|----------------|
| Self-preference / preference leakage | Generator and judge must be independent: different models, different teams, or human judge; don't let same agent write code and grade it |
| Critical distance | Human review gate must be epistemically separate from generation — different assumptions, different risk models |
| LLM-as-judge | Useful but requires calibration, multiple evaluators, bias mitigation; not turnkey |

## Critical Analysis

**Strengths:**
- Connects 20-year testing mindset debate to current LLM-as-judge research with citations.
- Concrete research (2024, 2026 papers) not just opinion.

**Gaps:**
- Doesn't prescribe concrete judge-independence architecture (model diversity, human-in-loop).
- Focused on mindset; less on operational guardrails.

## Cross-links

- Related: [Michael Bolton systems thinking](michael-bolton-systems-thinking-constraints-2026.md) (Bottles Have Necks, perturb-the-system)
- Related: [Testing vs Checking (James Bach)](prachi-dahibhate-james-bach-rst-2026.md)
- Related: [AI QA evidence layer](ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md) — evaluator independence as evidence quality
- Newsletter: [Software Testing Weekly #325](software-testing-weekly-newsletter-2026.md)

---


## Practical Checklist (Independence)
- Generator and evaluator must differ: separate model family, separate prompt lineage, or human evaluator.
- Multiple evaluators + calibration before trusting LLM judge.
- Don't let same session write and grade; at minimum fresh context.
- Michael Bolton's 2019 field study reminder: devs overestimate testing — measure, don't assume.


## Link to QA Gate
Pair with evidence layer: verification layer must have epistemic independence — different agent, different model, different data.

Note: Testing mindset ≠ gatekeeping — it's deliberately occupying different epistemic position.

Additional takeaway: independent testing = different assumptions, risk models, purpose — not just different person.

Additional takeaway: independent testing = different assumptions, risk models, purpose — not just different person.

Additional takeaway: independent testing = different assumptions, risk models, purpose — not just different person.

*Ingested: 2026-09-01*
