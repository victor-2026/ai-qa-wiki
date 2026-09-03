# Who Is Accountable for AI-Generated Code?

**Source:** https://juliapottinger.com/ (Julia Pottinger, Quality Engineering) — via Software Testing Weekly #325 #3; also referenced: Richard Forjoe "Stop Trying to Keep Up With AI Code Generation"
**Date:** August 2026 (newsletter #325, Aug 25 "When an AI writes the code, a person still owns that it is right" 10 min)
**Tags:** #accountability #AI-generated-code #sign-off #human-review-gate
**Raw:** [software-testing-weekly-newsletter-2026.md](software-testing-weekly-newsletter-2026.md)

---

## What It Is

Simple test: can you sign off on an AI-assisted change? Where is sign-off recorded in the PR? If you can't, you don't have accountability — you have diffused responsibility. AI didn't remove accountability; it diffused it across so many hands that no one owns outcome.

Companion: Richard Forjoe — "Stop Trying to Keep Up With AI Code Generation" (don't chase generation speed, fix review throughput).

## Core Thesis

- AI accelerated authorship, not ownership. Ship still owned by team that ships.
- Three layers where accountability must have a human name:
  1. **Individual:** one named human reviewed and is willing to be on-call at 2 a.m. for that change. "Human in the loop" = a name, not "team approved" or "tests passed."
  2. **Team:** working agreement / definition of done decides which work can use AI without extra review vs which (auth, payment, PII) always requires it. Protects reviewers from auditing everything; protects org from slipping critical path.
  3. **Organizational:** leadership policy: approved AI tools, categories, quality metrics, leadership owner for AI quality events, quarterly review. Without structures, "supervision" is unmanaged.

## Practical Mechanism: Reviewer of Record

Tiny change to definition of done, proposed by a Scrum Master:

```
Reviewer of record: [human name]
```

For any PR with AI-assisted code, reviewer is named human, name in PR description. Person who looked, understood, is willing to take 2 a.m. call. If nobody willing → clarity problem, not AI-quality problem.

Within a week you learn: who feels comfortable being named, which PRs nobody wants to sign (riskiest), where review expectations actually lie.

## Why "Tests Passed" Is Not Accountability

- AI that introduces subtle bug can also write test that doesn't catch it. Green on AI-written code + AI-written tests = weakest evidence alone.
- Diffused ownership breaks traditional chain: author on commit didn't write logic ("I didn't put that in there"), but did prompt; downstream unsure where job ends. Coordination failure, not developer malice — leadership design problem.

## Relevance to QA/QE

| Accountability Gap | QA Action |
|--------------------|-----------|
| No named owner | Require `Reviewer of record: [name]` in PR template for AI-assisted changes |
| "It passed" as proxy | Treat green as information, not decision; decide out loud: "Ship, with this evidence" or "Not yet, because gap" |
| Unclear AI-allowed scope | Team agreement: AI OK for private utility refactor, never without deep review for auth/payment/PII |
| No evidence of check | Record prompt/model, what changed, what was tested, who reviewed — traceable in 30 seconds, not 30 minutes |

## Critical Analysis

**Strengths:**
- Actionable one-line process change vs 50-page policy no one reads.
- Connects to QA control layer (Julia Pottinger's theme: QA owns risk/evidence/approval, agent assists).

**Gaps:**
- Soc/Compliance perspective (board-level risk, audit trail) less deep than Augment/CISA framing; supplements with evidence storage.
- Doesn't resolve legal copyright/training-data IP — ownership of output vs accountability for outcome are separate.

## Cross-links

- Related: [Julia Pottinger QA is the Control Layer](qa-control-layer-for-ai-assisted-development-2026.md) (control layer wraps around work)
- Related: [Testing AI-Generated Code: 6 Checks](https://juliapottinger.com/is-that-green-checkmark-real/) — narrowest test, read assertions, real device, artifact
- Related: [Keith Klain Testing Mindset](keith-klain-testing-mindset-after-all-2026.md) — evaluator independence supports accountable sign-off
- Newsletter: [Software Testing Weekly #325](software-testing-weekly-newsletter-2026.md)

---


## Quick Start (This Week)
- Pick one team.
- Require `Reviewer of record: [name]` on every AI-assisted PR.
- Track: who signs, who avoids, which PRs nobody wants — that's risk signal.
- After 7 days, discuss what reviewing AI output should actually look like — then codify.


## Control Layer Connection
Accountability is human decision in QA control layer: risk → evidence → approval. Green checkmark is information, not decision.

Note: Testing mindset ≠ gatekeeping — it's deliberately occupying different epistemic position.

Additional takeaway: independent testing = different assumptions, risk models, purpose — not just different person.

Additional takeaway: independent testing = different assumptions, risk models, purpose — not just different person.

Additional takeaway: independent testing = different assumptions, risk models, purpose — not just different person.

Reminder: velocity without accountability = unsupervised org — not AI-assisted.

*Ingested: 2026-09-01*
