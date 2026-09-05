# AI QA Wiki — навигация по корню

299 файлов, плоская структура — так задумано: Obsidian-вики с `[[wiki/...]]`-ссылками, поиск через `wiki-topics.json` / `groq_qa.py`. Раскладывать по папкам нельзя — порвутся сотни кросс-ссылок. Вместо этого: этот хаб + именование по конвенции.

## Start here

- [AI Testing Glossary](ai-testing-glossary.md) (A–M) + [Glossary N–Z](ai-testing-glossary-n-z.md) — термины с переводом
- [QA Topics](qa-topics.md) + [Topics Map](topics-map.md) — старые карты (частично устарели, см. этот README)
- [AI Testing Map](ai-testing-map.md) — карта области
- [AI QA Evidence Layer](ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md) — слой доказательств, анти-overfit

## Mutation testing и верификация (ядро)

- [Advanced Mutation Testing with Playwright](Mutation-testing-advanced-playwright.md) — главная (FOM/HOM, segmentation)
- [Мутационное тестирование без доступа к коду](Mutation-testing-without-code.md) (RU)
- [Mutation vs Code Coverage (Autonoma)](mutation-testing-vs-code-coverage-autonoma.md)
- [Rotation without Relevance](rotation-without-relevance-preseed-mutant-filtering-2026.md) — preseed-фильтрация
- [AI QA Tool Evaluation: Mutation Matrix](ai-qa-tool-evaluation-mutation-matrix.md) — методология B
- [How to Tell If Tests Are Testing Anything](how-to-tell-if-tests-are-testing-anything-autonoma.md)

## Агенты и мультиагентные системы

- [Agentic Patterns](agentic-patterns.md) + [Agent Teams Architecture](agent-teams-architecture.md)
- [MAS Testing Framework](mas-testing-framework.md) + [summary](mas-testing-framework-summary.md)
- [Kiro Crew: Multi-Agent Orchestration](kiro-crew-multi-agent-orchestration-open-source-2026.md)
- [Pi Subagents](pi-subagents-2026.md) + [Pi ↔ OpenCode Integration](pi-opencode-integration-2026.md)
- [Ruvnet Agentic Stack](ruvnet-agentic-stack-2026.md)
- [Claude Code QA Testing](claude-code-qa-testing-2026.md) + [Skill Examples](claude-code-skill-examples-2026.md)

## LLM-тестирование и эвалы

- [LLM Testing: 6 Approaches](llm-testing-6-approaches.md)
- [PBT + LLM Codegen](pbt-llm-code-generation.md) + [Promptfoo Eval Suite](promptfoo-eval-suite.md)
- [RAG Evaluation (RAGAS)](rag-evaluation-ragas.md) + [Red Teaming](red-teaming-tests.md)
- [Offline Evaluation Trajectories](offline-evaluation-trajectories-2026.md)
- [Stoic Tester: Goodhart's Law in AI Eval](stoic-tester-goodharts-law-ai-evaluation-2026.md)
- [SlopCodeBench](slopcodebench-2026.md) + [BeyondQuality AI-Era Testing](beyondquality-ai-era-testing-2026.md)

## Playwright и автоматизация

- [Playwright Test Agents](playwright-test-agents-2026.md) + [Data-testid (React)](data-testid-react-playwright.md)
- [Self-Healing Tests](self-healing-tests.md) + [Anti-flakiness](anti-flakiness-habr.md)
- [Ad-hoc Testing Guide](ad-hoc-testing-guide.md) + [Canary Testing](canary-testing-guide.md) + [Feature Flags](feature-flags-guide.md)
- [Pact Contract Testing](pact-contract-testing-guide-2026.md) + [Consumer-Driven Post](consumer-drivencontracttestingpost.md)
- [Mobile Testing: Windows Setup](mobile-testing-windows-server-setup-2026.md) + [Parallel Infra](mobile-testing-infrastructure-parallel-2026.md)

## Каталоги вендоров и блогов

- [Kiro Blog Catalog](kiro-blog-catalog-all-publications-2025-2026.md) (+9 детальных `kiro-*`)
- [Autonoma Blog Catalog](autonoma-blog-catalog-all-publications-2026.md) (+20 детальных `autonoma-*`)
- [TestRigor / TestMu / Zalando / Martin Fowler / Postman / Julia Pottinger](testrigor-blog-catalog-all-publications-2026.md) (см. также `testmuai-*`, `zalando-*`, `martinfowler-*`, `postman-*`, `juliapottinger-*`)
- [TesterStories / Virtuoso / QualityRemarks](testerstories-blog-catalog-all-publications-2026.md) (см. также `virtuoso-*`, `qualityremarks-*`)
- [DevQAExpert Blog Catalog](devqaexpert-blog-catalog-all-publications-2026.md) — evaluation only

## Люди и интервью (по авторам)

Файлы вида `имя-тема-год`: `andrew-ng-*` (3), `anton-gulin-*` (3), `julia-pottinger-*` (2), `jeff-nyman-*` (2), `keith-klain-*`, `michael-bolton-*`, `karpathy-*`, `krivitsky-*`, `david-burke-*`, `sergey-yudin-*`, `ruslan-desyatnikov-*`, `loris-bartolini-*`, `alex-barady-*`, `prachi-dahibhate-*` (Bach/RST), `stephen-platten-*`, `wayne-roseberry-*`, `ruben-hassid-*`, `milko-slavov-*`, `matt-robson-*`, `mark-paemaa-*`, `ishan-anand-*`, `ilya-kabanov-*`, `boris-cherny-*`, `brij-kishore-pandey-*`, `alex-karp-*`, `shcherbinin-*`, `lee-robinson-*`, `ai-in-qa-issue-17-butch-mayhew-2026.md`, `tony-seale-*`.

## Testing AI (книга, серия)

- [Index](testing-ai-book-index.md) + [Evidence Foundations](testing-ai-book-evidence-foundations.md) + [Generated Code](testing-ai-book-generated-code-confidence-engineer.md) + [Playbook Future](testing-ai-book-playbook-future.md) + [Security](testing-ai-book-security-dynamic-systems.md)

## Конвенции (чтобы не плодить дубли)

1. Перед созданием — поиск по корню и `wiki-topics.json`; дубли сливать в канонический файл, а не держать рядом.
2. Имя файла: `тема-год.md` или `автор-тема-год.md`, латиница, дефисы; RU-контент допустим внутри.
3. Каждая страница: Source + Raw-ссылка + кросс-ссылки + `*Ingested: дата*`; английский для технических, русский для саммари — как в файле.
4. После изменений — `python3 wiki_llm.py --update-index`, проверка `wiki-topics.json` валиден.
5. Подпапки только для серий (`istqb/`, `people/`, `requirements/`) — одиночные страницы живут в корне.

*Обновлено: 2026-09-05 — дедупликация 4 пар (butch-mayhew, barady, klain, mutation-stub).*
