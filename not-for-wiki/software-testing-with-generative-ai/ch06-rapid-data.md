# Rapid Data Creation Using AI

**Source**: Chapter 6, *Software Testing with Generative AI* (pages 133-156)

## 6.1 Generating Test Data

### Using Delimiters
```
% room_name | string | random
% type | string | 'single' or 'double'
% beds | integer | 1 to 6
% roomPrice | integer | 100 to 200
```

### Prompt
"You are JSON data generator. Generate 5 objects..."

### Example Output
```json
{
  "room_name": "Cozy Suite",
  "type": "single",
  "beds": 1,
  "roomPrice": 150
}
```

---

## 6.2 Transforming Data Formats

### JSON → XML
 Change delimiter to # rooms

### JSON → SQL
 Prompt to create table + insert statements

---

## 6.3 API Integration

- Generate data on-demand during tests
- Transform data based on context
- Anonymize production data

---

## Вопросы к главе

1. Как использовать delimiters для генерации данных?
2. Пример prompt для JSON данных.
3. Как LLM трансформирует JSON в SQL?
4. Как интегрировать LLM в тестовый фреймворк через API?
5. Как создать сложные данные для boundary testing?
6. Что такое data masking и анонимизация?
7. Пример on-demand генерации данных?
8. Какие форматы данных поддерживает LLM?

---

## Related Topics

- [Ch5: Test Planning](ch05-test-planning.md)
- [Ch7: UI Automation](ch07-ui-automation.md)

---

*Licensed content: Software Testing with Generative AI (EuroSTAR)*