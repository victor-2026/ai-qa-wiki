# The Outside Eye: independent AI assurance consortium proposal (Tony Zaccarini, 2026-09-29)

**Author:** Tony Zaccarini (working proposal, individual + AIs)
**Published:** 2026-09-29 (summarised version, 6 pages)
**Source:** `raw/TonyZaccarini-The-Outside-Eye.pdf` (local, human-added)
**Status:** PROPOSAL — no operating consortium, no certified orgs, no live Kill Switch; website/app are demonstrations. Rights reserved (cite with attribution, no commercial adaptation).

## Саммари

Предложение независимого assurance-консорциума: помогать людям понимать влияющие на них AI-системы, проверять evidence за клеймами и видеть, что произойдет при остановке системы. Три связанные части: прозрачный публичный реестр, AI Facts Label на систему, governed Kill Switch procedure. Честная оговорка автора: начинать надо с публичной записи ("evidence requested", "assessment pending", "Kill Switch untested"), а не с вида свершившейся проверки.

## Три части

1. **Public register** — запись: система, оператор, применение, предоставил ли оператор evidence. Листинг возможен без вступления оператора (identity + use проверены, публикация fair). Сертификаты входят со scope: сертификат процессов ≠ доказательство безопасности конкретного деплоя.
2. **AI Facts Label** — лейбл на систему (что проверено, что неопределенно).
3. **Governed Kill Switch** — процедура остановки с 48h duty (только для подписавших соглашение), witnessed stop-and-fallback test, публикация исхода. Ключевое различие статусов: "Kill Switch notice issued" vs "operator stop verified".

## Инженерия честности (ядро ценности)

- "Оператор сказал «остановил»" записывается как report, пока не verified.
- Видимая история исправлений, записываемые конфликты и dissent-мнения.
- "Payment must not buy a favourable finding" — платные assessment/testing/monitoring с раскрытием fees и интересов, решения отделены от коммерции.
- Демо маркируются как демо, пока нет людей, соглашений, техтестов и операционки.
- Находки датируются, ревьювятся после материальных изменений, выводы expirty'ятся.

## План и открытые вопросы

- 2 недели: scope, поля case file, значения статусов, правила отличия proposal от live.
- Месяц: операторы, специалисты, байеры, фандеры + legal/privacy review правил.
- ~90 дней: первые точные case files (первая запись может быть просто "evidence requested"); при согласии — независимая оценка и witnessed stop-and-fallback тест.
- Не решено: юрлицо и фандинг, Code of Ethics + 48h obligation, порог жалоб и urgent route, состав панели и конфликты, приватность и handling evidence, техметод стопа и верификации на деплой.

## Связь с нашими темами

- **Claim vs evidence дословно наша граница.** "Report until verified" — то же правило, что и к вендорским green-отчетам (статьи 26/27, VerdictGate): заявление есть, доказательства нет — вердикта нет.
- **Kill Switch verification ≈ abort authority из скетча Полу** (seed-test protocol): остановка считается только witnessed + fallback работает. [[ai-qa-tool-evaluation-mutation-matrix]] — матрица как внешний оракул той же природы.
- **Gaps-first на уровне института.** Видимые дыры ("Kill Switch untested") вместо витрины — зеркало нашего "report gaps first, then the verdict".
- **Evidence-цепочка Доути/Touchstone:** реестр + Label — та же идея трассируемости (objective → evidence), но с независимым координатором вместо вендора.
- **Вопрос Тони — наш вопрос:** "what evidence would convince you that oversight can intervene?" Ответ W1: seeded break, о котором надсмотрщики не знали — интервенция по evidence, а не по расписанию (драфт коммента у W1, отправка за Виктором).
- **Кросс-волт:** Positions-CV-CL vault — контакта нет (3rd+, диалога нет — карточку не заводим, правило Rinat); Articles vault — кандидат в банк цитат W4.
- [UK DSIT Introduction to AI assurance (2024)](wiki/dsit-ai-assurance-guide-2024.md) — государственная рамка assurance-техник, в которую ложится консорциум.

## Relevance

- Wiki-ценность: первый в базе governance-консорциум с прописанной процедурой Kill Switch и моделью честных статусов — референс для разговоров про oversight на уровне институтов, не команд.
- Outreach-ценность: автор просит фидбек у assurance/governance/testing — warm-вход через ответ на его вопрос (без питча, peer).

## Caveat

- Живого ничего нет: ни участников, ни сертификации, ни свитча. Цитировать только как proposal с датой.
- Права зарезервированы: атрибуция обязательна, коммерческая адаптация — только письменным соглашением.
- Raw-PDF добавлен человеком 01.10.2026 — цепочка raw→wiki чистая.
