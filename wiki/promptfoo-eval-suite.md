---
title: "Promptfoo Eval Suite for AI QA Wiki"
updated: 2026-05-05
tags: [promptfoo, eval, llm-comparison, wiki, groq]
type: guide
---

# Promptfoo Eval Suite for AI QA Wiki

**Purpose:** Compare LLM outputs on wiki Q&A tasks using systematics evaluation  
**Tool:** [Promptfoo](https://www.promptfoo.dev/) — open-source LLM testing framework  

---

## 1. What is Promptfoo?

Promptfoo is a CLI tool for:
- **Comparing models** (Groq Llama3.3 70B vs GPT-5 Nano)
- **Testing prompts** across multiple inputs
- **Measuring metrics** (accuracy, faithfulness, relevance)
- **Finding regressions** in prompt changes

**Installation:**
```bash
npm install -g promptfoo
# or
yarn global add promptfoo
```

---

## 2. Basic `promptfoo.yaml` Structure

```yaml
prompts:
  - |
    You are an expert in AI Testing and QA.
    Answer based on provided wiki context.
    Answer concisely (3-5 sentences).
    
    Context: {{context}}
    
    Question: {{question}}

providers:
  - groq:llama3-70b-8192
  - openai:gpt-4o

tests:
  - description: "What is metamorphic testing?"
    vars:
      context: "Metamorphic testing checks relations between inputs/outputs..."
      question: "What is metamorphic testing?"
    
  - description: "How to implement POM in Playwright?"
    vars:
      context: "Page Object Model uses page.getByRole()..."
      question: "How to implement POM in Playwright?"
```

---

## 3. Integration with `wiki_qa.py`

### Generate Q&A Pairs from Wiki

```bash
cd /Users/victor/Projects/ai-qa-wiki

# Use wiki_qa.py to generate 50 Q&A pairs
for file in wiki/*.md; do
  python3 wiki_qa.py --ask "Generate 3 test questions for $(basename $file)" --save
done
```

### Convert to promptfoo format

```python
# convert_to_promptfoo.py
import json
from pathlib import Path

qa_dir = Path("outputs")
test_cases = []

for f in qa_dir.glob("qa_*.md"):
    content = f.read_text()
    # Parse Q&A from markdown
    # Add to test_cases list

config = {
    "prompts": ["You are QA expert..."],
    "providers": ["groq:llama3-70b-8192"],
    "tests": test_cases
}

Path("promptfoo.yaml").write_text(json.dumps(config, indent=2))
```

---

## 4. Eval Metrics for Wiki Q&A

### 4.1 Answer Relevance (LLM-as-Judge)

```yaml
defaultTest:
  assert:
    - type: llm-rubric
      value: "Is the answer relevant to the question? Rate 1-5."
      threshold: 4
```

### 4.2 Faithfulness (RAG Evaluation)

```yaml
defaultTest:
  assert:
    - type: llm-rubric
      value: "Is the answer faithful to the provided context? Rate 1-5."
      threshold: 4
```

### 4.3 Accuracy (Fact Checking)

```yaml
defaultTest:
  assert:
    - type: equals
      value: "{{expected}}"
      output: "{{answer}}"
```

---

## 5. Running Evals

### Basic Run

```bash
cd /Users/victor/Projects/ai-qa-wiki
promptfoo eval --config promptfoo.yaml
```

### Compare Multiple Models

```yaml
providers:
  - groq:llama3-70b-8192
  - groq:llama3.2-3b
  - openai:gpt-4o
  - anthropic:claude-3-5-sonnet
```

```bash
promptfoo compare --config promptfoo.yaml --output results.html
```

---

## 6. Connection to Metamorphic Testing

### Transform Wiki Questions (Metamorphic Relations)

```yaml
tests:
  # Synonym Substitution
  - vars:
      question: "What is metamorphic testing?"
  - vars:
      question: "What is METAMORPHIC testing?"  # Same, different case
  
  # Negation
  - vars:
      question: "What is metamorphic testing?"
  - vars:
      question: "What is NOT metamorphic testing?"  # Negated
  
  # Parameter Permutation
  - vars:
      context: "API_BASE: /api, endpoints: /auth/login..."
      question: "Test login API"
  - vars:
      context: "API_BASE: /api, endpoints: /auth/login..."
      question: "Test API login"  # Same, different wording
```

**Assert:** All should produce same/similar answers (within threshold).

---

## 7. Implementation Steps (TODO)

1. ✅ Install promptfoo (`npm install -g promptfoo`)
2. ⏳ Generate 50 Q&A pairs from `wiki/` using `wiki_qa.py`
3. ⏳ Create `promptfoo.yaml` with 3-5 test cases
4. ⏳ Run `promptfoo eval` with Groq Llama3.3 70B
5. ⏳ Add metamorphic transforms (synonyms, negation)
6. ⏳ Compare 3+ models (Groq, GPT-4o, Claude)
7. ⏳ Generate HTML report (`promptfoo compare --output results.html`)

---

## 8. Example: Full `promptfoo.yaml`

```yaml
prompts:
  - |
    You are an expert in AI Testing and QA.
    Answer based on the provided context from Wiki.
    Answer concisely (3-5 sentences).
    
    Context: {{context}}
    Question: {{question}}

providers:
  - groq:llama3-70b-8192
  - groq:llama3.2-3b

defaultTest:
  assert:
    - type: llm-rubric
      value: "Is the answer relevant and faithful to context? Rate 1-5."
      threshold: 4

tests:
  - description: "Metamorphic Testing"
    vars:
      context: "Metamorphic testing uses relations: Synonym Substitution, Parameter Permutation, Symmetry..."
      question: "What is metamorphic testing?"
  
  - description: "Playwright POM"
    vars:
      context: "Page Object Model in Playwright uses page.getByRole() and page.getByTestId()..."
      question: "How to implement POM in Playwright?"
  
  - description: "Agent Skills"
    vars:
      context: "Agent Skills specification by Anthropic, Obsidian skills by Steph Ango..."
      question: "What are Agent Skills?"
```

---

## 9. Key Benefits

| Benefit | Description |
|--------|-------------|
| **Objective Comparison** | Numbers (4/5, 85% accuracy) vs "feels better" |
| **Regression Testing** | Catch prompt changes that break answers |
| **Model Selection** | Data-driven choice (Groq vs GPT vs Claude) |
| **RAG Evaluation** | Faithfulness + Relevance metrics |
| **Metamorphic Testing** | Transform questions, verify consistent answers |

---

**Tags:** #promptfoo #eval #llm-comparison #wiki #groq #qa  
**Related:** [[prompt-tips-and-skills]] [[metamorphic-tests-comparison]] [[qa-ai-transition-guide]]  
**Updated:** 2026-05-05
