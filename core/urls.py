from django.urls import path
from . import views

urlpatterns = [
    path('onderzoek/invoeren/', views.onderzoek_invoeren, name='onderzoek_invoeren'),
]