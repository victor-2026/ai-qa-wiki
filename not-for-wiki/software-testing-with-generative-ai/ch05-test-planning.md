# Test Planning with AI Support

**Source**: Chapter 5, *Software Testing with Generative AI* (pages 114-133)

## 5.1 Test Planning in Modern Testing

### Problem
Asking LLMs "generate test cases" produces generic, context-free results.

### Better: Focus on Risks
- Risks → different testing techniques
- LLMs as assistants to expand coverage
- Human controls direction

### Area of Effect Model
```
Human (risk analysis) → LLM expands → Human guides
```

---

## 5.2 Weak Prompts = Weak Results

### Weak Prompt
"Create tests for file upload"

### Solution: Create Models First

**Model** = abstract representation (data flow, component, sequence)

---

## 5.3 SFDIPOT Mnemonic

| Letter | Perspective |
|--------|-------------|
| **S**tructure | What product is made of |
| **F**unction | What product does |
| **D**ata | What processes |
| **I**nterfaces | How interacts |
| **P**latform | What depends on |
| **O**perations | How used |
| **T**ime | How time affects |

---

## Key Takeaways

1. Ask for risks, not test cases
2. Create models then prompt specific parts
3. Use SFDIPOT for different perspectives

---

## Вопросы к главе

1. Почему фокус на рисках важнее тест-кейсов?
2. Как weak prompts влияют на качество?
3. Какие типы моделей можно использовать?
4. Пример prompt с моделью данных?
5. Что такое SFDIPOT и как применять?
6. Как создавать модели для тестирования?
7. Как Area of effect model работает?
8. Разница между test cases и risks?

---

## Related Topics

- [Ch6: Rapid Data](ch06-rapid-data.md)
- [Ch8: Exploratory](ch08-exploratory.md)

---

*Licensed content: Software Testing with Generative AI (EuroSTAR)*