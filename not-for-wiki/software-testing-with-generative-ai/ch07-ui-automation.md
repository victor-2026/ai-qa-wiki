# Accelerating UI Automation Using AI

**Source**: Chapter 7, *Software Testing with Generative AI* (pages 157-179)

## 7.1 UI Automation Problem

Asking ChatGPT "create Selenium test" → requires extensive rework.

### Better: Component-Based AI

| Component | AI Use |
|-----------|--------|
| Page Objects | Generate from HTML |
| Setup/Teardown | Generate with code comments |
| Methods | Tab through suggestions |

---

## 7.2 Page Object Generation

### Prompt
"You are Java Developer. Convert HTML into Page Object using @FindBy annotations"

### Input HTML
```html
<input id="username" type="text">
<input id="password" type="password">
<button id="login">Login</button>
```

### Output
```java
@FindBy(id = "username")
private WebElement username;

@FindBy(id = "login")
private WebElement loginButton;
```

---

## 7.3 Testability Considerations

- Semantic HTML helps AI
- Stable IDs/attributes matter
- Low testability = more tweaks needed

---

## Вопросы к главе

1. Почему не генерировать полные тесты?
2. Что лучше генерировать через LLM?
3. Пример prompt для Page Object.
4. Как улучшить HTML для AI?
5. Как интегрировать Page Object в фреймворк?
6. Проблемы с deprecated API в LLM?
7. Разница Page Factory и @FindBy?
8. Как улучшить testability HTML?

---

## Related Topics

- [Ch6: Rapid Data](ch06-rapid-data.md)
- [Ch9: AI Agents](ch09-ai-agents.md)

---

*Licensed content: Software Testing with Generative AI (EuroSTAR)*