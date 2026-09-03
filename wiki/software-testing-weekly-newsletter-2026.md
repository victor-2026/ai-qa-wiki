# Software Testing Weekly — обзор ресурса

**URL:** https://softwaretestingweekly.com
**Основатель:** Dawid Dylowicz (LinkedIn)
**Формат:** Email-дайджест, еженедельно, бесплатно
**Подписчики:** 9,200+ тестировщиков
**Архив:** https://softwaretestingweekly.com/issues/ (325+ выпусков, с 2020)
**Частота:** еженедельно (Ср)
**Подписка:** email

---

## Структура выпуска

| Раздел | Описание |
|--------|----------|
| **News** | Статьи о QA-стратегии, AI в тестировании, roles, mindset |
| **Automation** | Практические статьи по автоматизации, фреймворки, подходы |
| **Tools** | Инструменты, playground-проекты, релизы |
| **Books** | Обзоры книг по тестированию |
| **Videos** | Видео-туториалы, обзоры |

---

## Анализ выпуска #325 (01 Sep 2026) — ТОП-10 статей

### 1. Apparently We Need a Testing Mindset After All (Keith Klain)
**Источник:** qualityremarks.com
AI строит — а кто проверяет? Новые исследования доказывают, что testing mindset был правильной идеей всё время. Связывает с judge bias при оценке AI-кодом.
**Релевантность:** ★★★★★ — Актуально для AI QA governance и human review gate.

### 2. Your QE Program Has a Structural Problem, and AI Just Made It Visible (Rick Crawford, Postman)
**Источник:** blog.postman.com
6 структурных проблем QE-программы, которые ускоренная доставка кода делает видимыми. Серия из 3 статей: pipeline metrics + platform strategy.
**Релевантность:** ★★★★★ — Системный взгляд на QE gaps; подходит для Антона Гулина context.

### 3. Who Is Accountable for AI-Generated Code? (Julia Pottinger)
**Источник:** juliapottinger.com
Простой тест: можешь ли ты подписать off на AI-assisted change? Где фиксируется sign-off в PR. Also: Richard Forjoe — «Stop Trying to Keep Up With AI Code Generation».
**Релевантность:** ★★★★★ — Accountability + sign-off напрямую связаны с human review gate.

### 4. Your Regression Suite Is a Museum: 5 Questions (Anton Gulin)
**Источник:** anton.qa
5 проверок для decision delete vs keep тестов. Способ поймать always-green тесты. Связано с Yaron Assa «The dust your test suite is kicking up is blocking the light».
**Релевантность:** ★★★★☆ — Mutation testing + regression maintenance.

### 5. Test Rocket: Rethinking the Test Pyramid for the AI Era
**Источник:** dev.to
Новый подход к тест-пирамиде для AI coding agents: равные unit + integration слои. Also: Gil Zilberfeld «Testability Is a Feature. Does Your Code Agent Know About It?»
**Релевантность:** ★★★★☆ — AI-era test architecture.

### 6. Your Test Suite Shouldn't Break Because Someone Renamed a Div (Surya Kulshreshtha)
**Источник:** medium.com
Fallback-стратегии от test IDs до ARIA roles + AI healing как last resort. Лестница sturdy selectors.
**Релевантность:** ★★★★☆ — locator resilience, self-healing critique.

### 7. How to Use Claude Code for QA Automation (Sage Holloway)
**Источник:** pub.towardsai.net
/init, skill.md, Playwright MCP/CLI — как всё сочетается. Почему сгенерированные селекторы и credentials нуждаются в review перед мержем.
**Релевантность:** ★★★★☆ — AI coding tools + review process.

### 8. MCP 2.0 for QA: A Beginner's Guide (Pramod Dutta)
**Источник:** scrolltest.com
Новый stateless handshake, OAuth hardening, 4-layer test plan для AI agents. Also: MCP 2.0 Breaking Changes.
**Релевантность:** ★★★★☆ — MCP + agent testing.

### 9. Should Testers Write Unit Tests? (Bas Dijkstra)
**Источник:** ontestautomation.com
3 способа, как тестер может добавить ценность к unit tests: coverage review, mutation testing alongside developer.
**Релевантность:** ★★★☆☆ — Тестеры и unit tests, mutation testing.

### 10. AI will make QAs actually be QAs (Reddit + Nate Custer)
**Источник:** reddit.com
AI убирает mundane → фокус на важном. Нужно «Think Differently About AI and Testing» (TTC Global). Обсуждение: exhausted vs empowered.
**Релевантность:** ★★★☆☆ — Role evolution, mindset.

---

## Саммари TOP 5 (развернуто + ссылки на wiki)

### 1. Testing Mindset — [→ wiki](keith-klain-testing-mindset-after-all-2026.md) · [оригинал](https://qualityremarks.com/apparently-we-need-a-testing-mindset-after-all/)
Миф «testing mindset не существует» опровергнут AI. LLM-as-judge с self-preference и preference leakage (2024, 2026) доказывает: creator не может нейтрально оценить свое — нужен evaluator independence. Старая идея critical distance (Michael Bolton) вернулась как "evaluator independence". Для QA: генератор и судья — разные модели/люди, калибровка, мульти-оценщики.

### 2. QE Structural Problem — [→ wiki](rick-crawford-qe-structural-problem-2026.md) · [оригинал](https://blog.postman.com/your-qe-program-has-a-structural-problem-and-ai-just-made-it-visible/)
Postman Field CTO: AI × PR-velocity вскрыл 6 структурных разрывов QE-программы — serial quality, фрагмент инструментов по протоколам, гниение тестов, непокрытый long tail, scramble доказательств для аудита, AI усиливает слабую трубу. Решение: оценить 6 зон R/Y/G для домена 3-10 сервисов → 5 метрик pipeline (Design/Gate/Validate/Monitor/Improve).

### 3. Accountable for AI Code — [→ wiki](julia-pottinger-accountable-ai-code-2026.md) · [оригинал](https://juliapottinger.com/) *(Weekly #325 #3 + Aug 25 "When an AI writes the code, a person still owns that it is right")*
Простой тест: можешь подписать AI-assisted change? Где sign-off в PR? Accountability размылась — решение 3 уровня с именем: individual reviewer of record (`Reviewer of record: [name]`), team working agreement (что можно без доп-ревью, что — только с: auth/payment/PII), org policy. Green ≠ решение — `tests passed` информация, не approve.

### 4. Regression Suite Is a Museum — [→ wiki](anton-gulin-regression-suite-museum-2026.md) · [оригинал](https://www.anton.qa/blog/posts/regression-suite-museum)
Каждый спринт добавляет, почти никто не удаляет. 5 вопросов аудита старейшей трети: когда падал по реальному багу? какой user риск? заметит ли кто пропажу? проверяет результат или шаги? может ли упасть? + эксперименты `grep-invert`, `not.toBe`. На наследуемом сьютe треть ушла — ничего не сломалось. Контракт для AI-генерируемых тестов.

### 5. Test Rocket — [→ wiki](test-rocket-pyramid-ai-era-2026.md) · [оригинал](https://dev.to/sudokar/test-rocket-rethinking-the-test-pyramid-for-the-ai-era-2d6n)
Пирамида была экономическим аргументом. AI обнулил cost написания unit-тестов → пирамида теряет смысл. Rocket: static analysis = thrust base, unit+integration = два полных корпуса (быстрый фидбек для агента), E2E = nose cone (мал). Ловушка — моки, привязанные к реализации; фикс — тесты из спеки/плана/TDD, не из кода.

---

## Рейтинг релевантности для AI QA

| Статья | Релевантность | Тема |
|--------|--------------|------|
| Testing Mindset (Klain) | ★★★★★ | Human review gate, judge bias |
| QE Structural Problem (Postman) | ★★★★★ | QE gaps, pipeline metrics |
| Accountability AI Code (Pottinger) | ★★★★★ | Sign-off, governance |
| Regression Museum (Gulin) | ★★★★☆ | Mutation testing, regression |
| Test Rocket (dev.to) | ★★★★☆ | Test architecture AI-era |
| Div Rename (Kulshreshtha) | ★★★★☆ | Locator resilience |
| Claude Code QA (Holloway) | ★★★★☆ | AI tools + review |
| MCP 2.0 (Dutta) | ★★★★☆ | Agent testing, MCP |
| Unit Tests (Dijkstra) | ★★★☆☆ | Mutation testing |
| AI make QAs (Reddit) | ★★★☆☆ | Role evolution |

---

## Интеграция с AI QA Wiki

Дайджест связан с:
- `ai-productivity-paradox-verification-layer-2026.md` — Verification layer
- `ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md` — Evidence layer
- `Mutation-testing-advanced-playwright.md` — Mutation testing
- `agent-skills-specification.md` — Agent skills, MCP

Добавлено: 2026-09-01