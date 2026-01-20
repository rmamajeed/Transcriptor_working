# Cloud Automation Brainstorming for Transcriptinator

## Current Situation

**Manual Process**:
1. Open laptop
2. Start VSCode
3. Activate venv
4. Run application manually

**Goal**: Fully automated cloud execution at 11:30 AM daily with accessible transcript storage

---

## Application Requirements Analysis

### What the App Needs

#### **Runtime Requirements**
- Python 3.8+ environment
- Virtual environment with dependencies:
  ```
  yt-dlp, google-generativeai, openai, groq, 
  ffmpeg-python, pyyaml, psutil, python-dotenv
  ```
- **FFmpeg binary** (system dependency - critical!)

#### **API Keys (Secrets Management)**
```env
GOOGLE_API_KEY=         # Gemini (required for transcription)
METADATA_PROVIDER=      # groq/openrouter/gemini
GROQ_API_KEY=          # If using Groq
OPENROUTER_API_KEY=    # If using OpenRouter
```

#### **Storage Needs**

**Input Processing**:
- `downloads/` - Temporary audio files from YouTube
  - Audio files (.mp3, .m4a, etc.)
  - `.info.json` files from yt-dlp
  - **Deleted per-file after processing** ✓

**Output Storage**:
- `Transcripts/` - Generated markdown/text files
  - `.md` files (with rich metadata)
  - `.txt` files (plain text)
  - **Must persist permanently** ✓

**State Management**:
- `youtube_memory.json` - Tracks processed videos
  - Prevents duplicate processing
  - **Must persist across runs** ✓

#### **Execution Profile**
- **Duration**: 2-20 minutes per video (depends on length, metadata level)
- **Example**: 60-minute video = ~17 minutes processing (enhanced mode)
- **Memory**: 500MB-2GB peak (chunking large files)
- **Disk Space**:
  - Temporary: 100MB-500MB per video while processing
  - Permanent: ~1-5MB per transcript (markdown + metadata)

---

## Option 1️⃣: GitHub Actions (FREE)

### How It Works
- Store code in GitHub repository
- GitHub Actions runs scheduled workflows (cron)
- Workflow runs at 11:30 AM daily
- Stores transcripts back to repository or cloud storage

### Configuration

**`.github/workflows/daily-transcription.yml`**:
```yaml
name: Daily Transcription

on:
  schedule:
    - cron: '0 6 * * *'  # 11:30 AM IST = 6:00 AM UTC
  workflow_dispatch:     # Manual trigger option

jobs:
  transcribe:
    runs-on: ubuntu-latest
    timeout-minutes: 120  # 2 hour max
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      
      - name: Install FFmpeg
        run: sudo apt-get update && sudo apt-get install -y ffmpeg
      
      - name: Install dependencies
        run: pip install -r requirements.txt
      
      - name: Run transcription
        env:
          GOOGLE_API_KEY: ${{ secrets.GOOGLE_API_KEY }}
          GROQ_API_KEY: ${{ secrets.GROQ_API_KEY }}
        run: python run_full_audio_pipeline.py
      
      - name: Upload transcripts
        uses: actions/upload-artifact@v3
        with:
          name: transcripts
          path: Transcripts/
```

### ✅ Pros
- **FREE**: 2,000 minutes/month free tier (enough for daily runs)
- **Zero setup**: No server management
- **Simple**: Just push code to GitHub
- **FFmpeg included**: Pre-installed on Ubuntu runners
- **Secrets management**: Built-in GitHub Secrets
- **Easy debugging**: Logs in GitHub UI

### ❌ Cons
- **6-hour execution limit** per workflow run
- **No persistent storage**: Must upload artifacts or push to repo
- **Public repository** required for free tier (use secrets for API keys)
- **Manual retrieval**: Must download artifacts from GitHub UI
- **Not ideal for large batches**: 2,000 min/month = ~66 min/day

### Storage Strategy
**Option A: Commit to Repository**
```bash
- name: Commit transcripts
  run: |
    git config --global user.name "GitHub Actions"
    git config --global user.email "actions@github.com"
    git add Transcripts/ youtube_memory.json
    git commit -m "Daily transcripts $(date)"
    git push
```

**Option B: Upload to Google Drive/Dropbox**
```yaml
- name: Upload to Google Drive
  uses: satackey/action-google-drive@v1
  with:
    credentials: ${{ secrets.GOOGLE_DRIVE_CREDENTIALS }}
    folder: Transcripts
```

### Cost
**$0/month** (within free tier limits)

---

## Option 2️⃣: Google Cloud Run + Cloud Scheduler (RECOMMENDED)

### How It Works
- Package app as Docker container
- Deploy to Cloud Run (serverless)
- Cloud Scheduler triggers at 11:30 AM daily
- Store transcripts in Google Cloud Storage

### Architecture
```
Cloud Scheduler (11:30 AM IST)
         ↓
Cloud Run Job (Python container)
         ↓
Google Cloud Storage (transcripts/)
```

### Configuration

**Dockerfile**:
```dockerfile
FROM python:3.10-slim

# Install FFmpeg
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "run_full_audio_pipeline.py"]
```

**Cloud Scheduler**: `0 6 * * *` (11:30 AM IST)

**Cloud Storage Structure**:
```
gs://your-bucket/
├── transcripts/
│   ├── 2026-01-20/
│   │   ├── video1.md
│   │   └── video1.txt
│   └── 2026-01-21/
├── memory/
│   └── youtube_memory.json
└── logs/
```

### ✅ Pros
- **Exactly what you asked for**: Cloud + scheduled + storage
- **Unlimited execution time**: Up to 24 hours per job
- **Persistent storage**: Google Cloud Storage (99.999999999% durability)
- **Automatic scaling**: Handles any workload
- **Web UI**: Easy to view/download transcripts
- **Integrated secrets**: Cloud Secret Manager
- **Logs**: Cloud Logging for debugging

### ❌ Cons
- **Requires Google Cloud account**
- **Learning curve**: Docker + GCP concepts
- **Not entirely free** (see cost below)

### Storage Integration

**Modified `audio_process_and_transcribe.py`** (minor changes):
```python
from google.cloud import storage

def upload_to_gcs(local_file, bucket_name, blob_path):
    """Upload file to Google Cloud Storage"""
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_path)
    blob.upload_from_filename(local_file)
    print(f"✅ Uploaded {local_file} to gs://{bucket_name}/{blob_path}")

# After saving transcript:
upload_to_gcs(output_file_path_md, "your-bucket", f"transcripts/{date}/{basename}.md")
upload_to_gcs("youtube_memory.json", "your-bucket", "memory/youtube_memory.json")
```

### Cost Estimate
| Component | Usage | Cost |
|-----------|-------|------|
| **Cloud Run** | ~20 min/day @ 1GB RAM | ~$1-2/month |
| **Cloud Scheduler** | 31 jobs/month | $0.10/month |
| **Cloud Storage** | 10GB storage + egress | $0.20/month |
| **Total** | | **~$2-3/month** |

**Free Tier**: First 2 million requests/month = likely covers most usage

---

## Option 3️⃣: AWS Lambda + EventBridge

### How It Works
- Package app as Lambda layer/container
- EventBridge triggers at 11:30 AM daily
- Store transcripts in S3

### Configuration

**EventBridge Rule**: `cron(0 6 * * ? *)`  # 11:30 AM IST

**Lambda Container** (similar to Dockerfile above)

**S3 Structure**:
```
s3://your-bucket/
├── transcripts/
└── memory/
    └── youtube_memory.json
```

### ✅ Pros
- **15-minute execution** limit (Lambda timeout)
- **Generous free tier**: 400,000 GB-seconds/month
- **S3 integration**: Easy storage
- **Wide adoption**: Lots of tutorials/support

### ❌ Cons
- **15-minute timeout**: May not be enough for long videos
- **Package size limits**: 10GB unzipped (FFmpeg is large)
- **Cold starts**: First invocation may be slow
- **Complex permission management**: IAM roles

### Cost Estimate
- **Lambda**: $1-2/month
- **S3**: $0.20/month
- **Total**: **~$1-3/month**

---

## Option 4️⃣: Dedicated Cloud VM (DigitalOcean/Google Compute)

### How It Works
- Rent a small Linux VM ($5-10/month)
- Install Python + FFmpeg + dependencies
- Set up cron job: `30 11 * * *`
- Store transcripts on VM disk
- Access via SFTP/web interface

### Configuration

**Server**: Ubuntu 22.04 (1GB RAM, 25GB disk)

**Crontab**:
```bash
30 6 * * * cd /home/user/Transcriptinator && ./venv/bin/python run_full_audio_pipeline.py >> /var/log/transcription.log 2>&1
```

**Access Transcripts**:
- **SFTP**: Use FileZilla/WinSCP to download `Transcripts/` folder
- **Nextcloud/File Browser**: Install web-based file manager
- **Sync to Dropbox**: Install `rclone` to auto-sync to cloud

### ✅ Pros
- **Full control**: Install anything you want
- **No execution limits**: Run as long as needed
- **Simple setup**: Just like your laptop
- **Persistent disk**: Everything stays on server
- **Can add web UI**: Deploy Flask app for browser access

### ❌ Cons
- **Always-on cost**: $5-10/month even if only used daily
- **Manual maintenance**: You manage OS updates, security
- **Single point of failure**: If VM crashes, no backups (unless configured)

### Cost
- **DigitalOcean Droplet**: $6/month (1GB RAM)
- **Google Cloud e2-micro**: $7/month (0.5GB RAM + 10GB disk)
- **Total**: **$6-10/month**

---

## Option 5️⃣: PythonAnywhere (Specialized Python Hosting)

### How It Works
- Dedicated Python hosting platform
- Upload code via web interface
- Schedule task: Daily 11:30 AM
- Download transcripts from web dashboard

### Features
- **Built-in Python**: No setup needed
- **Scheduled tasks**: Native cron-like scheduler
- **Web-based file browser**: Easy download
- **Pre-installed packages**: Most dependencies included

### ✅ Pros
- **Python-focused**: Perfect for Python apps
- **Zero DevOps**: No Docker/VM knowledge needed
- **File browser**: Download transcripts from web UI
- **Shared environments**: Easy to hand off to team member

### ❌ Cons
- **Execution limits**: Free tier = 100 sec/day CPU (not enough!)
- **Paid required**: Need $5/month plan for longer tasks
- **Limited customization**: Restricted environment

### Cost
- **Free tier**: Not sufficient (100 CPU-sec/day)
- **Hacker plan**: $5/month (up to 5,000 CPU-sec/day)
- **Total**: **$5/month**

---

## Comparison Matrix

| Feature | GitHub Actions | Google Cloud Run | AWS Lambda | Cloud VM | PythonAnywhere |
|---------|---------------|------------------|------------|----------|----------------|
| **Cost** | **FREE** ✅ | ~$2-3/month | ~$1-3/month | $6-10/month | $5/month |
| **Setup Complexity** | Low | Medium | Medium | Low | Very Low |
| **Execution Limit** | 6 hours | 24 hours ✅ | 15 min ❌ | Unlimited ✅ | Varies |
| **FFmpeg Support** | ✅ Pre-installed | ✅ In container | ⚠️ Must package | ✅ Install | ⚠️ Limited |
| **Persistent Storage** | ❌ Artifacts only | ✅ Cloud Storage | ✅ S3 | ✅ Local disk | ✅ Disk |
| **Transcript Access** | GitHub UI | GCS web UI | S3 web UI | SFTP/Web | Web browser |
| **Secrets Management** | ✅ GitHub Secrets | ✅ Secret Manager | ✅ Secrets Manager | .env file | .env file |
| **Debugging** | ✅ Workflow logs | ✅ Cloud Logging | ✅ CloudWatch | SSH + logs | Web console |
| **Scalability** | Low | ✅ Auto-scale | ✅ Auto-scale | Manual | Low |
| **Best For** | Hobby/Free | Production ✅ | AWS users | Full control | Beginners |

---

## My Recommendations

### 🥇 **BEST OPTION: GitHub Actions** (Start Here)

**Why**:
- **FREE**: No monthly costs
- **Easiest**: Minimal setup, no billing account needed
- **Sufficient**: 2,000 min/month = ~66 min/day (enough for 3-4 videos/day)
- **Integrated**: Code + automation + storage in one place

**How to Access Transcripts**:
1. **Option A**: Auto-commit to repository → Browse on GitHub
2. **Option B**: Upload to Google Drive → Access normally
3. **Option C**: Download artifacts from Actions tab

**Start with this, upgrade if needed.**

---

### 🥈 **RECOMMENDED FOR SCALING: Google Cloud Run**

**Why**:
- **Production-ready**: Unlimited execution, proper storage
- **Cost-effective**: ~$2-3/month
- **Professional**: Proper logging, monitoring, backups
- **Google ecosystem**: If you're using Gemini API already

**When to choose**:
- Processing 5+ videos per day
- Need >6 hour runs
- Want centralized cloud storage
- Building this for long-term use

---

### 🥉 **EASIEST FOR NON-TECHY: PythonAnywhere**

**Why**:
- Zero technical knowledge needed
- Web UI for everything
- No Docker/VM/Cloud concepts
- $5/month is cheap

**When to choose**:
- Don't want to learn Docker/Cloud
- Just want it to work
- Willing to pay $5/month

---

## Questions for You

Before we proceed, please answer these to help choose the best option:

### 1. **How many videos per day?**
   - [ ] 1-2 videos (GitHub Actions FREE is fine)
   - [ ] 3-5 videos (GitHub Actions or Cloud Run)
   - [ ] 5-10 videos (Cloud Run or dedicated VM)
   - [ ] 10+ videos (Dedicated VM)

### 2. **How do you want to access transcripts?**
   - [ ] GitHub UI (download files manually)
   - [ ] Google Drive (auto-sync)
   - [ ] Web browser (cloud storage UI)
   - [ ] SFTP/file sync tool
   - [ ] Dropbox/OneDrive integration

### 3. **Budget comfort?**
   - [ ] $0/month only (GitHub Actions)
   - [ ] $2-5/month acceptable (Cloud Run/PythonAnywhere)
   - [ ] $5-10/month OK (Dedicated VM for full control)
   - [ ] No budget limit (choose best solution)

### 4. **Technical comfort level?**
   - [ ] Beginner (PythonAnywhere or GitHub Actions)
   - [ ] Intermediate (GitHub Actions or Cloud Run)
   - [ ] Advanced (Any option, can learn Docker)

### 5. **Where should `youtube_memory.json` be stored?**
   - [ ] GitHub repository (committed with code)
   - [ ] Cloud storage bucket (S3/GCS)
   - [ ] VM disk (if using dedicated server)
   - [ ] Don't care, whatever works

### 6. **Do you need to manually trigger runs?**
   - [ ] No, only automated daily run at 11:30 AM
   - [ ] Yes, sometimes want to run on-demand
   - [ ] Would be nice to have both options

### 7. **How important are logs/debugging?**
   - [ ] Critical - need to see what went wrong
   - [ ] Nice to have - occasionally check
   - [ ] Don't care - just want results

---

## Next Steps

**DO NOT IMPLEMENT YET - WAITING FOR YOUR ANSWERS** ✋

Once you answer the questions above, I will:
1. Create detailed implementation guide for chosen option
2. Write all configuration files
3. Provide step-by-step deployment instructions
4. Set up automated transcript retrieval
5. Test the entire workflow

**Please let me know**:
- Your answers to the questions
- Any specific preferences/constraints
- Any questions about the options

Then we'll proceed with implementation! 🚀
