# data-testid в React: как QA добавлять атрибуты в компоненты

**Источник:** Yulia Sergeeva, LinkedIn (2026-07-08)

Как QA инженеру самостоятельно добавить `data-testid` в React-компонент — без согласования с разработчиком на каждый чих.

## Проблема

Хрупкие XPath и текстовые селекторы — источник flaky тестов. Решение: добавить `data-testid` в компонент. Для этого не нужно быть React-разработчиком — достаточно понимать 3 шага.

## Механика: Component Props vs DOM Attributes

| | Prop Name (TypeScript) | DOM Attribute (браузер) |
|---|---|---|
| Формат | `dataTestId` (camelCase) | `data-testid` (kebab-case) |
| Где живёт | В аргументах компонента | В готовом HTML |

## 3 шага для кастомного компонента

Если компонент оборачивает нативный HTML-элемент:

```tsx
// 1. Добавить prop в интерфейс
interface ButtonProps {
  dataTestId?: string;
  children: React.ReactNode;
}

// 2. Деструктурировать в аргументах
export const Button: React.FC<ButtonProps> = ({
  dataTestId,
  children
}) => (
  // 3. Привязать к нативному элементу
  <button data-testid={dataTestId}>
    {children}
  </button>
);
```

## Как быстро найти компонент в коде

| Что ищем | Где искать | Как |
|---|---|---|
| Страницу | `routes.ts` | Поиск по URL → Resolver → компонент |
| Sidebar/Modal/Drawer | Глобальные хуки | Найти trigger ID → глобальный поиск |
| Определение компонента | Весь проект | Поиск по ID с закрывающей скобкой: `"SidebarIds.batchEdit}"` |

## Итог

5 минут на добавление `data-testid` — и тесты перестают ломаться от изменения текста кнопки или CSS-класса.

---

*Добавлено: 2026-07-08*
