# Jev Performance Benchmark (2026-09-22)

## Summary
**Jev (TypeSafe System One) vs Pi/openrouter fallback** — 50 findings classified.

| Metric | **Jev** | **Pi/openrouter** |
|--------|---------|-------------------|
| **Avg latency** | **0.30s** | **~15s** |
| **Throughput** | **3.3 calls/sec** | **0.07 calls/sec** |
| **Success rate** | **100%** | **33%** |
| **50 findings total** | **~15s** | **~12+ min** |
| **Cost** | Free tier (until 2026-09-25) | Free tier (unreliable) |

## Test Conditions
- **Jev:** `TYPE_SAFE_API_KEY` via `https://api.typesafe.ai/v1/systemone`, model `jev-latest`
- **Pi:** `pi --provider openrouter --model openrouter/auto --print` with JSON prompt
- **Findings:** 10 OrangeHRM test failure patterns × 5 = 50 total
- **Environment:** macOS, Python 3.12, requests 2.31 / pi-subagents 0.64.0

## Key Observations
1. **Jev cold start:** First call ~0.95s, subsequent ~0.30s
2. **Pi cold start:** First call ~6s, subsequent ~5-10s with frequent timeouts (30s default)
3. **Pi success rate:** Only 2/6 sample calls returned valid JSON; rest timed out or returned empty
4. **Structured output:** Jev returns calibrated probabilities + confidence; Pi returns bare JSON (sometimes invalid)

## Conclusion
**Jev is 50x faster and 3x more reliable** for classification tasks. For 500-file scan:
- Jev: ~3 minutes total
- Pi fallback: ~2+ hours with high failure rate

## Recommendation
Use Jev as primary classifier. Keep Pi/openrouter only as emergency fallback for Jev API outages (not free tier exhaustion).

---

*Benchmark run: 2026-09-22, W3 Sprint Day 3*
*Related: `docs/jev-patterns.md` (custom schemas for FlowScout/OrangePro/OrangeHRM)*

## See also

- [Tier → Model → Threshold: Judge Selection Matrix (2026-09-24)](wiki/tier-model-selection-matrix-2026.md)
