# Pilot metrics template: hook-first locator policy, before/after

Заполнять по релизам: 3 релиза ДО + 3 ПОСЛЕ (минимум 2 после). Один ряд = один релиз.

```csv
release,period,e2e_runs_total,e2e_runs_failed,break_rate_pct,repair_hours_per_break,flaky_rate_pct,survival_rate_pct,escape_count,hook_coverage_elements_pct,hook_coverage_tests_pct,ci_rerun_minutes,notes
R-3,before,,,,,,,0,,,,
R-2,before,,,,,,,0,,,,
R-1,before,,,,,,,0,,,,
R+1,after,,,,,,,,,,
R+2,after,,,,,,,,,,
R+3,after,,,,,,,,,,
```

## Определения (не менять mid-pilot)

- **break_rate_pct** = 100 * failed_runs / total_runs (E2E suite, CI).
- **repair_hours_per_break** = среднее часов человек (QA+дев) на починку одного упавшего E2E до зеленого.
- **flaky_rate_pct** = 100 * тесты, менявшие исход без изменения кода / всего тестов.
- **survival_rate_pct** = 100 * тесты без модификаций, прошедшие релиз / всего тестов.
- **escape_count** = прод-баги, которые E2E должен был поймать (штуки, не %).
- **hook_coverage_elements_pct** = % критических элементов с data-test-id.
- **hook_coverage_tests_pct** = % E2E-тестов, использующих хуки как primary locator.
- **ci_rerun_minutes** = минуты CI на перезапуски упавших E2E за релиз.

## Экономика (считать после 3-го "после")

- Сэкономленные часы = (repair_before − repair_after) × падений.
- Сэкономленное CI = (rerun_before − rerun_after) × релизов.
- Доза-эффект: корреляция hook_coverage_* с break_rate (если хуки не внедрялись где-то — там улучшений быть не должно).

## Правила сбора

- Один человек считает одинаково все 6 релизов (иначе дрейф методики).
- repair_hours — честные, включая "быстро глянул" (минимум 0.25h на инцидент).
- escape_count — только баги в зоне покрытия E2E (вне зоны — отдельной строкой в notes).
