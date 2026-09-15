# RAG Evaluation — How to Test Retrieval-Augmented Generation

RAG (Retrieval-Augmented Generation) systems combine retrieval (finding relevant documents) with generation (LLM producing answers). Testing them requires evaluating **both** the retrieval quality and the generation quality — not just one.

## Why RAG Testing Is Hard

| Challenge | Why |
|-----------|-----|
| **Non-determinism** | Same query → different answers each run |
| **No single oracle** | Multiple correct answers exist |
| **Two failure modes** | Bad retrieval OR bad generation (or both) |
| **Context window limits** | Chunking strategy affects what the model sees |
| **Hallucination vs faithful** | Model may ignore retrieved context |

## Evaluation Dimensions

### 1. Retrieval Quality
Did the system find the right documents?

- **Context Precision** — out of retrieved chunks, how many are relevant?
- **Context Recall** — out of all relevant chunks, how many were retrieved?
- **Chunk relevance** — are individual chunks actually useful?

### 2. Generation Quality
Did the LLM produce a good answer from the retrieved context?

- **Faithfulness** — is the answer grounded in the retrieved context (not hallucinated)?
- **Answer Relevance** — does the answer actually address the question?
- **Answer Correctness** — is the answer factually correct?

### 3. End-to-End Quality
- **Correct Answer Rate** — percentage of questions answered correctly
- **Refusal Rate** — does the system say "I don't know" when it should?
- **Latency** — time from query to answer

## Evaluation Frameworks

### Ragas (Reference-based)
- Metrics: Faithfulness, Answer Relevance, Context Relevance, Context Precision
- Uses LLM-as-judge for scoring
- Requires ground truth Q&A pairs for some metrics
- Reference: [[rag-evaluation-ragas]]

### RAGAS (no reference)
- Context Recall, Context Precision, Faithfulness, Answer Relevance
- Can evaluate without ground truth (some metrics)

### LLM-as-Judge Pattern
- Use a stronger model (GPT-4) to evaluate a weaker model's output
- Score: 0-1 per dimension
- Cheaper than human evaluation, faster than pairwise comparison
- Reference: [[llm-testing]], [[aria-qa-data-automation-agent-2026]]

## RAG Customization Levers (What to Vary in Tests)

| Lever | What It Controls |
|-------|-----------------|
| **Retrieval algorithm** | BM25, vector search, hybrid |
| **Chunking strategy** | Fixed-size, semantic, sliding window |
| **Embedding model** | OpenAI, Cohere, local models |
| **Vector DB** | Pinecone, Weaviate, Qdrant, pgvector |
| **Top-K** | How many chunks retrieved |
| **Re-ranking** | Post-retrieval relevance ordering |

Each lever is a variable to test. Changing chunking from 512 to 1024 tokens can double recall but halve precision.

## Testing Patterns

### Pattern 1: Retrieval Sanity Check
```
Given: document containing "X is Y"
When: user asks "What is X?"
Then: retrieved chunks contain the answer
```

### Pattern 2: Faithfulness Test
```
Given: retrieved context does NOT contain answer
When: LLM generates response
Then: response says "I don't know" or "not found in context"
     (NOT a hallucinated answer)
```

### Pattern 3: Irrelevant Context Rejection
```
Given: retrieved chunks are about Topic A
When: user asks about Topic B
Then: response says "not relevant" or provides minimal answer
     (NOT a confident answer from wrong context)
```

### Pattern 4: Multi-chunk Aggregation
```
Given: answer requires combining info from 3 chunks
When: only 2 of 3 retrieved
Then: partial answer or "insufficient information"
     (NOT a complete answer fabricated from thin air)
```

## Security Testing for RAG

- **Indirect injection via retrieved context** — malicious content in source documents that hijacks the LLM
- **Prompt injection through search** — user query crafted to manipulate retrieval
- **Data exfiltration** — system reveals sensitive chunks it shouldn't

Reference: [[llm-testing]], [[known_patterns|Pattern: llm_filter_approach]]

## Metrics Summary

| Metric | What It Measures | Requires Ground Truth? |
|--------|-----------------|----------------------|
| Context Precision | Retrieved chunks relevance | Partial |
| Context Recall | Coverage of relevant docs | Yes |
| Faithfulness | Answer grounded in context | No (LLM-as-judge) |
| Answer Relevance | Answer addresses question | No (LLM-as-judge) |
| Answer Correctness | Factual accuracy | Yes |
| Refusal Rate | Says "don't know" appropriately | Yes |

## Source
- Reference: `raw/rag-evaluation-ragas.md` (BeyondQuality Research)
- See also: [[rag-evaluation-ragas]], [[llm-testing]], [[mas-testing-framework]], [[Test-Reliability]]
- Tags: #rag, #evaluation, #retrieval, #faithfulness, #llm-judge, #chunking
