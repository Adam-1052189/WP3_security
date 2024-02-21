from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistratieFormulier, GebruikerForm, CustomPasswordChangeForm, ErvaringsdeskundigeForm, BeperkingenForm, HulpmiddelenForm, ToezichthouderForm
from core.models import Gebruikers, Beperkingen, Toezichthouder, Hulpmiddelen, Ervaringsdeskundige, Onderzoek, OnderzoekErvaringsdeskundige
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import get_user_model, update_session_auth_hash
from datetime import date

def registratie_ervaringsdeskundige(request):
    if request.method == 'POST':
        form = RegistratieFormulier(request.POST)
        if form.is_valid():
            gebruiker = Gebruikers.objects.create_user(
                voornaam=form.cleaned_data['voornaam'],
                achternaam=form.cleaned_data['achternaam'],
                postcode=form.cleaned_data['postcode'],
                geslacht=form.cleaned_data['geslacht'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['wachtwoord'],
                telefoonnummer=form.cleaned_data['telefoonnummer'],
                geboortedatum=form.cleaned_data['geboortedatum']
            )
            gebruiker.save()

            # Beperkingen object aanmaken en opslaan
            beperkingen = Beperkingen(
                auditieve_beperkingen=form.cleaned_data['auditieve_beperkingen'],
                visuele_beperkingen=form.cleaned_data['visuele_beperkingen'],
                motorische_lichamelijke_beperkingen=form.cleaned_data['motorische_lichamelijke_beperkingen'],
                cognitieve_neurologische_beperkingen=form.cleaned_data['cognitieve_neurologische_beperkingen']
            )
            beperkingen.save()

            # Toezichthouder object aanmaken en opslaan
            toezichthouder = Toezichthouder(
                naam=form.cleaned_data['toezichthouder_naam'],
                email=form.cleaned_data['toezichthouder_email'],
                telefoonnummer=form.cleaned_data['toezichthouder_telefoonnummer']
            )
            toezichthouder.save()

            # Hulpmiddelen object aanmaken en opslaan
            hulpmiddelen = Hulpmiddelen(
                vergrootglas=form.cleaned_data['vergrootglas'],
                scherm_voorlezer=form.cleaned_data['scherm_voorlezer']
            )
            hulpmiddelen.save()

            # Ervaringsdeskundige object aanmaken en koppelen
            ervaringsdeskundige = Ervaringsdeskundige(
                gebruiker=gebruiker,
                beperkingen=beperkingen,
                toezichthouder=toezichthouder,
                hulpmiddelen=hulpmiddelen,
                bijzonderheden=form.cleaned_data['bijzonderheden'],
                voorkeur_benadering=form.cleaned_data['voorkeur_benadering'],
                bijzonderheden_beschikbaar=form.cleaned_data['bijzonderheden_beschikbaar']
            )
            ervaringsdeskundige.save()

            # Aangepaste redirect en succesbericht
            messages.success(request, 'Registratie succesvol.')
            return redirect('login')  # Zorg ervoor dat dit de correcte URL-naam is

    else:
        form = RegistratieFormulier()

    return render(request, 'registratie_ervaringsdeskundige.html', {'form': form})

User = get_user_model()

@login_required()
def dashboard(request):
    ervaringsdeskundige = Ervaringsdeskundige.objects.filter(gebruiker=request.user).first()
    if ervaringsdeskundige:
        beschikbare_onderzoeken = Onderzoek.objects.filter(beschikbaar=True)
        context = {
            'beschikbare_onderzoeken': beschikbare_onderzoeken,
        }
        return render(request, 'dashboard_deskundige.html', context)
    else:
        return HttpResponse('Je moet een ervaringsdeskundige zijn om deze pagina te bekijken.', status=403)

@login_required()
def aanmelden_voor_onderzoek(request, onderzoek_id):
    if request.method == 'POST':
        ervaringsdeskundige = Ervaringsdeskundige.objects.filter(gebruiker=request.user).first()
        if ervaringsdeskundige:
            onderzoek = Onderzoek.objects.get(id=onderzoek_id)
            OnderzoekErvaringsdeskundige.objects.create(onderzoek=onderzoek, ervaringsdeskundige=ervaringsdeskundige)
            messages.success(request, 'Je bent succesvol aangemeld voor het onderzoek.')
            return redirect('dashboard_deskundige')
        else:
            return HttpResponse('Je moet een ervaringsdeskundige zijn om je aan te melden voor een onderzoek.', status=403)

@login_required()
def onderzoek_details(request, onderzoek_id):
    onderzoek = Onderzoek.objects.get(onderzoek_id=onderzoek_id)
    organisatie = onderzoek.organisatie
    context = {
        'onderzoek': onderzoek,
        'organisatie': organisatie,
    }
    return render(request, 'onderzoek_details.html', context)

def leeftijd_berekenen(geboortedatum):
    vandaag = date.today()
    leeftijd = vandaag.year - geboortedatum.year - ((vandaag.month, vandaag.day) < (geboortedatum.month, geboortedatum.day))
    return leeftijd

@login_required
def profiel(request):
    gebruiker = request.user
    leeftijd = leeftijd_berekenen(gebruiker.geboortedatum)
    toon_toezichthouder_form = leeftijd < 18
    ervaringsdeskundige, _ = Ervaringsdeskundige.objects.get_or_create(gebruiker=gebruiker)
    hulpmiddelen, _ = Hulpmiddelen.objects.get_or_create(ervaringsdeskundige=ervaringsdeskundige)
    beperkingen, _ = Beperkingen.objects.get_or_create(ervaringsdeskundige=ervaringsdeskundige)
    toezichthouder, _ = Toezichthouder.objects.get_or_create(ervaringsdeskundige=ervaringsdeskundige) if toon_toezichthouder_form else (None, False)

    if request.method == 'POST':
        gebruiker_form = GebruikerForm(request.POST, instance=gebruiker)
        ervaringsdeskundige_form = ErvaringsdeskundigeForm(request.POST, instance=ervaringsdeskundige)
        hulpmiddelen_form = HulpmiddelenForm(request.POST, instance=hulpmiddelen)
        beperkingen_form = BeperkingenForm(request.POST, instance=beperkingen)
        toezichthouder_form = ToezichthouderForm(request.POST, instance=toezichthouder) if toon_toezichthouder_form else None
        password_form = CustomPasswordChangeForm(user=gebruiker, data=request.POST)

        if 'wijzigen_profiel' in request.POST:
            forms_valid = (gebruiker_form.is_valid() and ervaringsdeskundige_form.is_valid() and
                           hulpmiddelen_form.is_valid() and beperkingen_form.is_valid() and
                           toezichthouder_form.is_valid() if toon_toezichthouder_form else True)
            if forms_valid:
                gebruiker_form.save()
                ervaringsdeskundige_form.save()
                hulpmiddelen_form.save()
                beperkingen_form.save()
                if toon_toezichthouder_form:
                    toezichthouder_form.save()
                messages.success(request, 'Profiel succesvol bijgewerkt.', extra_tags='profiel')
                return redirect('profiel')
            else:
                messages.error(request, 'Controleer alstublieft de ingevoerde gegevens.', extra_tags='profiel')

        elif 'wijzigen_wachtwoord' in request.POST and password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Wachtwoord succesvol gewijzigd.', extra_tags='profiel')
            return redirect('profiel')
    else:
        gebruiker_form = GebruikerForm(instance=gebruiker)
        ervaringsdeskundige_form = ErvaringsdeskundigeForm(instance=ervaringsdeskundige)
        hulpmiddelen_form = HulpmiddelenForm(instance=hulpmiddelen)
        beperkingen_form = BeperkingenForm(instance=beperkingen)
        toezichthouder_form = ToezichthouderForm(instance=toezichthouder) if toon_toezichthouder_form else None
        password_form = CustomPasswordChangeForm(user=gebruiker)

    context = {
        'gebruiker_form': gebruiker_form,
        'ervaringsdeskundige_form': ervaringsdeskundige_form,
        'hulpmiddelen_form': hulpmiddelen_form,
        'beperkingen_form': beperkingen_form,
        'toezichthouder_form': toezichthouder_form,
        'password_form': password_form,
        'toon_toezichthouder_form': toon_toezichthouder_form,
    }
    return render(request, 'profiel.html', context)