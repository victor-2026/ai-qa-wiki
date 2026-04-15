# Prompt Engineering Summary

**Generated:** 2025-04-15
**Sources:** raw/winteringham-prompts.md, raw/qa-prompt-engineering-guide.md

---

## What is Prompt Engineering?

Prompt engineering = crafting inputs to get desired outputs from LLMs. For QA, it's about getting useful, accurate, testable results.

---

## Two Core Principles (Winteringham)

### Principle 1: Write Clear and Specific Instructions

| Tactic | Example |
|--------|---------|
| **Use delimiters** | ```Analyze: --- [code] ---``` |
| **Structured output** | "Return as JSON with fields X, Y, Z" |
| **Check assumptions** | "Identify any assumptions that could fail" |
| **Few-shot** | Provide examples: Input → Expected Output |

### Principle 2: Give the Model Time to "Think"

| Tactic | Example |
|--------|---------|
| **Specify steps** | "Step 1: X, Step 2: Y, Step 3: Z" |
| **Work out first** | "Don't jump to conclusions. First work through the logic..." |

---

## Prompt Structure (from DeviQA)

```
1. Frame the role        → "You are a senior QA engineer..."
2. Pack context         → Include specs, code, constraints
3. Specify output format → JSON, Markdown, table
4. Few-shot examples    → Demonstrate expected pattern
5. Self-checks          → "List any assumptions made"
```

---

## Prompt Patterns for Testing

### Test Case Generation
```
Generate test cases for: [feature]

Return in Markdown table:
| Test ID | Input | Expected Output | Priority |
```

### Risk Identification
```
Analyze requirements for risks:

[requirements]

Identify:
- Functional risks
- Non-functional risks
- Edge cases
```

### Code Analysis
```
As a senior tester, analyze this code:

[code]

Consider:
- What dependencies need mocking?
- Side effects?
- Testability score?
```

### TDD Loop
```
Help me practice TDD:

Step 1: Write a failing test
Step 2: Write minimal code
Step 3: Refactor

Feature: [description]
```

---

## Key Risks to Mitigate

| Risk | Mitigation |
|------|------------|
| **Hallucinations** | Cross-reference with known facts, structured output |
| **Data leakage** | Strip PII, use synthetic data |
| **Context overflow** | Chunk large inputs, prioritize |
| **Bias amplification** | Diverse examples, human review |

---

## When to Use Prompt Engineering

| Use For | Don't Use For |
|---------|---------------|
| Test case generation | Final security decisions |
| Code analysis | Replacing human judgment |
| Data generation | Compliance audits |
| Exploratory augmentation | Legal/regulatory requirements |

---

## Metrics for Evaluating Prompts

- **Accuracy** — Does output match reality?
- **Precision** — Relevant responses only?
- **Recall** — All relevant items found?
- **Relevance** — Contextually appropriate?
- **Diversity** — Varied approaches?
- **Execution success** — Did it run without errors?

---

## Related

- [[raw/winteringham-prompts]] — Full prompt library
- [[wiki/agentic-patterns]] — Prompt chaining, agents
- [[wiki/istqb-certifications/ct-genai]] — CT-GenAI syllabus
- [[raw/implement-ai-in-qa-process]] — AI implementation guide
