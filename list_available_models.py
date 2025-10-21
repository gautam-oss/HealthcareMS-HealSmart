#!/usr/bin/env python
"""
List all available Gemini models for your API key
"""

import os
import sys

print("=" * 60)
print("Finding Available Gemini Models")
print("=" * 60)

# Load Django settings
try:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'healthcarems.settings')
    import django
    django.setup()
    from django.conf import settings
    print("✅ Django settings loaded")
except Exception as e:
    print(f"❌ Error loading Django: {e}")
    sys.exit(1)

# Import Gemini
try:
    import google.generativeai as genai
    print("✅ google-generativeai imported")
except ImportError:
    print("❌ google-generativeai not installed")
    sys.exit(1)

# Configure API
api_key = settings.GEMINI_API_KEY
if not api_key:
    print("❌ No API key found")
    sys.exit(1)

print(f"✅ Using API key: {api_key[:10]}...")
genai.configure(api_key=api_key)

# List all available models
print("\n" + "=" * 60)
print("AVAILABLE MODELS FOR YOUR API KEY:")
print("=" * 60)

try:
    models = genai.list_models()
    
    generative_models = []
    
    for model in models:
        # Check if model supports generateContent
        if 'generateContent' in model.supported_generation_methods:
            generative_models.append(model.name)
            print(f"\n✅ {model.name}")
            print(f"   Display Name: {model.display_name}")
            print(f"   Description: {model.description}")
            print(f"   Methods: {', '.join(model.supported_generation_methods)}")
    
    print("\n" + "=" * 60)
    print("SUMMARY:")
    print("=" * 60)
    
    if generative_models:
        print(f"\nFound {len(generative_models)} model(s) that support text generation:\n")
        for model_name in generative_models:
            # Extract just the model name part
            simple_name = model_name.replace('models/', '')
            print(f"   • {simple_name}")
        
        print("\n" + "=" * 60)
        print("RECOMMENDATION:")
        print("=" * 60)
        
        # Recommend the first available model
        recommended = generative_models[0].replace('models/', '')
        print(f"\nUse this model in your core/views.py:")
        print(f"\n   model = genai.GenerativeModel('{recommended}')")
        print("\n" + "=" * 60)
    else:
        print("\n❌ No models found that support text generation!")
        print("\nPossible issues:")
        print("1. Your API key might not have access to Gemini models")
        print("2. You might need to enable the Gemini API in Google Cloud Console")
        print("3. Try creating a NEW API key at: https://aistudio.google.com/app/apikey")
        
except Exception as e:
    print(f"\n❌ Error listing models: {e}")
    print("\nTroubleshooting:")
    print("1. Check your internet connection")
    print("2. Verify API key at: https://aistudio.google.com/app/apikey")
    print("3. Try creating a NEW API key")
    print("4. Make sure you're using Google AI Studio (not Google Cloud Platform)")
    sys.exit(1)