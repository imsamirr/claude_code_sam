#!/bin/bash
# ============================================
# Daily Metrics Sync — Cron Job Setup Helper
# ============================================
# This script helps you set up a cron job to run
# the metrics sync automatically every day.
#
# Usage: bash schedule_daily.sh
# ============================================

set -e

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
PYTHON_BIN="$PROJECT_DIR/venv/bin/python"
SCRIPT="$PROJECT_DIR/src/main.py"
LOG_DIR="$PROJECT_DIR/logs"

echo "=== Daily Metrics Sync — Cron Setup ==="
echo ""

# Check that venv exists
if [ ! -f "$PYTHON_BIN" ]; then
    echo "ERROR: Virtual environment not found at $PROJECT_DIR/venv"
    echo "Please run: python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt"
    exit 1
fi

# Create log directory
mkdir -p "$LOG_DIR"

# Ask for preferred time
echo "What time should the sync run daily? (24-hour format)"
read -r -p "Enter time (e.g., 08:00): " SYNC_TIME

HOUR=$(echo "$SYNC_TIME" | cut -d: -f1)
MINUTE=$(echo "$SYNC_TIME" | cut -d: -f2)

# Validate
if [ -z "$HOUR" ] || [ -z "$MINUTE" ]; then
    echo "Invalid time format. Please use HH:MM (e.g., 08:00)"
    exit 1
fi

CRON_LINE="$MINUTE $HOUR * * * cd $PROJECT_DIR && $PYTHON_BIN $SCRIPT >> $LOG_DIR/daily_run.log 2>&1"

echo ""
echo "This will add the following cron job:"
echo "  $CRON_LINE"
echo ""
read -r -p "Add this to your crontab? (y/n): " CONFIRM

if [ "$CONFIRM" = "y" ] || [ "$CONFIRM" = "Y" ]; then
    # Add to crontab without overwriting existing entries
    (crontab -l 2>/dev/null || true; echo "$CRON_LINE") | crontab -
    echo ""
    echo "Cron job added! The sync will run daily at $SYNC_TIME."
    echo "Logs will be written to: $LOG_DIR/daily_run.log"
    echo ""
    echo "To verify, run: crontab -l"
    echo "To remove, run: crontab -e  (and delete the line)"
else
    echo "Cancelled. No changes made."
fi
