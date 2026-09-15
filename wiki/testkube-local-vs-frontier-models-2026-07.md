# Local vs Frontier Models for Test Analysis — Testkube (2026-07-29)

**Source:** Sonali Srivastava (Tech Evangelist, Testkube) https://testkube.io/blog/local-vs-frontier-models-test-analysis — Failure Categorization Agent on Ollama/Qwen vs GPT-5.2, Troubleshoot Agent escalation.
**Use for us:** independent validation of our free-first + fallback + tiered-thinking architecture (openrouter/free → paid, maxSubagentSpawns 3, thinking caps).

## Doctrine (theirs = ours)

- **Local first-pass, frontier escalation:** local model classifies high-volume clear-signal failures ($0, private, fast); frontier Troubleshoot Agent only on ambiguous multi-layer cases (~$0.005/case in their example).
- **Separate prompts per tier:** local = pattern matcher (constrained prompts, fixed labels, examples); frontier = reasoner (open analysis). Same request ≠ same prompt. Matches our hint-engineering split (explore hints vs run plan text).
- **Trade table (10 dims):** reasoning depth, best fit, cost, residency, prompt control, latency, context, ops overhead, remediation quality, hybrid role. Key rows for us: residency (logs never leave cluster — our local-first Desktop narrative), remediation (local = known fixes, frontier = nuanced RCA).
- **Cost honesty:** local isn't free (infra/hosting/scaling), frontier burns tokens "faster than you realize" — hybrid optimizes both.

## Mapping to our stack

- openrouter/free first, 429 → paid fallback = their hybrid with different vendors.
- maxSubagentSpawns 3 + thinking caps = their "route to appropriate agent" on a budget.
- Agentiqa managed-Gemini-only on Starter = anti-pattern by their doctrine (no local tier, no escalation choice) — worth one line in vendor comparison.

## Links

- Sibling pieces: four-layers (orchestration), smart-suites (selection), delivery-pipelines (thresholds)
- Our mapping: AGENTS.md free-first section, openrouter-guard.sh, context-engineering skill
