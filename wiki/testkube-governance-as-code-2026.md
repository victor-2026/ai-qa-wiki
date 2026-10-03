# Testkube Governance as Code (2026-09-24, Sonali Srivastava)

**Source:** https://testkube.io/blog/ai-generated-code-governance-as-code
**Status:** vendor blog (Testkube pitch second half); method part separable. Via Rudolf Groetz post.

## Саммари

Governance как версионированный/тестируемый код: правила compliance бегут на каждом этапе входа AI-артефакта. Два слоя: build-time (PR: k6/TLS 1.2+, блок merge со structured result) и deploy-time TestTriggers (K8s-события без пайплайна: Deployment/image/ConfigMap → валидация живого endpoint). Evidence — побочный продукт enforcement (timestamped, versioned — SOC 2 II continuous + EU AI Act 8–15). Тезис: "AI-generated code rarely fails unit tests" — политика нарушается тихо.

## Наши зацепы

1. **Pre-agreed rules + evidence-as-byproduct** — дословно наша связка (правила до, evidence из прогона).
2. **Deploy-time слой** — дрейф конфига мимо CI: нового у нас в явном виде не было, забрать как дополнение к gates (гейт на кластер, не только на пайплайн).
3. **"Rarely fails unit tests"** — их формулировка нашей проблемы silent green (проходит, но врет).

## Связь

- [[ai-qa-tool-evaluation-mutation-matrix]] — pre-agreed rules как вердикты; deploy-time drift — кандидат в seeded-класс.
- [[testmu-agent-red-teaming-11row-2026]] — compliance checks рядом с adversarial строками.
- Testkube blog уже в дайджесте (RSS) — следующие посты придут сами.

## Caveat

- Вторая половина — питч Testkube (control plane, Runner Agents). Методология отделима.
- Raw не заводился: первоисточник — URL выше.
