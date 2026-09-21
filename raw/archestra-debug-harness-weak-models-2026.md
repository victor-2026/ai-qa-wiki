# Archestra: We Debug Our AI Harness on Weak Models on Purpose (2026-07-20)

**Author:** Arseny Kravchenko (Founding AI Engineer, Archestra)
**Source:** https://archestra.ai/blog/we-debug-our-ai-harness-on-weak-models-on-purpose
**Context:** How Archestra benchmarks its AI harness (Archestra Chat) on weak/cheap models to find bugs strong models hide. Nightly 26-task benchmark across ~10 models, public in monorepo `ai-labs`.

---

## TL;DR

Strong models are excellent at hiding product bugs — give one a broken tool call, it may still finish the task. Weaker models fail quickly when tools/prompts/runtime are wrong → useful for debugging. Think: test your app on an old ThinkPad, not a maxed-out MacBook Pro. They run Archestra Chat on weak models on purpose, record full trajectory, investigate failures → found defects in file handling, sandbox tooling, provider schemas, agent runtime. Bonus: a 26-task nightly benchmark across ~10 models answers "how far down the price ladder can we go before the assistant stops doing useful work."

## The MacBook/ThinkPad metaphor

- Premium AI models = maxed-out MacBooks: they bulldoze through bad plumbing (malformed tool call, confusing error, missing fallback) and make the product look healthier than it is. The model works around the bug, benchmark comes back green, you learn nothing.
- Weak models = old ThinkPad: they don't self-heal, they trip over anything slightly wrong, immediately and loudly → show you exactly what to fix. "The weak models are a better smoke alarm precisely because they're worse at compensating for our mistakes."
- Software that survives the old ThinkPad runs well everywhere. A model that compensates for bugs is still paying for them in retries, tokens, latency, fragility. Hardening against weakest models = stop taxing the strongest ones. "The test method and the business goal turn out to be the same thing."

## Benchmark design (two pillars)

1. **Answer submitted through a dedicated channel that checks FORMAT, not correctness** (rejects text if number expected, etc.). Correctness checked only after submission, by **deterministic code, not another LLM**. Grader and expected answer HIDDEN from the agent during the run — agent can't read the answer key, so score means something. `submit_result` never tells the agent whether it was right — only whether JSON parsed against task schema. Ground truth never staged into the sandbox.
2. **Record the entire visible trajectory**: every message, tool call, file touched, artifact. Turns "it failed" into "here's exactly where it failed" — "the difference between a number that shames you and a report you can actually use."

## Tasks: from reality, permanent tripwires

- Real customer workflows / real incidents, lightly anonymized.
- Once a task goes in, it stays in — a **permanent tripwire** for that failure mode.
- Examples: document workflows (approve invoices, shortlist CVs, reject hidden prompt injections + inconsistent data), incident triage (find outage cause in zip of unsorted logs with red herrings), memory across conversations (create file in one convo, retrieve in new one), live facts (repo star count, asset price, latest package version).
- Hard boundary: difficult but solvable with tools Chat actually has. "We're not measuring whether a model can do frontier physics." The useful failure mode: "The product should have been able to do this, but didn't."
- Not a mock benchmark — boots the real product: fresh backend on new port, fresh database, seeds providers/skills/MCP servers, drives real chat sessions, grades out of band, tears down.

## The analyzer (benchmark vs root-cause separated)

- After ~10 identical failures, built a separate analyzer on the recordings: map-reduce, summarizes what *appears* to have gone wrong, groups similar failures, points engineers to relevant parts.
- **Benchmark never tries root cause; analyzer never runs the product.** Kept separate so a human can use the analyzer's leads without trusting them blindly. Human still reviews trajectory, traces source, confirms, decides. "That human step is what turns 'the benchmark failed' into a real product improvement instead of an automated blame machine."

## Real bugs found in one week (representative)

| Area | What broke | Fix |
|---|---|---|
| File handling | Binary uploads crashed the LLM request | Keep files as sandbox references, don't inline unsupported MIME (#5623) |
| Sandbox output | Command printing binary with NUL bytes crashed Postgres persistence | Strip NULs before saving; warn models not to stream raw binary to stdout (#5697) |
| Sandbox tools | Incident tasks arrive as zips, but image lacked zip/unzip | Add zip/unzip (#5707) |
| Agent runtime | Some rollouts repeated same tool call hundreds of times until no answer | Detect loops, stop at fixed ceiling (#5756, #5786) |
| Provider backend | finish_reason string not in API schema, trajectory playback failed | Preserve arbitrary provider finish reasons (#5780) |
| Benchmark harness | Shared lanes + DB connectivity mixed product failures with harness noise | Dedicated Postgres, isolate lanes, explicit file conflicts, transient auth ≠ fatal (#5749, #5787) |
| Sandbox engine | Panic poisoned backend; orphaned child processes hammered engine | Retry panic, respawn session, reap children, keepalive checks (#5797, #5801) |

"Unit and integration tests remain necessary, but they rarely exercise files, tools, sandboxes, provider quirks, and persistence in one path, and do not bring enough variance to cover a non-deterministic system."

## Open-weight vs frontier results (26 tasks, nightly, ~17 models)

| Model | Pass rate | Swing (pp) | Suite cost |
|---|---|---|---|
| Claude Sonnet 5 | 100% | single run | $19.95 |
| Claude Opus 4.8 | 96% | single run | $27.60 |
| GPT-5.6 (sol) | 96% | single run | $7.50 |
| GPT-5.6 (terra) | 96% | single run | $3.93 |
| Qwen3.7 Plus (OW) | 94% | ±2 | $0.57 |
| Sakana Fugu-Ultra | 92% | single run | $27.69 |
| GLM-5.2 (OW) | 91% | ±7 | $1.23 |
| DeepSeek V4 Flash (OW) | 88% | ±7 | $0.34 |
| Claude Fable 5 | 88% | single run | $46.17 |
| Xiaomi MiMo v2.5 (OW) | 86% | ±4 | $0.27 |
| Qwen3.6 27B (OW) | 85% | ±4 | $1.19 |
| GPT-5.6 (luna) | 81% | single run | $1.62 |
| Qwen3.6 35B-A3B (OW) | 71% | ±10 | $0.82 |
| Claude Haiku 4.5 | 68% | ±6 | $7.82 |
| Gemma 4 31B (OW) | 45% | ±8 | $0.57 |
| GPT-5.4 nano | 12% | ±6 | $0.37 |
| GPT-5.4 mini | 9% | ±3 | $0.90 |

(Swing = std dev across 7 daily runs Jul 3-9; 26 tasks → each task ≈ 4 points. Focus on ranges, not decimals.)

Three findings:
1. **Strongest open models overlap the frontier tier** — cheapest in range $0.34/run vs $20-28/run frontier.
2. **Below ~70% the wheels come off entirely.**
3. **Price and capability don't follow the same order** — one brand-name mid-tier ($7.82) scores below five open models costing $0.27-$1.23.

Outlier: Qwen3.6 35B-A3B scored 58%-88% across the week on the same tasks — a single-run benchmark would have hidden that instability.

Takeaway: "Stop asking, 'Which premium model should we buy for everyone?' Ask, 'What's the cheapest model that can still handle our actual work?'"

## Where it's going

- Suite is 26 tasks (enough to see broad ranges, small enough one task = 4 pts). Growing from real customer problems.
- Next: release gates, better regression reports. Harder: orchestration — help smaller models approach larger ones WITHOUT hiding problems behind retries/tokens.
- Public harness in monorepo `archestra-ai/archestra` → `ai-labs`.

---

## Cross-references (in this wiki)

- `wiki/archestra-jev-100-agent-calls-benchmark-2026.md` — same author, same benchmark culture (77% constant trap, judge hidden)
- `wiki/archestra-crab-bot-slack-agent-2026.md` — night runs / agent in production
- `wiki/archestra-skills-aren-t-prompts-code-sandbox-2026.md` — same company, sandbox lineage

## Relevance to VerdictGate / Article series

- **Debug harness on weak models on purpose** = MUTATION-MATRIX intuition formalized at the harness level: break the harness first, then trust green runs. Our fault-injection / mutation testing philosophy verbatim.
- **Hidden ground truth + format-only submit channel + deterministic grader (no LLM judge)** = exact recipe for honest evals; anti "model grades its own homework" (Article 26/27).
- **Trajectory >> score** ("number that shames you vs report you can use") = evidence-pack principle; the analyzer/human loop = attestation (Reviewer of record).
- **Price/capability disconnect + open-weight overlap + instability hidden by single-run** = vendor-independent model selection; publish the benchmark, steal the good bits.
- **"The test method and the business goal are the same thing"** — strong closing line candidate.