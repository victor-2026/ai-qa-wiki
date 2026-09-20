# Virto QA surface recon (2026-09-17) — vc-mcp-testing-module

**Источник:** GitHub VirtoCommerce/vc-mcp-testing-module (public, 1,464 commits, 2 stars) + local wiki glossary (QA interview prep, Oleg Zhuk 17.08.2026).
**Что это:** Agentic QA system — NL-тесты через MCP, LLM browser automation. Два слоя: `vc-fix` plugin (bug lifecycle, marketplace) + full `vc-qa` crew (регрессия, BA, CSV suites, agent crew; direct-clone only).

---

## Аудируемая поверхность (что можно взять)

- **regression/suites/** — CSV suites Frontend/ + Backend/, module-aligned; manifest `config/test-suites.json` (groups: smoke, critical, release, frontend, backend, sprint, full + catalog/b2b/payment). P0: 042/078 smoke, 039 CyberSource, 044 Security, 049 Platform REST API.
- **CI twins**: `ci/run-regression.ts` headless в Docker (`npm run ci:*`) — детерминированный путь помимо NL-промптов. Именно сюда ложится lite/mutation замер.
- **test-data/** fixtures, **reports/**, skills/commands/agents под `.claude/` (авто-дискавер).

## Барьеры независимого прогона

- Секреты: полный прогон хочет Anthropic key (наш есть), QA env creds, PAT, Postman key — чужое не трогаем.
- Стенд: нужен локальный деплой Virto (vc-deploy-dev: .NET 10 + MSSQL + модули) — GBs, часы сетапа. Без него сидить не во что.
- Kiro/orangepro тут не замена: Kiro .NET не поднимет, orangepro смотрит код, а не runtime. Deploy — long pole, наш край — вердиктная методология.

## Вывод для 2.3 (партнерские паки)

- Референс-поверхность существует и открыта: CSV suites + CI twins + P0-список. Обоснование Олегу строить на ней (конкретика вместо «ваши тесты»).
- Полный локальный прогон — 0.5–1 день сетапа; жечь ДО сигнала от Олега не надо. Recon (эта записка) — достаточный proof of seriousness для предложения.
- Local history: glossary готовился под Head-of-QA pipeline Virto (17.08) — контекст отношений есть.
