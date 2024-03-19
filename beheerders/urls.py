from django.urls import path
from ervaringsdeskundige.views import logout_view
from . import views


urlpatterns = [
    path('dashboard/', views.onderzoek_dashboard, name='dashboard_beheer'),
    path('goedkeuren/<int:pk>/', views.onderzoek_goedkeuren, name='onderzoek_goedkeuren'),
    path('afkeuren/<int:pk>/', views.onderzoek_afkeuren, name='onderzoek_afkeuren'),
    path('onderzoeksvragen/afkeuren/<int:pk>/', views.onderzoek_afkeuren_ajax, name='onderzoek_afkeuren_ajax'),
    path('onderzoeksvragen/goedkeuren/<int:pk>/', views.onderzoek_goedkeuren_ajax, name='onderzoek_goedkeuren_ajax'),
    path('inschrijvingen/goedkeuren/<int:pk>/', views.goedkeuren_inschrijving, name='inschrijving_goedkeuren'),
    path('inschrijvingen/goedkeuren_ajax/<int:pk>/', views.goedkeuren_inschrijving_ajax, name='inschrijving_goedkeuren_ajax'),
    path('inschrijvingen/afkeuren/<int:pk>/', views.afkeuren_inschrijving, name='inschrijving_afkeuren'),
    path('inschrijvingen/afkeuren_ajax/<int:pk>/', views.afkeuren_inschrijving_ajax, name='inschrijving_afkeuren_ajax'),
    path('toon_inschrijvingen/', views.toon_inschrijvingen, name='inschrijvingen'),
    path('ervaringsdeskundige/goedkeuren/<int:pk>/', views.goedkeuren_ervaringsdeskundige, name='ervaringsdeskundige_goedkeuren'),
    path('ervaringsdeskundige/afkeuren/<int:pk>/', views.afkeuren_ervaringsdeskundige, name='ervaringsdeskundige_afkeuren'),
    path('onderzoek/gegevens/<int:pk>/', views.onderzoek_gegevens, name='onderzoek_gegevens'),
    path('onderzoek/update/<int:pk>/', views.onderzoek_update, name='onderzoek_update'),
    path('onderzoeksvragen/', views.onderzoeksvragen, name='onderzoeksvragen'),
    path('toon_inschrijvingen/verwijder_inschrijving/<int:pk>/', views.verwijder_inschrijving, name='verwijder_inschrijving'),
    path('ervaringsdeskundige/', views.ervaringsdeskundige, name='ervaringsdeskundige'),
    path('logout/', logout_view, name='logout'),
    path('api/notificaties/', views.NotificatieAPIView.as_view(), name='notificaties'),
    path('api/notificaties/<int:notificatie_id>/markeer-als-gelezen/', views.markeer_notificatie_als_gelezen, name='markeer-als-gelezen'),
    path('api/nieuwe_inschrijvingen_notificaties/', views.nieuwe_inschrijvingen_notificaties, name='nieuwe_inschrijvingen_notificaties'),
    path('api/nieuwe_inschrijvingen/<int:inschrijving_id>/markeer_als_gelezen/', views.markeer_als_gelezen, name='markeer_als_gelezen'),
]