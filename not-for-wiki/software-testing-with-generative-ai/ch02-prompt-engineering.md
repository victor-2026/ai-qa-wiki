# Large Language Models and Prompt Engineering

**Source**: Chapter 2, *Software Testing with Generative AI* (pages 39-62)

## Overview

Fundamentals of how LLMs work, risks (hallucinations), and prompt engineering techniques.

---

## 2.1 How LLMs Work

### Probability-Based Prediction

LLMs predict next token based on training data probability.

**Example**: Smartphone keyboard suggestions - type "I am" → suggests next words based on probability.

### Training Approaches

| Approach         | Description                         |
| ---------------- | ----------------------------------- |
| **Supervised**   | Labeled data paired with output     |
| **Unsupervised** | No labels, learns implicit patterns |

---

## 2.2 Risks of Using LLMs

### Hallucinations

LLM produces confident but false information.

**Example**: "I recommend 'AI-Driven Testing' by Julian Harty" — book doesn't exist!

### Causes

- Poor training data
- Overfitting
- Model fills gaps

### Key Rule

> Never anthropomorphize LLMs. They are probabilistic, not reasoning.

---

## 2.3 Prompt Engineering Techniques

### Weak vs Strong Prompt

**Weak**: "Create tests for file upload"

**Strong**: "Act as software tester. Generate test ideas for feature delimited by hashes. Focus on Functionality, Data Integrity, Security"

### Key Techniques

1. **Delimiters** - Separate parts of prompt with #, %, |
2. **Structured output** - Request JSON, tables
3. **Few-shot** - Examples in prompt
4. **Time-to-think** - "Work out solution before outputting"

---

## Вопросы к главе

1. Как работают LLMs? Объясни на примере клавиатуры.
2. Что такое hallucination? Приведи пример.
3. Почему не стоит антропоморфизировать LLMs?
4. Разница supervised vs unsupervised learning?
5. Пример слабого и сильного prompt.
6. Как работает delimiter tactic?
7. Что такое few-shot prompting?
8. Что такое "time-to-think" техника?

---

## Related Topics

- [Ch5: Test Planning](ch05-test-planning.md)
- [Ch10: Customized LLMs](ch10-customized-llms.md)

---

*Licensed content: Software Testing with Generative AI (EuroSTAR)*