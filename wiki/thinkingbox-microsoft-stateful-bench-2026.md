# ThinkingBox: Microsoft Stateful Agent Bench (Oct 2026)

**Source:** Microsoft + Hugging Face joint blog (Tuhin Kundu et al., Oct 3 2026, full text read 08.10) + paper arXiv:2608.19741 (Aug 20). Code MIT (microsoft/thinkingbox), data CDLA-Permissive (thinkingbox-data v1.0), runnable via OpenEnv. URLs: https://huggingface.co/blog/microsoft/thinkingbox · https://arxiv.org/abs/2608.19741
**Via:** TestMu Coding Jag #316 (https://www.linkedin.com/pulse/agent-said-done-database-disagreed-testmu-ai-ps4uc/).

## Design

507 stateful business workflows (retail/insurance/travel/neobank/consulting), each run 20× from clean backend, isolated MCP sessions. Grading on terminal backend state + side effects via deterministic judges (477 state-only, 30 + response rubric). Trust boundary: model sees tasks/dialogue/schemas; golden state/assertions/credentials stay evaluator-side. Reproducible pins (framework commit + data release + bundle hash).

## Three metrics (report all, define each)

pass@1 (usually) / pass@20 (ever = breadth) / observed 20/20 (always, literal count, no smoothing). Findings: Opus 5.5 leads pass@1 (67.16%); Kimi-K3 broadest (93.89% ever, 476/507) but only 13.41% always; Opus 5 fewer-ever (79.09%) but 47.53% always (173 more consistent tasks than Kimi). Newer ≠ more dependable (5.5 vs 5: same 241 always-tasks). Retention: GPT-6 Astra 78%, Opus 5/5.5 71%, GLM/K2.6/DeepSeek-V4-Pro ~8%.

## Cost (OpenRouter Sep-20 snapshot, comparative index not invoice)

Cost per successful attempt (pass@1 denominator): GPT-5.6 Sol $0.127 → GPT-5.4 $0.131 → Opus 5.5 $0.276 (frontier). Cost per DEPENDABLE task (20-run campaign ÷ 20/20 tasks): GPT-5.4 $6.80 (128 tasks), GPT-6 Astra $7.45 (231), Opus 5.5 $7.80 (241). "The cheapest way to get a right answer is not the cheapest way to get a dependable one."

## Failure signatures + doctrine lines

Tool usage 79.9% / wrong state 10.3% / incomplete resolutions 7% / no state action 2.9% — "retry and error-recovery problem before model problem". 67.24% of failures terminated cleanly with no tool error; wrong values 77.61%, extra effects 43.30%, missing 25.36%. "A trajectory is a claim. Database state is the evidence. Repetition is the trust test." Production rule: "check the terminal state before you commit, not the model's summary"; human approval on irreversible changes.

## QA interpretation

- Strongest independent backup to date for: backend-state verdicts (not trajectories/replies), repeat-metrics (pass@1 vs always), cost-per-dependable economics (W2 ledger: cite with snapshot caveat), trajectory/response split (Hari/Igor/Goldshmidt threads).
- Runnable OSS harness = W3 pilot-adjacent (their call); dataset CDLA-permissive.
- ReviewBench self-grading note (same issue: Copilot tops GitHub's own bench; rivals tested by GitHub) = benchmark-gaming exhibit for Article 26.

## See also

- [[kenhuang-claude-eval-hillclimbing-note-2026]] — uncertainty at task level
- [[breaklight-ai-testing-methodology-whitepaper-2026]] — paired designs, run-to-run range
- [[igor-goldshmidt-trajectory-response-2026]] — trajectory vs response axes
- [[anthropic-spotify-quality-at-ai-speed-2026]] — cost-of-verdict economics
