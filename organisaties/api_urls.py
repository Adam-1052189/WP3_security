from django.urls import path
from .views import Weergeef_organisatie_met_API, Maak_organisatie_aan_APIView, Maak_onderzoek_aan_APIView, Weergeef_onderzoek_met_API

urlpatterns = [
    path('organisatie/aanmaken/', Maak_organisatie_aan_APIView.as_view(), name='maak_organisatie_aan_met_api'),
    path('organisatie/lijst/', Weergeef_organisatie_met_API.as_view(), name='organisatie_lijst_api'),
    path('onderzoek/aanmaken/', Maak_onderzoek_aan_APIView.as_view(), name='onderzoek_aanmaken_api'),
    path('onderzoek/lijst/', Weergeef_onderzoek_met_API.as_view(), name='onderzoek_lijst_api'),
]