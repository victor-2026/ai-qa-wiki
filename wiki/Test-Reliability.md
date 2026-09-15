# Test Reliability (Надёжность тестов)

**Определение:** Способность тест-сьюты давать воспроизводимые, стабильные результаты без ложноположительных и ложноотрицательных срабатываний. Включает борьбу с flakiness, изоляцию тестов, контроль окружения.

**Связь с мутациями:** Тест, который проходит всегда (always-green) — ненадёжен для мутаций: он не ловит даже намеренно введённые дефекты. Надёжный тест = стабильный + чувствительный к изменениям.

**Ключевые метрики:** Flaky rate, Mean Time Between Flakes, mutation score stability.

**Связанные темы:**
- [[Mutation-testing-advanced-playwright]] — flakiness + мутации
- [[Mutation-testing-without-code]] — стабильность мутационного анализа
- [[Self-healing-tests]] — самовосстановление при нестабильных тестах
- [[Chaos-Engineering]] — надёжность при сбоях

---

*Теги: #Test-Reliability #Flakiness #Stability #Reproducibility*
