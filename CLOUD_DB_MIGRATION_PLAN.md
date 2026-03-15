# Cloud Database Migration Plan

We will migrate the application from using a local `youtube_memory.json` to a **Supabase PostgreSQL Database**. This ensures that wherever the application runs (VPS, Laptop, or multiple servers simultaneously), they all share the exact same memory bank, preventing duplicate transcriptions forever.

## Why Supabase?
- **Free Tier:** Excellent free tier with a fast, scalable PostgreSQL database.
- **REST API:** Supabase provides an auto-generated REST API over the database, manipulated via the `supabase-py` client library.
- **Structured Data:** Perfect for your structured video data. We will create a single `processed_videos` table to exactly map your existing memory structure.

## Implementation Steps

### 1. Account Setup (User Action)
1. Go to [Supabase](https://supabase.com/) and create a free account.
2. Create a new "Project" (this will provision a database). Let the setup complete.
3. Once created, go to the "Project Settings" -> "API" section on the left sidebar.
4. Copy the `Project URL` and the `Project API Key` (specifically the `anon` / `public` key).
5. In the Supabase SQL Editor, we will need to create a table. You can run this exact SQL to create it:
```sql
CREATE TABLE processed_videos (
    video_id TEXT PRIMARY KEY,
    title TEXT,
    channel TEXT,
    url TEXT,
    processed_date TIMESTAMP WITH TIME ZONE,
    duration INTEGER,
    transcript_files JSONB
);
```

### 2. Application Updates
- Add `supabase` to `requirements.txt`.
- Update `.env` and `.env.example` to include `SUPABASE_URL` and `SUPABASE_KEY`.
- Modify `transcription_memory.py` to replace all local JSON file logic with Supabase API queries. This includes updating:
  - `is_video_processed()`
  - `add_processed_video()`
  - `get_processing_stats()`
  - `list_all_processed_videos()`

### 3. Data Migration
We will create a temporary Python script (`migrate_to_cloud.py`) that reads your current `youtube_memory.json` and bulk uploads all the history to the new Supabase database so nothing is lost.

### 4. Verification
- We run `python transcription_memory.py` to test the connection and see the stats.
- We run a test download to ensure the system successfully interacts with the cloud memory.
