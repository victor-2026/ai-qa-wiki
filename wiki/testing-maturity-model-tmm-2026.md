---
title: "Testing Maturity Model (TMM/TMMi)"
type: article
updated: "2026-08-17"
tags: [qa]
---

# Testing Maturity Model (TMM/TMMi)

## Определение

TMM (Testing Maturity Model) — модель оценки зрелости процессов тестирования, аналогичная CMM для разработки. TMMi (Testing Maturity Model integration) — современная версия, разработанная TMMi Foundation.

## 5 уровней TMMi

```
Level 5: Optimization
    └── Continuous process improvement, defect prevention, statistical metrics
Level 4: Management & Measurement
    └── Quantitative metrics, DORA, SLA, measurement-driven decisions
Level 3: Defined
    └── Standardized processes across teams, test policy, test strategy, peer reviews
Level 2: Managed
    └── Basic processes exist: test planning, test design, defect tracking
Level 1: Initial
    └── Ad-hoc, no defined process, success depends on individual effort
```

### Level 1 — Initial
- Нет формального процесса тестирования
- Тестирование = "после разработки"
- Успех зависит от героев, не от процесса
- Нет метрик, нет оценки качества
- **Пример Avito:** Team 1 (нет QA) — вероятно Level 1

### Level 2 — Managed
- Базовые процессы: test planning, test design (test cases documented)
- Defect tracking (баги в Jira/YouTrack)
- Тестирование — отдельная фаза в SDLC
- Метрики: #багов, #пройденных тестов (базовые)
- **Пример Avito:** Team 2 (1 QA, тесты есть) — вероятно Level 2

### Level 3 — Defined
- Стандартизованные процессы тестирования во всех командах
- Единая test policy и test strategy
- Peer reviews тест-кейсов, code coverage gates
- Integration testing между командами
- **Target для Avito:** Level 3 — цель для Test Lead

### Level 4 — Management & Measurement
- Количественные метрики качества: DORA, CFR, MTTR, mutation score
- Measurement-driven decisions: quality gates в CI, релиз по метрикам
- SLA для качества: crash budget, error budget
- Тестирование интегрировано в SDLC, не отдельная фаза

### Level 5 — Optimization
- Continuous process improvement (ретроспективы → data-driven changes)
- Defect prevention (root cause → process change, не просто фикс)
- Статистические методы: trend analysis, predictive analytics
- AI-assisted testing, autonomous quality

## Как использовать на интервью

### Когда спросят про TMM

> «Оценка TMM — не самоцель, а инструмент. Я не начинаю с формального TMM-аудита. Сначала 2-4 недели сбора данных: инциденты, цикли, coverage, satisfaction команд. Потом оцениваю текущий уровень и определяю, какой уровень достижим за 6 месяцев.»

### TMM в контексте кейса Avito

| Team | Текущий уровень | Target | Что делать |
|------|----------------|--------|------------|
| Team 1 | Level 1 (no QA, ad-hoc) | Level 2 (managed) | Внедрить test planning, code coverage, defect tracking |
| Team 2 | Level 2 (1 QA, process есть) | Level 3 (defined) | Стандартизовать process, добавить peer review, contract tests |
| Team 3 | Unknown | Level 3 | Audit → стандартизация |
| DS | N/A | Level 3 | PBT + A/B gates + drift detection |

### Антипаттерны

| Неправильно | Правильно |
|-------------|-----------|
| "Вот TMM Level 3 — это требование, делаем" | "TMM Level 3 — это цель на 6 месяцев, идём phased approach" |
| "TMM audit в первую неделю" | "Сначала данные, потом оценка" |
| "Всем командам Level 3 за 3 месяца" | "Team 1 → Level 2, Team 2 → Level 3, разные темпы" |

## TMMi vs CMMI

| Аспект | TMMi | CMMI |
|--------|------|------|
| Фокус | Тестирование | Разработка (вся компания) |
| Уровней | 5 | 5 |
| Разработчик | TMMi Foundation | CMMI Institute (ISACA) |
| Применимость | QA-функция | Software engineering |
| В Avito | Используется для QA | Есть для разработки |

## Источники

- TMMi Foundation: tmmi.org
- ISTQB Advanced Level — Test Management: process improvement chapters
- Практический опыт: Wimark (Level 1→3 за 2.5 года), Buzzhive (Level 2→3 за 3 месяца)

**Created:** 2026-07-02
