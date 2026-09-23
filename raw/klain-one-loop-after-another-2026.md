# Keith Klain — One Loop After Another (2026-09-16)

**Author:** Keith Klain (Quality Remarks)
**Source:** https://qualityremarks.com/one-loop-after-another/
**Context:** Post in the qualityremarks series (The Great Capitulation / Verification Asymmetry lineage). Response to Fast Company "Software That Can Check Its Own Quality" and to vendor claims of autonomous testing. Date 2026-09-16.

---
Expectations are being lowered to the point where AI generated and executed checks will be the primary method for testing systems. This will be paired with the "hands thrown up in the air" approach of the agentic coding community as they concede to Verification Asymmetry and just give up on reviewing AI generated code. This phenomenon Klain calls "The Great Capitulation".

Fast Company argues AI generates software faster than traditional testing can keep up, so the only answer is autonomous AI testing: AI generates the code, AI generates the tests, AI maintains those tests, AI analyses the results, humans move into higher-order oversight. Eventually "AI writes code, AI tests code, and humans are in the loop."

Klain: when the "quality loop closes", the human is in the loop like a sock in a dryer.

A former OpenAI safety researcher wrote in NYT about AI systems whose developers cannot predict what boundaries they will obey. Anthropic published analysis of cybersecurity incidents involving its models, acknowledging that creating evaluations which genuinely represent what those systems will do in real-world deployment remains an open research problem. Both should make anyone advocating for autonomous agentic testing rethink that position.

Anthropic is discovering that AI evaluators can be influenced by the reasoning of the systems they evaluate. European regulators explicitly warn about automation bias and require competent human oversight capable of challenging output.

EU AI Act Article 14 requires high-risk AI systems to be designed so they can be effectively overseen by natural persons. Article 26 places obligations on deployers to assign oversight to people with necessary competence, training and authority. Overseers must understand capabilities and limitations, monitor for unexpected behavior, remain conscious of automation bias, be capable of disregarding, overriding or reversing output and stopping it altogether.

The more humans depend on AI to decide which evidence matters, the less independently capable they are of evaluating the system they are charged with verifying; HITL just becomes acceptance.

The same vendor claiming software can now "check its own quality" acknowledged in another article (testmuai agentic-sdlc-vs-stlc, six days later) that "a system cannot independently confirm its own reading of a requirement". Their answer: ANOTHER AI loop acting as independent verifier.

The paper the article cites (arXiv:2605.15245) doesn't demonstrate autonomous agents independently establish software quality. Focus is narrower: agents work best when constrained to problems where someone has already made the answer objectively checkable. That's evidence AI is getting very good at checking, not that AI has solved testing.

The paper's own authors, when needing to establish whether their multi-agent system produced reliable results, manually verified the output — they didn't ask another agent and call the loop closed.

Vendor claims in software testing have always had a hard time standing up to scrutiny; "coverage" has been doing Trojan amounts of work for decades. "The productivity gains of autonomous testing are self-evident" should be met with skepticism in a business founded on the idea that NOTHING is self-evident.

A closed loop where a vendor defines the problem, provides the solution, provides the evidence, evaluates the evidence, claims benefits are self-evident, and all point to the article as independent validation of the trend. "Apparently, AI isn't the only thing capable of hallucinating." Repetition between vendors, analysts, conferences, executive networks and customers begins to look like evidence.

Conclusion: Software cannot "check its own quality". The problem isn't confined to using one AI loop after another to verify its own output, but another loop detached from reality operating alongside it: the software testing echo chamber surrounding autonomous testing.