# Verdict - demo-pass.csv

verdictgate v0.2.2 · deterministic: same input → same verdict · gates are per-tier, never blended
config: B2 band 5% at N>=20, B2 small-N max 1 survivor(s), fail-on-unexercised=off, requirements-cross-check=off — tiers unverified

## Per-tier results

| Tier | Seeded | Caught | Observed-only | Survived | Mutation score | Survival rate | Gate |
|---|---|---|---|---|---|---|---|
| B0 Critical | 2 | 2 | 0 | 0 | 100.0% | 0.0% | PASS |
| B1 High | 1 | 1 | 0 | 0 | 100.0% | 0.0% | PASS |
| B2 Medium | 0 | 0 | 0 | 0 | 0.0% | 0.0% | NOT EXERCISED |
| B3 Low | 0 | 0 | 0 | 0 | 0.0% | 0.0% | NOT EXERCISED |

## Gate verdicts

**B0 Critical - PASS** (zero-tolerance held (survived 0 of 2))
- Signal: B0 sign-off additionally requires a confirmatory re-run (two consecutive passing runs)

**B1 High - PASS** (zero-tolerance held (survived 0 of 1))

**B2 Medium - NOT EXERCISED** (no seeded mutants (expected=Y) in this tier)

**B3 Low - NOT EXERCISED** (no seeded mutants (expected=Y) in this tier)

## Fix first

None - no survivors recorded.

## Sign-off (evidence pack)

| Role | Name | Decision | Date |
|---|---|---|---|
| Reviewer of record | | | |
| Independent Assessor | | signed comment required - signals fired | |
| Engineering owner | | | |

Attach: this file, the .json twin, the raw results.csv, and run logs/screenshots for every seeded mutant (lineage, not belief). Anyone with the same CSV and scorer version reproduces this verdict exactly.
