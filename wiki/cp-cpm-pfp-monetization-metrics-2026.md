# CPM/CPC/PFP — Модели Монетизации для QA

## Определение

Три основные модели монетизации в классифайдах и рекламных платформах. QA-подход к каждой — разный.

## CPM — Cost Per Mille (Cost Per 1000 Impressions)

**Как работает:** Продавец платит фиксированную цену за 1000 показов объявления.

```
Формула: Revenue = (Impressions / 1000) × CPM_Price
Пример: CPM = $10, 5000 показов → $50
```

**QA фокус:**
- Корректность подсчёта показов (не дублировать, не терять)
- Списание средств: точная сумма, правильный момент
- Fraud detection: накрутка показов (боты, click farms)

**Типовые баги:**
- Показ считается дважды при рефреше страницы
- CPM меняется в середине периода, списание по старой цене
- Баннер показан, но не засчитан (ad-blocker, viewability)

## CPC — Cost Per Click

**Как работает:** Продавец платит только когда пользователь кликнул по объявлению.

```
Формула: Revenue = Clicks × CPC_Price
Пример: CPC = $0.50, 100 кликов → $50
```

**QA фокус:**
- Клик засчитывается однократно (double-click не = 2 клика)
- Click fraud detection: боты, autoclick, repetitive clicking
- Viewability: клик засчитан только если объявление было видно

**Типовые баги:**
- Клик засчитывается до показа объявления
- Повторный клик = двойное списание (duplicate event)
- Собственные клики сотрудников = revenue (не отфильтрованы)

## PFP — Pay For Performance (Pay Per Action)

**Как работает:** Продавец платит только когда объявление привело к конкретному действию (продажа, лид, регистрация, установка).

```
Формула: Revenue = Conversions × CPA_Price
Где CPA = Cost Per Action (лид, продажа, подписка)
Пример: CPA = $20, 10 продаж → $200
```

**QA фокус:**
- **Атрибуция:** какой клик/показ привёл к конверсии? Last-click model? Multi-touch?
- **Time window:** конверсия через 1 день vs 30 дней — засчитывается?
- **Fraud:** фейковые конверсии (боты, incentivized traffic)
- **Reconciliation:** revenue в системе = revenue в бухгалтерии

**Типовые баги:**
- Double-charging: одна продажа → два списания
- Атрибуция ошибочная: клик по объявлению A → продажа записана на B
- Time window: конверсия на 31-й день не засчитана, хотя window = 30 дней

## Сравнение для QA

| Аспект | CPM | CPC | PFP |
|--------|-----|-----|-----|
| Сложность тестирования | 🟢 Low | 🟡 Medium | 🔴 High |
| Fraud risk | Low (impressions) | Medium (clicks) | High (conversions) |
| Double-charge risk | Низкий | Средний | Высокий |
| Attribution needed | Нет | Нет | Да |
| QA approach | Validate impression count | Validate click uniqueness | Validate attribution + reconciliation |
| Monitoring | Impression volume anomalies | Click pattern anomalies | Conversion rate, time-to-convert |

## Что тестировать в Avito (classifieds)

| Фича | Модель | QA-check |
|------|--------|----------|
| Продвижение объявления | CPM | Показы = оплачено? |
| Клик по объявлению | CPC | Уникальность клика? |
| Оплата за результат (PFP) | PFP | Атрибуция корректна? |
| VA (Visibility Ads) | CPM | Приоритет показа? |

## Ключевые фразы для интервью

> «CPM — просто: проверить количество показов. CPC — сложнее: нужен anti-fraud и дедупликация. PFP — самый сложный: атрибуция вероятностная, reconciliation обязателен. QA подход к каждой модели — разный, потому что разные точки отказа.»

> «Для Avito (классифайд) — PFP ключевой тренд. Переход от "плати за показы" к "плати за результат" меняет QA: нужны contract tests для атрибуции, golden dataset для reconciliation, мониторинг conversion rate как guardrail.»

## Связанные термины

- **ARPU** (Average Revenue Per User) — средний доход на пользователя
- **CTR** (Click-Through Rate) — % кликов от показов
- **CVR** (Conversion Rate) — % конверсий от кликов
- **ROAS** (Return on Ad Spend) — доход на потраченный рекламный бюджет
- **eCPM** (Effective CPM) — фактический CPM с учётом всех моделей

**Created:** 2026-07-02
