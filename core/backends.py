from django.contrib.auth.backends import BaseBackend
from .models import Gebruikers
from django.contrib.auth.hashers import check_password

class GebruikersBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            user = Gebruikers.objects.get(email=email)
            if user and check_password(password, user.wachtwoord):
                return user
        except Gebruikers.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Gebruikers.objects.get(pk=user_id)
        except Gebruikers.DoesNotExist:
            return None
