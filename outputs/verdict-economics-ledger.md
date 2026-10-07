# Verdict-economics ledger (thin; W2-approved track)

**Rule:** stays a ledger. Price/latency/quality per judge-hands, one glance per "which judge" dispute. If it ever demands heavier governance — rescope, don't feed.
**Provenance:** rows marked W2-provided vs vendor-claim vs measured. No unattributed numbers.

| Judge / model | Price | Latency | Quality note | Source | Date |
|---------------|-------|---------|--------------|--------|------|
| LLM judge (ours) | ~$0.04/verdict | — | measured | W1-provided (7680145) | 2026-10-02 |
| VerdictGate gate | ~$0.80/tier | — | static, zero deps; measured | W1-provided (7680145) | 2026-10-02 |
| local-judge v0 | $0 | 0.1s | baseline | W2-provided | 2026-09 |
| local-judge v1 | — | 0.28s | — | W2-provided | 2026-09 |
| local-judge thinking | — | 24s thinking tax | — | W2-provided | 2026-09 |
| local-judge v2 | — | 0.4s | — | W2-provided | 2026-09 |
| Jev (TypeSafe AI, via ngrok GW) | $0.042/M in, out free | — | typed verdicts (97% true / 3% false style) | vendor-claim (ngrok newsletter) | 2026-10-01 |
| GLiDE (Fastino, vs Jev) | — | low (adaptive reasoning) | +6.90 Decision Index (vendor-claim, their harness) | vendor-claim (Fastino post) | 2026-10-01 |
| Clef Flash 9B (Cloudflare, Ollama, local, text+image) | local ($0) | median 38.8ms / p95 122ms | Qwen3.5-9B finetune, 11GB, 256K ctx; 1 forward pass (3 output tokens); types choice/noul/score; Jev-API compatible (/v1/systemone); Apache 2.0; needs Ollama ≥0.35.1 | vendor-run benchmarks (Cloudflare Decision Index) | 2026-10-03 |
| Clef 27B (Cloudflare, Ollama, local) | local ($0) | median 209ms / p95 239ms | Qwen3.8-27B, 18GB; tops Decision Index, beats Jev on most | vendor-run benchmarks | 2026-10-03 |
| Clef Flash 9B pilot (ours, GTX 1660 Ti 6GB) | local | FAIL (non-finite logit, 4/4 configs) | VRAM 7.4/6GB over budget; PARKED pending upstream fix (model 2 days old); upstream issue drafted, unsent | W3 pilot | 2026-10-04 |
| Jev (TypeSafe, reference) | $0.042/M in, out free | median 524ms / p95 536ms | baseline the other two beat | vendor-run benchmarks (same table) | 2026-10-03 |
| Router economics (Kravchenko/Archestra, turn-0) | — | — | +7.6…+9.2% @c=0.2 (tail 64% hard) → loses −0.2…−4% @c≥0.4 (pre-human-time scope); botched cheap = c+1+h; use: cost-of-wrong-verdict illustration vs judge $0.04 / gate $0.80 | W5-provided 2026-10-05 (figures not verified by W2): https://archestra.ai/blog/routing-coding-agents-on-the-cheap + https://lnkd.in/p/e3dTH79v | 2026-10-01 |
| Cache-switch tax (Kravchenko/Archestra) | Sonnet $2.09/task vs Opus $1.94 (Databricks) | — | downgrade median 0.83 (not 0.5); cache hit 55%→8% after model switch; use: model-switch tax in tier cost | W5-provided 2026-10-05 (figures not verified by W2; same two links as Router row above) | 2026-10-01 |
| Delegation supply (Kravchenko/Archestra) | ~5% parent spend ($219/$4.5k) | — | 2/3 context carry; use: delegation for context, not price | W5-provided 2026-10-05 (figures not verified by W2): https://archestra.ai/blog/routing-coding-agents-on-the-cheap | 2026-10-01 |
| Kolibri (Aleph Alpha, open MoE) | local $0 weights Apache 2.0; iron H100-class, NOT 6GB-runnable | — | 78.1B/3.46B act, 1M ctx; abstention-trained; judge-substrate candidate | vendor blog 03.10.2026, verified W2 from primary | 2026-10-03 |
| e2e assertions (awesome-testing eval, Sonnet 5.5) | $0.0073/assertion (~0.7¢); $7.32/1000 assertions; full suite $1.99/run ($1.03 replay); 1000 runs ≈$1992 ($1035 replay) | 21s → 200s (9.5x) | 68 tests, 95 assertions per full UI suite | W5-provided 2026-10-06 (figures not verified by W2): awesome-testing e2e eval 02.10 + Sonnet 5.5 pricing 02.10.26 | 2026-10-02 |
| Trace-error judge (Robert Kim, laminar.sh) | 23x cheaper than GPT-6-sol (relative, no absolute $) | — | matches GPT-6-sol; −25% vs GPT-6-luna; fewer false alarms; every-run monitoring; 523-trace own benchmark | vendor-claim (UNVERIFIED), W5-provided 2026-10-06: Robert Kim post (laminar.sh, YC S24) | 2026-10-06 |

## Digest-watch: decision models (W5)
- Track: Jev, GLiDE, analogues (typed-output judges, verdict economics).
- Action on sighting: one ledger row + checkpoint line. No pages until pattern repeats 3×.

---
*Teams index: verdicts + token savings = blood (owner's metaphor, W2-confirmed with local-judge numbers).*
