# Ruben Hassid: Jev — "Internet moment", setup + 3 use cases (2026-09-21)

**Author:** Ruben Hassid ("Master AI before it masters you", newsletter)
**Source:** LinkedIn post 2026-09-21 (5h old)
**Context:** Same Jev as typesafe-jev-judgment-service-gates-2026.md — TypeSafe Jev (judgment service, not an LLM).

---

## Positioning

- Called "Internet moment" for AI industry — tells LLMs what to do next, in milliseconds, at almost zero cost.
- "If you set it up correctly, you will have the AI engineer's setup for 2028" (hype discount applies).

## Setup (from post)

1. Join waitlist: typesafe.ai (fairly quick per Ruben)
2. Go to Claude Code or Codex
3. Choose Opus 5-Low or Sol-Low (model variants)
4. Copy-paste prompt: `[claude or codex] plugin marketplace add typesafe-ai/skills` + `[claude or codex] plugin install typesafe@typesafe`
5. `/typesafe` skill shows up
6. Paste API key once, click "Allow"
7. Start with $5 free credit. "It's hard to spend more."

## The 3 use cases

### 1. Jev for LinkedIn (outreach classification)
- Context: 38,000 connections & invitations, new company launch, need a few hundred people to message.
- Flow: Export LinkedIn connections/invitations → Connect Claude to GitHub, Vercel & Apify → Apify API key to enrich → LinkedIn Settings → Data privacy → Get copy (ZIP by email) → find Connections CSVs → upload to Jev → classify contacts → review shortlist.

### 2. Jev for Gmail
- Flow: Google Contacts → Other contacts → Select all → Export → upload to Claude Code/Codex → Jev sorts into Keep / Review / Remove → review before removing anything.

### 3. Overwhelm (Claude Code + GitHub + Vercel + Apify + Jev + Typesafe)
- Full copy-paste prompts per use case in the newsletter (https://lnkd.in/ePyG-QKM). 45s TL;DR by Matija Sosic (X).

## Relevance

- Use case 1 (LinkedIn contacts classification → shortlist) = direct match for Victor's outreach pipeline (export connections, enrich, classify, shortlist); Jev primitives (choice/score/bool + calibrated confidence) replace ad-hoc LLM classification.
- Signal: plugin-driven distribution (Claude Code/Codex skill), $5 free credit, "hard to spend more" — consistent with 20-200x cheaper positioning from prior raw.
- judgment-as-a-service spreading: Paluy, Gareth Sharpe, Watsche, now Ruben's outreach use cases → market confirmation of the "code controls workflow, Jev supplies judgment" pattern.