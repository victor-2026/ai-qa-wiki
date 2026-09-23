# Qodo: We built a state-of-the-art RAG system for code review. In Qodo 2.4, we took most of it out. (2026-09-23)

**Source:** https://www.qodo.ai/blog/we-built-a-state-of-the-art-rag-system-for-code-review-in-qodo-2-4-we-took-most-of-it-out/
**Context:** Qodo (ex-Codium) = AI code quality & governance platform. TIER 1.5 catalog candidate. Note: FULL READ - RAG removal lesson. Fetched 2026-09-23 with browser UA.

---

A year ago, the smartest thing we could do for code review was index everything. Today the smartest thing we can do is index almost nothing, and remember the right things instead.
I want to walk through how that happened, because the interesting part isn’t the conclusion, but the measurements that forced it, and the fact that we had to delete something we were genuinely proud of to get here. This isn’t a “RAG is dead” post, but something more boring and (hopefully) more useful: retrieval is a tool, the value of a tool changes as everything around it changes, and you have to be willing to put your own best work on the scale and take off the parts that stopped paying for themselves.
Quick definition so nobody’s lost: RAG, retrieval-augmented generation, just means you fetch the relevant context first and hand it to the model before it answers. The whole idea is to find the right stuff, then reason about it.
Where we started: when retrieval really was the answer
When we set out to do code review and codebase Q&A at scale, the core problem was context. A model can only reason about what it can see, and a real repository is way bigger than any context window. Worse, the lines that matter for reviewing one change are scattered all over the place. Things like:
The function you touched
The code that calls it
The test that pins its behavior
The config flag that turns it on
The three other spots where someone copy-pasted the same pattern
So we built what you’d build. We turned the codebase into searchable chunks, stored them, and pulled the most relevant ones into context before the model started reasoning. We wrote about that work at the time, including the genuinely hard part, making it hold up across thousands of repos instead of one tidy demo (
Qodo, RAG for a codebase with 10k repos
).
And it worked. For the moment we were in, this was the right call. Models had small context windows and shaky tool use, so handing them a clean slice of the codebase was the difference between a reviewer that helped and one that guessed. The system was state of the art. The phrase doing the work in that sentence is “for the moment we were in.”
What changed underneath us
Two things shifted, and they fed each other.
First, agents got a lot better at going and looking instead of just answering. Think about how a human actually reviews a pull request. You don’t load the entire repo into your head first. You read the diff, notice it touches a function, grep for everywhere that function is called, open the one file that looks risky, and follow the thread one hop at a time. The main behavioral pattern became an agent with a shell does the same thing: git diff to see what changed, grep to chase a symbol, open the specific file it now knows it needs. This is a documented house style for agent-assisted review now (
agent-assisted code review patterns
), and you can see it spelled out in review skills that run the whole flow through plain git and grep instead of a prebuilt index (
genius-code-review skill
).
Second, context windows got bigger and tool use got reliable enough that fetching on demand is fast and accurate enough to compete. Once a model can be trusted to decide what to read and then actually read it, a lot of what our index used to do quietly moves into the agent’s own loop.
Put those together and the gap RAG existed to fill got narrow. The model could increasingly find the right lines itself, on the changes that mattered, with no index for us to maintain.
The cost nobody puts in the demo
One thing about a retrieval system is that it is not a build you finish. It’s more like a standing bill you pay every single day, in two currencies.
The first is infrastructure. The codebase has to be processed and reprocessed, the search store has to be hosted and scaled, and the re-indexing has to run every time code changes, which in an active repo is basically always. The cost-of-ownership breakdowns for production RAG lay this out plainly across compute, storage, indexing, and upkeep, measured over a real year instead of a launch week (
RAG project costs and TCO
,
RAG development cost breakdown
).
The second currency is engineering attention, and that’s the one that actually stings. Every retrieval system grows a tail of work that never ends. Keep the index fresh. Tune the chunking so you don’t slice a function in half. Handle the repo that’s ten times bigger than you planned for. Debug the review that went weird because retrieval surfaced a stale or near-duplicate chunk. We did real iteration here, including smarter, agent-driven retrieval and multi-repo scaling (
Qodo, agentic RAG explained
). It was good work, but it was also the telltale sign. When you’re spending a real slice of your best engineers’ week keeping one component breathing, that component had better be earning its keep.
Measuring the lift, honestly
This is the part it’s tempting to skip, so I’ll plant the flag on it. We did not pull retrieval because the industry mood shifted. We pulled most of it because we measured what it was actually adding, and the number stopped covering the bill.
So we ran the experiments. Full retrieval stack versus agent-driven, fetch-on-demand, on real changes instead of cherry-picked ones. What we saw matches the wider research on retrieval: the lift from heavy retrieval is often modest, and it shrinks as the model itself gets better at finding context (
experimental study on retrieval-augmented generation
).
For our review workload, the extra lift from the index layer had dropped low enough that, once you set it against the infrastructure and the maintenance, the ROI on that layer was sitting right around zero. It was simply no longer worth it to keep alive.
But cutting it loose feels like throwing all of the hard work away. However, that’s the sunk-cost trap talking. Every hour you’ve already poured in is spent, and you can’t earn it back by spending another one. None of it is a reason to keep paying for lift that isn’t there anymore. It was worth building a year ago and it isn’t worth keeping today, and both of those can be true at once. The only honest question is what it’s worth now.
What we kept: retrieval as memory, not as search
Retrieval is the wrong tool for finding code an agent can fetch itself, and the right tool for remembering things an agent has no way to rediscover from the repo as it stands today.
For example, when a new senior engineer joins your team, they can’t read off your team’s history and the judgment from the repository files. Or find out why a past change was made the awkward way it was; what a reviewer flagged on a similar change three months back. The convention this team enforces that lives in no style guide. None of that is in the working tree. It’s in the pull request history.
So that’s where retrieval moved. In Qodo 2.4, the system acts less like a search index over your source and more like long-term memory over your PR history: past reviews, the decisions behind them, the feedback that keeps repeating, the patterns of what this specific team treats as correct. That’s the same direction a lot of people are landing on, away from broad indexes and toward git- and history-backed memory that’s cheaper to keep and
closer to how teams actually reason
.
The economics flip too. We’re not reprocessing the whole codebase every time someone merges. We’re building a focused, slow-moving memory of review decisions, which is smaller, steadier, and far cheaper to keep current. And it makes the reviews better in a way that raw code retrieval never could, because the agent gets to apply
this team’s
hard-won judgment instead of generic best guesses. That’s the difference between a reviewer who knows your codebase and one who’s seeing it for the first time.
Did it actually get better
All of this only matters if the output improved. Doing less is not interesting on its own.
It did improve. With the leaner footprint and PR-history memory in place, Qodo 2.4 leads on our review benchmarks while carrying a fraction of the indexing infrastructure the old design needed. The full numbers and the methodology live
in our benchmark writeups
, and honestly that’s the part of this I’d want you to poke at hardest, because the architecture call only earns the word “right” if the benchmark backs it up.
What I’d take from this
The lesson isn’t really about RAG. It’s three things.
Measure your own best work against what it competes with today, not what it beat a year ago. The world your system was built for keeps moving, and a component can slide from essential to optional without anyone noticing until you actually look.
Sort everything into “the agent can rediscover this for itself” and “the agent can never know this.” Spend your retrieval on the second pile. Let the agent fetch the first.
And be willing to take out something you’re proud of. We shipped a state-of-the-art RAG system, and the most senior decision we made about it all year was to measure it honestly and then remove most of it. Qodo 2.4 is the better product for it.
