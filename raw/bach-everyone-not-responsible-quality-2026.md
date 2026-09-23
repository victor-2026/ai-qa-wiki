# Everyone is NOT Responsible for Quality (Satisfice, 2026-02-01)

**Author:** James Bach
**Source:** https://www.satisfice.com/blog/archives/487632
**Context:** Satisfice blog. Refutes the Agile slogan "quality is everyone's responsibility". Categories: Agile Methodology, Critique, Management, Process Dynamics, Quality, RST Methodology, Testing Culture.

---
Testing is a role, not just a task. "Testers do not assure quality. Testers CANNOT assure quality. Testers do not now and never have 'owned quality' in any way." Four readings of "everyone is responsible for quality":

1. **Chain Analogy** — each link answers only for its own work, no link makes any other stronger; nobody looks at the product as a whole. Weak system for obtaining a quality product. Worst case: everyone contributed, no one responsible for absence of defect.
2. **Total Redundancy** — any single person embodies all know-how/effort; each person tests everything and reaches independent opinion. Feasible only in 2-3 person close-knit teams (e.g. Bach & Bolton teaching RST); never seen work at medium-to-large scale.
3. **Herd Responsibility** — the feared one: "everyone is responsible" means no one person ever has to do anything or answer for quality; all questions referred to "the team"; the team is the scapegoat because nobody on the team is the team. Deployed defensively/magically, like "Expecto Patronum!"
4. **Weak Redundancy / Shared Aspiration** — everyone aspires to goodness, no real commitment. True commitment requires (a) same quality standard for all (diligent debate, shared culture — hard, time-consuming, socially risky), (b) sufficient knowledge of quality (either everyone tests everything, or shared knowledge well — but good testing is hard and enthusiasm varies), (c) control over product quality (without control commitment is meaningless; separation of spheres means no one controls everything, so responsibility is unequal).

Shallow-testing cop-out: teams without testers write and automate simple procedures, then declare passing those checks = good product.

**Recommendation: abandon collectivism, embrace personal responsibility, establish clear roles.** Localize and personalize responsibility to minimize conflict of interest (testing, dedicated to finding trouble, conflicts with development, dedicated to ending trouble):
- each person knows their own job and does it well;
- knows what the team expects;
- knows their role within the project;
- any difficult/unpopular activity must be matched to a defined role (else it won't be done well);
- product quality as a whole = responsibility of the people who *control* the project;
- quality of a piece = responsibility of the one who builds it;
- systematic software testing = responsibility of people dedicated to that process;
- each person responsible for providing reasonable support to all other members.

QA relevance: the "herd responsibility"/scapegoat critique is the governance-layer counter to collective-responsibility slogans; "quality of the whole = those who control the project" gives the accountable-role thesis (Article 27, VP of AIQE position 488204) a principled grounding; "everything is everyone's" as anti-pattern maps to Conway/ownership (Article 21).