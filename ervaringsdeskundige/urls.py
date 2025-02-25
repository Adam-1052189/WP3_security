from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard_deskundige'),
    path('onderzoek/<int:onderzoek_id>/', views.onderzoek_details, name='onderzoek_details'),
    path('onderzoek/<int:onderzoek_id>/aanmelden/', views.aanmelden_voor_onderzoek, name='aanmelden_voor_onderzoek'),
    path('onderzoek/<int:onderzoek_id>/annuleren/', views.annuleren_voor_onderzoek, name='annuleren_voor_onderzoek'),
    path('profiel/', views.profiel, name='profiel'),
    path('logout/', views.logout_view, name='logout'),
    path('laad-onderzoeken/', views.laad_onderzoeken, name='laad_onderzoeken')
]
