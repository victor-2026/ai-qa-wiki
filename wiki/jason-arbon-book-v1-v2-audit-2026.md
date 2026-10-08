# Jason Arbon: v1 → v2 TOC Table + Proposal Audit (07.10, Verified in Text)

**Sources:** v1 PDF (337pp, 20.09, /tmp/hats1-full.txt) + v2 corrected PDF (488pp, raw/how-ai-tests-software-victor-ematin-corrected.pdf, /tmp/hats2-full.txt). Proposals: messages/draft-feedback-2026-09-20.md (Positions Jason_Arbon). Method: TOC extraction + keyword-anchored diff (counts + contexts, not impressions).

## 1. TOC v1 → v2 (chapter mapping)

v1: 9 parts, 33 chapters. v2: 6 parts, 33 chapters. Move = pure reorder: old Part III (7-10) and old Part IV (11-16) swapped blocks + renumber; harness block 17-25 and tail 26-33 untouched in numbering.

| v1 | v2 | Title (stable) |
|----|----|----------------|
| P-I: 1, 2 | P-I: 1, 2 | Evidence / Crawl |
| P-II: 3, 4, 5, 6 | P-II: 3, 4, 5, 6 | Drive / Whole system / Beyond browser / APIs |
| P-IV: 11, 12, 13, 14, 15, 16 | P-II: 7, 8, 9, 10, 11, 12 | Intent record / Triage / Legacy upgrade / AI-first shape / Self-healing / Failures-we-avoid |
| P-III: 7, 8, 9, 10 | P-III: 13, 14, 15, 16 | White-box / Personas / Oracles / Devs-become-testers |
| P-V: 17-25 | P-IV: 17-25 | Harness block (unchanged numbers) |
| P-VI: 26, 27, 28; P-VII: 29, 30 | P-V: 26, 27, 28, 29, 30, 31 | Ten-minutes / Feels-wrong / Human-loop / Leaderboards / Price (+31 Transformation absorbed from old P-VIII) |
| P-VIII: 31 | (in P-V) | Transformation (moved, not dropped) |
| P-IX: 32, 33 | P-VI: 32, 33 | Future / Inside software |

Appendices 4 → 10: A-D kept; new E (AI Check Catalog), F (15 Myths in-book), G (crawl/dedupe), H (tool-stack change), I (cross-surface multi-agent), J (CARBON setup). Forewords: Whittaker kept; PH/JC placeholders gone (resolved or cut — not verified which).

## 2. Proposal audit (what got in, what did not)

### P1 — mutation-based proof layer: IN, as systematization (not creation)

- **v1 baseline (present, fragmented):** p160 already held the core paragraph nearly verbatim ("green dashboard is a claim... Mutation testing asks whether the suite detects deliberately changed behavior. Seeded defects measure whether the full loop notices known failures"). Action classes incl. "reversible local mutation" at p229. Ch 16 + Ch 6 fault-injection mechanics existed. Missing: operators, tiers, reporting discipline ("consequence tier" = 0 hits; "review effort" only in unrelated7-minutes context).
- **v2 addition:** pp176-180 spread (predeclared operator allowlist + independent verification; harmless rename/ID changes as clean controls; reporting by consequence tier incl. inconclusive/invalid/false-alarms/**review effort**/detection time; frozen repeats, no best-pick) + Ch 13 whole-Harness example + App D back-ref ("Chapter 13's mutation exercise tests the broader evidence-gathering loop"). "Consequence tier" 0 → 2.
- **Verdict: IN (elevated fragments → method).** Our exact vocabulary partially adopted: tiers + review effort yes; "mutate the product" phrasing no (book uses industry "mutation testing"); per-test-case rotation NOT named — canonical operator list still open. (Correction 08.10: no operator enumeration here — paused-track hygiene.)

### P2 — near-tie abstention as policy: IN, fully

- **v1 baseline:** App D p334 anecdote only (0.49/0.47, "did not have an abstention rule... weakness in the harness"). "Decision margin" = 0 hits; "abstention" = 1.
- **v2 addition:** p375 named consequence-tier abstention policy (evidence + minimum decision margin per tier, held-out validation, no invented thresholds, versioned policy) + 5-step near-tie protocol (preserve distribution, mark unresolved, deterministic check, clean-state reproduce, escalate). "Abstention" 1 → 5, "unresolved" 18 → 28.
- **Verdict: IN, verbatim promotion anecdote → policy as proposed.** Dedication confirms intent.

### P3 — fast-for-whom comparison: IN as protocol, NOT as results

- **v1 baseline:** Ch 30 time-to-credible (1 hit) + App D no-comparison caveat ("did not compare... fixed sequence, random exploration, simple coverage rule").
- **v2 addition:** p377 explicit comparative design (human exploration vs scripted vs fixed/random vs AI harness; same baseline/faults/environment/evidence standard; TestBucks risk set) — immediately followed by honest disclaimer ("does not establish the size of that advantage"; 63/24.3s = throughput).
- **Verdict: HALF-IN.** The question is now asked in-book with a protocol; the answer (measured comparison) still does not exist. This is the open door.

## 3. Remarks / additions (open items for next round or our pilots)

1. **Run the comparison (P3 remainder):** the in-book protocol is executable by us — TestBucks-style risk set × our seeded breaks × human/scripted/random/AI arms. Offer pilots' numbers if Jason wants them; otherwise our own publication cites his protocol.
2. **Canonical operator allowlist is still vacant:** book says "predeclare a small allowlist" without publishing one. Any contribution from our side = W1 decision (paused-track hygiene); no enumeration, no offer from here.
3. **Margin validation burden:** "validated on held-out, independently labeled examples" is prescribed with no tooling. W2 mini-jev seeded check (narrow-margins rule) is an independent implementation of exactly this — loop back as evidence it is buildable.
4. **Review effort metric (p180)** matches the Megi dimension — flag for Articles (mutation-matrix-full line).
5. **Myths 5-15 freed from paywall** via Appendix F — quote-bankable on next digest pass if needed.
6. **No action:** foreword placeholders, title "First edition" (published state), dedication on file — arc closed, warm standby holds.

## See also

- [[jason-arbon-book-second-edition-delta-2026]] — delta summary
- [[jason-arbon-how-ai-tests-software-2026]] — first-edition note
- [[typesafe-jev-judgment-service-gates-2026]] — App D / Jev material
