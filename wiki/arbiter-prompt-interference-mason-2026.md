# Arbiter: Interference in Coding-Agent System Prompts (Mason 2026)

**Source:** Tony Mason (UBC/Georgia Tech), "Arbiter: Detecting Interference in LLM Agent System Prompts — A Cross-Vendor Analysis", v2 Oct 2026 (v2 corrects three method statements; Feb-2026 prompt measurements unchanged). Raw: `raw/2603.08993v2.pdf` (19pp). Targets: Claude Code, Codex CLI, Gemini CLI system prompts (245–1,490 lines). Total cross-vendor cost: **$0.27**.

## Thesis: system prompts are untested software

System prompts govern agent behavior yet lack the testing infrastructure of conventional software. Arbiter = formal evaluation rules + multi-model LLM scouring to detect interference patterns.

## Directed phase: prompt archaeology (Claude Code v2.1.50)

56 blocks classified (tier × category × modality × scope). Five rules: mandate-prohibition conflict, scope-overlap redundancy, priority-marker ambiguity, implicit dependency, verbatim duplication. Structural rules run as Python predicates (zero LLM cost); pre-filtering cuts ~15,680 pairs to 100–200.

21 patterns found: **4 critical direct contradictions** (TodoWrite "ALWAYS use" vs commit/PR "NEVER use" — model must violate one), 13 scope overlaps (same constraint restated 2–3× with drift), 2 priority ambiguities, 2 implicit dependencies (plan-mode dead zone). **20/21 (95%) statically detectable** — a scope/modality compiler catches them with no LLM.

## Undirected phase: multi-model scouring

Deliberately vague prompt ("not auditing... just reading... trust your judgment"). Findings self-rated on epistemic scale: curious / notable / concerning / alarming. Map-passing (later passes get prior findings + unexplored territory), different model per pass — goal is **complementarity, not consensus**. Convergent termination: three consecutive models decline. 152 findings total (116 Claude + 15 Codex + 21 Gemini).

## Architecture ↔ failure class

Monolithic prompts → growth-level bugs at subsystem boundaries; flat prompts → capability-for-consistency trades; modular prompts → design-level issues. Architecture correlates with failure *class*, not severity. One scourer finding (structural data loss in Gemini CLI memory) independently confirmed — Google patched the symptom, not the schema root cause.

## Honesty notes (v2, author-audited)

Stopping criterion applied in full to Claude Code only; no per-finding human verdicts recorded (fabrication mitigation claimed in v1 did not run); multi-model-complementarity is a hypothesis (non-repetition instruction confounds it, no same-model control). Corrections from external review + stored campaign data.

## QA interpretation

- **95%-static is the headline:** prompt interference is mostly a lint problem, not a judgment problem — same lesson as deterministic-checks-first (AQEF rule 2).
- **Epistemic severity > confidence scores:** curious→alarming admits uncertainty instead of fake-calibrating it — pairs with abstention verdicts.
- **Complementarity-not-consensus** is the diverse-judges doctrine in another field (window-discipline rule 9).
- **$0.27 cross-vendor analysis** sets the cost bar for pre-merge prompt checks: cheap enough to run every time.
- **Patched-symptom-not-cause** (Gemini memory) is the observational-only fix pattern — our mutation-matrix "observed-only ≠ caught" in vendor reality.

## See also

- [[anthropic-claude-code-expertise-2026]] — 70/20 split, fixing-rate collapse
- [[forms-llm-integrated-applications-weber-2026]] — copilot vs agent test scope
- [[aqef-seeded-controls-spec-2026]] — deterministic checks first, judge second
