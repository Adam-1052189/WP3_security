from django.urls import path
from .views import dashboard, aanmelden_voor_onderzoek, onderzoek_details

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('onderzoek/<int:onderzoek_id>/', onderzoek_details, name='onderzoek_details'),
    path('aanmelden/<int:onderzoek_id>/', aanmelden_voor_onderzoek, name='aanmelden_voor_onderzoek'),
]
