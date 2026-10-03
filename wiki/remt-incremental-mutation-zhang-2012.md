# Regression Mutation Testing (Zhang/Marinov/Zhang/Khurshid, ISSTA 2012)

**Source:** `raw/regression-mutation-testing-567bsssoq1.pdf` (human-added, 12pp; same text: https://lingming.cs.illinois.edu/publications/issta2012.pdf)
**Status:** foundational (Java/C, static+dynamic analysis)

## Саммари

ReMT: инкрементальные mutation-результаты между версиями программы вместо полного перепрогона. Ядро — dangerous-edge reachability: результат mutant-test переиспользуется, если (1) тест не покрывает dangerous edge до мутированного statement (dynamic coverage) и (2) не может достичь dangerous edge после (новый CFL-reachability статический анализ). Плюс MTP: mutation-specific test prioritization — переупорядочивание тестов на мутант по прошлой kill-эффективности.

## Наш мост: инкрементальность как доктрина

- ReMT = run-over-run для мутантов (ср. TestMu regression companion: baseline vs candidate). Dangerous edges — формализация нашего "что изменилось → что перепрогнать".
- MTP (приоритизация по прошлым kills) — предок нашей ротации/сэмплинга по эффективности.
- Change-impact scoping вместо blind re-run — та же экономика, что stratified subset (38.5% рана) и per-tier сэмплинг.

## Связь

- [[testmu-agent-regression-2026]] — run-over-run гейт; ReMT — его академический фундамент 2012 года.
- [[offutt-weak-vs-strong-mutation]] — соседняя cost-атака (сила vs цена); ReMT — третья ось (инкрементальность).
- [[bogacki-response-injection-2006]] — cost-трилогия десятилетия: компиляция → сила → инкремент.

## Caveat

- Нота по тексту (~71K знаков); цифры speedup в фигурах, не вытащены — не цитировать числа без сверки.
- Java/C, CFG-анализ; к LLM-мутантам не применяется напрямую.
