# AI QA Wiki

LLM-powered knowledge base for AI Testing best practices, patterns and research.

## Structure

```
raw/       — Source materials (articles, papers, notes, snippets)
wiki/      — AI-organized knowledge (extracted from raw)
outputs/   — Generated artifacts (podcasts, summaries, reports)
```

## Principles

1. **AI owns the wiki layer** — Don't edit wiki manually
2. **Knowledge compounds** — Answers go back to wiki
3. **Just collect** — AI organizes automatically
4. **Monthly lint** — Check for contradictions
5. **Source files are never modified by AI**

## Workflow

1. Add interesting AI/QA content to `raw/`
2. Ask questions via `wiki_llm.py --ask "..."`
3. AI extracts and organizes knowledge into `wiki/`
4. Generate outputs (summaries, podcasts) in `outputs/`

## Content Areas

- AI Testing Strategies
- LLM Evaluation & RAG Testing
- Prompt Engineering for QA
- AI-Assisted Test Automation
- Quality Metrics for AI Systems

## Tools

```bash
# Q&A about wiki
python3 wiki_llm.py --ask "вопрос"

# Generate podcast from topic
python3 wiki_llm.py --podcast "тема подкаста"

# Monthly lint check
python3 wiki_llm.py --lint
```
