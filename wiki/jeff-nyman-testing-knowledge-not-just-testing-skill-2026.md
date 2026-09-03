---
source: "jeff-nyman-testing-knowledge-not-just-testing-skill-2026.md"
ingested: "2026-09-01"
---

## Jeff Nyman - Testing Knowledge Isn't (Just) a Testing Skill

**Summary**
Third post in series `testing as a role, not a person` (2026-09-01, https://testerstories.com/2026/09/testing-knowledge-isnt-just-a-testing-skill/). Prior two posts showed one person interleaving dev/tester roles cheaply. This post asks what happens with two different people who never swap seats: cooperation requires each to already carry the other's discipline as a precondition. Example: retry with exponential backoff + full jitter.

---

## Example - Retry Function

```python
def compute_delay(attempt, base_delay, max_delay, rng): # attempt 1-indexed
    exponential = base_delay * (2 ** (attempt - 1))
    capped = min(exponential, max_delay)
    return capped * rng() # full jitter

def retry_with_backoff(fn, max_attempts=5, base_delay=0.1, max_delay=10.0, sleep=time.sleep, rng=random.random):
    for attempt in range(1, max_attempts+1):
        try: return fn()
        except:
            if attempt == max_attempts: raise
            sleep(compute_delay(attempt, base_delay, max_delay, rng))
```

**Why `sleep` and `rng` are parameterized:** not needed for correctness (production always uses time.sleep/random.random), but needed for testability. Without the tester question `how would anyone verify this without a stopwatch and coin flip?`, tests are slow (real sleep) or flaky via global monkeypatch. Design seam at the place touching outside world.

**Tests:**
- `test_retries_until_success_within_the_limit` - needs only docstring (black-box)
- `test_computes_delay_by_the_exact_formula` - needs algorithm knowledge: pin `rng=1.0` to remove jitter, compute `0.1 * 2**(3-1)=0.4` by hand, catches `2**attempt vs 2**(attempt-1)` off-by-one that black-box would miss

---

## Key Insight

Interleaving = one person switching hats mid-task (cheap). Cooperation = two people never trading seats, but each carrying working knowledge of the other's discipline *before* the work starts.

Take borrowed knowledge away: developer -> untestable function; tester -> suite that agrees with a bug. `Developers should test better` and `testers should understand code` are the same requirement viewed from two chairs.

---

## Our analysis (for Victor)

1. **Testability as design requirement (Quality Operating Model).** The `sleep/rng` seam is the same as Victor's `Trust Scorecard Fragility` - tests that need monkeypatching are brittle. Good engineering anticipates verification shape upfront, not after.

2. **Algorithm literacy for testers = mutation thinking.** Exact-formula test is a manual mutation oracle: knows the off-by-one to target and builds a test that cannot miss it. That's Victor's mutation matrix in miniature - tester must know the fault model, not just the spec.

3. **Supports Article 27 Guided QA Engineer.** QA not re-running checks, but carrying dev discipline to ask `what would an off-by-one look like here?` This is the promoted QA role Ng describes: developer moves up, but the gate stays at the discipline overlap.

4. **Cooperation vs interleaving is Conway for QA.** Article 21 (Conway drain) is the org version of this post's two-person cooperation. If dev and tester each carry the other's discipline, quality knowledge lives at the seam, not in a handoff.

---

## Cross-links
- [Mark Paemaa - Confidence](wiki/mark-paemaa-automated-testing-confidence-2026.md) — confidence vs evidence; tests as production code
- [Ilya Kabanov - Hygiene](wiki/ilya-kabanov-cybersecurity-ai-cost-2026.md) — basic hygiene (seams) vs vendor hype
- [Andrew Ng - Loop Engineering](wiki/andrew-ng-loop-engineering-2026.md) — three loops, evals
- [Article 27 - Guided QA Engineer](../../Articles/linkedin-posts/Quality-Operating-Model/27-guided-qa-engineer.md) — QA promoted, not deleted

---

*Source: Jeff Nyman 2026-09-01 via https://testerstories.com/2026/09/testing-knowledge-isnt-just-a-testing-skill/ and https://lnkd.in/gU8rM_Tx · Ingested 2026-09-01*
