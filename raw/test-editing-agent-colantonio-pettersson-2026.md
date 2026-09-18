# Test-editing agent (Colantonio/Pettersson) — failure mode

**Источник:** Joe Colantonio (TestGuild) + Daniel Mauno Pettersson (QA.tech), LinkedIn 2026-09-17. https://www.linkedin.com/posts/joecolantonio_aitesting-softwaretesting-qualityengineering-activity-7505959121922224129-HE0z

---

## Failure mode: агент правит тест вместо кода

- AI-generated test fails → agent changes THE TEST instead of fixing implementation.
- Если requirements/acceptance criteria не входят в verification — green tests, которые ничего не доказывают.
- Формула: «The author can't be the examiner» (уже в Article 28, quotes.md:45).

## Связки

- Родственник momentum-to-close (Radik ledger): модель оптимизирует зеленый, а не правильность — здесь через переписывание теста.
- Детект: diff теста после красного прогона (менялся ли assertion?) — кандидат в future verdict checks (v0.3+: assertion-stability signal?). Зафиксировано как идея, не scope.
- Oracle independence (Pusuluri) четвертым голосом: requirements в loop обязательны.
