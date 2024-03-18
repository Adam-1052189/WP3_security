from core.models import Onderzoek, Gebruikers, Organisaties
from django.shortcuts import render, redirect
from organisaties.forms import OnderzoekForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import OrganisatieSerializer, OnderzoekSerializer
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .forms import Onderzoek_Wijzigen_Form
from django.utils.decorators import method_decorator

class Maak_organisatie_aan_APIView(APIView):
    def post(self, request, format=None):
        serializer = OrganisatieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Maak_onderzoek_aan_APIView(APIView):
    def post(self, request, format=None):
        serializer = OnderzoekSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Weergeef_onderzoek_met_API(APIView):
    @method_decorator(login_required)
    def get(self, request, format=None):
        organisatie = request.user.organisatie
        onderzoeken = Onderzoek.objects.filter(organisatie=organisatie)
        serializer = OnderzoekSerializer(onderzoeken, many=True)
        return Response(serializer.data)

class Weergeef_organisatie_met_API(APIView):
    @method_decorator(login_required)
    def get(self, request, format=None):
        organisatie = request.user.organisatie
        organisaties = Organisaties.objects.filter(pk=organisatie.pk)
        serializer = OrganisatieSerializer(organisaties, many=True)
        return Response(serializer.data)

def maak_organisatie_aan(request):
    if request.method == 'POST':
        naam = request.POST.get('naam')
        type = request.POST.get('type')
        website = request.POST.get('website')
        beschrijving = request.POST.get('beschrijving')
        contactpersoon = request.POST.get('contactpersoon')
        email = request.POST.get('email')
        telefoonnummer = request.POST.get('telefoonnummer')
        overige_details = request.POST.get('overige_details')
        api_key = request.POST.get('api_key')

        organisatie = Organisaties.objects.create(naam=naam, type=type, website=website,
                                                  beschrijving=beschrijving, contactpersoon=contactpersoon, email=email,
                                                  telefoonnummer=telefoonnummer, overige_details=overige_details,
                                                  api_key=api_key)

        return JsonResponse({'message': 'Organisatie aangemaakt met succes!'})

    return render(request, 'maak_organisatie_aan.html')

@login_required
def onderzoekstabel_view(request):
    if request.user.is_authenticated and request.user.is_organisatie:
        onderzoeken = Onderzoek.objects.filter(organisatie=request.user.organisatie)
        return render(request, 'organisatie_dashboard.html', {'onderzoeken': onderzoeken})
    else:
        return redirect('login')

@login_required
def onderzoek_sluiten(request, onderzoek_id):
    if request.method == 'POST':
        onderzoek = Onderzoek.objects.get(pk=onderzoek_id)
        onderzoek.status = 'Gesloten'
        onderzoek.save()
        messages.success(request, 'Onderzoek is succesvol gesloten.')
    return redirect('dashboard_organisatie')

@login_required
def onderzoek_wijzigen(request, onderzoek_id):
    onderzoek = get_object_or_404(Onderzoek, pk=onderzoek_id)
    if request.method == 'POST':
        form = Onderzoek_Wijzigen_Form(request.POST, instance=onderzoek)
        if form.is_valid():
            form.save()
            return redirect('dashboard_organisatie')
    else:
        form = Onderzoek_Wijzigen_Form(instance=onderzoek)
    return render(request, 'onderzoek_wijzigen.html', {'form': form})

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

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'Je bent succesvol uitgelogd.')
        return JsonResponse({"success": True, "message": "Je bent succesvol uitgelogd."})
    else:
        return JsonResponse({"success": False, "message": "Foutieve verzoekmethode."}, status=400)