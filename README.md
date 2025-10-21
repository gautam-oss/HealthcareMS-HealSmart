# HealthcareMS-HealSmart 🏥

A comprehensive Django-based Healthcare Management System with AI-powered features.

## Phase 1 Features ✨

### 1. Home Page
- Modern, responsive design
- Overview of all features
- Easy navigation

### 2. AI Healthcare Chatbot 💬
- Powered by Google Gemini API
- Quick healthcare advice
- Interactive chat interface
- Real-time responses

### 3. Insurance Cost Predictor 💰
- Estimate annual insurance costs
- Based on multiple factors:
  - Age
  - BMI (Body Mass Index)
  - Number of children
  - Smoking status
  - Geographic region
- Detailed cost breakdown

## Installation Guide 🚀

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Google Gemini API key

### Step-by-Step Setup

1. **Clone or create the project directory**
```bash
mkdir HealthcareMS-HealSmart
cd HealthcareMS-HealSmart
```

2. **Create and activate virtual environment**
```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on Mac/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Create Django project structure**
```bash
# Create Django project
django-admin startproject healthcarems .

# Create core app
python manage.py startapp core
```

5. **Set up environment variables**
- Create a `.env` file in the root directory
- Add your Gemini API key:
```
SECRET_KEY=your-django-secret-key
DEBUG=True
GEMINI_API_KEY=your-gemini-api-key-here
```

**Get Gemini API Key:**
- Visit: https://aistudio.google.com/app/apikey
- Sign in with Google account
- Create a new API key
- Copy and paste into `.env` file

6. **Create necessary directories**
```bash
mkdir templates
mkdir templates/core
mkdir static
mkdir media
```

7. **Apply all the code files**
- Copy all the provided code files to their respective locations
- Make sure `settings.py`, `urls.py`, `views.py` are in correct places
- Ensure all HTML templates are in `templates/core/` folder

8. **Run migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

9. **Create superuser (optional, for admin access)**
```bash
python manage.py createsuperuser
```

10. **Run the development server**
```bash
python manage.py runserver
```

11. **Access the application**
- Open browser and go to: `http://127.0.0.1:8000/`

## Project Structure 📁

```
HealthcareMS-HealSmart/
│
├── healthcarems/              # Main project folder
│   ├── settings.py           # Project settings
│   ├── urls.py               # Main URL configuration
│   └── wsgi.py
│
├── core/                      # Main application
│   ├── views.py              # View functions
│   ├── urls.py               # App URL patterns
│   └── models.py             # Database models (for Phase 2)
│
├── templates/                 # HTML templates
│   ├── base.html             # Base template
│   └── core/
│       ├── home.html         # Homepage
│       ├── chatbot.html      # Chatbot page
│       └── insurance_predictor.html
│
├── static/                    # Static files (CSS, JS, images)
├── media/                     # User uploaded files
├── .env                       # Environment variables
├── requirements.txt          # Python dependencies
├── manage.py                 # Django management script
└── db.sqlite3               # SQLite database
```

## Features Explanation 📋

### Home Page
- Clean, modern interface with gradient design
- Feature cards showcasing main functionalities
- Responsive layout that works on all devices

### Healthcare Chatbot
- AI-powered responses using Google Gemini
- Chat history during session
- User-friendly interface with smooth animations
- Disclaimer for medical advice

### Insurance Cost Predictor
- Interactive form with validation
- Real-time calculation
- Detailed cost breakdown showing:
  - Base cost
  - Age-related costs
  - BMI impact
  - Family size impact
  - Smoking status impact
  - Regional variations

## API Endpoints 🔌

- `/` - Home page
- `/chatbot/` - Chatbot interface
- `/insurance-predictor/` - Insurance predictor page
- `/api/chat/` - POST endpoint for chatbot
- `/api/predict-insurance/` - POST endpoint for insurance prediction

## Troubleshooting 🔧

### Common Issues

**1. Module not found errors**
```bash
pip install -r requirements.txt
```

**2. Gemini API not working**
- Check if API key is correctly set in `.env`
- Verify API key is active at Google AI Studio
- Check internet connection

**3. Database errors**
```bash
python manage.py makemigrations
python manage.py migrate
```

**4. Static files not loading**
```bash
python manage.py collectstatic
```

**5. Port already in use**
```bash
python manage.py runserver 8080
```

## Next Steps (Phase 2) 🔜

- User authentication (Patient & Doctor)
- OAuth 2.0 integration
- Patient dashboard
- Doctor dashboard
- Appointment management
- Medical records system
- Chat system between patients and doctors
- Payment integration

## Technologies Used 💻

- **Backend**: Django 4.2
- **AI**: Google Gemini API
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite (default)
- **Environment Management**: python-decouple

## Tips for Beginners 💡

1. **Always activate your virtual environment** before working
2. **Keep your API key secret** - never commit `.env` to version control
3. **Run migrations** after any model changes
4. **Use the admin panel** (`/admin/`) to manage data easily
5. **Check the console** for error messages when debugging

## Security Notes 🔒

- Keep `SECRET_KEY` and `GEMINI_API_KEY` secure
- Never share your `.env` file
- Set `DEBUG=False` in production
- Add `.env` to `.gitignore` file

## Support 🆘

If you encounter any issues:
1. Check the error message in the terminal
2. Verify all files are in correct locations
3. Ensure virtual environment is activated
4. Check if all dependencies are installed

## License 📄

This project is for educational purposes.

---

**Created for learning Django and Machine Learning integration**

Happy Coding! 🚀