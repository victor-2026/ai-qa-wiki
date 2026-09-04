# Rotation Without Relevance: Why Mutants Must Be Filtered Before Seeding

**Source:** QAEverest pilot (2026-09-02/03) + external mutation-testing literature
**Type:** methodology note · **Status:** draft for wiki

## Summary
"Rotation without relevance" is our field name for a classic failure: picking the
mutation operator by rotation order (element_remove / id_change / id_remove /
text_change / swap_targets, one per test case) without checking whether that
defect can affect what the test verifies. In our 01/09 run 0 of 4 seeded mutants
were catchable in principle — only the hidden-username case touched its
assertion; id_remove / label-change / id-rename mutants asserted success
message / error message / field type, which the mutation could not change.
Filtering them *after* the run dilutes the score; filtering them *before*
seeding fixes the denominator. The literature has studied this problem for
30+ years under other names — this page maps our terms to theirs.

## Term mapping: ours → classical

| Our term (pilot) | Classical term | Key source |
|---|---|---|
| Rotation without relevance | Unselective / naive operator selection | Offutt et al., Mathur 1991; Gopinath et al. empirical comparison |
| Irrelevant mutant (seeded, cannot matter) | Equivalent / low-utility / redundant mutant | Wikipedia "Mutation testing"; Madeyski 2014 review (17 techniques: DEM/SEM/AEMG) |
| Score diluted by noise (0/4) | Mutation-score inflation/deflation by equivalents | Score = Killed / (Total − Equivalent); Stryker docs |
| Pre-seed relevance gate (step 0) | Selective mutation; sufficient operators; context-based targeted selection | Petrovic et al. "Practical Mutation Testing at Scale" (Google, TSE 2022) |
| Assertion scope → operator allowlist | AST-context productivity model; arid-node suppression | Same Google paper §4 (random vs targeted, RQ4) |
| Survived-but-should-not-count | Subsumed mutant; TCE-duplicate | Cerebro (TSE 2023); TCE filtering |
| LLM/rule pre-filter before run | ML-guided mutant prioritization; semantic equivalence check | Meta ACH; Cerebro; CodeBERT pre-execution filter |

## 1. Equivalent mutants — the original "irrelevant" problem
A mutant syntactically different but semantically identical can never be killed;
deciding equivalence is undecidable, and humans misjudge ~20% of cases (Cerebro
§6.2). The 2014 Madeyski review catalogs 17 techniques in 3 families: detecting
(DEM), suggesting (SEM), avoiding generation (AEMG). Practical rule used
everywhere: **score = Killed / (Total − Equivalent)**, never Killed / Total.
Our "Not seeded = outside denominator" is the same rule, applied before
execution instead of after adjudication.

## 2. Selective mutation and sampling — less is more
Since Acree 1979 (Random X%) and Mathur/Offutt selective mutation, the field
knows most operators are redundant: Namin et al. found 28 of 108 Proteum
operators sufficient; Untch/Deng showed statement-deletion alone correlates
R²≈0.97 with full score. Gopinath et al. and Zhang et al.: uniform random
sampling (even 5%) predicts full score at ~99% correlation, often beating
operator selection. Lesson for us: rotation over a fixed operator list with no
relevance check is the worst of both worlds — neither selective nor random.

## 3. Google at scale — the direct precedent for pre-seed filtering
Petrovic/Ivankovic/Fraser/Just ("Practical Mutation Testing at Scale",
arXiv:2102.11378, TSE 2022; 24k developers, 1000+ projects, 2B LOC) solve
exactly our problem with three ideas: (1) mutate only changed code at review
time; (2) **filter likely-irrelevant mutants before execution** — arid-node
suppression + max one mutant per line; (3) **targeted operator selection by
historical productivity in AST context** (random vs targeted, §4). Result:
orders of magnitude fewer mutants; context-based selection +40% survival and
+50% developer-judged productivity (RQ4). Our step-0 gate (assertion scope
from step action + prose → 5-operator allowlist) is a rule-based instance of
their targeted selection, adapted from code AST to UI test steps.

## 4. RIP model and weak vs strong mutation — why scope matters
A mutant is killed only if the test **R**eaches it, **I**nfects state, and
**P**ropagates to a checked output (RIP model). Weak mutation requires only
Reach+Infect; strong mutation requires all three. Our taxonomy maps cleanly:
Caught ≈ strong kill, Observed-only ≈ weak (platform saw it, suite did not
propagate to verdict), Survived ≈ missed. A mutant whose operator cannot reach
the assertion scope (id mutant vs type assertion) fails RIP at step 1 — it is
equivalent *for that test* and must never enter N.

## 5. Subsumed mutants and TCE — the denominator hygiene
Subsumed mutants (same location, same fate as another mutant) add executions
without information; Trivial Compiler Equivalence (TCE) removes equivalent and
duplicated mutants before running. Cerebro (TSE 2023, 48 C + 10 Java programs)
selects only subsuming mutants statically from context: 91–92% fewer test
executions, equivalent rate 3.7% vs ~55% for random. Our "rotation varies
operator only within the relevant set, target = last step before first
assertion" plus one-mutant-per-case is the same hygiene at UI level.

## 6. ML-guided pre-execution filtering — the automated version
Meta ACH generates realistic (not template) mutants and filters low-value /
equivalent ones with an LLM *before* execution; CodeBERT-style semantic
equivalence checks cut equivalent rate from 20–40% to ~5–15% and runtime by
~85% while keeping critical gaps. Our allowlist is the deterministic,
auditable cousin: same position in the pipeline (before seeding), but
rule-based so an Assessor can trace every exclusion.

## 7. What this means for our gate
- Keep the relevance decision **before** seeding (step 0), never as a
  post-hoc "Expected to catch?" column — post-hoc keeps noise in N.
- Split `Not seeded` into `Excluded as irrelevant` (outside DOM / no scope
  overlap — legitimately out of N) vs `Tooling gap` (locator-cache miss —
  separate Infra-gap metric, never silent). This answers the P0-2 review.
- Require `Baseline green gate` before seeding (P0-1): N counts only cases
  green unmutated, with baseline run id logged.
- Log per mutant: operator, target step, derived assertion kinds, candidate
  set, type (Value/Decision/Statement) — makes the mechanical decision
  auditable, as proposed in the 19:44 diff.
- Missing `Decision`-type operator (enabled⇄disabled etc.) is the known gap
  for B0 Critical logic-flips — add or document exclusion with risk note.

## Sources (external)
- Petrovic et al., "Practical Mutation Testing at Scale", arXiv:2102.11378 (2021) / TSE 2022 — https://arxiv.org/abs/2102.11378
- Wikipedia, "Mutation testing" (RIP model, equivalent/subsumed mutants, selective mutation, Madeyski 2014) — https://en.wikipedia.org/wiki/Mutation_testing
- Jia & Harman 2009 survey (cost problem); Gopinath et al. (sampling vs operator selection); Zhang et al. (5% sampling ≈99% correlation)
- "Selecting mutation operators with a multiobjective approach" (Barbosa/Namin/Offutt line, sufficient operators) — https://www.sciencedirect.com/science/article/pii/S0957417412006380
- Cerebro: Static Subsuming Mutant Selection (TSE 2023) — https://www.computer.org/csdl/journal/ts/2023/01/09677967/1A4SyVTjzhu
- Stryker docs, "Equivalent mutants" (score formula) — https://stryker-mutator.io/docs/mutation-testing-elements/equivalent-mutants
- Madeyski et al., "Overcoming the Equivalent Mutant Problem" (TSE) — http://madeyski.e-informatyka.pl/download/Madeyski13TSE.pdf

## See also
- [AI QA Tool Evaluation Mutation Matrix](ai-qa-tool-evaluation-mutation-matrix.md)
- [Mutation Testing vs Code Coverage (Autonoma)](mutation-testing-vs-code-coverage-autonoma.md)
- [Mutation Testing for Playwright Front-End](mutationtestingplaywrightfront-end.md)
- [Advanced Mutation Testing with Playwright](Mutation-testing-advanced-playwright.md)
- Per-risk-tier framework v0.3 (`Private/Positions-CV-CL/outreach/active/Rupesh_Kabra/per-risk-tier-framework.md`): step-0 gate, B0–B3 tiers, 5-operator allowlist

---
*Wiki note 2026-09-04 · answers "is rotation-without-relevance a known problem?" — yes: equivalent/low-utility mutants + unselective operators; the fix the field converged on is filtering/selection **before** execution (Google arid+targeted, Cerebro static, ML pre-filters). Our gate is the UI-test instance.*
