# Pusuluri (AscendQE) — oracle independence + self-healing boundary

**Источник:** Nag Pusuluri, Founder & CEO AscendQE (25y QE, 90K+ mentored), LinkedIn 2026-09-15. Пост-принцип под mySDET/myDiya.

---

## 1. Automated self-validation (диагноз)

- Если одна имплементация — источник цепочки Code → Expected behavior → Tests → Validation, получаем automated self-validation: build green, software wrong.
- Вопрос: «who is actually verifying whom?»

## 2. Independence of the quality oracle (рецепт)

Тест должен знать «correct» из источников, независимых от имплементации:
Requirements · Acceptance criteria · Business rules · API contracts · Reference data · Approved baselines · Database invariants · Human-approved expected outcomes.
- Правильный вопрос автоматизации: «Did the system behave as expected?» — не «...the way it was implemented?».

## 3. Self-healing boundary (точная норма)

- Heal МОЖЕТ: locator, wait strategy, technical execution issues.
- Heal НЕ МОЖЕТ: expected business outcome. Silent change ожидания ради зеленого — «that is not healing, that is hiding a defect».

## 4. Три нужды enterprise Agentic QE

- Governed Automation (кто/что/где/по какой политике),
- Lifecycle Automation (Discovery → Data → Generation → Execution → Diagnosis → Healing → Change Impact),
- Independent Verification (что — source of truth корректности).

## Связки с нашей работой

- Oracle-from-requirements = наш requirements.csv (behavior claims до мутаций) + правило linkage (verbatim). Pusuluri дает авторитетную формулировку зачем.
- Healing boundary — норма для оценки self-healing вендоров (testRigor M1–M4 кейсы: что чинится ок, где граница). Готовый критерий в vendor-оценку, кандидат в Article-серию / VerdictGate docs (vendor profiles v0.2!).
- «As expected vs as implemented» — односложная проверка любого AI-сьюта, в копилку формулировок.
- Триада Governed/Lifecycle/Independent ↔ наши слои: gates+sign-off / matrix steps / mutation oracle. Совместимость фреймворков, не конкуренция.
- Engagement: standing нет (enterprise vendor). Только evidence.
