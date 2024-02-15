from django import forms
from core.models import Gebruikers, Beperkingen, Toezichthouder, Hulpmiddelen, Ervaringsdeskundige

class RegistratieFormulier(forms.Form):
    # Gebruikers velden
    voornaam = forms.CharField(max_length=255)
    achternaam = forms.CharField(max_length=255)
    is_beheerder = forms.BooleanField(required=False)
    postcode = forms.CharField(max_length=6, required=False)
    geslacht = forms.CharField(max_length=1, required=False)
    email = forms.CharField(max_length=255)
    wachtwoord = forms.CharField(widget=forms.PasswordInput())
    telefoonnummer = forms.CharField(max_length=15, required=False)
    geboortedatum = forms.DateField()

    # Beperkingen velden
    auditieve_beperkingen = forms.CharField(widget=forms.Textarea, required=False)
    visuele_beperkingen = forms.CharField(widget=forms.Textarea, required=False)
    motorische_lichamelijke_beperkingen = forms.CharField(widget=forms.Textarea, required=False)
    cognitieve_neurologische_beperkingen = forms.CharField(widget=forms.Textarea, required=False)
    reden_beperking = forms.CharField(widget=forms.Textarea, required=False)

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