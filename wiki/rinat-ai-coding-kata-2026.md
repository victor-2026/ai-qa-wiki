---
source: "https://abdullin.com/ai-coding/kata-1/"
ingested: "2026-09-21"
title: "AI+Coding Kata (2025)"
type: article
updated: "2026-09-21"
tags: [ai-coding, spec, testing, kata]
---

## AI+Coding Kata (2025)

**Автор:** Rinat Abdullin, серия "AI Coding". Каталог: [[rinat-abdullin-blog-catalog-all-publications-2026]].

---

### Идея

AI + Coding приносит пользу на задачах прототипирования, рассуждений и поиска багов. Katа - упражнение: реализовать парсер "BizDocumentAI" по спеке, использовать любые инструменты (без ограничений; небольшой pydantic-каркас в условии). "Ваша команда будет поддерживать этот код годами - сделайте тщательно".

---

### Spec-driven тест-сьют

Главная фишка: **сам документ-спека - это и есть тест-сьют**. Описание формата является комментарием ```документа, а ожидаемый JSON - тестом.

Ключевые элементы:

1. **Empty text** → пустой root block `{"kind": "block"}`
2. **Body** - обычный текст; пустые строки стрипаются
3. **Head** - `<head>...</head>`
4. **Nested blocks** - `<block>...</block>`
5. **Dictionary** - `<dict sep=":">` key: value (сепаратор настраивается, ключи могут иметь пустые значения)
6. **Lists** - `<list kind=".">` ordered, `<list kind="*">` bulleted; вложенность авто-детектится по номерам (`2.1.`), bullet с `o`; mixed-списки через вложенные теги; "тело" списка = контент, не матчящий префикс
7. **Pydantic-модели** с `kind` Literal, forward references внутри Union

Код-адmonitions всегда парные (input → json). Парсер должен выдавать структурно-похожий JSON для каждого входного документа.

---

## Значение для AI QA

1. **Тесты-как-спека:** единый источник истины. Это vs "SDD-мёртвые спецификации" из [[rinat-abdullin-bdd-vs-sdd-ai-native-harness]].
2. **Проверка структурного подобия** (не точного совпадения) - правильный soft-assert для JSON-сравнения (ср. [[autonoma-non-deterministic-outputs-2026]]).
3. Kata-среда = удобная плоскость для mutation: сломай парсер → выживший тест = зона риска. (Parser - детерминированная составляющая AI-пайплайна.)
4. **Человеческий тест-дизайн важен** даже для AI-кода: спека пишется людьми, ко дет декомпозируется агентами.

---

## Связанные темы

- [[rinat-boring-code-2026]] - та же серия; верификация = основной труд
- [[rinat-abdullin-bdd-vs-sdd-ai-native-harness]] - BDD как AI-native harness
- [[rinat-sgr-2026]] - структура как контракт
- [[fault-injection]] skill - мутации строк/структур

---

### Источник
- [AI+Coding Kata (2025)](https://abdullin.com/ai-coding/kata-1/) (Published April 06, 2025)

## See also

- [We Never Wanted Human Code](wiki/rinat-boring-code-2026.md)
