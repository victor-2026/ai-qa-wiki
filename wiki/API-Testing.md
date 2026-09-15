# API Testing (Тестирование API)

**Определение:** Проверка API (Application Programming Interface) на корректность, производительность, безопасность и соответствие спецификации. Включает проверку запросов/ответов, статус-кодов, схем, контрактов и граничных значений.

**Связь с мутациями:** Мутации API — изменение статус-кодов (200→500), удаление полей из ответа, изменение типов данных. Мутация-тестирование проверяет, ловят ли тесты эти дефекты.

**Инструменты:** Postman, REST Assured, Pytest (requests), Playwright API, Pact (контрактные тесты).

**Связанные темы:**
- [[Mutation-testing-without-code]] — мутации API без доступа к коду
- [[Mutation-testing-advanced-playwright]] — API-мутации в Playwright
- [[Fuzzing]] — фаззинг API-эндпоинтов
- [[Black-Box-Testing]] — тестирование без знания внутренностей

---

*Теги: #API-Testing #Contract-Testing #REST #Schema*
