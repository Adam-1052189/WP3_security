from django.urls import path
from .views import OrganisatieListView, OrganisatieCreateAPIView

urlpatterns = [
    path('organisaties/', OrganisatieListView.as_view(), name='organisatie-list'),
    path('organisatie/create/', OrganisatieCreateAPIView.as_view(), name='organisatie_create_api'),
]