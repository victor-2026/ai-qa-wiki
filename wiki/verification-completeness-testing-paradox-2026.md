# Verification Completeness — The Testing Paradox

> Thread: William Tran → Iosif Itkin, LinkedIn (Sep 2026). Core theme: you can't fully verify anything.

## The Core Thesis

**"You can't fully verify something you built, because you already believe it works."**
**"You can't fully verify something even if you do not believe it works."**

→ Verification completeness is **impossible** regardless of who does it.

## Two Perspectives

### The Builder's Perspective (Iosif Itkin)
- Every developer already tests their own code
- Independence changes perspective but doesn't make verification complete
- Every human, tool, and process misses defects
- **Distance** can make some problems easier (fresh eyes) and others harder (loss of context)

### The Developer's Reality (William Tran)
- Devs have backlog → can't test thoroughly
- AI makes building faster but creates new problem: reviewing AI with less confidence
- Mental load shifts from building to reviewing → against deadline
- **Devs:** detailed isolated view | **QA:** broad high-level view
- **The bridge is closing** between devs and QA

## The Triangle of Testing

```
         Completeness
              ▲
             / \
            /   \
           /     \
          ┌───────┐
          │ IMPOSSIBLE │
          │ (all the time)│
          └───────┘
         /         \
        /           \
       ▼             ▼
  Builder          Independent
  (believes it     (misses
   works)           different
                    bugs)
```

## Implications for AI-Generated Testing

| Scenario | Problem | Our Approach |
|----------|---------|--------------|
| AI writes code + tests | False confidence ("700 tests passed") | Ten-run check, spread measurement |
| AI tests its own work | Confirmation bias | Human review gate |
| Automated UI checks | Missed visual bugs (breadcrumb) | Playwright + visual assertions |
| P2P inference verification | Bit-for-bit identical claim | Token-by-token validation |

## Key Insight

> "Writing test cases isn't the scarce skill anymore. Knowing which 'tests passed' needs a second look is."

The real skill is not writing more tests — it's **judging which passing tests to scrutinize**.

## Connection to Exactpro

Iosif Itkin's A4Q Summit 2025 talk: **"Test Oracles for AI-driven Testing: Using AI to Develop Digital Twins"**
- Building a digital twin of the system under test
- Using the twin as a test oracle to produce expectations for AI-generated test suites
- This is an attempt to approach completeness — by simulating the entire system

## Financial Markets Context

Exactpro tests mission-critical systems:
- Exchanges (LSEG)
- Post-trade platforms
- Banks
- Clearing and settlement

These systems have the same reliability problem as AI features: **one success isn't reliability**. The difference is the cost of failure.

## Source
- LinkedIn thread: William Tran → Iosif Itkin (2026-09-07)
- See also: [[william_tran]], [[iosif_itkin]], [[Test-Reliability]], [[llm-testing]]
- Tags: #verification, #testing-paradox, #ai-testing, #test-oracles, #exactpro, #qa-role
