# CT-GenAI Hands-on Exercises

**Last Updated:** 2025-04-15
**Source:** ISTQB CT-GenAI Course

---

## Overview

CT-GenAI includes 20 hands-on exercises across 5 modules. These are practical skills to practice alongside theoretical learning.

## Exercise Mapping by Module

### Module 1: Introduction to GenAI

| ID | Exercise | Description |
|----|----------|-------------|
| HO-1.1.2 | Tokenization | Practice token count evaluation when using LLM for test task |
| HO-1.1.4 | Multimodal Prompting | Execute prompt with text + image inputs for test task |

**Skills:** Understanding token limits, cost estimation, multimodal inputs

---

### Module 2: Prompt Engineering

| ID | Exercise | Description |
|----|----------|-------------|
| HO-2.1.1 | Analyze Prompts | Identify role, context, instruction, input, constraints, output |
| HO-2.1.2a | Prompt Techniques Demo | Observe prompt chaining, few-shot, meta prompting |
| HO-2.1.2b | Identify Techniques | Recognize prompting techniques in examples |
| HO-2.2.1a | Multimodal Acceptance Criteria | Generate acceptance criteria from GUI wireframe |
| HO-2.2.1b | Progressive Refinement | Prompt chaining + human verification for user story |
| HO-2.2.2a | Gherkin Generation | Prompt chaining for functional test cases from user stories |
| HO-2.2.2b | Few-shot Gherkin | Generate Gherkin-style conditions from user stories |
| HO-2.2.2c | Test Prioritization | Prompt chaining for prioritizing test cases with dependencies |
| HO-2.2.3a | Keyword Scripts | Few-shot prompting for keyword-driven test scripts |
| HO-2.2.3b | Report Analysis | Structured prompts for test report analysis |
| HO-2.2.4 | Monitoring Metrics | AI-prepared test monitoring metrics from test data |
| HO-2.2.5 | Technique Selection | Choose appropriate prompting technique for task |
| HO-2.3.1 | Result Evaluation | Use metrics for evaluating GenAI output quality |
| HO-2.3.2 | Prompt Optimization | Evaluate and refine prompt for test task |

**Skills:** Structured prompts, prompt chaining, few-shot, evaluation metrics

---

### Module 3: Risk Management

| ID | Exercise | Description |
|----|----------|-------------|
| HO-3.1.2a | Hallucination Experiment | Observe and document hallucinations in GenAI |
| HO-3.1.2b | Reasoning Errors | Identify reasoning errors in outputs |
| HO-3.2.3 | Privacy/Security Case | Recognize data privacy and security risks |
| HO-3.3.1 | Energy Calculator | Calculate energy and CO emissions for test tasks |

**Skills:** Risk identification, hallucination detection, environmental impact

---

### Module 4: Test Infrastructure

| ID | Exercise | Description |
|----|----------|-------------|
| HO-4.1.2 | RAG Experiment | Implement RAG for a test task |
| HO-4.1.3 | Agent Observation | Observe LLM-agent for repetitive test automation |
| HO-4.2.1 | Fine-tuning Process | Observe example of fine-tuning process |

**Skills:** RAG implementation, agentic workflows, fine-tuning

---

### Module 5: Integration

| ID | Exercise | Description |
|----|----------|-------------|
| HO-5.1.3 | Cost Estimation | Calculate recurring costs of GenAI for test tasks |

**Skills:** Business case, ROI calculation

---

## Key Techniques to Practice

### 1. Prompt Chaining
```
Task → Step 1 → Step 2 → Step 3 → Output
```
Use for: Complex tasks, progressive refinement

### 2. Few-Shot Prompting
```
Example 1: Input → Expected Output
Example 2: Input → Expected Output
Your Input →
```
Use for: Pattern matching, format generation (Gherkin, test data)

### 3. Meta Prompting
```
"Critique this prompt and suggest improvements..."
```
Use for: Prompt optimization, quality assurance

### 4. Multimodal Prompting
```
Image (wireframe) + Text instruction → Acceptance criteria
```
Use for: UI-based testing, visual requirements

---

## Tools to Practice With

| Category | Tools |
|----------|-------|
| **LLM APIs** | OpenAI API, Anthropic Claude, Groq |
| **RAG** | LangChain, LlamaIndex |
| **Agents** | AutoGen, CrewAI, LangGraph |
| **Cost Estimation** | Token calculators, API pricing pages |

---

## Related

- [[wiki/qa-prompt-engineering-guide]] — Prompt engineering basics
- [[wiki/agentic-patterns]] — Agentic patterns
- [[wiki/rag-evaluation]] — RAG evaluation
- [[wiki/ai-testing-metrics]] — Evaluation metrics
