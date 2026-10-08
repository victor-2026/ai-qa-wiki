# NIST TEVV-Athlon Framework (AI 200-2 ipd, Aug 2026)

**Source:** NIST AI 200-2 ipd (Initial Public Draft, Aug 2026, 41pp, DOI 10.6028/NIST.AI.200-2.ipd). Authors: P.J. Phillips, T. Jensen, P. Hall et al. PDF text extracted (/tmp/tevv-athlon.pdf), TOC + abstract + key sections verified 08.10. Via Klain AI Testing & Assurance group (public comment CLOSED per Klain post). PDF: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.200-2.ipd.pdf

## Core construct

TEVV-Athlon = an assessment where AI systems are tested via **Events** and **Tools** producing data on **Blocks** (measurement concepts of interest). Four stages: **Articulate & Organize → Define & Construct → Apply & Measure → Synthesize & Interrogate**. Worked example: Query-Violation Problem (§3). Guidance: expertise gathering, toolbox composition (model testing §4.3.1 + realistic settings §4.3.2), scientific measurement practices, validating measurement (§4.5).

## Points for our lane

- **Goodhart named in-paper (§4.6 + body):** optimizing for benchmark performance → passes tests, fails deployment. Remedy prescribed: in-house/application-specific benchmarks + complementing model tests with real-world-condition testing. Vendor-independent backup for our denominator/benchmark-skepticism language.
- **Toolbox appendices:** A benchmarks, B red-teaming methods, C user/field testing, D measurement science, E experimental design. Ready reference list for eval-design work.
- **Validating measurement as a stage** (§4.5 + Synthesize & Interrogate): measurement itself gets interrogated — pairs with judge calibration + abstention doctrine.
- Status: initial public draft, comment closed. Track final publication.

## QA interpretation

Federal vocabulary converging on ours: custom assessments per org objectives (not one-size benchmarks), measurement-of-measurement, Goodhart explicitly. Cite as standards-track backup in Articles 26/29 (regulator-recognized language, same family as Breaklight's NIST AI RMF mapping).

## See also

- [[breaklight-ai-testing-methodology-whitepaper-2026]] — NIST RMF mapping, reference-set hygiene
- [[brijesh-deb-testable-oversight-2026]] — NIST RMF 1.0 caveat (2023, under revision)
- [[kenhuang-maestro-google-control-roadmap-2026]] — 12 red-team categories (Toolbox B neighbor)
- [[swe-proof-machine-checked-proofs-2026]] — green suite ≠ correctness
