from django.shortcuts import render
from core.models import Onderzoek
from django.shortcuts import render, redirect
from organisaties.forms import OnderzoekForm

def onderzoekstabel_view(request):
    onderzoeken = Onderzoek.objects.all()
    return render(request, 'organisatie_dashboard.html', {'onderzoeken': onderzoeken})



def onderzoek_invoeren(request):
    if request.method == 'POST':
        form = OnderzoekForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'onderzoek_form.html', {'form': OnderzoekForm(), 'success_message': True})
    else:
        form = OnderzoekForm()

    return render(request, 'onderzoek_form.html', {'form': form})