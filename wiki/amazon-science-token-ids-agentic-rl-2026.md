---
source: "amazon-science-token-ids-agentic-rl-2026.md"
ingested: "2026-09-24"
---

## Amazon Science – Turnstile: Token‑ID Capture for Agentic Reinforcement Learning  

**Date:** 9 July 2026  

### Summary  
Reinforcement learning (RL) for large language models (LLMs) works best when the model can repeatedly attempt complex, multistep tasks (coding, web navigation, research workflows) inside a *harness* that mediates tool calls and observations. The bottleneck is not the learning algorithm but the fidelity of the data fed back to the trainer. Traditional harness logs contain only human‑readable transcripts, which can hide subtle token‑level differences caused by formatting, tokenizer quirks, or chat‑template changes. These mismatches—*retokenization drift* and *chat‑template drift*—break the alignment between the context the model actually saw and the context the trainer assumes, degrading the policy‑gradient signal.

**Turnstile** is a lightweight Rust proxy that sits between any agent harness and the inference backend (currently SGLang, with vLLM support planned). By intercepting the OpenAI Chat‑Completions API calls, Turnstile records the exact token IDs, per‑token log probabilities, and loss masks at the moment of generation. The captured trajectories are exported as framework‑neutral `TrainingSequence` objects, ready to be combined with rewards and fed into any RL stack. This approach eliminates the need to modify existing harnesses, preserves the true token‑level history, and guarantees that the trainer optimizes against the exact context the behavior policy experienced.

### Key Concepts  

| Term | Definition | Why it matters |
|------|------------|----------------|
| **Tokenizer** | Deterministic mapping from text to integer token IDs (and back). Each model has a fixed tokenizer; even tiny formatting changes can alter the token sequence. | Guarantees that the model’s internal representation matches the trainer’s data. |
| **Retokenization Drift** | Divergence caused by re‑tokenizing already‑generated text (e.g., after a whitespace change). | Leads to mismatched token IDs, corrupting the RL update. |
| **Chat‑Template Drift** | Shift in token IDs due to changes in the surrounding prompt template that wraps role‑messages. | Same visible text, different token stream → training signal loss. |
| **Rollout** | One complete attempt at a task, including prompt, tool calls, model responses, and final outcome. | The atomic unit of RL data; must be token‑accurate. |
| **Behavior Policy** | The specific model version that generated a rollout. | RL updates compare the policy’s actions to rewards; version tracking is essential when weights change mid‑rollout. |
| **Loss Mask** | Binary mask indicating which tokens are model‑generated (trainable) versus user‑ or system‑provided (non‑trainable). | Prevents the trainer from back‑propagating on irrelevant tokens. |
| **Turnstile Proxy** | HTTP‑level interceptor that forwards requests to the backend while logging token‑level details. | Provides a universal, harness‑agnostic data pipeline. |

### Practical Applications  

1. **Plug‑and‑Play RL for Existing Harnesses**  
   - Harnesses such as **OpenHands**, **Codex**, or **Terminus** can remain unchanged; they simply point their Chat‑Completions endpoint to Turnstile.  
   - Turnstile automatically splits or merges trajectories based on whether the next request is a faithful token‑level continuation.

2. **Stable Policy‑Gradient Training**  
   - By feeding exact token IDs and log‑probs, the trainer’s gradient computation aligns perfectly with the behavior policy’s experience, eliminating hidden drift.  
   - Supports asynchronous weight updates: the `TrainingSequence` records weight‑version boundaries, allowing correct credit assignment.

3. **Framework‑Neutral Data Export**  
   - Turnstile’s output can be adapted to any RL library (e.g., PPO, DPO, offline RL). The only required step is attaching rewards and reshaping masks.

4. **Multimodal Agent Support**  
   - The proxy records token sequences even when the rollout includes image embeddings or other modalities processed by the backend, ensuring end‑to‑end consistency.

5. **Research and Diagnostics**  
   - Precise token logs enable fine‑grained analysis of failure modes (e.g., where a tool‑call JSON formatting caused drift) and facilitate reproducibility of RL experiments.

### How Turnstile Works (Simplified Flow)

1. **Harness → Turnstile**: Sends a Chat‑Completions request (list of messages).  
2. **Turnstile → Backend**: Forwards request, receives streamed token IDs, log‑probs.  
3. **Capture**: Stores token IDs, per‑token log‑probs, loss mask, and model‑version timestamps.  
4. **Rollout Completion**: Harness queries Turnstile for the accumulated `TrainingSequence`.  
5. **Training Stack**: Receives the trajectory, attaches reward, and performs policy‑gradient update.

### Benefits Over Traditional Logging  

| Traditional Harness Logging | Turnstile Proxy |
|-----------------------------|-----------------|
| Stores only human‑readable text; token reconstruction required → error‑prone. | Captures token IDs at generation → exact representation. |
| Requires harness‑specific instrumentation to emit log‑probs and masks. | Works with any standard OpenAI‑compatible harness, no code changes. |
| Drift can silently degrade learning; hard

---
*Source: [raw/amazon-science-token-ids-agentic-rl-2026.md](../raw/amazon-science-token-ids-agentic-rl-2026.md) · Generated by wiki_llm.py (Groq)*
