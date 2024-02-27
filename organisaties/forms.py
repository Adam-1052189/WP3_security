from django import forms
from core.models import Onderzoek


class OnderzoekForm(forms.ModelForm):

    STATUS_CHOICES = [
        ('Nieuw', 'Nieuw'),
    ]

    status = forms.ChoiceField(choices=STATUS_CHOICES)
    class Meta:
        model = Onderzoek
        fields = '__all__'
        widgets = {
            'datum_vanaf': forms.DateInput(attrs={'type': 'text', 'class': 'datepicker', 'autocomplete': 'off'}),
            'datum_tot': forms.DateInput(attrs={'type': 'text', 'class': 'datepicker', 'autocomplete': 'off'})
        }