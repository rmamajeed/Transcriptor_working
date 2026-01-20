# GitHub Actions Setup Guide

## Quick Start

This guide will help you deploy Transcriptinator to run automatically every day at 11:30 AM IST using GitHub Actions (100% FREE).

---

## Prerequisites

- GitHub account (username: `Auto_Transcriptinator`)
- Google API key (Gemini)
- Groq or OpenRouter API key (for metadata)
- 10 minutes for setup

---

## Step 1: Create GitHub Repository

### A. Initialize Git (if not already done)
```bash
cd /home/asd/Python/Transcriptinator_working
git init
git add .
git commit -m "Initial commit: Transcriptinator with automated mode"
```

### B. Create Repository on GitHub
1. Go to: https://github.com/new
2. Repository name: `Transcriptinator`
3. Description: `Automated YouTube transcription with AI metadata extraction`
4. Visibility: **Public** (for free unlimited Actions minutes)
5. **Do NOT** initialize with README, .gitignore, or license
6. Click "Create repository"

### C. Push to GitHub
```bash
git remote add origin https://github.com/Auto_Transcriptinator/Transcriptinator.git
git branch -M main
git push -u origin main
```

---

## Step 2: Configure GitHub Secrets

Secrets store your API keys securely. They're encrypted and never visible in commit history.

### Navigate to Secrets
1. Go to your repository: `https://github.com/Auto_Transcriptinator/Transcriptinator`
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**

### Add These Secrets

| Secret Name | Value | Required | Where to Get |
|-------------|-------|----------|--------------|
| `GOOGLE_API_KEY` | Your Gemini API key | ✅ Yes | [Google AI Studio](https://aistudio.google.com/app/apikey) |
| `GROQ_API_KEY` | Your Groq API key | ⚠️ Recommended | [Groq Console](https://console.groq.com/) |
| `OPENROUTER_API_KEY` | Your OpenRouter key | ⚠️ Optional | [OpenRouter](https://openrouter.ai/) |
| `METADATA_PROVIDER` | `groq` or `openrouter` | ✅ Yes | Type manually: `groq` |
| `GEMINI_MODEL` | `models/gemini-2.0-flash-exp` | ⚠️ Optional | Type manually (uses default if not set) |

**Example: Adding GOOGLE_API_KEY**
1. Name: `GOOGLE_API_KEY`
2. Secret: `AIzaSyD...` (paste your actual key)
3. Click "Add secret"

**Repeat for all secrets above.**

---

## Step 3: Verify Workflow File

The workflow is already created at `.github/workflows/daily-transcription.yml`. Let's verify it's correct:

```bash
cat .github/workflows/daily-transcription.yml
```

**Key settings in the workflow**:
- **Schedule**: `cron: '0 6 * * *'` = 11:30 AM IST (6:00 AM UTC)
- **Timeout**: 120 minutes (2 hours max)
- **Auto-commit**: Commits transcripts back to repo automatically

---

## Step 4: Test Manual Run

Before waiting for the scheduled run, test it manually:

1. Go to: `https://github.com/Auto_Transcriptinator/Transcriptinator/actions`
2. Click on **"Daily YouTube Transcription"** workflow (left sidebar)
3. Click **"Run workflow"** button (right side)
4. Select branch: `main`
5. Click green **"Run workflow"** button

### Monitor Progress
- Watch the workflow run in real-time
- Check logs for each step
- Should complete in ~5-15 minutes (depending on videos)

### Expected Output
- ✅ Green checkmark = Success
- ❌ Red X = Failed (check logs)
- New commits in repository with transcripts
- Updated `youtube_memory.json`

---

## Step 5: Verify Scheduled Runs

The workflow will now run automatically every day at **11:30 AM IST** (6:00 AM UTC).

### Check Execution History
- Go to **Actions** tab
- See all past runs with timestamps
- Click any run to see detailed logs

### Workflow Behavior
- Checks playlist for new videos
- Auto-skips already processed videos
- Transcribes only new videos
- Commits results automatically
- Stops on Gemini quota errors

---

## Accessing Your Transcripts

### Option 1: Browse on GitHub
1. Go to repository → `Transcripts/` folder
2. Click any `.md` file to view with formatting
3. Download files as needed

### Option 2: Clone Locally
```bash
git clone https://github.com/Auto_Transcriptinator/Transcriptinator.git
cd Transcriptinator/Transcripts
```

### Option 3: Use GitHub API
```bash
# Get latest transcripts
curl -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/Auto_Transcriptinator/Transcriptinator/contents/Transcripts
```

---

## Configuration

### Change Playlist URL
Edit `config.py`:
```python
PLAYLIST_URL = "https://www.youtube.com/playlist?list=YOUR_NEW_PLAYLIST_ID"
```

Commit and push:
```bash
git add config.py
git commit -m "Update playlist URL"
git push
```

### Change Max Downloads
Edit `config.py`:
```python
MAX_DOWNLOADS = 5  # Process max 5 videos per day
# Or
MAX_DOWNLOADS = None  # Process all new videos
```

### Change Schedule
Edit `.github/workflows/daily-transcription.yml`:
```yaml
schedule:
  - cron: '30 5 * * *'  # 11:00 AM IST
  - cron: '0 12 * * *'  # 5:30 PM IST
```

**Cron syntax**: `minute hour day month weekday`
- All times in UTC (subtract 5:30 from IST)

---

## Troubleshooting

### Workflow Fails Immediately
**Check**: GitHub Secrets are configured correctly
- Go to Settings → Secrets
- Verify `GOOGLE_API_KEY` is set
- Verify `METADATA_PROVIDER` is set

### No New Videos Processed
**Reason**: All videos already in `youtube_memory.json`
1. Check `youtube_memory.json` in repository
2. Add new videos to playlist
3. Wait for next run or trigger manually

### Gemini Quota Exceeded
**Behavior**: Workflow stops with exit code 1
**Solution**: 
- Wait for quota to reset (usually 24 hours)
- Next run will continue from where it stopped
- Already processed videos won't be re-transcribed

### Commits Not Appearing
**Check**: 
1. View workflow logs → "Commit transcripts" step
2. Look for "No changes to commit" or "Nothing to push"
3. Means no new videos were processed (all already done)

---

## Cost Breakdown

| Service | Usage | Cost |
|---------|-------|------|
| **GitHub Actions** | ~20 min/day × 30 days = 600 min/month | **FREE** (2,000 min free tier) |
| **GitHub Storage** | ~500MB transcripts | **FREE** (1GB free) |
| **Repository Hosting** | Public repo | **FREE** |
| **Total** | | **$0.00/month** ✅ |

---

## Advanced Features

### Email Notifications on Failure
Add to workflow (after "Notify on failure" step):
```yaml
- name: Send email notification
  if: failure()
  uses: dawidd6/action-send-mail@v3
  with:
    server_address: smtp.gmail.com
    server_port: 465
    username: ${{ secrets.MAIL_USERNAME }}
    password: ${{ secrets.MAIL_PASSWORD }}
    subject: Transcriptinator workflow failed
    to: your-email@gmail.com
    from: GitHub Actions
    body: Check logs at ${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}
```

### Multiple Playlists
Create separate config files and multiple workflows:
- `config_playlist1.py`
- `config_playlist2.py`
- `.github/workflows/playlist1.yml`
- `.github/workflows/playlist2.yml`

---

## Security Best Practices

✅ **DO**:
- Use GitHub Secrets for API keys
- Keep repository public for free Actions
- Review workflow logs regularly

❌ **DON'T**:
- Commit `.env` file
- Share GitHub Secrets
- Use private repository (costs money)

---

## Next Steps

1. ✅ Create GitHub repository
2. ✅ Configure secrets
3. ✅ Test manual workflow run
4. ⏳ Wait for first scheduled run (11:30 AM IST tomorrow)
5. 🎉 Enjoy automated transcriptions!

---

## Support

- **Workflow logs**: Actions tab → Click run → View logs
- **Test locally**: `python run_full_audio_pipeline.py`
- **Check syntax**: https://crontab.guru/ (for cron schedules)

**Status**: ✅ Ready for deployment!
