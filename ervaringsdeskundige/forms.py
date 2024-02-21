from django import forms
from core.models import Gebruikers, Beperkingen, Toezichthouder, Hulpmiddelen, Ervaringsdeskundige
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import  get_user_model

User = get_user_model()

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
        model = User
        fields = ['voornaam', 'achternaam', 'postcode', 'geslacht', 'email', 'telefoonnummer', 'geboortedatum']

    def __init__(self, *args, **kwargs):
        super(GebruikerForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False

class ErvaringsdeskundigeForm(forms.ModelForm):
    class Meta:
        model = Ervaringsdeskundige
        fields = ['bijzonderheden', 'voorkeur_benadering', 'bijzonderheden_beschikbaar']

    def __init__(self, *args, **kwargs):
        super(ErvaringsdeskundigeForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False

class HulpmiddelenForm(forms.ModelForm):
    class Meta:
        model = Hulpmiddelen
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(HulpmiddelenForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False

class BeperkingenForm(forms.ModelForm):
    class Meta:
        model = Beperkingen
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(BeperkingenForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False

class ToezichthouderForm(forms.ModelForm):
    class Meta:
        model = Toezichthouder
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ToezichthouderForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False

class CustomPasswordChangeForm(PasswordChangeForm):
    pass