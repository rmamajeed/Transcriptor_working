# Implementation Plan: Automated Cloud Execution

## Overview

**Phase 1**: Remove interactive prompts, add hardcoded configuration  
**Phase 2**: GitHub Actions with Google Drive auto-sync  

**Total Cost**: $0/month ✅

---

## Phase 1: Remove Interactive Prompts (Automated Mode)

### Problem
Current app requires manual input:
- Option selection (video/playlist/skip)
- URL input
- Already-processed video handling
- Max downloads confirmation

### Solution
Add **automated mode** with hardcoded configuration:
- Always process playlist
- Hardcoded playlist URL
- Auto-skip processed videos
- Download all videos from playlist
- Zero user interaction

---

### Changes Required

#### 1. Create Configuration File

**NEW FILE**: [`config.py`](file:///home/asd/Python/Transcriptinator_working/config.py)

```python
"""
Configuration for automated cloud execution
"""

# Automated mode settings
AUTOMATED_MODE = True  # Set to False for interactive mode

# Playlist configuration
PLAYLIST_URL = "https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID"

# Download settings
MAX_DOWNLOADS = None  # None = all videos, or set a number (e.g., 10)
SKIP_ALREADY_PROCESSED = True  # Always skip videos in memory

# Metadata level
METADATA_LEVEL = "enhanced"  # "basic" or "enhanced"

# Folders
DOWNLOADS_FOLDER = "downloads"
TRANSCRIPTS_FOLDER = "Transcripts"
```

**Why**: Centralized configuration, easy to modify for different playlists

---

#### 2. Modify `run_full_audio_pipeline.py`

**File**: [run_full_audio_pipeline.py](file:///home/asd/Python/Transcriptinator_working/run_full_audio_pipeline.py)

**Changes**:

**A. Import config**:
```python
import config
```

**B. Replace `prompt_for_download()` with automated version**:

```python
def automated_download(memory):
    """
    Automated download mode - no user interaction
    Downloads from hardcoded playlist URL
    """
    print("🤖 AUTOMATED MODE")
    print("=" * 60)
    print(f"📋 Playlist: {config.PLAYLIST_URL}")
    print(f"📥 Max downloads: {'ALL' if config.MAX_DOWNLOADS is None else config.MAX_DOWNLOADS}")
    print(f"⏭️  Skip processed: {config.SKIP_ALREADY_PROCESSED}")
    print("=" * 60)
    
    downloader = YouTubeAudioDownloader(
        output_dir=config.DOWNLOADS_FOLDER,
        audio_format="mp3",
        audio_quality="192"
    )
    
    # Download playlist with memory-aware skipping
    result = downloader.download_playlist_with_memory(
        config.PLAYLIST_URL, 
        memory, 
        max_downloads=config.MAX_DOWNLOADS
    )
    
    if result['success']:
        print(f"\n✅ Playlist Processing Complete!")
        print(f"   Downloaded: {result.get('downloaded', 0)} videos")
        print(f"   Skipped: {result.get('skipped', 0)} videos (already processed)")
        if result.get('failed', 0) > 0:
            print(f"   Failed: {result.get('failed', 0)} videos")
    else:
        print(f"\n❌ Playlist processing failed: {result.get('error', 'Unknown error')}")
        sys.exit(1)
```

**C. Update `main()` to use automated or interactive mode**:

```python
def main():
    downloads_folder = config.DOWNLOADS_FOLDER
    transcripts_folder = config.TRANSCRIPTS_FOLDER

    # Initialize memory system
    memory = TranscriptionMemory()

    # Step 1: Download audio files
    if config.AUTOMATED_MODE:
        automated_download(memory)
    else:
        prompt_for_download()  # Keep old interactive mode

    # Step 2: Chunk and transcribe with metadata
    print("\nStarting chunking and transcription process...")
    sys.argv = ["audio_process_and_transcribe.py", downloads_folder, "-o", transcripts_folder, "--metadata-level", config.METADATA_LEVEL]
    process_and_transcribe_main(memory_system=memory, downloads_folder=downloads_folder)

    # Note: Memory update and audio deletion now happen per-file
    print("\n✅ Pipeline complete.")

if __name__ == "__main__":
    main()
```

**Summary**:
- ✅ No user input when `AUTOMATED_MODE = True`
- ✅ Uses hardcoded playlist URL
- ✅ Auto-skips processed videos via memory system
- ✅ Can easily switch back to interactive mode

---

### Verification Plan (Phase 1)

#### Test 1: Automated Mode with Existing Playlist

**Steps**:
1. Edit `config.py`:
   ```python
   PLAYLIST_URL = "https://www.youtube.com/playlist?list=YOUR_TEST_PLAYLIST"
   AUTOMATED_MODE = True
   MAX_DOWNLOADS = 2  # Test with 2 videos
   ```

2. Run:
   ```bash
   python run_full_audio_pipeline.py
   ```

3. **Expected**:
   - No prompts for input
   - Downloads 2 videos from playlist
   - Processes both
   - Exits automatically

#### Test 2: Skip Already Processed Videos

**Steps**:
1. Run again with same playlist
2. **Expected**:
   - Skips 2 previously processed videos
   - Prints "Skipped: 2 videos (already processed)"
   - No new downloads

#### Test 3: Interactive Mode Still Works

**Steps**:
1. Set `AUTOMATED_MODE = False` in `config.py`
2. Run app
3. **Expected**:
   - Shows old menu
   - Prompts for input
   - Works as before

---

## Phase 2: GitHub Actions with Google Drive Sync

### Requirements Summary (from your feedback)
- ✅ FREE ($0/month)
- ✅ 3-5 videos/day processing
- ✅ Auto-sync to Google Drive
- ✅ Store `youtube_memory.json` in repository
- ✅ Automated daily runs at 11:30 AM IST
- ✅ Critical logging/debugging
- ✅ No manual triggers needed

---

### Architecture

```
GitHub Repository (code + memory)
         ↓
GitHub Actions Runner (11:30 AM IST daily)
         ↓
[Download → Transcribe → Generate metadata]
         ↓
Commit transcripts + memory back to repo
         ↓
Auto-sync to Google Drive
```

---

### Files to Create

#### 1. GitHub Actions Workflow

**NEW FILE**: `.github/workflows/daily-transcription.yml`

```yaml
name: Daily YouTube Transcription

on:
  schedule:
    # 6:00 AM UTC = 11:30 AM IST
    - cron: '0 6 * * *'
  
  # Allow manual trigger for testing
  workflow_dispatch:

jobs:
  transcribe:
    runs-on: ubuntu-latest
    timeout-minutes: 120  # 2 hours max
    
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
      
      - name: Set up Python 3.10
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'
          cache: 'pip'
      
      - name: Install FFmpeg
        run: |
          sudo apt-get update
          sudo apt-get install -y ffmpeg
          ffmpeg -version
      
      - name: Install Python dependencies
        run: |
          pip install --upgrade pip
          pip install -r requirements.txt
      
      - name: Run transcription pipeline
        env:
          GOOGLE_API_KEY: ${{ secrets.GOOGLE_API_KEY }}
          GROQ_API_KEY: ${{ secrets.GROQ_API_KEY }}
          OPENROUTER_API_KEY: ${{ secrets.OPENROUTER_API_KEY }}
          METADATA_PROVIDER: ${{ secrets.METADATA_PROVIDER }}
        run: |
          echo "🚀 Starting transcription pipeline..."
          python run_full_audio_pipeline.py
          echo "✅ Pipeline completed"
      
      - name: Commit transcripts and memory
        run: |
          git config --global user.name "GitHub Actions Bot"
          git config --global user.email "actions@github.com"
          
          # Add new transcripts
          git add Transcripts/
          git add youtube_memory.json
          
          # Commit with timestamp
          TIMESTAMP=$(date -u +"%Y-%m-%d %H:%M:%S UTC")
          git commit -m "Daily transcripts: $TIMESTAMP" || echo "No new transcripts"
          
          # Push to repository
          git push
      
      - name: Sync to Google Drive
        uses: satackey/action-google-drive@v1
        with:
          credentials: ${{ secrets.GOOGLE_DRIVE_CREDENTIALS }}
          folder: Transcripts
          target: ./Transcripts
          method: sync
      
      - name: Upload logs as artifact
        if: always()  # Run even if job fails
        uses: actions/upload-artifact@v4
        with:
          name: transcription-logs-${{ github.run_number }}
          path: |
            *.log
            downloads/*.info.json
          retention-days: 7
```

**Features**:
- ✅ Runs daily at 11:30 AM IST (6:00 AM UTC)
- ✅ Installs FFmpeg automatically
- ✅ Caches pip packages for faster runs
- ✅ Commits results back to repository
- ✅ Syncs to Google Drive
- ✅ Uploads logs for debugging
- ✅ 2-hour timeout (enough for 5+ videos)

---

#### 2. Google Drive Sync Configuration

**NEW FILE**: `.github/scripts/setup-gdrive.sh`

```bash
#!/bin/bash
# Run this locally ONCE to get Google Drive credentials

echo "🔐 Setting up Google Drive API credentials"
echo "1. Go to https://console.cloud.google.com/apis/credentials"
echo "2. Create a Service Account"
echo "3. Download JSON key"
echo "4. Convert to base64:"
echo ""
echo "   cat your-service-account-key.json | base64 | tr -d '\n'"
echo ""
echo "5. Add to GitHub Secrets as GOOGLE_DRIVE_CREDENTIALS"
```

---

#### 3. Repository Setup Guide

**NEW FILE**: `GITHUB_ACTIONS_SETUP.md`

```markdown
# GitHub Actions Setup Guide

## 1. Create GitHub Repository

```bash
cd /path/to/Transcriptinator_working
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/Transcriptinator.git
git push -u origin main
```

## 2. Configure Secrets

Go to: **Settings → Secrets and variables → Actions**

Add these repository secrets:

| Secret Name | Value | Where to Get |
|-------------|-------|--------------|
| `GOOGLE_API_KEY` | Your Gemini API key | https://aistudio.google.com/app/apikey |
| `GROQ_API_KEY` | Your Groq API key | https://console.groq.com/ |
| `OPENROUTER_API_KEY` | Your OpenRouter key (optional) | https://openrouter.ai/ |
| `METADATA_PROVIDER` | `groq` or `openrouter` | Your choice |
| `GOOGLE_DRIVE_CREDENTIALS` | Base64 service account JSON | See below |

## 3. Google Drive Service Account

### Create Service Account:
1. Go to: https://console.cloud.google.com/apis/credentials
2. Click "Create Credentials" → "Service Account"
3. Name: `transcriptinator-bot`
4. Grant role: "Editor"
5. Click "Done"

### Generate Key:
1. Click on your service account
2. "Keys" tab → "Add Key" → "Create new key"
3. Choose JSON → Download

### Share Google Drive Folder:
1. Create folder in Google Drive: `Transcriptinator_Transcripts`
2. Right-click → Share
3. Add service account email (e.g., `transcriptinator-bot@...iam.gserviceaccount.com`)
4. Give "Editor" permissions

### Convert to Secret:
```bash
cat your-service-account-key.json | base64 | tr -d '\n'
```
Copy output → Add as `GOOGLE_DRIVE_CREDENTIALS` secret

## 4. Update `config.py`

Set your playlist URL:
```python
PLAYLIST_URL = "https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID"
```

## 5. Test Workflow

### Manual Test:
1. Go to: **Actions** tab
2. Select "Daily YouTube Transcription"
3. Click "Run workflow"
4. Monitor execution

### Check Results:
- Transcripts in repository: `Transcripts/` folder
- Transcripts in Google Drive: Your shared folder
- Memory file updated: `youtube_memory.json`
- Logs: Download from workflow artifacts

## 6. Verify Schedule

Workflow runs automatically at **11:30 AM IST (6:00 AM UTC)** daily.

First run requires ~10-15 minutes for 3-5 videos.
```

---

### Cost Breakdown (Phase 2)

| Item | Usage | Cost |
|------|-------|------|
| **GitHub Actions** | ~20 min/day × 30 days = 600 min/month | **FREE** (2,000 min free tier) |
| **GitHub Storage** | ~500MB (transcripts) | **FREE** (1GB free) |
| **Google Drive** | 15GB free tier | **FREE** |
| **Total** | | **$0/month** ✅ |

---

### Accessing Transcripts (Phase 2)

#### Option 1: Browse on GitHub
- Go to repository → `Transcripts/` folder
- Download individual files
- View markdown with formatting

#### Option 2: Google Drive (Auto-synced)
- Open Google Drive folder
- All transcripts automatically synced
- Can access from phone/tablet
- Share with others easily

#### Option 3: Clone Repository Locally
```bash
git clone https://github.com/YOUR_USERNAME/Transcriptinator.git
cd Transcriptinator/Transcripts
```

---

## Summary of Changes

### Phase 1 Files
| File | Action | Purpose |
|------|--------|---------|
| `config.py` | **NEW** | Hardcoded configuration |
| `run_full_audio_pipeline.py` | **MODIFY** | Add automated mode |

### Phase 2 Files
| File | Action | Purpose |
|------|--------|---------|
| `.github/workflows/daily-transcription.yml` | **NEW** | GitHub Actions workflow |
| `.github/scripts/setup-gdrive.sh` | **NEW** | Google Drive setup helper |
| `GITHUB_ACTIONS_SETUP.md` | **NEW** | Step-by-step setup guide |
| `.gitignore` | **UPDATE** | Exclude downloads/, venv/ |
| `README.md` | **UPDATE** | Add automation documentation |

---

## User Questions & Confirmations

### Phase 1 Confirmation Needed:

1. **Playlist URL**: What's the YouTube playlist URL to hardcode?
   - Example: `https://www.youtube.com/playlist?list=PLrAXtmErZgOeiKm4sgNOknGvNjby9efdf`

2. **Default metadata level**: Keep `enhanced` or switch to `basic`?
   - Enhanced = 4 AI calls (more detailed, slower)
   - Basic = 2 AI calls (faster, less metadata)

3. **Max downloads per run**: Download all new videos or limit?
   - `None` = All new videos
   - `5` = Max 5 videos per day
   - Your choice: __________

### Phase 2 Confirmation Needed:

4. **Repository visibility**: Public or Private?
   - Public = Free unlimited Actions minutes
   - Private = Free but only 2,000 min/month

5. **GitHub username/organization**: What's your GitHub account?
   - Need to know for repository URL

6. **Google Drive folder name**: What should the folder be called?
   - Suggestion: `Transcriptinator_Transcripts`
   - Your preference: __________

---

## Next Steps

**After you approve**:

### Phase 1 (15 minutes):
1. Create `config.py`
2. Modify `run_full_audio_pipeline.py`
3. Test automated mode locally
4. Confirm it works with your playlist

### Phase 2 (30 minutes):
5. Create GitHub repository
6. Add workflow files
7. Set up Google Drive service account
8. Configure secrets
9. Test workflow manually
10. Verify auto-sync to Google Drive

**WAITING FOR YOUR APPROVAL TO PROCEED** ✋

Please provide:
- ✅ Confirmation to proceed with Phase 1
- ✅ Answers to questions above
- ✅ Any modifications to the plan
