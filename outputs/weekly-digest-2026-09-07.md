# AI QA Wiki - Weekly Digest (2026-09-01 - 2026-09-07)

**Period:** Sep 1 - Sep 7, 2026
**New wiki pages:** ~76 (из них 2 сегодня, не в индексе)
**Index:** 302 topics | **raw:** 189 files

---

## 1. Autonoma knowledge base - 20 статей + полный каталог

Самая крупная поставка недели (2026-09-01). Полный разбор блога Autonoma: 20 статей с двух поверхностей тестирования агентов - поведенческой и внутренней.

**Темы (все 20):**
- **Действия агента:** [testing-tool-calls](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fautonoma-testing-tool-calls-2026.md), [how-to-test-ai-agent-e2e](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fautonoma-how-to-test-ai-agent-e2e-2026.md), [agent-simulation](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fautonoma-agent-simulation-2026.md) (3-акторный harness), [multi-agent-handoffs](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fautonoma-multi-agent-handoffs-2026.md), [multi-turn-conversations](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fautonoma-multi-turn-conversations-2026.md)
- **Нестабильность:** [non-deterministic-outputs](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fautonoma-non-deterministic-outputs-2026.md), [streaming-responses](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fautonoma-streaming-responses-2026.md), [hallucinations](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fautonoma-hallucinations-2026.md)
- **Состояние и память:** [agent-memory](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fautonoma-agent-memory-2026.md)
- **RAG:** [rag-pipeline](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fautonoma-rag-pipeline-2026.md) (две поверхности, не один счёт), [rag-retrieval](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fautonoma-rag-retrieval-2026.md), [rag-evaluation-metrics](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fautonoma-rag-evaluation-metrics-2026.md) (4 метрики)
- **Инфраструктура тестов:** [llm-unit-testing](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fautonoma-llm-unit-testing-2026.md), [llm-evals-cicd](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fautonoma-llm-evals-cicd-2026.md), [mcp-server](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fautonoma-mcp-server-2026.md) (3 слоя), [qa-ai-feature](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fautonoma-qa-ai-feature-2026.md)
- **Фреймворки:** [langgraph-testing](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fautonoma-langgraph-testing-2026.md), [crewai-evaluation](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fautonoma-crewai-evaluation-2026.md), [agent-regression](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fautonoma-agent-regression-2026.md), [agent-reliability](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fautonoma-agent-reliability-2026.md)
- **Каталог:** [autonoma-blog-catalog](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fautonoma-blog-catalog-all-publications-2026.md) - 581 статья, TOP 20 с Саммари-колонкой

**Ключевое:** "RAG pipeline: two surfaces, not one score" и "3-акторный harness для simulation" - прямые валидационные платформы для методологии. 20 статей - фактически готовый учебник по LLM/agent testing.

## 2. Kiro blog - 9 статей + каталог + pilot plan

(2026-09-01) Вторая по объёму поставка. Kiro (агент для CI, 1.5M+ conversations).

- [continuous-prompt-evaluation](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fkiro-continuous-prompt-evaluation-llm-judges-2026.md) - LLM judges, 15 измерений, -32% регрессий промптов
- [diagnostics-over-time](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fkiro-diagnostics-over-time-agent-quality-2026.md) - 6 месяцев, Java 26.7% top-fix rate
- [property-based-testing-security-bug](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fkiro-property-based-testing-security-bug-2026.md) - кейс `__proto__`, PBT поймал то, что никто не искал
- [root-cause-33s](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fkiro-root-cause-33s-2026.md) - root cause 30 мин -> 1 мин
- [soc2-planview-automation](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fkiro-soc2-planview-automation-2026.md) - 40+ часов на цикл аудита
- [snyk-guardrails](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fkiro-snyk-guardrails-2026.md) - MCP/AIBOM, многослойные guardrails
- [trust-agent-triage](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fkiro-trust-agent-triage-2026.md) - прод-инциденты, 13m35s среднее время
- [bug-fix-paradox](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fkiro-bug-fix-paradox-2026.md) - почему агенты ломают рабочий код (совпадение фикса C/P)
- [openapi-to-testsuite](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fkiro-openapi-to-testsuite-2026.md), [kiro-crew](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fkiro-crew-multi-agent-orchestration-open-source-2026.md) (open-source оркестрация) + [pilot-plan](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fkiro-crew-pilot-plan.md)
- Каталог: [kiro-blog-catalog](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fkiro-blog-catalog-all-publications-2025-2026.md) - annotations, TOP 10

## 3. Каталоги блогов - 11 новых

Мета-слой недели. Все каталоги собраны по единому шаблону (аналог Kiro/Autonoma).

| Каталог | Кому | Объём | Ссылка |
|---------|------|-------|--------|
| [testRigor](obsidian://open?vault=ai-qa-wiki&file=wiki%2Ftestrigor-blog-catalog-all-publications-2026.md) | AI & agentic + codeless | ~3 013 ст. | TOP 25 |
| [TesterStories / Jeff Nyman](obsidian://open?vault=ai-qa-wiki&file=wiki%2Ftesterstories-blog-catalog-all-publications-2026.md) | testing knowledge | ~150 | DeepEval series |
| [Virtuoso](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fvirtuoso-blog-catalog-all-publications-2026.md) | Composable, StepIQ | ~200 | Journey Confidence |
| [Quality Remarks / Keith Klain](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fqualityremarks-blog-catalog-all-publications-2026.md) | Verification Asymmetry | ~170 | EU AI Act |
| [Postman](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fpostman-blog-catalog-all-publications-2026.md) | QE as Platform | ~1 127 | AI Agents orbit |
| [Julia Pottinger](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fjuliapottinger-blog-catalog-all-publications-2026.md) | accountability | 46 | TOP 15 |
| [Martin Fowler](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fmartinfowler-blog-catalog-all-publications-2026.md) | data + agentic | ~600 | TOP 15 |
| [TestMu AI](obsidian://open?vault=ai-qa-wiki&file=wiki%2Ftestmuai-blog-catalog-all-publications-2026.md) | (ex-LambdaTest) | ~2 380 | TOP 20 |
| [Jeff Nyman catalog](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fjeff-nyman-ai-testing-catalog.md) | AI testing | - | личный |
| [DevQAExpert](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fdevqaexpert-blog-catalog-all-publications-2026.md) | evaluation only | ~50 | низкая глубина |
| [Kiro](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fkiro-blog-catalog-all-publications-2025-2026.md) | agent CI | annotated | TOP 10 |

**Deep-dives к каталогам:**
- [julia-pottinger-who-validates-ai-generated-code](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fjulia-pottinger-who-validates-ai-generated-code-2026.md) - RACI + 5-вопросный PR-гейт
- [martinfowler-making-data-ready-agentic-ai](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fmartinfowler-making-data-ready-agentic-ai-2026.md) - 5 атрибутов данных + 4 слоя (contracts, quarantine, medalion, lineage)
- [test-rocket-pyramid-ai-era](obsidian://open?vault=ai-qa-wiki&file=wiki%2Ftest-rocket-pyramid-ai-era-2026.md) - пересборка пирамиды тестов
- [keith-klain-testing-mindset-after-all](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fkeith-klain-testing-mindset-after-all-2026.md)
- [rick-crawford-qe-structural-problem](obsidian://open?vault=ai-qa-wiki&file=wiki%2Frick-crawford-qe-structural-problem-2026.md)

**Ключевое:** DevQAExpert оставлен как evaluation-only (90% анекдоты, низкая глубина) - не полный каталог, только оценка.

## 4. Software Testing Weekly #325 - TOP 5 + обзор ресурса

(2026-09-03) Топ-5 выпуска, все в wiki по 90-96 строк + Саммари-секция с ссылками:
- klain 91, crawford 95, pottinger 90, gulin 96, rocket 92

Страница ресурса: [software-testing-weekly-newsletter](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fsoftware-testing-weekly-newsletter-2026.md)

## 5. Pi / OpenRouter tooling

- [ruvnet-agentic-stack](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fruvnet-agentic-stack-2026.md) - rUv (Reuven Cohen): agentic-стек, 11.3k followers
- [pi-subagents](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fpi-subagents-2026.md) - плагин Pi для асинхронного делегирования сабагентам
- [pi-opencode-integration](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fpi-opencode-integration-2026.md) - 3 слоя: AGENTS.md, MCP, CLI
- [pi-image-generation](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fpi-image-generation-2026.md) - 424 модели, 18 `:free` (image не покрыты free)

## 6. AI-era testing и навыки агентов

- [andrew-ng-coding-agents-skills-map](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fandrew-ng-coding-agents-skills-map-2026.md) - Skills Map + Building/Deploying; главный trait - **eval-driven**
- [beyondquality-ai-era-testing](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fbeyondquality-ai-era-testing-2026.md) - Vitaly Sharovatov (Qase)
- [slopcodebench](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fslopcodebench-2026.md) - SprocketLab v1.0, бенчмарк slop-кода
- [qburst-quality-engineering-framework-validating-agent-behavior](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fqburst-quality-engineering-framework-validating-agent-behavior-2026.md)
- [tony-seale-multi-agent-semantic-web](obsidian://open?vault=ai-qa-wiki&file=wiki%2Ftony-seale-multi-agent-semantic-web-2026.md)
- [claude-meetup-beginners-beyond](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fclaude-meetup-beginners-beyond-aug2026-summary.md) - митап Claude for Beginners (Aug 18, 2026)
- [rotation-without-relevance-preseed-mutant-filtering](obsidian://open?vault=ai-qa-wiki&file=wiki%2Frotation-without-relevance-preseed-mutant-filtering-2026.md) - **мутации: фильтр до сидинга** (QAEverest + внешняя литература)

## 7. Эксперты и хот-тейки

- [alex-karp-neurodivergent-advantage](obsidian://open?vault=ai-qa-wiki&file=wiki%2Falex-karp-neurodivergent-advantage-2026.md)
- [anton-gulin-regression-suite-museum](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fanton-gulin-regression-suite-museum-2026.md) - 5 вопросов delete vs keep (ex-Apple)
- [boris-cherny-claude-maintains-apps](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fboris-cherny-claude-maintains-apps-2026.md)
- [brij-kishore-pandey-retroactive-ai-titles](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fbrij-kishore-pandey-retroactive-ai-titles-2026.md) - ретроактивные AI-титулы
- [ilya-kabanov-cybersecurity-ai-cost](obsidian://open?vault=ai-qa-wiki&file=wiki%2Filya-kabanov-cybersecurity-ai-cost-2026.md)
- [ishan-anand-llm-persona-feedback-failure-modes](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fishan-anand-llm-persona-feedback-failure-modes-2026.md)
- [jeff-nyman-testing-knowledge](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fjeff-nyman-testing-knowledge-not-just-testing-skill-2026.md) - знание vs скилл
- [mark-paemaa-automated-testing-confidence](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fmark-paemaa-automated-testing-confidence-2026.md)
- [matt-robson-human-in-the-loop](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fmatt-robson-human-in-the-loop-ai-testing-2026.md) - HITL недостающий слой (Virtuoso)
- [milko-slavov-two-doors-mcp](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fmilko-slavov-two-doors-mcp-2026.md)
- [practitest-state-of-testing](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fpractitest-state-of-testing-2026.md) - 13-й ежегодный отчёт

## 8. Обновления площадок (2026-09-07, pending commit)

- [bas-dijkstra-learning-takes-time](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fbas-dijkstra-learning-takes-time-2026.md) - ремесло тест-автоматизации требует времени обучения; заморозка найма junior-ов поверх AI-агентов
- [orangepro-risk-based-coverage](obsidian://open?vault=ai-qa-wiki&file=wiki%2Forangepro-risk-based-coverage-2026.md) - Aamir Siddiqui: risk-based coverage layer (incident -> guardrail), vendor для пилота

## Справочное

- [ai-testing-glossary](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fai-testing-glossary.md) + [glossary-n-z](obsidian://open?vault=ai-qa-wiki&file=wiki%2Fai-testing-glossary-n-z.md) - сплит на 2 файла (104 термина)

---

## Итоги недели

1. **Самое ценное:** Autonoma (20 статей) + Kiro (9) - два готовых учебника по тестированию агентов, прогнаны через шаблон wiki (90-100 строк каждый).
2. **Каталоги стали системой:** 11 каталогов блогов по единому шаблону с Колонкой Саммари - поиск по литературе за один шаг.
3. **Методология жива:** rotation-without-relevance (пресидинг мутантов) и testRigor 3+3, QAEverest B1 100% - эмпирика недели.
4. **Пробел:** 2 страницы от сегодня (Bas Dijkstra, OrangePro) ждут добавления в индекс wiki-topics.json.

*Сгенерировано: 2026-09-07*