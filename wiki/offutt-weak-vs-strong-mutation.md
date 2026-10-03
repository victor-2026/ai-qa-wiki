# Weak vs strong mutation (Offutt & Lee, Clemson — via Mothra/Leonardo)

**Source:** `raw/how-strong-is-weak-mutation.pdf` (human-added, 14pp, ACM 10.1145/120807.120826)
**Status:** foundational experiment (Fortran, interpreter-based)

## Саммари

Сравнение strong mutation vs 4 weak-вариантов (EX-WEAK, ST-WEAK, BB-WEAK/1, BB-WEAK/N) на интерпретаторе Leonardo (из Mothra, все 22 оператора). Вывод: weak почти так же эффективен со значительной экономией; неожиданно small components (ST/BB-1) сильнее large (BB-N); универсальной формулы перевода weak-score → strong-score нет (зависит от программы). Рекомендация: ST-WEAK (сравнение состояния сразу после мутированного statement) для non-critical; для critical — strong или комбинация (weak first, strong на остаток — дешевле чистого strong).

## Наш мост: tiered strength (забрать в доктрину)

- Эксперимент 90-х легитимирует нашу per-tier экономику: слабая (дешевая) проверка на низких тирах, сильная на B0. Weak-first + strong-на-остаток = буквально наш сэмплинг по тирам.
- "No universal translation formula" — аргумент против единого mutation score поперек тиров (ср. Mapping Limit: numbers, not gate shapes).
- Overhead-замечание: 80–90% времени Mothra — не техника, а дизайн системы (setup/apply). Наш аналог: инференс судьи, не матрица.

## Связь

- [[bogacki-response-injection-2006]] — соседняя cost-атака того же десятилетия (компиляция vs интерпретация).
- [[ai-qa-tool-evaluation-mutation-matrix]] — tiered operators как индустриальный наследник weak/strong сплита.
- outputs/verdict-economics-ledger.md — cost per verdict строка.

## Caveat

- Fortran, интерпретатор, академические программы (Euclid, Bubblesort...); переносить осторожно.
- Нота по тексту (~44K знаков), таблицы/гистограммы не сверялись.
