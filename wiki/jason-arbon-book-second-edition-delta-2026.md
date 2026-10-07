# Jason Arbon: Book Second Edition Delta 337 → 488pp (Oct 2026, Verified)

**Source:** how-ai-tests-software-victor-ematin-corrected.pdf (14.4 MB, owner-placed in raw/ 07.10), decrypted with original unlock code, 488 pp / 856K chars. Full text extracted to /tmp/hats2-full.txt and verified 07.10. First edition baseline: book-summary.md (20.09, 337pp) in Positions Jason_Arbon + wiki/jason-arbon-how-ai-tests-software-2026.md.

## Dedication (p2, verbatim key lines)

"For Victor Ematin ... Your feedback arrived in the nick of time and made this version stronger. This copy includes the whole-Harness fault-injection example in Chapter 13, the explicit abstention policy in Appendix D, and a clearer distinction between fast probes and time to a credible decision. ... I owe you! Jason, October 6, 2026". Title page: "First edition". All three incorporations verified in text below — TRUE, not courtesy.

## Structure delta (TOC-verified)

- Parts 9 → 6 (I Find and Verify Problems; II Execute Tests by Intent; III Improve Test Thinking; IV Build the AI Test Harness; V Operate and Improve; VI Where Testing Goes Next).
- Chapters: 33 both editions. Harness block keeps numbers (17-25); self-healing 15 → 11; oracles 9 → 15; white-box 7 → 13. Chapters with no 1st-edition attestation in book-summary (new or heavily reworked): 5 (beyond browser), 12 (failures we avoid), 14 (personas), 16 (devs become testers), 28 (human in AI loop).
- Appendices 4 → 10 (A-J). New: E AI Check Catalog, **F 15 Myths in-book** (intro+closing verified pp424-436; the paywalled Substack myths 5-15 are now inside the book), G crawl/dedupe, H tool-stack change, I cross-surface multi-agent, J CARBON setup.

## Feedback point 1: fault injection / mutation (Ch 13 + spread pp176-180)

- Ch 6 mechanics ref (p153), Ch 13 white-box hosts the whole-Harness example; p87 AI CODING AGENT prompt (reversible seams, prioritized fault set, before/after preservation).
- Meta-testing spread (pp176-180): "Mutation testing asks whether the suite detects deliberately changed behavior"; allowlist of operators predeclared + independently verified; harmless changes (rename/ID) included as clean controls; report by consequence tier incl. inconclusive runs, invalid mutations, false alarms on clean controls, **review effort**, detection time; frozen repeats with variation (no best-run picking). "Keep the denominator and scope visible" (p176). "A green dashboard is a claim produced by a model of the product. Test that model." (p179).

## Feedback point 2: abstention policy (Appendix D, p375)

Consequence-tier policy: evidence + minimum decision margin per tier, validated on held-out labeled examples; no invented thresholds (evidence sufficiency gates instead); policy version preserved with every verdict. Near-tie protocol: preserve full distribution + model + requirements + before/after; mark unresolved (never silently accept winner); deterministic assertion check; reproduce from clean state; escalate to stronger model/person when justified. Ch 13's mutation exercise referenced as the loop-level test.

## Feedback point 3: fast vs credible (pp376-377)

"Do not chase fast for fast's sake. Measure time to a credible finding or a supported decision, including false alarms, missed problems, retries, and human follow-up." TestBucks 63 probes/24.3s = throughput, NOT comparative time-to-decision. Honest experiment design proposed (human vs scripted vs fixed/random vs AI harness, same baseline/faults/evidence standard) — explicitly "does not establish the size of that advantage".

## New lines worth banking

- "Instructions are not a sandbox." (p434, containment: enforce outside the prompt)
- "A green dashboard is a claim produced by a model of the product. Test that model." (p179)

## See also

- [[jason-arbon-how-ai-tests-software-2026]] — first-edition note
- [[typesafe-jev-judgment-service-gates-2026]] — Appendix D Jev material, Jason hands-on relay
- W1 FYI: arc closed 07.10 (feedback → incorporated → verified → close-out SENT); track warm standby.
