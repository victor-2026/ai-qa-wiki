# SWE-Tester Framework

**Last Updated:** 2026-04-18
**Sources:** arxiv:2603.24160v1 (confirmed via Gemini), real paper content

---

## Overview

**SWE-Tester** — фреймворк для обучения open-source LLM генерации тестов воспроизводящих баги из текстовых описаний.

**Проблема:** Разработчики не любят писать тесты. Автоматическое воспроизведение багов из issue/description повысило бы производительность.

**Ключевой вывод:**
> Fine-tuning на 41K примерах из 2600 GitHub репозиториев даёт до +10% success rate и +21% change coverage. Open-source модели приближаются к proprietray.

---

## Two-Step Workflow

```
Bug Report (Natural Language)
        │
        ▼
┌─────────────────────┐
│  1. Code           │
│  Localization      │ ← Find defective files
│  (Retrieval)      │
└─────────────────────┘
        │
        ▼
┌─────────────────────┐
│  2. Code Editing   │
│  (Search/Replace)   │ ← Insert test patches
└─────────────────────┘
        │
        ▼
   Issue Reproduction Test
```

### Step 1: Code Localization

Поиск дефектного кода и тестовых файлов.

**Methods used:**
- **BM25** — probabilistic ranking algorithm
- **Qwen2.5-Embedding** — semantic embeddings
- **SWE-Fixer retriever** — fine-tuned retriever model

**Metrics:**
- **Precision** — точность найденных файлов
- **Recall** — полнота (доля найденных релевантных файлов)
- **W (Applicability)** — % патчей которыеApplyWithoutErrors

### Step 2: Code Editing

Генерация тестов в формате Search/Replace.

**Search/Replace format:**
```
<<<< << .head
(original code)
====
(new test code)
>>>> .tail
```

**Why Search/Replace:**
- Safer than raw code generation
- Explicit boundaries
- Easier to validate syntax

---

## Dataset: 41K Instances

Собрано из **2600+ GitHub репозиториев**.

**Критерии отбора:**
- Real PRs с тестами
- Reproducible bugs
- Clear issue descriptions

**Data sources:**
- SWE-Bench Verified benchmark
- Real production repos

---

## Fine-tuned Models

| Model | Family | Improvements |
|-------|--------|---------------|
| Qwen-2.5-Coder | Qwen | +10% success rate |
| Llama-3.1-8B | Meta | +8% success rate |
| Gemma3-12B | Google | +7% success rate |

**Metrics after fine-tuning:**
- **S (Success Rate)** — % тестов успешно воспроизводящих баг
- **ΔC (Change Coverage)** — % строк кода в патче, которые стали выполняться чаще

---

## Inference Scaffold

Конвейер для обработки ошибок и улучшения результатов:

```
1. Sample multiple candidate patches
         │
         ▼
2. Execute on codebase (filter syntax/execution errors)
         │
         ▼
3. Rerank surviving patches
   - Self-consistency scoring
   - Sequence similarity scoring
         │
         ▼
4. Output best patch
```

**Why scaffold:**
- LLM может генерировать syntactically incorrect код
- Multiple attempts → filter → rerank = better quality

---

## Key Insights

### 1. Scaling Inference-Time Compute

Больше compute на этапе inference → лучше результаты:
- Sampling more candidates
- Better reranking

### 2. Scaling Training Data

Больше training data → better performance:
- 41K examples shows clear improvements
- Data quality matters more than quantity

### 3. Oracle Comparison

Интересный вопрос: "А что если мы знаем где баг (oracle retrieval)?"
- Change coverage значительно выше
- Но это не всегда реалистично

---

## Comparison: SWE-Tester vs MAS-Testing

| Aspect | SWE-Tester | MAS-Testing (my earlier draft) |
|--------|------------|---------------------------|
| Agents | 0 (pipeline) | 4 roles |
| Approach | Retrieval + Edit | Multi-agent system |
| Fine-tuning | Required | Prompt-only |
| Isolation | Via scaffold | Via Quality Data Plane |

**Clarification:** MAS-Testing Framework with 4 roles was my conceptual interpretation — not confirmed in the actual paper. SWE-Tester is the real framework.

---

## Related Concepts

### PEFT (Parameter-Efficient Fine-Tuning)

Methods like **LoRA** для быстрого дообучения:
- Training only small adapter weights
- Original model stays frozen
- Can combine with base model

**Question raised in paper:** Can we use PEFT? — Показывает что полное fine-tuning лучше для этой задачи.

### BM25

**Best Matching 25** — probabilistic search algorithm.
- Used for initial retrieval
- Complementary to semantic embeddings

---

## QA Engineer Implications

1. **Issue reproduction tests** становятся автоматическими
2. **Fine-tuning** open-source моделей возможен на корпоративных данных
3. **Search/Replace** формат безопаснее raw generation
4. **Scaffold** критически важен — один LLM вызов недостаточно

---

## Related Wiki Topics

- [[wiki/mas-vs-swe-comparison]] — MAS vs SWE-Tester comparison
- [[wiki/agentic-patterns]] — Agentic engineering (different approach!)
- [[wiki/ai-testing-metrics]] — Metrics like S, ΔC
- [[wiki/testing-stability]] — Test execution quality

## Sources

- arxiv:2603.24160v1 — SWE-Tester: Training Open-Source LLMs for Issue Reproduction
- SWE-Bench Verified benchmark
- Gemini conversation analysis