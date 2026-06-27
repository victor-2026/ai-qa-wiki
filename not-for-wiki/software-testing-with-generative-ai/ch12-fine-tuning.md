# Fine-tuning LLMs with Business Domain Knowledge

**Source**: Chapter 12, *Software Testing with Generative AI* (pages 280-306)

## 12.1 What is Fine-tuning?

Train pre-trained LLM on your specific data to change behavior.

### How It Works

1. Prepare training data (prompts + outputs)
2. Select base model
3. Fine-tune
4. Test results
5. Deploy

---

## 12.2 LoRA

**Low-Rank Adaptation** = Efficient method:

- Creates "adapters" instead of retraining full model
- Much faster
- Allows sharing adapters

---

## 12.3 Training Data Format

JSONL (JSON Lines):
```json
{"instruction": "What annotations are in BrandingResult?", "output": "@Getter @Setter..."}
{"instruction": "How to test?", "output": "@BeforeEach..."}
```

---

## 12.4 Evaluation

| Metric | Description |
|--------|-------------|
| Loss | Distance from expected |
| Accuracy | % correct |
| Relevance | Answers question? |

**Human evaluation is key** - check for hallucinations

---

## 12.5 Fine-tuning vs RAG

| Aspect | Fine-tuning | RAG |
|--------|-------------|-----|
| Changes model | Yes | No |
| Adds knowledge | Implicit | Explicit |
| Cost | Higher | Lower |
| Best for | Style/tone | Facts |

---

## Вопросы к главе

1. Что такое fine-tuning?
2. Как работает LoRA?
3. Формат training data?
4. Как оценить fine-tuned модель?
5. В чем разница fine-tuning vs RAG - когда и что применять?
6. Что такое JSONL формат?
7. Как подготовить данные для fine-tuning?
8. Инструменты для fine-tuning?

---

## Related Topics

- [Ch10: Customized LLMs](ch10-customized-llms.md)
- [Ch11: RAG](ch11-rag.md)

---

*Licensed content: Software Testing with Generative AI (EuroSTAR)*