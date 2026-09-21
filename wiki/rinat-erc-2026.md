---
source: "https://abdullin.com/erc/"
ingested: "2026-09-21"
title: "Enterprise RAG Challenge"
type: article
updated: "2026-09-21"
tags: [rag, evals, benchmark, competition]
---

## Enterprise RAG Challenge (ERC)

**Автор/организатор:** Rinat Abdullin (+ TimeToAct Austria). Каталог: [[rinat-abdullin-blog-catalog-all-publications-2026]].

---

### Формат

Дружественное соревнование архитектур RAG. Цель: AI-система, отвечающая на вопросы по annual reports компаний. Техдетали в [GitHub-репозитории](https://github.com/abdullin/...).

**Round 2:** TimeToAct + спонсор IBM WatsonX AI. Задача: автоматически ответить на 100 случайных вопросов о 100 annual reports. Самый большой PDF - 1047 страниц; часть вопросов требует сравнения нескольких PDF.

- **Р** - Retrieval Score (max 100)
- **G** - Generation Score (max 100)
- **Score = R/3 + G** (max 133)
- 🔒 - полностью локальное решение

---

### Топ-результаты (Round 2, ключевые уроки)

| Позиция | Команда | Время | R/G | Score | Стек |
|---------|---------|-------|-----|-------|------|
| 1 | Ilya Rice | 49 min | 83/81 | 123.7 | Dense Retrieval + Router + LLM reranking + o3-mini, Parent-doc retrieval, Self-Consistency majority vote |
| 2 | Emil Shagiev | 55 min | 86/78 | 121.6 | **Без векторов**: query expansion + дешёвый LLM retrieval + мощный LLM generate, refine |
| 3 | Dmitry Buykin | 8h | 81/76 | 117.5 | Dynamic Struct. Output + SEC EDGAR ontologies, без embeddings |
| 4 | Sergey Nikonov | 30h | 85/73 | 116.4 | Все страницы через gpt-4o на каждый вопрос (дольше, проще) |
| 12 | Swisscom Innovation Lab 🔒 | 21h | 83/66 | 107.8 | Полностью локальная мульти-агентная LangGraph+LlamaIndex+Llama 3.3 |

Полный лидерборд: 43 команды. Позиции 2-3 доказывают: **векторы не обязательны** - структура+query expansion+SO CoT дают топ-результат.

---

### Ключевые паттерны-победители (повторяются в топ-10)

1. **Eval-first experimentation framework**: победа Round 2 - команда, заранее подготовившая framework экспериментов (Ilya оценил ~11 архитектур за часы).
2. **Router** - сначала выбрать релевантный агент/поток.
3. **LLM reranking** после плотного поиска (FAISS) - или parent-document retrieval (chunk → полная страница).
4. **Custom CoT + Structured Outputs** у лучших.
5. **Self-Consistency с majority vote** - согласованность как защита от галлюцинаций.
6. Честные "what didn't work" журналы (llama-3.1-8b reranking, gemini full-context, локальные embed-модели) - ценность R&D-прозрачности.

---

### Round 3 (планирование)

Цель: заранее дать всем участникам качественный eval + experimentation framework (сделать R&D процесс более сфокусированным). Урок Round 2: точно побеждает тот, у кого framework готов ДО соревнования. ETA был May-June 2025.

---

## Значение для AI QA

1. **Конкурентный RAG-бенчмарк = лаборатория evals.** Скорость (49 мин на топ-1) vs качество - подтверждение "eval-first" методологии.
2. **Score = R/3 + G** - классический раздельный учёт retrieval vs generation (ср. [[autonoma-rag-pipeline-2026]] "two surfaces, one score").
3. **PROBLEM ниши:** если агентные архитектуры способны к 99-123/133 за минуты-часы - верификация/мутация этих answer-пайплайнов становится задачей тест-инженера.
4. Связь с Victor: бенч/чЛенч-style прогонов можно переиспользовать как плоскость для mutation-based attestation (score-дельта при вносимых Defect'ах).

---

## Связанные темы

- [[rinat-ERC-winner-deep-dive-2026]] - разбор победителя
- [[rinat-llm-benchmarks-2026]] - семейный бенчмарк бизнес-нагрузок
- [[autonoma-rag-pipeline-2026]] - две поверхности RAG
- [[rinat-sgr-2026]] - SO CoT = структура победы
- [[llm-testing]] - golden dataset подход

---

### Источник
- [Enterprise RAG Challenge](https://abdullin.com/erc/) (2025-03-13)