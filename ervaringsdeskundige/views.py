from django.shortcuts import render, redirect
from .forms import RegistratieFormulier
from .models import Gebruikers, Beperkingen, Toezichthouder, Hulpmiddelen, Ervaringsdeskundige

def dashboard(request):
    return render(request, 'dashboard_deskundige.html')

def registratie_ervaringsdeskundige(request):
    if request.method == 'POST':
        form = RegistratieFormulier(request.POST)
        if form.is_valid():
            # Gebruiker object aanmaken en opslaan
            gebruikers = Gebruikers(
                voornaam=form.cleaned_data['voornaam'],
                achternaam=form.cleaned_data['achternaam'],
                is_beheerder=form.cleaned_data['is_beheerder'],
                postcode=form.cleaned_data['postcode'],
                geslacht=form.cleaned_data['geslacht'],
                email=form.cleaned_data['email'],
                wachtwoord=form.cleaned_data['wachtwoord'],  # Overweeg het gebruik van set_password
                telefoonnummer=form.cleaned_data['telefoonnummer'],
                geboortedatum=form.cleaned_data['geboortedatum']
            )
            gebruikers.save()

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
                gebruikers=gebruikers,
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