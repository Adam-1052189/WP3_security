from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard),
    path('registratie_ervaringsdeskundige/', views.registratie_ervaringsdeskundige),
]
