# EARS и BDD: От требований к тестам

## EARS — Easy Approach to Requirements Syntax

EARS — это лёгкий структурированный подход к написанию текстовых требований, разработанный Alistair Mavin (Mav) и коллегами из Rolls-Royce PLC. Впервые опубликован на IEEE RE'09 (2009). Используется Airbus, Bosch, Dyson, Honeywell, Intel, NASA, Rolls-Royce, Siemens.

**Проблема:** Требования на естественном языке неоднозначны, сложны, допускают множественные интерпретации. Особенно критично, когда автор пишет не на родном английском.

**Решение:** Небольшой набор шаблонов (5 основных + complex), которые жёстко фиксируют порядок клауз: `[While precondition] [When trigger] the system shall response`.

### 5 базовых паттернов EARS

| Тип | Ключевое слово | Шаблон | Пример |
|-----|---------------|--------|--------|
| **Ubiquitous** (вездесущее) | (нет) | `The system shall <response>` | The mobile phone shall have a mass of less than XX grams |
| **State-driven** (состояние) | `While` | `While <precondition>, the system shall <response>` | While there is no card in the ATM, the ATM shall display "insert card to begin" |
| **Event-driven** (событие) | `When` | `When <trigger>, the system shall <response>` | When "mute" is selected, the laptop shall suppress all audio output |
| **Optional feature** (опция) | `Where` | `Where <feature>, the system shall <response>` | Where the car has a sunroof, the car shall have a sunroof control panel |
| **Unwanted behavior** (ошибка) | `If…Then` | `If <trigger>, then the system shall <response>` | If an invalid card number, then the website shall display "re-enter card details" |

### Complex requirements

Сочетание базовых паттернов через `While + When`:

> While <precondition>, When <trigger>, the system shall <response>

Пример: *While the aircraft is on ground, when reverse thrust is commanded, the engine control system shall enable reverse thrust.*

### Почему EARS работает

- **Порядок клауз фиксирован** (precondition → trigger → response) — соответствует временной логике
- **Ключевые слова интуитивны** — совпадают с естественным английским
- **Нет специализированных инструментов** — работает в любой документ-системе
- **Особенно эффективен для non-native speakers** — структура компенсирует языковой барьер

Источники:
- [Alistair Mavin — EARS Official Guide](https://alistairmavin.com/ears/)
- [Mavin et al. — Easy Approach to Requirements Syntax (IEEE 2009)](https://ieeexplore.ieee.org/abstract/document/5328509)
- [Sebastian Dingler — EARS: The Easy Approach to Requirements Syntax (2025)](https://dev.to/sebastian_dingler/ears-the-easy-approach-to-requirements-syntax-39a5)

---

## EARS → BDD: Мост к тестам

EARS и BDD решают разные части одной задачи:

| | EARS | BDD (Gherkin) |
|---|---|---|
| **Суть** | Точное определение требований | Верификация через сценарии |
| **Формат** | Юридический контракт | Сценарий фильма |
| **Аудитория** | PM, архитектор, создатель правил | Инженер, QA, AI-агент |
| **Проблема** | «Ты сделал не то, что я думал» | «Логика верна, но непригодна» |

**Связь:** Требование в EARS напрямую транслируется в один или несколько Gherkin-сценариев.

### Пример трансляции EARS → Gherkin

**EARS requirement:**
> While user is authenticated, when withdrawal request exceeds balance, the system shall return HTTP 400 with INSUFFICIENT_FUNDS.

**Gherkin scenario:**
```gherkin
Scenario: Withdrawal fails due to insufficient funds
  Given user is authenticated
  And user balance is $50
  When withdrawal of $100 is requested
  Then API returns HTTP 400
  And error code is "INSUFFICIENT_FUNDS"
```

### Маппинг EARS → Gherkin

| EARS клауза | Gherkin шаг |
|-------------|-------------|
| `While <precondition>` | `Given <precondition>` |
| `When <trigger>` | `When <trigger>` |
| `The system shall <response>` | `Then <response>` |
| `If <error condition>` | `Given <error> / When <action>` + `Then <error handling>` |
| `Where <feature>` | `Given <feature is enabled>` |

---

## SDD — Spec-Driven Development (2026)

Spec-Driven Development — это применение EARS + BDD к Vibe Coding. Вместо расплывчатых промптов AI-агент получает:

1. **EARS rules** — строгие логические границы («так можно, так нельзя»)
2. **BDD scenarios** — конкретные примеры с Given/When/Then
3. **Acceptance criteria** — проверяемые условия

**Prompt-шаблон для AI-агента:**
```markdown
# Task: Implement a debit API

## EARS rules (strictly follow):
- [Event-driven]: When request received, balance must be checked.
- [Unwanted]: If balance insufficient, return 400 INSUFFICIENT_FUNDS.
- [State-driven]: While wallet is "Frozen", reject all debits.

## BDD acceptance scenario:
Scenario: Insufficient funds
  Given user balance is $50
  When debit of $100 is requested
  Then API returns HTTP 400
  And error code is "INSUFFICIENT_FUNDS"
```

### Зачем это QA

- **EARS** даёт тестировщику точные границы: что система *должна* делать в каждом состоянии
- **BDD** даёт готовые сценарии для автоматизации (Cucumber, SpecFlow, Playwright)
- **SDD** — это мост между PM, разработчиком и AI-агентом

---

## Ресурсы

- [EARS Quick Reference (PDF, Aalto University)](https://aaltodoc.aalto.fi/bitstream/handle/123456789/12861/D5_uusitalo_eero_2012.pdf)
- [EARS Tutorial @ Intel (PDF, John Terzakis)](https://www.iaria.org/conferences2013/filesICCGI13/ICCGI_2013_Tutorial_Terzakis.pdf)
- [Conduct of Code — EARS to BDD transition (C#/SpecFlow)](https://conductofcode.io/post/easy-approach-to-requirements-syntax-and-the-segue-to-behavior-driven-development)
- [Dev TLDRLSS — Что такое EARS и BDD (рус., 2026)](https://dev.tldrlss.com/ru/article/2026/02/whats-bdd-and-ears-sdd-scenario/)
- [MBSE.dev — Improving Requirements Engineering with EARS (2024)](https://mbse.dev/improving-requirements-engineering-with-ears-easy-approach-to-requirements-syntax/)
