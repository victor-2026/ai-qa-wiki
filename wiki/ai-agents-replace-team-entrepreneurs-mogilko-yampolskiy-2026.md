# AI Agents Replace Team Roles: The 35-Agent Startup Model

**Source:** Mogilko, Marina. "AI Safety Expert: No One Is Ready for What's Coming in 2 Years | Roman Yampolskiy." *Silicon Valley Girl: AI, Tech and Career Growth*, 20 Apr. 2026, 44 min. https://www.youtube.com/watch?v=00RHph_eok4
**Raw:** [mogilko-yampolskiy-35-ai-employees-2026.md](../raw/mogilko-yampolskiy-35-ai-employees-2026.md)
**Date ingested:** 2026-08-30

---

## Key Thesis

Roman Yampolskiy (AI safety researcher, University of Louisville, 15 years) says one person can now do the work of 35 people using AI agents — and it costs nothing. The 35 roles: lawyer, accountant, designer, developer, assistant, researcher, and their full teams.

Marina Mogilko (founder, 35-person team) counters: if 35 agents drive 2x revenue, the move is to hire more humans and get to 5x. AI agents multiply the team, they don't replace it.

## Three Structural Advantages (Mogilko)

1. **Tools got cheap.** What used to take a team and a budget, one person does with AI.
2. **Networks cannot be copied.** Your audience, their trust, the habit of returning — AI doesn't produce this. (Twitter sold for $44B on the network, not the code.)
3. **First mover with a network wins.** Once you become "the one" in your niche, even a competitor with a better product cannot push you out.

## Yampolskiy's AI Safety Context

- Coined "AI safety" in 2010. Published 100+ papers on AI dangers.
- Prediction: AGI by 2028–2030 (prediction markets collapsed from 2045).
- 28% drop in CS co-op placements at his department in 2026.
- 99% of jobs will be automated — "not 10% unemployment which is scary, but 99%."
- Five jobs that survive: those where humans prefer human interaction (nurse, nanny, psychologist, personal accountant, creative roles).
- We cannot control superintelligence — "like creating a perpetual safety machine, it's impossible."

## Key Quotes from the Transcript

### On job automation (113-136s)
> "It's not about can AI do 20% of your job. It's can AI do 80% of your job and fire 4 out of 5 people on your team."
>
> "The question is, what's the trend? And if you look at the trend, it goes very fast in the direction of AI doing more and more. What was impossible two years ago is trivial today. What's impossible today will be trivial in two years."

### On tools vs superintelligence (831-863s)
> "You're using word AI to mean completely different things. You're referring to narrow tool you're using right now to summarize your email and you're also kind of using it as future super intelligence smarter than all of us combined. Not the same technology."
>
> "AI tools, narrow AI is awesome. I use it all the time. We should have more of it. We can use it to solve real problems like pajama day. But if we create general super intelligence, we don't understand it, we cannot predict it, we cannot control it."

### On the 35-agent startup (628-637s)
> "If you have a team 35 people right now, I can have 35 agents working for me for free. A lawyer, an accountant, Lego designer, web designer. That's an opportunity we never had before."

### On networks vs code (2587-2614s)
> "To write code to do something like what Twitter does is trivial. But people end up buying it for 40 billion instead of just coding it up. Cuz what you have is the network. You have people, all the relationship that you cannot automate."

### On investment in scarcity (1695-1728s)
> "Invest in something AI cannot make more of. So, if AI can just produce more of it, that's probably going to go down in value."
>
> "Bitcoin, it doesn't matter what the price is. It's exactly the same supply."

### On the cognitive gap (886-905s)
> "Think someone with IQ of a million. We have no concept for that... The cognitive gap is something like humans versus squirrels. Squirrels have no concept of what we're doing, how we can harm them, traps, poisons, none of it makes sense to them."

### On regulation (2489-2505s)
> "Problem is every year it gets cheaper and cheaper to train very powerful models. So if today you need a trillion dollars, next year it's a billion. At some point you can do it on a laptop. And at that point you can't stop all the psychopaths in the world."

### On personal brand (1937-1959s)
> "There is, but you have to do it pretty quickly. You have to become somewhat recognizable before AI is better than you and you are competing now as a nobody with something better."
>
> "As soon as we switch to human level or above... I see people say 2027, 2028, 2030. All of those numbers have been suggested by people who are not insane."

## What Are "Networks" That Cannot Be Copied?

Mogilko's context: Twitter sold for $44B not because of the code (anyone can build a microblogging platform) but because of the network — 400M users, their trust, their daily habit of checking the feed. No clone could replicate that, even with a better product.

For QA engineers, the "network" is **institutional knowledge that compounds over time**:

### Personal network (your career moat)
- **Reputation with devs** — they trust your bug reports because you've been right before
- **Codebase intuition** — you know which modules break on Fridays, which APIs are fragile, where the real risks hide
- **Relationships** — you can walk to a dev and say "this will break in prod" and they listen, because you've proven it 50 times

### Team network (your QA infrastructure)
- **Test knowledge base** — wiki pages, learned patterns JSON, mutation matrix, AGENTS.md rules — accumulated over months of iteration
- **CI/CD integration** — your tests run on every PR, your regression-advice script posts checklists, your GitHub Actions pipeline catches regressions before they ship
- **Institutional memory** — why this test exists, why that assertion was added, why this module needs retries

### Why AI tools can't copy this
- A vendor (QAEverest, testRigor, Autonoma) can give you generic AI tests — but they can't know your specific codebase risks
- A competitor can buy the same AI agent — but they can't copy your 6 months of learned patterns
- Open-source tools commoditize the *generation* of tests — but the *curation* of what matters is your network

**The paradox:** AI makes test generation cheap (Mogilko's insight #1). But the knowledge of *what to test* and *why* is the network that compounds. The QA engineer who builds this network first wins — even if a competitor deploys the same AI tools later.

## Implications for QA Engineering

| Transcript insight | QA application |
|---|---|
| "80% of your job, fire 4 out of 5" | QA lead evaluates: which 80% of manual testing can AI handle? Which 20% requires human judgment? |
| Tools vs superintelligence | Narrow AI = awesome QA tool (mutation testing, coverage, regression advice). Superintelligence = existential risk. Don't confuse them. |
| AI agents multiply the team | QA lead deploys 5-10 specialized agents (API audit, POM generation, regression, mutation, coverage) instead of hiring 5 QAs |
| Networks cannot be copied | Test knowledge bases (wiki, patterns, learned patterns JSON, CI/CD integration, dev relationships) are the irreplicable network — vendor tools can't copy your institutional QA knowledge |
| First mover wins | Teams that adopt AI-assisted testing now build institutional knowledge that late adopters cannot replicate — same pattern as Zalando's "agentic engineering snapshot" (risk-based PR approval, CCN inflection) |
| Invest in scarcity | QA's scarcity = codebase intuition + dev trust + institutional memory. These compound; AI tools commoditize. |
| "Recognizable before AI replaces you" | QA engineer who builds LinkedIn brand + published articles + recognized expertise in AI-QA niche = career moat before AI commoditizes generic testing |
| "Something AI cannot make more of" | Personal reputation = finite supply. Institutional QA knowledge = finite supply. These are QA's Bitcoin. |

## Practical Steps (from the episode)

- Build a team of 2–3 AI agents for narrow tasks: copy, research, design, finance, calendar.
- Pick one platform for recognition (LinkedIn, YouTube, newsletter).
- Invest in scarcity (network, brand, relationships) — not in tools (they commoditize).

## Cross-links

- Yampolskiy interviews: [Joe Rogan #2345](https://podscripts.co/podcasts/the-joe-rogan-experience/2345-roman-yampolskiy), [Lex Fridman #431](https://podscripts.co/podcasts/lex-fridman-podcast/431-roman-yampolskiy-dangers-of-superintelligent-ai), [Diary of a CEO](https://podscripts.co/podcasts/the-diary-of-a-ceo-with-steven-bartlett/roman-yampolskiy-these-are-the-only-5-jobs-that-will-remain-in-2030-proof-were-living-in-a-simulation), [Know Thyself E191](https://podscripts.co/podcasts/know-thyself/e191-roman-yampolskiy-the-man-who-proved-we-cant-control-ai-and-what-that-means-for-humanity)
- Related wiki: [andrew-ng-loop-engineering-2026.md](andrew-ng-loop-engineering-2026.md) (3 nested loops, developer-as-QA)
- Related wiki: [krivitsky-agentic-factory-nested-loops-2026.md](krivitsky-agentic-factory-nested-loops-2026.md) (coding/feature/impact loops)
- QA evidence layer: [ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md](ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md)
