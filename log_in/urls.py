from django.urls import path
from . import views
from ervaringsdeskundige.views import registratie_ervaringsdeskundige

urlpatterns = [
    path('', views.login_view, name="login"),
    path('registratie/', registratie_ervaringsdeskundige, name="registratie"),
]

