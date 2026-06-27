# Contextualizing Prompts with RAG

**Source**: Chapter 11, *Software Testing with Generative AI* (pages 250-275)

## 11.1 RAG Components

1. **Corpus** - Collection of documents
2. **Embeddings** - Convert text to vectors
3. **Similarity Search** - Find relevant docs
4. **Prompt Builder** - Combine query + docs

---

## 11.2 Implementation

```java
// Find closest document
public String findClosestMatch(List<String> corpus, String query) {
    // Use cosine distance
}

// Build prompt
public String buildPrompt(String query, String relevantDoc) {
    return "You are expert tester..." + relevantDoc + "\n" + query;
}
```

---

## 11.3 Embeddings & Search

### Simple: Cosine Distance
```java
CosineDistance cosineDistance = new CosineDistance();
double distance = cosineDistance.apply(doc, query);
```

### Limitation
Simple distance may not find best match.

---

## 11.4 Advanced Tools

| Tool | Type |
|------|------|
| Pinecone | Vector DB |
| Weaviate | Open source |
| Chroma | Lightweight |

---

## Вопросы к главе

1. Компоненты RAG?
2. Как работает similarity search?
3. Ограничение cosine distance?
4. Какие vector databases используются?
5. Что такое embeddings?
6. Как работает chunking документов?
7. Что такое vector database?
8. Пример использования RAG в тестировании?

---

## Related Topics

- [Ch10: Customized LLMs](ch10-customized-llms.md)
- [Ch12: Fine-tuning](ch12-fine-tuning.md)

---

*Licensed content: Software Testing with Generative AI (EuroSTAR)*