# Metamorphic Testing: Next Test Cases (Chen-Cheung-Yiu 1998)

**Source:** T.Y. Chen, S.C. Cheung, S.M. Yiu, HKUST-CS98-01 (1998, arXiv 2002.12543). Raw: `raw/metamorphic-testing-next-test-cases-chen-1998.pdf` (11pp, full text read 10.10; OCR noisy). The founding MT paper (via Klain Bach-video thread).

## Three observations (the motive)

1. Successful tests are discarded — whether they still hide errors is unstudied.
2. Development-phase testing never exhausts errors; production-phase detection is almost unaddressed; production outputs go unverified.
3. Oracles are pragmatically unattainable (Weyuker) yet conventional techniques assume them.

## Method: fault-based follow-ups from successful pairs

Assume errors persist despite correct output. From each (apparently) successful input-output pair, design follow-up cases targeting error classes typical for the domain: non-existence reporting, overwriting, splitting errors, q-th-vs-k-th occurrence. Worked through binary search (missing `mid+1` element), k-th occurrence in unsorted array, Gaussian elimination pivot. Combines with any selection strategy + Blum's program checker (checker verifies, MT proposes next).

## Honest limits (author-stated)

No full methodology yet — next-case design rests on programming/testing experience, needs domain knowledge; domain-specific methodology as future work. Checker must be faster than the program (oh-property) or impractical.

## QA interpretation

- **"Assume errors despite green"** is the seeded-breaks mindset in 1998 form: green ≠ proven, follow-ups mandatory.
- **Production-phase testing** (unverified production outputs) prefigures our post-deployment verification lane.
- **No-oracle operation** = relations over outputs, not expected values — the ancestor of judge rubrics + abstention.
- **Checker-verifies / MT-proposes split** maps to judge-vs-seeder separation (one confirms, the other hunts).
- **Experience-based design** caveat rhymes with our operator-allowlist: method needs encoded domain knowledge, not just will.

## See also

- [[aqef-seeded-controls-spec-2026]] — fault seeding as oracle instrument
- [[rotation-without-relevance-preseed-mutant-filtering-2026]] — relevance filtering
- [[bach-ai-writing-policy-psa-2026]] — Bach/RST lane (video thread origin)
