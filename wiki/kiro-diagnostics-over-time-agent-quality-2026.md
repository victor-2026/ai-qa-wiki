# Are AI Coding Agents Actually Getting Better? — Six Months of Diagnostics

**Source:** https://kiro.dev/blog/diagnostics-over-time/
**Date:** August 26, 2026
**Authors:** Pardis Pashakhanloo, Rajdeep Mukherjee (Applied Science)
**Tags:** #kiro #diagnostics #static-analysis #agent-quality #evaluation
**Raw:** [kiro-diagnostics-over-time-2026.md](../raw/kiro-diagnostics-over-time-2026.md)

---

## What It Is

Analysis of 406K diagnostics-tool invocations over 6 months (Jan-Jun 2026), 1.5M conversations, 7 Claude models (Opus 4.5-4.8, Sonnet 4-4.6) across TypeScript, Python, Java, Rust, Go, Kotlin, C++, Swift. Measures *how* agents self-correct via static analyzers, not just final-state quality.

Diagnostics tool = language servers (tsserver, jdtls, Pyright, rust-analyzer, gopls, etc.) + linters (ESLint) + infra validators (CloudFormation). Catches compile-time issues; runtime/logic/performance invisible.

Two lenses: (A) post-hoc static analysis of final output vs (B) diagnostic invocations during generation (this study). B reveals self-monitoring, fix capability, cost in tool calls.

**Caveats:** environment varies (installed extensions), Amazon-internal users (narrower variance), model improvements confounded with steering/hooks/subagent changes.

## Six Findings

### 1. How Often Models Call Diagnostics (Invocation Rate)

| Model | Rate |
|-------|------|
| Opus 4.6 | 22.26% (peak) |
| Opus 4.5 14.58%, 4.7 10.15%, 4.8 10.85% |
| Sonnet 4 7.65%, 4.5 2.74% (lowest), 4.6 13.89% |

3-22% overall — most tasks complete without proactive static check. Models default to training-time tools; need prompting/fine-tuning to use diagnostics. Blocking agent until diagnostics clean could cut incorrect-code acceptance from ~90% → ~8%.

### 2. Errors per Checked File (Are Models Getting Better?)

- Sonnet: 3.01 (v4) → 2.90 (4.5) → 1.29 (4.6) = **57% reduction**
- Opus: 1.74 (4.5), 1.21 (4.6), 1.82 (4.7), 1.21 (4.8) — non-monotonic
- Latest convergence ~1.2 errors/file — progress toward compilable code.

### 3. Files Checked per Invocation (Scope)

- Opus 4.5 1.78 → 4.7 2.04 → 4.8 1.91
- Sonnet 4 1.57 → 4.6 1.86

Newer models check *related* files together (impl + test, module + consumers) → catch cross-file regressions (broken imports, interface mismatches).

### 4. Top Error Categories

Unresolved imports dominates: ~30-58% across models (Opus 4.7 57.6%). Then undefined symbols, syntax, implicit any, property access. Distribution differs: some models fail narrowly (imports), others broadly.

### 5. Source vs Test Files

Test files 3-4x harder:

| Model | Source | Test |
|-------|--------|------|
| Opus 4.6 | 0.96 | 3.64 |
| Opus 4.8 | 0.81 | 6.00 |
| Sonnet 4.5 | 2.26 | 9.13 |

Mocking/assertion/setup complexity drives test errors.

### 6. Language Landscape (Opus 4.6, % files with error)

Java 26.7% (1 in 4 files — verbose imports, generics, checked exceptions) > Rust 15.1% > C++ 12.2% > TSX 11.2% > TypeScript 8.6% > Kotlin 8.5% > Go 8.0% > Python 4.0% > JavaScript 1.6% (weak static analysis, not better generation). Python low = dynamic typing hides runtime issues.

## Conclusion

- Error rates dropping, but composition shifts (different mistakes, not just fewer).
- Unresolved imports are #1 fix target.
- Test code remains hardest.
- Language choice predicts cleanup cost.

## Relevance to QA/QE

| Insight | Action |
|---------|--------|
| Diagnostics invocation = self-monitoring signal | Require agents to call diagnostics before finalize; gate on 0 errors |
| Test files 3-4x harder | Invest in test-generation specialists; review test mocks heavily |
| Cross-file checks catch regressions | Enforce impl+test joint validation |
| Java 26.7% vs Python 4% | Budget more review for Java codebases; don't trust JS 1.6% (under-measured) |
| Invocation rate 3-22% | Without prompting, agents skip verification — make it mandatory via steering/hook |

## Critical Analysis

**Strengths:**
- Granular breakdown by model/language/file-type; actionable.
- Self-correction lens stronger than final-state pass/fail.

**Gaps:**
- Static only; runtime correctness invisible. Clean diagnostics ≠ correct code.
- Observational, not controlled — can't attribute to model vs harness.

## Cross-links

- Related: [Continuous prompt evaluation](kiro-continuous-prompt-evaluation-llm-judges-2026.md) — same evaluation mindset, different signal
- Related: [PBT security bug](kiro-property-based-testing-security-bug-2026.md) — dynamic testing complements static diagnostics
- QA evidence layer: [ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md](ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md)

---

*Ingested: 2026-08-30*
