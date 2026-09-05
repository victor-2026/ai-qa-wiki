# Product Concept — Mutation Verifier (рабочее название, DRAFT для обсуждения)

**Статус:** DRAFT 2026-09-04, на обсуждение. Выходит за рамки публикации и пилота → при решении "делаем продукт" выносится в новый проект (отдельный репо + AGENTS.md).
**Формат:** по образцу `wiki/weekly-time-planner-prd-example.md` (Описание → Почему не X → Архитектура → Поток → Стек → Оценка → Слабое место), расширено: Цель, Функции, Рамки, Ограничения, План этапов.
**Исходники:** методика `outputs/mutation-matrix-full.md` + `outputs/mutation-matrix-lite.md`, пилоты (`qaeverset-pilot-mini`, OrangeHRM-клоны), `opro gaps/score/prove` как референс поведения.

---

## 1. Концепция (одним абзацем)

Статический open-source калькулятор + чек-лист, который по описанию набора мутаций и результатов прогона считает mutation score, survival rate, recall на пропущенных и выдает вердикт по per-risk-tier гейту — без выполнения кода, без интеграции с раннерами. Доказательство методики — статья + пилот; продукт — внедрение методики в чужие руки.

## 2. Цель

- Через 3 месяца после MVP: 50+ звезд / 10+ внешних применений методики с evidence pack (скрин score + таблица verdicts).
- Проверка гипотезы: командам нужен не еще один раннер мутаций, а независимый способ проверить "тесты реально ловят?" для AI-сгенерированных сьютов.
- Не-цель MVP: никого не убеждать переходить с Stryker/PIT — дополнять их verdict-слоем.

## 3. Почему не существующее

| Существующее | Чего не хватает для нашей задачи |
|---|---|
| Stryker / PIT / universalmutator | Считают score внутри раннера, но не дают per-risk-tier вердикта и не работают без интеграции (Playwright у `opro prove` — unrunnable, мы в это уперлись) |
| `opro gaps/score` (OrangePro) | Отличный референс поведения (deterministic, metadata-only), но чужой продукт, привязка к их графу и BYOK-ключам |
| QAEverest Trust Scorecard | Вендорный, закрытый, методология не раскрыта (наш вопрос Rupesh про порог без ответа) |
| Руками + чек-лист (сейчас) | Работает для публикации, не масштабируется: каждый считает в своей таблице, вердикты несравнимы |

Вывод: ниша — **раннер-независимый калькулятор вердиктов**, а не еще один мутатор.

## 4. Функции MVP (v0)

**Must (без этого не MVP):**
1. Ввод: CSV `behavior,mutation,operator,risk_tier,expected,actual` (формат как `requirements.csv` + колонки результата; пример из M6-M9 в комплекте).
2. Расчет: mutation score, survival rate, recall на пропущенных (nightly full vs subset, бар Facebook 99.9% на change-level), разбивка по risk tiers.
3. Вердикт: per-risk-tier gate (tier-1 high: 0 survived → BLOCK; tier-2: порог; tier-3: trend) + список "что чинить первым" (как `top_risk_gaps`, но из наших данных).
4. Вывод: `evidence pack` (md + json): таблица verdicts + RACI sign-off блок (из Julia Pottinger PR-шаблона) + `Reviewer of record`.
5. Чек-лист ревью методики (5 вопросов Gulin + C/P partition из bug-fix-paradox) как встроенный gate перед расчетом.

**Later (не MVP):**
- v1: `prove-loop` для vitest/jest (паттерн `opro prove`, только JS-юниты; Playwright не пишем — out of scope навсегда или до чужого PR).
- v2: импорт из `opro gaps --json` / Stryker JSON как вход (интеграция чтением, не выполнением).
- v3: GitHub Action-обертка (читает CSV из артефактов, постит вердикт в PR).

## 5. Рамки (scope)

**Внутри:** статика, детерминизм (same input → same verdict), metadata-only (никакого кода пользователя никуда не отправляем), CLI + выдача md/json, MIT.
**Снаружи:** выполнение тестов, генерация мутантов, поддержка Playwright-раннера, хостинг/SaaS, приватность данных чужих репо (их проблема — мы ничего не храним).

## 6. Ограничения

- Без интеграции с выполнением: вердикт настолько хорош, насколько честны входные данные (garbage in — как и у `opro gaps`).
- Порог tier-2 (типа "допустимо N survived") — методологический спор с Rupesh не закрыт; в MVP порог конфигурируемый, дефолт строгий.
- Затраты: разработка в free-режиме (openrouter/free, 1$/день лимит); CI примера — на GitHub free minutes.
- Время автора: продукт не должен съесть Article 26/27 и диссертацию по пилотам — MVP только после публикации методики.

## 7. Архитектура и стек (предложение)

```
mutgate/  (новый репо, свой AGENTS.md)
├── cli.py (или node, один файл, zero-deps кроме stdlib) — parse CSV → calc → verdict → md/json
├── templates/ — mutation-matrix-lite/full, requirements.csv, evidence-pack.md
├── examples/ — M6-M9 (qaeverset-mini, anonymized pilot-mini-5), demo-math vitest
└── .github/workflows/ — self-check: калькулятор считает свой же example (догфудинг)
```

Стек: Python stdlib (как `wiki_llm.py` — уже наш стандарт) или Node (если хотим переиспользовать в JS-командах); без фреймворков, без сервера. Почему Python: вся наша тулинг-цепочка уже на нем, `openrouter-guard.sh` рядом.

## 8. Поток пользователя

1. User копирует `templates/requirements.csv`, заполняет 5-15 строк (behavior, mutation, expected/actual).
2. `python mutgate.py results.csv` → `verdict.md` + `verdict.json`.
3. User вставляет таблицу в PR + блок `Reviewer of record`, прикладывает как evidence pack.
4. При споре с вендором (как с Rupesh/QAEverest) — вердикт воспроизводим третьей стороной из того же CSV.

## 9. Оценка

| Задача | Время |
|---|---|
| CSV-парсер + расчет (score/survival/recall по tiers) | 3-4ч |
| Вердикты + evidence pack md/json + RACI блок | 2-3ч |
| Чек-лист-гейт + примеры M6-M9 + догфудинг CI | 2ч |
| README + скрин для Article 26 | 1-2ч |
| **Итого MVP** | **8-11ч (2-3 вечера)** |
| С Pi worker + reviewer | ~6-8ч (проверено: reviewer ловит P0) |

## 10. Слабое место / риски

- **Главный:** калькулятор без выполнения доверяет входу — вендор может нарисовать CSV. Митигация: evidence pack требует `Reviewer of record` + сырые логи (как Zalando: lineage, а не вера).
- Порог tier-2 станет предметом споров (как с Rupesh) — держим конфигурируемым, дефолт публикуем открыто.
- Нейминг-коллизии: Trust Score (Rupesh), Proven (OrangePro) — не использовать эти слова в бренде.
- Скоуп-крип: "а давайте еще и мутанты сами сеять" — нет, это v-never без отдельной концепции.

## 11. План этапов

| Этап | Что | Статус |
|---|---|---|
| Pilot | M6-M9 на клонах, Proven-демо 670ms, OrangeHRM 122 behaviors | ✅ done 2026-09-03 |
| Article 26/27 | Публикация методики + evidence (Ng gyn5e цитата — примечание уже в файлах) | 🔄 draft, примечание добавлено |
| MVP v0 | Чек-лист + калькулятор (этот PRD) | ⏳ решение после статей |
| v1 | + prove-loop vitest/jest (optional) | 💡 backlog |
| v2/v3 | + импорты (opro/Stryker JSON), GitHub Action | 💡 backlog |
| Product | Новый репо + AGENTS.md + MIT + Pages-демо | ⏳ после MVP-сигнала (10+ применений) |

Правило перехода: MVP кодим только если Article 26/27 дали ≥3 внешних вопроса "а как посчитать самим?" — иначе достаточно чек-листа в статье.

## 12. Варианты названия (на обсуждение)

| # | Вариант | За | Против |
|---|---|---|---|
| 1 | **MutGate** | Коротко, gate = суть (per-risk-tier gate), .io свободен вероятно | "Mut" режет слух не-QA |
| 2 | **Verdict** | verdict layer — наш термин из статей; `verdict.md` как артефакт | Общее слово, занято в npm наверняка |
| 3 | **KillRate** | Метрика в имени (kill rate = 1 - survival); понятно QA | Узко (только rate, а у нас еще tiers + RACI) |
| 4 | **ProofGate** | Proven tier + gate; близко к OrangePro-лексике (понятно их аудитории) | Коллизия с Proven (OrangePro) |
| 5 | **CheckMut** | Чек-лист + mutation; дружелюбно | Звучит как линтер, слабее |
| 6 | **NoSurvivors** | Меморабельно, суть (0 survived в tier-1) | Шутливое для enterprise |
| 7 | **Evidence Gate** | evidence pack — наш артефакт; серьезно | Длинно, два слова |
| 8 | **MutLens** | "Линза" на мутации (как risk profiling — линза, не покрытие) | Меньше про gate |

Рекомендация автора: **MutGate** (продукт) + артефакт `verdict.md` (термин Verdict живет внутри, без коллизий). Запасной: KillRate.

---

## Вопросы на обсуждение

1. MVP после статей или параллельно? (автор: после — правило перехода выше)
2. Python stdlib vs Node? (автор: Python — наш стандарт)
3. Название: MutGate vs твой вариант?
4. Порог tier-2 дефолт: 0 survived (строго) или N? ~~(спор с Rupesh не закрыт)~~ → **частично закрыт письмом 04.09 09:31:** strict-0 подтвержден для High (B0/B1 — recorded decision НЕ проходит zero-tolerance tier; no-op = seeder defect, pre-seed refusal, не accept-risk). Для Medium (B2, наш tier-2) дефолт открыт: band ≤5% vs vendor 1/60 — тюнить по live-данным.
5. Новый репо сейчас (скелет) или после MVP-сигнала? (автор: после — пока `outputs/` достаточно)
