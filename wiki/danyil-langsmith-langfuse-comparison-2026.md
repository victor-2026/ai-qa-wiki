# Danyil Zuiev: LangSmith vs Langfuse (Same Bot, 12 Cases, Oct 2026)

**Sources:** LinkedIn post (canonical, guest-fetch verified 08.10): https://www.linkedin.com/posts/daniil-zuiev_llmevaluation-llmops-aiquality-activity-7513514744541143041-BfSC + repo README (full text read 08.10): https://github.com/Daniilzuyev/llm-evaluation-portfolio/blob/main/20-langfuse/README.md. Author: Danyil Zuiev (Tier-1 peer watch, 3,293 followers). Bot: Imagine Bank RAG support bot, 12 cases with failure_mode, Claude Haiku 4.5 + Sonnet 5 judge, one-line retriever change between runs.

## Results (N of 12, not averages)

LangSmith 9→10, Langfuse 8→11 on same change; input tokens identical (retrieval reproduced exactly); output/judge differ = model non-determinism (temperature unset), NOT attributed to either tool. Latency not compared (different spans, single runs). Dataset defect admitted (daily-limit case also requires monthly limit); stale_data fails every run; no_phone_number never fires.

## Tool costs (observed, version-pinned)

- LangSmith (0.14.1): wrap_anthropic breaks on anthropic 1.x (pin <1); instant P50/tokens/cost in UI; dataset edit = delete + re-upload.
- Langfuse (4.16.0, OTel-based): clean upserts by id; manual usage_details mapping (wrong keys → zeros); no run-level totals in UI (scripted via API); legacy endpoints 410 for orgs created after 2026-09-16 (use v2 reads); UI list view hides item 0 (Raw shows all).
- Explicit non-verdicts: token rates inferred not checked; retention-cut claim unchecked; single runs = no latency conclusions.

## Takeaway (his)

"On this dataset the main cost with LangSmith was SDK compatibility. The main costs with Langfuse were API drift and missing run-level totals. The data does not support an overall better tool verdict." Plus post thesis: single run = statistical noise; bottleneck = tool compatibility + API drift, not the model.

## QA interpretation

Exemplary small-N honesty protocol: counts not averages, 8.3pp-per-item arithmetic stated, non-conclusions labeled, version pins published, offline pytest green. Direct backup for Breaklight noise-floor doctrine at practitioner scale + our abstention/small-N language. Seeded-break adoption already on record from same author (prior reply).

## See also

- [[breaklight-ai-testing-methodology-whitepaper-2026]] — noise floor, slice discipline
- [[elastic-shared-eval-framework-chang-2026]] — trace evaluators, calibration ownership
- [[kenhuang-claude-eval-hillclimbing-note-2026]] — uncertainty at task level
