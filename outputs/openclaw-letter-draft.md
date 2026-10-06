# OpenClaw letter DRAFT (W5, 05.10 — owner sends; DO NOT SEND without owner + W1 sign-off)

**To:** OpenClaw maintainers (via #165043 / #165045 threads or email)
**Status:** draft on W2 GO (packs S4/S5 read from disk; S1-pack missing — marked below, not waited)
**Tone:** peer contributor with repro, PR offer, no pitch

---

Subject: mutation-testing pass over UI e2e — two exhibits, opposite outcomes, pins attached

Hi,

I ran a small mutation-testing pass over your UI e2e suite (two suspicious assertions, one control each) and I'm reporting both outcomes, including the one where your code was right and my claim was wrong.

**Exhibit A — #165043 (agent handle, agent-github-device-authorization ~line 295): coverage effective, my claim withdrawn.**
Pack S4-001: negating the handle-text visibility assertion stayed green across 3 confirmation runs (EQ_NEGATION, B2 provisional, tiers unverified). Your review correctly pointed out the negation can pass during async loading and you couldn't reproduce on main. I ran the stronger control you prescribed: removed the handle render, kept the positive toBeVisible. Result: red on exactly the target test (1 failed / 5 passed), green again after revert (6/6, ~51s). So coverage here is effective and the negated assertion was the weak mutant, not evidence of a gap. Withdrawing the claim as formulated. Pins: baseline 923df36b, mutant 8d866ad, revert c6001b88. (Your build reviewed: 0816aa1b57dc.)

**Exhibit B — #165045 (avatar anchor, session-suggestions ~line 255): gap confirmed, fix direction stands.**
Pack S5-001: negating the `:is(.chat-avatar, .chat-avatar-slot)` visibility assertion stayed green across 3 runs. (Bot review 04.10; reviewed-commit SHA not stated in the visible review text — unlike A, no bot pin claimed here.) Mechanism, not timing: the empty slot satisfies visibility while the avatar is absent, so the assertion cannot tell "avatar rendered" from "slot rendered, avatar missing". Removal control: rendered the slot without the avatar (empty initials, classes preserved) — suite stayed green, 7/7; revert green 7/7 as sanity. The fix direction stands: assert strictly on the avatar image/content rather than the `:is()` wrapper. Pins: baseline c6001b88, mutant 6f92edf0, revert 661af842. Happy to PR the narrowed assertion if that direction looks right.

**Method note (so you can discount correctly):** these are two targeted probes (single-row each, tiers unverified, B2 provisional), not tiered coverage of your suite — don't read them as an audit. The point of the pair is calibration: the same removal control exonerated one assertion and convicted the other, with pins for both, so the instrument demonstrably distinguishes. A third pack (S1) exists but isn't in my hands yet; I'll follow with it separately if material, not bundled.

Thanks for the precise reviews — the stronger-control prescription is what made both exhibits decisive.

— Victor

---

**Pending inserts:** S1-pack marked ABSENT-PENDING (missing on disk; not W3 scope; assembles only from W3-closeout which doesn't exist — don't wait, follow separately only if material). Avatar exhibit 45 COMPLETE (probe closed GREEN 7/7 + revert; chain note: handle-probe revert c6001b88 = avatar baseline — continuous pins across both exhibits).
**Sends:** owner's buttons (threads and/or email per W1 call).
