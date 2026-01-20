
"""
YouTube Audio Downloader
A simple backend application to download audio from YouTube videos using yt-dlp.
"""

import os
import sys
import json
import traceback
from pathlib import Path
import logging

class YouTubeAudioDownloader:
    def __init__(self, output_dir="downloads", audio_format="mp3", audio_quality="192"):
        """
        Initialize the YouTube Audio Downloader

        Args:
            output_dir (str): Directory to save downloaded audio files
            audio_format (str): Audio format (mp3, m4a, wav, etc.)
            audio_quality (str): Audio quality (best, worst, or bitrate like "192")
        """
        self.output_dir = Path(output_dir)
        self.audio_format = audio_format
        self.audio_quality = audio_quality

        # Create output directory if it doesn't exist
        self.output_dir.mkdir(exist_ok=True)

        # Configure logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('downloader.log'),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)

        # Check if yt-dlp is available
        try:
            import yt_dlp
            self.yt_dlp = yt_dlp
            self.logger.info("yt-dlp library found and imported successfully")
        except ImportError:
            self.logger.error("yt-dlp not found. Please install it using: pip install yt-dlp")
            sys.exit(1)

    def configure_ydl_options(self, custom_filename=None, include_date=True):
        """
        Configure yt-dlp options for audio extraction

        Args:
            custom_filename (str): Custom filename template
            include_date (bool): Whether to include upload date in filename

        Returns:
            dict: yt-dlp options dictionary
        """

        # Default filename template with date in YYYYMMDD format
        if custom_filename:
            filename_template = custom_filename
        elif include_date:
            # Use upload_date which yt-dlp provides in YYYYMMDD format
            # If upload_date is not available, use "NODATE" as fallback
            # Format: ChannelName_VideoTitle_UploadDate.ext
            filename_template = "%(uploader)s_%(title)s_%(upload_date|NODATE)s.%(ext)s"
        else:
            filename_template = "%(uploader)s_%(title)s.%(ext)s"

        # Configure yt-dlp options
        ydl_opts = {
            'format': 'bestaudio/best',  # Download best audio quality available
            'outtmpl': str(self.output_dir / filename_template),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': self.audio_format,
                'preferredquality': self.audio_quality,
            }],
            'ffmpeg_location': None,  # Auto-detect FFmpeg
            'writeinfojson': True,  # Save video info as JSON
            'writethumbnail': False,  # Don't download thumbnail by default
            'ignoreerrors': False,
            'noplaylist': True,  # Download single video only by default
        }

        return ydl_opts

    def validate_url(self, url):
        """
        Validate if the provided URL is a valid YouTube URL

        Args:
            url (str): YouTube URL to validate

        Returns:
            bool: True if valid, False otherwise
        """
        valid_domains = [
            'youtube.com', 'youtu.be', 'www.youtube.com', 'm.youtube.com'
        ]

        return any(domain in url.lower() for domain in valid_domains)

    def get_video_info(self, url):
        """
        Extract video information without downloading

        Args:
            url (str): YouTube URL

        Returns:
            dict: Video information or None if error
        """
        try:
            ydl_opts = {
                'quiet': True,
                'no_warnings': True,
            }

            with self.yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)

                return {
                    'id': info.get('id', ''),  # Add video ID for memory system
                    'title': info.get('title', 'Unknown Title'),
                    'duration': info.get('duration', 0),
                    'uploader': info.get('uploader', 'Unknown Uploader'),
                    'upload_date': info.get('upload_date', 'Unknown Date'),
                    'view_count': info.get('view_count', 0),
                    'like_count': info.get('like_count', 0),
                    'description': info.get('description', '')[:200] + '...',
                    'url': url,  # Add original URL for memory system
                }
        except Exception as e:
            self.logger.error(f"Error extracting video info: {str(e)}")
            return None

    def download_audio(self, url, custom_filename=None, include_thumbnail=False):
        """
        Download audio from YouTube URL

        Args:
            url (str): YouTube URL
            custom_filename (str): Custom filename template
            include_thumbnail (bool): Whether to download thumbnail

        Returns:
            dict: Download result with status and information
        """

        if not self.validate_url(url):
            return {
                'success': False,
                'error': 'Invalid YouTube URL provided',
                'url': url
            }

        try:
            # Get video info first
            video_info = self.get_video_info(url)
            if not video_info:
                return {
                    'success': False,
                    'error': 'Could not extract video information',
                    'url': url
                }

            self.logger.info(f"Starting download for: {video_info['title']}")

            # Configure download options
            ydl_opts = self.configure_ydl_options(custom_filename)
            ydl_opts['writethumbnail'] = include_thumbnail

            # Download the audio
            with self.yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            self.logger.info(f"Successfully downloaded: {video_info['title']}")

            return {
                'success': True,
                'video_info': video_info,
                'output_dir': str(self.output_dir),
                'audio_format': self.audio_format,
                'url': url
            }

        except self.yt_dlp.utils.DownloadError as e:
            error_msg = f"Download error: {str(e)}"
            self.logger.error(error_msg)
            return {
                'success': False,
                'error': error_msg,
                'url': url
            }
        except Exception as e:
            error_msg = f"Unexpected error: {str(e)}"
            self.logger.error(error_msg)
            self.logger.error(traceback.format_exc())
            return {
                'success': False,
                'error': error_msg,
                'url': url
            }

    def get_playlist_info(self, playlist_url, max_downloads=None):
        """
        Extract playlist information and individual video URLs
        
        Args:
            playlist_url (str): YouTube playlist URL
            max_downloads (int): Maximum number of videos to process
            
        Returns:
            dict: Playlist info with video list or error
        """
        try:
            # Clean the playlist URL - extract just the list parameter
            import re
            list_match = re.search(r'[?&]list=([a-zA-Z0-9_-]+)', playlist_url)
            if list_match:
                clean_playlist_url = f"https://www.youtube.com/playlist?list={list_match.group(1)}"
                print(f"   🔧 Cleaned URL: {clean_playlist_url}")
            else:
                clean_playlist_url = playlist_url
            
            ydl_opts = {
                'quiet': True,
                'no_warnings': True,
                'extract_flat': True,  # Only get basic info, don't download
                'noplaylist': False
            }
            
            if max_downloads:
                ydl_opts['playlistend'] = max_downloads
            
            with self.yt_dlp.YoutubeDL(ydl_opts) as ydl:
                playlist_info = ydl.extract_info(clean_playlist_url, download=False)
                
                if not playlist_info:
                    return {
                        'success': False,
                        'error': 'Could not extract playlist information'
                    }
                
                # Extract video entries
                entries = playlist_info.get('entries', [])
                videos = []
                
                for entry in entries:
                    if entry:  # Some entries might be None for private/deleted videos
                        video_url = f"https://www.youtube.com/watch?v={entry.get('id', '')}"
                        videos.append({
                            'id': entry.get('id', ''),
                            'title': entry.get('title', 'Unknown Title'),
                            'url': video_url,
                            'duration': entry.get('duration', 0),
                            'uploader': entry.get('uploader', 'Unknown Channel')
                        })
                
                return {
                    'success': True,
                    'playlist_title': playlist_info.get('title', 'Unknown Playlist'),
                    'playlist_url': playlist_url,
                    'total_videos': len(videos),
                    'videos': videos
                }
                
        except Exception as e:
            error_msg = f"Playlist info extraction error: {str(e)}"
            self.logger.error(error_msg)
            return {
                'success': False,
                'error': error_msg,
                'playlist_url': playlist_url
            }

    def download_playlist_with_memory(self, playlist_url, memory_system, max_downloads=None, auto_skip=True):
        """
        Download playlist with memory-aware duplicate prevention
        
        Args:
            playlist_url (str): YouTube playlist URL
            memory_system: TranscriptionMemory instance
            max_downloads (int, optional): Maximum number of videos to download. None = all videos
            auto_skip (bool): If True, automatically skip processed videos without prompting (for automation)
        
        Returns:
            dict: Summary with 'success', 'downloaded', 'skipped', 'failed' counts
        """
        print(f"\n🔍 Checking playlist: {playlist_url}")
        
        # Get playlist info
        playlist_info = self.get_playlist_info(playlist_url, max_downloads)
        
        if not playlist_info['success']:
            return playlist_info
        
        print(f"\n🎵 Playlist: {playlist_info['playlist_title']}")
        print(f"📹 Total videos: {playlist_info['total_videos']}")
        print("=" * 60)
        
        # Check each video against memory
        videos_to_download = []
        already_processed = []
        
        for i, video in enumerate(playlist_info['videos'], 1):
            print(f"\n{i:2d}. Checking: {video['title'][:50]}...")
            
            processed_info = memory_system.is_video_processed(video['url'])
            if processed_info:
                print(f"    ⚠️  Already processed on {processed_info.get('processed_date', 'unknown date')}")
                already_processed.append({
                    'video': video,
                    'processed_info': processed_info
                })
            else:
                print(f"    ✅ New video - will download")
                videos_to_download.append(video)
        
        # Display summary
        print(f"\n📊 MEMORY CHECK SUMMARY:")
        print(f"   🆕 New videos to download: {len(videos_to_download)}")
        print(f"   ♻️  Already processed: {len(already_processed)}")
        
        # Handle already processed videos
        if already_processed:
            if auto_skip:
                # AUTOMATED MODE: Always skip processed videos
                print(f"\n✅ AUTO-SKIP enabled: Skipping {len(already_processed)} already processed video(s)")
            else:
                # INTERACTIVE MODE: Ask user
                print(f"\n⚠️  Found {len(already_processed)} already processed video(s):")
                for item in already_processed:
                    video = item['video']
                    print(f"   - {video['title']}")
                
                choice = input(f"\nHow to handle already processed videos?\n"
                              f"1. Skip all processed videos (recommended)\n"
                              f"2. Download all anyway\n"
                              f"3. Choose for each video\n"
                              f"Enter choice (1-3): ").strip()
                
                if choice == '2':
                    # Download all anyway
                    videos_to_download.extend([item['video'] for item in already_processed])
                    print("✅ Will download all videos including already processed ones.")
                elif choice == '3':
                    # Ask for each video
                    for item in already_processed:
                        video = item['video']
                        memory_system.display_processed_video_info(item['processed_info'])
                        user_choice = input(f"Download '{video['title']}' anyway? (y/N): ").strip().lower()
                        if user_choice == 'y':
                            videos_to_download.append(video)
                else:
                    # Default: skip processed videos
                    print("✅ Will skip already processed videos.")
        
        # Download the selected videos
        if not videos_to_download:
            return {
                'success': True,
                'message': 'No new videos to download',
                'playlist_info': playlist_info,
                'downloaded': 0,
                'skipped': len(already_processed)
            }
        
        print(f"\n🚀 Starting download of {len(videos_to_download)} video(s)...")
        
        download_results = []
        successful_downloads = 0
        
        for i, video in enumerate(videos_to_download, 1):
            print(f"\n📥 Downloading {i}/{len(videos_to_download)}: {video['title']}")
            
            result = self.download_audio(video['url'])
            download_results.append({
                'video': video,
                'result': result
            })
            
            if result['success']:
                successful_downloads += 1
                print(f"✅ Downloaded successfully")
            else:
                print(f"❌ Download failed: {result.get('error', 'Unknown error')}")
        
        return {
            'success': True,
            'playlist_info': playlist_info,
            'download_results': download_results,
            'downloaded': successful_downloads,
            'skipped': len(already_processed),
            'failed': len(videos_to_download) - successful_downloads
        }
        """
        Download playlist with memory-aware duplicate prevention
        
        Args:
            playlist_url (str): YouTube playlist URL
            memory_system: TranscriptionMemory instance
            max_downloads (int, optional): Maximum number of videos to download. None = all videos
            auto_skip (bool): If True, automatically skip processed videos without prompting (for automation)
        
        Returns:
            dict: Summary with 'success', 'downloaded', 'skipped', 'failed' counts
        """
        print(f"\n🔍 Checking playlist: {playlist_url}")
        
        # Get playlist info
        playlist_info = self.get_playlist_info(playlist_url, max_downloads)
        
        return {
            'success': True,
            'playlist_info': playlist_info,
            'download_results': download_results,
            'downloaded': successful_downloads,
            'skipped': len(already_processed),
            'failed': len(videos_to_download) - successful_downloads
        }

    def download_playlist(self, playlist_url, max_downloads=None):
        """
        Download audio from YouTube playlist (legacy method)

        Args:
            playlist_url (str): YouTube playlist URL
            max_downloads (int): Maximum number of videos to download

        Returns:
            dict: Download results
        """
        try:
            ydl_opts = self.configure_ydl_options()
            ydl_opts['noplaylist'] = False  # Enable playlist mode

            if max_downloads:
                ydl_opts['playlistend'] = max_downloads

            with self.yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([playlist_url])

            return {
                'success': True,
                'playlist_url': playlist_url,
                'output_dir': str(self.output_dir)
            }

        except Exception as e:
            error_msg = f"Playlist download error: {str(e)}"
            self.logger.error(error_msg)
            return {
                'success': False,
                'error': error_msg,
                'playlist_url': playlist_url
            }

def main():
    """
    Main function to demonstrate the usage
    """
    print("YouTube Audio Downloader")
    print("=" * 50)

    # Initialize downloader
    downloader = YouTubeAudioDownloader(
        output_dir="downloads",
        audio_format="mp3",
        audio_quality="192"
    )

    while True:
        print("\nOptions:")
        print("1. Download single video")
        print("2. Download playlist")
        print("3. Get video information")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == '1':
            url = input("Enter YouTube video URL: ").strip()
            if url:
                result = downloader.download_audio(url)
                print(f"\nDownload Result: {json.dumps(result, indent=2)}")

        elif choice == '2':
            playlist_url = input("Enter YouTube playlist URL: ").strip()
            max_downloads = input("Enter max downloads (press Enter for all): ").strip()
            max_downloads = int(max_downloads) if max_downloads.isdigit() else None

            if playlist_url:
                result = downloader.download_playlist(playlist_url, max_downloads)
                print(f"\nPlaylist Download Result: {json.dumps(result, indent=2)}")

        elif choice == '3':
            url = input("Enter YouTube video URL: ").strip()
            if url:
                info = downloader.get_video_info(url)
                print(f"\nVideo Information: {json.dumps(info, indent=2)}")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
