# Locator robustness via hooks (De Luca/Fasolino/Tramontana, JSS 2024)

**Source:** `raw/robustness of locators GUI.pdf` (human-added, JSS 210, open access CC BY-NC-ND)
**Status:** full text read (~100K chars)

## Саммари

Фраджилити C&R-тестов: 7 типов локаторов × 192 инжектированных layout-изменения на 2 Angular-приложениях. Hook-based локаторы (авто-инжект HTML-атрибутов в темплейты) — меньше breakages чем все 6 остальных техник. Цена инжекта negligible (авто Hook-Injector). Ограничение: только template-based apps. Источник breakages: 73.62% — модификации source (атрибуты/теги/тексты), остальное — behavior/brower.

## Ключевые ходы для нас

1. **"Test breakages" ≠ failures** — их термин чище нашего: breakage = тест сломался, продукт цел.
2. **TKO vs TKOFRA** (SEAA-дека 2022, предшественница JSS): obsolescence (сценарий удален — чинить нечего) vs fragility (нужен, сломался зря). Цифры деки: 214 кейсов, 30 fragility-fails на дефолте vs 0 на hooks (−82% broken, −100% fragility). Алгоритм idempotent + incremental (node.js, TextMate).
2. **3D change classification model** (Object: tag/attr/value/text/template × ...) — таксономия поломок как benchmark. Наш аналог: операторный allowlist; их модель — кандидат на расширение его классификации GUI-поломок.
3. **73.62% breakages из source-модификаций** — эмпирический вес аргумента "дрейф локаторов = главный пожиратель" (QAEverest drift-кейс: та же цифра по смыслу).
4. **Hooks = контракт между тестом и кодом** (data-testid философия, доказанная): стабильность покупается явным контрактом, не умным поиском. Наш пересказ: pre-agreed identification, сестра pre-agreed verdicts.

## Связь

- [[ai-qa-tool-evaluation-mutation-matrix]] — locator drift (M6) как seeded-класс; hooks — дизайн-ответ на него.
- QAEverest Trust Scorecard drift-сигналы — индустриальное подтверждение той же фраджилити.
- REvERSE Naples — группа-источник (вотч).

## Caveat

- Student-made + 2 open-source Angular apps; industrial CI/CD — future work авторов.
- Только template-based; ROBULA+ и др. SOTA — в планах, не в замере.
