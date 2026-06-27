# AI Agents as Testing Assistants

**Source**: Chapter 9, *Software Testing with Generative AI* (pages 205-227)

## 9.1 What Defines AI Agent

| Characteristic | Description |
|---------------|-------------|
| Goal-driven | Receives and achieves goals |
| Perceptive | Interacts with external systems |
| Autonomous | Chooses which functions to call |
| Adaptive | Uses results to inform next steps |

---

## 9.2 Function Calling

```
1. Prompt + functions sent to LLM
2. LLM determines which function to trigger
3. Function executes code
4. Results returned to LLM
5. Process repeats until complete
```

### Example with LangChain4J
```java
@Tool("Create room records")
public void createRooms(int count) { }

@Tool("Create booking records")
public void createBookings(int count) { }
```

---

## 9.3 Building Test Data Agent

### Tools
- Create rooms in DB
- Create bookings in DB
- Query database

### Chaining
Pass data from one tool to another.

---

## Вопросы к главе

1. Характеристики AI agent?
2. Как работает function calling?
3. Разница tool vs agent?
4. Пример создания AI agent с LangChain4J?
5. Что такое chaining инструментов?
6. Как передавать данные между tools?
7. Пример use case для test data agent?
8. Какие инструменты нужны для test data agent?

---

## Related Topics

- [Ch6: Rapid Data](ch06-rapid-data.md)
- [Ch10: Customized LLMs](ch10-customized-llms.md)

---

*Licensed content: Software Testing with Generative AI (EuroSTAR)*