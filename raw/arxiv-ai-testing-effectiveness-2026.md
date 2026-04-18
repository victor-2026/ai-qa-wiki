# Arxiv Papers: AI Testing Effectiveness Research

**Source:** Arxiv.org search results
**Date:** 2026-04
**Context:** Collection of 30+ research papers on AI Testing effectiveness

---

## Papers Collection (March 2026)

### 2603.24160 - PersonaTester
- **Title:** Towards Automated Crowdsourced Testing via Personified-LLM
- **Authors:** Shengcheng Yu, Yuchen Ling, Chunrong Fang, Zhenyu Chen, Chunyang Chen
- **Venue:** FSE 2026
- **Key Findings:**
  - LLM agents for crowdsourced GUI testing
  - +117-126% improvement over baseline
  - Found 100+ crashes, 11 functional bugs
  - Simulates diverse human-like testing behaviors via personas

### 2603.23448 - Code Review Agent Benchmark (c-CRAB)
- **Title:** Code Review Agent Benchmark
- **Authors:** Yuntong Zhang, Zhiyuan Pan, Imam Nur Bani Yusuf, Haifeng Ruan, Ridley Shariffdeen, Abhik Roychoudhury
- **Key Findings:**
  - Current agents solve only 40% of code review tasks
  - Benchmark constructed from human reviews
  - Evaluates Devin, Claude Code, Codex, PR-agent
  - Agent reviews consider different aspects than human reviews

### 2603.23142 - LLM Testing Certification
- **Title:** Can Language Models Pass Software Testing Certification Exams?
- **Authors:** Fitash Ul Haq, Jordi Cabot
- **Key Findings:**
  - Evaluated 60 multimodal language models on ISTQB exams
  - 1,171 questions across 30 certification exams
  - Two models passed all certifications (65%+)
  - Commercial models outperform open-source

### 2603.28592 - AI Code Debt
- **Title:** Debt Behind the AI Boom: A Large-Scale Empirical Study of AI-Generated Code in the Wild
- **Authors:** Yue Liu, Ratnadira Widyasari, Yanjie Zhao, Ivana Clairine Irsan, David Lo
- **Key Findings:**
  - 304,362 verified AI-authored commits from 6,275 GitHub repos
  - 5 AI coding assistants studied
  - 484,606 distinct issues identified (89.1% code smells)
  - 15%+ commits from each assistant introduce issues
  - 24.2% of AI-introduced issues survive in latest revision

### 2603.26487 - GenAI Governance OSS
- **Title:** Beyond Banning AI: A First Look at GenAI Governance in Open Source Software Communities
- **Authors:** Wenhao Yang, Runzhi He, Minghui Zhou
- **Key Findings:**
  - 67 highly visible OSS projects analyzed
  - 3 governance orientations: ban, adapt, integrate
  - 12 governance strategies identified
  - Beyond banning - coordinated responses needed across accountability, verification, review capacity, code provenance

### 2603.26329 - LLM Testing Education
- **Title:** Large Language Models for Software Testing Education: an Experience Report
- **Authors:** Peng Yang, Yunfeng Zhu, Chao Chang, Shengcheng Yu, Zhenyu Chen, Yong Tang
- **Venue:** FSE 2026 Education Track
- **Key Findings:**
  - Phase I: 15 students + 337 survey responses
  - Identified prompt-related difficulties: missing context, insufficient constraints, rigid one-shot prompting
  - Phase II: stage-aware prompt scaffold for test generation
  - Automated test script generation is heterogeneous and effort-intensive

### 2603.25507 - Network Traffic Synthesis
- **Title:** Lightweight GenAI for Network Traffic Synthesis: Fidelity, Augmentation, and Classification
- **Authors:** Giampaolo Bovenzi et al.
- **Key Findings:**
  - Lightweight GenAI for network traffic generation
  - Up to 87% F1-score on synthetic-only training
  - +40% improvement in low-data regimes
  - Transformer-based models best trade-off

---

## Papers Collection (February 2026)

### 2602.21997 - LLM Test Generation Coverage
- **Title:** Enhancing LLM-Based Test Generation by Eliminating Covered Code
- **Authors:** WeiZhe Xu, Mengyu Liu, Fanxin Kong
- **Key Findings:**
  - Scalable LLM-based unit test generation
  - Context information retrieval using LLMs + static analysis
  - Iterative test generation with code elimination
  - Outperforms state-of-the-art LLM and search-based methods

### 2602.13766 - GenAI Agile Productivity
- **Title:** Impacts of Generative AI on Agile Teams' Productivity: A Multi-Case Longitudinal Study
- **Authors:** Rafael Tomaz, Paloma Guenes, Allysson Allex Araújo, Maria Teresa Baldassarre, Marcos Kalinowski
- **Venue:** Forge 2026
- **Key Findings:**
  - 13-month multi-case study, 3 agile teams
  - SPACE framework evaluation
  - Sharp increase in Performance + Efficiency, flat Activity
  - GenAI increases value density, not volume

### 2602.12256 - Few-shot Test Generation
- **Title:** Automated Test Suite Enhancement Using Large Language Models with Few-shot Prompting
- **Authors:** Alex Chudic, Gül Çalıklı
- **Venue:** ICPC 2026
- **Key Findings:**
  - Human-written examples produce best coverage and correctness
  - Combined similarity of problem description + code yields best prompts
  - GPT-4o evaluated on HumanEval, ClassEval

### 2602.10522 - ConVerTest
- **Title:** Consistency Meets Verification: Enhancing Test Generation Quality in LLMs Without Ground-Truth Solutions
- **Authors:** Hamed Taherkhani et al.
- **Key Findings:**
  - Two-stage pipeline without requiring code implementations
  - Self-Consistency (SC) + Chain-of-Verification (CoVe) + Dual Execution Agreement
  - +39% validity, +28% coverage, +18% mutation scores
  - Mitigates hallucinations in autonomous testing agents

### 2602.08242 - HTTP API Testing
- **Title:** Software Testing at the Network Layer: Automated HTTP API Quality Assessment and Security Analysis
- **Authors:** Ali Hassaan Mughal, Muhammad Bilal, Noor Fatima
- **Key Findings:**
  - 18 production websites, 108 HAR files
  - Quality scores: 56.8 to 100
  - Redundant API calls (67%), missing cache headers (67%)
  - Third-party overhead >20% on 72% of sites

### 2602.07412 - GenAI IDE Futures
- **Title:** Forecasting Developer Environments with GenAI: A Research Perspective
- **Authors:** 33 experts from SE, AI, HCI (Raula Gaikovina Kula et al.)
- **Venue:** Shonan Meeting 222
- **Key Findings:**
  - Four themes for future research
  - IDE abstraction level changing with GenAI
  - Human-AI interaction evolution in IDEs

---

## Papers Collection (January 2026)

### 2601.17903 - REST API Test Amplification
- **Title:** Prompt-Based REST API Test Amplification in Industry: An Experience Report
- **Authors:** Tolgahan Bardakci, Andreas Faes, Mutlu Beyazit, Serge Demeyr
- **Key Findings:**
  - Largest logistics company in Belgium
  - Production microservice with security-sensitive system
  - LLM-based test amplification increases coverage
  - Practical use in industry confirmed

---

## Key Themes Summary

| Theme | Papers | Key Insight |
|-------|--------|--------------|
| Agentic Testing | PersonaTester, c-CRAB | Multi-agent systems outperform; 40% task solve rate |
| Test Generation | 2602.21997, 2602.12256, ConVerTest | Coverage + validity improvements via iteration |
| Technical Debt | 2603.28592 | 24.2% of AI issues survive long-term |
| Governance | 2603.26487 | 12 strategies, 3 orientations beyond banning |
| Education | 2603.26329 | Prompt scaffolding critical for students |
| Productivity | 2602.13766 | Value density increases, not volume |
| Industry | 2601.17903 | Confirmed practical utility in logistics |
| Benchmarking | c-CRAB, PersonaTester | Growing number of evaluation frameworks |

---

## Metrics Identified

- **F2P** (Failures to Pass) — Bug discovery rate
- **Coverage** — Line/branch coverage from AI tests
- **Validity** — Test quality without ground truth
- **Mutation Scores** — Test effectiveness
- **SPACE** — Satisfaction, Performance, Activity, Communication, Efficiency

---

## Related

- [[raw/ai-testing-effectiveness-papers]] — Original summary
- [[wiki/topics-map]] — Full wiki overview
- [[wiki/testing-strategies]] — Testing strategies
- [[wiki/ai-testing-metrics]] — Metrics deep dive