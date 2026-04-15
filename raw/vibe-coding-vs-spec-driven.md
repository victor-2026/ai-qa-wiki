**Source:** [RedMonk - Rachel Stephens](https://redmonk.com/rstephens/2025/07/31/spec-vs-vibes/)
**Date:** 2025-07-31
**Author:** Rachel Stephens

---

# Vibe Coding vs. Spec-Driven Development

## The Problem with Vibe Coding at Scale

Vibe coding tools are great for early exploration but fall short for production systems:

- **Not efficient** — not neat, maintainable, or reusable code
- **Hard to debug** — tricky debugging
- **Performance problems** — e.g., `select *` queries
- **Unreliable behaviors** — catastrophic failures possible
- **Shifts bottlenecks** — from writing to debugging, testing, deployment

"There's a chasm to cross from magical prototypes to maintainable, deployable systems."

## Spec-Driven Development

Spec-driven development captures requirements **before** writing code. Instead of jumping to code, the user augments AI context with structured specifications.

### Example (from Kiro IDE)

**Vibe Coding:**
```
Prompt: "I want to build a personal website..."
AI jumps straight to writing code, suggesting tech stack
```

**Spec-Driven:**
```
Prompt: "I want to build a personal website..."
AI creates markdown documents with user stories and design first
User can edit, add, remove requirements
Requirements captured in living document
```

## Key Concepts (Kiro)

- **Specs** — structured requirements documents
- **Steering** — rules agents follow before responding
- **Agent Hooks** — offload tasks (e.g., run unit test on commit)

## Vibe Coding vs Spec-Driven

| Aspect | Vibe Coding | Spec-Driven |
|--------|-------------|------------|
| **Nature** | Speculative, exploratory | Structured, intentional |
| **Artifacts** | Ephemeral prompts | Living documents |
| **Collaboration** | Dev + AI only | Wider team access |
| **Context** | Lost in chat history | Captured in specs |
| **Intent** | Abstract reasoning | Documented "why" |

## Key Insight: Source of Intention

> "Specs aren't the source of truth. The source of truth is what builds. The code is the source of truth."

Specs are better called "**source of intention**" — they capture why code was built, not just how.

## Not Either/Or — Yes And

- **Vibe coding** — unlocks momentum, spark, get unstuck, test ideas
- **Spec-driven** — slows down to think clearly, captures context, creates lasting artifacts

Both have their place. Vibe coding for prototyping. Spec-driven for production.

## For QA/Testing

Spec-driven development creates artifacts useful for:
- Test case generation from specifications
- Traceability from requirements to tests
- Better understanding of system intent
- Improved collaboration with dev team

## Related

- Hidden Costs of Vibe-Coded Apps (Diffian)
- Comprehension Debt
- Infinite Midwit (objective vs subjective)
- Pipeline Triad Pattern
