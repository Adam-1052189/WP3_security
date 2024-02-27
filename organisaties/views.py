from django.shortcuts import render
from core.models import Onderzoek, Gebruikers
from django.shortcuts import render, redirect
from organisaties.forms import OnderzoekForm
from django.contrib.auth.decorators import login_required


@login_required
def onderzoekstabel_view(request):
    if request.user.is_authenticated and request.user.is_organisatie:
        onderzoeken = Onderzoek.objects.all()
        return render(request, 'organisatie_dashboard.html', {'onderzoeken': onderzoeken})
    else:
        return redirect('login')

@login_required
def onderzoek_invoeren(request):
    if request.method == 'POST':
        form = OnderzoekForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'onderzoek_form.html', {'form': OnderzoekForm(), 'success_message': True})
    else:
        form = OnderzoekForm()

    return render(request, 'onderzoek_form.html', {'form': form})