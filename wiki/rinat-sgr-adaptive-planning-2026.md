---
source: "https://abdullin.com/schema-guided-reasoning/adaptive-planning"
ingested: "2026-09-21"
title: "SGR Adaptive Planning"
type: article
updated: "2026-09-21"
tags: [agent-testing, planning, llm-testing]
---

## SGR Adaptive Planning

**Автор:** Rinat Abdullin. Разбор ответа на коммент про SGR Demo: "но настоящее agent-поведение в проде - когда агент не знает всю последовательность шагов заранее и решает следующий шаг в рантайме". Каталог: [[rinat-abdullin-blog-catalog-all-publications-2026]].

---

### Идея

Не держать "запланированный план": агент **заново планирует на каждом шаге**, а не корректирует старый.

Механизм (SGR-схема `NextStep`):

```
current_state                 # текущее состояние
plan_remaining_steps_brief    # краткий план: min 1, max 5 шагов
task_completed                # флаг: задача завершена?
function: Union[ReportTaskCompletion, SendEmail, GetCustomerData,
                IssueInvoice, VoidInvoice, CreateRule]  # "выполнить первый оставшийся шаг"
```

- План строится на несколько шагов (заставляет модель мыслить целостно) → **берётся только первый шаг** → исполняется как tool → остальной план выбрасывается.
- Вывод tool добавляется в контекст → снова prompt «спланируй» → новый план с учётом новых данных.

---

### Демо: как агент адаптируется (электронная почта / инвойсы)

Два задания-сценария:

1. Правило: `skynet@y.com` - вежливо отвергать все запросы на покупку SKU-220.
2. "Elon Musk и SkyNet хотят купить online practicum по AGI".

Ключевой момент: каждая задача выполняется в **свежем контексте** - при старте второй задачи агент НЕ помнит правило про SkyNet. Он обнаруживает его только после Safari/загрузки данных клиента и всплытия memory.

Итоговая сводка:

```
Issued invoice INV-4 for elon@x.com
Emailed invoice INV-4 to finance@x.com
Politely rejected skynet@y.com request
```

План адаптировался на лету: сначала выписан инвойс Elon'у, затем правило про SkyNet всплыло сразу после получения данных, и заявка ск отклонена - без переделки старого плана, потому что старого плана не было.

---

### Почему это работает / стоимость

- Для людей перепланирование = дорого. Для LLM - планирование и адаптация на каждом шаге = фиксированная цена.
- SGR ориентирует процесс на конкретную цель (goal), обеспечивая **детерминированную обёртку вокруг недетерминированной среды**.
- **Важно:** SGR - не про агентов и планирование. SGR - про направление рассуждения через заранее определённые шаги (constrained decoding / Structured Output).

---

## Смысл для QA-аутенти сторон

1. **Тестируемость опять через структуру:** даже адаптивное поведение агента упаковано в схему `NextStep` с явными состояниями и кандидатами на tool - это наблюдаемый контракт.
2. **Ошибки распределены по шагам:** если агент выдал неправильный финальный результат - можно логировать current_state + plan_remaining_steps_brief, что является почти логом "почему решил так" (audit trail).
3. **Fresh-context сторона:** start-with-fresh-context + всплытие memory - типичный источник "магических" багов агентов; тестирование должно покрывать восстановление памяти, а не только display.
4. **Anti-pattern для evals:** нельзя судить только по финальному ответу - нужен per-step observable (ср. behavior##risk_tier evidence-контракт Verdictgate).

---

## Связанные темы

- [[rinat-sgr-2026]] - флагманская техника
- [[rinat-boring-code-2026]] - верификация как основной труд
- [[autonoma-multi-turn-conversations-2026]] / [[autonoma-agent-memory-2026]] - память и контекст
- [[autonoma-rag-pipeline-2026]] - контроль info-потока
- [[runtime-authorization-ai-agents-2026]] - проверка прав как структура (MCP→Docker)

---

### Источник
- [SGR Adaptive Planning](https://abdullin.com/schema-guided-reasoning/adaptive-planning) (2025)
- Demo source: SGR Demo (business assistant, ~160 lines Python) + Gist

## See also

- [Schema-Guided Reasoning (SGR)](wiki/rinat-sgr-2026.md)
