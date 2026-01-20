import os
import sys
import shutil
from pathlib import Path

# Import configuration
import config

# Import the downloader class from youtube_audio_downloader.py
from youtube_audio_downloader import YouTubeAudioDownloader

# Import the main function from audio_process_and_transcribe.py
from audio_process_and_transcribe import main as process_and_transcribe_main

# Import the memory system
from transcription_memory import TranscriptionMemory

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
        print("1. Download single video")
        print("2. Download playlist")
        print("3. Skip download (process existing files)")
        print("4. View processing history")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            url = input("Enter YouTube video URL: ").strip()
            if url:
                # Check if already processed
                processed_info = memory.is_video_processed(url)
                if processed_info:
                    memory.display_processed_video_info(processed_info)
                    
                    continue_choice = input("\nProcess anyway? (y/N): ").strip().lower()
                    if continue_choice != 'y':
                        print("Skipping already processed video.")
                        continue
                
                # Proceed with download
                result = downloader.download_audio(url)
                print(f"\nDownload Result: {result}")
                break
                
        elif choice == '2':
            playlist_url = input("Enter YouTube playlist URL: ").strip()
            max_downloads = input("Enter max downloads (press Enter for all): ").strip()
            max_downloads = int(max_downloads) if max_downloads.isdigit() else None
            
            if playlist_url:
                # Use memory-aware playlist download
                result = downloader.download_playlist_with_memory(playlist_url, memory, max_downloads)
                
                if result['success']:
                    print(f"\n✅ Playlist Processing Complete!")
                    print(f"   Downloaded: {result.get('downloaded', 0)} videos")
                    print(f"   Skipped: {result.get('skipped', 0)} videos")
                    if result.get('failed', 0) > 0:
                        print(f"   Failed: {result.get('failed', 0)} videos")
                else:
                    print(f"\n❌ Playlist processing failed: {result.get('error', 'Unknown error')}")
                
                break
                
        elif choice == '3':
            print("Skipping download. Will process existing files in 'downloads' folder.")
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
    Automated download mode - no user interaction required.
    Downloads from hardcoded playlist URL in config.py.
    Automatically skips already-processed videos.
    """
    print("\n" + "=" * 70)
    print("🤖 AUTOMATED MODE - Cloud Execution")
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
    
    # Download playlist with memory-aware skipping
    print(f"\n📥 Starting playlist download...")
    result = downloader.download_playlist_with_memory(
        config.PLAYLIST_URL, 
        memory, 
        max_downloads=config.MAX_DOWNLOADS,
        auto_skip=True  # Automated mode: always skip processed videos without prompting
    )
    
    # Display results
    if result['success']:
        print(f"\n✅ Playlist Download Complete!")
        print(f"   ✓ Downloaded: {result.get('downloaded', 0)} videos")
        print(f"   ⏭️  Skipped: {result.get('skipped', 0)} videos (already processed)")
        if result.get('failed', 0) > 0:
            print(f"   ❌ Failed: {result.get('failed', 0)} videos")
    else:
        print(f"\n❌ Playlist download failed: {result.get('error', 'Unknown error')}")
        print("   Stopping pipeline execution.")
        sys.exit(1)

def delete_audio_files(audio_folder):
    exts = ('.mp3', '.m4a', '.wav', '.ogg', '.flac', '.weba', '.webm')
    for f in os.listdir(audio_folder):
        if f.lower().endswith(exts):
            try:
                os.remove(os.path.join(audio_folder, f))
            except Exception as e:
                print(f"Error deleting {f}: {e}")

def main():
    downloads_folder = config.DOWNLOADS_FOLDER
    transcripts_folder = config.TRANSCRIPTS_FOLDER

    # Initialize memory system
    memory = TranscriptionMemory()

    # Step 1: Download audio files (automated or interactive mode)
    if config.AUTOMATED_MODE:
        print("\n🤖 Running in AUTOMATED mode (cloud execution)")
        automated_download(memory)
    else:
        print("\n👤 Running in INTERACTIVE mode (manual input)")
        prompt_for_download()

    # Step 2: Chunk and transcribe with metadata
    print("\n" + "=" * 70)
    print("🎬 Starting transcription and metadata extraction...")
    print("=" * 70)
    sys.argv = ["audio_process_and_transcribe.py", downloads_folder, "-o", transcripts_folder, "--metadata-level", config.METADATA_LEVEL]
    process_and_transcribe_main(memory_system=memory, downloads_folder=downloads_folder)

    # Note: Memory update and audio deletion now happen per-file in audio_process_and_transcribe.py
    print("\n" + "=" * 70)
    print("✅ Pipeline execution complete!")
    print("=" * 70)

if __name__ == "__main__":
    main()
