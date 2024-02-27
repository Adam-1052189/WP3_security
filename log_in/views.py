from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from core.models import Gebruikers

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Authenticeren van de gebruiker
        user = authenticate(request, email=email, password=password)

        if user is not None:
            # Gebruiker bestaat, inloggen en doorsturen
            auth_login(request, user)
            gebruiker = Gebruikers.objects.get(email=email)

            next_url = request.POST.get('next') or request.GET.get('next')

            if gebruiker.is_organisatie:
                return redirect(next_url if next_url else '/organisaties/onderzoekstabel/')
            elif not gebruiker.is_beheerder:
                return redirect(next_url if next_url else 'dashboard_deskundige')
            else:
                return redirect(next_url if next_url else 'dashboard_beheer')
        else:
            # Ongeldige inloggegevens
            messages.error(request, 'Ongeldige e-mail of wachtwoord.')
            return redirect('login')
    else:
        return render(request, 'inloggen.html')
