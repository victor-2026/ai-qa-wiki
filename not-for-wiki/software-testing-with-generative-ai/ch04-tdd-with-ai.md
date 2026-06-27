# AI-Assisted Testing for Developers (TDD)

**Source**: Chapter 4, *Software Testing with Generative AI* (pages 91-114)

## 4.1 TDD + AI Loop

### Traditional TDD
```
1. Red → Write failing test
2. Green → Make test pass
3. Refactor → Improve code
```

### AI-Augmented TDD

| Step | AI Role |
|------|--------|
| Red | ChatGPT generates test ideas |
| Green | Copilot suggests implementation |
| Refactor | ChatGPT analyzes risks |

---

## 4.2 Using Copilot for TDD

### How Copilot Works
- Triggered by code comments
- Suggests next lines
- Improves with context

### Example
```java
// JUnit Jupiter Engine
→ Copilot suggests dependency
```

---

## 4.3 AI for Risk Analysis

### Prompt
"Analyze code and identify risks related to accuracy and consistency"

### Example Output
- Risk: submitTimesheet overwrites existing data
- Risk: Null keys in HashMap
- Risk: No thread synchronization

---

## Вопросы к главе

1. Как TDD помогает при работе с AI?
2. Отличия Copilot от ChatGPT?
3. Пример prompt для генерации тестов?
4. Как AI помогает в анализе рисков кода?
5. Как работает цикл Red-Green-Refactor с AI?
6. Пример использования Copilot в TDD цикле?
7. Как использовать ChatGPT для рефакторинга?
8. Какие риски может выявить AI в коде?

---

## Related Topics

- [Ch2: Prompt Engineering](ch02-prompt-engineering.md)
- [Ch7: UI Automation](ch07-ui-automation.md)

---

*Licensed content: Software Testing with Generative AI (EuroSTAR)*