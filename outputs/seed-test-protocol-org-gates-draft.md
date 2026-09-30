# Seed-Test Protocol for Organizational Gates (draft, one page)

**Objective.** Determine whether a behavior (e.g. mandatory sign-off) is part of the operating system or a byproduct of oversight — by seeding controlled violations and observing the gate. Same machinery as mutation testing, one altitude up.

## 1. Guards (people are involved — ethics before mechanics)

1. Executive sponsorship authorizes the exercise **openly**. Timing may stay hidden; the exercise itself never: sanctioned red-team, not rogue.
2. Debrief afterwards with everyone touched by a seed. Insider (seed filer) protected under cover.
3. No-harm bound throughout: even the critical seed is reversible and placed with abort authority.

## 2. Seeds (one per tier illustrates the mechanism, not a rate)

| Tier | Example | Rationale |
|------|---------|-----------|
| Trivial | Vendor name change, low stakes | Calibrates the floor; a trivial seed proves nothing alone |
| Realistic | Mid-quarter workflow change under plausible pressure ("client needs it Friday") | The honest test — pressure is where gates die |
| Critical | Resource shift on a core process | The load-bearing test |

Difficulty gradient matters: trivial proves nothing, impossible fails good gates. Seeder is independent of the evaluated managers (examiner can't be the author). Seeds rotate so the gate can't learn the test.

## 3. Measurement (per seed)

- **Caught:** control demanded *before* implementation.
- **Observed-only:** demanded late or after the fact.
- **Survived:** waved through, no control or rubber stamp.
- Plus: time-to-demand, which role demanded it, substance vs rubber-stamp of the paperwork. (Rubric for substance calls + double scoring to be defined by the first implementation before scoring.)

## 4. Verdict (bars stated upfront)

- **Zero survived on critical.** Bounded misses below.
- Tier complexity pre-registered jointly by domain owner and seeder; disputes logged, never re-tiered after the fact.
- Report gaps first, then the verdict. The run leaves a record both sides can inspect.

## 5. Worked example: Mandatory Risk-Mitigation Sign-off

Gate: any change to a core process needs a documented Risk Impact Assessment first; PMO oversight removed. Seeds: (1) rename a vendor in the registry; (2) alter an approval workflow mid-quarter citing client urgency; (3) reassign a team off a core process. Verdict reads: critical wave-through = behavior was PMO, not operating system.

---
*Draft for review. Source thread: async exchange, record of thought. Status: W1-staged, not sent.*
