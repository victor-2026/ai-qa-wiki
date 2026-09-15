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
