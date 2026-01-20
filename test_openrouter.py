#!/usr/bin/env python3
"""
Simple test script to verify OpenRouter API configuration.
Tests the configured model by sending a short paragraph and requesting a summary.
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import our AI provider
from ai_provider import get_metadata_provider

def test_openrouter():
    """Test OpenRouter API with current configuration"""
    
    print("=" * 70)
    print("🧪 OpenRouter API Test")
    print("=" * 70)
    
    # Check environment variables
    print("\n📋 Configuration:")
    provider = os.environ.get("METADATA_PROVIDER", "NOT SET")
    api_key = ""
    
    # Get API key and model based on provider
    if provider == "openrouter":
        model = os.environ.get("OPENROUTER_MODEL", "NOT SET")
        api_key = os.environ.get("OPENROUTER_API_KEY", "NOT SET")
    elif provider == "groq":
        model = os.environ.get("GROQ_MODEL", "NOT SET")
        api_key = os.environ.get("GROQ_API_KEY", "NOT SET")
    elif provider == "gemini":
        model = os.environ.get("GEMINI_MODEL", "NOT SET")
        api_key = os.environ.get("GOOGLE_API_KEY", "NOT SET")
    elif provider == "local":
        model = os.environ.get("LOCAL_MODEL", "NOT SET")
        api_key = "not-needed"  # Local doesn't need API key
    else:
        model = "NOT SET"
        api_key = "NOT SET"
    
    print(f"   Provider: {provider}")
    print(f"   Model: {model}")
    if provider == "local":
        base_url = os.environ.get("LOCAL_BASE_URL", "http://localhost:1234/v1")
        print(f"   LM Studio URL: {base_url}")
        print(f"   API Key: Not required (local)")
    else:
        print(f"   API Key: {api_key[:20]}..." if len(api_key) > 20 else f"   API Key: {api_key}")
    
    if provider not in ["openrouter", "groq", "gemini", "local"]:
        print("\n❌ ERROR: METADATA_PROVIDER must be 'openrouter', 'groq', 'gemini', or 'local'")
        print("   Please update your .env file")
        return False
    
    if provider != "local" and (api_key == "NOT SET" or api_key.startswith("your_")):
        print(f"\n❌ ERROR: {provider.upper()}_API_KEY is not configured")
        print("   Please add your API key to .env file")
        return False
    
    # Test paragraph
    test_text = """
    Artificial intelligence has revolutionized the way we interact with technology. 
    Machine learning algorithms can now process vast amounts of data, recognize patterns, 
    and make predictions with remarkable accuracy. From natural language processing to 
    computer vision, AI is transforming industries ranging from healthcare to finance.
    """
    
    print("\n📝 Test Input:")
    print(f"   {test_text.strip()[:100]}...")
    
    # Initialize provider
    print("\n🔄 Initializing AI provider...")
    try:
        ai_provider = get_metadata_provider()
        print(f"   ✅ Provider initialized: {ai_provider.get_provider_name()}")
    except Exception as e:
        print(f"   ❌ Failed to initialize provider: {e}")
        return False
    
    # Create prompt
    prompt = f"""Please provide a one-sentence summary of the following text:

{test_text}

Summary:"""
    
    # Make API call
    print("\n🚀 Sending API request...")
    print(f"   Model: {model}")
    
    try:
        response = ai_provider.generate_content(prompt)
        
        print("\n✅ SUCCESS!")
        print("=" * 70)
        print("📤 Response from AI:")
        print("-" * 70)
        print(response)
        print("=" * 70)
        
        # Validate response
        if not response or len(response.strip()) < 10:
            print("\n⚠️  WARNING: Response seems too short or empty")
            return False
        
        print("\n✅ OpenRouter API is working correctly!" if provider == "openrouter" else f"\n✅ {provider.capitalize()} API is working correctly!")
        print(f"✅ Model '{model}' is responding")
        print(f"✅ API key is valid")
        
        return True
        
    except Exception as e:
        print(f"\n❌ API call failed!")
        print(f"   Error: {e}")
        
        # Check for specific errors
        error_str = str(e).lower()
        if "rate limit" in error_str or "429" in error_str:
            print("\n💡 TIP: This model is rate-limited on free tier")
            print("   Try switching to a different model or provider:")
            print("   OpenRouter: OPENROUTER_MODEL=meta-llama/llama-3.3-70b-instruct:free")
            print("   Groq: GROQ_MODEL=llama-3.3-70b-versatile")
            print("   Local: METADATA_PROVIDER=local (requires LM Studio)")
        elif "connection" in error_str or "refused" in error_str:
            if provider == "local":
                print("\n💡 TIP: Cannot connect to LM Studio")
                print("   1. Make sure LM Studio is running")
                print("   2. Go to 'Local Server' tab in LM Studio")
                print("   3. Click 'Start Server'")
                print("   4. Check server is on http://localhost:1234")
            else:
                print("\n💡 TIP: Connection error")
                print(f"   Check your internet connection")
        elif "401" in error_str or "unauthorized" in error_str:
            print(f"\n💡 TIP: {provider.upper()} API key might be invalid")
            print(f"   Check your {provider.upper()}_API_KEY in .env")
        elif "404" in error_str or "not found" in error_str:
            if provider == "local":
                print("\n💡 TIP: Model not found in LM Studio")
                print("   1. Open LM Studio")
                print("   2. Go to 'Discover' tab") 
                print("   3. Download a model (e.g., Llama 3.1 8B)")
                print("   4. Load the model in 'Local Server' tab")
            else:
                print("\n💡 TIP: Model might not exist or is unavailable")
                print(f"   Check {provider.upper()}_MODEL in .env")
        
        return False

def main():
    """Run the test"""
    print("\n" + "🔬 Starting OpenRouter API Test".center(70))
    print()
    
    success = test_openrouter()
    
    print("\n" + "=" * 70)
    if success:
        print("✅ TEST PASSED - API is ready to use!")
        print("\n🎯 Next step: Run your full application")
        exit_code = 0
    else:
        print("❌ TEST FAILED - Please fix the issues above")
        print("\n💡 Common fixes:")
        print("   1. Check your API key is correct in .env")
        print("   2. Try a different model")
        print("   3. Wait a few minutes if rate-limited")
        print("   4. Ensure METADATA_PROVIDER matches your config (openrouter/groq/gemini/local)")
        print("   5. For local: Make sure LM Studio server is running")
        exit_code = 1
    
    print("=" * 70)
    sys.exit(exit_code)

if __name__ == "__main__":
    main()
