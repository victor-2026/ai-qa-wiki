# Michael Bolton — WHeReAS: critical thinking vs experts (RST)

**Источник:** Michael Bolton (1st connection, Rapid Software Testing), LinkedIn 2026-09-15. Пост + ссылка на статью годичной давности про «experts» и критическое мышление. Триггер: Dario Amodei blog post Sept 2026 (https://lnkd.in/g_XzDfiM — кандидат на ингест) + другие события.
**Контекст:** Болтон уже процитирован в Article 27 («bottles have necks», verified 15.09 из его поста 28.08).

---

## WHeReAS — мнемоника критического мышления (RST namespace)

Critical thinking = thinking about thinking with the goal of avoiding being fooled.

- **Who?** — social dimension (добавлена позже по подсказке коллеги): мотивы, экспертиза, trustworthiness того, кто заявляет. Who says?
- **Huh?** — поняли ли мы вообще утверждение? Новенький в домене путается в языке экспертов — и ошибочно принимает непонятное за экспертное. Может, это просто word salad. Если человек не может прояснить идею понятно — усомнись в экспертизе.
- **Really?** — валидность claims.
- **And?** — что мы могли упустить.
- **So?** — последствия, стоит ли действовать.

## Две ловушки экспертизы

1. **Непонятное ≠ экспертное.** Confusion новичка ≠ глубина говорящего. Проверка — «Huh?»: попроси articulation, нет прояснения — нет экспертизы.
2. **Halo effect.** Эксперт в одном домене ≠ эксперт в другом. Плюс agenda: у заявляющего могут быть political/social/economic последствия, о которых стоит порассуждать до принятия claim.

## Связки с нашей работой

- WHeReAS = готовый протокол human review для findings и sign-off: на каждый vendor claim (100% confidence, 0% risk) — Who? (вендор, заинтересован), Huh? (что именно измерено), Really? (mutation score где), And? (что вне скора), So? (шипаем или нет).
- «Who says?» — прямое обоснование attestor-модели: вердикт вендора о себе ≠ evidence; нужен независимый проверяющий.
- Halo effect → Jay Aigner thread: bleeding-edge AI CTO (эксперт в AI) тянет волосы над verification harness (другой домен). Живая иллюстрация из той же недели.
- «Avoiding being fooled» — вся attestation-теза на языке RST. Мостик между RST-сообществом и mutation-подходом для статей/комментов.
- Amodei Sept 2026 post — новый источник, проверить и при substance ингестить отдельно.
- Engagement: standing есть (цитата verified, 1st). Но после урока Радика — никаких outbound без команды. Draft коммента только по запросу.
