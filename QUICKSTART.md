# Quick Start Guide - Phase 1 🚀

## Complete Setup in 10 Steps

### 1. Get Gemini API Key (5 minutes)
1. Go to: https://aistudio.google.com/app/apikey
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the API key (starts with "AIza...")
5. Keep it safe - you'll need it in step 4

### 2. Create Project (1 minute)
```bash
mkdir HealthcareMS-HealSmart
cd HealthcareMS-HealSmart
```

### 3. Setup Virtual Environment (2 minutes)
```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### 4. Create .env File (1 minute)
Create a file named `.env` in your project root and add:
```
SECRET_KEY=django-insecure-your-secret-key-change-this
DEBUG=True
GEMINI_API_KEY=your-gemini-api-key-here
```
**Replace `your-gemini-api-key-here` with your actual API key from step 1**

### 5. Install Django & Dependencies (2 minutes)
Create `requirements.txt` file with:
```
Django==4.2.7
google-generativeai==0.3.1
python-decouple==3.8
Pillow==10.1.0
```

Then install:
```bash
pip install -r requirements.txt
```

### 6. Create Django Project (1 minute)
```bash
django-admin startproject healthcarems .
python manage.py startapp core
```

### 7. Create Folder Structure (1 minute)
```bash
mkdir templates
mkdir templates/core
mkdir static
mkdir media
```

### 8. Copy All Code Files
Copy the provided code files to these locations:

**Configuration Files:**
- `healthcarems/settings.py`
- `healthcarems/urls.py`
- `core/urls.py`
- `core/views.py`

**Template Files:**
- `templates/base.html`
- `templates/core/home.html`
- `templates/core/chatbot.html`
- `templates/core/insurance_predictor.html`

### 9. Initialize Database (1 minute)
```bash
python manage.py makemigrations
python manage.py migrate
```

### 10. Run Server (30 seconds)
```bash
python manage.py runserver
```

**🎉 Done! Open your browser and go to: `http://127.0.0.1:8000/`**

---

## Testing Your Application

### Test the Homepage
- Go to `http://127.0.0.1:8000/`
- You should see three feature cards
- Navigation menu should work

### Test the Chatbot
1. Click "Start Chat" or go to `http://127.0.0.1:8000/chatbot/`
2. Type: "What are symptoms of common cold?"
3. Press Enter or click Send
4. You should get an AI response within a few seconds

### Test Insurance Predictor
1. Click "Predict Cost" or go to `http://127.0.0.1:8000/insurance-predictor/`
2. Fill in the form:
   - Age: 30
   - BMI: 25.0
   - Children: 0
   - Smoker: Non-Smoker
   - Region: Northeast
3. Click "Calculate Insurance Cost"
4. You should see estimated cost and breakdown

---

## Common First-Time Issues & Fixes

### ❌ "Module not found" error
```bash
# Make sure virtual environment is activated
# You should see (venv) in your terminal
# Then reinstall:
pip install -r requirements.txt
```

### ❌ Gemini API not responding
1. Check `.env` file has correct API key
2. No spaces around the `=` sign
3. No quotes around the API key
4. Test your API key at: https://aistudio.google.com/

### ❌ "Template does not exist" error
- Make sure folders are created: `templates/core/`
- Check file names match exactly (case-sensitive)
- Verify `TEMPLATES` setting in `settings.py`

### ❌ Port already in use
```bash
# Use a different port
python manage.py runserver 8080
```

### ❌ Static files not loading
```bash
# Collect static files
python manage.py collectstatic --noinput
```

---

## Quick Commands Reference

```bash
# Activate virtual environment
venv\Scripts\activate          # Windows
source venv/bin/activate       # Mac/Linux

# Install packages
pip install -r requirements.txt

# Database operations
python manage.py makemigrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Run server
python manage.py runserver

# Run server on different port
python manage.py runserver 8080
```

---

## File Checklist ✅

Make sure you have all these files:

```
HealthcareMS-HealSmart/
├── .env ✅
├── .gitignore ✅
├── requirements.txt ✅
├── manage.py ✅
├── db.sqlite3 (created after migrate)
│
├── healthcarems/
│   ├── __init__.py
│   ├── settings.py ✅
│   ├── urls.py ✅
│   ├── wsgi.py
│   └── asgi.py
│
├── core/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py ✅
│   └── urls.py ✅
│
└── templates/
    ├── base.html ✅
    └── core/
        ├── home.html ✅
        ├── chatbot.html ✅
        └── insurance_predictor.html ✅
```

---

## Next Steps After Phase 1

Once everything works:
1. Explore the admin panel at `/admin/`
2. Customize the design and colors
3. Test all features thoroughly
4. Get ready for Phase 2 (Authentication & Dashboards)

**Need help? Check the error messages in your terminal - they usually point to the problem!**

Good luck! 🍀