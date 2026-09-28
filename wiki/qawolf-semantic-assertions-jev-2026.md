# QA Wolf: semantic assertions with Jev (bounded judgment, 2026)

**Source:** QA Wolf blog, "Semantic assertions: Using Jev to make rigid tests flex" (Goran Gajic, 2026-09-25) — https://www.qawolf.com/blog/semantic-assertions-using-jev (fetched ✅ 2026-09-27). Raw: `raw/qawolf-semantic-assertions-jev-2026.md`.
**LinkedIn:** Goran Gajic (Staff Engineering Lead, 2nd) post 3d + comments (Christian DeLaphante counterpoint, Eddie Fisher tagging Dan Holmqvist). Person card: `Positions outreach/active/Goran_Gajic/index.md`.

## The design (two primitives, one rule)

- `ai.expect(...).toSatisfy(...)` — judges whether generated language satisfies a stated requirement (bounded question, no text generation).
- `ai.act(...)` — takes alternate UI routes to a known state (maxSteps + timeout bounds; exact assertions verify the resulting state).
- Governing rule: **permit variation only outside the requirement.** Code owns workflow + requirements; Jev supplies narrow judgments where rigid rules go brittle.

## Honest lines (vendor-stated, quotable)

1. **"Language is not proof of an outcome."** A support assistant can say it referred an issue without creating a ticket — transcript vs receipt in vendor wording. Their fix: Playwright asserts the 201 + saved ticket; Jev only judges the reply wording.
2. **Self-healing caveat, stated by the vendor:** "If onboarding is the behavior under test, the onboarding steps should be explicit. Letting `act` find another route **could hide the defect the test is supposed to catch**." This is our M2/M6 argument from the other side — flexible routing masks defects when the route IS the requirement.
3. **Fail-closed evaluator:** "Uncertain judgments and evaluator errors fail the assertion." Uncertainty → fail, not pass. The correct default, stated explicitly.
4. **Scope honesty:** "Jev's typed output prevents it from returning an answer outside the expected shape. That does not make every judgment correct." Plus the prescription: specific requirements, relevant context, **validate with positive and negative examples**.

## The gap (our standard question, unanswered in the article)

Method disclosed, evidence absent: no measured false-PASS rate, no seeded-break validation of `toSatisfy`/`act`. The article prescribes positive+negative validation but publishes no numbers. Same class as Atmaram's post (better disclosure than most vendors, still vendor-side). The mirror experiment writes itself: seed a wrong-ticket / wrong-queue / misleading-reply break and check whether the bounded judgment catches it — that's our M2/M6 set shape applied to their primitives.

## Counterpoint (thread, paste-only ⚠️)

Christian DeLaphante (C# Test Automation Architect): "If your UI is changing so much for automation then it's also a bad user experience for humans." Practitioner counter-thesis — when locators/routes break constantly, the defect may be the product's stability, not the tests' rigidity. Worth keeping next to every self-healing claim.

## Cross-links

- [[filip-hric-playwright-cli-jev-vs-mcp-2026]] — same lane (Jev + Playwright), different vendor angle.
- [[llm-testing-6-approaches]] — LLM-as-judge approach; `toSatisfy` is a judge with a bounded question + fail-closed default.
- [[testrigor-blog-catalog-all-publications-2026]] + QAEverest drift rows — the self-healing comparison set (their "fewer dumb breaks" vs our seeded-break measurement).
- Quotes banked: Articles/quotes.md → Independence/Attestation (language-not-proof), Market Signals (act-hides-defect, uncertain-fail).
