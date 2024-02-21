from django.shortcuts import render, redirect
from .forms import OnderzoekForm

def onderzoek_invoeren(request):
    if request.method == 'POST':
        form = OnderzoekForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'onderzoek_form.html', {'form': OnderzoekForm(), 'success_message': True})
    else:
        form = OnderzoekForm()

    return render(request, 'onderzoek_form.html', {'form': form})

