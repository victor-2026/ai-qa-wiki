# Chaos Engineering (Хаос-инжиниринг)

**Определение:** Дисциплина экспериментирования с системами для выявления слабых мест через контролируемые сбои. Цель — обнаружить, как система ведёт себя при отказах, прежде чем они произойдут в production.

**Ключевой принцип:** Chaos Monkey (Netflix, 2011) — намеренно отключать компоненты, чтобы убедиться, что система выживает.

**Связь с мутациями:** Мутация-тестирование проверяет, ловят ли тесты дефекты в коде. Хаос-инжиниринг проверяет, выживает ли система при отказах инфраструктуры. Оба метода — controlled failure injection, но на разных уровнях: код vs инфраструктура.

**Инструменты:** Chaos Monkey, Gremlin, LitmusChaos, Toxiproxy (для сетевых сбоев).

**Связанные темы:**
- [[Mutation-testing-advanced-playwright]] — мутации на уровне кода
- [[Mutation-testing-without-code]] — мутации без доступа к коду
- [[ai-chaos-testing]] — AI-подход к хаос-тестированию
- [[Fuzzing]] — хаос на уровне входных данных
- [[Self-healing-tests]] — самовосстанавливающиеся тесты при сбоях

---

*Теги: #Chaos-Engineering #Resilience #Failure-Injection #Reliability*

## See also

- [Fuzzing (Фаззинг)](wiki/Fuzzing.md)
- [Test Reliability (Надёжность тестов)](wiki/Test-Reliability.md)
- [AI for Chaos Testing](wiki/ai-chaos-testing.md)
