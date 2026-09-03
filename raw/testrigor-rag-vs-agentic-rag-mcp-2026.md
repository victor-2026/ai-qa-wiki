# Source: https://testrigor.com/blog/rag-vs-agentic-rag-vs-mcp/
Fetched: 2026-09-03

---

<div id="content" class="blog" role="main">

<div class="single-top-line-ad">

Turn your manual testers into <span class="text-red">automation experts!</span><a href="/request-trial/" class="btn btn-danger">Request a Demo</a>

</div>

<div class="single-post">

<div class="featured-img trans" style="background-image: url('https://testrigor.com/wp-content/uploads/2026/02/RAG-vs-Agentic-RAG-vs-MCP-Key-Differences-Explained-Title.jpeg'); height: 250px;">

</div>

<div class="post-container-wrapper">

<div class="aside post-column-left">

<div class="sticky-container">

<div class="table-contents-title">

Table of contents:

</div>

</div>

</div>

<div class="post-content">

<div class="header entry-header">

# RAG vs. Agentic RAG vs. MCP: Key Differences Explained

</div>

<div class="post-body">

<table class="author-details">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td class="pr-10"><img src="https://secure.gravatar.com/avatar/f1f08a6f213535245bd24ecf97b2bc8ca4fd3a06c85c9f6aa398663f5370c063?s=96&amp;d=retro&amp;r=g" class="avatar avatar-96 photo" srcset="https://secure.gravatar.com/avatar/f1f08a6f213535245bd24ecf97b2bc8ca4fd3a06c85c9f6aa398663f5370c063?s=96&amp;d=retro&amp;r=g 2x" decoding="async" width="96" height="96" /></td>
<td><div class="entry-author">
Hari Mahesh
</div>
<div id="postDate_1130794" class="entry-date">
&#10;</div></td>
</tr>
</tbody>
</table>

<div class="mb-30 text-center">

- <a href="https://testrigor.com/blog/category/ai-in-software-development/" rel="category tag">AI in Software Development</a>
- <a href="https://testrigor.com/blog/category/generative-ai/" rel="category tag">Generative AI</a>
- <a href="https://testrigor.com/blog/category/software-architecture/" rel="category tag">Software Architecture</a>

</div>

<div class="post-newsletter shadow">

<div>

**Weekly Newsletter**\
Receive weekly testRigor newsletters packed with insights on test automation, codeless testing, and the latest advancements in AI.

</div>

<div>

Subscribe

</div>

<div id="blogHSform">

</div>

</div>

<div id="mobileTableOfContents" class="mb-30">

<div id="mobileNavTitle">

</div>

</div>

Large Language Models (LLMs) have drastically changed the way software systems process information, produce responses, and aid humans in making decisions. But for all their wizardry at reasoning and natural language, LLMs have a fundamental limitation; They do not intrinsically “understand” your data.

All those techniques, including RAG, Agentic-RAG, and Model Context Protocol, are there to address a single, core problem: ***How do we safely, reliably, and intelligently connect LLMs to real, external, constantly changing knowledge?***

<div class="mb-30">

<img src="https://testrigor.com/wp-content/uploads/2026/02/RAG-vs-Agentic-RAG-vs-MCP-Key-Differences-Explained-Title.jpeg" class="shadow" style="width: 100% !important" decoding="async" />

</div>

At first sight, these three ideas seem to be similar. All of them are based on “feeding context” into AI models. But architecturally, philosophically, and operationally, they are three stages of AI system design that really could not be more different from one another.

<div class="table-responsive mb-30">

<table class="table table-bordered">
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th>Key Takeaways:</th>
</tr>
</thead>
<tbody>
<tr>
<td><ul>
<li>RAG grounds LLM responses using retrieved documents, but remains a simple, linear, and non-autonomous architecture.</li>
<li>Agentic RAG adds reasoning, iteration, and tool usage, enabling models to decide what to retrieve and when.</li>
<li>MCP redefines context as governed infrastructure, allowing models to request structured data through secure protocols.</li>
<li>The three approaches represent increasing levels of intelligence, control, and scalability rather than competing solutions.</li>
<li>Mature enterprise AI systems will likely combine MCP for governance, agentic reasoning for autonomy, and RAG, where retrieval adds value.</li>
</ul></td>
</tr>
</tbody>
</table>

</div>

## Why LLMs Need External Knowledge

Before we compare solutions, it is important that we have a clear understanding of the problem at hand. LLMs are modeled on static data and thus lack runtime intelligence about the news, organization or fast-changing facts, leading to outdated, incomplete or overly generic responses when precise current or domain-specific knowledge is required.

Read: [What are LLMs (Large Language Models)?](https://testrigor.com/blog/what-are-llms/)

### The Knowledge Boundary of LLMs

LLMs are trained on static snapshots of data and do not have access to a real-time system unless connected to it. When in doubt, they [hallucinate](https://testrigor.com/blog/ai-hallucinations/) with confidence and don’t have an independent means of checking the objective truth value of their performance. It is not related to the context outside of a window, and they cannot recall or think over large datasets.

Even the most advanced model is blind to your internal documents and unaware of your APIs unless they are explicitly integrated. It remains ignorant of recent updates because its knowledge is not continuously refreshed in real time. By default, it is also incapable of dynamically querying systems or validating information on its own.

As soon as companies attempted to utilize LLMs in enterprise Q&A, code intelligence, QA analysis, incident investigation, compliance reasoning, and decision support, they encountered serious limitations. Prompting was not sufficient in bridging generic model knowledge and current organization-specific information that could be confirmed. This fact made it clear that LLMs were dependent on external data and systems to be really useful in concrete enterprise scenarios.

## Retrieval-Augmented Generation (RAG)

RAG (Retrieval-Augmented Generation) was introduced to fill the gap between powerful language models and the actual dynamic knowledge that enterprises depend on every day. To truly know its worth and the extent of its powerlessness, we need to see through marketing claims and examine RAG for what it actually is: an architectural abstraction.

<div class="mb-30">

<img src="https://testrigor.com/wp-content/uploads/2026/02/Retrieval-Augmented-Generation-RAG-IMG.jpeg" class="shadow" style="width: 100% !important" decoding="async" />

</div>

### What RAG Actually is

Retrieval-Augmented Generation (RAG), an architectural paradigm in which the retrieval of documents from an external knowledge source is sparked by a user’s query. This extracted content is then injected into the LLM prompt to enable the model to generate an answer based on its training data and available context. In other words,

**RAG = LLM + Search + Prompt Injection**, essentially lacking reasoning or memory or any kind of autonomy.

### Why RAG Emerged

RAG was proposed to address three fundamental limitations of vanilla LLM usage: hallucinations, stale knowledge, and not being domain-specific. By anchoring model responses relative to retrieved external evidence, the approach substantially mitigates guessing and overconfidence. As the outcome, RAG significantly boosts factual correctness, domain fidelity, and reliability.

*Read:* [*Retrieval Augmented Generation (RAG) vs. AI Agents*](https://testrigor.com/blog/rag-vs-ai-agents/)*.*

### Typical RAG Architecture

<div class="mb-10">

A classic RAG pipeline consists of a document store, a chunking and embedding process, a vector database, a retriever, a prompt assembler, and an LLM. These components operate in a fixed, linear sequence where content is retrieved once and injected into the prompt to generate a response. A classic RAG pipeline includes:

</div>

- **Document Store**: Holds source content such as PDFs, wikis, tickets, and logs that serve as the knowledge base.
- **Chunking Strategy**: Splits large documents into smaller, manageable pieces suitable for embedding and retrieval.
- **Embedding Model**: Converts text chunks into numerical vectors that capture semantic meaning.
- **Vector Database**: Stores embeddings and enables fast similarity-based searches.
- **Retriever**: Selects the most relevant chunks based on the user query and embedding similarity.
- **Prompt Assembler**: Injects the retrieved content into a structured prompt for the model.
- **LLM**: Generates the final response using its training data combined with the injected context.

The overall flow is linear and deterministic, with each step executed once in a fixed sequence.

### Strengths and Weaknesses of RAG

RAG is widely adopted because it offers a simple and reliable way to ground LLM responses in external knowledge. However, beneath this simplicity lie structural limitations that become evident as use cases grow more complex.

<div class="table-responsive mb-30">

| Advantages of RAG | Disadvantages of RAG |
|----|----|
| Conceptually simple and easy to understand | Lacks reasoning about *what* or *why* to retrieve |
| Relatively easy to implement and maintain | Retrieval is similarity-based, not intent-driven |
| Cost-efficient compared to agentic systems | Cannot ask follow-up questions or refine retrieval |
| Transparent and deterministic behavior | Single-shot context with no ability to request more information |
| Predictable outputs due to a fixed pipeline | Cannot verify answers or backtrack when wrong |
| Works well for document-based Q&A and search | Highly sensitive to chunk size and retrieval ranking |
| Effective for support bots and internal docs | Fragile prompts where small changes impact results |
| Suitable for static knowledge bases | No memory, planning, or self-reflection capabilities |

</div>

## Agentic RAG: When Retrieval Becomes Intentional

Agentic RAG is the next generation of retrieval-augmented systems, in which retrieval is motivated by intent rather than a fixed pipeline. That is not just about one-shot context injections, though, but AI systems that can think and adapt for themselves.

### Why Agentic RAG Exists

Even as teams tried to create more advanced AI, they rapidly reached a limit with standard RAG. They wanted systems that could decide what and when to retrieve without stacking multiple retrievals, use tools, reflect on their own answers, and retry when they weren’t sure. This active role of decision-making and adaptive retrieval is what immediately gave rise to Agentic RAG.

<div class="mb-30">

<img src="https://testrigor.com/wp-content/uploads/2026/02/Agentic-RAG-When-Retrieval-Becomes-Intentional-IMG.jpeg" style="width: 100% !important" decoding="async" />

</div>

### What is Agentic RAG?

Agentic RAG is an extension of classic RAG by introducing autonomy and reasoning to the retrieval. It doesn’t use a single “retrieve once, answer once” flow, but rather follows an iterative loop of thinking, retrieving, considering, and retrieving again until it gets to a confident conclusion. In this manner, the LLM behaves as a proactive agent seeking ahead, choosing its devices, seeking advice, and thinking about results so that it iterates towards improvement.

*Read:* [*Different Evals for Agentic AI: Methods, Metrics & Best Practices*](https://testrigor.com/blog/different-evals-for-agentic-ai/)*.*

### Core Components of Agentic RAG

<div class="mb-10">

An agentic RAG typically includes:

</div>

- **Planner or Reasoning Loop**: Defines the order in which the agent will act, considering the goal and intermediate results.
- **Multiple Tools**: Allow the agent to be able to collect information, make an api call, do math or interact with databases when necessary.
- **Memory Layer**: It stores past interactions and decisions as an intermediate result to make them consistent across steps.
- **Decision Logic**: Determines the next action or tool, and retrieval strategy based on its current context of operation.
- **Retry and Evaluation Mechanisms**: Determine the quality of an answer, trigger re-retrieval or alternative reasons if low confidence.

### Difference Between Agentic RAG and Regular RAG

Standard RAG and Agentic RAG may sound similar, but they represent fundamentally different approaches to how AI systems retrieve and reason over information. Understanding these differences is critical to choosing the right architecture for complex, real-world use cases.

<div class="table-responsive mb-30">

| Dimension | Standard RAG | Agentic RAG |
|----|----|----|
| Retrieval | Single, one-time retrieval based on similarity search | Iterative retrieval where the agent can refine queries and fetch additional context as needed |
| Control | System-driven flow with a fixed pipeline | Model-driven flow where the LLM decides the next action |
| Reasoning | Implicit and limited to prompt interpretation | Explicit reasoning loop that plans, evaluates, and adapts |
| Tool Usage | Static and predefined at design time | Dynamic selection and chaining of tools at runtime |
| Error Recovery | No built-in recovery; incorrect answers pass through | Built-in evaluation and retry mechanisms |
| Memory | No memory beyond the prompt context | Optional memory to retain intermediate state and past insights |

</div>

This makes Agentic RAG fundamentally more adaptive, resilient, and capable of handling complex, real-world tasks.

### Advantages and Limitations of Agentic RAG

Agentic RAG significantly expands what retrieval-augmented systems can do by introducing reasoning, autonomy, and adaptability. However, these gains come with important trade-offs that teams must understand before adopting this approach.

<div class="table-responsive mb-30">

| Advantages of Agentic RAG | Limitations of Agentic RAG |
|----|----|
| Enables multi-step and iterative reasoning | Introduces significant architectural complexity |
| Supports conditional and dynamic retrieval | Higher latency due to multiple reasoning steps |
| Allows intelligent tool selection and chaining | Harder to debug when failures occur |
| Can evaluate and self-correct responses | Self-evaluation is imperfect and can still fail |
| Expands context progressively as needed | Risk of over-retrieval and unnecessary exploration |
| Well-suited for complex investigations and analysis | Often excessive for simple or deterministic use cases |
| Powers AI copilots and autonomous assistants | Less predictable behavior and possible intent drift |

</div>

## MCP (Model Context Protocol): A Structural Shift

MCP (Model Context Protocol) is a radical break from existing paradigms of how large-scale language models can be interfaced with external knowledge and systems. Rather than piling retrieval machinery atop models, MCP redoes context itself as a solid, utilitarian base for cognition.

*Read:* [*What is Model Context Protocol (MCP)?*](https://testrigor.com/blog/model-context-protocol/)

### Why MCP is Fundamentally Different

RAG and Agentic RAG both view the context as being fetched and injected on demand. MCP, however, presents the notion of context as a first-class infra level on top of which models have reliable access and agility to reason over. This abstraction from ‘context as payload’ to ‘context as infrastructure’ is single-handedly the most valuable distinction in this whole article, and radically shifts how AI systems are conceived.

<div class="mb-30">

<img src="https://testrigor.com/wp-content/uploads/2026/02/Why-MCP-is-Fundamentally-Different-IMG.jpeg" style="width: 100% !important" decoding="async" />

</div>

### What is MCP?

Model Context Protocol (MCP) is a well-defined protocol comprising an interface to ensure that accesses and usage of external context from the model will be constant and secure. It defines how tools expose data, how permissions are applied and enforced, how context is accessed dynamically, and models that can interface with systems without resorting to brittle prompt injection or ad-hoc integrations.

MCP isn’t a retrieval mechanism, prompting method, or agent architecture built on top of a model. Rather, it is a protocol layer which mediates the flow of context that provides models with structured, reliable, and regulated context or in coder’s words: **It gives AI applications inbound.**

### The Core Idea Behind MCP

The fundamental idea of MCP is that one would like to avoid having to stuff gigantic amounts of data into prompts. Rather, MCP enables models to ask for the specific context they want when they want it via structured and governed interfaces. This change displaces how models connect to systems, data, and understanding.

### MCP vs. Prompt Injection

In RAG, context is indiscriminately injected into the prompt without any guarantees about its sufficiency or relevance. The model cannot ask for more data, process what it receives, and then double-check that this was the data from where you think it comes. Thus, the quality of the response is strongly dependent on prompt generation and retrieval correctness.

*Read:* [*Prompt Engineering in QA and Software Testing*](https://testrigor.com/prompt-engineering-in-software-testing/)*.*

In MCP, models explicitly request context information through clear interfaces instead of passive prompt injection. Systems define what data can be accessed, permissions are enforced, and the responses are strongly typed structures of information, not just raw text. This results in a controlled, testable, and much more reliable way of the models interacting with other systems.

### MCP Architecture

<div class="mb-10">

MCP is based on a completely new architectural approach in which context occurs via a structured, governed infrastructure rather than being injected into prompts. This framework allows models to actively request, verify, and utilize external information in a thoughtful and safe way. An MCP-based system typically includes:

</div>

- **MCP Servers**: Expose tools and data through standardized, structured interfaces.
- **Context Providers**: Supply relevant information dynamically based on model-initiated requests.
- **Permission Boundaries**: Enforce access control and ensure models only see authorized data.
- **Structured Schemas**: Define typed, predictable data formats instead of unstructured text.
- **Model-initiated Requests**: Allow the model to actively request context rather than receive injected prompts.

### ​​Why MCP is a Paradigm Shift

MCP achieves a nice separation of concerns by specifying explicit contracts between models and systems, strong security boundaries, and governance. This design allows for reusability of context access, as well as making it auditable and easier to evolve without breaking other people’s applications. In this way, MCP makes context management something more than ad-hoc prompt logic: **A solid engineering layer**.

This paradigm shift is comparable to how HTTP standardized web communications, SQL established database access, and APIs have enabled transactions to be standardized between services. Each of these abstractions abolished brittle, bespoke interfaces in favor of reasonable and interoperable ones. MCP uses the same logic for AI models interacting with tools and data.

## RAG vs. Agentic RAG vs. MCP: Architectural Comparison

Although RAG, Agentic RAG and MCP are usually mentioned together but they share a fundamentally different architectural view. It is important to comprehend how each of these schemes handles the concepts of context, intelligence, and control for building scalable and dependable AI systems.

<div class="table-responsive mb-30">

| Aspect | RAG | Agentic RAG | MCP |
|----|----|----|----|
| Context Delivery | Context is injected directly into the prompt in a single step | Context is retrieved iteratively through agent-driven decisions | Context is explicitly requested through a standardized protocol |
| Intelligence Location | Minimal intelligence, mostly prompt-driven | High intelligence embedded in agent reasoning loops | Intelligence is delegated to system design and infrastructure |
| Governance | Weak governance with limited control over data exposure | Weak to moderate governance, depending on agent design | Strong governance is enforced through protocol rules and permissions |
| Security Model | Prompt-based and fragile | Tool-based with partial isolation | Protocol-based with explicit access boundaries |
| Scalability | Limited as context size and complexity grow | Complex and costly to scale due to orchestration overhead | High scalability due to standardized, reusable interfaces |
| Debuggability | High due to linear, deterministic flow | Low due to non-linear agent behavior | High due to clear contracts and structured interactions |

</div>

<div class="mb-10">

To be precise, we can say that:

</div>

- **RAG**: “Here’s everything I found: answer now.”
- **Agentic RAG**: “Let me think about what I need, then answer.”
- **MCP**: “Let me ask the system for exactly what I’m allowed to know.”

## Choosing the Right Architecture

Depending on the depth of the problem, governance requirements, and planned scalability, it should be the one. The table given above summarizes when RAG, Agentic RAG or MCP is the most suitable.

<div class="table-responsive mb-30">

| Approach | When to Use It | Typical Examples |
|----|----|----|
| RAG | Data is static, queries are simple, accuracy matters more than reasoning, and cost and simplicity are priorities | Internal FAQ bots, documentation assistants, knowledge portals |
| Agentic RAG | Problems require multi-step reasoning, context is distributed, exploration is required, and you accept added complexity | Incident analysis, AI copilots, investigative assistants, and QA root-cause analysis |
| MCP | Strong governance is required, security and permissions matter, multiple tools and systems are involved, and long-term scalability is a goal | Enterprise AI platforms, regulated environments, developer tooling, and autonomous systems at scale |

</div>

## The Evolutionary Path

RAG, Agentic RAG, and MCP are not conflicting ideas so much as competing stages of AI development. RAG adds grounding, Agentic RAG adds autonomy, and MCP provides the structure and governance necessary for scale and reliability.

Most mature AI systems will eventually use MCP as the foundation, layer agentic reasoning on top of it, and apply retrieval selectively where it provides the most value rather than as a default mechanism. This progression mirrors how software systems evolve from simple integrations to robust, platform-level architectures.

## Conclusion

The right question to be asked isn’t which one is better, but how much intelligence, control, and scale you really need. RAG democratized a form of grounding, Agentic RAG freed reasoning and autonomy, and MCP professionalizes AI system architectures for production-grade systems. With AI moving from the experimental to the critical, this distinction is no longer a luxury; it’s a necessary precursor to building serious AI systems in the future.

<div class="bp-cta">

You're <span class="text-red">15 Minutes Away</span> From Automated Test Maintenance and Fewer Bugs in Production

</div>

<div class="text-center" style="margin: 20px auto; max-width: 600px">

Simply fill out your information and create your first test suite in seconds, with AI to help you do it easily and quickly.

</div>

|  |  |
|----|----|
| <span class="svg-point-bg">![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCA1MTIgNTEyIj48cGF0aCBkPSJNMTczLjkgNDM5LjRsLTE2Ni40LTE2Ni40Yy0xMC0xMC0xMC0yNi4yIDAtMzYuMmwzNi4yLTM2LjJjMTAtMTAgMjYuMi0xMCAzNi4yIDBMMTkyIDMxMi43IDQzMi4xIDcyLjZjMTAtMTAgMjYuMi0xMCAzNi4yIDBsMzYuMiAzNi4yYzEwIDEwIDEwIDI2LjIgMCAzNi4ybC0yOTQuNCAyOTQuNGMtMTAgMTAtMjYuMiAxMC0zNi4yIDB6IiAvPjwvc3ZnPg==)</span> | Achieve More Than **90% Test Automation** |
| <span class="svg-point-bg">![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCA1MTIgNTEyIj48cGF0aCBkPSJNMTczLjkgNDM5LjRsLTE2Ni40LTE2Ni40Yy0xMC0xMC0xMC0yNi4yIDAtMzYuMmwzNi4yLTM2LjJjMTAtMTAgMjYuMi0xMCAzNi4yIDBMMTkyIDMxMi43IDQzMi4xIDcyLjZjMTAtMTAgMjYuMi0xMCAzNi4yIDBsMzYuMiAzNi4yYzEwIDEwIDEwIDI2LjIgMCAzNi4ybC0yOTQuNCAyOTQuNGMtMTAgMTAtMjYuMiAxMC0zNi4yIDB6IiAvPjwvc3ZnPg==)</span> | Step by Step **Walkthroughs and Help** |
| <span class="svg-point-bg">![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCA1MTIgNTEyIj48cGF0aCBkPSJNMTczLjkgNDM5LjRsLTE2Ni40LTE2Ni40Yy0xMC0xMC0xMC0yNi4yIDAtMzYuMmwzNi4yLTM2LjJjMTAtMTAgMjYuMi0xMCAzNi4yIDBMMTkyIDMxMi43IDQzMi4xIDcyLjZjMTAtMTAgMjYuMi0xMCAzNi4yIDBsMzYuMiAzNi4yYzEwIDEwIDEwIDI2LjIgMCAzNi4ybC0yOTQuNCAyOTQuNGMtMTAgMTAtMjYuMiAxMC0zNi4yIDB6IiAvPjwvc3ZnPg==)</span> | **14 Day Free Trial**, Cancel Anytime |

<div class="bp-cta-testimonial">

<div class="bp-cta-t-left-block">

<div class="bp-cta-t-person-img">

<img src="/wp-content/uploads/2022/03/Keith@2x_-150x150-1.png" decoding="async" />

</div>

</div>

<div class="bp-cta-t-right-block">

<div class="mb-20">

“We spent so much time on maintenance when using Selenium, and we spend nearly zero time with maintenance using testRigor.”

</div>

<div>

<span class="bp-cta-t-person-name">Keith Powe</span> <span class="bp-cta-t-person-position">VP Of Engineering - IDT</span>

</div>

</div>

</div>

<div class="buttons-block bb-centered mb-30">

<div>

<a href="/sign-up/" class="btn btn-outline-danger">Start testRigor Free</a>

</div>

<div>

<a href="/request-demo/" class="btn btn-danger">Request a Demo</a>

</div>

</div>

<style>
.bp-cta-table {
margin: 0 auto 30px auto;
}
.bp-cta-table tr td:first-child {
padding: 0px 10px 0px 0px
}
.bp-cta-table tr td {
padding-bottom: 15px
}
.bp-cta-table tr td:first-child svg {
width: 18px;
height: 16px;
}
.bp-cta-table tr td:first-child svg path {
fill: #fff
}
.bp-cta-testimonial {
position: relative;
display: flex;
gap: 20px;
padding: 20px;
background: #faf7f7;
-webkit-border-radius: 12px;
border-radius: 12px;
}
.bp-cta-t-person-name {
font-weight: bold
}
.bp-cta-t-person-img img {
width: 103px !important;
}
.bp-cta-t-person-position {
color: #6b7280;
}
.bp-cta {
font-weight: bold;
text-align: center;
margin: 60px 0px 20px 0px;
font-size: 35px;
line-height: 130%;
}
.svg-point-bg {
display: inline-block;
background: #26942f;
-webkit-border-radius: 50%;
border-radius: 50%;
padding: 5px 10px;
margin-bottom: 10px;
}
@media screen and (max-width: 768px) {
.bp-cta {font-size: 30px; margin-bottom: 60px}
}
</style>

</div>

</div>

<div class="aside post-column-right">

<div class="sticky-container">

<div>

<style>
.post-newsletter {padding: 15px; background: #f7f7fc; font-size: 15px; line-height: 130%; display: flex; margin-bottom: 30px; align-items: center;}
.post-newsletter .newsletter-question, .post-newsletter .newsletter-action {margin-top: 20px}
.post-newsletter .hs-error-msg, .post-newsletter .hs-error-msgs {color: #f10001; font-weight: 400; font-size: 13px; line-height: 140% !important}
.post-newsletter .hs-error-msgs {font-weight: bold; margin-bottom: 0px}
.post-newsletter .grecaptcha-logo {display: none}
.post-newsletter .grecaptcha-badge {height: auto !important; -webkit-box-shadow: 0 0 0 0 #fff !important; box-shadow: 0 0 0 0 #fff !important;}
.post-newsletter .hbspt-form {position: relative; text-align: left; padding: 5px}
.post-newsletter .hs-form {padding: 0px; border: 0px; -webkit-border-radius: 0px; border-radius: 0px; -webkit-box-shadow: 0 0 0 0 #fff; box-shadow: 0 0 0 0 #fff;}
.post-newsletter .hs-form label {margin-top: 20px; font-size: 15px}
.post-newsletter .hs-form .hs-error-msgs li label {margin-top: 0px}
.post-newsletter .hs-form .hs-input {background: #fff; -webkit-border-radius: 10px; border-radius: 10px; padding-left: 10px; padding-right: 10px; width: 100% !important}
.post-newsletter .hs-form .hs-button {background-color: #f10000; border: 3px solid #fff; margin-top: 20px; -webkit-border-radius: 10px; border-radius: 10px; width: auto !important; padding: 8px 20px !important; font-size: 15px;}
.post-newsletter .hs-submit a {cursor: pointer; color: #000; text-decoration: underline; text-decoration-color: #f10001 !important; text-decoration-thickness: 0.7px !important; text-underline-offset: .5ex; transition-duration: 0.2s; -moz-transition-duration: 0.2s; -webkit-transition-duration: 0.2s; -o-transition-duration: 0.2s; -ms-transition-duration: 0.2s}
.post-newsletter .newsletter-action {cursor: pointer; color: #f10001; text-decoration: underline; text-decoration-color: #f10001 !important; text-decoration-thickness: 0.7px !important; text-underline-offset: .5ex; transition-duration: 0.2s; -moz-transition-duration: 0.2s; -webkit-transition-duration: 0.2s; -o-transition-duration: 0.2s; -ms-transition-duration: 0.2s}
.post-newsletter.newsletter-hidden {display: none !important}
.post-container-wrapper article.post-column ul.hs-error-msgs {margin-bottom: 0px}
.hbspt-form .submitted-message.hs-main-font-element {padding: 10px; color: #0f5132; background: #def6e0}
</style>

</div>

</div>

</div>

</div>

<div class="md-text">

Related Articles

</div>

<div class="row">

<div class="col-md-4 mt-50" style="margin-bottom: 120px;">

<div class="card">

<div class="featured-img-container">

[](https://testrigor.com/blog/how-to-test-applications-built-with-claude-code-using-testrigor/)

<div class="featured-img trans" style="background-image: url('https://testrigor.com/wp-content/uploads/2026/08/How-to-Test-Applications-Built-with-Claude-Code-Using-testRigor-Title.jpeg'); height: 200px;">

</div>

</div>

<div class="card-body">

<div class="category-block-left">

- <a href="https://testrigor.com/blog/category/ai-in-software-development/" rel="category tag">AI in Software Development</a>
- <a href="https://testrigor.com/blog/category/generative-ai/" rel="category tag">Generative AI</a>

</div>

<div class="header entry-header">

## [<span class="text-black">How to Test Applications Built with Claude Code Using testRigor</span>](https://testrigor.com/blog/how-to-test-applications-built-with-claude-code-using-testrigor/ "How to Test Applications Built with Claude Code Using testRigor")

</div>

<div class="entry-excerpt">

Claude Code can inspect repositories, build components, connect APIs, modify databases, write tests, and fix failures to quickly ...

</div>

<div class="entry-footer">

<div class="sep mb-20">

</div>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td class="pr-10"><img src="https://secure.gravatar.com/avatar/dd24e1d84d119ce4acbab64f253523d8f7c5a3706dcb42b4bf6d0258dcfbf752?s=96&amp;d=retro&amp;r=g" class="avatar avatar-96 photo" srcset="https://secure.gravatar.com/avatar/dd24e1d84d119ce4acbab64f253523d8f7c5a3706dcb42b4bf6d0258dcfbf752?s=96&amp;d=retro&amp;r=g 2x" decoding="async" width="96" height="96" /></td>
<td><div class="entry-author">
Gabriel Ernandes
</div>
<div id="postDate_1133059" class="entry-date">
&#10;</div></td>
</tr>
</tbody>
</table>

</div>

</div>

</div>

</div>

<div class="col-md-4 mt-50" style="margin-bottom: 120px;">

<div class="card">

<div class="featured-img-container">

[](https://testrigor.com/blog/what-is-test-plan-driven-development/)

<div class="featured-img trans" style="background-image: url('https://testrigor.com/wp-content/uploads/2026/07/Why-Traditional-Development-Causes-Testing-Issues-Title.jpeg'); height: 200px;">

</div>

</div>

<div class="card-body">

<div class="category-block-left">

- <a href="https://testrigor.com/blog/category/software-architecture/" rel="category tag">Software Architecture</a>
- <a href="https://testrigor.com/blog/category/test-development/" rel="category tag">Test Development</a>

</div>

<div class="header entry-header">

## [<span class="text-black">What is Test Plan Driven Development (TPDD)?</span>](https://testrigor.com/blog/what-is-test-plan-driven-development/ "What is Test Plan Driven Development (TPDD)?")

</div>

<div class="entry-excerpt">

Most in the software development industry will agree that for years, testing was treated as the last task in the SDLC. This was ...

</div>

<div class="entry-footer">

<div class="sep mb-20">

</div>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td class="pr-10"><img src="https://secure.gravatar.com/avatar/978f516e741528a501a7c4124c0a0a6a33c6127bd4b3eda8cda76c1e3c5d9b78?s=96&amp;d=retro&amp;r=g" class="avatar avatar-96 photo" srcset="https://secure.gravatar.com/avatar/978f516e741528a501a7c4124c0a0a6a33c6127bd4b3eda8cda76c1e3c5d9b78?s=96&amp;d=retro&amp;r=g 2x" decoding="async" width="96" height="96" /></td>
<td><div class="entry-author">
Megana Natarajan
</div>
<div id="postDate_1132806" class="entry-date">
&#10;</div></td>
</tr>
</tbody>
</table>

</div>

</div>

</div>

</div>

<div class="col-md-4 mt-50" style="margin-bottom: 120px;">

<div class="card">

<div class="featured-img-container">

[](https://testrigor.com/blog/system-design-vs-software-architecture/)

<div class="featured-img trans" style="background-image: url('https://testrigor.com/wp-content/uploads/2025/07/System-Design-vs-Software-Architecture-Article-Banner.jpeg'); height: 200px;">

</div>

</div>

<div class="card-body">

<div class="category-block-left">

- <a href="https://testrigor.com/blog/category/engineering/" rel="category tag">Engineering</a>
- <a href="https://testrigor.com/blog/category/software-architecture/" rel="category tag">Software Architecture</a>

</div>

<div class="header entry-header">

## [<span class="text-black">System Design vs. Software Architecture</span>](https://testrigor.com/blog/system-design-vs-software-architecture/ "System Design vs. Software Architecture")

</div>

<div class="entry-excerpt">

In software development, the terms system design and software architecture are often used interchangeably. However, while they ...

</div>

<div class="entry-footer">

<div class="sep mb-20">

</div>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td class="pr-10"><img src="https://secure.gravatar.com/avatar/978f516e741528a501a7c4124c0a0a6a33c6127bd4b3eda8cda76c1e3c5d9b78?s=96&amp;d=retro&amp;r=g" class="avatar avatar-96 photo" srcset="https://secure.gravatar.com/avatar/978f516e741528a501a7c4124c0a0a6a33c6127bd4b3eda8cda76c1e3c5d9b78?s=96&amp;d=retro&amp;r=g 2x" decoding="async" width="96" height="96" /></td>
<td><div class="entry-author">
Megana Natarajan
</div>
<div id="postDate_1127262" class="entry-date">
&#10;</div></td>
</tr>
</tbody>
</table>

</div>

</div>

</div>

</div>

</div>

<style>
.wrapper {overflow: initial}
.entry-title {margin: 40px 0px}
.sticky-container {position: sticky; top: 90px; max-height: calc(100vh - 100px); overflow: auto}
.post-container-wrapper {position: relative}
.post-container-wrapper aside.post-column-left {position: absolute; top: 10px; left: 20px; width: 260px}
.post-container-wrapper aside.post-column-right {position: absolute; top: 10px; right: 20px; width: 260px}
.post-container-wrapper article.post-column {width: 100%;padding:0px 300px}
.post-container-wrapper article.post-column table.table tr th {background: #f9f9f9}
.post-container-wrapper article.post-column h2 {margin: 30px 0px}
.post-container-wrapper article.post-column h3, .post-container-wrapper article.post-column h4, .post-container-wrapper article.post-column h5, .post-container-wrapper article.post-column h6 {margin: 20px 0px}
.post-container-wrapper article.post-column ul, .post-container-wrapper article.post-column ol, .post-container-wrapper article.post-column pre {margin-bottom: 30px}
.post-container-wrapper article.post-column ul li ul {margin-bottom: 0px}
.table-contents-title {text-transform: uppercase; font-size: 14px; font-weight: 900}
#postLeftNav, #mobileNav {list-style-type: none; margin: 0px; padding: 0px}
#postLeftNav li, #mobileNav li {position: relative; padding-left: 20px; font-size: 16px; line-height: 25px; margin: 10px 0px}
#postLeftNav li::before, #mobileNav li::before {content: ''; position: absolute; left: 0; top: 15px; width: 10px; height: 10px; background-color: #f10001; transform: translateY(-50%)}
#postLeftNav li a, #mobileNav li a {color: #000}
@media only screen and (max-width: 1100px) {
.post-container-wrapper aside.post-column-left, .post-container-wrapper aside.post-column-right {display: none}
.post-container-wrapper article.post-column {width: 100%; padding: 0px 20px}
}
@media only screen and (max-width: 650px) {
.post-newsletter {flex-direction: column}
}
</style>

</div>

</div>
