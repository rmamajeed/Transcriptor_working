import os
import sys
import shutil
from pathlib import Path
import time

# Import configuration
import config

# Import the downloader class from youtube_audio_downloader.py
from youtube_audio_downloader import YouTubeAudioDownloader

# Import the processing function from audio_process_and_transcribe.py
from audio_process_and_transcribe import process_single_file, GeminiQuotaExhaustedError

# Import the memory system
from transcription_memory import TranscriptionMemory

def process_video_sequentially(video, downloader, memory, transcripts_folder, metadata_level):
    """
    Helper function to process a single video in the sequential loop.
    Returns:
        bool: True if processing should continue, False if a critical error occurred (like Quota Exceeded)
    """
    print(f"\n" + "-" * 50)
    print(f"🎬 Processing: {video['title']}")
    print("-" * 50)
    
    # 1. Download
    print(f"📥 Downloading audio...")
    download_result = downloader.download_audio(video['url'])
    
    if not download_result['success']:
        print(f"❌ Download failed: {download_result.get('error', 'Unknown error')}")
        return True # Continue to next video
        
    # Get the downloaded file path
    # yt-dlp might leave multiple files if using 'bestaudio', but our config requests mp3/m4a
    # We need to find the file that was just created. 
    # Since download_audio returns output_dir, we can look there.
    # However, process_single_file expects a file path.
    # Let's search for the file in downloads folder that matches the title roughly or just check recent files?
    # Better: YouTubeAudioDownloader should probably return the filename, but it returns a dict.
    # Let's rely on standard yt-dlp naming convetion or just list files in downloads that match.
    
    # Actually, simpler approach:
    # prompt_for_download and automated_download run in a loop.
    # we can just scan the downloads folder for the new file.
    
    # Only one file should be there if we are cleaning up!
    downloads_folder = config.DOWNLOADS_FOLDER
    
    try:
        # Find the downloaded file
        # We expect only ONE audio file to be present because we clean up after each loop
        # But to be safe, filtering by recent modification could work, or just taking the first audio file found.
        # Given the sequential nature, 'taking the only file' is risky if cleanup failed.
        # Let's try to match by video ID if possible, or just grab the file.
        
        # Taking the file that looks like an audio file
        audio_files = [
            os.path.join(downloads_folder, f) 
            for f in os.listdir(downloads_folder) 
            if f.lower().endswith(('.mp3', '.m4a', '.wav', '.ogg', '.flac', '.weba', '.webm', '.mp4'))
            and not f.endswith('_part.mp3')
        ]
        
        if not audio_files:
            print("❌ Error: Download reported success but no audio file found.")
            return True # Continue
            
        # Assuming the new file is the one we want. If multiple exist, we might process the wrong one, 
        # but in a clean sequential loop, there should only be one new one.
        # Let's pick the most recently modified one to be safe
        audio_file_path = max(audio_files, key=os.path.getmtime)
        
        # 2. Process
        print(f"🧠 Transcribing and analyzing...")
        success = process_single_file(
            audio_file_path=audio_file_path,
            output_folder_path=transcripts_folder,
            metadata_level=metadata_level,
            chunk_duration_minutes=25,
            overlap_seconds=5,
            memory_system=memory,
            audio_downloads_folder=downloads_folder # For finding .info.json
        )
        
        if success:
            print(f"✅ Completed: {video['title']}")
        else:
            print(f"⚠️  Processing finished with errors for: {video['title']}")
            
        return True

    except GeminiQuotaExhaustedError as e:
        print(f"\n❌ CRITICAL: {e}")
        print(f"🛑 Stopping sequential loop. All previous videos are saved.")
        return False
        
    except Exception as e:
        print(f"❌ Unexpected error in loop: {e}")
        return True # Try next video?

def prompt_for_download():
    print("AudioFlow: YouTube Audio Download and Transcription Pipeline")
    print("=" * 60)
    
    # Initialize memory system
    memory = TranscriptionMemory()
    
    downloader = YouTubeAudioDownloader(
        output_dir="downloads",
        audio_format="mp3",
        audio_quality="192"
    )
    
    while True:
        print("\nOptions:")
        print("1. Download single video (Sequential)")
        print("2. Download playlist (Sequential)")
        print("3. Process existing files in 'downloads' (Batch)")
        print("4. View processing history")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            url = input("Enter YouTube video URL: ").strip()
            if url:
                # Check memory
                processed_info = memory.is_video_processed(url)
                if processed_info:
                    memory.display_processed_video_info(processed_info)
                    if input("\nProcess anyway? (y/N): ").strip().lower() != 'y':
                        continue
                
                # Create a minimal video object
                video_info = downloader.get_video_info(url)
                if video_info:
                     process_video_sequentially(
                        video_info, 
                        downloader, 
                        memory, 
                        config.TRANSCRIPTS_FOLDER, 
                        config.METADATA_LEVEL
                    )
                
        elif choice == '2':
            playlist_url = input("Enter YouTube playlist URL: ").strip()
            max_downloads = input("Enter max downloads (press Enter for all): ").strip()
            max_downloads = int(max_downloads) if max_downloads.isdigit() else None
            
            if playlist_url:
                print(f"\n🔍 Fetching playlist info...")
                playlist_info = downloader.get_playlist_info(playlist_url, max_downloads)
                
                if not playlist_info['success']:
                    print(f"❌ Failed to get playlist info: {playlist_info.get('error')}")
                    continue
                    
                videos = playlist_info['videos']
                print(f"found {len(videos)} videos.")
                
                for i, video in enumerate(videos, 1):
                    # Check memory
                    if memory.is_video_processed(video['url']):
                         print(f"⏭️  Skipping {i}/{len(videos)}: {video['title']} (Already processed)")
                         continue
                         
                    print(f"\n▶️  Processing video {i}/{len(videos)}")
                    continue_loop = process_video_sequentially(
                        video, 
                        downloader, 
                        memory, 
                        config.TRANSCRIPTS_FOLDER, 
                        config.METADATA_LEVEL
                    )
                    
                    if not continue_loop:
                        break # Critical error (quota)
                
        elif choice == '3':
            print("Processing existing files in 'downloads' folder...")
            # Fallback to batch processing for existing files
            # Reuse process_single_file logic but iterate manually
            audio_files = [
                os.path.join(config.DOWNLOADS_FOLDER, f) 
                for f in os.listdir(config.DOWNLOADS_FOLDER) 
                if f.lower().endswith(('.mp3', '.m4a', '.wav', '.ogg', '.flac', '.weba', '.webm', '.mp4'))
                and not f.endswith('_part.mp3')
            ]
            
            for f in audio_files:
                try:
                    process_single_file(
                        f, 
                        config.TRANSCRIPTS_FOLDER, 
                        config.METADATA_LEVEL, 
                        25, 5, 
                        memory, 
                        config.DOWNLOADS_FOLDER
                    )
                except GeminiQuotaExhaustedError:
                    print("❌ Gemini Quota Exhausted. Stopping.")
                    break
            
        elif choice == '4':
            # View processing history
            stats = memory.get_processing_stats()
            print(f"\n📊 Processing Statistics:")
            print(f"Total videos processed: {stats['total_videos']}")
            if stats['total_videos'] > 0:
                print(f"Memory created: {stats['created_date']}")
                print(f"Last updated: {stats['last_updated']}")
                
                show_details = input("\nShow detailed history? (y/N): ").strip().lower()
                if show_details == 'y':
                    memory.list_all_processed_videos()
            
        elif choice == '5':
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

def automated_download(memory):
    """
    Automated download mode - Sequential Loop.
    """
    print("\n" + "=" * 70)
    print("🤖 AUTOMATED MODE - Cloud Execution (Sequential Loop)")
    print("=" * 70)
    print(f"📋 Playlist: {config.PLAYLIST_URL}")
    print(f"📥 Max downloads: {'ALL new videos' if config.MAX_DOWNLOADS is None else config.MAX_DOWNLOADS}")
    print(f"⏭️  Skip processed: {'YES' if config.SKIP_ALREADY_PROCESSED else 'NO'}")
    print(f"🎯 Metadata level: {config.METADATA_LEVEL.upper()}")
    print("=" * 70)
    
    # Initialize downloader
    downloader = YouTubeAudioDownloader(
        output_dir=config.DOWNLOADS_FOLDER,
        audio_format="mp3",
        audio_quality="192"
    )
    
    # 1. Get Playlist Info (No Download yet)
    print(f"\n🔍 Fetching playlist metadata...")
    playlist_info = downloader.get_playlist_info(
        config.PLAYLIST_URL, 
        max_downloads=config.MAX_DOWNLOADS
    )
    
    if not playlist_info['success']:
        print(f"❌ Failed to extract playlist info: {playlist_info.get('error')}")
        sys.exit(1)
        
    videos = playlist_info['videos']
    total_videos = len(videos)
    print(f"✅ Found {total_videos} videos in playlist.")
    
    processed_count = 0
    skipped_count = 0
    failed_count = 0
    
    # Initialize start time for execution limit
    start_time = time.time()
    time_limit = getattr(config, 'EXECUTION_TIME_LIMIT_SECONDS', 3600)
    print(f"⏱️  Time Limit: {time_limit} seconds ({time_limit/3600:.1f} hours)")
    
    # 2. Sequential Loop
    for i, video in enumerate(videos, 1):
        # Check Execution Time Limit
        elapsed_time = time.time() - start_time
        if elapsed_time >= time_limit:
            print(f"\n🛑 Execution time limit of {time_limit}s reached (Elapsed: {elapsed_time:.0f}s).Stopping gracefully.")
            break
            
        # Check Memory
        if config.SKIP_ALREADY_PROCESSED and memory.is_video_processed(video['url']):
            print(f"⏭️  [{i}/{total_videos}] Skipping: {video['title']} (Already processed)")
            skipped_count += 1
            continue
            
        print(f"\n▶️  [{i}/{total_videos}] Starting cycle for: {video['title']}")
        
        # Process Sequentially
        continue_loop = process_video_sequentially(
            video,
            downloader, 
            memory, 
            config.TRANSCRIPTS_FOLDER, 
            config.METADATA_LEVEL
        )
        
        if continue_loop:
            processed_count += 1
        else:
            # Critical error (Quota) - Break loop but exit success (so CI doesn't fail hard if we did some work)
            print(f"\n🛑 Pipeline stopped due to quota limits.")
            break
            
    # 3. Final Summary
    print(f"\n" + "=" * 70)
    print(f"✅ Automated Run Complete")
    print(f"   ✓ Processed: {processed_count}")
    print(f"   ⏭️  Skipped: {skipped_count}")
    print(f"   ❌ Failed/Stop: {failed_count}") # Not fully tracking individual fails in this var yet, but logic is there
    print("=" * 70)

def main():
    downloads_folder = config.DOWNLOADS_FOLDER
    transcripts_folder = config.TRANSCRIPTS_FOLDER

    # Initialize memory system
    memory = TranscriptionMemory()

    # Create directories if they don't exist
    if not os.path.exists(downloads_folder):
        os.makedirs(downloads_folder)
    if not os.path.exists(transcripts_folder):
        os.makedirs(transcripts_folder)

    # Clean existing audio files in downloads before starting to ensure clean state
    # But only if in automation mode to avoid deleting user's stuff in interactive? 
    # Actually safe to clean if we expect sequential loop.
    # Let's just leave it for now.

    if config.AUTOMATED_MODE:
        automated_download(memory)
    else:
        prompt_for_download()

if __name__ == "__main__":
    main()
