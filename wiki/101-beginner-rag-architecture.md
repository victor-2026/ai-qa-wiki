---
title: "RAG Architecture for Beginners"
type: skill
updated: "2026-09-22"
tags: [rag, embeddings, vector-database, semantic-search, skill]
---

# RAG Architecture for Beginners

## What It Is
RAG = Retrieval-Augmented Generation. AI-приложение не отвечает «по памяти» — оно сначала **ищет** ответ в своём корпусе документов, а потом **генерирует** ответ на основе найденного. Три главных куска: (1) индексация документов, (2) поиск по запросу, (3) генерация с найденным контекстом.

Для QA это важно: RAG — база многих AI-продуктов (support bot, внутренний search, документ-ассистент), и тестируем мы не «модель», а связку «модель + база + поиск».

## The Three-Stage Pipeline (для чайников)

**Stage 1 — Embedding (индексация).**
Документ режется на куски (chunks, обычно 300-1000 токенов), каждый кусок превращается в вектор-число (embedding) через модель-энкодер. Похожие по смыслу куски получают похожие вектора.

Пример:
```
"Кофе портится"      → [0.1, 0.8, 0.3, ...]
"Как хранить кофет"  → [0.1, 0.7, 0.3, ...]  // похожий вектор
"Погода в Минске"    → [0.9, 0.2, 0.5, ...]  // далёкий вектор
```

**Stage 2 — Semantic search (поиск).**
Пользовательский вопрос тоже становится вектором. Вычисляется близость (cosine similarity) между вектором вопроса и векторами всех кусков. Возвращаются top-K самых близких.

Пример:
```
Вопрос: "Кофе испортился" → [0.1, 0.75, 0.3, ...]
→ ближайший кусок: "Замечаете что кофе неприятно пахнет" (score 0.91)
→ это и есть то, что LLM получит как контекст
```

**Stage 3 — Generation (генерация).**
Найденные куски + вопрос попадают в промпт LLM. LLM отвечает, опираясь только на эти куски. Промпт выглядит примерно так:

```
Контекст: [top-K кусков]
Вопрос: "Кофе испортился"
Ответь только на основе контекста.
```

## Vector Databases — что это и почему
Обычная БД (SQL) ищет точное совпадение. Vector DB (pgvector, Chroma, Milvus, Weaviate, Pinecone, Qdrant, FAISS) ищет **семантическую близость** — это главный навык.

| Вопрос | SQL | Vector DB |
|---|---|---|
| «Сколько заказов у клиента 42?» | ✅ точный запрос | ❌ не умеет |
| «Найди документ по смыслу похожий на запрос» | ❌ не умеет | ✅ similarity search |

Начальник сематики: **чушки с индексом** одинаково бесполезны. Хорошая vector DB нужна, когда корпус большой (10k+ документов) и поэтому линейный перебор медленный. На маленьком корпусе можно без vector DB — просто в памяти.

## Semantic Search Optimization (что оптимизируют)
1. **Chunk size** — мелкие куски (200-300 токенов): точнее релевантность, но теряется контекст. Крупные (1000+): больше контекста, но больше шума. Тестировать порог на реальных запросах.
2. **Embedding model** — разные модели дают разную размерность (768, 1024, 1536) и качество. Пробовать на эталонном наборе.
3. **Top-K** — сколько кусков отдать LLM. K=3 мало, K=10 шумно.
4. **Re-ranking** — грубый поиск + потом дорогая пере-ранжировка top-50 → top-5.
5. **Hybrid search** — semantic + BM25 (ключевые слова) вместе. Для «точных» терминов (артикул, кодовое слово) semantic один может промахиваться.

## TL;DR Для резюме
- **RAG architecture**: ingesting (chunking + embeddings) → retrieval (semantic search, top-K) → generation (context-grounded answer).
- **Embeddings**: text → vector; cosine similarity; выбрать модель и размерность.
- **Vector DB**: pgvector (самый простой, в PostgreSQL), Chroma (beginner), FAISS (библиотека, не сервер), Milvus/Pinecone/Qdrant (production).
- **Semantic search optimization**: chunk-size, embedding-model, top-K, re-ranking, hybrid retrieval, fallback на ключевой поиск.

## Связанные страницы (тестирование RAG)
- [[wiki/rag-evaluation-ragas|RAG Evaluation Using Ragas]]
- [[wiki/rag-evaluation|RAG Evaluation Framework]]
- [[wiki/autonoma-rag-pipeline-2026|How to Test a RAG Pipeline: Two Surfaces]]
- [[wiki/autonoma-rag-retrieval-2026|How to Test if RAG Is Retrieving the Right Context]]
- [[wiki/autonoma-rag-evaluation-metrics-2026|Autonoma RAG Evaluation Metrics]]
- [[wiki/vector-databases-fintech-2026|Vector Databases in Fintech]]
- [[wiki/loris-bartolini-jean-yves-garcin-banking-rag-adversarial-testing-2026|Banking RAG Adversarial Testing]]