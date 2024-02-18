from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Authenticeren van de gebruiker
        user = authenticate(request, email=email, password=password)

        if user is not None:
            # Gebruiker bestaat, inloggen en doorsturen
            auth_login(request, user)
            return redirect('dashboard')
        else:
            # Ongeldige inloggegevens
            messages.error(request, 'Ongeldige e-mail of wachtwoord.')
            return redirect('login')
    else:
        return render(request, 'inloggen.html')
