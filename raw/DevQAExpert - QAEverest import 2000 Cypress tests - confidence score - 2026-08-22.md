# DevQAExpert — QAEverest: Import for 2,000 Cypress Tests and Confidence Score

**Source:** LinkedIn — DevQAExpert Solution Private Limited / QAEverest — https://www.linkedin.com/company/devqaexpert/posts/
**Post age at capture:** 3d (captured 2026-08-22)
**Company:** DevQAExpert Solution Private Limited (QAEverest.ai)
**URL in post:** https://lnkd.in/d5jA9b2P

## Full excerpt (as captured)

The demo always goes well.
Story in, test cases out, everyone nods. Then someone asks the question that ends the meeting:

"So what happens to our 2,000 Cypress tests?"

For most AI testing tools, the honest answer is: nothing. They stay where they are. You run two suites, or you spend two quarters rewriting. That's the real reason teams who want this stall.

And starting fresh throws away more than code. Somewhere in that repo is a test asserting that the discount recalculates after the shipping method changes, not before. Nobody wrote that in a spec. It's there because it broke in production in 2023 and someone had a bad Thursday.

Your suite is the most accurate record of how your product actually behaves. Most of it exists nowhere else.
So we built the import, not the rewrite. QAEverest reads your tests and the page objects they call, then hands back editable test cases with a confidence score on each. Some will be wrong — which is why nothing runs until you've reviewed it.

Bring the suite with you.
What's in your oldest test that isn't written down anywhere else?

## Why save this
- Answers the `brownfield` objection: teams stall because AI tools ignore the existing 2,000-test suite
- Positions existing suite as `most accurate record of actual behavior` (tribal knowledge not in specs)
- Import claim: reads tests + page objects → editable test cases **with confidence score each**; **nothing runs until reviewed** (human gate)
- Complements the maintenance-tax post: first explains `why runtime intent`, second explains `how to bring existing coverage`
- Directly relevant to Rupesh Kabra thread: import is semantic migration (not running original Playwright), old locator overwritten without history, confidence internal vs report

## Capture note
Saved as fair excerpt for wiki ingestion. Full post includes image.
