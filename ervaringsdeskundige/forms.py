from django import forms
from core.models import Gebruikers, Beperkingen, Toezichthouder, Hulpmiddelen, Ervaringsdeskundige
from django.contrib.auth.hashers import make_password

class RegistratieFormulier(forms.Form):
    # Gebruikers velden
    voornaam = forms.CharField(max_length=255)
    achternaam = forms.CharField(max_length=255)
    postcode = forms.CharField(max_length=6, required=False)
    GESLACHT_CHOICES = [('', 'Selecteer geslacht'), ('man', 'man'), ('vrouw', 'vrouw'),]
    geslacht = forms.ChoiceField(choices=GESLACHT_CHOICES, required=False)
    email = forms.CharField(max_length=255)
    wachtwoord = forms.CharField(widget=forms.PasswordInput())
    telefoonnummer = forms.CharField(max_length=15, required=False)
    geboortedatum = forms.DateField()

    GEEN_OPTIE = [('', 'Geen')]
    # Beperkingen velden
    auditieve_beperkingen = forms.ChoiceField(
        choices=GEEN_OPTIE + Beperkingen.AUDITIEVE_BEPERKINGEN_CHOICES,
        required=False,
        label="Auditieve beperkingen"
    )
    visuele_beperkingen = forms.ChoiceField(
        choices=GEEN_OPTIE + Beperkingen.VISUELE_BEPERKINGEN_CHOICES,
        required=False,
        label="Visuele beperkingen"
    )
    motorische_lichamelijke_beperkingen = forms.ChoiceField(
        choices=GEEN_OPTIE + Beperkingen.MOTORISCHE_BEPERKINGEN_CHOICES,
        required=False,
        label="Motorische / lichamelijke beperkingen"
    )
    cognitieve_neurologische_beperkingen = forms.ChoiceField(
        choices=GEEN_OPTIE + Beperkingen.COGNITIEVE_BEPERKINGEN_CHOICES,
        required=False,
        label="Cognitieve / neurologische beperkingen"
    )

    # Toezichthouder velden
    toezichthouder_naam = forms.CharField(max_length=255, required=False)
    toezichthouder_email = forms.EmailField(required=False)
    toezichthouder_telefoonnummer = forms.CharField(max_length=255, required=False)

    # Hulpmiddelen velden
    vergrootglas = forms.BooleanField(required=False)
    scherm_voorlezer = forms.BooleanField(required=False)

    # Ervaringsdeskundige velden
    bijzonderheden = forms.CharField(widget=forms.Textarea, required=False)
    voorkeur_benadering = forms.CharField(max_length=255, required=False)
    bijzonderheden_beschikbaar = forms.CharField(max_length=255, required=False)

class GebruikerForm(forms.ModelForm):
    class Meta:
        model = Gebruikers
        fields = ['voornaam', 'achternaam', 'postcode', 'geslacht', 'email', 'telefoonnummer', 'geboortedatum']
        widgets = {
            'geslacht': forms.Select(choices=[('Man', 'Man'), ('Vrouw', 'Vrouw')]),
        }

class WachtwoordWijzigenForm(forms.Form):
    nieuw_wachtwoord = forms.CharField(widget=forms.PasswordInput())

    def save(self, gebruiker_id):
        gebruiker = Gebruikers.objects.get(gebruiker_id=gebruiker_id)
        gebruiker.wachtwoord = make_password(self.cleaned_data['nieuw_wachtwoord'])
        gebruiker.save()

class ErvaringsdeskundigeForm(forms.ModelForm):
    class Meta:
        model = Ervaringsdeskundige
        fields = ['bijzonderheden', 'voorkeur_benadering', 'bijzonderheden_beschikbaar']


class BeperkingenForm(forms.ModelForm):
    GEEN_OPTIE = [('', 'Geen')]

    auditieve_beperkingen = forms.ChoiceField(
        choices=GEEN_OPTIE + Beperkingen.AUDITIEVE_BEPERKINGEN_CHOICES,
        required=False,
        label="Auditieve beperkingen"
    )
    visuele_beperkingen = forms.ChoiceField(
        choices=GEEN_OPTIE + Beperkingen.VISUELE_BEPERKINGEN_CHOICES,
        required=False,
        label="Visuele beperkingen"
    )
    motorische_lichamelijke_beperkingen = forms.ChoiceField(
        choices=GEEN_OPTIE + Beperkingen.MOTORISCHE_BEPERKINGEN_CHOICES,
        required=False,
        label="Motorische / lichamelijke beperkingen"
    )
    cognitieve_neurologische_beperkingen = forms.ChoiceField(
        choices=GEEN_OPTIE + Beperkingen.COGNITIEVE_BEPERKINGEN_CHOICES,
        required=False,
        label="Cognitieve / neurologische beperkingen"
    )

    class Meta:
        model = Beperkingen
        fields = [
            'auditieve_beperkingen',
            'visuele_beperkingen',
            'motorische_lichamelijke_beperkingen',
            'cognitieve_neurologische_beperkingen',
        ]

class HulpmiddelenForm(forms.ModelForm):
    class Meta:
        model = Hulpmiddelen
        fields = ['vergrootglas', 'scherm_voorlezer']

class ToezichthouderForm(forms.ModelForm):
    class Meta:
        model = Toezichthouder
        fields = ['naam', 'email', 'telefoonnummer']