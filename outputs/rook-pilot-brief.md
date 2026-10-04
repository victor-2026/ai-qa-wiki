# Rook pilot brief (for W3 — TestMu Agent Assurance CLI)

W5 → W3: бриф ниже — продукт, done-критерии, предусловия. Исполнение за тобой после подтверждения мишени.

## Что за продукт

Rook CLI (`npm install -g @testmuai/rook`, Node 22+) — раннер Agent Assurance (TestMu, ex-LambdaTest): генерит adversarial + regression сценарии из кода агента (или PRD/спеки), гоняет против staging, грейдит критерии по evidence (tool calls vs declared, file diffs, read-only probes), Unable to Verify — вне rate. Skill для Claude Code (`npx @testmuai/rook-skill`). Сцены/раны/evidence — plain files в репо (`rook scenarios list/exclude/include`). Gate читает `rook report --json` (exit code всегда 0!).

## Пилот-критерий (done = ?)

1. Staging-мишень подтверждена (W1-условие: без мишени пилота нет).
2. Отдельный неймспейс (свой KAN/memory/стенд — правило клонов).
3. Прогнаны: 11-row red-team план + regression gate на мишени.
4. Наш acceptance поверх: засеянные поломки (2–3, known) — ловит ли Rook? (Article-26 линза: seeded breaks как проверка проверяющего.)
5. Выход: вердикты с evidence + Unable-to-Verify policy + решение go/no-go на Rook как инструмент.

## Предпосылки

- Staging-агент под рукой (мишень).
- Node 22+ (Homebrew/shell installer несут свой рантайм).
- Reviewed branch, staging credentials (агент реально пишет!).

## Не делать

- Не гонять на проде (writes are real).
- Не смешивать с D6/бенчем без реприоритезации (очередь W1).
- Mo — вторым, как решено (exhibit only, не инструмент).

## Источники (наши wiki)

- testmu-agent-red-teaming-11row-2026 (R1–R11, OWASP/ATLAS, evidence-таблица).
- testmu-agent-regression-2026 (6 состояний, gate на вердиктах, silent-across-versions дыра).
- red-teaming-tests (хаб).

---
*W5 → W3. Статус: бриф готов, исполнение за W3 после подтверждения мишени.*
