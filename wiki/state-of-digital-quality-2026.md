# State of Digital Quality 2026 — AI Testing Report

**Last Updated:** 2026-04-18
**Source:** Applause.com «The State of Digital Quality in Testing AI 2026»

---

## Overview

Главный вывод отчёта: **Quality Gap** — внедрение AI происходит быстрее, чем организации успевают его тестировать и контролировать.

```
 внедрение AI ████████████████████ 100%
 тестирование AI ████████████░░░░░░░░░░░░░░░░░░░░ 54%
                    ↑
              Quality Gap
```

---

## Key Statistics

| Stat | Value |
|------|-------|
| Организации с AI в production | 54.5% |
| Отключили AI после запуска | 44.1% |
| Причина: превысили эксплуатационные расходы | — |
| Budget growth > Dev budget | 29.6% |

---

## 1. POC to Production Problem

**Проблема:** AI функции не доходят от концепции до рабочей версии.

```
┌─────────────────────────────────────────────────┐
│              AI Project Lifecycle              │
└─────────────────────────────────────────────────┘
                      │
    ┌──────────────┐  │
    │   POC / PoD  │──┘ 44.1% отключены
    │  (54.5%)  │      из-за затрат
    └──────────────┘
          │
          ▼
    ┌──────────────┐
    │ Production │─── 55.9% остались
    │  (30%?)  │
    └──────────────┘
```

**Причины провалов:**
1. **Интеграционные проблемы** — AI не дружит с существующей инфраструктурой
2. **Высокие затраты** — LLM API дороже чем ожидалось
3. **Нехватка экспертизы** — нет внутренних специалистов по AI security
4. **Safety issues** — уязвимости не выявлены на ранних этапах

**Вывод:** Требуется этап **AI Readiness Assessment** перед запуском.

---

## 2. Hybrid Testing (Human + AI)

Ключевой паттерн: **Человек + AI вместе, не по отдельности**.

```
         ┌──────────────┐
         │  AI Test   │ ← Запускает тесты
         │ Generator │   генерирует сценарии
         └────┬─────┘
              │
              ▼
┌───────────────────────────────────────────┐
│           Hybrid Testing                   │
│  ┌─────────────┐     ┌─────────────┐   │
│  │  AI does  │     │ Human    │   │
│  │ repetitive│     │ validates│   │
│  │ checks   │ +   │ meaning  │   │
│  └─────────────┘     └─────────────┘   │
└───────────────────────────────────────────┘
```

**Почему нельзя только AI:**
- AI может автоматизировать проверку вещей, **которые не важны** для бизнеса
- AI не понимает **context** — что имеет реальную ценность для пользователя
- **RLHF** (Reinforcement Learning from Human Feedback) остаётся незаменимым

**Почему нельзя только человек:**
- Масштабируемость — AI может сгенерировать 1000 сценариев за минуту
- Consistency — AI не устаёт, не забывает критерии
- Cost — human time дороже

**Вывод:** State — **"AI provides scale and consistency, but humans ground truth"**

---

## 3. Evaluation Architecture (4 Stages)

Надёжная методология оценки LLM:

```
┌────────────────────────────────────────────────────────────────────┐
│              4-Stage Evaluation Framework            │
└────────────────────────────────────────────────────────────────────┘
                        │
    ┌─────────────────┴─────────────────┐
    ▼                               ▼
┌─────────────┐             ┌─────────────┐
│   Stage 1  │────────────▶│   Stage 2  │
│ Gold      │             │ Prompt    │
│ Dataset   │             │ Generation│
│ Creation │             │ (local   │
│ (experts)│             │ models)  │
└─────────────┘             └─────────────┘
        │                           │
        │                       ┌────┴─────┐
        ▼                       ▼
┌─────────────┐             ┌─────────────┐
│   Stage 4 │◀──────────│  Stage 3  │
│ Human    │             │ Model    │
│ Expert  │             │ Jury    │
│ Validation             │ (3+ LLMs)│
└─────────────┘             └─────────────┘
```

### Stage 1: Gold Dataset Creation

Профильные эксперты создают эталонный набор проверенных примеров.
- 50-100 examples
- Verified correct answers
- Edge cases included

### Stage 2: Prompt Generation

Локальные модели расширяют dataset для покрытия:
- Edge cases (граничные условия)
- Adversarial scenarios (атаки на промпты)
- Industry-specific cases

### Stage 3: Model Jury

Ответы оцениваются **3+ разными LLM** параллельно.
- Избегаем **monoculture** (предвзятость одной модели)
- Каждая модель может иметь систематические ошибки

### Stage 4: Human Expert Validation

Специалисты проверяют выборку результатов.
- Фокус на cases где AIjudges разошлись
- Final quality gate

---

## 4. Red Teaming Strategy

Оценка безопасности и поиск уязвимостей.

```
┌─────────────────────────────────────┐
│        Red Teaming Framework         │
└─────────────────────────────────────┘
              │
    ┌─────────┴─────────┐
    ▼                   ▼
┌───────────┐       ┌───────────┐
│ Domain   │       │ General  │
│ Experts  │       │ Testers  │
│ (deep)   │       │ (wide)  │
└───────────┘       └───────────┘
    │                   │
    ▼                   ▼
│ Specific    │   │ Real-world  │
│ bugs       │   │ chaos     │
└─────────────┘   └─────────────┘
```

**Domain Experts:**
- Глубокие специфичные для предметной области ошибки
- Понимание business logic
- Edge cases в niche областях

**General Testers:**
- Отражают хаос реальных пользователей
- Непредсказуемые действия
- Common vulnerabilities

---

## 5. High-Performing Teams Characteristics

| Characteristic | What It Means |
|--------------|------------|
| **Continuous eval cycles** | Оценка после каждого deployment |
| **Hybrid approaches** | AI + Human together |
| **Domain experts** | Привлечение для business-specific задач |
| **Structured Red Teaming** | Регулярная проверка security |
| **ROI monitoring** | Отслеживание рентабельности |

---

## Quality Gap Solutions

| Problem | Solution |
|---------|---------|
| AI deployed faster than tested | AI Readiness Assessment gate before launch |
| 44% AI features disabled | Cost-benefit analysis before POC |
| Monoculture in eval | Model Jury (3+ LLMs) |
| AI optimizes wrong things | Human validates meaning |
| Unknown vulnerabilities | Structured Red Teaming |

---

## Related Wiki Topics

- [[wiki/ai-testing-glossary]] — термины: RLHF, Model Jury, Red Teaming
- [[wiki/swe-tester-framework]] — автоматическая генерация тестов
- [[wiki/ai-testing-metrics]] — метрики оценки AI
- [[wiki/testing-stability]] — stability и flakiness

## Sources

- Applause.com: «The State of Digital Quality in Testing AI 2026»
- Session with Gemini
- Industry research