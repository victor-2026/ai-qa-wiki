# Sergey Yudin: Neurolegal (verified citations), HSE AI Leaders program (Yandex)

Source: LinkedIn posts by Sergey Yudin (Technical Director of Professional AI Services - Yandex), ~2025-2026. Projects: Neurosupport (customer support automation), Neuroexpert (info retrieval from files/links), Neurolegal (legal AI assistant).

---

## 1. Neurolegal launch - turning user fear into a feature (post, 8mo)

Launch of Neurolegal (neurolegal.ya.ru), Yandex service on Alice AI.

Context: 2023 US case - a lawyer used ChatGPT for court documents, which generated nonexistent court decisions. Cost him his license. The fear: technology could not provide the needed quality level.

Result:
- 75% of Yandex legal department employees use Neurolegal
- Lawyers from other companies send enthusiastic feedback

Key insight (own words): "Any user fear and failure of the past approach can be turned into an advantage. We spent a lot of time making sure all cited court practices are confirmed by links. Now lawyers use our tool including to double-check their own decisions. It seems so simple now, but a year ago we saw a blocker in this problem."

## 2. Three B2B projects (post, 1yr)

Started B2B direction of YandexGPT more than a year ago, developing several startups:
- Neurosupport (https://lnkd.in/ekGE_-sm) - automates customer support
- Neuroexpert (https://lnkd.in/eBB5gn_r) - finds needed info in files and links
- Neurolegal (https://lnkd.in/eqbj4kAZ) - helps answer legal questions

Hiring ML developers, data analysts, Go/Python developers, and leaders for several directions.

## 3. HSE AI Leaders program (post, 5mo)

With HSE CS faculty (ФКН ВШЭ): six-month AI program for company leaders (https://aileaders.hse.ru/). Goal: teach company executives to apply AI. Also looking for invited teachers with practical experience.

## 4. YaC (Yet another Conference) 2025 AI Edition (post, 7mo)

Sergey was a host at Yandex annual conference; materials at https://lnkd.in/d-FMeUER

## 5. YandexGPT spellchecker in browser (post, 1yr)

Full LLM-based spellchecker in Yandex browser text editor: understands where an error is vs author's style.

## 6. Taimuraz Tibilov (repost, 5mo) - ML-analyst vacancy for Neurolegal

Head of ML analytics in B2B AI services of Yandex, looking for data analyst / ML-analyst for Neurolegal:
- Work with a large team of legal experts; critical to deeply understand current product quality and development direction
- Improve existing approaches to ML pipeline quality evaluation, create new more scalable and specialized ones
- Build tools for ML team and PM to quickly and effectively evaluate quality of various product components and configurations
- Build an internal legal benchmark (сборка внутреннего юридического бенчмарка)

---

## Why this matters for QA (analysis notes)

- Verified citations pattern: hallucination mitigation by design - every legal practice must have a link. QA angle: traceability requirement (cite source or reject). Directly relevant to LLM testing (hallucination detection), guardrails, and evidence layer. Similar to RAG groundedness checking in support dialogues (Yandex Crowd Habr article).
- Internal legal benchmark + quality evaluation of ML pipelines (Tibilov) = golden dataset pattern for domain-specific LLM eval. Legal domain = high-risk regulated domain, parallel to GxP/FDA in clinical (Castor), ISO 27001.
- "Lawyers use the tool to double-check their own decisions" - the tool became a verification layer for humans, not replacement. Same "checking" theme as Pavel Shcherbinin posts.
- HSE AI Leaders program - education of executives on AI; networking potential for QA leadership positioning.