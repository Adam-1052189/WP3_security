from django.shortcuts import render, redirect
from .forms import RegistratieFormulier
from core.models import Gebruikers, Beperkingen, Toezichthouder, Hulpmiddelen, Ervaringsdeskundige, Onderzoek, OnderzoekErvaringsdeskundige
from django.views import View
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from core.decorators import custom_login_required

def registratie_ervaringsdeskundige(request):
    if request.method == 'POST':
        form = RegistratieFormulier(request.POST)
        if form.is_valid():
            # Gebruiker object aanmaken en opslaan
            gebruiker = Gebruikers(
                voornaam=form.cleaned_data['voornaam'],
                achternaam=form.cleaned_data['achternaam'],
                postcode=form.cleaned_data['postcode'],
                geslacht=form.cleaned_data['geslacht'],
                email=form.cleaned_data['email'],
                wachtwoord=form.cleaned_data['wachtwoord'],  # Overweeg het gebruik van set_password
                telefoonnummer=form.cleaned_data['telefoonnummer'],
                geboortedatum=form.cleaned_data['geboortedatum']
            )
            gebruiker.save()

            # Beperkingen object aanmaken en opslaan
            beperkingen = Beperkingen(
                auditieve_beperkingen=form.cleaned_data['auditieve_beperkingen'],
                visuele_beperkingen=form.cleaned_data['visuele_beperkingen'],
                motorische_lichamelijke_beperkingen=form.cleaned_data['motorische_lichamelijke_beperkingen'],
                cognitieve_neurologische_beperkingen=form.cleaned_data['cognitieve_neurologische_beperkingen'],
                reden_beperking=form.cleaned_data['reden_beperking']
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
                bijzonderheden = form.cleaned_data['bijzonderheden'],
                voorkeur_benadering = form.cleaned_data['voorkeur_benadering'],
                bijzonderheden_beschikbaar = form.cleaned_data['bijzonderheden_beschikbaar']
            )
            ervaringsdeskundige.save()

            return redirect('login')  # Pas dit aan naar de gewenste redirect URL
    else:
        form = RegistratieFormulier()

    return render(request, 'registratie_ervaringsdeskundige.html', {'form': form})

@custom_login_required
def dashboard(request):
    gebruiker_id = request.user.id  # Veronderstelt dat je een manier hebt om de huidige gebruiker te krijgen
    ervaringsdeskundige = Ervaringsdeskundige.objects.filter(gebruiker_id=gebruiker_id).first()
    if ervaringsdeskundige:
        beschikbare_onderzoeken = Onderzoek.objects.filter(beschikbaar=True)
        context = {
            'beschikbare_onderzoeken': beschikbare_onderzoeken,
        }
        return render(request, 'dashboard_deskundige.html', context)
    else:
        return HttpResponse('Je moet een ervaringsdeskundige zijn om deze pagina te bekijken.', status=403)

def aanmelden_voor_onderzoek(request, onderzoek_id):
    if request.method == 'POST':
        gebruiker_id = request.user.id
        ervaringsdeskundige = Ervaringsdeskundige.objects.filter(gebruiker=gebruiker_id).first()
        if ervaringsdeskundige:
            onderzoek = Onderzoek.objects.get(id=onderzoek_id)
            OnderzoekErvaringsdeskundige.objects.create(onderzoek=onderzoek, ervaringsdeskundige=ervaringsdeskundige)
            messages.success(request, 'Je bent succesvol aangemeld voor het onderzoek.')
            return redirect('dashboard')
        else:
            return HttpResponse('Je moet een ervaringsdeskundige zijn om je aan te melden voor een onderzoek.', status=403)