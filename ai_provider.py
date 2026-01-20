"""
AI Provider Abstraction Layer
Supports multiple AI providers for metadata extraction while keeping Gemini for audio transcription.
"""

import os
import json
from typing import Optional
from abc import ABC, abstractmethod
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class AIProvider(ABC):
    """Base class for AI providers"""
    
    @abstractmethod
    def generate_content(self, prompt: str) -> str:
        """Generate content from prompt"""
        pass
    
    @abstractmethod
    def get_provider_name(self) -> str:
        """Get provider name for logging"""
        pass


class GeminiProvider(AIProvider):
    """Google Gemini AI Provider"""
    
    def __init__(self):
        self.api_key = os.environ.get("GOOGLE_API_KEY")
        self.model_name = os.environ.get("GEMINI_MODEL", "models/gemini-2.5-flash")
        
        if not self.api_key:
            raise ValueError("GOOGLE_API_KEY not found in environment variables")
        
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(self.model_name)
    
    def generate_content(self, prompt: str) -> str:
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            raise Exception(f"Gemini API error: {e}")
    
    def get_provider_name(self) -> str:
        return f"Gemini ({self.model_name})"


class OpenRouterProvider(AIProvider):
    """OpenRouter AI Provider (supports DeepSeek-R1:free and other models)"""
    
    def __init__(self):
        self.api_key = os.environ.get("OPENROUTER_API_KEY")
        self.model_name = os.environ.get("OPENROUTER_MODEL", "deepseek/deepseek-r1:free")
        self.base_url = os.environ.get("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
        
        if not self.api_key:
            raise ValueError("OPENROUTER_API_KEY not found in environment variables")
        
        # Import OpenAI client for OpenRouter compatibility
        try:
            from openai import OpenAI
            self.client = OpenAI(
                base_url=self.base_url,
                api_key=self.api_key,
            )
        except ImportError:
            raise ImportError("OpenAI package required for OpenRouter. Install with: pip install openai")
    
    def generate_content(self, prompt: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
            )
            
            content = response.choices[0].message.content
            
            # Check for empty response
            if not content or content.strip() == "":
                raise Exception(f"Empty response from {self.model_name}. This may be due to rate limits or content filtering.")
            
            return content
            
        except Exception as e:
            error_msg = str(e)
            if "rate" in error_msg.lower():
                raise Exception(f"OpenRouter rate limit hit: {e}")
            elif "content" in error_msg.lower() and "filter" in error_msg.lower():
                raise Exception(f"Content filtered by OpenRouter: {e}")
            else:
                raise Exception(f"OpenRouter API error: {e}")
    
    def get_provider_name(self) -> str:
        return f"OpenRouter ({self.model_name})"


class GroqProvider(AIProvider):
    """Groq AI Provider"""
    
    def __init__(self):
        self.api_key = os.environ.get("GROQ_API_KEY")
        self.model_name = os.environ.get("GROQ_MODEL", "llama-3.3-70b-versatile")
        
        if not self.api_key:
            raise ValueError("GROQ_API_KEY not found in environment variables")
        
        # Import Groq client
        try:
            from groq import Groq
            self.client = Groq(api_key=self.api_key)
        except ImportError:
            raise ImportError("Groq package required. Install with: pip install groq")
    
    def generate_content(self, prompt: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
            )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"Groq API error: {e}")
    
    def get_provider_name(self) -> str:
        return f"Groq ({self.model_name})"

class LocalProvider(AIProvider):
    """Local LM Studio provider (OpenAI-compatible API on localhost)"""
    
    def __init__(self):
        self.model_name = os.environ.get("LOCAL_MODEL", "local-model")
        self.base_url = os.environ.get("LOCAL_BASE_URL", "http://localhost:1234/v1")
        
        # Import OpenAI client for LM Studio compatibility
        try:
            from openai import OpenAI
            self.client = OpenAI(
                base_url=self.base_url,
                api_key="not-needed"  # LM Studio doesn't require API key
            )
        except ImportError:
            raise ImportError("OpenAI package required for local models. Install with: pip install openai")
    
    def generate_content(self, prompt: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
            )
            
            content = response.choices[0].message.content
            
            # Check for empty response
            if not content or content.strip() == "":
                raise Exception(f"Empty response from local model {self.model_name}")
            
            return content
            
        except Exception as e:
            error_msg = str(e)
            if "connection" in error_msg.lower() or "refused" in error_msg.lower():
                raise Exception(f"Cannot connect to LM Studio at {self.base_url}. Is LM Studio running?")
            else:
                raise Exception(f"Local model error: {e}")
    
    def get_provider_name(self) -> str:
        return f"Local LM Studio ({self.model_name})"


def get_metadata_provider() -> AIProvider:
    """
    Factory function to get the appropriate metadata provider.
    Provider is determined by METADATA_PROVIDER environment variable.
    
    Supported providers:
    - gemini: Google Gemini (default)
    - openrouter: OpenRouter (multi-model aggregator)
    - groq: Groq (ultra-fast inference)
    - local: LM Studio (local models on localhost)
    """
    provider_name = os.environ.get("METADATA_PROVIDER", "gemini").lower()
    
    try:
        if provider_name == "openrouter":
            provider = OpenRouterProvider()
        elif provider_name == "groq":
            provider = GroqProvider()
        elif provider_name == "local":
            provider = LocalProvider()
        else:  # Default to gemini
            provider = GeminiProvider()
        
        print(f"📡 Using {provider.get_provider_name()} for metadata extraction")
        return provider
        
    except ValueError as e:
        print(f"⚠️  Provider configuration error: {e}")
        print(f"⚠️  Falling back to Gemini provider...")
        return GeminiProvider()
    except Exception as e:
        print(f"⚠️  Error initializing {provider_name} provider: {e}")
        print(f"⚠️  Falling back to Gemini provider...")
        return GeminiProvider()


def get_transcription_provider() -> GeminiProvider:
    """
    Get Gemini provider for audio transcription.
    This is always Gemini as it's the only provider that supports audio input.
    
    Returns:
        GeminiProvider: Gemini provider instance
    """
    return GeminiProvider()
