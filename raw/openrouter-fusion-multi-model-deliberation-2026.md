# OpenRouter Fusion — Multi-Model Deliberation of Panels

**Date:** 2026-06-16
**Status:** Confirmed — launched June 12, 2026
**Source:** OpenRouter official docs + blog + third-party coverage

## What It Is

OpenRouter Fusion is a **multi-model deliberation API** that fans a single prompt to a panel of models in parallel, has a judge model compare their responses, and returns a synthesized final answer. It launched on June 12, 2026 and is available as:

- `openrouter/fusion` model slug (drop-in replacement for any model)
- `openrouter:fusion` server tool (attach to any model — model decides when to invoke)
- Fusion plugin (configured via `plugins` array)
- Chatroom at openrouter.ai/fusion (no-code)

It is **not** a model router (which picks one model per request). It is a compound-AI system: N models answer, a judge analyses, the outer model writes the final answer.

## How Multi-Model Deliberation Works

```
Your request → Your model decides whether to invoke fusion
            → Panel (1–8 models) answers in parallel + web_search + web_fetch
            → Judge compares → structured JSON (consensus, contradictions, blind spots)
            → Final model writes answer from analysis
```

Key details:

1. **Panel models** each answer the prompt in parallel, each with `web_search` and `web_fetch` enabled (up to 8 tool-calling steps each)
2. **Judge model** receives all panel responses and returns structured JSON — it does **not** merge them, it compares:
   - **Consensus** — points all or most models agreed on (higher confidence)
   - **Contradictions** — direct disagreements between panel members
   - **Partial coverage** — topics only some models addressed
   - **Unique insights** — ideas from individual models
   - **Blind spots** — gaps none addressed
3. **Outer model** (usually the same as judge) writes the final answer from that analysis — not a simple majority vote
4. **Recursion protection** — panel/judge models cannot recursively invoke fusion (single level only, tracked via `x-openrouter-fusion-depth` header)

### Default presets

| Preset | Panel models | Judge | Cost |
|--------|-------------|-------|------|
| Quality (default) | Claude Opus latest + GPT latest + Gemini Pro latest | First panel model | ~4–5× single completion |
| Budget | Gemini 3 Flash + Kimi K2.6 + DeepSeek V4 Pro | Smaller judge | ~0.40× cost of Fable 5 |

### Custom configuration

Users can override `analysis_models` (panel, 1–8 models), `model` (judge), `max_tool_calls` (1–16), `temperature`, `reasoning` effort, and `max_completion_tokens`.

## Benchmark Performance (DRACO)

OpenRouter tested on 100 deep research tasks from the DRACO benchmark (Perplexity AI):

| Configuration | Score | vs Fable 5 |
|--------------|-------|------------|
| Fusion: Fable 5 + GPT-5.5 (judge: Opus 4.8) | **69.0%** | +3.7 pts |
| Fusion: Opus 4.8 + Opus 4.8 (judge: Opus 4.8) | **65.5%** | +0.2 pts |
| Solo: Claude Fable 5 | 65.3% | baseline |
| Fusion Budget: Gemini 3 Flash + Kimi K2.6 + DeepSeek V4 Pro | **64.7%** | −0.6 pts (at ~50% cost) |
| Solo: Claude Opus 4.8 | 58.8% | −6.5 pts |
| Solo: GPT-5.5 | 60.0% | −5.3 pts |

**Key insight:** Running the same model twice (Opus 4.8 + Opus 4.8) gave a 6.7-point lift (58.8% → 65.5%), proving the synthesis step itself adds value — not just model diversity.

## Use Cases for QA/Testing

1. **Test strategy critique** — Panel evaluates a test plan from multiple angles (security, coverage, performance, maintainability); judge surfaces blind spots
2. **Bug triage / root cause analysis** — Multiple models analyse logs/screenshots independently; consensus = high confidence; contradictions = need human review
3. **Flaky test classification** — Panel judges whether a failure is environmental or code-related; cross-model agreement reduces false positives
4. **Test case generation review** — Generate test cases with one model, have a panel critique them for gaps/edge cases
5. **Spec ambiguity detection** — Panel reads requirements and flags where interpretations diverge — highlights requirements that need clarification
6. **High-stakes code review** — Escalation layer for security-sensitive or destructive changes (DB migrations, auth, billing) where cost of error > cost of deliberation
7. **Metamorphic testing oracle** — When there's no ground truth, panel consensus on expected behaviour substitutes as oracle

Fusion is best used as an **escalation layer** — not for every prompt, but for tasks where being wrong is expensive.

## Cost Implications

- **Quality preset:** ~4–5× cost of a single completion (3 panel + 1 judge)
- **Budget preset:** ~0.40× cost of Fable 5 but matches/exceeds frontier solo models
- **Cost scales linearly** with panel size (1 extra completion per additional model)
- **Panel + judge both use web search/fetch** — additional search costs apply
- **No extra per-request fee** from OpenRouter — you pay the sum of underlying model completions
- **Model decides when to invoke** — simple prompts skip fusion and pay 1× cost only

### Strategy for QA teams

- Use the Budget preset as a daily driver (beats most solo frontier models at half cost)
- Escalate to Quality preset only for high-risk decisions (release sign-off, security review)
- Custom panels can mix cheap+expensive models to balance cost vs quality

## Source URLs

- OpenRouter Fusion docs (plugin): https://openrouter.ai/docs/guides/features/plugins/fusion
- OpenRouter Fusion Router docs: https://openrouter.ai/docs/guides/routing/routers/fusion-router
- OpenRouter Fusion Server Tool docs: https://openrouter.ai/docs/guides/features/server-tools/fusion
- Blog announcement: https://openrouter.ai/blog/announcements/fusion-beats-frontier/
- Fusion pricing page: https://openrouter.ai/openrouter/fusion
- Fusion API pricing: https://openrouter.ai/openrouter/fusion/api
- The Neuron explainer: https://www.theneuron.ai/explainer-articles/openrouter-fusion-makes-the-case-for-compound-ai-models/
- Developers Digest: https://www.developersdigest.tech/blog/openrouter-fusion-model-panels-escalation
- Digit.in article: https://www.digit.in/features/general/what-is-openrouter-fusion-and-how-does-it-beat-frontier-ai-models.html
- TokenMix review: https://tokenmix.ai/blog/openrouter-fusion-api-review-2026
- DRACO benchmark paper: https://arxiv.org/abs/2602.11685
