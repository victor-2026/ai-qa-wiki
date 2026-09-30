# The QA AI Engineer: role definition from live postings (Alden Mallare, 2026-09-29)

**Author:** Alden Mallare (Principal Test Architect, Uturn Data Solutions)
**Published:** 2026-09-29
**Source:** https://www.linkedin.com/pulse/qa-ai-engineer-what-role-actually-do-all-day-alden-mallare-njvcc/

## Саммари

Статья фиксирует момент, когда "QA AI Engineer" перестал быть маркетинговым ярлыком и стал строкой в живых вакансиях: Xpansiv, GE Vernova, Orion Innovation, AI71 (defense/enterprise). Ядро тезиса: премия ~$39K (анализ 17K+ постингов, InterviewStack.io, May 2026) платится не за умение пользоваться AI-тестинговыми тулами, а за умение тестировать сам AI. Ключевое определение (AI71): "define what good looks like for non-deterministic AI systems" - человек, который строит стандарт корректности для софта без единственно верного ответа, а потом доказывает соответствие.

## Пять категорий задач (повторяются во всех posting'ах)

1. **Detecting AI-specific failure modes** - hallucinations, prompt injection, inconsistent outputs, formatting errors, data leakage, bias, unsafe responses, regressions от model/prompt update. Xpansiv перечисляет поименно.
2. **Building evaluation frameworks, not just running tests** - golden datasets, model-graded assertions, prompt regression suites, quality scorecards с нуля. Архитектура измерителя, а не исполнение.
3. **Validating the full system around the model** - RAG pipelines, agents, structured outputs, API и document workflows. Галлюцинация может родиться в retrieval-шаге, а не в модели - различать источник обязан тестер.
4. **Owning go / no-go decisions** - Xpansiv: quality gates и readiness criteria на пилоты, беты, релизы и каждый model/prompt update. AI71: Test Readiness Reviews + Functional Configuration Audits до деплоя. Sign-off реально останавливает релиз.
5. **Generating synthetic test data at scale** - промпт модели вместо ручных кейсов: объем выше, privacy exposure ниже.

## Три столпа навыков + инвентарь из четырех блоков

Столпы: (1) traditional QA judgment - что считать провалом, скоринг риска; (2) AI/ML literacy - как ломаются LLM, RAG изнутри, плохой промпт vs плохая модель; (3) systems building - построить harness, а не оперировать чужим (самый дефицитный).

Инвентарь (самопроверка из статьи): QA judgment and testing strategy (risk-based prioritization, root cause, go/no-go); traditional QA (functional/regression/API, exploratory, Playwright/Selenium); AI/ML literacy (failure modes, prompt engineering, RAG, probabilistic output); AI evaluation and systems building (golden datasets, model-graded eval, synthetic pipelines, regression suites, red teaming).

## Рыночный контекст

- Премия концентрируется в "build for AI" слое (AI как фича продукта), а не в "ambient" слое (команды просто пользующиеся AI-тулами).
- Роль уже на бордах: Xpansiv (Lever), GE Vernova (The Muse), Orion Innovation (Built In, 2025), AI71 (Greenhouse). Ссылки на все четыре постинга - в источниках статьи, проверяемы.
- Соседние статьи автора за август-сентябрь 2026: Planner/Generator/Healer в Playwright, "Your DORA Metrics Are Lying", "Confidence Level Testing", "The QA Team Is Shrinking" (самая живая: 47 лайков, 9 комментов).

## Связь с нашими темами

- **AI71-определение = наша oracle/verdict-проблема их словами.** "Define what good looks like" - это постановка задачи VerdictGate; наш ответ (per-risk-tier gate + mutation check) - то, чего в статье нет.
- **Зазор статьи: проверка самого измерителя отсутствует.** Golden datasets, model-graded eval, scorecards - все про измерение; ни слова про silent green, проверку судьи мутациями, misses on both sides. Сюда встает [[ai-qa-tool-evaluation-mutation-matrix]] и VerdictGate: кто проверяет scorecard.
- **Go/no-go per model update = per-risk-tier gate.** Xpansiv требует gate на каждый model/prompt update; наш фреймворк дает градацию строгости по тирам (B0 zero и т.д.). Статья - рыночное подтверждение спроса на такой gate.
- **Golden datasets + model-graded eval** - связка с [[qawolf-beyond-golden-datasets-2026]] и [[autonoma-llm-evals-cicd-2026]]: как строят измеритель другие.
- **Adversarial testing / red teaming** - связка с [[red-teaming-tests]] и [[loris-bartolini-jean-yves-garcin-banking-rag-adversarial-testing-2026]].
- **Кросс-волт:** Articles vault - статьи 26 (оценка вендоров через 5 сценариев поломок) и 27 (guided QA engineer: risk/oracle/sign-off); Positions-CV-CL vault - Alden Mallare как контакт-наблюдение (enterprise-архитектор, пишет про то же поле).
- **Кандидат в цитаты:** "define what good looks like for non-deterministic AI systems" (AI71, через Alden) - короткое определение роли для quotes-банка статей.

## Relevance

- Wiki-ценность: первое в базе определение роли QA AI Engineer из живых вакансий + проверяемые ссылки на 4 постинга + готовый скилл-инвентарь для самопроверки.
- Outreach-ценность: Alden пишет каждые 2-3 дня про то же поле (Playwright-агенты, DORA, confidence testing) - теплый кандидат на peer-контакт после комментария.

## Caveat

- Цифра $39K - из вендорского анализа (InterviewStack.io, рекрутинговая площадка): направление верное, точное число воспринимать как ориентир, не факт.
- Вакансии цитируются через статью, первоисточники (Lever/Muse/Built In/Greenhouse) не открывались - перед цитированием в своих статьях проверить живьем.
- raw/-сырец не заводился (raw пополняет человек): первоисточник - URL статьи выше.
