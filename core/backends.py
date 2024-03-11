from django.contrib.auth.backends import BaseBackend
from .models import Gebruikers, Ervaringsdeskundige
from django.contrib.auth.hashers import check_password


class GebruikersBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            user = Gebruikers.objects.get(email=email)
            if check_password(password, user.password):
                return user
        except Gebruikers.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Gebruikers.objects.get(pk=user_id)
        except Gebruikers.DoesNotExist:
            return None

    def user_can_authenticate(self, user):
        try:
            ervaringsdeskundige = Ervaringsdeskundige.objects.get(gebruiker=user)
            return ervaringsdeskundige.is_goedgekeurd
        except Ervaringsdeskundige.DoesNotExist:
            return False
