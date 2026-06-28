# LinkedIn Performance Analyzer — DS-подход к контент-аналитике

**Дата:** 2026-06-29
**Контекст:** Применение 4-уровневой модели DS/ML тестирования к анализу LinkedIn-статей

---

## Идея

Перенести ту же методологию, что используем для тестирования DS-моделей (алгоритмы распределения ликвидности), на анализ эффективности LinkedIn-контента:

| Уровень | DS/ML тестирование | LinkedIn Analyzer |
|---------|-------------------|-------------------|
| 1. PBT | Инварианты модели | Инварианты данных: impressions > 0, даты не в будущем |
| 2. A/B gate | Сравнение моделей | Сравнение hashtag-наборов, форматов постов |
| 3. Drift | Мониторинг деградации модели | Падение engagement неделя к неделе |
| 4. Golden dataset | Эталонный набор данных | Бенчмарк: медианные/P90 показатели |

## Что внутри

Go-инструмент, который:
- Читает `performance-log.csv` (44 поста)
- Проверяет качество данных (PBT)
- Ранжирует хэштеги по средним показам
- Сравнивает форматы (article vs carousel vs post)
- Детектит недели с падением engagement (drift)
- Вычисляет бенчмарк (P50, P90, топ hashtags)

## Установка

```bash
go run ./code/linkedin-analyzer/ <путь-к-csv>
```

Без аргумента — использует `testdata.csv` (16 строк, встроенный датасет).

## Результаты по полному датасету

| Метрика | Значение |
|---------|----------|
| Avg impressions | 670 |
| Median (P50) | 337 |
| P90 | 2,150 |
| Avg engagement | 0.64% |
| Best format | article (avg 1,003 imp) |
| Worst format | post (avg 380 imp) |
| Топ hashtag | #TestAutomation, #AIAgents, #Playwright |

## Куда развивать

- CTA/hook analysis — добавить поле hook_type в CSV
- Weekly auto-report — интеграция с LinkedIn API
- Hashtag clustering — какие хэштеги работают вместе
- Engagement prediction — baseline для новых постов
