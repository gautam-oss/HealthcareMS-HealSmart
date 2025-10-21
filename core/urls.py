from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('insurance-predictor/', views.insurance_predictor, name='insurance_predictor'),
    path('api/chat/', views.chat_api, name='chat_api'),
    path('api/predict-insurance/', views.predict_insurance, name='predict_insurance'),
]