# TypeSafe Jev (via Paluy) — judgment-as-service for gates

**Источник:** David Paluy (Production AI Agents & Private LLM Evals), LinkedIn 2026-09-18. Релиз TypeSafe AI (yesterday): Jev — не LLM, не генерирует текст. Даешь chunk + список вопросов → отвечает разом в машиночитаемом формате.

---

## Примитивы (3)

1. **choice** — выбор из списка + probability + confidence
2. **score** — оценка по шкале
3. **bool** — yes/no probability

## Заявленное

- 20–200x дешевле frontier на классификации; миллисекундный latency; параллельный eval всех вопросов за один запрос
- Калиброванные confidence вместо overconfident prose; typed JSON сразу в код
- НЕ для: chat, explanation, reasoning, prose
- Кейс: Vercel заменил Gemini 2.5 Flash Lite → ~6x быстрее, saturated their eval (бенчмарк перестал различать модели)

## Юзкейсы прямо наши

- Guardrails/security review как pre-check вместо субагента
- Model routing (classify task → pick model)
- Tool-call selection (which MCP tool/skill)
- Triage, fraud/risk scoring, extraction booleans, realtime loops

## Связки

- «Let software ask AI whenever it needs judgment» = гейт как вызов суждения, не модель в цикле. Архитектурно рядом с нашими signals (детерминированный гейт + judgment по требованию).
- Calibrated confidence vs overconfident prose — требование к любому judge (наш mass-signal слой, Kiro rubric, Bach judge-variance).
- «Saturated eval» — потолок бенчмарков как phenomenon; рядом с variance-темой (один замер ≠ тренд).
- Cost-разрыв 20–200x — в копилку token-economics (Osmani frontier, $80/day HN).
## Diagram (saved: typesafe-jev-judgment-service-gates-2026.png)

"Three ways software makes decisions": (1) Program every decision (rule maze, humans define everything upfront); (2) Let AI run the process (flexible, but AI controls the process — Think/Plan/Choose tools/Act); (3) Give software judgment (code controls workflow, Jev nodes supply judgment at decision points, e.g. Approve 91% / Review 7% / Reject 2%). Bottom line: "Code controls the workflow. Jev supplies judgment." — our deterministic-gate + judgment-on-demand architecture, drawn by a vendor.

## Comments Q&A (Maya Paluy → David)

- Q: what type of data does it use? A: state = whatever context you want judged (email, support ticket, ...). No fixed schema — arbitrary context in.

## Hands-on (Gareth Sharpe, TextLayer, 2026-09-19)

- Реальный пайплайн: OCR → classify → extract → validate → escalate → repair → result. Каждый post-OCR node начинается с Jev; на LLM едут ТОЛЬКО сигналы/поля, провалившие валидацию (не весь payload); Jev выбирает размер LLM по payload/complexity; неуверенность → human. Straight-through (без эскалации) — sub-second, почти free.
- Числа: 70–500ms; ~$0.042/M input tokens, output free.
- Формулировки: «less smart extractor, more fast verifiable state machine»; «biggest lever on quality: Input» (OCR-качество, не каскад); next — DAG как state machine (checkpoints, replay).
- Ronnit (коллега): Jev как coding-agent model router — пост завтра, вотчить.
- Ilja L. thread: мечта — tiny local 3–5B для complexity assessment + детерминированные числовые сигналы → high-quality routing. Наш free-first pattern тем же боком.
- Mapping на нас: escalation ladder Jev → right-sized LLM → human = наши mass-signals → review queue дословно (сигнал дешевый, человек наверху, эскалируется только провал). Валидация дизайна 0.2.0 независимыми руками.

## Company page (launch week signals, hype-discounted)

- Founder: Diogo Almeida (ex-OpenAI, ChatGPT/GPT-4/RLHF/InstructGPT co-inventor). Thesis: RLHF techniques that made LLMs charming made them unreliable → left to fix. 2 years stealth.
- Funding: $40M seed, DCVC. Positioning: "machine-native, hallucination-free", "can't hallucinate, won't tell you what you want to hear", typed decisions with probabilities; $42/B input tokens, output free.
- Traction claims (unverified, hype-discounted): #1 HN, Forbes exclusive, Vercel/Box CEOs tweeting, 250K waitlist, 40K Discord, hackathon winner (14yo rocket, CoreWeave).
- Rest (hiring spam, protein fridge, hackathon promos): skipped.

## Site check (typesafe.ai, 2026-09-18): early access, not GA
- Jev in early access (waitlist implied by 250K figure); docs live at docs.typesafe.ai; version 0.01.
- Claims: 193.6x faster / 444.6x cheaper (System One tasks, proof blog linked); RLCD training (Reinforcement Learning for Calibrated Decisions); $42/B input.
- Blog has technical posts (System One intro, bitterest lesson, RLHF critique) — candidates for direct ingest when judge-integration work starts.

## Hands-on 2 (Watsche Khalatyan, Evolve Robotics, 2026-09-19)

- Контекст: Evo-ассистент на Sonnet (2–4s и full model call на каждое сообщение, включая "list fleets").
- Паттерн "reflex": Jev впереди Sonnet — одно сообщение = один запрос закрытых вопросов (какой tool, enum/yes-no аргументы, mention-чек каждого имени; пороги: tool >0.7, args >0.6, names >0.8/<0.2). Уверен везде → собирает tool call без Sonnet. Текст нужен или неуверенность → Sonnet с reason.
- Bench 101 сообщение: Jev сам 62 (61 верно, медиана 377ms vs 2.4s); 39 ушли Sonnet (половина — нужен текст, остальные у порогов ±0.1). Sonnet 98/101 (2 miss — misspelled имена пропустил буквально; одно Jev разрулил).
- Доступ получил ЗА МЕМ (понравился команде). Релизы окнами, ранний доступ.
