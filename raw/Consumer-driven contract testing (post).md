[

Bas Dijkstra


](https://www.linkedin.com/in/basdijkstra/)

Test automation trainer | Consultant | Valuable feedback, fast | Newsletter: ontestautomation.com/newsletter | Work with me: ontestautomation.com/contact

2h •

[

](https://www.linkedin.com/in/basdijkstra/)

I've been talking about, implementing and teaching contract testing for (at least) 5-6 years now. Mostly, I've been using Pact and the tools in the Pact ecosystem, although I've done some work with other tools in this space, too. I also have yet a few more still on the 'I should try it out some time soon' list.  
  
For those of you who haven't heard about contract testing yet, it is a very useful technique to get an answer to the question of  
  
"Are this consumer and this provider able to communicate with one another?"  
  
at an early stage in the development and testing process for distributed software systems, without having to deploy both consumer and provider assets into an integrated test or production environment (and potentially breaking things there).  
  
Contract testing as a technique is still often misunderstood, though. It's not a replacement for _all_ your end-to-end testing, though there's a good chance it will answer some of the same questions that E2E testing attempts to answer both earlier and more efficiently.  
  
The misunderstanding that 'contract testing === Pact' also still pops up sometimes. Yes, Pact is a contract testing tool, and a very good one at that, but it doesn't fit all contexts. Even if only because it is a _consumer-driven_ contract testing tool, and that approach might not be the best fit for a particular context in the first place.  
  
I've spoken with several teams that thought 'we should do contract testing' and started a full-blown Pact implementation right away, without even considering a) the problem they were trying to solve, and b) whether consumer-driven contract testing and Pact were the right approach and the right tool for the job.  
  
I do really appreciate contract testing for its ability to deliver valuable feedback, fast, and I'll continue to learn and talk about it, and teach what I know and have learned to others, too.  
  
This week, I'm running session 2 of a contract testing workshop with a client here in the Netherlands, I've got a conversation going with a prospect in the DACH region, and after a call I received just before the weekend, there's a good chance that I'll be involved in a couple of other contract testing projects in the nearby future, too.  
  
I for one am really excited about that.
![[Pasted image 20260622115842.png]]
=====

  
Victor Rincon Verified Profile 2ndVictor Rincon • 2nd

Engineering Leader | Scaling Delivery, Reliability & Team Performance





(https://www.linkedin.com/in/vmrincon/)

15m

Follow

consumer-driven contract testing removes the need of having both sides running at the same time, but does not remove the coupling... why may be problematic, specially when working at scale ( read, worldwide ). For that I've found bi-directional contract testing useful, cause the consumer pact file is assessed against the API spec delivered by the provider, eliminating the "I want to update my contract, can you run your side please?"  
  
The downside is that this is a commercial feature provided by PactFlow, but if you have the bucks, worth taking a look.