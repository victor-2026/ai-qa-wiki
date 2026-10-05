# TRIP handover — читается первым в каждой новой сессии (после AGENTS.md)

## Кто ты и где
W5, ai-qa-wiki (`/Users/victor/Projects/ai-qa-wiki`). Владелец wiki-слоя, связок и черновиков. Работаешь с мака удаленно (SSH), все файлы локальные.

## Порядок чтения при старте
1. `AGENTS.md` (корень, грузится сам) — границы: wiki/outputs правишь, raw/ НЕ трогаешь никогда.
2. Хвост `session-checkpoint.md` (последние ~30 строк) — текущее состояние.
3. Этот файл — сжатый контекст треков.

## Живые треки (02.10.2026)
- **Paul Kanaris (W1):** раунд 3 — Paul ответил 04.10 3:10 AM (what-vs-why divergence: seeding говорит WHAT, не WHY; invite на compare-notes про gap detecting-vs-understanding). W5-драфт готов, мяч у нас (W1 шлет).
- **Doughty/Touchstone:** коммент отправлен, CEO ответил (traceability). Карточка `outputs/virtuoso-touchstone-card-w1.md`. Мяч у W1.
- **Groetz:** инвайт принят (входящий), первый DM отправлен. Коммент под фид-постом в очереди (тайминг Victor).
- **Crispin:** коммент отправлен (small batches). Части 2–3 на вотче. **Bradshaw:** коммент отправлен. **Aston:** коммент отправлен. **Fabian/Leonardo/Brij:** наблюдение.
- **Megan (аутрич), Danyil (входящий 1st), Sergei Martynov (входящий 1st), Pavel (не писали), Nikita Gavrish:** статусы в чекпоинте.
- **Jason:** отзыв о книге готов (`Positions/.../Jason_Arbon/messages/draft-feedback-2026-09-20.md`), на завтра 03.10 — уточнить канал (DM vs пост).

## Инфра (не трогать без нужды)
- Хуки P0+P1 активны (`~/.config/opencode/plugins/`): raw-guard, secrets-deny, commit-guard (маркер `#owner-approved` только по явному слову Victor; standing cover — чекпоинт/run-log коммиты `add`+`commit` одним вызовом).
- Коммиты/пуши — только по явной команде; чужое (bach-*, mas-vs-swe, satisfice, aiid, s1web, lint-репорты) не стейджить.
- Линт: `python3 wiki_lint.py` (0 битых — норма; орфаны ~50 — системный фон).

## Правила переписки между окнами
- Релейные блоки — с шапкой (`W5 → W_:`, ...). Без шапки — не пересылать.
- Handover текстом в чат, не правками чужих файлов. W1 — коммерция/треки, W2 — verdictgate/продукт, W3 — пилоты/инфра, W4 — статьи/цитаты.

## Открытое на сейчас
- Рестарт подхватил v5 (подтверждено). P2 хуков не начат.
- Хотспот-проба с вин-лаптопа — gate перед отъездом (не моя зона, проверяет Victor).
- PC-Ollama = .209 (старое .224 мертво); мост :11435→:11434; KAN-2 у W3.
