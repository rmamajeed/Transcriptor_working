# Cloud Database Migration Plan

We will migrate the application from using a local `youtube_memory.json` to a **MongoDB Atlas Cloud Database**. This ensures that wherever the application runs (VPS, Laptop, or multiple servers simultaneously), they all share the exact same memory bank, preventing duplicate transcriptions forever.

## Why MongoDB Atlas?
- **Free Tier:** 512MB storage which is more than enough for millions of video records.
- **No Schema Required:** It stores JSON-like documents, making it a perfect 1-to-1 drop-in replacement for your current `youtube_memory.json` structure.
- **Python Support:** The `pymongo` library is the industry standard and extremely robust.

## Implementation Steps

### 1. Account Setup (User Action)
1. Go to [MongoDB Atlas](https://www.mongodb.com/atlas/database) and create a free account.
2. Create a free "M0" cluster. 
3. Under Database Access, create a user with a password.
4. Under Network Access, allow access from anywhere (`0.0.0.0/0`).
5. Click "Connect", select "Drivers", choose Python, and copy the Connection String URI.

### 2. Application Updates
- Add `pymongo` to `requirements.txt`.
- Update `.env` and `.env.example` to include `MONGODB_URI`.
- Modify `transcription_memory.py` to replace all local JSON file logic with MongoDB database queries. This includes updating:
  - `is_video_processed()`
  - `add_processed_video()`
  - `get_processing_stats()`
  - `list_all_processed_videos()`

### 3. Data Migration
We will create a temporary Python script (`migrate_to_cloud.py`) that reads your current `youtube_memory.json` and bulk uploads all the history to the new cloud database so nothing is lost.

### 4. Verification
- We run `python transcription_memory.py` to test the connection and see the stats.
- We run a test download to ensure the system successfully interacts with the cloud memory.
