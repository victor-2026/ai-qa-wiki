# Engineering Standards for AI-driven development: rmorison/engineering-standards + EveryInc Compound Engineering

**Author:** Rod Morison (Technology Executive, LinkedIn post 2026-09-21)
**Source:** https://github.com/rmorison/engineering-standards + https://github.com/EveryInc/compound-engineering-plugin
**Fetched:** 2026-09-21
**License:** MIT (both)

---

## Part 1: rmorison/engineering-standards (7 stars)

Lightweight AI-forward engineering standards for startups and solo projects "where the AI is the team". Dogfooded recursively by the AI review workflow they document.

### Six-Layer AI Architecture (ai/claude-code/README.md)

The abstraction: AI tooling integrates with SWE workflows in 6 layers. Vendor-neutral baselines live in the repo; toolkits (most concretely Compound Engineering) fill layers as canonical realizations.

| Layer | Principle | Vendor-neutral baseline |
|-------|-----------|-------------------------|
| 1 Rules | Persistence - always-loaded session context | ai/claude-code/rules/ |
| 2 Workflow Skills | Composability - multi-step orchestrators | templates/.claude/skills/ |
| 3 Persona Agents | Perspective - multiple expertises | templates/.claude/agents/ |
| 4 References | Progressivity - context grows with workflow depth | (none yet) |
| 5 Compound / Learnings | Compounding - institutional knowledge accumulates | (none yet) |
| 6 Hooks | Determinism - non-AI enforcement at zero context cost | templates/.claude/hooks/ |

CE fills Layers 2-5. Layers 1 (rules) and 6 (hooks/determinism) stay owned by the project's .claude/. ADR-0001 documents the decision.

Core principle: "Context is expensive - only load what's needed, when it's needed. The six layers each specialize this for a different context-cost slot."

### Process standards

- Documentation standards: docs/ is source of truth; specs before code; ADRs; decisions and context over implementation detail.
- Feature development workflow: Product Concept → Requirements & UI Design → Project Planning & Sequencing → Technical Design → Implementation → Validation & Iteration. "Intent → Spec → Plan → Execute → Validate. Small scoped changes, continuous validation, spec-driven development."
- GitHub Flow: main always deployable, issue-based branches, conventional commits, semantic versioning.
- Issue tracking: Milestones (initiatives) → Epics (feature themes) → implementation issues; native GitHub sub-issues, label strategy.
- Technical work workflow: bug fixes, tech debt, infra, security - separate from product feature work.

### Philosophy

- Lightweight not heavyweight; deviate when standard adds no value (document why in commit message).
- Spec-driven development: specs clarify intent, enable AI-assisted dev with clear context, serve as contracts for testing and validation. Code implements the spec.
- AI-native: "Clear specs give AI better context. Small scopes reduce AI errors. Validation catches AI-generated bugs. Iteration is cheaper with AI assistance."

## Part 2: EveryInc/compound-engineering-plugin (25.2k stars, MIT)

"AI skills that make each unit of engineering work easier than the last." 36 skills, 14 agent hosts (Claude Code, Cursor, Codex, Kimi, Cline, Grok, Devin, Copilot, Qwen, OpenCode, Pi, omp, Antigravity). Maintained by Kieran Klaassen and Trevin Chow.

### The loop (six steps)

brainstorm → plan → work → simplify → review → compound → repeat with better context.

- ce-brainstorm: interactive Q&A → requirements-only plan
- ce-plan: to implementation-ready plan
- ce-work: execute natively or through a qualified cross-model author
- ce-simplify-code: refine before review
- ce-code-review: report-only multi-agent review against the plan before merging; local apply explicit
- ce-compound: capture learning into docs/solutions/ so next loop starts smarter

"80% is in planning and review, 20% is in execution." The return arrow (compound → next brainstorm/plan) is the whole point: "Each unit of engineering work should make subsequent units easier - not harder. Run one teaches it. Run two remembers."

Example: a ce-compound run writes a learning about an env-var trap; 18 days later, on unrelated work, a ce-plan run finds that learning and carries its constraints into the new plan.

### Key design elements

- ce-explain: understand existing behavior before changing (why it exists).
- ce-pov / "oracle this": independent model opinions contributing to a workflow.
- Compound Packs (experimental): folders of prescriptive rules (local or ref-pinned git repos) that planning grounds in and review enforces, every use cited back to the rule file.
- lfg: hands-off autonomous pipeline - plan/work/simplify/review/compound, browser tests, commit, push, PR, watch CI with bounded repair loop (does not merge unless granted).
- Docs default artifact folders: docs/solutions/, docs/plans/ (configurable via docs_root).
- OpenCode install: plugin array in opencode.json (git+https URL), registers skills directly.

## Relevance notes

- Six-layer architecture = analog of Victor's split: AGENTS.md (Rules) → skills (Workflow) → subagents (Persona) → global memory (Compound/Learnings) → hooks (determinism). Compounding knowledge = forced institutional memory, like wiki layer for AI.
- CE code-review-against-plan = checklist/review-as-gate pattern; ce-compound = "answers go back to wiki" pattern.
- Spec-driven development: spec as contract for testing/validation → mutation testing reads spec as oracle. BDD/Gherkin analog.
- CE = canonical realization of abstraction; vendor-neutral baselines remain. Aligns with vendor-independence theme (Zalando wiki, Article 26).