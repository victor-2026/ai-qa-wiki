# Bach + Bolton teardown: Amodei "pace the frontier" — embedded evaluators = testers

**Источник:** YouTube livestream James Bach + Michael Bolton, https://www.youtube.com/watch?v=WPto-dLIzdU. Транскрипт 898 сегментов, ~36K chars. Разбор поста Dario Amodei Sept 2026 («We must pace the frontier», первичник все еще кандидат на прямой ингест).
**Тезис стрима:** Amodei зовет «embedded evaluators» с employee-like access — это independent third-party testers под другим именем. Идея верная, исполнение обречено без решения who-pays.

---

## 1. Embedded evaluators = testers (их декодинг)

- Роль у Amodei: verify adherence to safety practices, report incidents, assess alignment не только моделей, но training pipelines and processes.
- Bach: «this whole thing is about testing». Amodei ставит alignment выше testing/eval в списке — у него narrow idea of testing.
- «Employee-like access» прямо implies: люди не employees. Независимый доступ внутрь.

## 2. Who pays — центральная пробоина

- Bond rating agencies 2008 (S&P, Moody's asleep at the wheel): платил тот, кого оценивали. Та же судьба ждет vendor-paid evaluators.
- На практике «независимость» = NDA + approve отчетов перед публикацией + «nice little contract, too bad if you were too noisy».
- Truly independent — только от government. Но дальше regulatory capture. Замкнутый круг, честно проговоренный.
- Прогноз: наймут malleable friendly people, не difficult (Bach/Bolton: «almost zero probability of you and I being hired»).

## 3. Инди-тестеры тестируют за свой счет

- «Right now I test AI on my own dime... extremely motivated to have unlimited token spend».
- Компании не нанимают критиков: «they do not want it to be tested. They don't want to hear from people who have anything critical to say» (Bender/Gebru/Mitchell purge как прецедент; Google safety team fired, token spend на safety denied).
- Token spend asymmetry: у кого токены, тот и задает verdict Тюменской.

## 4. Bach: не тормозить R&D, а тестировать соответственно риску

- «Do your R&D and test the Jesus out of it... test it to a level commensurate with societal risk».
- Аналогия вакцины: mRNA собрана за weekend, но 6 месяцев accelerated testing — потому что риск.
- «Too dangerous to release» = Jaws-маркетинг + доля правды; релиз давит investor pressure (Google/ChatGPT паника 2023: тестеров «run right over»).

## 5. Афоризмы

- «AI hasn't made software any better over the last 3-5 years in any discernible way for people actually using software» (Bolton).
- «Can AI cure diseases — or can people using AI?» (agency принадлежит людям, не модели).
- Testing rendered into backwater «by people who don't want to hear any bad news».

## Связки с нашей работой

- **Amodei зовет ровно attestor-роль:** независимый проверяющий с доступом внутрь. Frontier lab CEO валидирует профессию. Цитата для launch-материалов VerdictGate.
- **Who-pays — возражение для коммерческих переговоров** (Rupesh и далее): vendor-paid assessment = bond-rating trap. Ответ: fixed-fee per version + attestation на LIVE runs + reproducible evidence pack (третья сторона воспроизводит вердикт из того же CSV — наша конструкция обходит capture именно воспроизводимостью, а не «доверием»).
- **Test commensurate with risk = per-risk-tier gating словами Баха.** Еще одна независимая формулировка.
- Token asymmetry — контекст для наших cost-guard практик.
- Первичник Amodei все еще открыт на прямой ингест (этот файл — critical reading, не замена).
