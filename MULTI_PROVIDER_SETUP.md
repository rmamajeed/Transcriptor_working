# Multi-Provider AI Configuration Guide

## Overview
Transcriptinator now supports multiple AI providers for metadata extraction to avoid rate limits and save costs.

## Quick Setup

### 1. Install Dependencies
```bash
source venv/bin/activate
pip install openai groq
```

### 2. Configure `.env`
```env
# Required: Gemini for transcription
GOOGLE_API_KEY=your_actual_key_here

# Metadata provider (openrouter recommended)
METADATA_PROVIDER=openrouter

# OpenRouter (free tier available)
OPENROUTER_API_KEY=sk-or-your_key_here
OPENROUTER_MODEL=deepseek/deepseek-r1:free

# Groq (alternative)
GROQ_API_KEY=gsk_your_key_here
GROQ_MODEL=llama-3.3-70b-versatile
```

### 3. Get API Keys
- **OpenRouter**: https://openrouter.ai/ (free tier includes DeepSeek-R1)
- **Groq**: https://console.groq.com/ (free tier with fast inference)

## What Changed?

**Audio Transcription** → Always uses Gemini (required for audio input)

**Metadata Extraction** → Configurable (OpenRouter/Groq/Gemini):
- Core metadata extraction
- Cross-domain insights
- Summary generation
- Key ideas extraction

## Cost Savings

For **Enhanced Mode** (5 AI calls per file):
- **Before**: 5 Gemini calls
- **After**: 1 Gemini + 4 OpenRouter/Groq
- **Savings**: 80% of Gemini quota!

## Provider Comparison

| Provider | Cost | Speed | Best For |
|----------|------|-------|----------|
| OpenRouter | Free tier | Medium | Avoiding limits |
| Groq | Free tier | Very Fast | Speed |
| Gemini | Pay-per-use | Fast | Simplicity |

## Recommended Setup
```env
METADATA_PROVIDER=openrouter
OPENROUTER_MODEL=deepseek/deepseek-r1:free
```

## Testing
```bash
source venv/bin/activate
python audio_process_and_transcribe.py downloads/ -o test_output --metadata-level basic
```

Expected output:
```
📡 Using OpenRouter (deepseek/deepseek-r1:free) for metadata extraction
```

## Troubleshooting

**Error: Module not found**
```bash
source venv/bin/activate
pip install -r requirements.txt
```

**Error: API key not found**
- Check `.env` file has correct key names
- Ensure no extra spaces around `=`

**Fallback behavior**: If configured provider fails, automatic fallback to Gemini with warning.

## Rate Limiting Configuration (NEW)

### Problem: Groq API 429 Errors

Groq has strict token-per-minute (TPM) limits:
- **llama-3.3-70b-versatile**: 12,000 TPM
- **Enhanced mode**: Uses ~16,000 tokens (4 API calls) in ~10 seconds
- **Result**: Exceeds limit → 429 Rate Limit error

### Solution: Configurable Delays

Add delays between metadata API calls to stay within limits.

**Configuration in `.env`:**
```env
# Delay after each metadata call (seconds)
METADATA_DELAY_AFTER_CORE=5
METADATA_DELAY_AFTER_CROSS_DOMAIN=5
METADATA_DELAY_AFTER_SUMMARY=5

# Adjust all delays proportionally (1.0 = normal, 0 = no delays)
METADATA_DELAY_MULTIPLIER=1.0

# Show delay messages in console
METADATA_DELAY_LOGGING=true
```

**Impact:**
- **With delays (5s each)**: ~16,000 tokens in 55 seconds ✅ No errors
- **Without delays**: ~16,000 tokens in 10 seconds ❌ 429 error
- **Processing time**: Adds ~15 seconds per file total

**Recommended Settings by Provider:**

| Provider | Delay Setting | Reason |
|----------|---------------|--------|
| **Groq** | 5 seconds | Prevents TPM limit (12K) |
| **OpenRouter** | 0 seconds | Higher limits, no delays needed |
| **Gemini** | 0 seconds | Different quota system |
| **Local (LM Studio)** | 0 seconds | No API limits |

**Quick disable for testing:**
```env
METADATA_DELAY_MULTIPLIER=0  # Disables all delays
```

## More Details
See `.env.example` for all configuration options and model choices.
