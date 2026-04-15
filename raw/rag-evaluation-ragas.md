# RAG Evaluation Using Ragas

**Source:** BeyondQuality Research — [GitHub](https://github.com/BeyondQuality/beyondquality/blob/main/research/rag-evaluation.md)
**Date:** 2025-09-11
**Authors:** Anupam Krishnamurthy, Vitaly Sharovatov

## Key Findings

### What is RAG?
- Retrieval Augmented Generation helps LLMs handle large context
- Breaks documents into chunks, indexes them, retrieves relevant parts
- Solves LLM context window degradation problem

### RAG Testing Challenges
1. **Non-determinism** — LLMs don't produce deterministic outputs
2. **Qualification difficulty** — Traditional testing doesn't work
3. **Evaluation frameworks** — Need objective metrics

### Ragas Metrics
- **Answer Relevance** — Is response relevant to prompt?
- **Faithfulness** — Is model faithful to retrieved context?
- **Context Relevance** — Is retrieved context relevant to question?
- **Method:** LLM-as-judge for evaluation

### RAG Customization Levers
1. Retrieval algorithm + parameters
2. Chunking strategy (how data is split)
3. Embedding choice (for vector DB)
4. Vector DB selection

### Key Insights
- Automated evaluation complements but doesn't replace human testing
- Security risk: prompt injection via retrieved context
- Model size matters (gpt-4o vs gpt-4o-mini for nuanced answers)
- Reasoning models (gpt-5) don't work with Ragas (temperature locked)

## Testing Implications

1. **Test RAG systems like AI systems** — not traditional software
2. **Use multiple evaluation metrics** — single metric insufficient
3. **Human judgment still required** — for nuanced quality
4. **Security testing needed** — indirect injection attacks
