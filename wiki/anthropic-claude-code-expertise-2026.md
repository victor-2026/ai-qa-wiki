# Anthropic: Agentic Coding Returns to Expertise (Jun 2026, 400K Sessions)

**Source:** Hitzig et al., "Agentic coding and persistent returns to expertise", Anthropic Research, 2026-06-16. Full text read 08.10. ~400K Claude Code sessions (~235K people, Oct 2025-Apr 2026), privacy-preserving analysis (Clio), judges Sonnet 4.6. URL: https://www.anthropic.com/research/claude-code-expertise
**Via:** Estefania Miceli post (Ameca anecdote + due-date-filter example + 3 questions).

## Division of labor (70/20)

People make ~70% of planning decisions (what/approach/done), Claude makes ~80% of execution (files/code/commands). Typical turn: 1 prompt → ~10 Claude actions (~2,400 words); 20h/week active use. Expert prompts set off 2× actions, 5× output vs novice.

## Expertise beats occupation

- Verified success (judged + hard signal: commits/PRs/tests/user affirmation): novice 15%, intermediate+ 28-33%; trouble-recovery 4% → 15%; abandonment 19% vs 5-7%.
- Occupations within 7pts of software engineers; management highest (specification skill transfers — "acting like a manager confers success").
- Fixing share 33% → 19%; task value +27%; debugging halved; shift to operate/analyze/write.

## Caveats (in-paper, honest)

No real-world outcomes observed (code used or discarded unknown); headless/SDK usage excluded; classifiers validate vs telemetry but long sessions resist human ground truth; freelance-price value estimates coarse. Watch metric proposed: returns-to-expertise decreasing = models supplying judgment.

## QA interpretation

- Domain expertise as the steering input = our "define the problem, guide the tool, challenge the result" in vendor-measured form; Estefania's 3 questions (missing risk? unchecked assumption? reconsider-evidence?) operationalize it for QE leads.
- Verified-success construct (judgment + hard signal) rhymes with our evidence discipline; abandonment-rate as quit-metric is adoptable.
- Article 27: "occupation matters less than expertise" + management-transfer finding.

## See also

- [[anthropic-spotify-quality-at-ai-speed-2026]] — 8x code, 25x CI (same vendor, production side)
- [[mike-peterson-qe-genai-perspective-2026]] — verification mindset, falsify/cite/rerun/cost
- [[storey-triple-debt-model-2026]] — shared understanding erosion (expertise as antidote)
