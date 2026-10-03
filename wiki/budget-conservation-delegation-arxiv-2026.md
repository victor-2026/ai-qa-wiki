# Fault-Tolerant Budget Conservation in delegation (arXiv 2610.00349, 2026-09-29)

**Authors:** Genliang Zhu, Chu Wang
**Published:** 2026-09-29 (v1, 67 pages — abstract-level note, full text not pulled)
**Source:** https://arxiv.org/abs/2610.00349
**Status:** research note

## Саммари

Формальная рамка conservation бюджетов при делегации между concurrent/failure-prone воркерами: квантованные resource vectors как exclusive escrow credits через delegation DAG; reservation с lineage/epoch/idempotency key; signed dispatch permit + quarantine; gateway verify до acceptance; uncertain effects charged до settlement/fenced no-effect proof/retirement. Доказаны: ownership partition, ledger/effect conservation, descendant non-amplification, at-most-once settlement, late-completion safety, partition confinement. Проверено: bounded TLA+, JS explorer, crash-injected SQLite; в скоупе — timeout-refund и historical-certificate-validation mutants (sic — mutation analysis внутри).

## Тезис для нас

- **Budget как authorization boundary:** лимиты ресурсов — граница полномочий агентов (рифма с нашим роутингом моделей и guard лимитов в ТЗ).
- **At-most-once settlement для side effects** — формальный ответ на класс "агент сделал дважды" (ср. дубликаты/ретраи в наших пилотах).
- **Idempotency keys + lineage** — тот же словарь, что per-tier evidence (что/кем/когда, воспроизводимо).
- Любопытно: их scope упражняется мутационным анализом — конвергенция формальных методов и mutation testing.

## Связь

- [[testmu-agent-red-teaming-11row-2026]] — R-строки про tool misuse; escrow/idempotency — дизайн-ответ на часть из них.
- **Кросс-волт:** outputs/tz-small-opencode-orchestrator-draft.md — экономика делегации (§4 роутинг, §8 риски).

## Caveat

- Нота по abstract; 67 страниц не читались. Перед цитированием в статьях — вытянуть полный текст.
- Raw не заводился: первоисточник — URL выше.
