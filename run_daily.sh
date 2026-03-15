#!/bin/bash

# Configuration
PROJECT_DIR="/home/asd/Python/Transcriptinator_working"
LOG_FILE="$PROJECT_DIR/daily_run.log"
VENV_ACTIVATE="$PROJECT_DIR/venv/bin/activate"

# Ensure we are in the project directory
cd "$PROJECT_DIR" || exit 1

# Once-per-day check
LAST_RUN_FILE="$PROJECT_DIR/.last_run"
TODAY=$(date +%Y-%m-%d)

if [ -f "$LAST_RUN_FILE" ]; then
    LAST_RUN=$(cat "$LAST_RUN_FILE")
    if [ "$LAST_RUN" == "$TODAY" ]; then
        # Already run today, exit silently or log it
        echo "$(date): Script already run today ($TODAY). Skipping." >> "$LOG_FILE"
        exit 0
    fi
fi

# Update last run file immediately to prevent race conditions
echo "$TODAY" > "$LAST_RUN_FILE"

# Activate virtual environment
source "$VENV_ACTIVATE"

# Log start time
echo "==================================================" >> "$LOG_FILE"
echo "Starting daily Transcriptinator run at $(date)" >> "$LOG_FILE"

# Run the pipeline
# The script relies on config.py for settings (AUTOMATED_MODE=True)
python3 run_full_audio_pipeline.py >> "$LOG_FILE" 2>&1

# Log end time
echo "Finished run at $(date)" >> "$LOG_FILE"
echo "==================================================" >> "$LOG_FILE"
