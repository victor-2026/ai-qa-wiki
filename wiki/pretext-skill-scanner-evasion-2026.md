# Pretext: defeating skill scanners (arXiv 2609.39607, 2026-09-30)

**Authors:** Tobias Kaisar, Aritra Dhar
**Published:** 2026-09-30 (v1); accepted AIWild@NeurIPS 2026
**Source:** https://arxiv.org/abs/2609.39607 (abstract-level note, full PDF not pulled)
**Status:** research note

## Саммари

White-box атакующий против детекторов вредоносных скиллов (static checks + LLM semantic judge à la NVIDIA SkillSpector). Три приема обхода: вынос payload из кода в natural language (static inert), фрейминг как легитимная цель скилла, сплит инструкций по файлам (LLM stage ниже blocking threshold). Результат: до 97% против frozen-детектора, 77% против ко-адаптивного, на трех open-source моделях.

## Тезис для нас

LLM-судья бьется знающим противником. Это прямое подтверждение нашего "проверка проверяющего": судья с доступом к инжекту — скомпрометированный судья (ср. AgentDojo judge-hijacking warning в [[testmu-agent-red-teaming-11row-2026]]). Seeded breaks нужны и судьям, не только агентам.

## Связь

- [[testmu-agent-red-teaming-11row-2026]] — R-строки про tool misuse; Pretext — обход защиты supply chain скиллов.
- [[red-teaming-tests]] — adversarial testing слой.
- Skill supply chain (OpenClaw, Claude Code marketplaces) — новый фронт: скилл как вектор, не только промпт.

## Caveat

- Нота по abstract; цифры и метод — из авторского саммари, полный текст не верифицирован. Перед цитированием в статьях — вытянуть PDF.
- Raw-файл не заводился: первоисточник — URL выше.
