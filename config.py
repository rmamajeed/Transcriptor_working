"""
Configuration for Transcriptinator - Automated Cloud Execution Mode

This file contains all configuration needed for automated runs (e.g., GitHub Actions).
Set AUTOMATED_MODE = True for cloud execution, False for interactive mode.
"""

# ============================================================================
# AUTOMATION MODE
# ============================================================================
AUTOMATED_MODE = True  # Set to False to use interactive menu

# ============================================================================
# PLAYLIST CONFIGURATION
# ============================================================================
# YouTube playlist to process automatically
PLAYLIST_URL = "https://www.youtube.com/playlist?list=PLA67COBNthEJbJCXwyjR9uHS1SJEOaRa5"

# Download settings
MAX_DOWNLOADS = None  # None = download ALL new videos, or set a number (e.g., 5)
SKIP_ALREADY_PROCESSED = True  # Always skip videos already in youtube_memory.json

# ============================================================================
# PROCESSING SETTINGS
# ============================================================================
# Metadata extraction level
# - "basic": 2 AI calls (faster, minimal metadata)
# - "enhanced": 4 AI calls (detailed metadata, graph-ready)
METADATA_LEVEL = "enhanced"

# ============================================================================
# FOLDER PATHS
# ============================================================================
DOWNLOADS_FOLDER = "downloads"
TRANSCRIPTS_FOLDER = "Transcripts"
