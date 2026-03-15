import os
import argparse
import ffmpeg
import psutil
import sys
import time
from datetime import timedelta, date
import google.generativeai as genai
from dotenv import load_dotenv
import yaml
import uuid
import gc
import json
import re
from typing import List, Dict, Optional

# Import AI provider abstraction
from ai_provider import get_metadata_provider, get_transcription_provider

# Load environment variables for Google API key and model
load_dotenv()

# Get model from environment or use default (for transcription only)
GEMINI_MODEL = os.environ.get('GEMINI_MODEL', 'models/gemini-2.5-flash')

# Custom exception for Gemini quota exhaustion
class GeminiQuotaExhaustedError(Exception):
    """Raised when Gemini API quota is exhausted (429 RESOURCE_EXHAUSTED)."""
    pass

def clean_json_response(response_text: str) -> str:
    """
    Clean AI response to extract valid JSON.
    Handles reasoning models (like DeepSeek-R1) that output thinking tags.
    
    Args:
        response_text: Raw AI model response
        
    Returns:
        Cleaned text ready for JSON parsing
    """
    original_text = response_text  # Keep for debugging
    
    # Remove thinking tags from reasoning models (DeepSeek-R1, etc.)
    if '<think>' in response_text or '<thinking>' in response_text:
        # Try to extract content after thinking tags
        patterns = [
            r'</think>\s*(.+)',  # Content after </think>
            r'</thinking>\s*(.+)',  # Content after </thinking>
        ]
        for pattern in patterns:
            match = re.search(pattern, response_text, re.DOTALL)
            if match:
                response_text = match.group(1).strip()
                break
    
    # Remove markdown code blocks
    if response_text.startswith('```'):
        lines = response_text.split('\n')
        response_text = '\n'.join(lines[1:-1]) if len(lines) > 2 else response_text
        if response_text.startswith('json'):
            response_text = response_text[4:].strip()
    
    # Fix common JSON errors from reasoning models
    # 1. Remove trailing commas before closing braces/brackets
    response_text = re.sub(r',(\s*[}\]])', r'\1', response_text)
    
    # 2. Remove any text after the last closing brace
    # Find the last } that matches the first {
    if '{' in response_text:
        brace_count = 0
        last_valid_pos = -1
        for i, char in enumerate(response_text):
            if char == '{':
                brace_count += 1
            elif char == '}':
                brace_count -= 1
                if brace_count == 0:
                    last_valid_pos = i + 1
                    break
        if last_valid_pos > 0:
            response_text = response_text[:last_valid_pos]
    
    return response_text.strip()

def get_metadata_delay_config() -> dict:
    """
    Load rate limiting delay configuration from environment.
    
    Returns:
        dict: Delay configuration with multiplier applied
    """
    try:
        core_delay = float(os.environ.get('METADATA_DELAY_AFTER_CORE', '5'))
        cross_domain_delay = float(os.environ.get('METADATA_DELAY_AFTER_CROSS_DOMAIN', '5'))
        summary_delay = float(os.environ.get('METADATA_DELAY_AFTER_SUMMARY', '5'))
        multiplier = float(os.environ.get('METADATA_DELAY_MULTIPLIER', '1.0'))
        logging_enabled = os.environ.get('METADATA_DELAY_LOGGING', 'true').lower() == 'true'
        
        return {
            'core': core_delay * multiplier,
            'cross_domain': cross_domain_delay * multiplier,
            'summary': summary_delay * multiplier,
            'logging': logging_enabled
        }
    except (ValueError, TypeError):
        print("⚠️  Invalid delay configuration, using defaults (5s)")
        return {
            'core': 5.0,
            'cross_domain': 5.0,
            'summary': 5.0,
            'logging': True
        }

def apply_rate_limit_delay(delay_seconds: float, delay_name: str, logging_enabled: bool = True):
    """
    Apply rate limiting delay between API calls.
    
    Args:
        delay_seconds: Number of seconds to wait
        delay_name: Name of the delay for logging
        logging_enabled: Whether to log the delay
    """
    if delay_seconds > 0:
        if logging_enabled:
            print(f"  ⏳ Rate limit delay ({delay_name}): {delay_seconds}s...")
        time.sleep(delay_seconds)


def get_audio_duration(file_path: str) -> Optional[float]:
    """Get the duration of an audio file using ffmpeg."""
    try:
        probe = ffmpeg.probe(file_path)
        duration = float(probe['format']['duration'])
        return duration
    except ffmpeg.Error as e:
        print(f"Error getting audio duration: {e.stderr.decode()}")
        return None

def format_timestamp(seconds: float) -> str:
    """Convert seconds to ffmpeg time format (HH:MM:SS.xxx)."""
    td = timedelta(seconds=float(seconds))
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{secs:06.3f}"

def check_memory_usage() -> bool:
    """Check current memory usage and print warning if too high."""
    process = psutil.Process()
    memory_percent = process.memory_percent()
    if memory_percent > 80:
        print(f"Warning: High memory usage ({memory_percent:.1f}%)")
        return False
    return True

def clean_partial_chunks(base_file_path: str) -> None:
    """Clean up any existing partial chunks before starting."""
    try:
        base_name = os.path.splitext(os.path.basename(base_file_path))[0]
        output_folder = os.path.dirname(base_file_path)
        pattern = f"{base_name}_part*"
        
        print(f"Cleaning up any existing chunks matching: {pattern}")
        for file in os.listdir(output_folder):
            if file.startswith(f"{base_name}_part") and file.endswith(".mp3"):
                file_path = os.path.join(output_folder, file)
                try:
                    os.remove(file_path)
                    print(f"Removed existing chunk: {file}")
                except Exception as e:
                    print(f"Warning: Could not remove {file}: {e}")
    except Exception as e:
        print(f"Warning: Error during cleanup: {e}")

def chunk_audio_file(audio_file_path: str, chunk_duration_minutes: int = 25, overlap_seconds: int = 5) -> List[str]:
    """Chunks an audio file into smaller parts using ffmpeg streaming."""
    chunked_files = []
    try:
        # Clean up any existing chunks first
        clean_partial_chunks(audio_file_path)

        # Get audio duration
        print("\nAnalyzing audio file duration...")
        duration = get_audio_duration(audio_file_path)
        if duration is None:
            print("Error: Could not determine audio file duration.")
            return chunked_files

        chunk_length = chunk_duration_minutes * 60
        overlap = overlap_seconds
        start_time = 0
        chunk_index = 1

        base_name = os.path.splitext(os.path.basename(audio_file_path))[0]
        output_folder = os.path.dirname(audio_file_path)

        total_chunks = int((duration - overlap) / (chunk_length - overlap)) + 1
        print(f"\nChunking audio file: {audio_file_path}")
        print(f"Total duration: {format_timestamp(duration)}")
        print(f"Chunk duration: {chunk_duration_minutes} minutes, Overlap: {overlap_seconds} seconds")
        print(f"Estimated number of chunks: {total_chunks}\n")

        while start_time < duration:
            if not check_memory_usage():
                print("Memory usage too high, waiting before continuing...")
                import time
                time.sleep(5)
                continue

            # Calculate end time for current chunk
            end_time = min(start_time + chunk_length, duration)
            
            # Make sure we don't create a tiny final chunk
            if end_time - start_time < 30:  # If chunk would be less than 30 seconds
                if chunk_index > 1:  # If not the first chunk
                    break  # Skip creating this small final chunk
                end_time = duration  # If it's the first chunk, include all audio

            chunk_file_name = f"{base_name}_part{chunk_index}.mp3"
            chunk_file_path = os.path.join(output_folder, chunk_file_name)

            print(f"Creating chunk {chunk_index}/{total_chunks}: {chunk_file_name}")
            print(f"  Time range: {format_timestamp(start_time)} to {format_timestamp(end_time)}")

            try:
                # Use ffmpeg to extract chunk
                if os.path.exists(chunk_file_path):
                    os.remove(chunk_file_path)
                    
                stream = ffmpeg.input(audio_file_path, ss=start_time, t=end_time-start_time)
                stream = ffmpeg.output(stream, chunk_file_path, acodec='libmp3lame', loglevel='error')
                ffmpeg.run(stream, capture_stdout=True, capture_stderr=True, overwrite_output=True)
                
                if os.path.exists(chunk_file_path):
                    chunk_size = os.path.getsize(chunk_file_path) / (1024 * 1024)
                    print(f"  ✓ Saved chunk: {chunk_file_path} ({chunk_size:.2f}MB)")
                    chunked_files.append(chunk_file_path)
                    chunk_index += 1
                else:
                    print(f"  ✗ Error: Chunk file was not created")
                    break

            except ffmpeg.Error as e:
                print(f"  ✗ Error processing chunk: {e.stderr.decode() if e.stderr else str(e)}")
                break

            # Update start time for next chunk, considering overlap
            if end_time == duration:  # If this was the last chunk
                break
            start_time = end_time - overlap

            # Force garbage collection after each chunk
            gc.collect()

        created_chunks = chunk_index - 1
        print(f"\nAudio file chunking completed:")
        print(f"- Created {created_chunks} out of {total_chunks} expected chunks")
        print(f"- Final chunk duration: {format_timestamp(end_time - start_time)}")

    except Exception as e:
        print(f"Error during audio chunking: {e}")

    return chunked_files

# --- Transcription Logic ---
def generate_transcription(audio_file_path: str) -> str:
    try:
        genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
        model = genai.GenerativeModel(GEMINI_MODEL)
        with open(audio_file_path, "rb") as audio_file:
            audio_data = audio_file.read()
        contents = [
            {
                "role": "user",
                "parts": [
                    {
                        "mime_type": "audio/mp3",
                        "data": audio_data
                    },
                    "Create a clean transcription of the audio file in English. Tag timestamps and speakers separately within the transcription. If speakers can be identified, use their names; otherwise, use 'Speaker 1', 'Speaker 2', etc. **Return ONLY the raw transcription text, starting directly with the first line of the transcription.** Do not include any introductory phrases, speaker identification plans, completion messages, or any text other than the transcription itself."
                ]
            },
            {
                "role": "model",
                "parts": [
                    "Understood. I will provide a clean, timestamped, and speaker-tagged transcription of the audio file, returning only the transcription text as requested."
                ]
            }
        ]
        response = model.generate_content(contents)
        return response.text
    except Exception as e:
        error_message = str(e)
        
        # Check for Gemini quota exhaustion (429 error)
        quota_indicators = [
            "429",
            "RESOURCE_EXHAUSTED",
            "quota",
        ]
        
        if any(indicator in error_message for indicator in quota_indicators):
            # Quota exhausted - raise custom exception to stop processing
            raise GeminiQuotaExhaustedError(f"Gemini API quota exhausted: {error_message}")
        
        # For other errors, return error message (non-critical)
        return f"Error during transcription: {e}"

# ============================================================================
# TIER 1: Enhanced Metadata Extraction (Phase 1 Implementation)
# ============================================================================

def extract_core_metadata(transcription_text: str, audio_file_name: str) -> dict:
    """
    AI Call #2: Extract core metadata including entities, concepts, relationships, 
    domain classification, and hierarchical tags.
    
    Uses configurable AI provider (OpenRouter/Groq/Gemini) via METADATA_PROVIDER env var.
    
    Returns structured JSON with:
    - classification (domain, sub-domains, difficulty, content_type)
    - entities (people, works_cited, concepts_mentioned, laws_theories_cited)
    - concepts (with definitions, hierarchies, abstraction levels)
    - relationships (between concepts with evidence)
    - tags (hierarchical, topical, methodological, people, concepts, temporal)
    """
    try:
        provider = get_metadata_provider()
        
        # Limit transcript length to avoid token limits
        transcript_preview = transcription_text[:12000]
        
        prompt_text = f"""Analyze this transcript and extract structured metadata in JSON format.

**TRANSCRIPT:**
{transcript_preview}

**AUDIO FILE:** {audio_file_name}

**Extract the following with HIGH PRECISION (only information explicitly mentioned or strongly implied):**

{{
  "classification": {{
    "primary_domain": "Single domain (Physics, Economics, AI, etc)",
    "sub_domains": ["2-4 specific sub-domains"],
    "difficulty_level": "Beginner|Intermediate|Advanced",
    "content_type": "Explainer|Tutorial|Interview|Lecture|Discussion"
  }},
  "entities": {{
    "people": [{{"name": "Name", "role": "Role", "contribution": "What they did/said"}}],
    "works_cited": [{{"title": "Title", "author": "Author", "year": 1234}}],
    "concepts_mentioned": ["5-10 key concepts"],
    "laws_theories_cited": ["Laws/theories mentioned"]
  }},
  "concepts": [
    {{
      "name": "Concept Name",
      "definition": "Clear 1-2 sentence definition",
      "parent_concepts": ["Broader category"],
      "related_concepts": ["Related concepts"],
      "abstraction_level": "Fundamental|Theoretical|Applied|Practical",
      "confidence": 0.0-1.0
    }}
  ],
  "relationships": [
    {{
      "source_concept": "Concept A",
      "target_concept": "Concept B",
      "relationship_type": "contradicts|supports|derives_from|causes|equivalent_to|applies_to",
      "strength": 0.0-1.0,
      "evidence": "Brief evidence",
      "reasoning": "Why this relationship"
    }}
  ],
  "tags": {{
    "hierarchical": ["#Domain → #SubDomain → #Topic → #Detail"],
    "topical": ["#TopicKeyword1", "#TopicKeyword2"],
    "methodological": ["#ThoughtExperiment", "#Derivation", "#etc"],
    "people": ["#PersonName"],
    "concepts": ["#ConceptName"],
    "temporal": ["#TimePeriod"]
  }}
}}

**GUIDELINES:**
1. Only extract PRESENT information - don't invent
2. Concepts: 5-7 most important ones
3. Relationships: explicit or strongly implied
4. Confidence: 0.9-1.0=explicit, 0.7-0.9=implied, <0.7=speculative
5. Hierarchical tags: general→specific (use → separator)
6. ALL tags must start with # (Zettelkasten linking format)

Return ONLY valid JSON (no markdown, no explanations)."""

        response_text = clean_json_response(provider.generate_content(prompt_text))
        
        try:
            metadata = json.loads(response_text)
        except json.JSONDecodeError as e:
            # Save problematic response for debugging
            debug_file = f"debug_core_metadata_error_{uuid.uuid4().hex[:8]}.txt"
            with open(debug_file, 'w', encoding='utf-8') as f:
                f.write(f"Error: {e}\n\n")
                f.write(f"Response text:\n{response_text}\n")
            print(f"⚠ Saved problematic response to {debug_file}")
            raise
        
        return metadata
        
    except Exception as e:
        print(f"⚠ Error extracting core metadata: {e}")
        return {
            "classification": {"primary_domain": "Unknown", "sub_domains": [], "difficulty_level": "Intermediate", "content_type": "Unknown"},
            "entities": {"people": [], "works_cited": [], "concepts_mentioned": [], "laws_theories_cited": []},
            "concepts": [],
            "relationships": [],
            "tags": {"hierarchical": [], "topical": [], "methodological": [], "people": [], "concepts": [], "temporal": []}
        }


def extract_cross_domain_insights(transcription_text: str, core_metadata: dict) -> dict:
    """
    AI Call #3: Extract cross-domain insights including analogies, bridge concepts,
    principle applications, and mental models.
    
    Uses configurable AI provider (OpenRouter/Groq/Gemini) via METADATA_PROVIDER env var.
    
    Returns structured JSON with:
    - cross_domain_insights (analogies between domains)
    - bridge_concepts (concepts appearing across domains)
    - mental_models (thinking frameworks used)
    - analogies_used (pedagogical analogies in content)
    """
    try:
        provider = get_metadata_provider()
        
        primary_domain = core_metadata.get('classification', {}).get('primary_domain', 'Unknown')
        concepts = core_metadata.get('concepts', [])
        concepts_list = [c.get('name', '') for c in concepts]
        
        prompt_text = f"""You are a polymath researcher analyzing a {primary_domain} transcript for cross-domain connections.

**PRIMARY DOMAIN:** {primary_domain}
**KEY CONCEPTS:** {json.dumps(concepts_list, indent=2)}

**TASK:** Identify cross-domain insights - connections between this content and OTHER fields.

**THINK ABOUT:**
- Structural similarities (same pattern, different domain)
- Analogies and metaphors used
- Principles that transfer across domains
- Mental models/frameworks applicable elsewhere
- Historical examples of cross-domain application

{{
  "cross_domain_insights": [
    {{
      "connection_type": "structural_analogy|principle_application|metaphor|historical_precedent",
      "source_domain": "{primary_domain}",
      "source_concept": "Concept from this transcript",
      "target_domain": "Other domain (Economics, Biology, Engineering, etc)",
      "target_concept": "Analogous concept in target domain",
      "insight": "Brief connection statement",
      "explanation": "2-3 sentences WHY these connect structurally",
      "potential_applications": ["Specific applications"],
      "confidence": 0.0-1.0,
      "historical_example": "Optional historical case"
    }}
  ],
  "bridge_concepts": [
    {{
      "concept": "Concept name",
      "appears_in_domains": ["Domain 1", "Domain 2", "Domain 3"],
      "role": "Why this bridges domains",
      "examples": ["Example from each domain"]
    }}
  ],
  "mental_models": [
    {{
      "name": "Mental Model (Systems Thinking, First Principles, etc)",
      "description": "What this thinking tool is",
      "applied_to": ["How used in transcript"],
      "transferable_to": ["Other domains/contexts"]
    }}
  ],
  "analogies_used": [
    {{
      "source_domain": "Familiar domain",
      "source_concept": "Familiar concept",
      "target_domain": "{primary_domain}",
      "target_concept": "Complex concept explained",
      "mapping": {{"Element A source": "Element A target"}},
      "pedagogical_value": "Why this helps understanding"
    }}
  ]
}}

**GUIDELINES:**
1. QUALITY>QUANTITY: 4-5 meaningful insights > 10 weak ones
2. Avoid superficial connections ("both use numbers" ❌)
3. Look for STRUCTURAL patterns, not surface similarities
4. Historical examples powerful (e.g., "Jevons Paradox 1865 → AI Rebound 2025")
5. Confidence: 0.8+=strong structural, 0.6-0.8=plausible, <0.6=speculative
6. If no strong insights exist, return fewer with high confidence

**EXAMPLES:**
- "Network effects (tech) ↔ Epidemic spreading (biology)" - same math
- "Thermodynamic entropy ↔ Information entropy (Shannon)" - mathematical equivalence
- "Jevons Paradox (economics 1865) ↔ AI automation paradox" - efficiency→consumption

Return ONLY valid JSON."""

        response_text = clean_json_response(provider.generate_content(prompt_text))
        insights = json.loads(response_text)
        return insights
        
    except Exception as e:
        print(f"⚠ Error extracting cross-domain insights: {e}")
        return {
            "cross_domain_insights": [],
            "bridge_concepts": [],
            "mental_models": [],
            "analogies_used": []
        }


# ============================================================================


def generate_zettelkasten_tags(transcription_text: str, audio_file_name: str) -> List[str]:
    """Generate Zettelkasten tags using configurable AI provider."""
    try:
        provider = get_metadata_provider()
        prompt_text = f"""
        Identify 5-8 keywords or short phrases that best represent the main topics, ideas, or discussion points in the following transcription.
        Consider also the audio file name '{audio_file_name}' as a potential tag if relevant.
        Return ONLY the tags, formatted as hashtags (#tag1 #tag2 #tag3 ...).

        Transcription Text:
        {transcription_text}
        """
        response_text = provider.generate_content(prompt_text)
        tags_text = response_text.strip()
        tags = [tag for tag in tags_text.split() if tag.startswith('#')]
        base_name = os.path.splitext(audio_file_name)[0]
        tags.append(f"#{base_name}")
        return tags
    except Exception:
        return []

def generate_domain(transcription_text: str) -> str:
    """Generate domain classification using configurable AI provider."""
    try:
        provider = get_metadata_provider()
        prompt_text = f"""
        Please read the following transcription text and suggest a single word or short phrase that best describes the domain or subject area it belongs to.
        Examples of domains include: Science, Technology, Business, Philosophy, History, Education, Health, Art, etc.

        Transcription Text:
        {transcription_text}

        Domain:
        """
        return provider.generate_content(prompt_text).strip()
    except Exception:
        return "Uncategorized"

def generate_summary(transcription_text: str) -> str:
    """Generate summary using configurable AI provider."""
    try:
        provider = get_metadata_provider()
        prompt_text = f"""
        Please read the following transcription text and write a concise summary of the main points in 2-3 sentences.

        Transcription Text:
        {transcription_text}

        Summary:
        """
        return provider.generate_content(prompt_text).strip()
    except Exception:
        return ""

def generate_key_ideas(transcription_text: str) -> List[Dict[str, str]]:
    """Generate key ideas using configurable AI provider."""
    try:
        provider = get_metadata_provider()
        prompt_text = f"""
        Please read the following transcription text and identify 3-5 key ideas or concepts discussed.
        Return these key ideas as a bulleted list, with each item in the list being an idea followed by a short (1-sentence) description of the idea.

        Transcription Text:
        {transcription_text}

        Key Ideas:
        """
        response_text = provider.generate_content(prompt_text)
        key_ideas_text = response_text.strip()
        key_ideas_list = []
        for item in key_ideas_text.split('\n'):
            item = item.lstrip('-* ')
            if item:
                parts = item.split(':', 1)
                if len(parts) == 2:
                    idea = parts[0].strip()
                    description = parts[1].strip()
                    key_ideas_list.append({'idea': idea, 'description': description})
                else:
                    key_ideas_list.append({'idea': item.strip(), 'description': 'No description provided by model.'})
        return key_ideas_list
    except Exception:
        return []

def save_transcription_to_file(transcription_text: str, output_file_path_md: str, output_file_path_txt: str, audio_file_name: str, metadata_level: str = 'enhanced') -> None:
    """
    Save transcription with configurable metadata levels.
    
    Metadata Levels:
    - 'basic': Transcription + legacy metadata only (faster, 2 AI calls)
    - 'enhanced': Transcription + legacy + Tier 1 metadata (slower, 4 AI calls, graph-ready)
    
    AI Calls made:
    1. extract_core_metadata() - entities, concepts, relationships, hierarchical tags
    2. extract_cross_domain_insights() - cross-domain connections, analogies, mental models
    3. generate_summary() - backward compatibility
    4. generate_key_ideas() - backward compatibility
    """
    try:
        base_name = os.path.splitext(audio_file_name)[0]
        
        if metadata_level == 'basic':
            # BASIC MODE: Legacy metadata only (faster)
            print(f"\n📝 Generating basic metadata for {audio_file_name}...")
            print("  → Generating summary and key ideas...")
            
            summary = generate_summary(transcription_text)
            key_ideas = generate_key_ideas(transcription_text)
            
            # Build basic YAML frontmatter
            yaml_metadata = {
                'title': base_name,
                'audio_file': audio_file_name,
                'note_id': str(uuid.uuid4()),
                'date_processed': str(date.today()),
                'summary': summary,
                'key_ideas': key_ideas if key_ideas else []
            }
            
            yaml_frontmatter = "---\n" + yaml.dump(yaml_metadata, sort_keys=False, indent=2, allow_unicode=True) + "---\n"
            
            # Simple markdown content
            content_sections_md = ""
            if key_ideas:
                content_sections_md += "## Discussion Topics\n\n"
                for idea_item in key_ideas:
                    content_sections_md += f"- **{idea_item.get('idea', 'Unknown')}:** {idea_item.get('description', '')}\n"
                content_sections_md += "\n"
            
            content_sections_md += "## Full Transcription\n\n"
            
            file_content_md = yaml_frontmatter + content_sections_md + transcription_text
            file_content_txt = yaml_frontmatter + "\nFull Transcription\n\n" + transcription_text
            
            print(f"  → Saving to {os.path.basename(output_file_path_md)}...")
            with open(output_file_path_md, "w", encoding="utf-8") as md_file:
                md_file.write(file_content_md)
            with open(output_file_path_txt, "w", encoding="utf-8") as txt_file:
                txt_file.write(file_content_txt)
            
            print("✅ Basic metadata saved successfully\n")
            
        else:  # metadata_level == 'enhanced'
            # ENHANCED MODE: Tier 1 metadata (graph-ready)
            print(f"\n🔄 Generating Tier 1 enhanced metadata for {audio_file_name}...")
            
            # Load delay configuration for rate limiting
            delay_config = get_metadata_delay_config()
            
            # Tier 1: Call #2 - Extract core metadata
            print("  → Extracting core metadata (entities, concepts, relationships)...")
            core_metadata = extract_core_metadata(transcription_text, audio_file_name)
            apply_rate_limit_delay(delay_config['core'], 'after core metadata', delay_config['logging'])
            
            # Tier 1: Call #3 - Extract cross-domain insights
            print("  → Analyzing cross-domain insights...")
            cross_domain = extract_cross_domain_insights(transcription_text, core_metadata)
            apply_rate_limit_delay(delay_config['cross_domain'], 'after cross-domain', delay_config['logging'])
            
            # Legacy calls for backward compatibility
            print("  → Generating summary and key ideas...")
            summary = generate_summary(transcription_text)
            apply_rate_limit_delay(delay_config['summary'], 'after summary', delay_config['logging'])
            
            key_ideas = generate_key_ideas(transcription_text)
            # Note: No delay after key_ideas (it's the last call)
            
            # Build Tier 1 enhanced YAML frontmatter
            yaml_metadata = {
                # Core identification
                'title': base_name,
                'audio_file': audio_file_name,
                'note_id': str(uuid.uuid4()),
                'date_processed': str(date.today()),
                
                # Tier 1: Classification
                'classification': core_metadata.get('classification', {}),
                
                # Tier 1: Entities
                'entities': core_metadata.get('entities', {}),
                
                # Tier 1: Concepts with hierarchies
                'concepts': core_metadata.get('concepts', []),
                
                # Tier 1: Relationships between concepts
                'relationships': core_metadata.get('relationships', []),
                
                # Tier 1: Cross-domain insights (THE KEY FEATURE!)
                'cross_domain_insights': cross_domain.get('cross_domain_insights', []),
                'bridge_concepts': cross_domain.get('bridge_concepts', []),
                'mental_models': cross_domain.get('mental_models', []),
                'analogies_used': cross_domain.get('analogies_used', []),
                
                # Tier 1: Enhanced Zettelkasten tags
                'tags': core_metadata.get('tags', {}),
                
                # Legacy fields (backward compatibility)
                'summary': summary,
                'key_ideas': key_ideas if key_ideas else []
            }
            
            # Generate YAML frontmatter
            yaml_frontmatter = "---\n" + yaml.dump(yaml_metadata, sort_keys=False, indent=2, allow_unicode=True) + "---\n"
            
            # Build enhanced markdown content sections
            content_sections_md = ""
            
            # Section 1: Key Concepts (top 5)
            concepts_list = core_metadata.get('concepts', [])
            if concepts_list:
                content_sections_md += "## Key Concepts\n\n"
                for concept in concepts_list[:5]:
                    content_sections_md += f"**{concept.get('name', 'Unknown')}**  \n"
                    content_sections_md += f"{concept.get('definition', 'No definition')}\n\n"
            
            # Section 2: Cross-Domain Connections (top 3)
            insights_list = cross_domain.get('cross_domain_insights', [])
            if insights_list:
                content_sections_md += "## Cross-Domain Connections\n\n"
                for insight in insights_list[:3]:
                    content_sections_md += f"**{insight.get('source_domain', '?')} → {insight.get('target_domain', '?')}**\n\n"
                    content_sections_md += f"*{insight.get('insight', 'No insight')}*\n\n"
                    content_sections_md += f"{insight.get('explanation', 'No explanation')}\n\n"
            
            # Section 3: Discussion Topics (legacy key_ideas)
            if key_ideas:
                content_sections_md += "## Discussion Topics\n\n"
                for idea_item in key_ideas:
                    content_sections_md += f"- **{idea_item.get('idea', 'Unknown')}:** {idea_item.get('description', '')}\n"
                content_sections_md += "\n"
            
            # Section 4: Full Transcription
            content_sections_md += "## Full Transcription\n\n"
            
            # Final markdown file
            file_content_md = yaml_frontmatter + content_sections_md + transcription_text
            
            # TXT file (simpler, no markdown formatting)
            file_content_txt = yaml_frontmatter + "\nFull Transcription\n\n" + transcription_text
            
            # Save files
            print(f"  → Saving to {os.path.basename(output_file_path_md)}...")
            with open(output_file_path_md, "w", encoding="utf-8") as md_file:
                md_file.write(file_content_md)
            with open(output_file_path_txt, "w", encoding="utf-8") as txt_file:
                txt_file.write(file_content_txt)
            
            print("✅ Tier 1 enhanced transcription saved successfully\n")
            
            # Print metadata summary
            print(f"📊 Metadata Summary:")
            print(f"   Domain: {core_metadata.get('classification', {}).get('primary_domain', 'Unknown')}")
            print(f"   Concepts: {len(concepts_list)}")
            print(f"   Relationships: {len(core_metadata.get('relationships', []))}")
            print(f"   Cross-Domain Insights: {len(insights_list)}")
            print(f"   Mental Models: {len(cross_domain.get('mental_models', []))}")
            print(f"   Bridge Concepts: {len(cross_domain.get('bridge_concepts', []))}\n")

    except Exception as e:
        print(f"❌ Error saving transcription to file: {e}")
        import traceback
        traceback.print_exc()


def process_single_file(audio_file_path: str, output_folder_path: str, metadata_level: str, 
                       chunk_duration_minutes: int, overlap_seconds: int, 
                       memory_system=None, audio_downloads_folder=None) -> bool:
    """
    Process a single audio file: chunk (if needed), transcribe, extract metadata, save, and clean up.
    
    Args:
        audio_file_path: Path to the audio file
        output_folder_path: Folder to save transcripts
        metadata_level: 'basic' or 'enhanced'
        chunk_duration_minutes: Duration for chunks
        overlap_seconds: Overlap for chunks
        memory_system: Optional TranscriptionMemory instance
        audio_downloads_folder: Optional folder for finding .info.json files
        
    Returns:
        bool: True if successful, False otherwise
        
    Raises:
        GeminiQuotaExhaustedError: If API limit reached
    """
    audio_file_name = os.path.basename(audio_file_path)
    files_to_transcribe = []
    
    try:
        file_size_mb = os.path.getsize(audio_file_path) / (1024 * 1024)
        print(f"\nProcessing: {audio_file_name} ({file_size_mb:.2f}MB)")

        if file_size_mb > 30:
            print(f"File is larger than 30MB. Chunking into smaller parts...")
            chunked_files = chunk_audio_file(audio_file_path, chunk_duration_minutes, overlap_seconds)
            files_to_transcribe.extend(chunked_files)
            if chunked_files:  # Only delete original if chunking was successful
                print(f"Deleting original large file: {audio_file_name}")
                os.remove(audio_file_path)
        else:
            print("File is small enough to process directly")
            files_to_transcribe.append(audio_file_path)

        # Transcribe each part
        for file_path in files_to_transcribe:
            file_name = os.path.basename(file_path)
            print(f"\nTranscribing: {file_name}")
            
            transcription_text = generate_transcription(file_path)
            if transcription_text.startswith("Error during transcription:"):
                print(f"Error: {transcription_text}")
                continue

            base_name = os.path.splitext(file_name)[0]
            # Handle chunk naming for final output if needed, but usually we just process parts as separate notes for now
            # OR better: if it was chunked, we might want to combine... 
            # Current logic treats chunks as separate files which is fine for V1
            
            output_file_name_md = f"{base_name}.md"
            output_file_path_md = os.path.join(output_folder_path, output_file_name_md)
            output_file_name_txt = f"{base_name}.txt"
            output_file_path_txt = os.path.join(output_folder_path, output_file_name_txt)

            save_transcription_to_file(transcription_text, output_file_path_md, output_file_path_txt, file_name, metadata_level)
            print(f"✓ Successfully processed {file_name}")

            # Cleanup temporary chunk
            if "_part" in file_name:
                try:
                    os.remove(file_path)
                    print(f"Removed temporary chunk: {file_name}")
                except Exception as e:
                    print(f"Warning: Could not remove temporary chunk {file_name}: {e}")

        # Post-processing for the original file (memory update & cleanup)
        # Only if we successfully processed something
        if files_to_transcribe:
            base_name = os.path.splitext(audio_file_name)[0]
            
            # 1. Update memory
            if memory_system and audio_downloads_folder:
                info_file_path = os.path.join(audio_downloads_folder, f"{base_name}.info.json")
                if os.path.exists(info_file_path):
                    try:
                        with open(info_file_path, 'r', encoding='utf-8') as f:
                            video_info = json.load(f)
                        
                        # Calculate transcript paths
                        transcript_files = []
                        if len(files_to_transcribe) > 1: # Chunked
                            for f in files_to_transcribe:
                                bn = os.path.splitext(os.path.basename(f))[0]
                                transcript_files.append(os.path.join(output_folder_path, f"{bn}.md"))
                        else:
                            transcript_files.append(os.path.join(output_folder_path, f"{base_name}.md"))

                        memory_system.add_processed_video(video_info, transcript_files)
                        
                        # Delete .info.json
                        os.remove(info_file_path)
                        print(f"🗑️  Cleaned up info file: {base_name}.info.json")
                    except Exception as e:
                        print(f"⚠️  Could not update memory for {audio_file_name}: {e}")
            
            # 2. Delete original audio file if it still exists (e.g. wasn't chunked/deleted)
            if os.path.exists(audio_file_path):
                try:
                    os.remove(audio_file_path)
                    print(f"🗑️  Deleted audio file: {audio_file_name}")
                except Exception as e:
                    print(f"⚠️  Could not delete audio file {audio_file_name}: {e}")
            
            return True
            
    except GeminiQuotaExhaustedError:
        raise # Propagate up
    except Exception as e:
        print(f"Error processing {audio_file_name}: {e}")
        return False
        
    return True

def main(memory_system=None, downloads_folder=None):
    parser = argparse.ArgumentParser(description="Chunk large audio files and transcribe all audio files in a folder.")
    parser.add_argument("audio_folder", help="Path to the folder containing audio files.")
    parser.add_argument("-o", "--output_folder", help="Path to save the transcription text files (default: 'Transcripts')")
    parser.add_argument("--metadata-level", choices=['basic', 'enhanced'], default='enhanced', 
                        help="Metadata level: 'basic' (fast, 2 AI calls) or 'enhanced' (graph-ready, 4 AI calls)")
    parser.add_argument("--chunk_duration", type=int, default=25, help="Chunk duration in minutes (default: 25)")
    parser.add_argument("--overlap", type=int, default=5, help="Overlap between chunks in seconds (default: 5)")
    args = parser.parse_args()

    audio_folder_path = args.audio_folder
    output_folder_path = args.output_folder if args.output_folder else "Transcripts"
    metadata_level = args.metadata_level
    chunk_duration_minutes = args.chunk_duration
    overlap_seconds = args.overlap
    
    # Store downloads folder for per-file audio deletion
    audio_downloads_folder = downloads_folder if downloads_folder else audio_folder_path

    print(f"🎯 Metadata Level: {metadata_level.upper()}")
    if metadata_level == 'basic':
        print("   Mode: Basic (faster, transcription + legacy metadata only)")
    else:
        print("   Mode: Enhanced (graph-ready, includes Tier 1 metadata)\n")

    if not os.path.exists(audio_folder_path):
        print(f"Error: Audio folder not found at '{audio_folder_path}'")
        return

    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)
        print(f"Created output folder: {output_folder_path}")

    audio_files = [
        f for f in os.listdir(audio_folder_path)
        if os.path.isfile(os.path.join(audio_folder_path, f))
        and f.lower().endswith(('.mp3', '.m4a', '.wav', '.ogg', '.flac', '.weba', '.webm', '.mp4'))
        and not f.endswith('_part.mp3')  # Exclude any partial chunks
    ]

    if not audio_files:
        print(f"No audio files found in the folder: '{audio_folder_path}'")
        return

    print(f"Found {len(audio_files)} audio files to process")
    
    for audio_file_name in audio_files:
        audio_file_path = os.path.join(audio_folder_path, audio_file_name)
        
        try:
            success = process_single_file(
                audio_file_path,
                output_folder_path,
                metadata_level,
                chunk_duration_minutes,
                overlap_seconds,
                memory_system,
                audio_downloads_folder
            )
            
        except GeminiQuotaExhaustedError as e:
            print(f"\n❌ {e}")
            print("Application stopped.")
            sys.exit(1)
        
        # Force garbage collection
        gc.collect()

    print("\nAll files processed and transcribed.")

if __name__ == "__main__":
    main()

