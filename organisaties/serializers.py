from rest_framework import serializers
from core.models import Organisaties, Onderzoek

class OrganisatieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisaties
        fields = '__all__'

    def create(self, validated_data):
        api_key = validated_data.pop('api_key')

        organisatie = Organisaties.objects.create(**validated_data)

        organisatie.api_key = api_key
        organisatie.save()

        return organisatie

class OnderzoekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Onderzoek
        fields = '__all__'