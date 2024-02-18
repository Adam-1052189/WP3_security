from django.urls import path
from .views import onderzoek_dashboard, onderzoek_goedkeuren, onderzoek_afkeuren

urlpatterns = [
    path('dashboard/', onderzoek_dashboard, name='dashboard_beheer'),
    path('goedkeuren/<int:pk>/', onderzoek_goedkeuren, name='onderzoek_goedkeuren'),
    path('afkeuren/<int:pk>/', onderzoek_afkeuren, name='onderzoek_afkeuren'),
]