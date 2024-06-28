from django.shortcuts import render, redirect
from django.http import JsonResponse
from store.models.chocolat import Chocolat, Boite, BoiteChocolat
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json

@csrf_exempt
@login_required
def simulation_menu(request):
    chocolats = Chocolat.objects.all()
    boites = Boite.objects.all()

    if request.method == 'POST':
        selected_chocolats_ids = request.POST.getlist('selected-chocolats')
        boite_id = request.POST.get('boite-id')  # ID de la boîte sélectionnée par l'utilisateur

        try:
            if selected_chocolats_ids and boite_id:
                boite = Boite.objects.get(id=boite_id)
                client = request.user.customer  # Supposons que vous avez un système d'authentification avec un utilisateur client

                # Créer une instance de BoiteChocolat pour enregistrer les détails
                boite_chocolat = BoiteChocolat.objects.create(
                    boite=boite,
                    prix=boite.prix,
                    nombre_chocolats=boite.nombre_chocolats(),
                    client=client
                )

                # Ajouter les chocolats sélectionnés à BoiteChocolat
                for chocolat_id in selected_chocolats_ids:
                    chocolat = Chocolat.objects.get(id=chocolat_id)
                    boite_chocolat.chocolats.add(chocolat)

                # Sauvegarder BoiteChocolat
                boite_chocolat.save()

                # Ajouter la boîte au panier (session) si nécessaire
                cart = request.session.get('cart', {})
                cart[str(boite_chocolat.id)] = {'quantity': 1}
                request.session['cart'] = cart

                return JsonResponse({'success': True, 'redirect_url': '/cart/'})
        
        except Exception as e:
            return JsonResponse({'success': False, 'error_message': str(e)}, status=500)

    context = {
        'chocolats': chocolats,
        'boites': boites,
    }
    return render(request, 'simulation_menu.html', context)
