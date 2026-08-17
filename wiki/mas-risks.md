---
title: "MAS-Pipeline Риски"
type: article
updated: "2026-08-17"
tags: [compliance, agents]
---

# MAS-Pipeline Риски

**Last Updated:** 2026-04-19
**Sources:** AGENTS.md, three-way-comparison.md, mas-vs-swe-comparison.md

---

## Overview

Риски использования MAS-Pipeline (Multi-Agent System) для автоматизированного QA тестирования.

> **Key Insight:** MAS снижает галлюцинации на ~35%, но добавляет новые риски.

---

## Основные Риски

| # | Риск | Описание | Mitigation |
|---|------|---------|------------|
| 1 | **Groupthink** | Все агенты одной модели → одинаковые слепые пятна | Использовать разные модели для разных ролей |
| 2 | **Fixer Loop Paradox** | Fixer бесконечно исправляет → цикл без выхода | Лимит итераций (max 3) |
| 3 | **Test Suite Erosion** | Покрытие растёт, mutation score падает | Отслеживать mutation score, не только coverage |
| 4 | **RAG Poisoning** | Плохие паттерны сохраняются как "хорошие" в RAG | Периодическая чистка векторной БД |
| 5 | **Objective Drift** | Оптимизация на "тест проходит" → не на качество | Добавить бизнес-метрики в DoD |

---

## Groupthink (Риск #1)

**Проблема:** Все 4 агента используют одну модель (GPT/Claude/Qwen). Ошибки модели одинаковы для всех.

**Симптомы:**
- Все тесты "проходят" но баг не найден
- Модель уверена в неправильном коде
- Critic пропускает очевидные баги

**Решение:**
- Generator: GPT-4o
- Critic: Claude-3.5
- Fixer: Gemini
- Executor: Llama 3B

---

## Fixer Loop Paradox (Риск #2)

**Проблема:** Fixer бесконечно исправляет упавший тест, но не может понять настоящую причину.

**Симптомы:**
- Тест падает/проходит/падает → 10+ циклов
- Fixer меняет random assertions
- Баг не в коде, а в тесте

**Решение:**
```
max_iterations = 3
if iterations > max_iterations:
    escalate_to_human()
```

---

## Test Suite Erosion (Риск #3)

**Проблема:** Coverage растёт (80% → 95%), но mutation score падает (85% → 40%).

**Причина:**
- Тесты "проверяют всё" кроме важного
- Weak assertions (вместо exact — contains)
- Flaky тесты игнорируются

**Метрики:**
```python
quality_score = mutation_score * 0.7 + coverage * 0.3
# good: > 80%
# bad:  < 60%
```

---

## RAG Poisoning (Риск #4)

**Проблема:** Плохие тесты сохраняются в векторной БД → RAG возвращает их как примеры.

**Симптомы:**
- Новые тесты похожи на старые "плохие"
- Mutation score падает со временем
- "Всегда так делали"

**Проверка:**
```
monthly:
    - запустить mutation testing
    - удалить "убитые" тесты
    - перестроить RAG индекс
```

---

## Objective Drift (Риск #5)

**Проблема:** DoD = "тест проходит" → оптимизация на pass, не на quality.

**DoD правильный:**
```yaml
Definition of Done:
  - test passes (boolean)
  - mutation_score > 70% ( качество )
  - no flaky (стабильность)
  - maintainable (поддержка)
```

---

## Summary Table

| Риск | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Groupthink | High | Medium | Different models |
| Fixer Loop | Medium | High | Max iterations |
| Test Suite Erosion | High | High | Mutation score tracking |
| RAG Poisoning | Low | Medium | Monthly cleanup |
| Objective Drift | High | High | Multi-metric DoD |

---

## Рекомендация

1. **Начать с малого:** SWE-Tester (1 агент) → потом MAS
2. **Отслеживать mutation score** — не tylko coverage
3. **DoD с бизнес-метриками** — не только "pass/fail"
4. **Периодический review** — AI + human

---

## Related

- [[wiki/mas-testing-framework]] — Концепция MAS
- [[wiki/three-way-comparison]] — MAS vs SWE vs Applause
- [[wiki/mas-vs-swe-comparison]] — Сравнение MAS и SWE
- [[wiki/testing-stability]] — Anti-flakiness