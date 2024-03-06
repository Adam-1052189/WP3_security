from django.urls import path, include
from .views import onderzoekstabel_view, maak_organisatie_aan
from organisaties import views

urlpatterns = [
    path('onderzoekstabel/', onderzoekstabel_view, name='dashboard_organisatie'),
    path('onderzoek/invoeren/', views.onderzoek_invoeren, name='onderzoek_invoeren'),
    path('maak_organisatie_aan/', views.maak_organisatie_aan, name='maak_organisatie_aan'),
    path('logout/', views.logout_view, name='logout'),
]