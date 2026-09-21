# QA is Dead: Orchestrating Quality Across AI Engineering Teams - deck transcript

**Authors:** Jay Aigner (CEO, JDAQA) x Ole Lensmar (CTO, Testkube)
**Event:** September 17, 2026 | Philadelphia Distilling | Philadelphia, PA
**Source:** QA-is-dead.pdf (27 slides, image-only, no text layer)
**OCR:** opencode/mimo-v2.5-free (2026-09-21)
**Note:** "For Attendee Use Only. Do Not Distribute."

---
=== SLIDE 01 ===
QA is Dead: Orchestrating Quality Across AI Engineering Teams

a conversation with Jay Aigner, CEO, JDAQA
and Ole Lensmar, CTO, Testkube

JDAQA LLC x testkube

September 17, 2026 | Philadelphia Distilling | Philadelphia, Pa

© 2026 JDAQA LLC. All rights reserved. For Attendee Use Only. Do Not Distribute.
=== SLIDE 02 ===
QA is Dead.

© 2026 JDAQA LLC. All rights reserved. For Attendee Use Only. Do Not Distribute.
=== SLIDE 03 ===
TRADITIONAL SDLC
Where we started
QUALITY DEBT
Velocity steady and quality consistent.

Engineering output
Release velocity
Production incidents
Quality debt

0 20 40 60 80 100

JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC

quality debt

© 2026 JDAQA LLC. All rights reserved. For Attendee Use Only. Do Not Distribute.
=== SLIDE 04 ===
AI SDLC
Where we were, spring 2026
QUALITY DEBT
Velocity is up. Quality is not keeping pace.

Engineering output    Release velocity    Production incidents    Quality debt

100
AI introduced
80

60
quality debt

40

20

0
JAN    FEB    MAR    APR    MAY    JUN    JUL    AUG    SEP    OCT    NOV    DEC

© 2026 JDAQA LLC. All rights reserved. For Attendee Use Only. Do Not Distribute.
=== SLIDE 05 ===
IN CHICAGO IN JULY

The recurring theme was ownership: product, engineering, and validation.

© 2026 JDAQA LLC. All rights reserved. For Attendee Use Only. Do Not Distribute.
=== SLIDE 06 ===
SINCE THEN

Nobody trusts AI to own quality.

© 2026 JDAQA LLC. All rights reserved. For Attendee Use Only. Do Not Distribute.
=== SLIDE 07 ===
Quality is the four things AI can't own.

Trust is missing because these four sit outside what AI can do.

01
Define correct
Deciding what correct even means. AI optimizes to a target. It cannot choose the target.

02
Determine truth
Judging whether the output is actually right, not just green. AI cannot be its own oracle.

03
Own the risk
Accepting accountability for the release. Someone signs their name. AI cannot.

04
Face the unknown
Judgment on the edge case and the adversarial. AI runs the known path; humans imagine the one nobody wrote down.

Automate around them all you want. You cannot **automate them away.**

© 2026 JDAQA LLC. All rights reserved. For Attendee Use Only. Do Not Distribute.
=== SLIDE 08 ===
AGENTIC SDLC
Where we are
QUALITY DEBT
Velocity plateauing. Lack of trust in agentic / AI validation prevents true scalability.

Engineering output | Release velocity | AI test coverage | Production incidents | Quality debt

JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC

AI introduced | today

quality debt

© 2026 JDAQA LLC. All rights reserved. For Attendee Use Only. Do Not Distribute.
=== SLIDE 09 ===
THE SHIFT

Code became "free."
Validation didn't.

© 2026 JDAQA LLC. All rights reserved. For Attendee Use Only. Do Not Distribute.
=== SLIDE 10 ===
THE SHIFT · ENGINEERING TEAM COST

The cost didn't leave. It's moving to validation.

TOTAL ENGINEERING COST · UNCHANGED

QA / Validation
20%

DevOps 6%

Development
56%

Product / UX
18%

TRADITIONAL SDLC
Development is the cost center.

Product / UX Development DevOps QA / Validation

BASIS: SHARE OF ENGINEERING TEAM COST. TRADITIONAL AND AI COLUMNS GROUNDED IN CAPGEMINI WORLD QUALITY REPORT, SONAR 2026 STATE OF CODE (42% AI-ASSISTED), LINEARB PR DATA (AI CODE WAITS 4.6X FOR REVIEW), AND STANDARD STAFFING RATIOS. AGENTIC COLUMN PROJECTED. // JDAQA

The total does not drop. With no agentic QA to absorb it, the cost of trust moves from building the software to validating it.

© 2026 JDAQA LLC. All rights reserved. For Attendee Use Only. Do Not Distribute.
=== SLIDE 11 ===
THE SHIFT · ENGINEERING TEAM COST

The cost didn't leave. It's moving to validation.

TOTAL ENGINEERING COST · UNCHANGED

TRADITIONAL SDLC
QA / Validation 20%
DevOps 6%
Development 56%
Product / UX 18%
Development is the cost center.

AI SDLC
QA / Validation 35%
DevOps 9%
Development 38%
Product / UX 18%
Code gets cheap. Review and testing jam the release.

The total does not drop. With no agentic QA to absorb it, the cost of trust moves from building the software to validating it.

Product / UX Development DevOps QA / Validation

BASIS: SHARE OF ENGINEERING TEAM COST. TRADITIONAL AND AI COLUMNS GROUNDED IN CAPGEMINI WORLD QUALITY REPORT, SONAR 2026 STATE OF CODE (42% AI-ASSISTED), LINEARB PR DATA (AI CODE WAITS 4.6X FOR REVIEW), AND STANDARD STAFFING RATIOS. AGENTIC COLUMN PROJECTED. // JDAQA

© 2026 JDAQA LLC. All rights reserved. For Attendee Use Only. Do Not Distribute.
=== SLIDE 12 ===
THE SHIFT · ENGINEERING TEAM COST

The cost didn't leave. It's moving to **validation**.

TOTAL ENGINEERING COST · UNCHANGED

TRADITIONAL SDLC
QA / Validation 20%
DevOps 6%
Development 56%
Product / UX 18%
Development is the cost center.

AI SDLC
QA / Validation 35%
DevOps 9%
Development 38%
Product / UX 18%
Code gets cheap. Review and testing jam the release.

NOW · AGENTIC
QA / Validation 45%
DevOps 12%
Development 18%
Product / UX 25%
Validation is the expense. Requirements are the leverage.

The total does not drop. With no agentic QA to absorb it, the cost of trust moves from building the software to **validating** it.

Product / UX | Development | DevOps | QA / Validation

BASIS: SHARE OF ENGINEERING TEAM COST. TRADITIONAL AND AI COLUMNS GROUNDED IN CAPGEMINI WORLD QUALITY REPORT, SONAR 2026 STATE OF CODE (42% AI-ASSISTED), LINEARB PR DATA (AI CODE WAITS 4.6X FOR REVIEW), AND STANDARD STAFFING RATIOS. AGENTIC COLUMN PROJECTED. // JDAQA

© 2026 JDAQA LLC. All rights reserved. For Attendee Use Only. Do Not Distribute.
=== SLIDE 13 ===
THE SHIFT · QUALITY DEBT

This is your next year of engineering output.
Quality debt is eating it alive.

# 110 days

Quality debt is on pace to consume

Nearly a third of your engineering year, gone before a single feature ships. Spent on rework, incident response, and manual retesting instead of product.

[Grid visualization: 365 squares representing days of the year, approximately 110 squares highlighted in yellow]

365 days in a year. Each square is one day. // Projection based on current quality debt trajectory.

© 2026 JDAQA LLC. All rights reserved. For Attendee Use Only. Do Not Distribute.
=== SLIDE 14 ===
THE SHIFT

Humans are still needed.
You need them to
own quality.

© 2026 JDAQA LLC. All rights reserved. For Attendee Use Only. Do Not Distribute.
=== SLIDE 15 ===
VALIDATION

What is the human footprint in the AI-SDLC?

© 2026 JDAQA LLC. All rights reserved. For Attendee Use Only. Do Not Distribute.
=== SLIDE 16 ===
THE HUMAN FOOTPRINT · PRODUCT QUALITY

Product Quality

AI can draft the **what**. Only humans decide if it is the right thing, built right for the user.

FUNCTION | AI DOES · SURFACE AREA | HUMAN REQUIRED · TRUTH

**Requirements** | drafts stories and specs | decides what correct means

**Acceptance criteria** | generates the checklist | sets the bar that matters

**User discovery** | clusters the feedback | hears what users won't say

**Prioritization** | suggests a ranking | owns the bet and the cost

**UX and interaction** | generates layouts and copy | judges whether it feels right

**Unhappy paths** | lists the obvious cases | imagines what real users do

**Business rules** | implements as told | confirms the rules match reality

**Accessibility** | flags WCAG basics | validates real assistive-tech use

**Voice and content** | drafts the copy | owns tone, brand, nuance

**Definition of good** | reports the numbers | decides what good means here

**User acceptance** | cannot run it | signs off: this is what we wanted

**Product ethics** | has no stake | owns what it should not do

© 2026 JDAQA LLC. All rights reserved. For Attendee Use Only. Do Not Distribute.
=== SLIDE 17 ===
THE HUMAN FOOTPRINT · ENGINEERING QUALITY

Engineering Quality

AI writes most of the code now. Humans decide whether it is **actually sound**, and own what it cannot.

FUNCTION | AI DOES · SURFACE AREA | HUMAN REQUIRED · TRUTH

Architecture | proposes the patterns | owns the tradeoffs

AI code review | flags known issues | catches hidden assumptions

Complex logic | handles the boilerplate | writes the hard, novel parts

Legacy integration | generates connectors | validates it in the real system

Performance and scale | writes basic load tests | judges real-world capacity

Security | flags known signatures | models the novel attack

Quality-debt paydown | creates debt fast | decides what debt matters

Standards | matches the pattern | defines good for this team

Dependencies | suggests the libraries | owns vendor and license risk

Observability | adds the logging | decides what a real signal is

CI/CD gates | writes the pipeline | owns rollback and environment truth

Velocity vs health | inflates PR volume | judges if the team is healthy

© 2026 JDAQA LLC. All rights reserved. For Attendee Use Only. Do Not Distribute.
=== SLIDE 18 ===
THE HUMAN FOOTPRINT · VALIDATION

Validation

AI expands the surface area: more tests, more coverage. Only humans **determine what is true.**

| FUNCTION | AI DOES · SURFACE AREA | HUMAN REQUIRED · TRUTH |
|---|---|---|
| **Test strategy** | generates the tests | decides what is worth testing |
| **AI test review** | writes what the code does | catches what it should do |
| **The oracle** | checks a given answer | decides the answer itself |
| **Exploratory testing** | runs the known paths | breaks it in new ways |
| **Real devices** | emulates | tests physical, gesture, touch |
| **Perceived experience** | cannot feel it | judges timing and feel |
| **Coverage to risk** | reports the percent | maps it to real risk |
| **Regression** | runs the suite | tells signal from flake |
| **Release go / no-go** | shows the signals | owns the decision and risk |
| **Production failures** | alerts on known signals | reasons through the novel one |
| **Domain validation** | gives a generic pass | confirms it is right for the field |
| **Quality governance** | cannot be accountable | answers to customers and regulators |

© 2026 JDAQA LLC. All rights reserved. For Attendee Use Only. Do Not Distribute.
=== SLIDE 19 ===
VALIDATION · TWO QUESTIONS

Reviewing the code is not testing the software.

CODE REVIEW · THE DEVELOPER
Is the code acceptable?
Reads the diff
Checks style, patterns, obvious bugs
One developer's read of the artifact

VALIDATION · THE QUALITY ENGINEER
Is the software correct?
Runs the system
Behavior, edge cases, integration, real users
Proof it actually works

Strong developers are strong reviewers. That is a different question from "does this work for the user," and being good at one does not make you the answer to the other. Different skill, different moment, different person.

A passing review is **not** a working product.

© 2026 JDAQA LLC. All rights reserved. For Attendee Use Only. Do Not Distribute.
=== SLIDE 20 ===
HOW MANY DO WE NEED?

Size to AI-engineering output, not developer headcount.

( AI + human output × validation per change ÷ quality-engineer output ) + quality infrastructure = quality infrastructure investment

**Quality infrastructure** is the product, engineering, and validation work from the ledgers, the standing footprint on top of per-change validation.

© 2026 JDAQA LLC. All rights reserved. For Attendee Use Only. Do Not Distribute.
=== SLIDE 21 ===
VALIDATION · HOW MANY

Quality engineers needed

Merged pull requests per week (AI + human)

120

Code reviewed and added to the codebase, not yet validated. Pull it from your repo dashboard.

Typical PR size

Small Mixed Large

2–4

quality engineers embedded in your team

120 PRs/week × 30-45 min ÷ 25 hrs/engineer = 2–4

Sizes per-PR validation only; quality infrastructure rides on top. Cross-referenced against LinearB 2026 PR data, Sonar 2026 State of Code, and your bottoms-up requirements map.

© 2026 JDAQA LLC. All rights reserved. For Attendee Use Only. Do Not Distribute.
=== SLIDE 22 ===
TOOLS

© 2026 JDAQA LLC. All rights reserved. For Attendee Use Only. Do Not Distribute.
=== SLIDE 23 ===
HUMANS

© 2026 JDAQA LLC. All rights reserved. For Attendee Use Only. Do Not Distribute.
=== SLIDE 24 ===
STRATEGY

© 2026 JDAQA LLC. All rights reserved. For Attendee Use Only. Do Not Distribute.
=== SLIDE 25 ===
TOOLS + HUMANS + STRATEGY

is how you deliver high quality software at the speed of AI engineering.

© 2026 JDAQA LLC. All rights reserved. For Attendee Use Only. Do Not Distribute.
=== SLIDE 26 ===
ABOUT TESTKUBE

testkube

We power testing at scale, directly inside your Kubernetes infrastructure

testing that moves as fast as your cloud native architecture built for modern teams who care about CI/CD, test automation & GitOps

Testkube is the open testing platform for AI-driven engineering teams. It works with any testing tool, integrates into your workflow, and scales effortlessly

connect with Ole

or visit testkube.io

© 2026 JDAQA LLC. All rights reserved. For Attendee Use Only. Do Not Distribute.
=== SLIDE 27 ===
ABOUT JDAQA

JDAQA

Your strategic partner at the intersection of AI software dev & quality engineering

Putting the humans in place to help you deploy rapidly, ship clean, and lead your engineering org into the future

10+ years designing & building quality systems inside Philadelphia engineering teams

connect with Jay

or visit jdaqa.com

© 2026 JDAQA LLC. All rights reserved. For Attendee Use Only. Do Not Distribute.
