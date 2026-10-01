# Отчет W5 → W4: улучшения за сессию 2026-09-30 (фактура для будущей статьи)

## Wiki-инфраструктура (ai-qa-wiki, все запушено в origin/main)
- Волна мутационного тестирования W6 (ратифицирована): 10 raw+wiki пар (LLM P0: llmorpheus, meta-ach, mutgen, intent-based; P1: secmutbench, quantum, witness, sting; P2: mewt/muton) + 4 секции в хабах (Tools Landscape, Practical Applications 6–7, Declarative Framework, JiT).
- Owner-pass W5: 6 орфанов сняты входящими из хабов (линт 56→50), raw_count 349→359, 10 raw переименованы человеком, 10 шапок + 10 сносок выровнены. Коммиты f4608ed (37 файлов) + 40af032 (11 файлов), оба pushed.
- Mallare-ингест: wiki/qa-ai-engineer-role-mallare-2026.md, topics 505→506 (+волна →516).
- Линт финальный: 0 битых, internal links 2017→2031, exit 0.

## Процесс: три факапа → три правила → код
1. Агент писал в raw/ дважды за неделю → правило "raw только человек" → хук raw-guard (`~/.config/opencode/plugins/safety-guards.js`).
2. Коммиты без явной команды (stop-rule #6) → commit-guard с флагом `#owner-approved` (не blanket-ban).
3. Проверка по grep вместо полного рида (ложные клеймы: TesterArmy NOT FOUND, приватность из места) → поправка к дисциплине: "Приемка пачки = полный рид файлов <500 строк + линт; claim без пути-и-строки = черновик" (апрув W1 2b66937, ушло W1→W2).
- Честная оговорка (W2 6cfdd20): secrets-deny — настоящая защита; raw/commit-guard — фрикция+аудит, не hard security.

## Визуал VerdictGate (все в outputs/)
- Баннеры C (контурные карточки — выбор пользователя) и D (сплошные плашки, рецепт статьи 8); оба сдвинуты от аватары (x=380). Скрипт outputs/make_linkedin_banner.py (variant_c/d + slide2-5).
- Слайдшоу 5 шт 1584×396: бренд → silent green → 5 сценариев → терминал B0 100% → CTA. Глиф-правило: Helvetica.ttc не имеет → (тофу), использовать >.
- One-page seed-test protocol (W1-staged, Полу не отправлен): outputs/seed-test-protocol-org-gates-draft.md.

## Контакты/треки (детали у W1, здесь только факты)
- Jason Arbon: коммент отправлен (verdict problem, misses both sides).
- Alden Mallare: статья про QA AI Engineer заингещена; коммент отправлен (scorecard needs own test); follow, коннекта нет; новый пост про prompt-as-asset — коммент НЕ отправлен (наблюдение).
- Igor Akymenko (FlowScout, трек W1): 3 замечания по Seeded Controls приняты, контрибьютор Volume VIII.
- Paul Kanaris (QACE, трек W1): скетч seed-test орга-гейта staged (8bd3bc1), мяч у Виктора на отправку.
- Andrew Doughty (Virtuoso Touchstone): коммент отправлен, CEO ответил по существу (traceability chain); карточка outputs/virtuoso-touchstone-card-w1.md + blog recon (GSI-пост, coverage-пост с mutation tip №5).
- Lisa Crispin: коммент отправлен (small batches снижают цену проверки, 55/54/46); части 2–3 на вотче.
- Fabian Baptista: триаж готов, действий нет.
- Leonardo Lanni: пост про evals занесен; Cat-GPT репо разобрано (DeepEval+guardrails+Arize → референс W2).
- Megan Black: холодный аутрич отправлен. Pavel Petukhov: не писали. Nikita Gavrish: входящий, рекомендация Accept (не решено).

## Кандидаты в статью про улучшения (на выбор W4)
- A: "От факапа к хуку" — как три операционных сбоя за день превратились в исполняемые guardrails.
- B: "Приемка пачки" — почему grep-проверка врет и сколько стоит полный рид (470 строк, 10 файлов).
- C: "Зеленая вики" — цифры гигиены (линт 0 битых, орфаны −6, индекс +11) как побочный эффект owner-проходки.

---
*Статус: фактура, не черновик. Цитаты для банка — отдельными handover (Virtuoso ×5, Leonardo ×2). Не коммитилось (отчет в outputs/, следующий коммит заберет).*
