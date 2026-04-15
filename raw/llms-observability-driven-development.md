**Source:** [Honeycomb Blog](https://www.honeycomb.io/blog/llms-demand-observability-driven-development)
**Date:** 2023-10-02
**Author:** Charity Majors

---

# LLMs Demand Observability-Driven Development

## The Core Problem

**LLMs are black boxes that produce nondeterministic outputs and cannot be debugged or tested using traditional software engineering techniques.**

## Software vs LLMs

| Software | LLMs |
|----------|------|
| Same input → same output | Same input → may differ |
| Testable, debuggable, reproducible | Not fully testable |
| TDD works | TDD doesn't work |
| Start with tests → graduate to production | Start with production → generate tests |

## Traditional Debugging Limitations

Software is theoretically 100% debuggable, but these chip away at it:
- Concurrency, parallelism
- Multiple abstraction layers
- Randomness
- Weak telemetry/instrumentation

## Why LLMs Are Different

- **Natural language is infinitely more expressive** than programming languages
- Long tail of possible results is very long
- High randomness in edge cases
- Users expect meaningful results everywhere

## Key Insight: Start with Production

> "With software, you typically start with tests and graduate to production. With ML, you have to *start* with production to generate your tests."

Early access programs fail to capture full range of user behavior.

## Hard Truths About LLMs

From Phillip (referenced in article):
- Failure will happen — when, not if
- Users will do unpredictable things
- Ship a "bug fix" → break something else
- Can't write unit tests for this
- Latency is unpredictable
- Early access programs won't help

## Observability-Driven Development (ODD)

Shift from **Test-Driven Development** to **Observability-Driven Development**:

1. Ship sooner
2. Observe results
3. Wrap observations back into development

### Why ODD is Necessary

- Systems are increasingly complex
- Nondeterministic outputs are the norm
- Only way to understand: instrument code + observe in production

### What ODD Requires

1. **Wide events** — capture arbitrary high-cardinality dimensions
2. **Traces** — ordered in time
3. **Ability to break down/group by any dimension**

## Improving LLM Products

Without touching prompt engineering, you can fix:
- Data model mismatches
- Parsing/validation checks

**Only way to improve LLM software ultimately:** Adjust prompt → score outputs → readjust

## What You Need

| For Software Engineers | For ML Engineers |
|-----------------------|------------------|
| Concern about data quality | Learn product development |
| Understand representivity | Focus on user interactions |
| Handle probabilistic systems | Think about business goals |

## The Operating Shift

> "The hardest part of software has always been running it, maintaining it, and understanding it."

AI is turning this upside down:
- Writing software → as easy as sneezing (AI)
- Understanding, operating, maintaining → harder than ever

## Recommendations

1. **Instrument code with intention** — emit useful telemetry
2. **Ship to production ASAP** — use feature flags
3. **Decouple deploys from releases** — gradual rollouts
4. **Look at systems in production** — not just code

## Key Quote

> "The days when you could predict how your system would behave simply by reading lines of code are long, long gone."

## The Gift of LLMs

LLMs might be the **Trojan Horse** that drags teams into modern best practices:
- Testing in production
- Observability-driven development
- Continuous delivery with tight feedback loops

## Related

- Testing AI Systems Overview (ISTQB)
- Monitoring for Vibe-Coded Apps
- Hidden Costs of Vibe-Coded Apps
