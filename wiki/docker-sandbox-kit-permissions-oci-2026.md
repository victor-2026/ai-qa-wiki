# Docker Sandbox Kit: permissions as OCI images (spec v3 → CNCF, 2026-10-02)

**Source:** https://www.infoq.com/news/2026/10/docker-sandbox-ai-agent/ (Claudio Masolo, via Docker blog + WeAreDevelopers 24.09)
**Spec:** Apache 2.0, v3, repo `docker/sandbox-kit-spec`, `sbx` CLI; announced for CNCF (acceptance level TBD)
**Status:** spec live, portability unproven

## Саммари

Набор прав AI-агента как переносимый артефакт: агент + тулзы + типизированный список запрошенных хостов/credentials/volumes в обычном OCI-образе (без custom media type — `docker buildx build` / `pull` / scan / sign работают как есть). Пининг digest пинит контент и права вместе.

## Механика (наш угол: enforcement материализованный)

- **Typed versioned capabilities:** `com.docker.sandbox/network-policy@2`, `com.docker.sandbox/credential@1`. Пример: `api.github.com` разрешен, но `DELETE /repos/**` запрещен — deny wins.
- **Proxy-managed credentials:** внутри песочницы только sentinel; реальный токен инжектит рантайм на именованные домены.
- **Kit просит, хост решает:** без conforming runtime аннотация инертна; невыполнимый запрос = отказ в запуске.
- **Mixins:** workload Kit + overlay-миксины по графу `provides/requires`; конфликты — ошибки; network rules union'ятся.
- **Normalized grant sets:** рантайм пишет множество грантов и стопает версии, которые его расширяют — включая снятие deny-правила. Gate на widening permissions из коробки.
- **Conformance suites:** две (артефакты + рантаймы). Соавторы: AWS, Box, Datadog, Snyk, Palo Alto и др.

## Оговорки

- Conforming runtime пока один (Docker Sandboxes на microVM) — переносимость между рантаймами не продемонстрирована.
- Descriptor grammar + семантика capabilities новые, требуют изучения; enforcement целиком на рантайме.
- CNCF-приемка (программа/уровень) не подтверждена.

## Связь с нашими темами

- **Permissions как reviewable artifact** против grants в shell-history/дашбордах/памяти — та же граница, что evidence vs claims: проверяемое vs рассказанное.
- **Deny wins + gate на widening** — per-tier policy в инфраструктурном виде (ср. [[ai-qa-tool-evaluation-mutation-matrix]]: B0 zero, запрет на расширение без решения).
- **Proxy credentials / sentinel** — least-privilege паттерн для агентских тулов (ср. guards в [[testmu-agent-red-teaming-11row-2026]]).
- **Кросс-волт:** outputs/tz-small-opencode-orchestrator-draft.md — enforcement-границы (§8); вебинар Episode 2 ("enforcement inside agent tooling isn't a boundary") — Kit отвечает именно на это: граница в рантайме, не в тулзе.

## Relevance

- Wiki-ценность: первый в базе спекоуровень permission boundaries (не вендор-питч, а Apache-спека в CNCF) — референс для разговоров про enforcement.
- Outreach-ценность: цитируемый industry-стандарт в тредах про границы (Пол/governance, Доути/evidence).

## Caveat

- Raw не заводился: первоисточник — URL выше.
