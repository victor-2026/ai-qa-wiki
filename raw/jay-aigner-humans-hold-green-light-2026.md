# "Humans hold the green light" — Jay Aigner thread (LinkedIn, 2026-09-15)

**Источник:** Jay Aigner (QA is Dead | CEO @ JDAQA | Host of The First Customer Podcast) + comments
**Тема:** AI-forward команды не могут шипать — verification harness не держит; ответ «прямо сейчас» = люди

---

## Пост (Jay Aigner)

- Вопрос CTO: «Если я дам тебе 100 senior QA бесплатно с бесконечным временем — это решит проблему быстрее, чем то, что ты строишь?» Ответ: «Не вижу причин отказаться».
- Контекст: brilliant bleeding-edge AI guy, «pulling his hair out trying to build a verification harness for 40 engineers. Trying to make AI human enough to test the work of other AI».
- Диагноз: самые AI-forward команды отпинали банку дальше всех — и первыми уперлись в стену. Piles of features they can't ship because they can't test them. 7,000 commits/month and no way out the door.
- «Cute fix» — extra reviewer на PR + feature-level testing с zero integration/system coverage. Не держит.
- Тезис: ответ сегодня = more humans. AI-enabled, surface-area maxed — но green light держат люди.

## Комментарии

### 1. Dan Dunford (AI Architect) — practitioner pipeline
- Manual QA still needed, минимум для exploratory.
- Его пайплайн: Claude строит → прогоняет через свои gates (security, performance, architectural) → сам поднимает Playwright, генерирует test plan против acceptance criteria/user stories → video + screenshot evidence каждого passing кейса.
- **Дыра:** кто тестирует генератор тестов. Self-testing AI = fox guarding the henhouse. Mutation score его сьюта неизвестен.

### 2. Matt Heusser (Consultant, co-author "Software Testing Strategies")
- «Cuz people ask me if it will work, I say no, they throw money at me and ask me to do it again tomorrow?»
- **Смысл:** attestor как бизнес-модель в одну строку. Платят не за тесты, а за право сказать «не шипать».

### 3. Jeffery Evans — market value question
- «We really don't know the market value of testing... we serve at the whim of an engineering manager with directly competing priorities... Why does anyone want to test software?»
- **Смысл:** ценность тестирования не priced. Ответ — per-risk-tier: ценность гейта = цена escaped defect x тир.

## Связки с нашей работой

- Jay «humans hold the green light» = attestation на LIVE runs (QAEverest pilot, per-risk-tier framework v0.3). Терминология разная, суть одна.
- Уточнение к Jay: не «больше людей», а tiered gates — человек держит свет только там, где риск требует (B0/B1), остальное автоматика.
- «Feature-level testing with zero integration coverage doesn't hold» = тема швов (Article 22, seams).
- «7,000 commits/month» — кандидат в money paragraph (со ссылкой на автора).
- Dunford pipeline vs наши пилоты: testRigor (label rename), QAEverest (locator drift) — оба показывают, что self-generated suites ловят свои known paths, но сыплются на мутациях в швах.
- Engagement: reply draft to Dunford (Prong C, один точный вопрос про mutation score) — см. outreach или LinkedIn drafts.
