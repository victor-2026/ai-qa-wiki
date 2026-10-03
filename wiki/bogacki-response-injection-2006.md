# Response Injection: AOP alternative to classical MT (Bogacki & Walter, 2006)

**Source:** `raw/BogackiW06.pdf` (human-added, IFIP SET 2006, Poznan University of Technology)
**Status:** historical foundation (Java/AOP), not directly applicable

## Саммари

Мутанты без компиляции: AspectJ around-advice подменяет return value/exception вызова на лету. Два прохода: capture оригинального flow → прогон тестов на мутант. Замер против Jester: **5.1x весь процесс, 9.3x генерация**. Мотивация дословно наша: "most onerous disadvantage — considerable time to generate, compile mutants and execute test cases".

## Рифма с нашим (зачем храним)

- 2006: cost per verdict снижают убиранием компиляции (5x). 2026: убиранием инференса судьи (JEV-класс, порядки). Одна проблема — цена вердикта — через 20 лет.
- outputs/verdict-economics-ledger.md — наш леджер той же строки расходов (судья $0.04, гейт $0.80/тир).

## Ограничения

- Java/AOP-мир, синтаксические мутанты, академический масштаб (Foo/bar).
- К seeded/API-уровням не применяется; weak/strong-эквивалентность не обсуждается (ср. Offutt weak mutation note).

## Caveat

- PDF с битыми объектами (pypdf warnings), текст извлечен полностью (~25K знаков).
- Цифры 5.1x/9.3x — из их экспериментов vs Jester; MuJava-сравнения у них нет (сами признают).
