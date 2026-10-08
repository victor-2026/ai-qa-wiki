# Mike Peterson: A QE Perspective on Gen AI (Practitioner Intro, Oct 2026)

**Source:** Michael Peterson (Principal Software Quality Engineer), "A QE Perspective on Gen AI" — short practitioner guide, full text read 2026-10-07. Via Klain's AI Testing & Assurance group (Klain: "good general introduction"). URL: https://mikepeterson-git.github.io/qe-docs/qe-understanding-ai.html

## Core model (two consequences of next-word prediction)

Fluent ≠ correct; outputs are probabilistic, not deterministic. Agent self-reports ("I checked the logs") are plausible sentences, not process evidence — check the log/artifact, not the sentence. Continuity across turns is only as real as what was logged and passed back in.

## Memory taxonomy (7 types, each fails differently)

Working / Semantic / Episodic / Procedural / External / Parametric / Prospective. QE angle: truncation vs persistence failures, external = ordinary integration bugs. "Treating 'the agent's memory' as one thing misses all of this."

## Oracle = highest-risk use

"Does this output look correct?" combines two unverified things; same check can pass then fail with no code change. If unavoidable: pin model version, log full response — a pass becomes a lead, not a verdict. Generated test that never fails = its own easy-to-miss failure mode. Autonomous agents move verification to boundaries: authorization scope, per-action evidence logs, after-the-fact audit.

## Verification mindset (4 questions) + adoption checklist

Falsify? Checkable citation? Re-run stability? Cost of being wrong (scale review accordingly)? Checklist: run+inspect AI tests before suite entry; root causes vs raw log lines; no AI sole-oracle on release-blocking; log model+prompt; review assertions not execution; team knows what hallucination looks like HERE.

## QA interpretation

Practitioner-grade formulation of examiner≠author + oracle-as-range + boundary verification. Memory taxonomy is directly usable as a test-design input (per-type failure modes). Pairs with Kohl structural testing (mock+trace) and Ted "vibe-checking" line.

## See also

- [Anthropic Claude Code expertise study](wiki/anthropic-claude-code-expertise-2026.md)
- [[runtime-authorization-ai-agents-2026]] — authorization scope, audit afterward
- [[breaklight-ai-testing-methodology-whitepaper-2026]] — judge calibration, reference hygiene
- [[kohl-structural-testing-llm-agents-2026]] — trace/assert layer (соседняя страница другого окна)
