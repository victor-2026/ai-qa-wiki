#!/bin/bash
# Nightly fix-orphans run: snapshot + conservative auto-link + lint + report. NO commit.
# Self-unloads its launchd job at the end (one-shot).
set -u
PROJ="/Users/victor/Projects/ai-qa-wiki"
DATE=$(date +%Y-%m-%d)
SNAP="/tmp/wiki-fixorphans-BEFORE-$DATE"
LOG="/tmp/aiqa-fixorphans-night.log"
REPORT="$PROJ/outputs/fix-orphans-night-$DATE.md"
LABEL="com.aiqa.fixorphans-night"

echo "=== fix-orphans night run $DATE $(date) ===" >> "$LOG"
rm -rf "$SNAP"; cp -r "$PROJ/wiki" "$SNAP" >> "$LOG" 2>&1
echo "snapshot: $SNAP" >> "$LOG"
git -C "$PROJ" status --short > "/tmp/wiki-fixorphans-gitstatus-$DATE.txt" 2>&1

cd "$PROJ" || exit 1
# Conservative auto mode ONLY (min_score 0.12, max 2 links). No loose passes.
python3 - <<'PYEOF' >> "$LOG" 2>&1
import sys
sys.path.insert(0, "/Users/victor/Projects/ai-qa-wiki")
import wiki_lint as L
plan = L.fix_orphans(dry_run=False, min_score=0.12, max_links=2)
print(f"APPLIED {len(plan)} links")
hubs = sorted(set(h for _, h, _ in plan))
print(f"HUBS touched: {len(hubs)}")
PYEOF
python3 wiki_lint.py >> "$LOG" 2>&1
{
  echo "# fix-orphans night report $DATE"
  echo
  echo "Snapshot (rollback source): \`$SNAP\`"
  echo "Git status before: \`/tmp/wiki-fixorphans-gitstatus-$DATE.txt\`"
  echo
  grep -E "APPLIED|HUBS|Broken links|Orphans|Exit" "$LOG" | tail -8
  echo
  echo "Review: \`git -C $PROJ status --short\` + \`git -C $PROJ diff --stat\`. Rollback per-file: \`cp $SNAP/<file> $PROJ/wiki/<file>\`. NO commit was made."
} > "$REPORT"
echo "report: $REPORT" >> "$LOG"
/bin/launchctl unload "$HOME/Library/LaunchAgents/$LABEL.plist" >> "$LOG" 2>&1 || true
echo "=== done $(date) ===" >> "$LOG"
