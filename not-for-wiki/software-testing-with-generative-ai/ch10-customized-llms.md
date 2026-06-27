# Introducing Customized LLMs

**Source**: Chapter 10, *Software Testing with Generative AI* (pages 227-250)

## 10.1 LLM Context Problem

LLMs don't know your:
- Domain
- Codebase
- Quality standards

### Token Limitations

**Token** = Basic unit (~0.75 words)
**Context Window** = Max tokens in prompt

| Model | Context Window |
|-------|---------------|
| GPT-4 | 128K tokens |
| GPT-3.5 | 4K-16K |
| Llama-2 | 4K |

---

## 10.2 RAG

Retrieval-Augmented Generation finds relevant docs and adds to prompt.

### RAG Process
1. User sends query
2. RAG finds relevant documents
3. Adds docs to prompt
4. LLM generates response

---

## 10.3 Fine-tuning

Train LLM on your data to change behavior.

### Fine-tuning vs RAG

| Aspect | RAG | Fine-tuning |
|--------|-----|-----------|
| Cost | Lower | Higher |
| Adds knowledge | Explicit | Implicit |
| Use case | Facts/docs | Style/tone |

---

## Вопросы к главе

1. В чем заключается проблема LLMs с контекстом?
2. Что такое token и context window?
3. Как работает RAG (Retrieval-Augmented Generation)?
4. В чем разница между RAG и fine-tuning - когда что использовать?
5. Когда и что применять - RAG или fine-tuning?
6. Преимущества и недостатки RAG?
7. Преимущества и недостатки fine-tuning?
8. Как выбрать подходящий подход для своего проекта?

---

## Related Topics

- [Ch11: RAG](ch11-rag.md)
- [Ch12: Fine-tuning](ch12-fine-tuning.md)

---

*Licensed content: Software Testing with Generative AI (EuroSTAR)*