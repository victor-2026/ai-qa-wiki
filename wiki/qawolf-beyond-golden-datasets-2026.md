# QA Wolf vs golden datasets: the anti-gold thesis, answered (2025)

**Source:** "AI prompt evaluations beyond golden datasets" (Gluck + Nishant Shukla, Sr Director AI, 2025-02-18) — https://www.qawolf.com/blog/read-ai-prompt-evaluations-beyond-golden-datasets (fetched ✅ 2026-09-27; companion webinar with Helicone CEO on Wistia, not transcribed). Raw: `raw/qawolf-beyond-golden-datasets-2025.md`.

## Their 4 arguments (strongest vendor anti-gold statement in our corpus)

1. **Overfitting + drift:** static curated data trains noise-capture; production shifts rot the model ("a new road makes an old paper map obsolete").
2. **Cost + scale:** manual curation is slow/expensive; **by completion the dataset may already be outdated.**
3. **Versioning breaks comparability:** after updates "you can't directly compare the new dataset to previous versions, making it hard to track performance improvements."
4. **Creator bias:** curated data reflects curators (senior-only reviews → fails on junior styles).

Their replacement: **random sampling from production** (Helicone tooling, minimal cleaning) — flexibility, speed, cost, trust via continuous evaluation, no drift.

## Our counter: who labels the sample? (the oracle question, unanswered in the article)

The article never states WHO judges the random production sample. Two cases, both bad for the thesis as written:

- **An LLM judges it** → judge without ground truth on exactly the drifted inputs where judges are weakest. Trading a stale oracle for no oracle.
- **Humans label samples continuously** → that is a golden dataset with extra steps (plus sampling): same curation cost, now recurring forever, plus a versioning problem on every refresh.

The honest synthesis (recorded as our position, not theirs):

- **Frozen gold = the gate** (version-pinned, expiry-dated; comparability holds inside a version — answers their argument 3 by construction: never compare across versions, compare within).
- **Production sampling = the drift monitor** (detects when the gate's world moved — answers their arguments 1–2 without surrendering the oracle).
- Their argument 4 (creator bias) stands against BOTH approaches and is answered only by adjudication discipline (blind labeling, disagreement rates) — which is our labeling-guideline lane, not a dataset-shape choice.

Note the convergence: their "validate with positive and negative examples" (semantic-assertions piece) IS a golden micro-set per assertion. They already use gold at small scale while arguing against it at large scale — the dispute is about size and refresh policy, not about ground truth itself.

## Cross-links

- [[qawolf-semantic-assertions-jev-2026]] — same vendor; per-assertion positive/negative validation = golden micro-sets (tension noted above).
- [[llm-testing-6-approaches]] — Golden Dataset approach; this page is the counter-thesis.
- [[qawolf-6-types-self-healing-2026]] — same vendor, maintenance layer.
- `Positions company/pilots/Jev/` — our gold-n30 / B0 freeze protocol is the gate side of this synthesis.
- Quote banked: Articles/quotes.md → Market Signals ("outdated by completion" line).
