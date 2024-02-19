from django.forms import ModelForm
from core.models import Onderzoek

class OnderzoekForm(ModelForm):
    class Meta:
        model = Onderzoek
        fields = '__all__'