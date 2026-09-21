# rmorison/engineering-standards — Six-Layer AI Architecture (MIT, 7 stars)

Source: https://github.com/rmorison/engineering-standards

## Summary
AI forward engineering standards with six-layer architecture for AI-assisted development:
- Layer 1: Rules (global constraints)
- Layer 2: Workflow Skills (reusable skills)
- Layer 3: Persona Agents (specialized agents)
- Layer 4: References (context docs)
- Layer 5: Compound/Learnings (accumulated knowledge)
- Layer 6: Hooks (automation triggers)

Principle: context is expensive, load only what you need. Mirrors our AGENTS.md → Pi → skills → memory stack.

Spec-driven development: specification is source of truth, "code implements the spec" — matches our "no vendor/written spec" principle.

Agent transcripts: logs of AI decisions for history (why-so).

Dogfooded: standards themselves prescribe AI review workflow that checks themselves.

## Relevance to Victor
Direct mapping to our stack: AGENTS.md (Rules) → Pi subagents (Persona) → skills (Workflow Skills) → wiki (References) → session-checkpoints/memory (Compound) → hooks/LaunchAgent (Hooks). Validates our current layering.

## Links
- Repo: https://github.com/rmorison/engineering-standards
- EveryInc compound: https://github.com/EveryInc/compound-engineering-plugin
