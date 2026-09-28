# Transcript: When DDD Met AI - Rinat Abdullin, KanDDDinsky 2025
# Video: https://www.youtube.com/watch?v=mdB6KbBeOjc
# Track: English auto-generated, 1386 segments, ~8450 words, ~50 min. Fetched 2026-09-28 via youtube-transcript-api.
# NOTE: auto-transcript, names and terms may be mistranscribed.
# One segment per line below.
# ---
[applause]
>> Hey.
Okay, I'll do it Denzel Washington
style. So, I'll start the timer.
Although, in his movies he's finishing
like in 50 seconds, I'll try to not to
overflow 50 minutes.
So,
let's get started. Uh I'm Rinat Abdulin.
I'm technical advisor helping teams to
ship LM driven products faster. I'm also
head of AI and innovation at Austrian
Time Tag Group.
Uh and I've been with DDD for quite some
time and
you might have known me from the DDD
summits uh which I had the pleasure to
be uh participating and invited from the
being the worst podcast. I contributed
the chapter on event sourcing to Vaughn
Vernon's uh domain driven design book.
Uh I was the author of Lokad CQRS which
was an old framework that allowed to
build uh CQRS event driven systems that
can run both locally and in the cloud.
But, that's a long story but
and one of the other things that we've
done uh was CQRS beers community.
It was a fun thing.
Uh people would come to a city and
they'd say, "Hey, who wants to talk CQRS
and event sourcing?" Because back then
CQRS and event sourcing were not popular
enough.
And especially with the connection to
domain driven design.
Uh and people would come, chat, have a
friendly conversation over a beverage of
their choice,
uh get connect and spread the knowledge.
And today I want to do the same. I
haven't been in the DDD community for a
very long time and it's awesome to be
back. And uh in the past years, even
though I wasn't actually participating
in the DDD, I was focusing on the AI and
machine learning,
DDD was a very valuable part of the
inventory.
Uh and in the talk this morning, Eric
Evans has talked about how DDD is used
and can be used to build an AI products,
systems that are composed of their
components which plug into the business
process and that are driven by large
language models.
Today I want to show you a couple of
stories where it shows that it is
impossible to build really cool and
really valuable systems without them.
Uh and I'll tell a couple of stories and
you had a lunch. Uh this is like
Securitas building. So just relax, sit
down and hear to a few stories. No
worries in taking notes for example
because the slides, all the links you'll
have them at the end of the
presentation.
So no rush.
Uh
but any story requires getting an
introduction. So when I'm talking that
I'm giving you the best three stories
that I had over the course of the last
half a year, what does it mean that
they're best? What does it make an AI
project peculiar uh compared to the
rest? It's like what does the map look
like?
Uh and uh
the map of the territory upon which I'm
basing my uh
foundation uh is essentially an amazing
community uh that is worldwide now that
has been doing the research.
Uh it is all focused around the
AI strategy and research hub around the
time type group Austria, but it spans
teams and companies in Europe and United
States.
Uh and within that community we have
been observing what businesses,
startups, because startups are fast uh
have been already using to how they have
been building products, products that
deliver value. Some of them succeed,
some of them fail. Uh this map shows uh
successful
AI cases in different industries and in
different application areas that have
been successful, meaning that they
didn't fail and they didn't result in a
hey, LLMs are hallucinating story.
These are the things that actually
worked out and you can already see that
there are some patterns like uh sales,
marketing, operations, and maybe
knowledge management parts of the
companies, they have seen more success
with adoption or at least that are
registered on our radars. Uh
manufacturing and business services are
the industries that see the most
adoption.
Most successful adoption. There are tons
of failures, but we're not counting for
them in the statistics.
Uh and in the community, uh
I'm not going to focus as much. There is
a process that is called AI case
mapping. It would be similar to the
outsourcing, but it relates to
identifying customer problems and
mapping them to AI cases. And we've been
doing that for a long time. We had uh
research on LLM fundamentals. What makes
large language models hallucinate in the
business cases? How can these be applied
to building practical cases that are fit
for the enterprise or the startups?
Uh what are the patterns and practices
that were extracted by systematically
looking at the cases of different AI
applications in the industries? Uh we
even have courses on that, but that's
not the topic. The topic is that if you
look at the whole area of the stuff that
works out for businesses and startups,
uh there are three large types of the
cases that you can uh broadly
categorize.
One of them, and this is my favorite one
because it has highest return on
investment,
it's data extraction at scale.
Data extraction at scale is simple uh
and it's also interplays with the
concept that Eric Adamson was previously
mentioning like a component.
And an example be a company has to
handle a lot of invoices. A company has
to handle a lot of incoming purchase
orders and there might be humans that
are sitting down and looking at the
PDFs, tens of thousands of PDFs per
month, and mapping them to the internal
systems or extracting the information,
especially in Europe because there's so
much paperwork these days.
Uh and large language models, especially
modern visual large language models,
they're extremely good in extracting all
sorts of information.
And this is the book kind of project
that it brings a lot of value very fast
because it saves a lot of hours of human
lives and it gives
pretty big feedback, uh big results.
Another one, uh broad category of
projects and products, it's AI search or
AI assistant or a chatbot uh or a rec
system. This is what is most popular and
common because everybody is talking
about the chatbot, especially failures
from the chatbots.
Yes, of course there are failures. Uh
there are
very public failures, but uh there is
also under this noise and
uh
hype, there is also a trend that
companies are actually sometimes
building things that are being used
internally to help connect uh silos of
information, to help connect services
and systems and teams. And this is the
second successful pattern.
And the third category, which I've seen
uh only in a couple of companies that
were the first to start, it's when a
company has tried to adopt AI to build
the products that automate new business
processes that were impossible to
automate efficiently before, uh they see
that it works and they want to start
rolling out. But when you start rolling
out the technology in different places,
you see the pattern that hey, we have
this dependency here and here and here.
So we want to track LLM usage, maybe we
want to host it locally, maybe we want
to host uh different models, different
versions at constraint decoding on the
top, and they start building AI
platforms.
So these are the three broad categories
of the cases which are common in the
industry, in the enterprises and
startups, and we're not going to talk
about them. Just put them on the map.
What we're going to take talk about
things that deviate from the successful
patterns.
And the first story is a story of 400
euro per hour.
Uh
so basically the Europe
is quite good in a couple of things.
Uh one of them is regulations. Like we
like to regulate things because so that
companies and countries can work
together.
Uh and regulations in Europe are known
for being
full of paperwork. And the way it works
is that uh for instance a European
financial regulator decides to say that
the banks should hold take care of the
money. And they will write a lot of
papers on this topic. Human-readable
papers.
And then the country, like for example
Austria or Deutschland, they will write
their own implementation of this
paperwork saying, "Yes, uh companies in
Deutschland have to take care of money."
And then any bank that operates in
Deutschland, it will have to write their
own policy saying, "Yes, we're going to
fulfill this clause of the regulation
this way. We're doing this and this and
this and that." Because if we don't do
that, then we're going to get fined, uh
then we're going to fail audits, then
we're going to make mistakes that will
cost us a license. So, the large
companies, this is very, very critical.
And
this regulation changes. So, the
European regulation can figure out that
there is something that else needs to be
regulated, and it will uh issue new new
papers, it will go to local policies,
and then somebody will have to translate
that to company procedures. And that
person or teams or large companies that
are responsible for taking papers for uh
updates of the documents on the left
side and bring them to the right side,
they charge a lot of money. And 400
euros per hour is not that much,
actually. Uh there was a company that
was uh making sure that banks can handle
uh crypto payments, and they were
saying, "Yes, we have a set of papers,
set of templates, uh and it costs you
200 Yeah, 20,000 euros."
So, not so much.
Uh and the documents, as you can see,
like this is example of uh one of the
ComplyTech compliance documents. These
are just PDFs with lots of lots of lots
of text.
And the documents themselves are
frequently in different form because
they are done by different companies, uh
different countries. Uh and this one is
very fun because it's also actually an
image of the text under the hood. And
the if you try to kind of extract it uh
the usual way, it will not extract very
well because there is a text and there
is citation and interpretability.
And then there was a question,
uh is it possible to build an LLM system
that can kind of take some of the
workload of these really expensive
experts?
Is it possible to build a system that
essentially looks at pile documents,
which exist within its own regulatory
model uh
domain, uh and then find differences uh
from the company documents, which is
also a pile of documents, free text,
zero structure, uh and it uh follows
different campaign company domain model?
The fun fact is that you can always test
this hypothesis by feeding it to the
most powerful reasoning model. In our
case, back then it was ChatGPT 01 Pro.
And if you just upload a couple of
documents and you ask the question, is
there a gap? It will find a couple of
gaps.
But if you try to uh
ask it to find more gaps, it will
probably find the same gaps. And the gap
is actually something that is missing in
the company document that has to be
present or the company will be fined.
So, you see, we were in this situation
where this project is theoretically
doable.
ChatGPT can do this occasionally,
sometimes, but not everything.
Uh
and a human can do this completely.
So, can we kind of build a project that
does that?
Uh and as always [snorts] in the times
of doubt, uh we ask ourselves, what
would Eric Evans do?
And actually, as it turns out,
domain-driven design has already
equipped us with all the methodology
that is needed to make a project like
this happen.
Uh if you remember, in domain-driven
design we talk about how we can pay
attention to the languages, to the
boundaries, to the context, to how
things are phrased and named and
mentioned, communicated in organization.
And how like just to pay attention, and
then if you pay attention enough, you
can transfer that to the code, and the
code will be durable. It will be more
robust because it reflects reality.
And
this reality looks like this.
But this is actually
this one.
So, the idea was that
>> [sighs]
>> when we're looking at the
process that can be automated to uh by a
large language model, we sometimes don't
have to deal with an organization.
Because there is not such such thing as
an organization. There is a single
expert that sits down, that takes paper,
that takes cards,
that starts analyzing these documents,
that maybe makes a mess, and this mess
is called actual zettelkasten, which is
opposes thinking from the mess, but
still.
Essentially, the expert does the
research.
And the idea that we've discovered, if
you
take what domain driven design does the
best, paying attention to boundaries, to
words, to the processes and information
flows, but in this case, you apply it
not to an organization, but to thinking
process of a single expert, how he is
juggling the information, how he working
with the papers, uh then there is a
chance to repeat it first on the papers,
like the good old days, and if it's
doable on the papers, it might be
transformable to large language models.
And the idea was uh and actually the
trick to solving this impossible project
was to actually
do it once, and that was the painful
part, uh because for engineers, they
don't like going into the domain maybe,
and don't like working with the paper.
But if you just do it once on paper, by
uh copy-pasting uh references from the
documents, by doing essentially
research,
and then translate that to LM driven
process, it was possible to get it done.
Uh and this is how essentially the
system was implemented. There weren't
that many prompts.
So, it was kind of chat GPT research
process. Uh deep research, but on the
documents and following very precise uh
regime. We pass the documents, we make
the settle custom or we make indexes, we
make references. We essentially annotate
each piece of the text, each clause with
relations. We build kind of graph.
Uh and this graph is like node of the
graphs are
classified according to the domain model
with which we're annotating. This is the
same classification that Eric Evans was
talking on the first talk.
Like you build a domain model ontology,
categorization, and then you use that to
describe different pieces of text
with a way that is specific to this
research.
And then you just go for the company
requirements or European requirements uh
taking one requirement at a time and
saying, "Hey chat GPT or like LM API,
whatever you're using. Let's do a deep
research and let's figure out prove me
if this requirement is fulfilled in a
company documents." And it means that it
has to go through uh find all relevant
passages in the company documents, see
if they're related, double check, do a
review, and then do a summary on the
clean context.
But the trick part here is that if you
put all this sequence of steps in the
prompt,
then it will not work reliably because
more steps that the model has to go
through you put in the prompt, more
complex they are, higher is the chance
that on the complex edge cases where the
model is working operating at its
cognitive capacity, uh it will start
hallucinating like left and back.
And we wanted the domain process to be
precise. And that's where we discovered
a thing called schema guided reasoning
where you can use constraint decoding
and it's
uh supported by pretty much all the open
AI like vendors. And constrained
decoding is essentially thing that tells
you, "Hey, ChatGPT, give me a response,
but the response has to fit exactly
schema."
So, it has to be this JSON, and the
fields has to be done in certain uh
order. And the amazing part is that when
you're telling
ChatGPT or any other large language
model uh in which order to fill the
fields,
uh
it will not fill them blindly. It will
just write a text. And [snorts] what by
doing that, we're making sure that when
it's, for example, writing something, it
will pay attention to the things that it
was forced to write before. So, in
essence, we're taking like a checklist.
We can encode [snorts] the checklist. Do
that. Pay attention to that. Pay
attention to that. And only then uh
provide me an answer. Think.
But not just
think step-by-step, but think about
this, this, and this. So, essentially,
we can take the mental process of an
expert that goes through the mental
checklist before answering a question
sometimes, or at best. And then we can
force large language model to do that
every time out of 10,000 times, 20,000
times, 100,000 times. They don't care.
They don't get tired.
Uh and this was actually the solution.
Uh and the best part uh is that this
process is transparent. Although we
cannot look deeply inside the black box,
that's what Eric Evans was talking about
in the first session, uh but we can
still understand how it is thinking
because we can uh plot all the clauses,
for example, in the documents which the
model considered and which it decided to
pull, for example, in for the final
generation, and we can plot them. We can
see how it was going through that. We
can review them. We can say, "Okay, it
uh so, it looked at this clause and
considered to be worthy. So, the
classifier was good. But it somehow
discarded this clause even though it was
relevant. So, it means that we have back
to the classification stage and tune
this part. So, it's all transparent and
it's the best part if you just take this
process, if you write it out like a
result of the research,
and then you show this research to a
expert who is native in this. He
understands that he'll be able to
pinpoint, he'll be able to add review
saying, "No, this research is not good
because it's missing a couple of pages."
And this is something that engineers can
actually take to back to the large
language model and
they can incorporate into the prompt
structure, into the schema-guided
reasoning structure, or the information
flow.
So, it all ties very neatly.
Uh and
I'll have links to the schema-guided
reasoning, but basically how this is
This is how it looks like. We can just
force a model to go exactly for the step
of the processes. We can enforce
classifications. Like if we have an
anthology for
1,000 of different categories.
A year ago, it would be impossible to
encode precisely. Now, OpenAI because it
listens to the practitioners, OpenAI
said that you can enforce anthology up
to 10,000 items in a single literal.
Essentially forcing large language
model, for example, to pick to pick
somewhere between an item of a category
out of 10. So, there are so many amazing
things that you can do there. You can
inside a single prompt, you can pack
routers, you can pack decision makers,
you can pretty much pack a execution
program or a
mental checklist that is branching, that
is repeating, that is cycling. And this
mental checklist will be uploaded to the
OpenAI servers in a single prompt and it
will be executed there, going through
all the predefined paths before
returning you an answer. It's amazing
technology.
Uh but basically the idea was that
domain-driven design made this possible
because it showed that if you pay
attention to the words, to the
boundaries, to the process, to the
information flows,
it
uh, be used to build better software.
But, in this case, we're just paying
attention to what happens inside head of
a domain expert,
replicating it in papers, and then
transferring this paper-based, uh,
workflow into the large language models.
Another story will be about 30-year-old
code.
Yeah. You know, we, uh, always hear that
the legacy code is bad. It's like 10
years old, 20 years old,
uh, and it's Java, nobody wants to
maintain.
It gets even more fun than, uh, when the
code is vintage.
Uh, and Europe, Europe in general is
very good at, uh, building vintage code
because we have businesses that have
been running around for decades. And
when they started, uh, showing up, they
started automating their workflows using
the technologies that were available at
the time. Mainframes, like IBM
mainframes, uh, OpenEdge, uh, Progress
mainframes, and God knows what.
And the worst part is that it made them
money.
It helped run the business.
Uh, it allowed to essentially encode
business decisions into that.
And it kind of fossilized year after
year, year after year, year after year.
Uh, and these days, actually, the
problem is that the people who started
writing this language and who would know
this codebase, they're going into the
retirement.
And new kids, they like Java, they like
TypeScript, maybe C#, Python. They don't
want to tackle Progress or some other
fourth fourth generation language
because it's not bringing any business.
And the companies, like they have to do
something because this monolith, nobody
will be able to maintain it. And we have
searched so many stories where
enterprises are trying to take this old
code, rewrite it completely to a new
code, while also adding beautiful UI,
like Angular or React on top of that,
and it fails horribly.
It's not interesting.
Uh, but the The is that it's currently
possible
thanks to the advances of the couple of
last years to automate big deal of that
rewrite. Why? Because old language, old
code, it has requirements, it has text
and the new language, it has
requirements in different form. Like
language on one side, language on the
other side. Even if it's huge, like for
example in that case we're working
through studying code base that is
500,000 lines of code.
A ton of screens, ton of tables and
we're not talking modern tables, like
SQL tables. These were the databases
that were operated on files.
And these files were essentially binary
structure. You could parse it yourself
and do you had locks, which are not
modern locks, but legacy locks. And the
column names, they used to be like five
letters, usually five very cryptic
letters.
It's very fun and especially in Europe,
where we have companies which are
multi-multinational, but they usually
start from one country. And usually the
system will be written in that country.
I like mostly Polish start, things that
started in Poland and then went for
example to Germany. It's such a horrible
and interesting mess.
So, and what can we do? Wipe coding
obviously doesn't
going to work here because wipe coding
has one requirement, you don't think too
much when you write the code. So, and we
had to think.
And once again, if you look the at the
problem long enough, it kind of starts
bring patterns. So, we have a pile of
code, which is old and it's following
the old domain model. Old languages, old
requirements. And there is a pile of new
code that you want to write and it will
follow a new domain model, new
architecture.
And the fun thing is that if you like
take a couple of old files
it doesn't really matter in which
language it is written and you ask
ChatGPT or on or something like that,
Hey, can you port me this to nice Kotlin
or nice Pascal?
Uh it will be able to suddenly make
sense out of that, especially with a
helpful hint. So, you see the pattern?
It is the same pattern as in the first
story.
So, we have two sets of knowledges. We
have to translate between them.
Like two kind of talk on two contexts or
large context. They have different
domain models, different languages even.
And the best reasoning model can do some
parts of that.
So, once again, what would Eric Evans
do? What would Greg Young do? What would
Alberto Brandolini do?
Just think like the best.
And what we've learned is that in this
case
we have to think like an expert that is
looking into the code
and that is translating them, the best
of them.
And we can look at how the expert would
look at one code, analyze that, and
transfer it maybe to the new code.
Analyze the thinking process, the
cognitive process.
And the important part is actually the
code is irrelevant because we're going
to throw it out anyway because large
language models can rewrite the code.
The requirements are the matter.
And which means that test, specs, and
requirements are essentially the thing.
And we've learned that already in the
past projects at Time to Act that if you
have good requirements, if you have
excellent tests, then you can actually
throw the entire back end away, write it
on a completely new stack, deploy it,
and nobody will ever notice if your
tests are good.
So, the tests are the most valuable
part. And obviously with the old
mainframe code, like 30 years old, 20
years old, there are zero codes, zero
tests.
Cuz it just works. Why should we test?
Uh so, given that, here was the things
that you knew.
It's unfeasible to read 500,000 lines of
code for every change.
But when you're actually changing
something, you need to pay attention to
pretty much all this code because you
never know where is this database
trigger leading to. And obviously old
systems, they didn't have relations,
they didn't have indexes, they had
database triggers. And database triggers
were programs that could execute
whenever there was a file change. And
these triggers could trigger other
triggers. And unless unless you look
carefully enough, you'd never know where
this cascade could end.
But what we knew, that LLMs can
theoretically do that because a one pro
can understand that. It's just too
expensive to do it all the time.
And we know that domain-driven design
can help us to distill the process and
the personas.
We just have to look carefully in the
heads of the experts. And we know that
whenever we have a process,
schema-guided reasoning can enforce it
so that it's repeatable and analyzable
and tunable. We can optimize it.
And we know that no automated system is
ideal. So, the humans will still have to
oversee. About the edge cases, they have
to control things on the side.
And this resulted in a concept that
we're calling AI code factory.
And AI code factory is essentially a
where humans are working with AI. In
that case, the responsibility of human
would be, for example, provided that
we're able to build that system, to
write the factory. Like
an example of factory would be the thing
that Marco was showing yesterday when
building a game.
It's a code factory still. It's a set of
processes, rules, prompts, and
methodologies, maybe tests, architecture
and guidelines that makes it easy for
LLM coding agents to write code to
deliver features.
And humans just set things up. And the
responsibility of AI-driven assistance
in this case was to write tests and
code.
And in this case, why do we say that we
it wrote 200% of tests, 200% of code?
Because when you have AI, economics
change.
>> [snorts]
>> They change dramatically. You can do
things that would be unthoughtenable for
the humans. Humans would hate you for
that. But here we just said, "Okay, why
not write in Python and Kotlin in
parallel? Because Python is so much
easier to understand and Kotlin is the
enterprise end.
And the
tests in this case these were
event-driven specs.
They're translatable fairly easily. So
we can maintain two code bases. So we're
done it twice.
Humans would hate maintaining multiple
code bases in parallel just because it
makes slightly readable and better
development experience.
Here it works.
And this is just an example of the spec
that was carefully written by AI. It's
an event-driven spec. It works very nice
for the console applications. But the
idea is if you cover your system
or if you get let AI
do the work of discovering requirements,
translating them to really accurate
tests, and making the tests are
accessible to the AI-driven agents,
then you can carefully specify behavior
of a service. You can specify edge
cases. You can capture regressions. It's
an own process.
And then it means that when you don't
care about the code, you can just group
tests or specs maybe in a clusters that
make more sense because they belong to
the same context. And then you can say,
"Hey dear AI, I don't care what that
you're it is end of the work week and it
is night and it's party night. Go ahead
and start rewriting the entire code so
that the tests in this new system will
pass and I'll go party." It will do
that.
Or better, you can just run 10 agents in
parallel saying, "Please do that and
actually I'll throw the work of nine
agents out. I'll just pick the one that
I like the most."
You can do that because value of people
is more valuable than
the cost of running large language
model, especially the efficient one.
And essentially the process, the mental
process that one could embed in this AI
code factory, it's the same. It's the
same as in a any normal systematic
AI-driven development where you ask for
example for every change to analyze
analyze the code, identify the gaps, and
we talked about identifying gaps in the
first story. And then here you are chat
GPT or prompt or SGR whatever, please
write me a detailed migration plan that
will just write a huge document that
will focus on migrating that tiny
feature from the old code base to the
new code base. And while writing that,
please make sure that you capture all
the each cases, you capture all the
nuances, and you also capture
requirements and tests.
And then once you have captured tests,
and you have failing unit tests, so
that's test driven development the way
it should have been. Yeah, I can write
the code. And at the point we have code
and passing unit tests, we can run them,
exercise the test infrastructure, we can
run code linting, we can run any types
of quality checks. And this is amazing
because humans are usually don't like
writing the code that complies with the
linters. They don't like writing code
that adheres to abstract guidelines.
AI agents, they don't care.
And actually if you change your
requirements or
code style halfway,
nobody will grumble because you can just
say, "Hey, now start working file by
file and write the code so that all
variables are now descriptive."
And you just repeat the loop and it
actually works.
And on a high level, this can be
represented as code factory. Once again,
I'm flipping through that. You'll have
it in slides. There will be a link.
If you want to learn more about that, so
once again, don't worry about taking the
photos. It will be in the slides, but
there is a safe shift service offered by
the time to act.
At post added. But the idea was that DDD
essentially unlocked this project. When
we were starting, we didn't know that it
was possible. We didn't know that how it
was feasible. And now it's actually
intuitive and simple. Just do what good
developers would do. Take attention on
how they're approaching, how they're
thinking, and code that in a process,
and let uh boring large language models
run it thousands and thousands of times.
And here's the last story, and I think
we're pretty much good on time. This is
the story of Hail Mary project, because
normal projects without time pressure
are not fun enough.
Uh and the context of that, we're
getting back uh to the data sheet
extraction or uh data extraction.
Uh this domain is power components. Uh
here is uh the data sheet for a Chinese
company which used to be on American
market,
and they have power components. And the
power components are these circuits
which can be plugged into a train, for
example, to uh MRI machine or even
plugged into the laptop to transform
between two different types of
electricity. That's the domain model.
Uh and these components are specified in
PDFs. These PDFs and data sheets,
they're very peculiar. This is not plain
text.
These are tables, these are charts, and
sometimes a mixture of both.
And uh
the idea is that we, at some point, want
to be able to take these PDFs.
Uh and these PDFs, actually, like each
PDF is unique. It will have a different
structure. It will have different
layout. It will have different pages.
You cannot build a parser for that. Uh
and the PDF will use different
terminology and different nuances.
They'll have different measurements.
Uh
but, in ideal world, somebody would want
to extract that to a single domain
model, which is a structured
representation of all the components of
any company that is producing that.
Because once we have normalized all
these different
uh components into a single domain model
that speaks the same language, then we
can compare. Then we can analyze. Then
we can see what uh subset of components
are serving which population, and is it
profitable or not profitable. How is it
working? How is it not working? And we
have to do it many, many times, because
inventory of a single company maybe
10,000 components, 20,000 components.
The fun part the same stuff and you
probably can see the pattern already.
Chat GPT Pro can do that. You just
upload the PDF, ask to do it and it will
do it. Most of the time it will do it.
Uh most of the time it will be stable.
But the thing is it is very expensive
and you cannot just tell it, "Hey, pay
attention to that, to that, to that."
because every time the reasoning
workflow will take a different path.
So,
uh we additionally had additional
constraints because this was a very
interesting project. So, a classical
solution would uh require like would be
a pipeline of large language model steps
uh that takes a couple of days just to
finish running this extraction, 20,000
components. And it would cost something
like 350 euros uh in OpenAI costs.
Uh and the accuracy without too much
tuning, it would be 60% out of the box.
But can we do better?
So, uh at a strategy hub research
strategy research hub uh of time track
Austria, we wanted to see if it's
possible to make it better, to make it
in shorter terms.
So, what do we know?
We know what uh Eric Evans thinks about
the domain-driven design. We know what
people uh think about LLMs and testing
and we also know that tests matter.
Uh that we uh can enforce uh reasoning
in the schema-guided reasoning.
And we can just take a look at how would
a human expert look at this PDFs and do
the boring job of writing the components
in a nice Excel spreadsheet.
Uh or in this case we had because we had
one week of time allocated to that for
this uh
we didn't have time to do that. We want
to some have some automation. So, we
wanted to model the thinking process of
a lazy DevOps person without time. And
DevOps are very amazing. I'm engineer.
I'm not a DevOps and I've found DevOps
approaches that are amazing because they
can just take scripts. They can do
horrible [snorts] things, but it will
make the Kubernetes cluster run. They
can instead of building a normal
program, they can assemble something out
of bash, awk, perl, grep, and it will
get the job done. It will be stable.
Like this is amazing. And we wanted to
try to capture that.
So, and that now is the story. It's 6
days, and because I'm telling you
on a conference, so it's probably end up
all right, but it was tense. And it
happened
like a month ago or something like that.
So, first day, real people, real
company. So, what do we do?
So, we wasted 1 day out of 6 days trying
to figure out what to do, and we decided
that we're going to gather test data in
Excel because Excel is ambiguous, and
it's it can be a shared file. So, we
just created an Excel sheet, and people
started building these tests. And the
test is essentially one test is one row,
and within that one row, the first
column was name of the PDF file. The
second
column was name of the component, and
there were 60 other columns, different
properties, like input voltage, output
voltage,
input voltage on the pin one, etc., etc.
And by the end of the second day,
people that were gathering tests, they
were grumbling because actually it is
very boring and painful work.
It takes a human
maybe 2 hours just to extract five
components into the Excel spreadsheet to
look through the PDFs.
And it was also extremely valuable
because it was showing up the capability
and the thinking process. The capability
meaning that if we were able to take
this mundane work and automate, that's
how much money and human time and sanity
we're going to save.
And it was also showing how people were
looking at different parts of the pages
in this process.
And in parallel, the engineering team
built unit tests, and these unit tests
were failing.
Obviously, because there was no test
data.
Uh but, the shape of this unit test is
peculiar. It's an error map or heat map.
Essentially, it shows
uh
a set of Excel sheets, Excel cells, and
it shows the delta. So, each row is a
document.
Each
column is one Excel cell or Excel
column. And whenever this is working,
then
it would the columns or the cells would
show green if the actual results are
matching the expected results. They
would show red if they're not matching.
And actually, on the third day, we
started getting some results from the
pipeline.
The pipeline was broken, the tests were
missing, but we started seeing the
results. And the accuracy was horrible.
46%.
But, the important part, we closed the
feedback loop.
Setting up the ability to test a system,
evaluate the system,
uh it allows to split process into two.
Because you can have eval team
or quality control team or product team
start working on the
tests. And this is the most valuable
part of the work. Because on based on
how you shape the tests, you're
essentially are enforcing requirements
on the pipeline.
Uh and essentially, this project was
saved by the wonderful eval team.
Uh I was the lucky one. Uh I got to play
with the engineering stuff.
So, uh my job was in the remaining 3
days try to get this chart
larger and to get it all green or as
much green as possible. Uh we had a goal
of uh having more than 80% of accuracy.
So, before, it's already 62% accuracy.
Why is that possible? Because when you
have a tight eval loop, then you can
just start running crazy experiments,
and you just tune something, and you see
the result in 15 minutes. Tune something
else, 15 minutes. And we can try crazy
theories. And this is essentially takes
the art away from the building element
drone system, it brings the engineering.
Because we try something, we tune one
knob, gets better, okay, we accept it.
Gets worse, we discard it.
And that's how it was working. And also
the value of the heat maps like that,
we're calling them strategic error maps,
is that you can everybody can
instinctively understand what the hell
is going on.
Because you can see the gray column
vertical, like the document wasn't even
processed by the pipeline. There was a
big problem. If it is the column is not
gray, then it means that we're
extracting this.
But if there is like a large chunk of
the red, it means that this set of
properties in the related documents, in
related entities was misclassified or
misextracted, whatever.
And humans can instinctively see the
patterns. They will see like, okay, this
property is being extracted incorrectly
all across the documents. So it usually
means that the domain model that is
embedded in this extraction process is
wrong or it is in a misaligned with the
real model.
And if we have large chunks of verticals
that are red, it means that we're not
handling some of the document well,
maybe because once again the domain
model, the way the
data was captured in this document is
too different because this is a Chinese
document and they were doing something
else.
But we had the pipeline loop and we just
experimented experimented experimented
by day five we had 82.4% accuracy.
But the amazing part is that was not a
real data set.
This was a test set. Like in any good
engineering system, we asked the vault
team, "Hey, please find us the worst
possible cases. Like the worst, the most
messed up documents, the most weird
cases. Like find find us things that
would break the pipeline."
And the vault team eventually called
this red teaming because their objective
when we were playing a game. Uh their
objective was to add as much reds on
this chart as possible.
And the job of the engineering team was
obviously to turn as much reds into
greens as possible.
The result of that?
When customer did their own evaluation
on their own data set, which didn't
didn't consist of the worst cases, they
had 99.7% accuracy.
So, that was pretty good. And that was
day six. And essentially the project,
which felt like it was impossible in the
beginning,
was completed in the end.
Yeah, and that's a fun thing.
This entire project, this six days,
starting from the beginning, starting
from the experiments, you can actually
see. That was day one, two, three,
weekend, and then the final extraction.
It was just $26
to extract 30,000 entities,
which is pretty nice.
Uh and along the way we actually,
because we're experimenting under the
protection of tests, we discovered a
pretty unusual architecture. In In
essence, we ended up with a pipeline
where there is an agent, and it's
writing a tool,
coding a tool, uh for every new step of
the pipeline. And then it's coding that
tool, it's uh writing this code.
To do full extraction, we had 100,000
lines of code. No human has ever saw
that code.
And may I made sure that I didn't look
there myself. Why? Because it wouldn't
make a nice story if I tell that uh
humans could see that code.
Uh no human will ever need to maintain
that code. Nobody cares about code
quality. Why? Because we have 99.7%
accuracy on the final tests.
Nobody cares how it's done under the
hood. Probably it's reasonable.
And the architecture The architecture is
amazing. Two prompts.
One prompt, it's just a prompt analysis
analysis. Hey, dear ChatGPT,
uh here's a PDF from which you will need
to eventually to extract some stuff. Uh
Uh, please do a meta-analysis of the
component structure of the domain model
according to this process. And SGR
structure that tells in which order to
look at what is applied. And then the
second step, dear ChatGPT, you're lazy.
You don't want to extract 100 documents
or 100 components from a single PDF
because it will not fit in your context.
And for each component you have to have
60 properties. So, just be lazy and
write Python code that will do this
extraction. So, don't extract itself,
write Python code. And then basically we
get this code, we extract it, we run it,
we get the extracted entities. And if
something goes wrong,
uh, if it the code doesn't behave that
well, we'll just pass it back to the
context saying, "Dear ChatGPT, you
messed up. Please fix it."
And initially the model that we're using
was GPT-5 mini.
Why? Because I tried to make it work
with ChatGPT-4o, but it didn't work. So,
we had to do something better. And in
case where the system, like in 5% of the
case where the system failed to write
this tool from the first try, we'd run
it again, but we'd let the reasoning be
high instead of the medium.
And essentially we had two feedback
loops, one for the agent coding itself,
and one for the humans that would
oversee this extraction factory. They
would take a look at the strategic air
map, see what are the biggest red
things, and prioritize the largest
surfaces or largest patterns. And
usually like when the something is red,
it means that there is a mismatch
between the domain model that is
embedded in the prompts in the analysis
and in the PDFs. Dive in, fix, and it
works.
And that was actually additionally
amazing, uh, part of the conversation.
Uh, the idea was that we've trained,
quote, uh, system to handle documents of
three vendors.
Then we added documents from two new
vendors. Every new vendor is completely
different mindset, different people,
different organization, different
templates.
And the system handled them well.
Because we
tuned not for the words that were
captured in the
uh documents, not for the patterns, but
for the underlying physical model.
Because power components is everywhere
the same. Because there are always
voltages. There are always things even
they though they can be named
differently.
Uh and as you can see, like
really domain-driven model,
domain-driven design, domain models, uh
like the chat is huge because 6 days is
a lot of time. And the domain probably
has been used the word domain probably
has been used more than 50 times.
Because it was a valuable thing. It was
one of the things in addition to the
work of the Eval team that made it
possible.
So once again, domain-driven design
unlocked this project. It made it
impossible possible. Uh and here we have
used SGR and reasoning from the story
one.
Uh we have used attention to the domain
model as usually. And we used the test
and coding approach, coding AI approach
from second story.
And probably by the time you see the
pattern here,
like these are blocks. You start with
the domain-driven design, you do
something, you learn, you put the next
block. And then you use lessons from
this block to make the next block. And
you're kind of building foundations of
something new.
Where is heading? We don't know.
But uh it would be awesome together as a
domain-driven design community to figure
this out.
So if you're interested, here's what you
can do next. Like I remember I promised
you the slides, all the links, all the
references. So permalink is here.
Uh there is a links for the SGR and deep
research, LM benchmarks, enterprise rack
challenge, time to act Australia, etc.
Uh this thing.
So uh part of this research was actually
running enterprise challenges, uh which
are fun things in which teams from the
companies, individuals participate. And
uh the results are public, the source
code is
public afterwards, but the
schema-guided reasoning, we didn't
discover it ourselves.
We actually had an Enterprise Challenge
1 and 2 were discovered that.
Uh and people were doing running
experiments, were were putting them
structurally, were systematizing, were
figuring out, were sharing the feedback.
And this was actually the process of
building something better.
So, if you're interested, and this
challenge will be about building agents
that make decisions in the enterprise uh
environment. It's going to be fun.
Uh sign up. And I heard that Greg Young
wrote on Twitter that he's looking
somebody to team up with him on
uh solving the challenge as well.
Uh additional thing
is
to summarize. Actually, no, no
additional things. So, domain-driven
design unlocks enterprise AI.
Just it's attention to the words,
attention to the language, attention to
how people are thinking.
It makes impossible and basically it
fall boils down to a simple thing.
We take any complex project process, we
identify the most boring, most
repeatable part that humans hate to do,
we bring it down to the basics, to the
paperwork, to
putting cards around, and then we just
digitize that.
And we keep this process that is
automated in large language models same
as a paper process, because that when we
can analyze them, we can map them, we
can improve.
Uh and this is possible because of the
community research. And community
research, community energy in the AI
field is amazing. Folks are inventing
new stuff. Like this was invented like
within the last 6 months. And who knows
what else can be invented. If you just
try, experiment, work together. And it
would be so amazing if the domain-driven
design community would be spending more
time trying the stuff, applying this,
sharing feedback, and learning together.
Uh domain-driven design and large
language models and SGR are hard
forever, of course.
Uh, and so there are more stories
together. So,
please
come up. Let's talk. Let's discuss.
Let's see what we can do together. Uh,
hit me up on the streets. Uh, just not
in the behind. I don't like behind. Uh,
and tomorrow on the open eye
open space, we're going to be hosting a
panel on that. So, where we can continue
this conversation.
Let's make DDD and AI great again.
>> [laughter]
>> Thank you.
>> [applause]