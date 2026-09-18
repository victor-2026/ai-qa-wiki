# Schaper — harness effectiveness check (scheduled re-measurement)

**Источник:** Matthias Schaper (Senior Solution Architect, via Perplexity), LinkedIn ~2026-08. Пост + three-part series. Harness = слой вокруг AI, кодирующий how-I-work (reviewer agents, build pipeline per issue, CI review per PR, autonomous batch runs, real money).

---

## 1. Measured optimization (100 PRs + 750 runs)

- Все на самой дорогой модели; каждый PR — полное ревью; два build-агента ждали друг друга зря.
- 6 изменений: cheap model на checking roles, judgement — на дорогой; ревьюеры перечитывают только новые коммиты после fix-push; test writer параллельно с implementer; cheap worker на batch runs.

## 2. Effectiveness-check issue (главная практика)

- Перед мерджем — issue «effectiveness check, 2026-08-15»: 7 измерений с baseline + hard rule (regressions become own issues) + DUE DATE.
- Тезис: «An optimization without a scheduled re-measurement is a hope». Check date превращает «посмотрим» в deliverable с дедлайном.

## 3. Итог через 3 недели

- Token cost ≈ halved. Time не сдвинулся. Одна из 6 оптимизаций удалена до запуска.

## Связки с нашей работой

- Готовая церемония для наших provisional-порогов (mass-E 5% / mass-obs 10%): effectiveness-check с датой вместо «подтянем когда будет volume». Предложение: датировать recalibration (например, через месяц после 0.2.0) прямо в roadmap.
- Model routing (cheap checker / expensive judge) — третье подтверждение efficiency frontier (Osmani digest, наш free-first): еще одна независимая формулировка.
- «Regressions become own issues» = наш fix-first + append-only discipline.
- Token halved / time flat — money-цифры в банк.
- Вопрос в конце («schedule re-measurement or trust launch-week feeling?») — готовый engagement-хук, standing нет, только evidence.
