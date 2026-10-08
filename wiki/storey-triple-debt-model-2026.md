# Storey Triple Debt Model (Technical / Cognitive / Intent, 2026)

**Sources:** Margaret-Anne Storey (Univ. of Victoria, SPACE co-creator), paper arXiv:2603.22106 (v4 Apr 6, 10pp, CC-BY) + blog 09.02.2026 (full text read 08.10) + QCon SF Nov 2026 talk listing. Via Lisa Crispin post (Tier-1, DORA Lean Coffee): https://www.linkedin.com/posts/lisacrispin_ai-technicaldebt-share-7513997649017192448-DqyW/ Paper: https://arxiv.org/abs/2603.22106 · Blog: http://margaretstorey.com/blog/2026/02/09/cognitive-debt/

## Triple Debt Model

- Technical debt: in code. Cognitive debt: in people (erosion of shared understanding / shared mental models, team-level property). Intent debt: in externalized knowledge (absent/eroded rationale, goals, constraints for humans AND agents).
- Claim: cognitive + intent may matter MORE than technical in AI-assisted dev. AI generates faster than teams can understand; Naur's "program as theory in developers' minds" fragments.
- Exhibit: student team hit wall at weeks 7-8 — blamed technical debt, real cause = nobody could explain design decisions (cognitive debt accumulated faster, paralysis).

## Mitigations (concrete)

- Require ≥1 human fully understands each AI change before ship; document WHY not just what; rebuild shared understanding via reviews/retros/knowledge-sharing.
- Warning signs: hesitation to change (fear), tribal knowledge in 1-2 heads, black-box feeling.
- Velocity without understanding is not sustainable; Brooks echo (more agents = coordination overhead); Beck "make the hard change easy".

## QA interpretation

- Intent debt = externalized rationale machines need = our evidence/intent layer in academic words (durable intent, pre-registration, decision logs).
- Cognitive debt explains review debt (Avito: looking-less) at team level; "lost the plot" = what seeded breaks detect from outside.
- Article 27/29: triple-debt framing for velocity-vs-understanding pieces; Naur theory as authority line.

## See also

- [[avito-agents-setup-metrics-review-2026]] — review debt, shared understanding loss
- [[anthropic-spotify-quality-at-ai-speed-2026]] — velocity vs verification
- [[jason-arbon-book-v1-v2-audit-2026]] — durable intent artifact
