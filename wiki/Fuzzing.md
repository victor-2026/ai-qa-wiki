# Fuzzing (Фаззинг)

**Определение:** Автоматизированный метод тестирования, при котором система получает массовые случайные, некорректные или специально сформированные входные данные для выявления сбоев, утечек памяти и нарушений безопасности.

**Типы фаззинга:**
- **Mutation-based** — модификация существующих корректных входов (flip bits, insert bytes, delete)
- **Generation-based** — генерация входов с нуля по грамматике/спецификации
- **Coverage-guided** — использует feedback от code coverage для генерации более «интересных» входов

**Связь с мутациями:** Fuzzing = мутации на уровне входных данных, mutation testing = мутации на уровне кода. Оба ищут blind spots, но fuzzing ломает систему снаружи, mutation testing — изнутри.

**Инструменты:** AFL++, libFuzzer, Hypothesis (Python), Jazzer (Java), go-fuzz (Go).

**Связанные темы:**
- [[Mutation-testing-without-code]] — мутации без доступа к исходному коду
- [[Mutation-testing-advanced-playwright]] — мутации в UI-тестах
- [[Chaos-Engineering]] — хаос-инжиниринг на уровне инфраструктуры
- [[ui-fuzzing]] — фаззинг UI-форм и ввода
- [[API-Testing]] — фаззинг API-эндпоинтов

---

*Теги: #Fuzzing #Security #Input-Testing #Mutation #Boundary*

## See also

- [API Testing (Тестирование API)](wiki/API-Testing.md)
- [Black Box Testing (Тестирование «чёрного ящика»)](wiki/Black-Box-Testing.md)
- [Chaos Engineering (Хаос-инжиниринг)](wiki/Chaos-Engineering.md)
