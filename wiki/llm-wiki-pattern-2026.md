# LLM Wiki Pattern (Karpathy): Mechanics & Our Delta

**Source:** https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f (April 2026, 16M+ views, 5K+ stars gist)
**Related:** `wiki/karpathy-autoresearch-agentic-engineering-2026.md` (loop engineering, not this pattern), `wiki/everyinc-compound-engineering-loop-2026.md` (compounding knowledge = same principle)
**Scope:** How Karpathy's LLM Wiki builds self-sustaining knowledge; what this wiki implements vs what we lack.

---

## The core synergy

Three layers + shifting the maintenance tax onto the LLM. Obsidian = IDE, the LLM = programmer, the wiki = codebase.

1. **Three layers:** `raw/` (immutable sources) + `wiki/` (LLM-generated pages) + `schema` (CLAUDE.md/AGENTS.md). The schema is what turns the LLM into a "disciplined wiki maintainer rather than a generic chatbot" — without it the LLM produces inconsistent output.
2. **Compiler analogy:** raw = source code, LLM = the compiler, wiki = the executable output, lint = tests, queries = runtime.
3. **Three operations:**
   - **Ingest** — one source "cascades" through 10-15 wiki pages (updates entity/concept pages, index, log). Preferred one-at-a-time with human steering.
   - **Query** — read `index.md` first to navigate, drill into relevant pages; **valuable answers get filed back into the wiki as new pages** so explorations compound like ingested sources.
   - **Lint** — periodic health-check: contradictions between pages, stale claims superseded by newer sources, orphan pages with no inbound links, concepts lacking a page, missing cross-references, data gaps.

## Design pillars (quotes from the gist)

- **"The wiki is a persistent, compounding artifact."** Knowledge is compiled once and kept current, not re-derived on every query (the key difference vs RAG).
- **"The wiki stays maintained because the cost of maintenance is near zero."** Humans abandon knowledge bases because bookkeeping grows faster than value. LLMs don't get bored, don't forget to update a cross-reference, can touch 15 files in one pass.
- **Division of labor:** "The human's job is to curate sources, direct the analysis, ask good questions... The LLM's job is everything else" — summarizing, cross-referencing, filing, bookkeeping.
- Spiritual ancestor: Vannevar Bush's Memex (1945) — connections between documents as valuable as the documents. Bush couldn't solve "who does the maintenance"; the LLM does.
- **`index.md`** — content catalog, updated on every ingest; read first to navigate. Works at moderate scale (~100 sources, ~hundreds of pages) without embedding RAG.
- **`log.md`** — append-only operation log.

## Community hardening (battle-tested deltas)

From the karpathy-wiki protocol repos (danvega, Alirezajalilii, toolboxmd):

- **Verification gate** after every task (8-point checklist) — "the agent will remember to update the wiki" is false; a gate forces it.
- **No placeholders ever** — "later" never comes.
- **Contradictions:** document both positions, flag PENDING, escalate to human — agent never silently picks one.
- **Multi-session compilation** in phases with hard STOP boundaries (one session silently truncates/hallucinates coverage).
- **Confidence scoring** (Synthadoc): structured JSON schemas, source URLs pinned to every page, human-in-the-loop below an 80% confidence threshold; contradictions at low confidence queue for manual review.
- **Scale limits:** ~50-200 sources / ~200 files before you need directory-level indexes, hybrid search (qmd BM25/vector), or multi-agent governance.

## Our implementation — delta map

| Karpathy mechanic | We have | Gap |
|---|---|---|
| `raw/` immutable | ✅ (AGENTS.md boundary: never edit) | — |
| `wiki/` LLM-owned | ✅ scripted ingest | — |
| Schema/AGENTS.md | ✅ boundaries table + workflow | — |
| Ingest cascades | ⚠️ backlinks to 5 related pages auto; content of related pages not rewritten | Cascade update of entity/concept pages |
| Query → files back into wiki | ⚠️ ad-hoc (rarely) | Regular "save answer as page" |
| `index.md` | ✅ `wiki-topics.json` (auto via `--update-index`) | — |
| `log.md` append-only | ❌ none (git + session-checkpoint only) | **Add** |
| Lint (contradictions/stale/orphans) | ❌ ad-hoc Sunday ritual | **Automate** |
| Confidence frontmatter | ❌ minimal frontmatter | optional |
| Cache/search (qmd) | ⚠️ index.json only | optional at scale |

## What we're adding (this session)

1. **`wiki/log.md`** — append-only operation log written by `wiki_llm.py` on every ingest/index/sync.
2. **`wiki_llm.py --lint`** — deterministic + LLM-assisted health check replacing the manual Sunday ritual:
   - deterministic: orphan pages (no inbound links), broken internal links, raw→wiki mismatches, stub pages
   - LLM crate: contradiction scan between strongly-related pages, new connection suggestions
3. **Checkpoint / global memory** — Sunday ritual → run `--lint`, review `outputs/lint-report-*.md`.

## Why this matters for our series

- The wiki IS our "network that compounds" (Mogilko insight, `wiki/ai-agents-replace-team-entrepreneurs-mogilko-yampolskiy-2026.md`) — the irreplicable institutional QA knowledge.
- The LLM-wiki self-maintenance loop is the same engineering principle as our mutation-gated regex suite: pay maintenance upfront, keep the artifact green at near-zero cost.
- "Compile once, keep current, don't re-derive" is the QE answer to RAG-cost-of-every-query — evidence compiled into wiki pages beats re-scraping raw on each answer.

---
*Source: [raw/Agents-discussion-300526.md](../raw/Agents-discussion-300526.md) + Karpathy gist (external) · Cross-references in place.*