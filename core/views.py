from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import google.generativeai as genai
import json

# Configure Gemini API
genai.configure(api_key=settings.GEMINI_API_KEY)

def home(request):
    """Home page view"""
    return render(request, 'core/home.html')

def chatbot(request):
    """Chatbot page view"""
    return render(request, 'core/chatbot.html')

def insurance_predictor(request):
    """Insurance predictor page view"""
    return render(request, 'core/insurance_predictor.html')

@csrf_exempt
def chat_api(request):
    """API endpoint for chatbot - handles Gemini API calls"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '')
            
            if not user_message:
                return JsonResponse({'error': 'No message provided'}, status=400)
            
            # Create healthcare-focused prompt
            healthcare_prompt = f"""You are a helpful healthcare assistant. Provide quick, 
            accurate healthcare advice. Keep responses concise and informative. 
            If the query is serious, recommend consulting a healthcare professional.
            
            User question: {user_message}"""
            
            # Call Gemini API
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(healthcare_prompt)
            
            return JsonResponse({
                'response': response.text,
                'success': True
            })
            
        except Exception as e:
            return JsonResponse({
                'error': str(e),
                'success': False
            }, status=500)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def predict_insurance(request):
    """API endpoint for insurance cost prediction"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Get form data
            age = int(data.get('age', 0))
            bmi = float(data.get('bmi', 0))
            children = int(data.get('children', 0))
            smoker = data.get('smoker', 'no')
            region = data.get('region', 'northeast')
            
            # Simple insurance cost calculation formula
            # Base cost
            base_cost = 3000
            
            # Age factor (cost increases with age)
            age_cost = age * 240
            
            # BMI factor
            if bmi < 18.5:
                bmi_cost = 500  # Underweight
            elif 18.5 <= bmi < 25:
                bmi_cost = 0  # Normal
            elif 25 <= bmi < 30:
                bmi_cost = 1000  # Overweight
            else:
                bmi_cost = 2500  # Obese
            
            # Children factor
            children_cost = children * 500
            
            # Smoker factor (significant impact)
            smoker_cost = 23000 if smoker == 'yes' else 0
            
            # Region factor (minor variations)
            region_costs = {
                'northeast': 0,
                'northwest': 500,
                'southeast': 1000,
                'southwest': 750
            }
            region_cost = region_costs.get(region, 0)
            
            # Calculate total
            total_cost = (base_cost + age_cost + bmi_cost + 
                         children_cost + smoker_cost + region_cost)
            
            # Add some realistic variance
            import random
            variance = random.uniform(0.95, 1.05)
            total_cost = round(total_cost * variance, 2)
            
            return JsonResponse({
                'predicted_cost': total_cost,
                'success': True,
                'breakdown': {
                    'base': base_cost,
                    'age_factor': age_cost,
                    'bmi_factor': bmi_cost,
                    'children_factor': children_cost,
                    'smoker_factor': smoker_cost,
                    'region_factor': region_cost
                }
            })
            
        except Exception as e:
            return JsonResponse({
                'error': str(e),
                'success': False
            }, status=500)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)