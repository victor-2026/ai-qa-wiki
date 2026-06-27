
**К permanentному решению:**

Вариант 1 — **Git для .obsidian папки:**

```
# Включить .obsidian в git
cd ~/Projects/ai-qa-wiki
git add .obsidian/
git commit -m "Backup obsidian settings"
```

Вариант 2 — **Скрипт восстановления:**

```
# Создай alias для быстрого восстановления
alias obsidian-restore='cp ~/ObsidianBackup/templates.json ~/Projects/ai-qa-wiki/.obsidian/'
```

## ✅ .obsidian уже в git!

**Теперь если сбросится:**

```
cd ~/Projects/ai-qa-wiki
git checkout .obsidian/
```

**Или сделать alias:**

```
echo 'alias obsidian-fix="cd ~/Projects/ai-qa-wiki && git checkout .obsidian/"' >> ~/.zshrc
source ~/.zshrc
```

Потом просто:

```
obsidian-fix
```

## ✅ Создал папку `daily-notes/`

**Настрой в Obsidian:**

1. **Settings → Templates**
    
    - Folder: `daily-notes/` (выбери из списка)
2. **Periodic Notes** (отдельный плагин)
    
    - Daily notes location: `daily-notes/`
    - Template: (выбери шаблон если есть)

---

**Полный путь:** `~/Projects/ai-qa-wiki/daily-notes/`
[[Obsidian-Setup]]