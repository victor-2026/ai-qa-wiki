# Demo kit: seeded side of the gate (for Vipul, on his "yes")

**Show only on his go-ahead. No dumps unasked. No vendor cases (Rupesh track = NDA).**
**Runtime:** ~15 min. **Needs:** python3 stdlib only + verdictgate.py. All files in this dir.

## Files

| File | Content | Verdict |
|------|---------|---------|
| `demo-pass.csv` | 3 mutants, all caught (suite failed as designed) | B0 PASS, exit 0 |
| `demo-fail.csv` | B0 mutant survived SILENT (no attribution) | B0 FAIL, exit 1 |
| `demo-observed.csv` | B0 mutant survived WITH attribution (seeded-run/demo-001/submit-button) | B0 PASS + signals (mutation score + observed-only budget) |
| `*-out/*.verdict.md` | pre-rendered evidence packs (backup if live run hiccups) | — |

## Runbook (live, 3 commands)

```bash
python3 verdictgate.py verdict demo-pass.csv      # all green, gate PASS
python3 verdictgate.py verdict demo-fail.csv       # silent B0 survivor -> gate FAIL
python3 verdictgate.py verdict demo-observed.csv  # attributed survivor -> PASS with review signals
```

## Narrative (one line per run)

1. **PASS:** every seeded break rang. Green means checked.
2. **FAIL:** one B0 break sailed through with no trace. Green means nothing — gate says FAIL, release stops. *This is the 5/5-green case from the article, in miniature.*
3. **OBSERVED:** same break, but with evidence attached (who saw it, which run, which element). Gate passes WITH mandatory review signals. Attribution is the difference between silent and observed.

## Policy one-pager (say, don't show)

- B0 Critical: zero silent survivors, plus confirmatory re-run. No exceptions.
- B1 High: zero silent survivors.
- B2 Medium: band (≤5% at N≥20, max 1 at small N).
- Gaps first, then the verdict. Unverified ≠ pass, never blended across tiers.
- Seeder ≠ runner; rotation; pre-registered verdicts. Blindness is org design.

## Boundaries (hard)

- No QAEverest/Rupesh cases, numbers, or names. Ever. (W1 zone, breach = track suicide.)
- No pricing, no offer, no follow-up ask. His call on direction.
- Toy scope only (payment/login demo rows). If he wants his own system seeded — that's a scoped pilot conversation, not this demo.
