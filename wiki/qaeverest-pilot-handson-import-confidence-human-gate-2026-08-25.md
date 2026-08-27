---
source: "Hands-on QAEverest.ai pilot 2026-08-25 (victor-2026/qaeverset-pilot-mini)"
ingested: "2026-08-25"
type: hands-on
---

## Summary
A small, controlled QAEverest.ai pilot on a public GitHub Pages stand (`victor-2026/qaeverset-pilot-mini`): a mini login app plus a 5-test Playwright suite. The run validated the import pipeline, the confidence score, the human review gate and the exact-text vs vision assertion model. It also exposed two practical failure modes: a GitHub Pages subpath navigation issue in plain Playwright CI, and an OCR assertion mismatch between the imported step intent ("Login") and the actual button label ("Sign in").

## Key Concepts

| Concept | Explanation |
|---------|-------------|
| Import-not-run | QAEverest never executes the original Playwright suite. It extracts steps, data and expected results and rebuilds native QAEverest cases. |
| Confidence score | AI estimate of how faithfully an imported case reflects the original (shown in import UI, avg 100% here). Nothing runs until a human accepts cases. |
| Human gate | No automation starts until the reviewer approves (or edits) imported cases. |
| Exact-text then vision | Assertions first match exact on-screen text, then a vision model judges the screenshot. Vision does not fabricate a missing literal. |
| OCR vs semantic label | An imported step "Verify Login button" fails if the real button text differs ("Sign in"), because exact-text runs before vision. |

## Hands-on Findings

**Import pipeline (validated)**
- GitHub Actions connection: owner `victor-2026`, repo `qaeverset-pilot-mini`, workflow `ci.yml`, branch `main`, fine-grained PAT (Contents/Actions/Metadata read).
- Result: `1/1 files extracted · 5/5 accepted · 0 low confidence (<60%) · 0 unresolved helpers · avg 100%`.
- Each of the 5 cases mapped 1:1 to `tests/login.spec.ts` lines with P1-P3 priorities and type tags (positive/negative/security/ui).

**Failure mode 1 - GitHub Pages subpath (CI)**
- `page.goto('/')` with `baseURL https://victor-2026.github.io/qaeverset-pilot-mini/` resolved to the Pages repo root, not the app subpath. Locators were never found.
- Fix: `page.goto('/qaeverset-pilot-mini/')` and `baseURL https://victor-2026.github.io`.

**Failure mode 2 - OCR exact-text vs real label (QAEverest runner)**
- Imported intent: "Verify the Login button is visible". Actual button: `<button id="loginBtn">Sign in</button>`.
- Runner failed the exact-text check and vision correctly reported: the visible button is labeled "Sign in", not "Login".
- Fix: Edit Step to assert `#loginBtn` or the text "Sign in" (or Point to Element).

**Result**
- 4/5 passed natively; 1 case needed a step-text fix. Run: 2026-08-25 23:42, UAT-1 env, Chromium, 07.6s.
- `Report a Bug → File to Jira / ClickUp` is available from failure results.

## Practical Applications

1. **Brownfield migration** - bring legacy Playwright/Cypress suites into an AI workflow without rewriting: import, review confidence, run natively.
2. **Assertion authoring discipline** - exact-text-before-vision means test intent and UI copy must match; rename refactors surface as reviewable failures, not silent passes.
3. **CI vs hosted stand** - when moving a suite to GitHub Actions, subpath navigation (`/repo/`) is the first thing to verify, before touching assertions.
4. **Evidence per step** - screenshots per step and last-good/failure frames give the human reviewer a concrete audit trail for every decision.

## Limitations Observed

- Locator history not exposed (new locator overwrites old, per vendor).
- Self-healing (locator drift, decoy targets, step changes) was not exercised in this static pilot - only the import + assertion path.
- Confidence is a vendor score without published methodology.

### See also
- [DevQAExpert - QAEverest import 2000 Cypress tests - confidence score](wiki/devqaexpert-qaeverestimport2000cypresstests-confidencescore-2026-08-22.md)
- [DevQAExpert - QAEverest maintenance tax - intent resolves at runtime](wiki/devqaexpert-qaeverestmaintenancetax-intentresolvesatruntime-2026-08-22.md)
- [AI QA Evidence Layer: Validation, Evals, Guardrails, and Telemetry](wiki/ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md)

---
*Source: hands-on pilot 2026-08-25 · `victor-2026/qaeverset-pilot-mini` · tracked in `Private/Positions-CV-CL/outreach/active/Rupesh_Kabra/`*