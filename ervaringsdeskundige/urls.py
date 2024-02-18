from django.urls import path
from .views import dashboard, aanmelden_voor_onderzoek, registratie_ervaringsdeskundige

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('registratie_ervaringsdeskundige/',registratie_ervaringsdeskundige),
    path('aanmelden/<int:onderzoek_id>/', aanmelden_voor_onderzoek, name='aanmelden_voor_onderzoek'),
]
