from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth import authenticate, login

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Authenticeren van de gebruiker
        user = authenticate(request, email=email, password=password)

        if user is not None:
            # Gebruiker bestaat, inloggen en doorsturen
            login(request, user)
            return redirect('dashboard')
        else:
            # Ongeldige inloggegevens
            messages.error(request, 'Ongeldige e-mail of wachtwoord.')
            return redirect('login')
    else:
        return render(request, 'inloggen.html')

