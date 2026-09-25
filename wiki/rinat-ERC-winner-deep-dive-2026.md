---
source: "https://abdullin.com/ilya/how-to-build-best-rag/"
ingested: "2026-09-21"
title: "How I Won the Enterprise RAG Challenge (Ilya Rice)"
type: article
updated: "2026-09-21"
tags: [rag, evals, benchmark, architecture]
---

## How I Won the Enterprise RAG Challenge - Deep Dive (Ilya Rice)

**Позиция:** победитель Round 2 ERC (Score 123.7, 49 минут на все эксперименты). Опубликовано на сайте Rinat Abdullin. Каталог: [[rinat-abdullin-blog-catalog-all-publications-2026]].

---

### Победная архитектура

1. **PDF Analysis** - Docling (IBM), сильно модифицированный для сохранения page references.
2. **Router Pattern** - первый шаг выбирает наиболее подходящего агента.
3. **Dense Retrieval** - семантический поиск (FAISS + OpenAI embeddings).
4. **Parent Document Retrieval** - ретривится не чанк, а полная страница (контекстная целостность).
5. **LLM Reranking** - ретривнутые страницы переоцениваются и переупорядочиваются LLM.
6. **Reasoning Patterns** - Custom Chain-of-Thought + Structured Outputs внутри одного промпта (контроль процесса мышления).
7. **Final Answer** - o3-mini.
8. **Self-Consistency с Majority Vote** - несколько вариантов ответа → выбирается наиболее консистентный.

---

### R&D эксперименты (журнал)

| Эксперимент | Время | R/G | Score |
|---|---|---|---|
| Dense + LLM rerank + Router + SO CoT; o3-mini | 16 min | 83.9/72.8 | 114.8 |
| Dense; llama-3.3-70b | 23 min | 81.4/74.7 | 115.4 |
| **Dense + Router + LLM rerank; o3-mini** | **49 min** | **83.8/81.8** | **123.7** |
| Dense; llama-3.1-8b | 50 min | 81.1/68.7 | 109.3 |
| Full Context; gemini-2.0 thinking | 51 min | 75.5/75.0 | 112.8 |
| Dense + Router + LLM rerank + Self-consistency; o3-mini | 33h | 83.4/79.8 | 121.6 |

Total: 11 экспериментов. За час нашёл >123 (оба 33h - Self-consistency были чуть ниже). **Что не сработало:** llama-3.1-8b для reranking; Full Context → gemini-2.0 thinking.

---

## Главный урок для QA/AI-QA

**Победу принёс не конкретный код, а eval-first инфраструктура:** предварительно построенная evaluation pipeline позволила быстро прогонять архитектуры и в конце концов выбрать лучшую среди самых быстрых. Это прямая аналогия принципам:

- "Evals as CI gate" ([[autonoma-llm-evals-cicd]])
- "Golden trajectory + diff" ([[autonoma-how-to-test-ai-agent-e2e-2026]])
- Разделение retrieval/generation оценки ([[rinat-erc-2026]], Score = R/3+G)

Если победитель получает результат за 49 минут, где каждую архитектуру можно оценить дешевле минуты - то оценка и есть ресурс, в который вкладываются заранее.

---

## Связанные темы

- [[rinat-erc-2026]] - обзор челленджа + лидерборд
- [[rinat-llm-benchmarks-2026]] - серия бенчмарков
- [[rinat-sgr-2026]] - SO CoT technical foundation
- [[autonoma-rag-evaluation-metrics-2026]] - метрики RAG

---

### Источник
- [Ilya Rice: How I Won the Enterprise RAG Challenge](https://abdullin.com/ilya/how-to-build-best-rag/) + [source code](https://github.com/...)
- ERC hub: https://abdullin.com/erc/

## See also

- [Enterprise RAG Challenge](wiki/rinat-erc-2026.md)
