from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.models import Onderzoek, Gebruikers
from django.http import HttpResponseRedirect
from django.urls import reverse

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

@login_required(login_url='login')
def onderzoek_dashboard(request):
    gebruiker_id = request.session.get('gebruiker_id')
    if not gebruiker_id or not Gebruikers.objects.filter(gebruiker_id=gebruiker_id, is_beheerder=True).exists():
        return redirect('login')

    onderzoeken = Onderzoek.objects.all()
    return render(request, 'dashboard_beheer.html', {'onderzoeken': onderzoeken})


def onderzoek_goedkeuren(request, pk):
    onderzoek = Onderzoek.objects.get(pk=pk)
    onderzoek.status = 'Goedgekeurd'
    onderzoek.save()
    return HttpResponseRedirect(reverse('onderzoek_dashboard'))

def onderzoek_afkeuren(request, pk):
    onderzoek = Onderzoek.objects.get(pk=pk)
    onderzoek.status = 'Afgekeurd'
    onderzoek.save()
    return HttpResponseRedirect(reverse('onderzoek_dashboard'))