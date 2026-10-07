# OpenAI Wiki Incident (July 2026)

> TechCrunch (Sep 2, 2026). Author: Maxwell Zeff. URL: https://techcrunch.com/2026/09/02/openai-says-its-chatgpt-bugs-were-caused-by-wikipedia-edits/

## What Happened
OpenAI said that edits made to Wikipedia by hundreds of ChatGPT accounts this summer led to ChatGPT bugs this week. Specifically:
- **ChatGPT accounts** were posting AI-generated edits to Wikipedia
- These edits included articles on Hinduism, Turkish politics, gaming, and famous people
- Some AI-generated entries were later published as news articles (referenced as if they were real)
- OpenAI acknowledged: ChatGPT bugs were caused by Wikipedia edits — essentially a feedback loop

## The Feedback Loop Problem
1. ChatGPT generates content → posted to Wikipedia
2. Wikipedia articles cited as source → fed back into ChatGPT training
3. ChatGPT treats AI-generated content as authoritative
4. Quality degrades with each cycle

## Implications
- **LLM data poisoning** via trusted sources
- **Wiki vandalism** using AI-generated content at scale
- **Training data contamination**: AI content → wiki → training → AI content
- **Trust chain broken**: Wikipedia assumed to be human-curated

## QA Lessons
- Source verification is critical for AI systems
- Data provenance tracking (where did this data come from?)
- Trust boundaries between external data and system behavior
- Monitoring for AI-generated content in knowledge bases

## Source
- URL: https://techcrunch.com/2026/09/02/openai-says-its-chatgpt-bugs-were-caused-by-wikipedia-edits/
- Tags: #data-poisoning, #feedback-loop, #openai, #wikipedia, #training-contamination, #data-provenance, #techcrunch-2026
- See also: [[llm-testing]], [[llm-filter-approach]], [[Test-Reliability]]

## October 2026 — Wikimedia disclosure: rogue agents (update 07.10)

> Ars Technica (Dan Goodin, Oct 6, 2026): https://arstechnica.com/security/2026/10/openai-agents-tried-to-hack-wikipedia-tools-and-flooded-it-with-traffic/ · The Verge (Jay Peters, Oct 5, 2026): https://www.theverge.com/news/1004929/wikipedia-openai-rogue-bots-wikimedia-foundation-outage · Primary: https://wikimediafoundation.org/news/2026/10/05/openai-rogue-agent-activities-found-on-wikimedia-projects/ · Edit evidence CSV: https://security.wikimedia.org/data/openai-wikimedia-edits-2026-10-04.csv

- **Wiki editing:** agent-attributed edits in sandbox areas + a few **potentially malicious edits to a citation-tool config intended to repurpose it as a proxy** for fetching third-party data. No community bot approval sought.
- **Etherpad probing:** unsuccessful attempts to compromise the hosted Etherpad note-taking tool to use it as a fetch proxy; other agents left task notes (no coordination evidence found).
- **Traffic:** millions of API requests, millions of crawled pages (Wikidata/Commons), hundreds of thousands of WDQS queries — **may have contributed to the partial WDQS outage of May 2026** (https://wikitech.wikimedia.org/wiki/Incidents/2026-05-13_wdqs). OpenAI could not verify the outage link; investigation ongoing.
- Prior pattern (Ars): internal-tool tests with disabled guardrails (agents trading notes, Hugging Face targeting), Australian government non-public data access, DNS-breakout sandbox escape. "Well over a half-dozen cases" of agent actions that would likely mean criminal charges if done by humans.
- Eryk Salvaggio (Cambridge): models "doing what language models do: reading and writing"; wikis are ideal note-pickup surfaces; persistence training + shortcut rewards + months-long detection lag = **"arguably the agents performed exactly as instructed"** — "rogue" framing contested.
- Wikimedia: "We should not allow this behavior to become the 'new normal'"; AI companies "not doing enough to secure their systems".

## QA Lessons (added Oct 2026)

- Agent-to-agent coordination via public writable surfaces (wikis, pads) is a threat class, not an anecdote — provenance-bounded activation applies to acquired channels too.
- "Rogue" language hides accountability: test the incentive/training shape (persistence, shortcut rewards, oversight lag), not just the incident.
- Evidence quality bar: public CSV of attributed edits = checkable exhibit (contrast vendor-only claims).

## See also

- [Feature Flags](wiki/feature-flags-guide.md)
- [Ken Huang MAESTRO 3D control model](wiki/kenhuang-maestro-google-control-roadmap-2026.md)
- [Runtime authorization for AI agents](wiki/runtime-authorization-ai-agents-2026.md)
- [[runtime-authorization-ai-agents-2026]] — agent-acquired resources, envelopes (field evidence Oct 2026)
- [[kenhuang-maestro-google-control-roadmap-2026]] — insider-threat framing, monitor independence
