---
title: "Agent Teams Architecture"
type: article
updated: "2026-08-17"
tags: [agents]
---

# Agent Teams Architecture

## Concept

Agent Teams = Multiple AI agents working together with defined roles, where one agent can check/verify the work of another before passing it forward.

```
Agent A (Generator) → Agent B (Critic) → Output
     ↑                    ↑
  "Write code"      "Verify code"
```

## Why Agent Teams?

| Problem | Solution |
|---------|----------|
| Single agent makes mistakes | Second agent catches errors |
| No quality gates | Adversarial checking |
| Blind spots | Different perspectives |
| Consistency issues | Defined roles and responsibilities |

## Architecture Patterns

### 1. Sequential Pipeline

```
[Generator] → [Reviewer] → [Approver]
   Creates      Checks       Final OK
```

**Use case:** Code generation → review → merge

### 2. Parallel Verification

```
[Agent A] ──→ [Both Pass?] ──→ Output
     ↕
[Agent B] ──→ [Consensus?]
```

**Use case:** Two agents verify same thing independently, require agreement.

### 3. Hierarchical (Supervisor Pattern)

```
     [Manager Agent]
         ↑
    ┌────┼────┐
    ↓    ↓    ↓
[Worker][Worker][Worker]
```

**Use case:** MiniMax Agent Teams, multi-task processing.

### 4. Adversarial (Quality Gates)

```
[Agent A] → [Agent B adversarial] → [Pass/Fail]
           ↑
       "Find flaws"
```

**Use case:** Our MAS workflow, security testing.

## Model Selection

### Fast + Slow Combination

| Role | Model | Purpose |
|------|-------|---------|
| Generator | llama-3.1-8b | Quick draft |
| Reviewer | llama-3.3-70b | Deep check |
| Critic | Claude 3.5 | Nuanced review |

**Benefits:**
- Cost optimization (fast for simple, slow for complex)
- Speed for bulk tasks
- Quality for critical paths

## Implementation Options

### Option 1: Same Model, Different Prompts

```python
# Same Groq 70B, different roles
generator_prompt = "You are a code generator. Write clean tests."

critic_prompt = "You are a code reviewer. Find bugs and issues."
```

**Pros:** Single API, consistent quality
**Cons:** Same blind spots

### Option 2: Different Models

```python
generator = Groq70B(role="writer")
reviewer = Claude35(role="critic")
```

**Pros:** Complementary strengths
**Cons:** Multiple APIs, different costs

### Option 3: Orchestration Layer

```
[Orchestrator]
    ↓
[Agent Pool] → [Assignment] → [Results]
```

Tools: LangGraph, CrewAI, AutoGen, MiniMax Agent

## Quality Gates

### Automatic Checks

| Gate | Question |
|------|----------|
| Syntax | Does code compile? |
| Style | Follows conventions? |
| Logic | Does it work? |
| Security | Any vulnerabilities? |
| Tests | Is it testable? |

### Human-in-the-Loop

- Agent A → Agent B → **Human Approval** → Deploy
- Only proceed if both agents agree
- Escalate disagreements

## Our MAS Implementation (Current)

```
Groq 70B → MAS Analysis → Score + Issues
```

Single model acting as both generator and critic (through different prompts).

## Proposed Enhancement

```
Groq 8B (Fast) → Initial Analysis
     ↓
Groq 70B (Deep) → Quality Check
     ↓
Claude 3.5 → Final Review
     ↓
Human → Decision
```

### Benefits for qa-automation-sandbox

- **Faster feedback** for simple tests
- **Thorough review** for complex scenarios
- **Cost balanced** allocation
- **Better coverage** through adversarial pairs

## Tools to Watch

- [MiniMax Agent](https://agent.minimax.io) - Agent Teams built-in
- [LangGraph](https://langchain.github.io/langgraph/) - Orchestration
- [CrewAI](https://crewai.com) - Role-based agents
- [AutoGen](https://microsoft.github.io/autogen/) - Multi-agent

## Related

- [[mas-testing-framework]]
- [[agentic-patterns]]
- [[perplexity-agent-skills]]

---

**Tags:** #agent-teams #multi-agent #orchestration #quality-gates
**Status:** Research only, not implemented
**Updated:** 2026-05-14