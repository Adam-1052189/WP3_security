from rest_framework import serializers
from core.models import Notificatie

class NotificatieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificatie
        fields = ['id', 'bericht', 'is_gelezen', 'aangemaakt_op']
