# Breaklight: The AI Assurance Gap (research briefing, 2026)

**Source:** `raw/the-AI-assurance-gap.pdf` (Breaklight AI LLC, Research Briefing Oct 2026, 16 pp; owner-placed in raw 07.10)
**Author:** Breaklight AI (Duncan Smith Founder/COO, Nikolai Grabner Tech Head)
**Date:** 2026-10-07 (full text read: 16 pp / 17K chars)

## Саммари

Брифинг для принимающих решения: разрыв между скоростью внедрения AI и доказуемостью. Рынок: 31% приоритетных AI-кейсов в проде (ISG 2025), 78% лидеров не уверены в аудите (Grant Thornton 2026, n=950), 80% без tested incident-response плана. Тезис: output review не покрытие (ревьювер видит 1 из 7 слоев); 4 failure modes доходят до юзеров мимо ответа; релиз строится DEFINE → TEST → RETAIN в контролируемом окружении; метод - 5 доменов + evidence pack. Честность документа: цифры из разных выборок названы рыночными сигналами, а не единой мерой (прямая оговорка - редкость для вендорских пейперов).

## Рыночные сигналы (с их оговоркой)

- 31% приоритетных AI use cases в полном проде (ISG State of Enterprise AI Adoption, 2025).
- 78% лидеров без уверенности пройти независимый AI-аудит за 90 дней (Grant Thornton 2026 AI Impact Survey, n=950).
- 20% имеют tested AI incident response plan (те же; 80% - без).
- Оговорка автора: выборки разные, единой меры покрытия не существует и не выдумывается. Цитировать только с ней.

## Output review vs test coverage (ядро)

- Output review отвечает: "ответ выглядел правильно этому ревьюверу в этот день?" Видит 1 слой из 7 (ответ на экране; слепы: модель, retrieval, данные, permissions, workflow, release process). Аппрув ревьювера при вариативности = sample of one.
- Test coverage спрашивает: по юзерам/данным/задачам/границам - где evidence, а где нет. Проверяется каждый слой, где система может упасть.
- Разница детерминированного мира: проходящий софт-тест держится пока код не менялся; AI меняет поведение без смены кода.

## Четыре failure modes (все за хорошим ответом)

1. Fluent, not grounded - правдоподобный ответ без опоры в корпусе. Тестируется: grounding + hallucination.
2. Source never came back - retrieval miss, модель добивает пробел молча. Тестируется: retrieval quality.
3. Crossed a boundary - инъекция, путаница ролей, access-control leak в retrieval. Тестируется: adversarial.
4. Silent regression - новый промпт/модель/корпус/ранжирование меняет поведение без классического дефекта. Тестируется: Eval Ops.
- Релизный вопрос: не "работает?", а "для каких юзеров/данных/задач/границ/модов у нас есть evidence?"

## Demo → defensible release

- Где тестировать: авторизованное контролируемое pre-prod окружение (NIST pre-deployment guidance [5]): authorised (письменное добро на adversarial), representative (реальные задачи/данные/роли), contained (ломать безопасно, эскалация на критике).
- Цикл DEFINE (что доказать? какие юзеры? что фейлит релиз?) → TEST (реалистичные кейсы, role-based данные, поведение + evidence) → RETAIN (пороги, findings, лимиты + rerunnable routine на следующее изменение). Каждый цикл оставляет regression baseline.
- Метод 5 доменов + расширения - см. карточку Breaklight_AI (не дублирую).

## QA-угол (наш слой поверх)

- Agreed test set до релиза = pre-registration (ожидания зафиксированы до прогона, rerunnable routine).
- Пороги + запись findings/limits = evidence pack доктрина; tested incident plan (detect/explain/contain/learn) - операционная форма adjudication.
- "Output review is sample of one" - sibling нашего "agreement-with-itself ≠ outcome" (Kravchenko gate-oracle).
- 4 failure modes маппятся на наши слои: grounding/hallucination → decision validation; boundary → adversarial/permissions; silent regression → Eval Ops/дрейф-гейты.
- Чего нет в брифинге: seeded breaks (их adversarial = инъекции/red-team, не мутация сьюта); survival-score и тиры (вердикт = findings report, не Caught/N); валидация судей (кто проверяет Galileo-стиль грейдеры - не поднято).

## Связь

- [[qburst-quality-engineering-framework-validating-agent-behavior-2026]] - decision validation как слой (их grounding/hallucination → наш Layer 2).
- [[ai-qa-evidence-layer-validation-evals-guardrails-telemetry]] - evidence pack доктрина.
- [[kohl-structural-testing-llm-agents-2026]] - структурное тестирование агентов (трейсы/моки/ассерты как инструмент под их вопросы).
- [Breaklight positioning](wiki/breaklight-ai-assurance-gap-briefing-2026.md) - входящая ссылка для связности (формат, видимый wiki_lint).

## Caveat

- Вендорский пейпер (консалт продает assessment): цифры только с их оговоркой про разные выборки; независимых измерений самого Breaklight в тексте нет (кейсов с числами нет вообще).
- NIST pre-deployment [5] и ISG/Grant Thornton - внешние опоры, проверены поименно, не по содержанию (полные отчеты не читаны).
- Raw-правки запрещены; источник зафиксирован как есть.
