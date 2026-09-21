---
source: "archestra-jev-100-agent-calls-benchmark-2026.md"
ingested: "2026-09-22"
---

## Archestra – Benchmarking Jev on 100 Real‑World Agent Calls (Sept 2026)

**Author:** Arseny Kravchenko, Staff AI/ML Engineer  
**Source:** https://archestra.ai/blog/we-tested-jev-on-100-real-agent-calls  

### TL;DR  
A head‑to‑head test of the Jev classifier against Anthropic Sonnet 5, several open‑weight models, and a naïve “always‑benign” baseline was run on 100 tool‑call traces extracted from production Claude‑Code sessions.  

* **Accuracy:** Jev reached 93 % zero‑shot and 95 % with a 9‑shot prompt; Sonnet 5 scored 98 % but all of its 8 mistakes were *leaks* (dangerous calls marked safe).  
* **Speed & cost:** Jev answered in ~300 ms per call, costing $0.37 for the whole set.  
* **Confidence:** Jev’s calibrated scores allowed safe routing (confidence ≥ 0.7 ⇒ zero errors). Open‑source decoders produced flat logits and unusable confidence.  
* **Pitfall:** 79 % of the dataset carried the default “benign” label, so a constant classifier already hits 79 % accuracy—making raw accuracy a misleading metric.

---

## 1. Problem Context  

OpenAPPA protects a security boundary by annotating each tool invocation with four binary attributes:

| Attribute | Meaning |
|-----------|---------|
| **delta_audience** | Who may see the tool’s output (self / internal / public) |
| **delta_trust** | Whether the output is trusted or suspicious |
| **requires_audience** | Who must be allowed to receive data sent by the call |
| **requires_trusted** | Whether the call should be blocked if the session already contains untrusted data |

If the classifier mislabels a dangerous call as safe, the system will permit a data leak.

### The “79 % constant trap”  
Because routine calls dominate real traffic, a trivial classifier that always returns the default “benign” label scores 79 % accuracy. Any model that does not significantly exceed this baseline is practically useless for security.

---

## 2. Benchmark Design  

| Component | Details |
|-----------|---------|
| **Input format (Jev)** | Structured JSON with a `state` (tool + arguments) and a list of typed questions (e.g., “delta_trust”). |
| **Models evaluated** | Jev (latest), Anthropic Sonnet 5, Qwen‑3‑Reranker‑4B, Laya (ModernBERT‑large), SemIf (Qwen 3.5‑4B & MiniCPM‑2B), Bespoke‑Nimble‑9B, plus a majority‑baseline. |
| **Decision space** | 100 calls × 4 labels = 400 binary decisions; 337 were retained after three‑judge consensus. |
| **Shot regimes** | Zero‑shot baseline and a 9‑shot prompt containing representative examples. |
| **Metrics** | Overall accuracy, *refusal recall* (ability to flag calls that require `requires_trusted`), and confidence calibration. |
| **Bias control** | Models were prevented from grading their own outputs; self‑grading inflated scores by 2–3 pts in earlier runs. |

---

## 3. Key Findings  

### 3.1 Accuracy & Security‑Critical Errors  

| Model | 0‑Shot | 9‑Shot | Refusal Recall |
|-------|--------|--------|----------------|
| **Sonnet 5** | 98 % | – | 44 % (4/9) |
| **Jev** | 93 % | 95 % | 78 % (7/9) |
| **Bespoke‑Nimble‑9B** | 83 % | 86 % | 33 % |
| **Constant baseline** | 79 % | 79 % | 0 % |
| **SemIf (Qwen 3.5‑4B)** | 63 % | 84 % | 78 % |
| **Qwen‑3‑Reranker‑4B** | 64 % | 75 % | 67 % |
| **Laya** | 48 % | 46 % | 100 %* |

\*Laya achieved perfect recall only by flagging *everything*, yielding 12 % precision.

**Leak vs. Stall** – Errors were split into *leaks* (false‑negatives) and *stalls* (false‑positives). Sonnet’s 8 errors were all leaks (e.g., missing outbound WebSearch queries), while Jev’s mistakes were a mix, with a higher proportion of stalls.

### 3.2 Confidence Calibration  

* Jev’s probability estimates were well‑behaved: predictions with confidence ≥ 0.7 incurred **zero** errors, enabling a practical “fast‑path / fallback” routing scheme.  
* Open‑source decoders produced near‑flat logits (max‑min ≈ 0.05), making confidence‑based filtering ineffective.

### 3.3 Position‑Order Sensitivity  

* Small encoder‑decoder models (Qwen 0.6B, MiniCPM‑2B) learned the option *position*, not the task: Qwen‑0.6B always chose “A”, MiniCPM‑2B always the last option. They failed all 100 permutation tests.  
* 9‑shot examples rescued the decoders (+20 to +34 pts; SemIf‑4B kept the correct answer in 92/100 order tests) but not the encoder‑based Laya (−2 pts; needs fine‑tuning instead).  
* Jev’s labels are reproducible (394–398 of 400 identical across identical repeats), but probabilities drift (median 0.01, worst 0.17) and ~4 of 100 decisions flip due to option order alone on 3‑way labels. No clean positional bias; flips cluster at near‑ties (within 0.02 of 0.50), with rare wild swings (0.83 → 0.48 under reorder).

---

## 4. Stalls vs. Leaks — the security angle  

Errors on a boundary have asymmetric cost:

* **Stalls (false alarms):** a safe call is blocked; inconvenient, rarely dangerous.  
* **Leaks (false negatives):** a dangerous call is allowed; data can leave the system. Severe.

Live examples:

* **Sonnet** missed *every* outbound search query (WebSearch, `slack_search_*`) — treated search as harmless *reading*, but the query string is an exfiltration channel if the session is poisoned. All 8 of its strict‑set errors were leaks.  
* **Reranker‑4B** over‑restricted 65 routine local commands to `delta_audience=self` (the paralyzing stall) — stricter is not always safer, because later calls lose the safe output.  
* **SemIf‑MiniCPM‑2B** produced 80 leaks / 337 decisions, flagging 58 internal file reads as public.

---

## 5. Methodology Lessons (the benchmark itself was wrong first)  

* The original 100‑call sample was ~90 % routine / ~10 % dangerous — a model scores well by labeling everything benign while missing the critical leaks. Evaluation datasets must *overrepresent the dangerous minority*.  
* Self‑grading inflates scores (models scored themselves 2–3 pts higher; Gemini gave itself 100 %). *Rule one of model evaluation: don’t let a model grade its own homework.*  
* Debug the harness on weak models on purpose — Laya stopping at 45 tokens and decoders always answering “A” exposed harness bugs, unclear prompts, and poor sampling that the strong model (Sonnet) silently worked around.

---

## 6. Takeaways for production  

* Beware public benchmark hype on out‑of‑distribution tasks; zero‑shot results on AG News / sentiment do not transfer to security tool contracts.  
* Inspect individual errors; judge disagreements exposed unclear rules, not unreliable models — the evaluation needed work too.  
* Jev is a promising *router*: ~300 ms, low cost, competitive with frontier LLMs on structured contracts; confidence ≥ 0.7 ⇒ zero errors makes confidence‑based escalation practical.  
* **Never rubber‑stamp a model on an execution boundary based on macro numbers alone — the overall score does not show whether it fails safely.**

---

## 7. Relevance to VerdictGate / Article series  

* **79 % constant trap** — an eval must beat a prior *constant* (default‑label baseline), not just random chance — identical to our golden‑dataset baseline discipline for VerdictGate.  
* **Stalls vs. Leaks** — false‑positive vs. false‑negative cost asymmetry; a *leak is a silent false negative* — the exact thesis of Articles 20/26.  
* **Don’t let a model grade its own homework** — quantitative evidence (2–3 pts inflation) for the “author ≠ examiner” principle at the core of attestation.  
* **Labels hold, probabilities drift** — verdict primitives are quasi‑deterministic: version‑stamp verdicts (SCORER_VERSION), treat confidence thresholds as fuzzy.  
* **Weak‑models‑first harness debugging** — the mutation‑matrix intuition: break the harness first, then trust green runs.

---

*Source: [raw/archestra-jev-100-agent-calls-benchmark-2026.md](../raw/archestra-jev-100-agent-calls-benchmark-2026.md) · Generated by wiki_llm.py*








<!-- backlinks-start -->
### Backlinks
- [Archestra Blog: Complete Publications Catalog with Annotations](wiki/archestra-blog-catalog-2026.md)
- [Archestra Crab Bot Slack Agent 2026](wiki/archestra-crab-bot-slack-agent-2026.md)
- [Archestra Skills Aren T Prompts Code Sandbox 2026](wiki/archestra-skills-aren-t-prompts-code-sandbox-2026.md)
<!-- backlinks-end -->
