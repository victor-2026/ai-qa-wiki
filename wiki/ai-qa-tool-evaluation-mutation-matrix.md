---
source: "Hands-on QAEverest.ai pilot + methodology (2026-08-26)"
ingested: "2026-08-26"
type: methodology
---

## Summary
A reusable method for evaluating any AI-QA platform (self-healing, AI test generation, confidence scoring): treat the tool as a product and test it with a mutation matrix, exactly like you would test an app. Applied in the QAEverest.ai pilot (Aug 2026) on `victor-2026/qaeverset-pilot-mini`. The method separates what the tool genuinely adds (human gate, evidence) from what it silently misses (duplicate-target ambiguity).

## Why this exists
AI-QA tools ship claims: self-healing, 99.9% reliability, confidence scores, "no risk" reports. Their output becomes your evidence layer. A tool that reports green on an ambiguous target is worse than one that fails red - a red build forces a decision, a green report does not. You cannot measure trust from a demo; you measure it by breaking the tool on purpose.

## The mutation matrix for tools

| Scenario | Injection | Required tool behavior | QAEverest result (Aug 26) |
|----------|-----------|------------------------|---------------------------|
| Baseline | clean app | green, matches manual expectation | 5/5 green, 0% risk - PASS |
| Locator drift | change id/class, same semantics | heal OR fail loudly, never silently wrong | green - PASS (id-agnostic, intent/text based) |
| Weak decoy | duplicate text on page | ambiguity flagged (confidence drop / suggestion / stop) | green, visual diff 2.20% seen but not classified - FAIL |
| Strong decoy | identical element (same style, type, label) | ambiguity flagged | green, visual diff 3.19% seen but not classified - FAIL |
| Product regression | label/semantics change, locator stable | caught as product issue, not healed silently | passed - text matcher found same string in a heading - FALSE GREEN |

## Worked example: QAEverest pilot

Setup: public repo `victor-2026/qaeverset-pilot-mini`, mini login app on GitHub Pages, 5 Playwright tests, imported via GitHub Actions connection (owner `victor-2026`, repo `qaeverset-pilot-mini`, workflow `ci.yml`, branch `main`, fine-grained PAT).

1. Import: 5/5 cases extracted, avg 100% confidence, mapped 1:1 to source lines. Human gate confirmed - nothing runs until a reviewer accepts cases.
2. Execution model: exact-text first, then vision model. OCR correctly caught a real label mismatch ("Login" vs "Sign in" on the button).
3. Mutations (all applied to the served artifact):
   - M2 locator drift (id `loginBtn` -> `signinBtn`): green. QAEverest resolves by intent/text, id irrelevant.
   - M3 weak decoy (extra "Sign in" text): green, diff 2.20%.
   - M3b strong decoy (second identical sign-in form, same style/type/label): green, diff 3.19%.
   - M5 product regression (button label "Sign in" -> "Log in", locator stable): passed - exact-text matched "Sign in" in the `<h1>` heading instead of the button. Duplicate text = the assertion scope is whole page, not the target element.
4. Exported reports: all three (baseline + both decoys) show 5/5 passed, 0% business risk, Low severity. Visual diff percentages (2.20 / 3.19) are NOT in the PDF - they exist only in the UI. A shareable green report can be indistinguishable from one where the page actually changed.

Deployment gotcha found along the way: GitHub Pages legacy build serves the repo-root `index.html`, not `app/index.html`. Mutations applied to `app/` never reached the stand. Check which artifact your pipeline actually serves before trusting results.

## Verdict pattern
- Genuine value: human gate (review-before-run), per-step evidence (screenshots, video, visual diff), exact-text-then-vision execution, report generation.
- Gap: exact-text matcher scoped to the first occurrence; no duplicate-target ambiguity detection; exported reports omit the visual-diff signal that the UI shows.
- Usage rule: usable as an evidence layer, not as a sole oracle. Pair with an external oracle (mutation testing, golden datasets, human review) for anything ambiguous.

## Playbook for evaluating any AI-QA vendor
1. Build a sanitized suite + static stand (no prod data, no credentials).
2. Run baseline, confirm green matches manual expectation.
3. Inject the mutation matrix (locator drift / weak decoy / strong decoy / product regression) in ascending strength.
4. For each scenario record: green/failed, diff %, ambiguity flag present?, what the exported report says.
5. Red flags: silent green on decoy; healed-without-diff-review; confidence score without published methodology; report omitting the very signal that detected the change.
6. Decide: useful evidence layer / useful maintenance assistant / authoring-only demo value.

## Other findings worth recording
- Environment URL field accepted a literal `URL = https://...` prefix without format error - silent failure at run time.
- Password validator advertised `@$#!%*?&^_+=.` but rejected `_` (only `@` confirmed working).
- `Point to Element -> #loginBtn` did not work; step fix required `Edit Step` to a text matcher.

## Vendor adoption (real signal, Aug 2026)
QAEverest's founder confirmed the mutation-matrix findings and is shipping a **Test Reliability** section in the report: when a locator drifts or a selector weakens, the run will flag it even when the test still passes. Findings will carry new-vs-recurring markers so teams see change, not just state. This is the methodology's core thesis - "works today, fragile tomorrow" - moving from consult to product. The independent mutation matrix is positioned to sit *on top* of that reliability layer as an external oracle. Sample report: `QAEverest_Sample_Execution_Report.pdf` (in Rupesh_Kabra catalog).

### Vendor adoption v2 - the Suite Trust Scorecard (concept, 2026-08-29)
Rupesh sent a **Suite Trust Scorecard — Quality Command Center** concept that productizes the method verbatim:
- **Suite Sensitivity 78% = "14 of 18 seeded mutants caught"** - the mutation matrix as a standing score (2 survived, 2 observed-only). This is the exact M6/M7 technique, now a product metric.
- **Fragility Index 4/31** (position-based selectors) + **"0 weakened selectors open"** - the locator-drift gap is now measured *and* driven to zero.
- **Confirmation Rate 83%** (24 confirmed, 5 dismissed), **Flakiness 2%**, **Coverage Gaps 3** (RTM), **Self-Heals 6/30d** (all reviewed).
- Design principle stated by founder: "every number links to its evidence" and the scorecard is "the artifact an independent evaluation attests to" - the anti-black-box framing from this methodology, adopted wholesale.

Implication: the mutation matrix moved from external audit to built-in product metric. The remaining role for the independent evaluator is **attestation** - verifying the evidence behind each score holds (taxonomy of "survived" vs "observed-only", mutation-score threshold, fragility→fix loop). This is the consulting wedge: originate the method, then attest to the vendor's implementation of it.

### See also
- [QAEverest Pilot Hands-On: Import, Confidence, Human Gate](wiki/qaeverest-pilot-handson-import-confidence-human-gate-2026-08-25.md)
- [DevQAExpert - QAEverest import 2000 Cypress tests - confidence score](wiki/devqaexpert-qaeverestimport2000cypresstests-confidencescore-2026-08-22.md)
- [DevQAExpert - QAEverest maintenance tax - intent resolves at runtime](wiki/devqaexpert-qaeverestmaintenancetax-intentresolvesatruntime-2026-08-22.md)
- [AI QA Evidence Layer: Validation, Evals, Guardrails, and Telemetry](wiki/ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md)
- [Advanced Mutation Testing with Playwright](wiki/Mutation-testing-advanced-playwright.md)
- Статья 20 (quadrant): FP/FN-угол · Статья 24 (accountability): auditability-угол · Статья 26 (skeleton): публикационный формат

---
*Source: hands-on pilot 2026-08-25/26 · tracked in `Private/Positions-CV-CL/outreach/active/Rupesh_Kabra/`*