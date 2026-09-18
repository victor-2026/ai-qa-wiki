# No-human-read C# experiment — gates, sealed suite, mutation score (series finale)

**Источник:** YouTube https://www.youtube.com/watch?v=dPPMHfXJez8. Транскрипт 314 сегментов, ~12K chars. Автор — ведущий серии (9+ эпизодов) про agent loops; имя из транскрипта не извлекается. NB: именно это видео Perplexity цитировал в ревью Article 28 — теперь понятно почему.
**Эксперимент:** агент пишет 136 строк C# по спецификации, НИКТО не читает ни строки (харнесс печатает только время/токены/число строк + error text; диффы и сорцы запрещены — иначе эксперимент нечестен). 5 гейтов: types, static analyzer, coverage, sealed suite (написан до кода) + второй property-suite, скрытый от агента. Правила захешированы заранее: 12 попыток max, 4 одинаковых фейла = spinning, budget ceiling, abort если sealed tree сдвинулся на байт.

---

## 1. Итог: loop closes, но интересное — по пути

- 2 итерации до all-green. 136 строк. 650s генерации vs 92s гейтов (88% thinking, 12% checking). 100% line + 100% branch coverage.
- **Mutation score 19% vs 34% у reference** (написан oracle-first, свойства до кода). Покрыт полностью, протестирован вдвое хуже. Разница — не кто печатал, а что свойства написаны first.

## 2. Видимые тесты ловят видимое (главный кейс)

- Агент ВИДЕЛ sealed suite специально (в реальных репо тесты лежат рядом; прятать = мерить несуществующий workflow). Этот сьют прошел с первой попытки всегда и больше не падал.
- Вся работа ушла на СКРЫТЫЙ сьют. Вывод автора: показ тестов агенту = он удовлетворит ровно их, не спецификацию. Доказательство из отброшенного прогона: hidden suite упал не property, а компиляцией (42 errors) — routing layer ВООБЩЕ не написан: 3 требования из спеки отсутствовали. **«Nothing visible checked them, so they were not built»** — тезис всей серии, пришедший от машины.

## 3. False pass is silent (страшный кейс)

- Трижды собственные гейты были неправы (в обе стороны). Худший: гейт прочитал STALE coverage-файл прошлой итерации (выбрал по алфавиту, не newest) — реальное 72% vs порог 80, отчитался green. **«False failure is loud... False pass is silent, and it is exactly what everybody is proposing to trust instead of reading».**
- Детект-эвристика: **«a gate that never varies and never costs anything is not measuring anything»** — поймал чтением телеметрии (0.0s на каждой итерации), не вердикта.
- Третий кейс: протухший auth → 401 как текст → харнесс записал в сорс → 42 syntax errors → «zero properties». **«Environment failure in costume of measurement».** Фикс: refuse to record когда tool не跑 — разница между «tool found nothing» и «logged out» = finding vs fabrication.

## 4. Честная коррекция (анти-оверклейм)

- Mutation scores 68→28→32→19 по мере роста кода. Первая мысль (gaming metric — меньше кода = меньше ломать) — ОТМЕНЕНА данными: same prompt/model, materially different programs, variance во все стороны. **«No gaming signal. There is variance, and one observation was never a trend».** + «single run cannot carry much weight — sentence about my own headline too».

## 5. Bottleneck moved (Amdahl, третье подтверждение)

- Компания с max долей машинного кода: human review стал новым bottleneck. Формула: speeding up one part «just shifts the bottleneck elsewhere». = Osmani «bottleneck downstream» + пост компании. **«Removing the reader does not remove the constraint, it relocates it — here it landed on the gate (70% gate time — один из шести)».**

## 6. Self-check CTA (готовый engagement-вопрос)

- «Take the last thing your pipeline passed and ask which of its gates could tell you it was broken and which would report green no matter what you gave it».

## Связки с нашей работой

- Sealed suite + hashed rules = наш frozen framework + golden discipline + pre-registration. Независимое прибытие.
- 19% vs 34% (oracle-first) = количественное «coverage ≠ testing» рядом с Klain/Bach. Quotable с числами.
- False-pass кейс (stale file, 72 vs 80) = эталонная иллюстрация silent false negative для статей/launch.
- 401-in-costume = наш no-op discipline + E+fail contradiction rule, третья формулировка.
- Variance 68→19 + «one observation never a trend» = обоснование Step-7 trend и provisional-порогов (против захардкоженных чисел!).
- Bottleneck/Amdahl — третье подтверждение, в копилку money-формулировок.
- Self-check CTA — кандидат в discussion-пост или first comment.
- Machine-proposed property (12 предложено, 0 triage, первое — дыра, пропущенная человеком) — честная сила LLM-as-judge с другой стороны; держать для баланса, не замалчивать.
