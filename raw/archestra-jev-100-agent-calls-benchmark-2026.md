# Archestra: We Tested Jev on 100 Real Agent Calls. How Easy Is It To Beat a Constant? (2026-09-21)

**Author:** Arseny Kravchenko (Staff AI/ML Engineer, author "ML System Design")
**Source:** https://archestra.ai/blog/we-tested-jev-on-100-real-agent-calls
**Context:** Full benchmark writeup behind the 2026-09-21 LinkedIn post. Archestra = open-source enterprise infrastructure for running AI (agents + MCP + LLM proxy + access control). OpenAPPA = Information Flow Control (IFC) product.

---

## TL;DR

Compared Jev vs Sonnet 5 vs open-weight models on 100 real tool calls from production Claude Code sessions, for a security-boundary classifier (annotator) in OpenAPPA. Key result: Sonnet led by 5-6 pts, but ALL 8 of its errors were leaks (false negatives). Jev competitive (93% → 95% with 9-shot), fast (~300ms), cheap ($0.37 total bill), useful confidence scores. Open decoders failed: position priors, flat logits, unusable confidence. Benchmark itself was flawed: random sampling = 90% routine / 10% dangerous, so macro scores hide leak risk.

---

## The problem

OpenAPPA annotator classifies each tool call at runtime for security:

- delta_audience: who can see the tool's output (self / internal / public)
- delta_trust: output trusted or suspicious
- requires_audience: who can receive data sent by the call
- requires_trusted: whether to block the call if session contains untrusted data

This classifier sits on a security boundary: if it marks a dangerous call as safe, OpenAPPA will allow it.

## The 79% constant trap

Real agent traces: tool calls like `cargo test -p appa`, `git status --porcelain`, `cat package.json` are harmless and stay local. **79% of the 100-call dataset is the default label.** A hardcoded classifier always returning "benign" scores 79%. A model scoring 75% accuracy is worse than that constant. "Accuracy can be misleading."

## The confusing cases (delta vs requires)

1. **Output trap (Slack message):** output is public+trusted (trivial ack), but delivers internal bytes to a channel → requires_audience=internal, requires_trusted=true. Models confuse delta (what the tool returns) with requires (what must be true before the call runs).
2. **Opaque references:** `{"tool":"execute_remedy_plan","arguments":{"offer_id":"4a2d16..."}}` — hex ID, no semantic context in args; judge strictly on tool identity.
3. **Outbound queries:** WebSearch returns untrusted bytes (delta_trust=suspicious) AND transmits the query outside the perimeter — if session already tainted, malicious injection exfiltrates sensitive context via the query string. Search ≠ harmless reading.

## Setup: Jev structured calls

Jev takes structured state + typed questions answered in parallel (not free-form prompt):

```python
response = client.predict(
    state={"tool": "Bash", "arguments": {"command": "cargo test"}},
    questions=[
        {"id": "delta_trust", "type": "choice", "instructions": "...",
         "criteria": {"trusted": "...", "suspicious": "..."}},
    ]
)
```

## Evaluation setup

Models: Jev (jev-latest), Qwen3-Reranker-4B, Laya (ModernBERT-large), SemIf (formerly OpenJev, Qwen + MiniCPM backbones), Bespoke-Nimble-9B, Sonnet 5.

System: zero-shot baseline with reranker scoring (tool call, label) pairs + softmax; 100 calls × 4 labels = 400 decisions; report 337 where all three judge families agreed (Claude Opus, GLM 5.3 Flash, Gemini 3.8 Flash, blind).

**Self-grading bias:** models scored their own answers 2-3 pts higher; Gemini gave itself 100%. Opus had no measurable preference for Sonnet (-0.1 pts). "Rule one of model evaluation: don't let a model grade its own homework."

63 excluded decisions exposed spec gaps: outbound reads (harmless read vs exfiltration channel), opaque IDs (no context in args), tool metadata classification. Rules were unclear — evaluation needed work too.

## Results table

| Model | 0-Shot | 9-Shot | Refusal Recall (requires_trusted) |
|---|---|---|---|
| Sonnet 5 | 98% | N/A | 44% (4/9) |
| Jev (jev-latest) | 93% | 95% | 78% (7/9) |
| Bespoke-Nimble-9B | 83% | 86% | 33% (3/9) |
| Majority Baseline (Constant) | 79% | 79% | 0% |
| SemIf (Qwen3.5-4B) | 63% | 84% | 78% (7/9) |
| Qwen3-Reranker-4B | 64% | 75% | 67% (6/9) |
| SemIf (MiniCPM5-2B) | 54% | 80% | 0% |
| Laya (ModernBERT-421M) | 48% | 46% | 100% (9/9)* |

*Laya caught all 9 dangerous only by flagging everything: 100% recall, 12% precision.

## Anatomy of failure: position priors & calibration

- Open models learned option position, not the task. Rotating options A/B/C → B/C/A: Qwen 0.6B always chose A; MiniCPM-2B always chose the last option. Small constrained decoders failed all 100 permutation tests.
- 9-shot examples helped decoders +20 to +34 pts (SemIf-4B kept correct answer in 92/100 order tests); no help for encoder-based Laya (-2 pts, needs fine-tuning).
- Most confidence scores were NOT useful. Jev well-calibrated when allowed to abstain: predictions with confidence ≥ 0.7 had zero errors — confidence-based routing practical (clear cases fast path, uncertain → bigger model / human review). Reranker + open decoders: highest/lowest option probs only 0.05-0.10 apart — flat logits, confidence filtering = filtering floating-point noise.

## Jev reproducibility & option-order sensitivity

5 back-to-back evaluations on 100 calls: 3 identical, 1 reversed criteria keys, 1 cyclically shifted.

- **Labels hold, probabilities drift:** identical repeats → 394-398/400 identical labels (flips at dead heats within 0.02 of 0.50); only 35-39% of predicted probabilities bit-identical; median p-drift 0.01, run-to-run swing up to 0.17.
- **Order sensitivity real, isolated to 3-way labels:** binary labels (requires_trusted, delta_trust) zero flips under reordering; 3-way labels (delta_audience, requires_audience) 5-7 calls/100 changed, minus baseline noise ≈ 4/100 from option order alone → 1.5-2 pts accuracy.
- **Most flips near-ties, rare wild swings:** one case flipped confident internal (0.83) → public (0.48) under reorder.
- **No clean positional bias** (unlike small decoders); competing options trade mass.

## Error analysis: stalls vs leaks

Errors at a security boundary have different costs:
- **Stalls (False Alarms):** safe call restricted/blocked; agent may lose output. Inconvenient.
- **Leaks (False Negatives):** dangerous call allowed; data can leave the system. Severe.

Live examples:
1. **Search blindspot (Sonnet 5):** missed EVERY outbound search query (WebSearch, slack_search_channels, slack_search_public_and_private) — treated search as harmless reading, but search sends query to external API; poisoned context → exfiltration via query string. All 8 of Sonnet's strict-set errors were leaks. (Both models caught obvious writes like `gh pr merge 343 --squash --delete-branch` → requires_trusted.)
2. **Paralyzing stall (Reranker 4B):** routine local command `CARGO_INCREMENTAL=0 cargo test ... | tail -40` → delta_audience=self instead of internal, across 65 calls. Over-restrictive: stricter is not always safer (prevents later commands using safe output).
3. **Leaky baseline (SemIf MiniCPM-2B):** 80 leaks / 337 decisions; classified 58 internal file reads as public.

## Methodology lessons

- Original benchmark was bad: ~90% routine / only 10% dangerous cases in 100 random samples. A model scores well by labeling almost everything benign while missing critical leaks. Needed to overrepresent the dangerous minority.
- Errors don't have the same cost — blocking safe call inconvenient, allowing unsafe one exposes data.
- Debug the AI harness on weak models on purpose — weak models make evaluation problems easier to spot (Laya stopped after 45 tokens, decoders returned "A" always). These exposed harness bugs, unclear prompts, poor sampling; Sonnet worked around them, making them harder to notice.

## Takeaways for production

- Beware public benchmark hype on out-of-distribution tasks. AG News/sentiment results don't transfer to security tool contracts; zero-shot produced strong output biases.
- Inspect individual errors — judge disagreements exposed unclear instructions, not model unreliability. The evaluation needed work too.
- Jev is a promising router: ~300ms, low cost, competitive with frontier on structured contracts, confidence = escalation signal (clear→fast, uncertain→larger model/human).
- Never rubber-stamp a model on an execution boundary based on macro numbers alone. "If a model controls an execution boundary, inspect how it fails. The overall score does not show whether it fails safely."

---

## Cross-references (in this wiki)

- `wiki/jev-openai-proprietary-beaten-open-source-2026.md` — Jev vs open-source debate
- `wiki/ruben-hassid-jev-internet-moment-setup-2026.md` — Jev workflow "Internet moment"
- `wiki/typesafe-jev-judgment-service-gates-2026.md` — Jev judgment service as gate
- `wiki/opencode-jev-113-free-system-one-model-2026.md` — Jev as free System-1 model
- `wiki/jev-jason-arbon-playwright-bounded-exploration.md` — Jev in Playwright loop

## Relevance to VerdictGate / Articles series

- 79% constant trap = same baseline discipline as VerdictGate golden-dataset: eval must beat a prior constant, not just random chance.
- Stalls vs Leaks = FP/FN asymmetric cost; Leak = silent false negative with no alarm (Articles 20/26).
- "Don't let a model grade its own homework" = why author ≠ examiner (self-grading bias 2-3 pts).
- Labels-hold-probabilities-drift + option-order flips ≈ verdict primitives are quasi-deterministic → version-stamp verdicts (SCORER_VERSION), treat confidence thresholds as fuzzy.
- Weak-models-first harness debugging = mutation-matrix intuition (break the harness first).