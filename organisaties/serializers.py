from rest_framework import serializers
from core.models import Organisaties

class OrganisatieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisaties
        fields = ['naam', 'api_key']

    def create(self, validated_data):
        api_key = validated_data.pop('api_key')

        organisatie = Organisaties.objects.create(**validated_data)

        organisatie.api_key = api_key
        organisatie.save()

        return organisatie