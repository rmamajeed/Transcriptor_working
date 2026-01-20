# Application Modes & Options Guide

## 🎯 **Yes! You Have TWO Ways to Run the Application**

Your application supports:
1. **Full Pipeline** (YouTube download + processing)
2. **Standalone Processing** (audio files only)

Plus **TWO metadata levels**:
- **Basic**: Fast, minimal API calls
- **Enhanced**: Graph-ready, comprehensive metadata

---

## 📋 **Mode 1: Full Pipeline** (run_full_audio_pipeline.py)

### **What It Does**
Complete YouTube → Audio → Transcription → Markdown workflow

### **How to Run**
```bash
python run_full_audio_pipeline.py
```

### **Workflow Steps**
1. **Download** YouTube video/playlist
2. **Process** audio files
3. **Transcribe** with Gemini
4. **Extract** metadata (basic or enhanced)
5. **Update** processing memory
6. **Cleanup** audio files

### **Features**
- ✅ YouTube downloader integration
- ✅ Memory system (tracks processed videos)
- ✅ Auto cleanup of audio files
- ✅ Playlist support
- ✅ Skip already-processed videos

### **Options Menu**
```
1. Download single video
2. Download playlist
3. Skip download (process existing files)  ← Use this!
4. View processing history
5. Exit
```

### **Metadata Level**
**Hardcoded to: `enhanced`** (Line 120)
```python
sys.argv = [..., "--metadata-level", "enhanced"]
```

**To change to basic**:
Edit line 120 in `run_full_audio_pipeline.py`:
```python
sys.argv = [..., "--metadata-level", "basic"]  # Change here
```

---

## 📋 **Mode 2: Standalone Processing** (audio_process_and_transcribe.py)

### **What It Does**
Process audio files directly (no YouTube download)

### **How to Run**
```bash
python audio_process_and_transcribe.py <audio_folder> [OPTIONS]
```

### **Basic Usage**
```bash
# Enhanced metadata (default)
python audio_process_and_transcribe.py downloads/

# Basic metadata (faster)
python audio_process_and_transcribe.py downloads/ --metadata-level basic
```

### **All Command-Line Options**

#### **Required Argument**
```bash
<audio_folder>    # Path to folder with audio files
```

#### **Optional Arguments**
```bash
-o, --output_folder <path>       # Output folder (default: 'Transcripts')
--metadata-level <basic|enhanced> # Metadata mode (default: 'enhanced')
--chunk_duration <minutes>        # Chunk size (default: 25 minutes)
--overlap <seconds>              # Chunk overlap (default: 5 seconds)
```

### **Full Examples**

**Example 1: Default (Enhanced)**
```bash
python audio_process_and_transcribe.py downloads/
# - Output: Transcripts/
# - Metadata: Enhanced
# - Chunks: 25 min
# - Overlap: 5 sec
```

**Example 2: Basic Metadata**
```bash
python audio_process_and_transcribe.py downloads/ --metadata-level basic
# - Fast processing
# - Only 2 AI calls per file
# - Basic metadata only
```

**Example 3: Custom Output**
```bash
python audio_process_and_transcribe.py Audio_Files/ -o MyTranscripts/
# - Input: Audio_Files/
# - Output: MyTranscripts/
# - Metadata: Enhanced (default)
```

**Example 4: Large Files (Custom Chunking)**
```bash
python audio_process_and_transcribe.py downloads/ --chunk_duration 30 --overlap 10
# - Longer chunks: 30 minutes
# - More overlap: 10 seconds
```

---

## ⚙️ **Metadata Levels Explained**

### **Basic Mode** (Fast - 2 API Calls)

**What You Get:**
- ✅ Full transcription
- ✅ Summary
- ✅ Key ideas
- ✅ Legacy metadata (title, date, tags)

**API Calls Per File:**
```
1. Gemini: Audio transcription      (Required)
2. Provider: Summary + Key Ideas     (1 call, combined)
---
Total: 2 API calls
```

**Use When:**
- Quick processing needed
- Don't need graph-ready metadata
- Reducing API costs
- Processing large batches

**Output Example:**
```yaml
---
title: My Audio File
date_processed: 2026-01-02
tags: [...]
summary: "Brief summary..."
key_ideas:
  - Idea 1
  - Idea 2
---
## Full Transcription
[0m0s - 0m30s] Speaker 1: ...
```

---

### **Enhanced Mode** (Graph-Ready - 4 AI Calls)

**What You Get:**
- ✅ Everything from Basic
- ✅ Domain classification
- ✅ Entities (people, works, concepts)
- ✅ Concept definitions with hierarchies
- ✅ Relationships between concepts
- ✅ Cross-domain insights & analogies
- ✅ Mental models
- ✅ Bridge concepts
- ✅ Hierarchical tags (Zettelkasten-ready)

**API Calls Per File:**
```
1. Gemini: Audio transcription            (Required)
2. Provider: Core metadata (entities, concepts, relationships)
3. Provider: Cross-domain insights (analogies, mental models)
4. Provider: Summary + Key ideas
---
Total: 4 API calls
```

**Use When:**
- Building a knowledge graph
- Using Obsidian/Roam/Logseq
- Want deep cross-domain connections
- Quality over speed

**Output Example:**
```yaml
---
title: My Audio File
classification:
  primary_domain: Physics
  sub_domains: [Astrophysics, Time]
entities:
  people: [...]
  concepts_mentioned: [Day, Sun, Rotation]
concepts:
  - name: Gravitational Time Dilation
    definition: "Time passes slower near massive objects"
    parent_concepts: [General Relativity]
relationships:
  - source: Day
    target: Rotation
    type: equivalent_to
cross_domain_insights:
  - Physics → Economics analogy
mental_models:
  - Systems Thinking
tags:
  hierarchical:
    - "#Physics → #Astrophysics → #Time"
---
## Full Transcription
[0m0s - 0m30s] Speaker 1: ...
```

---

## 📊 **Comparison: Basic vs Enhanced**

| Aspect | Basic | Enhanced |
|--------|-------|----------|
| **API Calls** | 2 | 4 |
| **Speed** | ⚡⚡⚡ Fast | ⚡⚡ Moderate |
| **Cost** | 💰 Low | 💰💰 Medium |
| **Graph-Ready** | ❌ No | ✅ Yes |
| **Cross-Domain** | ❌ No | ✅ Yes |
| **Hierarchical Tags** | ❌ No | ✅ Yes |
| **Concept Definitions** | ❌ No | ✅ Yes |
| **Relationships** | ❌ No | ✅ Yes |
| **Use Case** | Quick notes | Knowledge base |

---

## 🚀 **Common Usage Scenarios**

### **Scenario 1: YouTube Video (Full Pipeline)**
```bash
# Run full pipeline
python run_full_audio_pipeline.py

# Choose option 1 (Download video)
# Enter URL: https://youtube.com/watch?v=...
# Pipeline runs automatically with enhanced metadata
```

### **Scenario 2: Process Local Audio Files**
```bash
# Copy audio files to a folder
mkdir my_audio
cp *.mp3 my_audio/

# Process with enhanced metadata
python audio_process_and_transcribe.py my_audio/
```

### **Scenario 3: Quick Basic Processing**
```bash
# Fast processing for 50 podcast episodes
python audio_process_and_transcribe.py podcasts/ --metadata-level basic
# Saves API calls (2 per file instead of 4)
```

### **Scenario 4: Skip YouTube, Process Existing**
```bash
# Files already in downloads/ from previous run
python run_full_audio_pipeline.py

# Choose option 3 (Skip download)
# Processes existing files with enhanced metadata
```

---

## 🔧 **How to Choose**

### **Use Full Pipeline When:**
- ✅ Processing YouTube videos
- ✅ Want automatic cleanup
- ✅ Using memory system
- ✅ Need complete workflow

### **Use Standalone When:**
- ✅ Processing local audio files
- ✅ Need custom chunk settings
- ✅ Want control over metadata level
- ✅ Batch processing different folders

### **Use Basic Metadata When:**
- ✅ Processing 50+ files
- ✅ Don't need knowledge graph
- ✅ Want faster processing
- ✅ Reducing API costs
- ✅ Simple note-taking

### **Use Enhanced Metadata When:**
- ✅ Building knowledge base
- ✅ Using Obsidian/Logseq
- ✅ Want deep analysis
- ✅ Cross-domain connections needed
- ✅ Quality is priority

---

## 📝 **Summary**

### **Two Operation Modes**
1. **Full Pipeline**: `run_full_audio_pipeline.py`
   - YouTube → Audio → Transcription → Cleanup
   - Default: Enhanced metadata
   
2. **Standalone**: `audio_process_and_transcribe.py`
   - Audio → Transcription
   - Configurable metadata level

### **Two Metadata Levels**
1. **Basic**: 2 API calls, fast, simple notes
2. **Enhanced**: 4 API calls, graph-ready, deep insights

### **Your Current Setup**
```bash
# What you're running now
python run_full_audio_pipeline.py
# → Enhanced metadata (4 API calls per file)
# → Using Groq for metadata extraction
# → Graph-ready output with hierarchical tags
```

### **To Switch to Basic**
Edit `run_full_audio_pipeline.py` line 120:
```python
sys.argv = [..., "--metadata-level", "basic"]
```

Or use standalone mode:
```bash
python audio_process_and_transcribe.py downloads/ --metadata-level basic
```

---

## 💡 **Pro Tips**

**Tip 1: Reduce API Costs**
Use basic metadata when processing large batches:
```bash
python audio_process_and_transcribe.py downloads/ --metadata-level basic
# Saves 50% API calls (2 vs 4 per file)
```

**Tip 2: Option 3 in Full Pipeline**
Already have files in `downloads/`? Choose option 3 to skip download!

**Tip 3: Mix and Match**
- Use **Enhanced** for important content
- Use **Basic** for casual podcasts

**Tip 4: Custom Folders**
Process different folders separately:
```bash
python audio_process_and_transcribe.py lectures/ -o lecture_notes/
python audio_process_and_transcribe.py podcasts/ -o podcast_notes/ --metadata-level basic
```

Hope this clarifies all the options! 🚀
