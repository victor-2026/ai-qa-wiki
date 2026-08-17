---
title: "Google Terms of Service (July 2026) — Restrictions Outside EEA"
type: article
updated: "2026-08-17"
tags: [google]
---

# Google Terms of Service (July 2026) — Restrictions Outside EEA

**Effective:** July 30, 2026
**Country version:** Russia
**Provider:** Google LLC (Delaware, USA)

**Source:** Google ToS text (Russia version, preview before July 30, 2026)

## Key Restrictions Relevant to AI/QA Work

### 1. AI/ML Training Ban

```
using AI-generated content from our services to develop machine 
learning models or related AI technology
```

Запрещено использовать контент, сгенерированный Google-сервисами, для тренировки ML-моделей или разработки связанных AI-технологий.

### 2. Prompt Injection / Jailbreaking Ban

```
jailbreaking, adversarial prompting, or prompt injection, except 
as part of our safety and bug testing programs
```

Запрещены jailbreaking, adversarial prompting и prompt injection — **кроме safety и bug testing программ** Google.

### 3. Automated Access Restrictions

```
using automated means to access content from any of our services 
in violation of the machine-readable instructions on our web pages 
(for example, robots.txt files that disallow crawling, training, 
or other activities)
```

Автоматизированный доступ к контенту Google-сервисов в нарушение robots.txt запрещён.

### 4. AI Content Deception

```
misleading others into thinking that generative AI content was 
created by a human
```

Запрещено выдавать AI-сгенерированный контент за человеческий.

### 5. Service Provider & Jurisdiction

- **Provider:** Google LLC (Delaware, USA) — US entity, subject to US sanctions/export laws
- **Governing law:** California law, exclusive jurisdiction in Santa Clara County courts
- **Country version: Russia** — applies different terms based on user's location

## Impact on Victor's Projects

| Activity | Status | Reasoning |
|----------|--------|-----------|
| Using Gemini API via OpenRouter | ✅ OK | Not training ML models on Google content; OpenRouter mediates access |
| wiki_llm.py (Groq/Ollama) | ✅ OK | Not using Google services |
| Playwright scraping for tests | ✅ OK | Not targeting Google services; scraping own/Buzzhive/OrangeHRM |
| Prompt injection testing | ⚠️ Caution | OK against own LLMs (Groq/Ollama). Against Gemini — requires safety/bug testing program |
| Building ML from Google AI content | ❌ Prohibited | Direct violation of section 1 |
| robots.txt violation | ❌ Prohibited | Must respect robots.txt disallow directives |

### Non-EEA Implications

- Google LLC (US entity) applies US export control and sanctions laws
- Russia country version may impose additional restrictions versus EEA versions
- Serbia is not under US sanctions, but Google's ToS is US-governed
- Key difference from EEA: different legal protections (no GDPR-based override), different jurisdiction

## What Hasn't Changed

- Content ownership: "Your content remains yours"
- Privacy Policy: separate, not modified by these terms
- License scope: worldwide, non-exclusive, royalty-free (same as before)
- Copyright takedown process: unchanged

## Recommendations

1. Use Gemini through OpenRouter — adds a layer of abstraction
2. Keep prompt injection testing on own LLMs (Groq/Ollama), not Google services
3. If working with Google AI services (Gemini), apply only through official safety/bug testing programs
4. Document which AI services are Google-based for compliance tracking
5. For QA automation, no changes needed — scraping your own services is unaffected

## Related Wiki Articles

- `llm-testing-6-approaches.md` — prompt injection as testing technique
- `ai-testing-map.md` — overall AI testing landscape
- `red-teaming-tests.md` — red teaming methodology

**Updated:** 2026-06-24
