#!/bin/bash
# Weekly backup+lint — runs Sunday 21:00, with catch-up if laptop was off
# Called by launchd com.aiqa.backup-lint (RunAtLoad + StartCalendarInterval Sun 21:00)
# Logic: if last backup <7 days ago and today is Sunday 21:00 → run; if RunAtLoad and today is Mon and Sunday backup missing → catch-up run

set -e
LOG="/tmp/aiqa-backup-lint.out"
BACKUP_ROOT="$HOME/Backups/ai-qa-wiki"
TODAY=$(date +%Y-%m-%d)
DOW=$(date +%u) # 1=Mon 7=Sun
HOUR=$(date +%H)

# Find last backup
LAST=$(ls -t "$BACKUP_ROOT" 2>/dev/null | head -1 || echo "none")
LAST_EPOCH=0
if [ "$LAST" != "none" ] && [ -d "$BACKUP_ROOT/$LAST" ]; then
  LAST_EPOCH=$(stat -f %m "$BACKUP_ROOT/$LAST" 2>/dev/null || echo 0)
fi
NOW_EPOCH=$(date +%s)
AGE_DAYS=$(( (NOW_EPOCH - LAST_EPOCH) / 86400 ))

echo "[$(date -Iseconds)] weekly-backup-lint triggered DOW=$DOW HOUR=$HOUR LAST=$LAST AGE=${AGE_DAYS}d" | tee -a "$LOG"

# Decide if should run
SHOULD_RUN=false
if [ "$DOW" -eq 7 ] && [ "$HOUR" -ge 21 ]; then
  SHOULD_RUN=true # Sunday 21:00 window
  echo "→ Sunday window, run" | tee -a "$LOG"
elif [ "$AGE_DAYS" -ge 7 ]; then
  SHOULD_RUN=true # catch-up: no backup for 7+ days (missed Sunday because laptop off)
  echo "→ Catch-up: last backup ${AGE_DAYS}d ago, run now" | tee -a "$LOG"
else
  echo "→ Skip (not Sunday 21:00 and backup fresh ${AGE_DAYS}d)" | tee -a "$LOG"
fi

if [ "$SHOULD_RUN" = true ]; then
  echo "→ Running backup.sh" | tee -a "$LOG"
  "$HOME/Projects/ai-qa-wiki/backup.sh" 2>&1 | tee -a "$LOG"
  echo "→ Lint AGENTS.md" | tee -a "$LOG"
  # lint: check ≤32 KiB, no secrets, no dated facts, Boundaries table
  for f in "$HOME/Projects/ai-qa-wiki/AGENTS.md" "$HOME/Projects/Articles/AGENTS.md" "$HOME/Projects/qa-automation-sandbox/AGENTS.md"; do
    if [ -f "$f" ]; then
      SIZE=$(wc -c < "$f")
      LINES=$(wc -l < "$f")
      if [ "$SIZE" -gt 32768 ]; then echo "WARN $f >32KiB ($SIZE)" | tee -a "$LOG"; else echo "OK $f $SIZE bytes $LINES lines" | tee -a "$LOG"; fi
      if grep -q "sk-or-\|ghp_\|AKIA" "$f"; then echo "WARN secrets in $f" | tee -a "$LOG"; fi
    fi
  done
  echo "→ wiki-topics.json valid?" | tee -a "$LOG"
  python3 -m json.tool "$HOME/Projects/ai-qa-wiki/wiki-topics.json" > /dev/null && echo "OK wiki-topics.json valid" | tee -a "$LOG" || echo "FAIL wiki-topics.json" | tee -a "$LOG"
  echo "[$(date -Iseconds)] done" | tee -a "$LOG"
  # macOS notification (operative, catch-up aware)
  osascript -e "display notification \"Backup+lint done (last ${AGE_DAYS}d ago)\" with title \"AI QA Weekly\" sound name \"Glass\"" 2>/dev/null || true
fi
