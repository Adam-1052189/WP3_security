from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from core.models import Onderzoek, Gebruikers, Ervaringsdeskundige, OnderzoekErvaringsdeskundige
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import OnderzoekForm
from django.contrib.auth import get_user_model

def beheerder_required(view_func):
    def wrap(request, *args, **kwargs):
        gebruiker_id = request.session.get('gebruiker_id')
        if gebruiker_id:
            try:
                gebruiker = Gebruikers.objects.get(pk=gebruiker_id)
                if gebruiker.is_beheerder:
                    return view_func(request, *args, **kwargs)
                else:
                    return HttpResponse('Geen toegang: Geen beheerder', status=403)
            except Gebruikers.DoesNotExist:
                return HttpResponse('Gebruiker niet gevonden', status=404)
        else:
            return redirect('login')
    return wrap

@login_required()
def onderzoek_dashboard(request):
    User = get_user_model()
    if not request.user.is_staff:
        return redirect('dashboard_deskundige')

    niet_goedgekeurde_inschrijvingen = OnderzoekErvaringsdeskundige.objects.filter(is_goedgekeurd=False)
    nieuwe_ervaringsdeskundigen = Ervaringsdeskundige.objects.filter(is_goedgekeurd=False, gebruiker__is_organisatie=False)

    onderzoeken = Onderzoek.objects.filter(status__in=['', 'Afgekeurd', 'Nieuw'])
    return render(request, 'dashboard_beheer.html', {
        'niet_goedgekeurde_inschrijvingen': niet_goedgekeurde_inschrijvingen,
        'nieuwe_ervaringsdeskundigen': nieuwe_ervaringsdeskundigen,
        'onderzoeken': onderzoeken,
    })


def onderzoek_goedkeuren(request, pk):
    onderzoek = Onderzoek.objects.get(pk=pk)
    onderzoek.status = 'Goedgekeurd'
    onderzoek.is_goedgekeurd = True
    onderzoek.save()
    return HttpResponseRedirect(reverse('dashboard_beheer'))

def onderzoek_afkeuren(request, pk):
    if request.method == 'POST':
        try:
            onderzoek = Onderzoek.objects.get(pk=pk)
            onderzoek.status = 'Afgekeurd'
            onderzoek.save()
            return JsonResponse({'status': 'success', 'message': 'Onderzoek succesvol afgekeurd'})
        except Onderzoek.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Onderzoek niet gevonden'}, status=404)

def goedkeuren_inschrijving(request, pk):
    inschrijving = get_object_or_404(OnderzoekErvaringsdeskundige, pk=pk)
    inschrijving.is_goedgekeurd = True
    inschrijving.save()
    return redirect('dashboard_beheer')

def afkeuren_inschrijving(request, pk):
    if request.method == 'POST':
        inschrijving = get_object_or_404(OnderzoekErvaringsdeskundige, pk=pk)
        inschrijving.is_goedgekeurd = False
        inschrijving.save()
        return JsonResponse({'status': 'success', 'message': 'Inschrijving succesvol afgekeurd.'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Ongeldig verzoek'}, status=400)

def verwijder_inschrijving(request, pk):
    if request.method == 'DELETE':
        inschrijving = get_object_or_404(OnderzoekErvaringsdeskundige, pk=pk)
        inschrijving.delete()
        return JsonResponse({'status': 'success', 'message': 'Inschrijving succesvol verwijderd.'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Ongeldig verzoek'}, status=400)

def toon_inschrijvingen(request):
    inschrijvingen = OnderzoekErvaringsdeskundige.objects.all()
    return render(request, 'toon_inschrijvingen.html', {'inschrijvingen': inschrijvingen})

def goedkeuren_ervaringsdeskundige(request, pk):
    ervaringsdeskundige = get_object_or_404(Ervaringsdeskundige, pk=pk)
    ervaringsdeskundige.is_goedgekeurd = True
    ervaringsdeskundige.save()
    return redirect('dashboard_beheer')

def afkeuren_ervaringsdeskundige(request, pk):
    if request.method == 'POST':
        ervaringsdeskundige = get_object_or_404(Ervaringsdeskundige, pk=pk)
        ervaringsdeskundige.is_goedgekeurd = False
        ervaringsdeskundige.save()
        return JsonResponse({'status': 'success', 'message': 'Ervaringsdeskundige succesvol afgekeurd.'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Ongeldige verzoekmethode'}, status=400)

def onderzoek_gegevens(request, pk):
    onderzoek = get_object_or_404(Onderzoek, pk=pk)
    form = OnderzoekForm(instance=onderzoek)
    return render(request, 'onderzoek_gegevens.html', {'onderzoek': onderzoek, 'form': form})

def onderzoek_update(request, pk):
    if request.method == 'POST':
        onderzoek = get_object_or_404(Onderzoek, pk=pk)
        form = OnderzoekForm(request.POST, instance=onderzoek)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": "Onderzoek succesvol bijgewerkt."})
        else:
            return JsonResponse({"error": form.errors}, status=400)
    return JsonResponse({"error": "Alleen POST-verzoeken zijn toegestaan."}, status=400)

def onderzoeksvragen(request):
    onderzoeken = Onderzoek.objects.all()
    return render(request, 'onderzoeksvragen.html', {'onderzoeken': onderzoeken})


def ervaringsdeskundige(request):
    ervaringsdeskundigen = Gebruikers.objects.all()
    return render(request, 'ervaringsdeskundige.html', {'ervaringsdeskundigen': ervaringsdeskundigen})
