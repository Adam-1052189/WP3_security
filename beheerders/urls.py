from django.urls import path
from .views import onderzoek_dashboard, onderzoek_goedkeuren, onderzoek_afkeuren, toon_inschrijvingen
from . import views

urlpatterns = [
    path('dashboard/', onderzoek_dashboard, name='dashboard_beheer'),
    path('goedkeuren/<int:pk>/', onderzoek_goedkeuren, name='onderzoek_goedkeuren'),
    path('afkeuren/<int:pk>/', onderzoek_afkeuren, name='onderzoek_afkeuren'),
    path('inschrijvingen/goedkeuren/<int:inschrijving_id>/', views.goedkeuren_inschrijving, name='inschrijving_goedkeuren'),
    path('inschrijvingen/afkeuren/<int:inschrijving_id>/', views.afkeuren_inschrijving, name='inschrijving_afkeuren'),
    path('inschrijvingen/', toon_inschrijvingen, name='toon_inschrijvingen'),
    path('ervaringsdeskundige/goedkeuren/<int:pk>/', views.goedkeuren_ervaringsdeskundige, name='ervaringsdeskundige_goedkeuren'),
    path('ervaringsdeskundige/afkeuren/<int:pk>/', views.afkeuren_ervaringsdeskundige, name='ervaringsdeskundige_afkeuren'),
]