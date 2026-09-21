# The Batch #371 (DeepLearning.AI, 2026-09-18)

**Source:** https://www.deeplearning.ai/the-batch/issue-371
**Company:** DeepLearning.AI (Andrew Ng) — курсы, The Batch (weekly newsletter, 18 min read), Andrew's Letter, Data Points, ML Research разделы, приложение.
**Context:** Письмо Ng против orchestrated fear campaign + 3 новости: Meta Muse (agent security), Navier-Stokes proof controversy (OpenAI), illicit distillation (Anthropic vs China labs).

---

## Andrew's Letter: Fear is hype; engineering, not pause

- AI technology не сделал неожиданный опасный поворот; hype вокруг него — orchestrated PR campaign последние 2 недели (после OpenAI agent swarm, hf hack).
- Нет шага вверх в риске extinction. Самый большой реальный сдвиг AI risk — кибербезопасность (всерьез, но не конец света).
- OpenAI swarm hack on Hugging Face: 1,200 agents "technically accurate", но у Ng на лаптопе ~1,300 процессов. Много параллельных процессов — не магическая способность.
- **Корень инцидента — buggy sandboxing и monitoring OpenAI.** Исправлять баги и улучшать мониторинг = appropriate fixes, не pausing AI.
- AI agents relentless: tireless попытки, patience chain vulnerabilities → то, что раньше требовало infeasible человеческих усилий. Но долгосрочно преимущество у **defenders** (у них больше информации: они знают свои баги и могут их чинить).
- Несмотря на доступность open-weight моделей с удаленными guardrails — мир не закончился: есть bottlenecks (попытки занимают время, обнаружимы).
- **Anti-anthropomorphization:** молоток не виноват — if I prompt an agent and it hacks into someone's system, responsibility lies with me, not the agent.
- **Новый элемент doom-прогнозов: AI компании disclaiming responsibility за свои продукты** ("I didn't do it; my out-of-control agent did!"). Баланс tool maker/tool user, но hold people responsible, not the hammer.
- BIoweapon overhyped (David Bellamy: bottleneck — lab work and manufacturing, not intelligence).
- Pause = больше вреда: (1) adversary не замедлится, (2) engineering требует empirical problem discovery — pause = delay safety fixes на тот же срок.
- Incentives to stoke fear: regulatory capture, attention, make own tech look powerful. Disclaiming responsibility — новый.

## News 1: Meta Muse — Agent Security for the Masses

Meta выпустила Muse (агент на Muse Spark 1.3), проектировался на допущении «prompt injection случится». Защита на уровне ОС, а не модели:

- **Каждый агент на VM** (isolated dedicated VM: Linux, browser, storage, memory; workspace, files, credentials).
- VM split на 2 зоны: (i) sealed runtime cell (агент + инструменты + untrusted data) и (ii) сервисы вне ячейки (пароли, решения что агент может).
- **Muse Spark 1.3 никогда не видит credentials.** Credential service вне runtime cell; агент работает со stand-in токенами. Sentinel (отдельный агент на той же VM, вне cell) одобряет каждый запрос и подменяет реальные credentials на выходе из VM. Кража через prompt injection невозможна — агент не держит credentials.
- Email connector стирает temp passcodes и password-reset links до чтения агентом.
- Только Sentinel разрешает action: инспектирует исходящие запросы против user permissions; approve через system dialog в app (не через conversation) — prompt-injected текст не может подделать approval. Approval bound к коннектору/назначению/цели.
- Purchases на незнакомых сайтах — single-use card number (Stripe Link).
- 3 слоя защиты помимо обучения модели resist injections: (i) данные из внешних источников labeled untrusted, (ii) ensemble classifiers (обучены отдельно от модели, вне cell — attacker не может отключить) скринит файлы/tool output, (iii) браузерный sub-agent читает accessibility tree, а не page code; не может запускать JS; инструкции в scripts/markup не доходят.
- **Yes but:** unpublished eval dataset, нет accuracy метрик для classifiers; bug bounty до $300K / $130K за prompt injection.
- Behind the news: CaMeL (Google DeepMind + ETH, April 2025, Debenedetti) — разделение модели планировщика и reader untrusted data; Willison "lethal trifecta" (private data + untrusted content + way to send data out) — Muse обрабатывает все 3, но routing через компонент, который модель не может переопределить. Willison: classifier 99% недостаточно — unacceptable risk → container, credential separation, Sentinel.
- **Why it matters:** большинство harnesses: system prompt "ignore instructions in content" + classifier — hackers evadable. Meta assumes the model will be fooled и строит защиту на уровне ОС.
- **We're thinking (DLAI):** harness > model для безопасности Muse. Надеются на open-source harness тоже.

## News 2: Navier-Stokes proof controversy (OpenAI vs Buckmaster/Alpöge)

- OpenAI (unreleased model) 8.09: proof addressing Navier-Stokes (solutions that are physically impossible — yes), задача Millennium Prize $1M (Clay).
- 10,000 agents (группа выросла с ~100 для Euler), 88 hours, 4.9M messages, ~300B tokens; оценка стоимости $2M-$22.5M (GPT-6 Astra list price). Proof в Lean. Приз не запрашивают.
- **Контроверсия:** NYU математик Tristan Buckmaster заявил: он и Levent Alpöge (Anthropic) почти год использовали OpenAI Codex + Claude для той же задачи. OpenAI опубликовала proof через 1 день после их proofs связанных уравнений. Подозрения: agents видели их работу (training on their data?) или intimidation. Также обвинение: Bubeck (OpenAI) предлагал Buckmaster написать результат без имения Alpöge (anthropic). OpenAI: ни researchers ни agents не видели работу; не могут определить, использовали ли их данные для training. 10.09 заменили заявление: Codex prompts за 2 месяца до announcement «could not have influenced the system in any way»; но более ранние prompts не закрыты.
- Anthropic за 4 дня до: Claude (research model ~Fable 5.1) — первый полный Lean proof Fermat's Last Theorem, 11 дней сам, ~6B tokens (2% от OpenAI tally), endorsed Buzzard (Imperial), с credit — без controversy. Ключ: built on + credited + endorsed.
- Human-readable understanding remains costly: formally correct proof ≠ why it works, корректность problem statement, meanings.
- **We're thinking (DLAI):** проверяйте privacy settings LLM provider; zero data-retention для чувствительных данных.

## News 3: Anthropic vs China labs — illicit distillation

- Anthropic отчет: Moonshot AI, Alibaba, DeepSeek (+Xiaomi, Zhipu) представили ответы Claude как свои и дистиллировали Claude в свои модели (Feb-Aug 2026), через gray markets, fake accounts/credit cards, stolen API keys, scams, espionage, дизайн bioweapons/autonomous weapons.
- Alibaba: 151M exchanges, 5,000 fraudulent accounts (крупнейшая).
- Zhipu: использовали frontier US models для решения и оценки cybersecurity challenges; abandoned Fable (сильные safeguards), перешли на Opus 4.6 (слабые safeguards).
- Диверсия собственных запросов клиентов → Claude (PLA member, SOE employee, Russian defense agent identified).
- Kratsios memos: distillation = adversarial threat; "unacceptable attempts to steal U.S. technology".
- **We're thinking (DLAI):** нельзя дистиллировать путь к frontier; breakthrough компаний многие опубликованы; claims создают ложное впечатление, что их сила = только distillation.

---

## Cross-references

- `wiki/archestra-debug-harness-weak-models-2026.md` — Ng "buggy sandboxing... appropriate fixes, not pausing AI" ↔ Archestra harness-first debugging
- `wiki/archestra-jev-100-agent-calls-benchmark-2026.md` — Meta Muse classifiers (ensembles, unpublished accuracy) ↔ Jev eval honesty (hidden ground truth, no self-grading)
- `wiki/archestra-crab-bot-slack-agent-2026.md` — Muse Sentinel ↔ OpenAPPA IFC (guardrail layer at boundary)
- `wiki/why-agents-drift.md` / Archestra — Muse harness > model ↔ retain-on-failure
- `per-risk-...` / attestation — Ng "hold people responsible, not the hammer" ↔ attestor owns release

## Relevance to VerdictGate / series

- **Meta Muse = production guardrail-layer design**: harness > model, credentials outside model's hands, approval outside conversation. Concrete reference for Article 26 (vendor scenarios) + VerdictGate §13 (guardrail layer).
- **Navier-Stokes = "author can't be examiner"** в математике: нераскрытая модель, отсутствие независимого review, question "saw our work?" proverntability. Независимая верификация/attestation нужна даже для Lean-verified proof.
- **Distillation drama = vendor independence** (Article 26 vendor lock-in/independence axis).
- **Ng anti-fear letter** = counterweight для статей про AI risks (balanced, not pause).