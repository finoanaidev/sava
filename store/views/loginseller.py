from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

def loginseller(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
        except User.DoesNotExist:
            user = None

        if user is not None:
            login(request, user)
            messages.success(request, 'Connexion réussie.')
            return redirect('/seller/')  # Redirection vers /seller après connexion réussie
        else:
            messages.error(request, 'Email ou mot de passe incorrect.')

    return render(request, 'loginSeller.html')
