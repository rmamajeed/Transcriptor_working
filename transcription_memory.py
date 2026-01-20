"""
YouTube Transcription Memory System
Tracks processed YouTube videos to prevent duplicate transcriptions.
"""

import json
import os
import re
from datetime import datetime
from pathlib import Path


class TranscriptionMemory:
    def __init__(self, memory_file="youtube_memory.json"):
        """
        Initialize YouTube-only memory system
        
        Args:
            memory_file (str): Path to memory database file
        """
        self.memory_file = Path(memory_file)
        self.data = self._load_or_create_database()
    
    def _load_or_create_database(self):
        """Load existing database or create new one"""
        if self.memory_file.exists():
            try:
                with open(self.memory_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                print("⚠️  Memory file corrupted. Creating new memory database.")
                return self._create_empty_database()
        else:
            return self._create_empty_database()
    
    def _create_empty_database(self):
        """Create empty database structure"""
        return {
            "youtube_videos": {},
            "metadata": {
                "version": "1.0",
                "created_date": datetime.now().isoformat(),
                "last_updated": datetime.now().isoformat(),
                "total_processed": 0
            }
        }
    
    def _save_database(self):
        """Save database to file"""
        self.data["metadata"]["last_updated"] = datetime.now().isoformat()
        
        try:
            with open(self.memory_file, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"⚠️  Error saving memory database: {e}")
    
    def extract_video_id(self, url):
        """
        Extract YouTube video ID from URL
        
        Args:
            url (str): YouTube URL
            
        Returns:
            str: Video ID or None if not found
        """
        patterns = [
            r'(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/embed/)([a-zA-Z0-9_-]{11})',
            r'youtube\.com/.*[?&]v=([a-zA-Z0-9_-]{11})',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        return None
    
    def is_video_processed(self, url):
        """
        Check if YouTube video was already processed
        
        Args:
            url (str): YouTube URL
            
        Returns:
            dict: Processing info if found, None if not processed
        """
        video_id = self.extract_video_id(url)
        if not video_id:
            return None
        
        return self.data["youtube_videos"].get(video_id)
    
    def add_processed_video(self, video_info, transcript_files):
        """
        Add processed video to memory
        
        Args:
            video_info (dict): Video metadata from YouTubeAudioDownloader
            transcript_files (list): List of created transcript file paths
        """
        # Extract video ID from multiple possible sources
        video_id = None
        
        # Try direct ID field from yt-dlp (most reliable)
        if 'id' in video_info:
            video_id = video_info['id']
        
        # Try extracting from URL field
        elif 'url' in video_info:
            video_id = self.extract_video_id(video_info['url'])
        
        # Try extracting from webpage_url field (common in yt-dlp)
        elif 'webpage_url' in video_info:
            video_id = self.extract_video_id(video_info['webpage_url'])
        
        # Try extracting from original_url field
        elif 'original_url' in video_info:
            video_id = self.extract_video_id(video_info['original_url'])
        
        if not video_id:
            print("⚠️  Could not extract video ID from any source. Skipping memory storage.")
            print(f"Available fields: {list(video_info.keys())}")
            return
        
        # Store video information
        self.data["youtube_videos"][video_id] = {
            "video_id": video_id,
            "title": video_info.get('title', 'Unknown Title'),
            "channel": video_info.get('uploader', 'Unknown Channel'),
            "url": video_info.get('url', ''),
            "processed_date": datetime.now().isoformat(),
            "duration": video_info.get('duration', 0),
            "transcript_files": [os.path.basename(f) for f in transcript_files if f]
        }
        
        # Update metadata
        self.data["metadata"]["total_processed"] = len(self.data["youtube_videos"])
        
        # Save to file
        self._save_database()
        
        print(f"✅ Added '{video_info.get('title')}' to processing memory")
    
    def get_processing_stats(self):
        """Get memory statistics"""
        return {
            "total_videos": len(self.data["youtube_videos"]),
            "last_updated": self.data["metadata"]["last_updated"],
            "created_date": self.data["metadata"]["created_date"]
        }
    
    def display_processed_video_info(self, video_info):
        """Display information about already processed video"""
        print("\n" + "="*60)
        print("🔍 VIDEO ALREADY PROCESSED!")
        print("="*60)
        print(f"📺 Title: {video_info['title']}")
        print(f"📺 Channel: {video_info['channel']}")
        
        # Format duration nicely
        duration = video_info.get('duration', 0)
        if duration > 0:
            minutes = duration // 60
            seconds = duration % 60
            print(f"⏱️  Duration: {minutes}:{seconds:02d}")
        
        # Format date nicely
        try:
            processed_date = datetime.fromisoformat(video_info['processed_date'])
            formatted_date = processed_date.strftime("%Y-%m-%d %H:%M:%S")
            print(f"📅 Processed: {formatted_date}")
        except:
            print(f"📅 Processed: {video_info['processed_date']}")
        
        transcript_files = video_info.get('transcript_files', [])
        if transcript_files:
            print(f"📄 Transcripts: {', '.join(transcript_files)}")
        
        print("="*60)
    
    def list_all_processed_videos(self):
        """Display all processed videos"""
        videos = self.data["youtube_videos"]
        if not videos:
            print("📝 No videos have been processed yet.")
            return
        
        print(f"\n📊 PROCESSING HISTORY ({len(videos)} videos)")
        print("="*80)
        
        # Sort by processed date (newest first)
        sorted_videos = sorted(
            videos.values(), 
            key=lambda x: x.get('processed_date', ''), 
            reverse=True
        )
        
        for i, video in enumerate(sorted_videos, 1):
            print(f"{i:2d}. {video['title']}")
            print(f"    Channel: {video['channel']}")
            try:
                processed_date = datetime.fromisoformat(video['processed_date'])
                formatted_date = processed_date.strftime("%Y-%m-%d %H:%M")
                print(f"    Processed: {formatted_date}")
            except:
                print(f"    Processed: {video['processed_date']}")
            print(f"    URL: {video.get('url', 'N/A')}")
            print()
        
        print("="*80)
    
    def update_memory_from_info_files(self, downloads_folder, transcripts_folder):
        """
        Update memory with transcription results from .info.json files
        
        Args:
            downloads_folder (str): Path to downloads folder
            transcripts_folder (str): Path to transcripts folder
        """
        downloads_path = Path(downloads_folder)
        transcripts_path = Path(transcripts_folder)
        
        # Look for .info.json files that yt-dlp creates
        info_files = list(downloads_path.glob("*.info.json"))
        
        if not info_files:
            print("ℹ️  No YouTube info files found. Skipping memory update.")
            return
        
        print(f"📝 Updating memory from {len(info_files)} info file(s)...")
        
        for info_file in info_files:
            try:
                with open(info_file, 'r', encoding='utf-8') as f:
                    video_info = json.load(f)
                
                # Find corresponding transcript files
                base_name = info_file.stem.replace('.info', '')
                transcript_files = []
                
                # Look for transcript files with matching base name
                for ext in ['.md', '.txt']:
                    # Check for single file
                    transcript_path = transcripts_path / f"{base_name}{ext}"
                    if transcript_path.exists():
                        transcript_files.append(str(transcript_path))
                    
                    # Also check for chunked files (_part1, _part2, etc.)
                    chunked_files = list(transcripts_path.glob(f"{base_name}_part*{ext}"))
                    transcript_files.extend([str(f) for f in chunked_files])
                
                if transcript_files:
                    # Add to memory
                    self.add_processed_video(video_info, transcript_files)
                else:
                    print(f"⚠️  No transcript files found for {base_name}")
                
                # Clean up info file
                try:
                    info_file.unlink()
                    print(f"🗑️  Cleaned up info file: {info_file.name}")
                except:
                    print(f"⚠️  Could not delete info file: {info_file.name}")
                
            except Exception as e:
                print(f"⚠️  Error processing info file {info_file.name}: {e}")


def main():
    """Test function for the memory system"""
    print("YouTube Transcription Memory System Test")
    print("="*50)
    
    memory = TranscriptionMemory()
    
    # Display current stats
    stats = memory.get_processing_stats()
    print(f"Total videos in memory: {stats['total_videos']}")
    
    # List all processed videos
    memory.list_all_processed_videos()


if __name__ == "__main__":
    main()
