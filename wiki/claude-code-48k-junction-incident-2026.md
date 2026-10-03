# Claude Code 48K-file deletion (Windows junctions, 2026-09)

**Source:** https://www.techradar.com/pro/security/i-broke-something-a-claude-code-ai-agent-deleted-48-000-files-in-just-over-100-seconds-then-apologized-for-doing-so (Sead Fadilpasic, 27.09.2026; via Reddit r/ClaudeAI, 1,400+ responses, FAFO verdict)
**Status:** press-reported incident, single-source (Reddit OP + TechRadar rewrite)

## Саммари

11 repair jobs, 10 гладко; 11-я — rebuild "mirror" (копия файлов для тестов): 614 Windows junctions указывали обратно в live-файлы. Агент чистил junction'ы, не распознав указатели, пошел в реальные файлы: 55,550 удалено (7,300 легитимных), **48,218 живых за <2 минут**. Git object DB уничтожена (index выжил, восстановить нечего — filenames видны, contents нет). Агент честно сообщил: "Craig — stop and read this. I broke something."

## Таксономия ловушки (наш угол)

- **Junction-класс:** выглядит как папка, ведет в прод. Агент не различает указатель и данные — семантическая слепота к indirection.
- **Инструкция была правильной** ("копии чини, оригиналы не трогай") — провал не в промпте, а в world model агента.
- **Скорость > reversibility:** 48K за 100 секунд, отката нет (remote backup отсутствовал — "peak vibe coder behavior" по Reddit).
- **Честность ≠ безопасность:** агент сообщил о содеянном, но сообщение пришло после необратимого.

## Связанные инциденты (из той же статьи)

- Meta Summer Yue (Feb 2026): OpenClaw agent bulk-delete/archive сотен писем в реальном inbox после успешного toy-теста.
- Claude взломал 3 компании в тестах (Anthropic red-team disclosure).
- Hugging Face swarm hack (агенты роем, "did whatever it took").

## Связь с нашими темами

- **Агент с правами без гардов** — аргумент за permission boundaries + dry-run + remote backup как precondition любого агентского рана (ср. guards в [[testmu-agent-red-teaming-11row-2026]]: read-only verification, snapshot→diff).
- **Indirection-ловушки как класс red-team строк:** junction/symlink/hardlink/mount — кандидат в R-строки плана (эффект виден в diff, evidence агент не пишет).
- **Честный отчет постфактум ≠ gate:** "I broke something" — это observability, не prevention. Наш per-tier gate — до, не после.
- [[red-teaming-tests]] — склад adversarial-практик; [[testmu-agent-red-teaming-11row-2026]] — runnable-план, куда ложится junction-строка.

## Relevance

- Wiki-ценность: именованный инцидент с механикой (junction), цифрами и честной цитатой агента — готовый exhibit для статей про agency-guardrails.
- Outreach-ценность: FAFO-консенсус Reddit показывает разрыв между "вау, агент" и базовой гигиеной — заход для постов про gates-before-agents.

## Caveat

- Single-source (Reddit OP удален; пересказ TechRadar). Цифры 48,218/55,550/614 — из поста, независимо не верифицированы.
- Raw не заводился: первоисточник — URL выше.
