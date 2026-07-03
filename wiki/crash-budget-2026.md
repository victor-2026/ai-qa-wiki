# Crash Budget для Mobile Testing

## Определение

**Crash budget** — метрика качества мобильного приложения. Определяет максимально допустимый процент крашей (crash rate) за период (день/неделя/месяц).

```
Crash Budget = 100% - SLA%
SLA = Service Level Agreement (target uptime)

Пример:
SLA = 99.9% uptime (app not crashing)
Crash Budget = 0.1% of user sessions may crash

Если крашей за неделю > 0.1% → релиз блокируется
```

## Почему это важно для mobile

- **Mobile ≠ Web.** Нельзя сделать hotfix за 5 минут. App Store review = 1-24 часа.
- **Device fragmentation.** iOS + Android = тысячи устройств. Невозможно протестировать все.
- **Network conditions.** Mobile работает в unpredictable условиях (3G, offline, roaming).
- **Background processes.** Push-уведомления, фоновые обновления — новые источники багов.

## Crash budget в CI/CD

```
Релизный процесс с crash budget:

1. Новый билд → CI
2. Feature flags → 1% canary
3. Мониторинг crash rate (30 мин)
   ├── Crash rate < 0.1% → rollout 10%
   ├── Crash rate 0.1-0.3% → мониторинг + alert
   └── Crash rate > 0.3% → auto-rollback
4. 10% canary → мониторинг (1 час)
5. 100% rollout
```

## Crash Budget vs Error Budget

| Аспект | Crash Budget | Error Budget (DORA) |
|--------|-------------|---------------------|
| Фокус | Mobile app crashes | System errors/incidents |
| Метрика | % crash rate | % failed requests / downtime |
| Период | День/неделя | Месяц/квартал |
| Инструменты | Crashlytics, Sentry | Grafana, Datadog |
| Применение | Mobile releases | Backend/services |

## Зоны crash rate (mobile)

| Зона | Crash Rate | Действие |
|------|-----------|----------|
| 🟢 Green | < 0.1% | Normal release process |
| 🟡 Yellow | 0.1-0.3% | Мониторинг, alert разработчикам |
| 🔴 Red | 0.3-1% | Блокировка релиза, hotfix |
| 💀 Critical | > 1% | Auto-rollback, incident response |

## Как внедрить

**Week 1:**
- Подключить Crashlytics (Firebase) или Sentry
- Настроить алерты: crash rate > 0.1% → Slack/email
- Определить baseline: текущий crash rate за неделю

**Week 2:**
- Внедрить crash budget gate в CI: если crash rate > threshold → блокировка
- Feature flags для canary rollout

**Month 2:**
- ANR rate (Android: Application Not Responding)
- Time to Interactive degradation
- Screen-specific crash rate (какой экран падает чаще)

## Что сказать на интервью

> «Crash budget — первая метрика, которую я внедряю в mobile. Она объективная, понятная всем (разработчикам, QA, менеджменту) и даёт чёткий критерий: можно релизить или нет. Не гадаем — измеряем.»

## Источники

- Google Play Console: Android Vitals (crash rate, ANR rate)
- Apple App Store: Crash Reports, Xcode Organizer
- Firebase Crashlytics: real-time crash reporting
- Sentry: cross-platform error tracking
- DORA: Error Budget как предшественник Crash Budget

**Created:** 2026-07-02
