# NotebookLM Playbook — Agent Navigation File

> **Purpose for the agent.** This file is your routing index for any user task that mentions documents, sources, research, study, content production, knowledge bases or AI-assistant building. Match the user's intent to a Use Case, return the ready prompt, the source-type guidance and the expected output. Do not generate freeform answers when a Use Case applies — use the Use Case template.

---

## How to use this file

1. **Read the user's task.** Identify what they want to *produce* (knowledge base, course, report, SOP, content, etc.).
2. **Match intent → Use Case** with the index below.
3. **Confirm source types** with the user if not obvious.
4. **Return the paste-ready prompt** for that Use Case.
5. **Suggest the right Studio output or export format.**
6. **Recommend verification prompts** before the user trusts the result.

---

## Intent → Use Case routing table

| User's intent | Use Case | Section |
|---|---|---|
| "Build a knowledge base / wiki / encyclopedia from my sources" | UC1 | Knowledge Base |
| "Turn my materials into a course / training program" | UC2 | Course |
| "Write a long-form guide / deep dive / explainer" | UC3 | Guide |
| "Compare / extract / build a research table" | UC4 | Research Matrix |
| "Do a literature review / compare academic papers" | UC5 | Literature Review |
| "Study for an exam / make flashcards / quiz me" | UC6 | Study System |
| "Repurpose this YouTube video / podcast / transcript" | UC7 | Content Repurposing |
| "Build an SOP / operations manual" | UC8 | SOP |
| "Process meeting notes / extract action items" | UC9 | Meetings |
| "Build a consulting report / client deliverable" | UC10 | Client Work |
| "Build a content engine / extract hooks and angles" | UC11 | Content Engine |
| "Create a slide deck from these sources" | UC12 | Slide Deck |
| "Make an audio briefing / podcast-style overview" | UC13 | Audio Overview |
| "Visualise this / mind map / infographic" | UC14 | Visual Thinking |
| "Audit my sources for quality / credibility / contradictions" | UC15 | Source Audit |
| "Project spans multiple notebooks / massive corpus" | UC16 | Multi-Notebook |
| "Pair NotebookLM with Gemini for longer prompts" | UC17 | Gemini Pairing |
| "Build a knowledge file for a Custom GPT / Claude Project" | UC18 | AI Assistant File |
| "Outline a book / ebook / long-form work" | UC19 | Book Architecture |
| "Personal knowledge management / weekly synthesis" | UC20 | PKM |
| "Iterative project where notes become sources" | UC21 | Compounding |
| "Make a notebook to share publicly / with clients" | UC22 | Public Notebook |
| "Native report / export to Docs" | UC23 | Reports |
| "Run a very long instruction set" | UC24 | Long-Prompt (Gemini) |
| "Use NotebookLM on mobile" | UC25 | Mobile |
| "Organise / label sources in a large notebook" | UC26 | Source Labels |
| "Run the extraction prompt stack" | UC27 | Extraction Stack |

---

## Quick decision rules for the agent

- **If user has < 5 sources** → likely UC1, UC3 or UC7
- **If user mentions "exam / study / learn"** → UC6
- **If user mentions "client / customer / business proposal"** → UC10
- **If user has academic PDFs** → UC5
- **If user mentions "team / SOP / regulation"** → UC8
- **If task contains code / verification / contradictions** → run UC15 first
- **If project is bigger than one notebook** → UC16
- **If user wants AI to "do it all in one shot"** → push back, recommend the 5-step extraction stack from UC27

---

## Universal pre-flight checklist

Before any Use Case, confirm with the user:

- [ ] Sources are uploaded and curated (no junk, no duplicates)
- [ ] Specialist terminology — glossary uploaded as Source 1
- [ ] Long PDFs — chunked by theme
- [ ] Final output format clear (Docs / Sheets / PPTX / PDF / Markdown / MP3)
- [ ] Verification level required (claim audit, source coverage, contradiction check)

---

## Use Case Library

### UC1 — Knowledge Base

**When.** User wants a reusable knowledge asset that can later become a guide, course, manual, playbook or AI assistant file.

**Best sources.** PDFs, Google Docs, web pages, YouTube/audio transcripts, ePub, Markdown, Slides, Sheets, CSV, pasted notes.

**Prompt:**

```
Act as an Expert Knowledge Architect.

Create a complete knowledge base from the selected sources.

Work in this order:

1. Create a source inventory.
2. Extract key ideas, definitions, frameworks, processes, examples, warnings, tools and gaps.
3. Create a master theme map.
4. Create a concept map.
5. Create a framework map.
6. Create a process map.
7. Identify contradictions and missing information.
8. Build a modular knowledge base.
9. Add checklists, templates, prompts and practical exercises.
10. Finish with a source coverage and claim audit.

Be comprehensive. Do not invent unsupported examples. Mark gaps clearly.
```

**Output.** Structured knowledge base with modules, definitions, frameworks, checklists.

**Advanced.** Save inventory, framework map and module outline as Notes. Convert each into a Source. Rebuild final asset using the Note-Sources as structure.

---

### UC2 — Course

**When.** User wants a full course blueprint with modules, lessons, exercises, assessments.

**Best sources.** Training manuals, YouTube tutorials, lecture notes, PDFs, ePub, Slides, process docs.

**Prompt:**

```
Act as an Expert Curriculum Designer.

Turn the selected sources into a complete course.

Include:

1. Course title
2. Course promise
3. Target learner
4. Beginner, intermediate and advanced tracks
5. Module structure
6. Lesson titles
7. Learning outcomes
8. Exercises
9. Assessments
10. Final project
11. Common mistakes
12. Required templates or worksheets
13. Suggested study schedule

Use only the selected sources.
Mark gaps where the sources do not provide enough material.
```

**Output.** Course blueprint.

**Extensions.** Student workbook, instructor guide, slide deck outline, quiz bank, rubric, per-module audio overview.

---

### UC3 — Long-Form Guide / Deep Dive

**When.** User wants a serious written piece — essay, article, ebook chapter, technical explainer.

**Best sources.** PDFs, ePub, articles, transcripts, reports, Docs, web pages.

**Step 1 — architecture prompt:**

```
Act as a Senior Technical Writer.

Create a long-form guide from the selected sources.

First produce:

1. Working title
2. Thesis
3. Target reader
4. Section-by-section outline
5. Main argument of each section
6. Supporting sources for each section
7. Contradictions or tensions to address
8. Gaps that need a second pass

Do not write the full guide yet.
First create the architecture.
```

**Step 2 — write section by section:**

```
Write Section 1 only.

Use the agreed outline.
Use only the selected sources.

Include:
- clear explanation
- source-backed claims
- examples
- warnings
- practical steps
- gaps
- section summary
```

---

### UC4 — Research Matrix / Data Table

**When.** User wants a structured table: claim/evidence, competitor comparison, glossary, tool library, contradiction map, framework library.

**Best sources.** PDFs, papers, reports, spreadsheets, CSV, web pages, technical docs.

**Prompt:**

```
Create a Data Table from all selected sources.

Use these columns:

1. Item
2. Category
3. Definition or description
4. Source-backed evidence
5. Practical implication
6. Example
7. Limitation or warning
8. Related concept
9. Confidence level
10. Gap or missing information

Rules:
- Only include information supported by the selected sources.
- Merge exact duplicates.
- Preserve different framings where they add nuance.
- Mark inferred points clearly.
- Leave a cell blank if the source does not provide the information.
```

**Output.** Data Table for export to Sheets.

---

### UC5 — Literature Review

**When.** User wants thematic clusters, methodology comparison, gap analysis, research questions.

**Best sources.** Academic PDFs, journal articles, research datasets, methodology papers.

**Prompt:**

```
Act as a post-doctoral researcher.

Conduct a literature review of the selected papers.

Include:

1. Major thematic clusters
2. Consensus view in each cluster
3. Dissenting papers or opposing findings
4. Methodologies used
5. Methodological weaknesses
6. Key evidence
7. Research gaps
8. Suggested research questions
9. Literature review outline

Use source-backed claims only.
Mark inferred synthesis clearly.
```

**Warning to user.** NotebookLM is not a citation manager. Pair with Zotero.

---

### UC6 — Active Learning / Exam Prep

**When.** User wants study guides, flashcards, quizzes, Socratic tutor, revision plans.

**Best sources.** Lecture slides, textbook PDFs, past exam papers, notes, YouTube lectures.

**Socratic tutor prompt:**

```
Act as a strict Socratic tutor.

Test me on the selected sources one question at a time.

Rules:
- Ask one question.
- Wait for my answer.
- Grade my answer against the sources.
- Explain what I got right.
- Explain what I missed.
- Give a hint before giving the full answer.
- Track my weak areas.
- At the end, create a revision plan based on my mistakes.
```

**Three-level question prompt:**

```
Create three levels of questions from the selected sources:

1. Beginner recall questions
2. Intermediate application questions
3. Expert-level exam questions that expose shallow understanding

Include answers, explanation and source support.
```

---

### UC7 — Content Repurposing (YouTube / Podcast / Transcript)

**When.** User wants to turn one long video or podcast into multi-format content.

**Best sources.** YouTube URLs, podcast transcripts, audio files, pasted transcripts.

**Prompt:**

```
Analyse this transcript.

Extract:

1. Core thesis
2. Key ideas
3. Frameworks
4. Examples
5. Stories
6. Warnings
7. Strong quotes
8. Content hooks
9. Contrarian angles
10. Practical takeaways

Then turn the strongest ideas into:
- one newsletter outline
- one X thread
- one LinkedIn post
- one short-form video script
- one infographic prompt
```

---

### UC8 — SOP / Operations Manual

**When.** User wants a formal Standard Operating Procedure from messy operational material.

**Best sources.** Meeting transcripts, call recordings, voice notes, policy docs, internal manuals.

**Prompt:**

```
Turn the selected source material into a formal Standard Operating Procedure.

Use this structure:

1. SOP title
2. Purpose
3. When to use this SOP
4. Owner
5. Required tools
6. Required inputs
7. Step-by-step process
8. Quality standard
9. Common failure points
10. Troubleshooting
11. Escalation rules
12. Final checklist

Do not invent missing steps.
If a step is unclear, mark it as a gap.
```

---

### UC9 — Meetings / Calls / Voice Notes

**When.** User wants summary, decisions, action items, risks, follow-up from a conversation.

**Best sources.** Audio files, Zoom transcripts, call transcripts, voice notes.

**Prompt:**

```
Analyse this meeting transcript.

Provide:

1. 3-sentence executive summary
2. Key decisions made
3. Action item table with owner and deadline
4. Risks raised
5. Open questions
6. Dependencies
7. Follow-up email draft
8. Project brief update

If the transcript does not clearly assign an owner or deadline, mark it as unclear.
```

---

### UC10 — Client / Consulting Deliverable

**When.** User wants audit report, strategy memo, proposal, presentation, implementation plan.

**Best sources.** Discovery calls, questionnaires, sales pages, analytics exports, competitor URLs.

**Rule.** One notebook per client. Never mix.

**Prompt:**

```
Act as a Strategy Consultant.

Review the selected client materials.

Create an audit report with:

1. Client context
2. Stated goals
3. Current strategy
4. Main problems
5. Blind spots
6. Contradictions in the client's own material
7. Opportunities
8. Recommended implementation roadmap
9. Risks
10. Next steps

Use specific source-backed evidence.
Do not invent client facts.
```

---

### UC11 — Content Engine

**When.** Creator wants a research vault for articles, newsletters, posts, hooks, visuals.

**Best sources.** Articles, YouTube transcripts, books, voice memos, competitor content, analytics CSVs.

**Prompt:**

```
Act as a Content Strategist.

Review the selected sources and create a content engine.

Extract:

1. Strongest ideas
2. Best hooks
3. Contrarian angles
4. Examples and stories
5. Useful frameworks
6. Common mistakes
7. Audience pain points
8. Content angles
9. Newsletter ideas
10. X/Twitter thread ideas
11. LinkedIn post ideas
12. Visual infographic concepts

Preserve source accuracy.
Avoid generic content.
```

---

### UC12 — Slide Deck

**When.** User wants a presentation outline / storyboard / deck.

**Critical rule.** Build the outline in Chat first. Verify claims. Then generate the slide deck.

**Step 1 — outline in Chat:**

```
Create a source-backed slide deck outline.

For each slide include:

1. Slide title
2. Core message
3. Source-backed bullet points
4. Supporting source name
5. Any numbers or claims requiring manual verification
6. Suggested visual
7. Speaker note

Do not create the slide deck yet.
First produce the verified outline.
```

**Step 2 — revision prompt (after deck is generated):**

```
Revise the slide deck for clarity and presentation quality.

Only revise:
- wording
- layout
- visual hierarchy
- slide flow
- audience clarity

Do not introduce new factual claims.
Do not add new statistics.
Do not change numerical claims unless I provide the corrected numbers manually.
```

---

### UC13 — Audio Overview / Podcast

**When.** User wants a customised audio briefing.

**Custom format examples (Debate):**

```
Format this Audio Overview as a Debate.

Focus only on the failure modes of the methodology in the selected sources.

Host A should defend the methodology.
Host B should act as a sceptic and ask practical questions.

Do not summarise the whole notebook.
Focus on:
- risks
- limitations
- trade-offs
- implementation mistakes
- how to avoid failure
```

**Other formats:** brief, deep dive, critique, beginner explainer, expert briefing.

---

### UC14 — Visual Thinking

**When.** User wants a mind map, infographic concept, process diagram.

**Prompt:**

```
Review the selected sources.

Create a visual thinking map with:

1. Central concept
2. Main branches
3. Sub-branches
4. Dependencies
5. Sequence of ideas
6. Contradictions or tensions
7. Suggested diagram formats
8. Suggested infographic structure

Output as Markdown.
```

---

### UC15 — Source Audit

**When.** User needs to assess credibility, freshness, usefulness or contradictions before synthesis.

**Run this before any heavy synthesis.**

**Prompt:**

```
Conduct a rigorous Source Audit.

Create a table with:

1. Source name
2. Source type
3. Publication date if available
4. Author or organisation if available
5. Core thesis
6. Usefulness rating
7. Potential bias or weakness
8. What this source is best used for
9. Whether it should be kept, removed or used cautiously

Then identify any contradictions between sources.
```

---

### UC16 — Multi-Notebook / Large Project

**When.** Project exceeds one notebook (PhD, book, enterprise KB).

**Bridge Summary prompt:**

```
Create a Bridge Summary for this notebook.

The summary must represent the most important knowledge from all selected sources.

Include:

1. Core topic
2. Main themes
3. Key frameworks
4. Important evidence
5. Contradictions
6. Gaps
7. Useful examples
8. Recommended next-step questions
9. Source list

This Bridge Summary will be exported into an external knowledge base.
Make it dense and portable.
```

**External pairing.** Zotero (papers) + Obsidian/Notion (permanent KB) + Gemini (orchestration).

---

### UC17 — NotebookLM + Gemini Pipeline

**When.** Source-grounded extraction in NotebookLM, then long-prompt expansion in Gemini.

**Hand-off prompt for Gemini:**

```
You are working from a NotebookLM extraction.

Your job is to turn the extracted source-grounded material into a final knowledge asset.

Rules:
- Do not restart extraction.
- Do not invent unsupported claims.
- Separate source-backed material, synthesis and inference.
- Preserve all high-signal frameworks, examples, tactics and warnings.
- Structure the output as a practical playbook.

Build:
1. Executive overview
2. Core mental model
3. Feature-to-outcome map
4. Use-case library
5. Prompt library
6. Source-type strategy
7. Verification system
8. Recommended notebook architectures
9. Final knowledge asset pipeline
10. Final audit
```

---

### UC18 — AI Assistant Knowledge File

**When.** User wants a Markdown/JSON file for a Custom GPT, Claude Project or similar.

**Best sources.** SOPs, expert transcripts, manuals, frameworks, examples, style guides.

**Prompt:**

```
Create an AI Assistant Knowledge File from the selected sources.

Include:

1. Assistant role
2. Domain overview
3. Target user
4. Key terminology
5. Core principles
6. Frameworks
7. Workflows
8. Decision rules
9. Examples
10. Mistakes to avoid
11. Answer style guidance
12. Boundaries
13. Uncertainty rules
14. Required output formats

Write in clean Markdown.
Make it suitable for uploading into a Custom GPT or Claude Project.
```

---

### UC19 — Book / Ebook Architecture

**When.** Author wants chapter map, evidence allocation, gaps, workbook material.

**Prompt:**

```
Act as a Senior Editor.

Use the selected sources to create a book architecture.

Include:

1. Book title options
2. Core thesis
3. Target reader
4. Chapter-by-chapter outline
5. Main argument of each chapter
6. Supporting source material
7. Examples to include
8. Gaps in the source material
9. Exercises or workbook ideas
10. Promotional content angles
```

---

### UC20 — Personal Knowledge Management

**When.** User wants weekly synthesis from articles, notes, voice memos.

**Prompt:**

```
Review everything I uploaded this week.

Create a Weekly Synthesis with:

1. Main themes
2. Unexpected connections
3. Useful ideas
4. Action items
5. Questions to explore next
6. Content ideas
7. Personal lessons
8. Sources worth keeping
9. Sources to delete or archive
```

**Rule.** Export weekly to Obsidian. NotebookLM is not the long-term store.

---

### UC21 — Notes-to-Sources Compounding

**When.** Building a large asset in stages.

**Build-stage prompt:**

```
We are building this knowledge asset in stages.

Use the selected sources and the saved notes.

Task:
1. Review the saved notes that have been converted into sources.
2. Treat those note-sources as the agreed structure.
3. Use the original sources only to fill in detail, examples and verification.
4. Do not restart the project.
5. Build the next section of the final asset in Markdown.

Before writing, list:
- which note-sources you are using as structure
- which original sources you are using for detail
- any gaps that still remain
```

**Pre-conversion audit:**

```
Audit this note before I convert it into a source.

Check:

1. Is it source-backed?
2. Does it contain unsupported inference?
3. Does it contain duplicated ideas?
4. Does it contain weak or vague claims?
5. Should anything be removed before this becomes part of the notebook's knowledge base?
```

---

### UC22 — Public / Client / Audience Notebook

**When.** User wants to share a notebook publicly or with clients.

**Pre-publication audit:**

```
Prepare this notebook for public or client-facing use.

Audit the notebook and tell me:

1. Which sources are safe to share
2. Which sources may contain sensitive/private information
3. Which artefacts should be generated for viewers
4. What FAQ questions users are likely to ask
5. What should be hidden, removed or rewritten
6. What opening instructions should appear for users
```

---

### UC23 — Native Reports / Docs Export

**When.** User wants a written output inside NotebookLM and clean export.

**Prompt:**

```
Create a report from the selected sources.

The report should include:

1. Executive summary
2. Key concepts
3. Frameworks
4. Practical workflows
5. Examples
6. Warnings and mistakes
7. Actionable checklist
8. Gaps and unsupported areas
9. Recommended next steps

Keep it practical and structured.
Mark inferred points clearly.
```

---

### UC24 — Long-Prompt via Gemini

**When.** Instruction set is too long for NotebookLM Chat. Use Gemini as the controller. Same handoff prompt as UC17.

---

### UC25 — Mobile

**When.** User captures sources on phone for later desktop processing.

**Prompt:**

```
Review the sources I added on mobile today.

Create a short capture digest:

1. What each source is about
2. Why it might be useful
3. Which sources are worth keeping
4. Which sources should be deleted
5. What deeper desktop workflow I should run next
```

---

### UC26 — Source Labels / Organisation

**When.** Notebook has too many sources; user wants categorisation.

**Prompt:**

```
Help me organise this notebook.

Review all sources and suggest source labels.

Use categories such as:
- foundational
- practical
- advanced
- examples
- case studies
- weak or low-signal
- needs verification
- useful for final output

Then recommend the order I should process these source groups.
```

---

### UC27 — Full Extraction Prompt Stack

**When.** User wants a controlled extraction pipeline. Run these in sequence in Chat.

**Step 1 — source inventory:**

```
Create a complete inventory of all selected sources.

For each source include:
- source name
- source type
- main topic
- core thesis
- key ideas
- frameworks
- processes
- examples
- warnings
- usefulness rating
- extraction priority

Do not synthesise yet.
Only inventory the sources.
```

**Step 2 — source-by-source extraction:**

```
Extract the high-signal knowledge from each selected source.

For each source extract:
- definitions
- key ideas
- frameworks
- processes
- tactics
- examples
- warnings
- tools
- templates
- gaps

Do not turn this into a guide yet.
Only extract.
```

**Step 3 — cross-source synthesis:**

```
Now synthesise the extracted material.

Create:
- master theme map
- concept map
- framework map
- process map
- contradiction map
- gap map
- potential module structure

Do not write the final guide yet.
```

**Step 4 — knowledge base build:**

```
Build the final knowledge base from the extraction and synthesis.

Structure it as:

1. Executive overview
2. Big picture explanation
3. Core principles
4. Key definitions
5. Framework map
6. Process map
7. Modular course structure
8. Practical playbook
9. Checklist library
10. Templates and prompts
11. Final audit

Make it beginner-friendly but expert-level.
Do not invent unsupported examples.
Mark gaps clearly.
```

**Step 5 — final audit:**

```
Audit the final knowledge base.

Check:

1. Did every source get used?
2. Which sources were underused?
3. Which claims are source-backed?
4. Which claims are inferred?
5. Which sections are too shallow?
6. Which examples are missing?
7. Which parts need a second pass?
8. What should be expanded next?
```

---

## Extraction Sub-Prompts (callable individually)

### Key ideas

```
Review all selected sources.

Extract the most important key ideas.

For each idea include:
- idea name
- simple explanation
- deeper explanation
- why it matters
- example if available
- related source
- practical use
```

### Frameworks

```
Identify every named framework, model, structure or mental model in the selected sources.

For each one include:
- name
- purpose
- components
- how it works
- when to use it
- when not to use it
- example
- limitations
```

### Definitions / glossary

```
Create a glossary from the selected sources.

For each term include:
- term
- simple definition
- detailed definition
- source context
- related terms
- common misunderstanding
```

### Processes

```
Identify every process, workflow or step-by-step method in the selected sources.

For each process include:
- process name
- goal
- inputs
- steps
- expected output
- failure points
- quality standard
```

### Warnings / mistakes

```
Extract every warning, mistake, risk and failure mode mentioned in the selected sources.

For each include:
- mistake
- why it happens
- consequence
- how to avoid it
- better approach
```

### Examples / case studies

```
Extract all examples, stories, case studies and analogies from the selected sources.

For each include:
- example
- what it illustrates
- why it matters
- how it generalises
- where it belongs in a guide or course
```

---

## Synthesis Sub-Prompts

### Theme map

```
Synthesise the selected sources into a master theme map.

For each theme include:
- theme name
- explanation
- supporting ideas
- related sources
- contradictions
- practical implications
```

### Concept map

```
Create a hierarchical concept map.

Use this structure:
- central topic
- primary concepts
- secondary concepts
- supporting details
- dependencies
- related examples
```

### Framework map

```
Create a master framework map from the selected sources.

For each framework include:
- name
- purpose
- components
- use case
- related frameworks
- lesson or module where it belongs
```

### Course structure

```
Turn the selected sources into a modular course structure.

Include:
- course title
- course promise
- target learner
- modules
- lessons
- exercises
- assessments
- final project
```

---

## Verification Sub-Prompts

### Unsupported-claims check

```
Review your previous answer.

Identify any claim that is:
- unsupported
- inferred
- speculative
- stronger than the source allows
- generic filler

Then suggest corrected wording.
```

### Source coverage audit

```
Audit source coverage.

Create a table with:

1. Source name
2. Was it used?
3. Main ideas extracted
4. Important ideas missed
5. Usefulness rating
6. Should it be kept, removed or reprocessed?
```

### Claim audit

```
Audit the previous output.

Create a table with these columns:

1. Claim
2. Source-backed or inferred
3. Supporting source
4. Confidence level
5. Verification needed
6. Keep, soften or remove
7. Suggested corrected wording

Be strict.
Flag anything that sounds stronger than the source material supports.
```

### Contradiction audit

```
Identify contradictions across the selected sources.

For each contradiction include:

1. The disputed point
2. Source A position
3. Source B position
4. Possible explanation
5. How this should be presented in the final output
6. Whether the contradiction is fatal, important or minor
```

---

## Studio Output Sub-Prompts

### Debate format

```
Format this as a professional debate.

Host A should defend the main methodology in the sources.
Host B should act as a sceptic.

Focus on:
- strengths
- weaknesses
- risks
- implementation problems
- practical trade-offs

Do not summarise the whole notebook.
```

### Beginner explainer

```
Explain the selected sources as if teaching a smart beginner.

Use simple analogies.
Avoid jargon unless you define it.
Focus on the core ideas, why they matter and how to apply them.
```

### Expert briefing

```
Format this as a concise expert briefing.

Skip generic introductions.

Focus on:
- strategic implications
- risks
- important numbers
- trade-offs
- decisions the listener needs to make
```

---

## Output Creation Sub-Prompts

### SOP from messy material

```
Turn the selected source material into a formal SOP.

Include:

1. Purpose
2. Tools required
3. Inputs
4. Step-by-step execution
5. Quality checks
6. Common failure points
7. Troubleshooting
8. Escalation rules
9. Final checklist

Do not invent missing steps.
```

### Practical checklist

```
Turn the methodology in the selected source into a practical checklist.

The checklist should be:
- sequential
- specific
- beginner-friendly
- useful in real execution
- separated into preparation, execution and review
```

### Newsletter

```
Turn the core framework from the selected source into a newsletter.

Include:

1. Strong hook
2. Problem
3. Framework
4. Example
5. Practical takeaway
6. Closing line

Avoid generic AI style.
Preserve source accuracy.
```

### AI assistant file

```
Extract the decision-making logic from the selected sources into a Markdown AI assistant file.

Include:
- role
- scope
- terminology
- principles
- rules
- workflows
- examples
- output format
- uncertainty handling
```

---

## Source-Type Strategy (for the agent to recommend)

| Source type | Best for |
|---|---|
| PDFs / academic papers | UC1, UC3, UC4, UC5 |
| YouTube transcripts | UC7, UC11 |
| Podcast / call transcripts | UC7, UC9 |
| Google Docs / pasted text | UC1, UC8, UC10 |
| Web pages | UC11, UC15 |
| Audio files | UC9, UC13 |
| CSV / Sheets | UC4 |
| Slides | UC2, UC12 |
| Screenshots / images | UC14 |

---

## Notebook Architecture (for the agent to recommend)

| User type | Architecture |
|---|---|
| Casual learner | One "everything" notebook |
| Student | One notebook per class / module / exam |
| Researcher | One notebook per research theme |
| Creator | One vault per content pillar |
| Business | One notebook per client / department / workflow |
| Power user | Multi-notebook + Zotero + Obsidian + Gemini |

---

## Master Workflow (run this for any serious project)

```
1. Define outcome (format, audience, depth, verification level)
2. Choose notebook architecture
3. Prepare sources (curate, rename, chunk, glossary)
4. Run source inventory (UC27 step 1)
5. Extract knowledge (UC27 step 2)
6. Synthesise (UC27 step 3)
7. Build the asset (relevant UC prompt)
8. Verify (claim audit + source coverage + contradiction)
9. Export (Docs / Sheets / PPTX / PDF / Markdown / MP3)
10. Repurpose (one asset → many)
11. Archive externally
```

---

## Anti-Patterns the Agent Must Flag

- "Summarise everything" — push back, offer UC27 step 1 instead.
- Generating Studio outputs before extraction — push back, run Chat first.
- Mixing client data in one notebook — push back, recommend per-client notebooks.
- Treating NotebookLM as permanent storage — recommend export to Obsidian/Notion.
- Skipping verification — always offer claim audit before user trusts output.
- Asking for "viral content" — push back, extract structure first (UC11).
- Building a slide deck in one shot — split into outline (Chat) + generation (Studio).
- Using NotebookLM as a citation manager — recommend Zotero pairing.
- Loading every source for every Studio output — recommend source selection for relevance.

---

## When to Push Back to External Tools

- **Long-form generation** beyond NotebookLM context limits → Gemini
- **Custom GPT / Claude Project deployment** → export Markdown knowledge file
- **Citation management** → Zotero
- **Permanent knowledge base** → Obsidian / Notion
- **Code execution / heavy automation** → Claude Code / external scripts
- **Cross-notebook orchestration** → Gemini orchestrating multiple Bridge Summaries

---

## Final Audit Checklist (always offer to user)

- [ ] Every source appeared in the output
- [ ] No single source dominated
- [ ] Duplicates merged, nuanced differences preserved
- [ ] Contradictions handled explicitly
- [ ] Gaps visible
- [ ] Examples are real (not invented)
- [ ] Inferences labelled separately from source-backed claims
- [ ] Useful for both beginner and expert
- [ ] Export format ready (clean Markdown / Docs / Sheets / PPTX)
- [ ] Numerical claims manually verified

---

**End of agent navigation file.**
