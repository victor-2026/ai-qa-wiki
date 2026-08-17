---
title: "ISO 9001:2015 — Quality Management Systems for QA & Testing"
type: article
updated: "2026-08-17"
tags: [compliance]
---

# ISO 9001:2015 — Quality Management Systems for QA & Testing

## Overview

ISO 9001:2015 — международный стандарт для систем менеджмента качества (QMS), применимый к любой организации. Не software-specific, но его принципы и процессы напрямую отображаются на QA-практики.

### Отличие от ISO 25000
| ISO 9001 | ISO 25000 (SQuaRE) |
|----------|--------------------|
| Организационный QMS | Качество ПО |
| Процессы, риски, улучшение | Характеристики продукта |
| Любая индустрия | Software only |

---

## 7 Quality Management Principles (QMP)

| # | Принцип | Отображение на QA |
|---|---------|-------------------|
| 1 | **Customer Focus** | SPT-обращения = voice of customer. Метрики качества = customer satisfaction |
| 2 | **Leadership** | Test Lead задаёт quality vision, приоритеты, культуру |
| 3 | **Engagement of People** | Вовлечение dev в тестирование (code review, quality gates), не только QA |
| 4 | **Process Approach** | Качество — свойство системы, не команды. Input → Process → Output → Feedback |
| 5 | **Improvement** | CAPA (Corrective and Preventive Action) вместо простого фикса багов |
| 6 | **Evidence-Based Decision Making** | Метрики до/после. Без данных — не решение, а гадание |
| 7 | **Relationship Management** | Team 3 = supplier для Team 2. Контрактные тесты, SLA, соседское соглашение |

---

## PDCA Cycle

**Plan–Do–Check–Act** — центральный цикл ISO 9001. Отображается на любой QA-план:

| Phase | ISO 9001 clause | QA example |
|-------|----------------|------------|
| **Plan** | 6.1 (риски), 6.2 (цели) | Discovery: метрики current state, риски, цели на квартал |
| **Do** | 8.1 (операции) | Quick wins: process, автотесты, quality gates |
| **Check** | 9.1 (мониторинг), 9.2 (аудит) | DORA metrics dashboard, defect leakage tracking |
| **Act** | 10.1 (CAPA), 10.3 (улучшение) | Corrective actions, масштабирование, новый PDCA |

---

## Key Clauses for QA Teams

### 4. Context of the Organization
- **4.1** — понять внешние/внутренние факторы, влияющие на качество
- **4.2** — кто стейкхолдеры: клиенты, саппорт, соседние юниты
- **QA:** анализ current state перед любыми изменениями

### 6.1 Risk-Based Thinking
- Замена reactive («чиним баги») на proactive
- **Риск-реестр:** идентификация, оценка, mitigation
- **QA:** не ждать багов — оценить риски до релиза

### 7.5 Documented Information
- Какие документы обязательны: quality policy, procedures, records
- **QA:** test plans, test cases, bug reports — это documented information
- Версионирование, retention, доступность

### 8.3 Design and Development
- Review, verification, validation на этапе проектирования
- **QA:** ATDD/Три амиго, TDR, acceptance criteria до кода

### 8.4 Control of Externally Provided Products and Services
- Поставщик должен быть оценён и контролируем
- **QA:** Team 3 как supplier → contract tests, SLA, уведомления о changes
- Если платформа меняется без предупреждения — это нарушение 8.4

### 9.1 Monitoring, Measurement, Analysis
- **QA:** метрики качества — defect rate, coverage, MTTR, flaky rate
- Анализ трендов, не только snapshot
- **Evidence-based decision making**

### 9.2 Internal Audit
- **QA:** TMM самооценка, quality audit, peer review
- Периодические аудиты: соответствуют ли команды процессам?

### 10.1 Nonconformity and Corrective Action (CAPA)

**Corrective:** устраняем root cause (не баг, а почему баг появился)
**Preventive:** что сделать, чтобы этот класс багов не повторился

Шаги:
1. Идентификация несоответствия (баг, инцидент)
2. Root cause analysis (LSR/5 Whys)
3. Corrective action (фикс)
4. Preventive action (процессное изменение)
5. Verification of effectiveness
6. Update risk assessment

### 10.3 Continual Improvement
- Качество никогда не финиш — всегда следующий PDCA
- Retro + план на следующий квартал
- **QA:** повторяющийся процесс, не одноразовый проект

---

## Tools & Techniques

| Tool | ISO 9001 clause | When to use |
|------|----------------|-------------|
| **Risk Register** | 6.1 | Первая неделя: оценка рисков каждой команды |
| **RACI Matrix** | 5.3 (roles) | Кто отвечает за тестирование в команде без QA |
| **CAPA Log** | 10.1 | LSR и root cause analysis |
| **PDCA Tracker** | 10.3 | 90-day план как циклы PDCA |
| **Quality Policy** | 5.2 | Краткий документ: что значит «качество» для юнита |
| **SLA / SLO** | 8.4 | Договорённости между командами / с платформой |
| **Audit Checklist** | 9.2 | TMM аудит, quality gates compliance |

---

## How It Maps to Test Lead Role

| Ситуация в кейсе | ISO 9001 lens | Что даёт |
|------------------|---------------|----------|
| Team 1 (0 багов) | 4.4 Process approach | Баги падают на потребителей — процесс не замкнут |
| Team 2 (много багов) | 10.1 CAPA | Не просто фиксить, а CAPA-цикл: root cause → corrective → preventive |
| Team 3 (неизвестно) | 8.4 External provider | Платформа = supplier. Нужен контроль |
| Метрики | 9.1 + 6 (evidence-based) | Структура: диагностика → трекинг → улучшение |
| 90-day план | PDCA | Планируем, делаем, проверяем, корректируем |

---

## Related

- [[iso-27001-qa-testing-2026]] — ISO 27001 (security)
- [[iso-25000-square-quality-2026]] — ISO 25000 (software quality)
- [[improvements-from-bugs]] — CAPA на практике
- [[case-presentation-plan]] — как применено в кейсе Avito








<!-- backlinks-start -->
### Backlinks
- [Iso 13485 Qms Medical Devices 2026](wiki/iso-13485-qms-medical-devices-2026.md)
<!-- backlinks-end -->
