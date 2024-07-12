from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from store.forms import SellerRegistrationForm  # Corrigez le chemin d'importation

def register_seller(request):
    if request.method == 'POST':
        form = SellerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Votre compte vendeur a été créé avec succès.')
            return redirect('/seller/')  # Redirigez directement vers /seller après l'inscription
    else:
        form = SellerRegistrationForm()

    return render(request, 'registerSeller.html', {'form': form})
