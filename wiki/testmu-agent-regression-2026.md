# TestMu agent regression testing (companion to 11-row plan, 2026-09-30)

**Author:** Samyak Goyal (SMTS, TestMu/Kane CLI), reviewer Srinivasan Sekhar (Director Eng, ex-Thoughtworks)
**Published:** 2026-09-30
**Source:** https://www.testmuai.com/learning-hub/agent-regression-testing/
**Status:** vendor guide (Agent Assurance pitch in second half); method part separable

## Саммари

Run-over-run регрессия для агентов: фиксированная сюита, сравнение вердиктов baseline vs candidate. 6 состояний: newly failing (блок релиза), newly fixed (оставить как guard), flaky (не считать, чинить вариацию), changed definition (новый baseline), still failing (known issue в сторону), unverified (вне rate). Ассерты: эффекты (не reply), must-not-call, budgets вместо exact counts, compliance отдельно от quality. Gate на вердиктах из отчета, не на exit code (Rook всегда exit 0).

## Фактура

- Qwen Code CLI, 35 релизов, модель фиксирована: harness-only изменения двигают resolve rate 23.0% → 39.0%. Регрессия живет в харнесе, не в модели.
- Identical Runs (Ariño/Safka, 09.2026): 6 пар × 52 рана — идентичные раны варьируют сильнее, чем пары между собой. Повторы обязательны.
- Токены в том же Qwen-кейсе: 391K → 668K/task (+70%) без роста resolve — ловится budget-ceiling, не pass/fail.
- She-Lin adaptive: 200 вопросов (38.5% полного рана) в пределах 1.03pp полного скора — stratified subset на каждое изменение, полный ран как release gate.

## Дыра: silent-across-versions (наша оценка)

В гайде нет seeded-слоя вообще. Suite, слепая в обеих версиях (silent green сквозит через релизы), этот гейт не поймает никогда: newly-failing не сработает, потому что failing не было ни разу. Run-over-run меряет стабильность зелености, seeded-слой — ее честность. Комплементарны, не конкуренты.

## Связь

- [[testmu-agent-red-teaming-11row-2026]] — тот же авторский коллектив и Agent Assurance; red-team строки + regression-гейт = полный цикл.
- [[ai-qa-tool-evaluation-mutation-matrix]] — seeded-довесок к run-over-run: blind spots внутри версии.
- [[claude-code-48k-junction-incident-2026]] — что бывает без pre-release gates вообще.

## Caveat

- Вторая половина — питч Rook CLI (CI gate, skill install). Методология отделима, продукт не проверялся.
- Raw не заводился: первоисточник — URL выше.
