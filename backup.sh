#!/bin/bash
# AI QA Wiki Backup Script
# Usage: ./backup.sh

DATE=$(date +%Y-%m-%d)
BACKUP_DIR="$HOME/Backups/ai-qa-wiki"
SOURCE_DIR="/Users/victor/Projects/ai-qa-wiki"

# Create backup directory
mkdir -p "$BACKUP_DIR/$DATE"

echo "📦 Creating backup: $DATE"

# Backup wiki (source)
echo "  📄 Wiki articles..."
cp -r "$SOURCE_DIR/wiki" "$BACKUP_DIR/$DATE/"

# Backup raw
echo "  📄 Raw files..."
cp -r "$SOURCE_DIR/raw" "$BACKUP_DIR/$DATE/" 2>/dev/null || true

# Backup outputs
echo "  📄 Outputs..."
cp -r "$SOURCE_DIR/outputs" "$BACKUP_DIR/$DATE/"

# Backup scripts
echo "  📄 Scripts..."
cp "$SOURCE_DIR/groq_qa.py" "$BACKUP_DIR/$DATE/" 2>/dev/null || true

# Save backup list
ls -la "$BACKUP_DIR/$DATE" > "$BACKUP_DIR/$DATE/manifest.txt"

echo "✅ Backup created: $BACKUP_DIR/$DATE"
echo "   Size: $(du -sh "$BACKUP_DIR/$DATE" | cut -f1)"

# Keep only last 10 backups
cd "$BACKUP_DIR"
ls -td */ | tail -n +11 | xargs -r rm -rf
echo "   (Old backups cleaned)"
