# The 4+ Folder Structure for Every AI Project

## Core (4 Folders)

```
├── raw/           # Source data (PDFs, articles, original inputs)
├── wiki/          # Processed/organized knowledge base
├── outputs/       # Generated artifacts (summaries, charts)
└── docs/         # Documentation
```

## Extended (9 Folders - Production-Ready)

Based on community feedback:

```
├── agents/       # Agent nodes (decision trees, node definitions)
├── memory/       # Adapters, integrations, retrieval logic
├── tools/        # Tool implementations (external APIs, functions)
├── prompts/      # Prompt templates + modules
├── retrieval/    # Vector stores, Elasticsearch, ranking
├── llm/         # LLM client, caching, telemetry
├── api/          # Routes, chat service
├── db/           # SQL models, repositories
└── evals/        # Test cases, scorecards, traces
```

## The "Missing" Folder

```
specs/           # Specifications - requirements, interfaces, contracts
```

## Decision

**Recommendation:** Use 4 folders for simple projects, scale to 9+ for production AI systems.

**Key insight:** Start simple, evolve as complexity grows.

---

## Sources

- karpathy/llm.c
- community feedback (HN, Discord)
