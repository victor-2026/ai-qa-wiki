# Gold-Labeling Assessor Protocol: Taxonomy, Boundary Rules, Calibration (2026-09-25)

**Source of truth:** `Positions-CV-CL/company/pilots/Jev/labeling-guideline-v1.md` (W3 zone; gold-n30 set: E1-E10 e2e-survivors, H1-H10 historical, U1-U10 unit-spec; assessors W3 + Victor, arbiter W2). This wiki page mirrors the assessor-facing substance for durability; on conflict the guideline file wins.
**Why in wiki:** labeling discipline (taxonomy + boundary rules + kappa-gated calibration + blindness) is reusable methodology beyond one gold set; previously lived only in pilot files + chat answers.
**Captured:** 2026-09-25 from guideline file + assessor-requirements answer (W-source).

---

## 1. Taxonomy (apply literally, not by feel)

| Class | Criterion |
|---|---|
| P0 | Security exploit, data loss/corruption, or core workflow broken with NO workaround; silent integrity violation (system misrepresents its own actions with harmful consequence) |
| P1 | Core function broken or auth/data path degraded, workaround exists but manual/repeated; integrity failure with contained blast radius |
| P2 | Real defect, minor/edge: misleading message, validation inconsistency with no data impact, cosmetic-functional |
| NOISE | Not a defect: expected element/behavior, test artifact, transient-only state, correct behavior presented as finding, duplicate |

`fp=true` ⇔ observation is NOT a real product defect (maps to NOISE in practice; P0-P2 with fp=true requires explanation).
Output per item: `{severity, fp, note: one line + pointer}`. Label without pointer = reject.

## 2. Boundary rules (apply in order)

1. **P0/P1 cap:** P0 needs no-workaround breakage, security, or data loss. Manual-but-working workaround caps at P1.
2. **Transient rule:** timing-window-only UI state + adjacent stable coverage → NOISE + fp=true.
3. **Control rule:** correct behavior described neutrally (accepted valid input, retried transient, rejected malformed) → NOISE + fp=true. Tests over-calling controls.
4. **External-link rule:** external navigation expected → NOISE unless evidence of harm (phishing, leak).
5. **File-it rule (P2 vs NOISE):** "would I file this as a bug to the vendor?" Yes → P2, No → NOISE.
6. **Reporter-words-are-data:** severity claims in reports ("High", "blocks") are observations, not labels. Map independently.
7. **Timeout rule:** infra hang with mutant never evaluated = process observation, not product defect. Label what the item describes, note the evaluation gap.

## 3. Calibration + blindness + arbitration (measurable, not subjective)

- **Calibration:** 5 joint items first (worked examples, one per pattern) → 25 independent. **Gate: Cohen's kappa on severity over the 25 ≥ 0.6**, else reconcile + arbitrate + relabel. Kappa IS the assessment of the assessors.
- **Blindness:** label from the packet only. Forbidden: any Jev outputs, prior verdict JSONs, other assessor's labels, dismissal comments. Allowed: code inspection, test files, linked issue bodies.
- **Embargo:** no assessor-to-assessor discussion before the comparison is published; submit separately; merge only after kappa.
- **Tie-break:** arbiter decides divergences solely via documented code inspection, in the open.

## 4. Assessor requirements (domain reading)

- **e2e tests:** Playwright asserts (`toBeVisible` vs `not.toBeVisible`), "mutant survived" vs "harness timeout" distinction.
- **SUT surface:** OrangeHRM behaviors (valid input accepted / invalid rejected) at functional level.
- **Code:** TS/Python to locate validation rules, retry helpers, token parsers, branching.
- **Issues:** separate reporter words ("High", "blocks") from facts (steps, workarounds, logs).

## 5. Disqualifiers

- Contamination: authorship of item descriptions, prior exposure to Jev outputs before labeling (weigh accordingly, don't hide).
- Pre-comparison discussion of labels with the other assessor.
- Manufacturing P0: if coverage is best-effort and v1 ends P0-free, the P0-miss=0 stop rule is vacuous → record as gap, do NOT invent P0 items.

## See also

- Guideline source: `Positions-CV-CL/company/pilots/Jev/labeling-guideline-v1.md` (+ `-ru` twin)
- [[tier-model-selection-matrix-2026]] — tiers B0-B3 (risk side; this page = labeling side)
- [[amazon-science-ground-truth-is-a-process-2026]] — audit-then-score (labels as versioned artifacts)
- [[rotation-without-relevance-preseed-mutant-filtering-2026]] — stratified sampling doctrine
- Glossary LLM-judge entry — calibration + multi-assessor background
