from django.urls import path
from .views import onderzoekstabel_view

urlpatterns = [
    path('onderzoekstabel/', onderzoekstabel_view, name='onderzoekstabel'),
]