from django.urls import path
from .views import onderzoekstabel_view
from organisaties import views

urlpatterns = [
    path('onderzoekstabel/', onderzoekstabel_view, name='dashboard_organisatie'),
    path('onderzoek/invoeren/', views.onderzoek_invoeren, name='onderzoek_invoeren'),
]