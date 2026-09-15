# ARIA — QA Data Automation Agent (Agentic RAG + LLM Judge)

> arxiv.org/abs/2609.04913 (Sep 2026). Authors: Qixiao Zhang, Yuxin Wang, Yifei Li, Xiao Yu, Haotian Li, Yue Liu, Xin Liang, Fan Shu.

Agentic RAG-based data automation agent that autonomously handles end-to-end QA workflows for complex numerical tabular data. Published as **arXiv preprint** (no peer review).

## Problem
QA on real-world tabular data requires domain knowledge (ontology), iterative processing, and high-accuracy tool orchestration. Rule-based and fixed-pipeline agents fail on low-resource domains and messy real-world datasets.

## Architecture — Three-Layer System

### 1. Data Extraction Layer (Crawling Module)
- Multi-layer parsing: HTML → table recognition → content extraction
- Outputs clean structured tables

### 2. Reflection / Reasoning Layer
- **Agentic RAG**: domain-specific retrieval with iterative query refinement
- **Wiki ontology tree**: domain knowledge graph for query planning
- **Reflection mechanism**: automatic plan adjustment based on feedback

### 3. Verification Layer (LLM-Judge)
- Two-stage judge with **three core metrics**:
  - **Data Integrity** — no fabricated values
  - **Reasoning Consistency** — logic matches conclusions
  - **Sufficiency** — all sub-questions answered

## 30+ Tools
- Pandas, NumPy, Python execution, search, plotting, web crawling
- **Domain-specific tools** for complex operations

## Results
- **Non-IID data** (27.6%): ARIA significantly outperforms Agent-R
- **IID data** (23.5%): less benefit (domain knowledge less critical)
- Strong correlation between Reflection, Wiki, and LLM-Judge metrics
- Evaluation on **SDEBench** (software engineering benchmark)

## Key Insights for QA
- **Agentic RAG > fixed pipeline** for QA tasks requiring domain knowledge
- **LLM-as-Judge as verification gate** — same pattern as mutation testing quality gates
- **Domain ontology** = structured knowledge improves data verification accuracy
- **Reflection loop** = the agent adjusts its plan when intermediate results are wrong (similar to self-healing in test automation)

## Meta
- Source: arxiv.org/abs/2609.04913
- Date: 2026-09-09 (submitted)
- Tags: #agentic-rag, #llm-judge, #data-verification, #qa-automation, #arxiv-2026
- See also: [[llm-testing]], [[known_patterns|Pattern: llm_filter_approach]], [[mas-testing-framework]]
