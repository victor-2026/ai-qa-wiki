# MoT Moment — What AI-Generated Tests Keep Getting Wrong (2026-09-22)

**Author:** Lucio Daza (Product Marketing, Testkube; with Testkube team; CTO Ole Lensmar)
**Source:** https://www.ministryoftesting.com/moments/what-ai-generated-tests-keep-getting-wrong-and-what-finally-fixed-it-for-us
**Context:** MoT Moment. Full disclosure: author works at Testkube, launched test-creation feature that day. Launches on Testkube: generate test in plain language → framework of choice → runs in your own infra → delivered as PR. Digest 23.09 candidate.

---
The pattern: team asks an AI assistant for a test. Output looks great — proper structure, sensible assertions, right framework idioms. Quick review, merged, green. Weeks later something breaks in the exact area the test covered; someone opens it and discovers it was **asserting against its own mocks the whole time**. It never touched the real system; was never going to catch anything.

Why it keeps happening: a test is not general-purpose code. A test is a list of very specific claims about one particular system: this service name, this endpoint, this payload shape, this environment. General knowledge writes decent application code. It cannot write your tests, because almost nothing in your tests is general.

When a model doesn't know your system, it fills gaps with plausible guesses. A plausible guess in a test is worse than an obvious mistake, because **it survives review**. Two failure modes:
1. The test breaks for reasons that have nothing to do with the app → someone burns an afternoon fixing generated code.
2. The test passes forever, quietly, meaning nothing.

What changed the author's mind: not a better model — **moving the verification step**. If a generated test runs against a real environment immediately, while still a draft, before anyone accepts it, then the guesses stop being dangerous. They get caught in seconds instead of in production. The test earns its way into the suite by actually running, not by looking right.

Principle holds regardless of tools: **never accept a generated test that hasn't run against something real. Treat "it looks correct" as no information at all.**

Testkube launch: describe any test in plain language → generates in your framework (Selenium, Playwright, etc.) → runs in your own infrastructure right away → delivers as PR to your repo. Any test type, including load and infrastructure tests most generation tools ignore.

QA relevance: aligns with verification-first/mutation-matrix thinking — generated checks must be validated against real (unmocked) system; "looks right" ≠ evidence. Session Oct 8 (Lensmar + Daza) announced.