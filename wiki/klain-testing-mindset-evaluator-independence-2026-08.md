# Testing Mindset Vindicated: Klain on Evaluator Independence (2026-08)

**Source:** Keith Klain (Technology Leader, AI Assurance) LinkedIn post + https://qualityremarks.com/apparently-we-need-a-testing-mindset-after-all/ (2w ago). 159 reactions, 32 comments.
**Why in wiki:** independent research backbone for our verifier thesis (creator ≠ evaluator), with citable papers. Maps 20 years of testing vocabulary onto AI-eval terms.

## Core argument

"Testing mindset" was dismissed as myth (developers can learn testing skills, no separate mindset needed). Then AI became the developer — and everyone worries who evaluates the work. Research now re-derives independent testing under new names.

## The 3 papers (citable)

1. **Self-preference (2024):** LLM evaluators "recognize and favor their own generations" — https://arxiv.org/abs/2404.13076
2. **Preference leakage (2026):** generators/judges same model, inheriting, or same family → systematic bias toward related models; problem = relatedness, not prompting — https://arxiv.org/abs/2502.01534
3. **LLM-as-a-Judge survey (Jun 2026):** reliability + bias mitigation = fundamental problems; appointing a judge doesn't make judgment reliable — https://www.sciencedirect.com/science/article/pii/S2666675825004564
4. Bach backup: critical distance — https://developsense.com/blog/2025/04/four-frames-for-testing-part-7-critical-distance (Bolton: 20 years same argument)

## Vocabulary mapping (old → new)

critical distance → evaluator independence · builder perspective → generator · tester perspective → judge/evaluator · mindset → self-evaluation bias. Value unchanged: someone deliberately occupying a DIFFERENT epistemic position.

## Comment quotes (use in articles)

- Petr G. (350+ interviews): asking "why might this be wrong" never correlated with coding skill — hardest instinct to hire.
- QA Meditations: two Claude sessions grading each other = same student regrading own exam with different pen. Scales down to n=1.
- Yatender Sharma: creation vs evaluation = complementary, not identical.

## Our mapping

- Direct backbone for: Article 26 red flags (confidence without methodology), verifier thesis (DevAssure/Qase/Tobias choir), Agentiqa hetero-audit question (Model B must be DIFFERENT family — preference leakage is why).
- Klain = peer/content (Following). qualityremarks catalog exists — this post is its sharpest entry.
