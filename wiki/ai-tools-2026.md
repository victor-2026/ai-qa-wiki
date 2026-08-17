# AI Tools 2026 — Overview with Advantages

> Source: `raw/AI list 2026.md`
> Thesis: "2023: you used ChatGPT for everything. 2026: you use ChatGPT for nothing."

## Categories

| Domain | Tool | Key Advantage |
|--------|------|---------------|
| Writing | [Claude](https://claude.ai) | Long-form content, deep analysis, context-heavy writing. Superior to ChatGPT for multi-turn reasoning and large document processing (100K+ tokens). |
| Images | [Nano Banana](https://nanobanana.com) | State-of-the-art image generation in 2026. High fidelity and prompt adherence. |
| Search | [Perplexity](https://perplexity.ai) | Real sources with citations — no hallucinated answers. Built-in research mode with verified references. |
| Data Analysis | [Manus](https://manus.im) | Complex data analysis without coding. Natural language interface for data manipulation and visualization. |
| Websites | [Lovable](https://lovable.dev) | Builds complete websites from plain text description. Full-stack generation (frontend + backend + deployment). |
| Video | [Kling](https://klingai.com) | High-quality video generation from text or images. Strong temporal consistency. |
| Browsing | [Perplexity Comet](https://www.perplexity.ai/comet) | Agentic AI browser by Perplexity. Autonomous research, form-filling, email/shopping, multi-step web workflows. "Vibe browsing" — delegate, don't click. |
| Studying | [NotebookLM](https://notebooklm.google) | Upload documents → summaries, podcasts, study guides. Google's AI notebook with source-grounded answers. |
| Meetings | [TLDV](https://tldv.io) | Automatic recording, transcription, and summarization of meetings. Integrates with Zoom/Meet/Teams. |
| Integration | [Gemini](https://gemini.google.com) | Connects the entire Google ecosystem (Gmail, Drive, Docs, Calendar) with unified AI access. |

## Key Themes

1. **Specialization over generalization** — each tool dominates its niche rather than one model doing everything
2. **ChatGPT displacement** — no single "AI for everything"; users choose by task
3. **Autonomy is the trend** — agents that execute (Comet browsing, Lovable building, Manus analysing) vs tools that assist
4. **Multimodal expansion** — video generation (Kling), image creation (Nano Banana) are mature enough for production use

## Relevance for QA

| Tool | QA Use Case |
|------|-------------|
| Claude | Test plan generation, bug report analysis, test result interpretation |
| Perplexity | Researching testing frameworks, debugging errors with real sources |
| NotebookLM | Studying certification materials (ISTQB, AWS) and technical docs |
| Lovable | Rapid prototyping of test apps and mock UIs |
| Kling | Recording test execution videos for bug reports |
| Comet | Smoke regression, content audit crawling, form validation flows |
| TLDV | Recording and summarizing standup/retro meetings |
| Gemini | Orchestrating test data across Google Sheets, Drive, Gmail |

### Deep Dive: Comet for Regression Crawling

Regression crawling с Comet — это **исследовательское тестирование без тестового кода**. Comet как agentic browser может автономно:

1. **Smoke crawl после деплоя**: зайти на staging, авторизоваться, пройти по 5-10 ключевым страницам, проверить что нет 500/404/blank pages
   - *Пример:* `"Go to https://staging.example.com/login, log in as admin, visit Dashboard, Users page, Settings page. Report any errors or missing elements."`
   - Не заменяет Playwright регрессию (нет assertion matchers, нет CI-интеграции), но даёт быструю визуальную проверку за 2-3 минуты

2. **Content audit crawl**: обойти сайт по всем public URL, собрать скриншоты, проверить битые ссылки, missing images, дублирующиеся title/h1
   - *Пример:* `"Crawl all public pages of https://example.com, list any broken links (404), missing alt text on images, and pages without h1 heading."`
   - Полезно для SEO/QA пересечения — регрессия контента после CMS миграции

3. **Form validation regression**: заполнить формы (login, registration, checkout) с разными наборами данных и убедиться что validation messages корректны
   - *Пример:* `"Go to registration page, submit with empty email, then with invalid email format, then with password < 6 chars. Check error messages appear correctly."`

4. **Multi-step workflow smoke**: выполнить сквозной сценарий (регистрация → создание заказа → оплата → логаут) и проверить что каждый шаг завершается без ошибок

**Ограничения:**
- ❌ Flaky на production (зависит от скорости сети, рендера JavaScript, API timeouts)
- ❌ Нет CI-интеграции (нельзя встроить в pipeline как assert-тест)
- ❌ Нет сравнения с baseline (diff скриншотов только ручной)
- ✅ Идеально для: staging smoke перед релизом, exploratory testing, ad-hoc проверка фичи

**Когда использовать вместо Playwright:**
- Команда без автотестов, но хочет базовую проверку
- Одноразовая проверка после миграции/хотфикса
- Исследование нового функционала без написания тестов заранее

## See Also

- [NotebookLM frameworks](notebooklm-frameworks-2026.md)
- [Free AI services 2026](free-ai-services-for-qa-2026.md)








<!-- backlinks-start -->
### Backlinks
- [AI Landscape 2026: From “ChatGPT‑Everything” to Specialized Assistants](wiki/ailist2026.md)
<!-- backlinks-end -->
