# Tony Seale — Multi-Agent Systems and the Semantic Web

**Source:** LinkedIn post, Tony Seale (The Knowledge Graph Guy, 2nd degree)
**Date:** ~2026-09-03/04 (10h before fetch 2026-09-04)
**Fetched:** 2026-09-04
**Links in post:** Sharing https://lnkd.in/eAr-iD-b, Boundary https://lnkd.in/er_HjtWg, KGG https://lnkd.in/eSrYRybk (shortened, not resolved)

---

I have spent the last few months building multi-agent systems. Building them, running them, watching them talk.

And it is becoming clear where this is heading.

OpenClaw 2.0 shipped this week with a move towards collaborative agents. Meanwhile, OpenAI revealed something stranger: agents in separate environments discovered a way to communicate through infrastructure never designed for messaging. Hundreds of them then used it to coordinate the attack on Hugging Face.

We have not finished making one agent reliable, and already the frontier is many.

Once agents start talking to one another, AI becomes a distributed systems problem. And that is what the Semantic Web was designed for.

INFORMATION BOUNDARY MATTERS

The moment two agents communicate, something crosses between them.

Each agent has information that should remain private - credentials, client data, internal context - and information it is prepared to share. The hard part is that the useful and the private are tangled together.

I have written before about active inference and information boundaries: intelligent systems need a membrane between themselves and the world. Multi-agent systems make that concrete. Every agent has a boundary, and you have to decide what crosses it. DPROD 1.2 will add ODRL-based data contracts that can scale to this complexity.

ENGLISH IS NOT ENOUGH

Agents can talk in natural language. But if they are going to exchange information reliably, natural language is too ambiguous on its own.

"The customer." "The contract." "The product."

Two agents can use the same words while meaning different things.

We tighten that in two ways.

First, shared concepts. If my agent says Contract and yours says Agreement, do we mean the same thing? Connecting agents starts to look like ontology alignment - a negotiation about how their models of the world correspond.

Second, shared identifiers. Even if we agree what a Contract is, we still need to know whether we mean the same contract. You need an identifier both sides can resolve. In a distributed system, the obvious pattern is the one the Web already gave us: a URL.

SEMANTICS IS COMPRESSION

Agents are chatty. I have blown through token limits because agents keep explaining things to one another. Semantics is not only about precision. It is also about compression. If you can agree on the semantics of the message, you can compress the communication in information-theoretic terms.

What we are building between two or three agents today is only a rehearsal for the Agentic Web. Ontologies and URLs were designed to let independently built systems exchange meaning across boundaries at global scale. We are rediscovering it one agent at a time.

*Note: OpenClaw 2.0 release timing and OpenAI/Hugging Face coordination claims are per author, unverified at ingest.*
