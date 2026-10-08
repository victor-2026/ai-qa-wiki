# AQEF: Seeded Controls Spec v0.31.1 (Igor Akymenko, Credit to Victor, Oct 2026)

**Source:** repo https://github.com/igorakymenko-create/AQEF (open spec, CC BY, draft, one author, no consensus claimed), release v0.31.1 (Oct 6, commit a7fc96b). Volumes fetched raw 08.10 (README/index/contributors/judge/contracts/test-design). Launch post (owner-paste 08.10): 5 rules; rules 4-5 from LinkedIn community with credit to Roman Hurakov and Victor Ematin.
**Track:** Igor Akymenko = W1 (FlowScout/Seeded Controls v0.3). W1 relayed.

## Credit (contributors file, verbatim)

- Roman Hurakov (v0.27): faithfulness Judge scoring high on a response with a wrong load-bearing figure → clause-level weighting + aggregate declaration; per-check failure-cost statement makes scores actionable.
- Victor Ematin (v0.28): "evaluation tooling can stay green and silent on a known, deliberately planted defect motivated testing the Oracle itself, not only the system under test" → Seeded Controls (Volume VIII).

## 5 rules (launch post)

1. Write down acceptable BEFORE running anything. 2. Cheap deterministic checks first, LLM judges second. 3. Verdict ≠ judge's confidence (kept apart). 4. Score over 12 claims = average, not verdict (Roman). 5. Test the judge: plant known defect; miss = distrust verdicts of that class (Victor).

## Seeded Controls mechanics (Vol VIII, normative language)

- Definition: scenario with deliberately planted known defect; purpose = prove the Oracle can still detect that class IN THIS RUN (fault seeding applied to the instrument, not the product).
- Miss semantics: missed control = Oracle defect; all same-class Results of that Oracle in the run MUST take `inconclusive` (not `actionable`); no silent spillover outside the class; full-run invalidation allowed only as deliberate recorded decision.
- Seeded results MUST be excluded from Aggregation.
- Practice: ≥1 control per gate-feeding Oracle, run before other assessments, multiple per class with ROTATION ("A single fixed decoy invites tuning around it, especially by whoever adjusts a Judge's criteria while able to see it"); authorship/rotation independent from Oracle tuners (Vol XII roles); applies to Validators too.
- Victor's bus comment is in-spec on two points: train halts on reviewer miss; static seeds get routed around ("single fixed decoy invites tuning around it"). Ours = pre-seeded sets, rotated per test case, never reused across runs. (Correction 08.10: eval-time generation is Chris's practice, not ours — misattribution fixed.)

## Judge discipline (Vol VI, adjacent)

- awaiting_review: verdict + confidence ABSENT (not placeholder); review_timeout required; default = blocking (unanswered review never silently passes — same posture as unresolved/unverifiable).
- Human reviewer never subject to calibration/drift tracking (human = ground truth, not reverse).

## QA interpretation

- First external spec to codify our seeded-break doctrine with normative force (MUST inconclusive, exclusion from aggregation, rotation) + public credit. Direct backup for Articles 26/29 and per-risk-tier gate language.
- Roman's clause (per-check failure cost) + our oracle-miss rule compose: cost-aware inconclusive verdicts.
- Watch: spec velocity (0.25 Aug → 0.31.1 Oct 6); Volume VIII vs W1's "Seeded Controls v0.3" naming — confirm same artifact lineage with W1.

## See also

- [[typesafe-jev-judgment-service-gates-2026]] — abstention, unresolved marking
- [[breaklight-ai-testing-methodology-whitepaper-2026]] — exclusion rules, verdict discipline
- [[igor-goldshmidt-trajectory-response-2026]] — oracle failure (different Igor, keep apart: Akymenko = spec/FlowScout, Goldshmidt = trajectory posts)
