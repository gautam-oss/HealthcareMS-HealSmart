#!/usr/bin/env python
"""
Test Gemini API Connection
Run this to diagnose chatbot issues
"""

import os
import sys

print("=" * 60)
print("Gemini API Connection Test")
print("=" * 60)

# Step 1: Check if package is installed
print("\n1. Checking if google-generativeai is installed...")
try:
    import google.generativeai as genai
    print("   ✅ google-generativeai package found")
except ImportError:
    print("   ❌ google-generativeai NOT installed")
    print("   Fix: pip install google-generativeai")
    sys.exit(1)

# Step 2: Load Django settings
print("\n2. Loading Django settings...")
try:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'healthcarems.settings')
    import django
    django.setup()
    from django.conf import settings
    print("   ✅ Django settings loaded")
except Exception as e:
    print(f"   ❌ Error loading Django: {e}")
    sys.exit(1)

# Step 3: Check API key
print("\n3. Checking Gemini API key...")
api_key = settings.GEMINI_API_KEY

if not api_key:
    print("   ❌ GEMINI_API_KEY is empty or not set")
    print("   Fix: Add GEMINI_API_KEY=your-key-here to .env file")
    sys.exit(1)

if not api_key.startswith('AIza'):
    print(f"   ⚠️  Warning: API key doesn't start with 'AIza' (starts with: {api_key[:4]}...)")
    print("   This might be incorrect. Gemini API keys typically start with 'AIza'")

print(f"   ✅ API key found (length: {len(api_key)} characters)")
print(f"   Key starts with: {api_key[:10]}...")

# Step 4: Test API connection
print("\n4. Testing Gemini API connection...")
try:
    genai.configure(api_key=api_key)
    print("   ✅ API configured")
except Exception as e:
    print(f"   ❌ Error configuring API: {e}")
    sys.exit(1)

# Step 5: Try to create model
print("\n5. Creating Gemini model...")
try:
    # Use the Gemini 2.5 model that works with your API key
    model = genai.GenerativeModel('gemini-2.5-flash')
    print("   ✅ Model created successfully (using gemini-2.5-flash)")
except Exception as e:
    print(f"   ❌ Error creating model: {e}")
    print("   Trying gemini-flash-latest as fallback...")
    try:
        model = genai.GenerativeModel('gemini-flash-latest')
        print("   ✅ Model created successfully (using gemini-flash-latest)")
    except Exception as e2:
        print(f"   ❌ Fallback also failed: {e2}")
        sys.exit(1)

# Step 6: Test actual generation
print("\n6. Testing content generation...")
print("   Sending test message to Gemini...")
try:
    response = model.generate_content("Say 'Hello, I am working!' in one sentence.")
    
    if response and response.text:
        print(f"   ✅ SUCCESS! Got response from Gemini:")
        print(f"   Response: {response.text}")
    else:
        print("   ❌ Got empty response from Gemini")
        print(f"   Response object: {response}")
        
except Exception as e:
    error_msg = str(e)
    print(f"   ❌ Error generating content: {error_msg}")
    
    # Provide specific guidance based on error
    if 'API_KEY_INVALID' in error_msg or 'invalid api key' in error_msg.lower():
        print("\n   💡 Solution: Your API key is invalid")
        print("   1. Go to: https://aistudio.google.com/app/apikey")
        print("   2. Create a new API key")
        print("   3. Update .env file with: GEMINI_API_KEY=your-new-key")
        print("   4. Restart Django server")
    elif 'PERMISSION_DENIED' in error_msg:
        print("\n   💡 Solution: API not enabled")
        print("   1. Go to: https://console.cloud.google.com/")
        print("   2. Enable Gemini API for your project")
        print("   3. Make sure billing is enabled (free tier is available)")
    elif 'QUOTA_EXCEEDED' in error_msg:
        print("\n   💡 Solution: API quota exceeded")
        print("   1. Wait a few minutes and try again")
        print("   2. Or upgrade your API plan")
    else:
        print("\n   💡 This might be a network or API service issue")
        print("   - Check your internet connection")
        print("   - Try again in a few minutes")
        print("   - Verify your API key at: https://aistudio.google.com/app/apikey")
    
    sys.exit(1)

# Final summary
print("\n" + "=" * 60)
print("FINAL RESULT")
print("=" * 60)
print("✅ All tests passed! Gemini API is working correctly.")
print("\nYour chatbot should work now. If it still doesn't:")
print("1. Make sure you've replaced core/views.py with the updated version")
print("2. Restart Django server: python manage.py runserver")
print("3. Clear browser cache: Ctrl+Shift+Delete")
print("4. Try the chatbot again")
print("=" * 60)