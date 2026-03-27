# Setup Guide: Automated Daily Run with Cron

This guide explains how to set up the `run_daily.sh` script to run automatically every day at **11:30 AM** on a Linux laptop.

## Prerequisites

1.  **Script Permissions**: Ensure the script is executable.
2.  **Absolute Paths**: The script uses absolute paths. You **must** update the `PROJECT_DIR` variable inside `run_daily.sh` to match the exact path on the new laptop.

## Step 1: Update the Script Path

Open `run_daily.sh` and update line 4 to reflect the location of the project on the new laptop:

```bash
# Example: If the project is in /home/user/Documents/Transcriptinator_working
PROJECT_DIR="/home/user/Documents/Transcriptinator_working"
```

## Step 2: Make the Script Executable

Run the following command in the terminal to grant execution permissions:

```bash
chmod +x /path/to/your/project/run_daily.sh
```

## Step 3: Open the Crontab Editor

Open your user's crontab by running:

```bash
crontab -e
```

> [!NOTE]
> If it's your first time running this, it might ask you to choose an editor (like `nano` or `vim`). Choose `nano` if you're unsure.

## Step 4: Add the Cron Job

Scroll to the bottom of the file and add the following line:

```cron
30 11 * * * /path/to/your/project/run_daily.sh >> /path/to/your/project/cron_output.log 2>&1
```

### Breakdown of the Cron Expression:
-   `30`: Minute (30)
-   `11`: Hour (11 AM)
-   `* * *`: Every day of the month, month, and day of the week.
-   `/path/to/your/project/run_daily.sh`: The absolute path to your script.
-   `>> ... 2>&1`: Redirects any output or errors to a log file for troubleshooting.

## Step 5: Save and Exit

-   In `nano`: Press `Ctrl + O` (Enter) to save, then `Ctrl + X` to exit.
-   In `vim`: Press `Esc`, type `:wq`, and press `Enter`.

## Verification

You can verify the cron job is scheduled by listing your active cron jobs:

```bash
crontab -l
```

### Troubleshooting
-   Check `daily_run.log` in your project directory for script execution details.
-   Check `cron_output.log` for any system-level errors that prevented the script from starting.
