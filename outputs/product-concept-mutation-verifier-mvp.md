# Product Concept — Mutation Verifier (рабочее название, DRAFT для обсуждения)

**Статус:** ПРИНЯТ к исполнению 2026-09-15: имя verdictgate, приватный репо до публикации Article 27 (см. §11-12). Изначально DRAFT 2026-09-04.
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
| oracle-gate (Jott2121, Jul 2026) | Философски ближайший сосед: Tier 1-4 gates + mutation как G2 + evidence packages + conformance-валидатор — но это framework/spec, не калькулятор вердиктов из записанных результатов CSV; полезен как строка Why-not-X и как независимое подтверждение tier-gate конвергенции |

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

**Внутри:** статика, детерминизм (same input → same verdict), metadata-only (никакого кода пользователя никуда не отправляем), CLI + выдача md/json, MIT. **Три сигнала раздельно, не схлопывать:** ranking (где слабо) vs mutation (ловит ли тест) vs drift (хрупок ли сам тест) — требование из переписки с Aamir 2026-09-07: схлопывание дает результат чище, чем он есть.
**Снаружи:** выполнение тестов, генерация мутантов, поддержка Playwright-раннера, хостинг/SaaS, приватность данных чужих репо (их проблема — мы ничего не храним).

## 6. Ограничения

- Без интеграции с выполнением: вердикт настолько хорош, насколько честны входные данные (garbage in — как и у `opro gaps`).
- **Версионирование скорера обязательно:** 0.2.34 → 0.2.40 на тех же данных дали чуть другой ранкинг (своп #3↔#4, OrangeHRM 2026-09-07) — каждый вердикт штампует версию калькулятора, иначе дельты необъяснимы.
- Порог tier-2 (типа "допустимо N survived") — методологический спор с Rupesh не закрыт; в MVP порог конфигурируемый, дефолт строгий.
- Затраты: разработка в free-режиме (openrouter/free, 1$/день лимит); CI примера — на GitHub free minutes.
- Время автора: продукт не должен съесть Article 26/27 и диссертацию по пилотам — MVP только после публикации методики.

## 7. Архитектура и стек (предложение)

```
verdictgate/  (новый репо victor-2026/verdictgate, свой AGENTS.md)
├── verdictgate.py (один файл, Python stdlib, zero-deps) — parse CSV → calc → per-tier gate → verdict md/json
├── templates/ — mutation-matrix-lite/full, requirements.csv, evidence-pack.md
├── examples/ — M6-M9 (qaeverset-mini, anonymized pilot-mini-5), demo-math vitest
└── .github/workflows/ — self-check: калькулятор считает свой же example (догфудинг)
```

Стек: Python stdlib (как `wiki_llm.py` — уже наш стандарт) или Node (если хотим переиспользовать в JS-командах); без фреймворков, без сервера. Почему Python: вся наша тулинг-цепочка уже на нем, `openrouter-guard.sh` рядом.

## 8. Поток пользователя

1. User копирует `templates/requirements.csv`, заполняет 5-15 строк (behavior, mutation, expected/actual).
2. `python3 verdictgate.py results.csv` → `results.verdict.md` + `results.verdict.json`.
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
| Pilot | M6-M9 на клонах, Proven-демо 670ms, OrangeHRM 122 behaviors; внешняя валидация Aamir 2026-09-07 (снапшот→реран протокол, три сигнала раздельно) | ✅ done 2026-09-03/07 |
| Article 26/27 | Публикация методики + evidence (Ng gyn5e цитата — примечание уже в файлах) | 🔄 draft, примечание добавлено |
| MVP v0 | Чек-лист + калькулятор (этот PRD) | 🔄 started 2026-09-15: verdictgate, приватный репо; публичность после Article 27 |
| v1 | + prove-loop vitest/jest (optional) | 💡 backlog |
| v2/v3 | + импорты (opro/Stryker JSON), GitHub Action | 💡 backlog |
| Product | Новый репо + AGENTS.md + MIT + Pages-демо | ⏳ репо создан раньше плана (приватно, 2026-09-15, override юзера); публичность + Pages после Article 27; сигнал 10+ применений остается метрикой для v1 |

Правило перехода: MVP кодим только если Article 26/27 дали ≥3 внешних вопроса "а как посчитать самим?" — иначе достаточно чек-листа в статье.

## 12. Варианты названия (на обсуждение)

| # | Вариант | За | Против |
|---|---|---|---|
| 1 | ~~MutGate~~ | ~~коротко, gate = суть~~ | ❌ КОЛЛИЗИЯ (проверено 2026-09-15): PyPI `mutgate` v0.1.1 (JimGalasyn, опубликован 2026-09-08, активный — named mutations as contracts, sandbox-исполнение, CI+codecov+DOI); GitHub `mutation-gate` (pre-commit gate на mutmut); `mutago` (Go) — вся mut+gate окрестность занята |
| 2 | **Verdict** | verdict layer — наш термин из статей; `verdict.md` как артефакт | Общее слово, занято в npm наверняка |
| 3 | **KillRate** | Метрика в имени (kill rate = 1 - survival); понятно QA | Узко (только rate, а у нас еще tiers + RACI) |
| 4 | **ProofGate** | Proven tier + gate; близко к OrangePro-лексике (понятно их аудитории) | Коллизия с Proven (OrangePro) |
| 5 | **CheckMut** | Чек-лист + mutation; дружелюбно | Звучит как линтер, слабее |
| 6 | **NoSurvivors** | Меморабельно, суть (0 survived в tier-1) | Шутливое для enterprise |
| 7 | **Evidence Gate** | evidence pack — наш артефакт; серьезно | Длинно, два слова |
| 8 | **MutLens** | "Линза" на мутации (как risk profiling — линза, не покрытие) | Меньше про gate |

**Решение 2026-09-15: `verdictgate`** (PyPI/npm/GitHub свободны, проверено). Вердикт = coined term серии + артефакт verdict.md + ниша §3 ("раннер-независимый калькулятор вердиктов"); полный выход из mut-окрестности — фича, не баг: мы НЕ исполнитель (в отличие от mutgate/mutation-gate/mutago), и поиск должен нас разделять. CLI: `verdictgate results.csv` → `results.verdict.md/json`. Plan B: tiergate. Перебор проверен: mutgate (занят), mutation-gate (занят), mutacalc/tiergate/verdictgate/survivalgate/mutation-matrix-evaluator (свободны).

---

## Вопросы на обсуждение

1. ~~MVP после статей или параллельно?~~ → ✅ РЕШЕНО 2026-09-15: started после публикации Article 26 (14.09); работа параллельно с телом 27-й; публичность репо после 27-й. Override правила "≥3 внешних вопроса" — юзер 2026-09-15 (момент: quadruple validation + 4 CEO подтвердили метод).
2. ~~Python stdlib vs Node?~~ → ✅ Python stdlib (verdictgate.py, один файл).
3. ~~Название~~ → ✅ verdictgate (см. §12, коллизии проверены).
4. B2 Medium: **зафиксирована Позиция C** — дефолт строгий (≤5% при N≥20 / max 1 + recorded decision при N<20), вендорский вариант (1/60) = именованный профиль для сравнительных прогонов (в v0.2+); B0/B1 zero-tolerance неконфигурируем. Финальное решение после Article 27 / первой платной аттестации.
5. ~~Новый репо сейчас или после MVP-сигнала?~~ → ✅ override юзера 2026-09-15: приватный репо сейчас (victor-2026/verdictgate), публичный после Article 27.
