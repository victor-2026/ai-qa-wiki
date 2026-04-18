# Agentic Patterns

**Last Updated:** 2025-04-15
**Sources:** raw/ap-*, raw/pipeline-triad, raw/infinite-midwit, raw/comprehension-debt

---

## What Makes an Agent

An agent is an AI system that:
1. Uses tools (not just generates text)
2. Operates over multiple steps
3. Maintains state/memory
4. Can reason and plan

**vs Chat:** Chat = Q&A. Agent = takes actions.

## Core Agentic Design Patterns (Gulli)

### 1. Prompt Chaining
Break complex tasks into sequential steps.

```
Task → Step 1 → Step 2 → Step 3 → Output
        (LLM)    (LLM)    (LLM)
```

**Use when:** Task has clear sequential dependencies.

### 2. Routing
Conditional logic based on input type/category.

```
Input → Classifier → Route A / Route B / Route C
                        (Specialized handlers)
```

**Use when:** Different inputs need different handling.

### 3. Parallelization
Execute independent tasks simultaneously.

```
Task A ─┐
Task B ─┼─→ Aggregate → Output
Task C ─┘
```

**Use when:** Tasks don't depend on each other.

### 4. Tool Use
Agents use external tools (curl, git, APIs).

**Essential tools:**
- Web search
- File system
- Code execution
- API calls
- Database queries

### 5. Memory Management

Two types:
- **Short-term:** Current conversation context
- **Long-term:** Persistent knowledge across sessions

**Challenge:** What to remember vs forget?

### 6. Reflection
Agent critiques own outputs before returning.

```
Output → Self-review → Refined output
```

**Why:** LLMs can't self-correct reasoning (ICLR 2024). External critique needed.

## Pipeline Triad Pattern

Production-ready agentic workflow:

```
Creator ──→ Critic ──→ Arbiter
    ↑                      │
    └──────────────────────┘
         (Feedback loop)
```

**Creator:** Generates code/output
**Critic:** Finds problems, validates
**Arbiter:** Makes decisions (PASS/FAIL/PARTIAL)

### Full SDLC Pipeline

```
Idea → [Analytics] → [Development] → [Testing] → [Security] → Deploy
        ↑ Human      ↑ Human        ↑ Human    ↑ Human
        Gate         Gate           Gate      Gate
```

**Economics:** ~1 hour human, ~$6-12 API per task

## Agentic Testing Implications

### Objective vs Subjective Intelligence

| Objective (AI Can Do) | Subjective (AI Cannot) |
|----------------------|----------------------|
| Bounded problems | Ill-defined problems |
| Verifiable solutions | "Is this interesting?" |
| Factual recall | "Does this matter?" |
| Code generation | Writing with soul |

> "The universe is not governed by Settlers of Catan rules"
> — you can't trade 4 objective points for 1 subjective point

### Comprehension Debt

When AI generates code team doesn't understand:

**Symptoms:**
- Verbose PR descriptions
- Testing syntax, not logic
- Context rot (understanding fades)
- Weak ownership

**Mitigation:**
- Atomic commits
- Human review before merge
- AI-augmented review
- Clear documentation

## Key Principles

1. **One agent, one job** — keep agents focused
2. **Self-containment** — agents should be testable in isolation
3. **Git verification** — version control for agent outputs
4. **Session scopes** — manage context window carefully
5. **Least privilege** — agents only access what's needed

## Anti-Patterns

1. **God agent** — trying to do everything with one agent
2. **No error handling** — agents fail silently
3. **Infinite loops** — no max iterations
4. **Context overflow** — feeding too much data
5. **No rollback** — can't undo agent actions

## Security Considerations

- Prompt injection via retrieved context
- Data leakage through tools
- Unauthorized access via agent permissions
- Hallucinated commands

## Related

- [[wiki/mas-testing-framework]] — MAS-Testing Framework (новое!)
- [[wiki/testing-strategies]] — Testing agentic workflows
- [[wiki/vibe-wipe-coding-guide]] — Where agents fit in dev
- [[wiki/ai-testing-metrics]] — Measuring agent quality

## Sources

- raw/ap-01..09 (Agents Playbook)
- raw/pipeline-triad-pattern.md
- raw/infinite-midwit.md
- raw/comprehension-debt.md
- arxiv 2603.24160v1 (MAS-Testing)
- arxiv 2603.23448v1 (LLM Agents Benchmark)
