# Vector Databases in Fintech

## Overview

Vector databases store data as high-dimensional embeddings and retrieve them by semantic similarity rather than exact field matching. In fintech, this capability transforms how fraud detection, compliance retrieval, routing optimisation, and customer intent understanding are implemented.

## Why Fintech Needs Semantic Retrieval

Traditional relational indexing operates on discrete fields: account number, amount, timestamp, merchant ID. Vector databases operate on *meaning* — the behavioural shape of a transaction, the contextual pattern of a support ticket, the semantic fingerprint of a compliance document.

Fintech systems generate high-dimensional signals at scale:
- Transactions (amount, corridor, velocity, counterparty history)
- Device fingerprints (OS, screen, network, sensor telemetry)
- Behavioural logs (clickstream, navigation paths, session duration)
- KYC documents (identity proofs, liveness checks, watchlist matches)
- Merchant metadata (category, geography, chargeback ratio, onboarding date)

Storing these signals as embeddings enables retrieval by similarity, which captures relationships that field-based indexing cannot express.

## Use Cases

### Fraud Pattern Detection

Static rule-based fraud systems (IF amount > threshold THEN flag) generate high false-positive rates and fail on novel attack vectors. Vector similarity over transaction embeddings detects behavioural proximity to known fraud clusters without explicit rules.

### Customer Intent Understanding

Support tickets, onboarding forms, and dispute descriptions are unstructured text. Embedding them and matching against intent clusters (e.g., "lost card" vs "unrecognised charge" vs "limit increase") routes cases to the correct workflow without keyword parsing.

### Compliance Retrieval

Policies, regulations, and case histories are stored as embeddings. A compliance officer querying "cross-border sanctions exposure for high-velocity merchant corridors" retrieves semantically related documents, not just those matching the exact phrase.

### Routing Optimisation

Transaction metadata and corridor behaviour embedded together allow routing engines to select the optimal payment rail based on similarity to historical success patterns — not just static cost tables.

## Engineering Considerations

### ANN Indexes

Vector databases use approximate nearest neighbour (ANN) indexes for real-time retrieval:
- **HNSW** (Hierarchical Navigable Small World) — high recall, moderate memory, suitable for production fraud scoring
- **IVF** (Inverted File Index) — lower memory, good for large-scale batch retrieval
- **PQ** (Product Quantisation) — compression-heavy, useful when storage is constrained

### Hybrid Search

Production fintech systems combine vector similarity with traditional field filters: "transactions similar to fraud pattern X *and* above $10,000 *and* in corridor Y." Most vector DBs support hybrid search (e.g., filtering before ANN, or combining scores).

### Embedding Lifecycle

Fraud patterns evolve, new corridors open, merchant behaviour shifts. Embeddings must be refreshed periodically. The pipeline:
1. Generate embeddings from current data (using a consistent model)
2. Rebuild ANN indexes
3. Validate recall on known fraud/legacy test sets
4. Deploy new index with backward-compatible query fallback

### RAG for Operations

Retrieval-Augmented Generation powers agent assist, dispute resolution, and compliance QA. The retrieval stage uses vector DBs to fetch relevant context (policy snippets, past resolutions, regulatory text) before the LLM generates a response.

## Embedding Quality: The Hidden Lever

Choosing the database is only half the work. Embeddings define what "similarity" means. In fintech, that meaning must align with risk, behaviour, and regulatory context. The quality of fraud detection, anomaly scoring, routing optimisation, and semantic retrieval depends on how well embeddings capture the true structure of transactions, devices, merchants, and customer behaviour.

Good vector representations:
- Reduce noise by separating signal (fraud cluster shape) from coincidence (same amount by chance)
- Improve recall by matching on behavioural pattern rather than discrete fields
- Make downstream models more reliable by feeding them semantically coherent inputs

Bad embeddings produce high-recall-low-precision retrieval — semantically empty matches that degrade fraud models and confuse RAG responses.

## Vector DB as Risk Infrastructure

Vector databases are not just "AI infrastructure." In fintech, they become risk infrastructure — enabling faster decisions, fewer false positives, and more resilient global payment flows. The operational risk of a bad vector DB deployment (missed fraud, wrong compliance match, misrouted payment) is comparable to a failed rule engine or a corrupted lookup table.

## Quality Assurance for Vector DB Deployments

Testing a vector DB in fintech requires more than unit tests on queries:

- **Recall@K validation** — what fraction of true neighbours appear in the top K results; critical for fraud detection where missing one match is a miss
- **Embedding drift measurement** — track cosine similarity drift between model versions; flag deployments where embeddings shift > threshold
- **Hybrid filter correctness** — ensure combined vector + field filters return expected intersections, not false positives from either side
- **Latency SLOs under load** — ANN index build time, query latency at P50/P95/P99, re-indexing overhead
- **Golden dataset for regression** — curated set of known matches (fraud cluster, compliance pair, routing case) that must rank in top-K after every embedding re-index

## Key Players (2026)

- **Pinecone** — managed, serverless, hybrid search, pod-based indexes
- **Qdrant** — open-source, local filtering, payload storage, gRPC API
- **Weaviate** — open-source, built-in vectoriser modules, GraphQL API
- **Milvus** — cloud-native, GPU-accelerated, distributed, CNCF graduated
- **Chroma** — lightweight, embedded, developer-friendly, Python-first
- **pgvector** — PostgreSQL extension, no separate infrastructure, hybrid search

## References

- Johnson, J., Douze, M., & Jegou, H. (2019). Billion-scale similarity search with GPUs. *IEEE Transactions on Big Data*.
- Malkov, Y. A., & Yashunin, D. A. (2020). Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs. *IEEE TPAMI*.
- Pinecone. (2026). Hybrid Search: Combining Vector and Keyword Search. pinecone.io/learn/hybrid-search/
- Qdrant. (2026). Filtering and Payloads. qdrant.tech/documentation/filtering/
- pgvector. (2026). Open-source vector similarity search for Postgres. github.com/pgvector/pgvector








<!-- backlinks-start -->
### Backlinks
- [21 Cfr Part 11 Electronic Records 2026](wiki/21-cfr-part-11-electronic-records-2026.md)
<!-- backlinks-end -->
