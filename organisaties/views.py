from django.shortcuts import render
from core.models import Onderzoek


def onderzoekstabel_view(request):
    onderzoeken = Onderzoek.objects.all()
    return render(request, 'organisatie_dashboard.html', {'onderzoeken': onderzoeken})