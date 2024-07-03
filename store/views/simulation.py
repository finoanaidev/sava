from django.shortcuts import render
from store.models.chocolat import Chocolat, Boite, BoiteChocolat  # Importe seulement Chocolat et Boite depuis models.chocolat
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def simulation_menu(request):
    chocolats = Chocolat.objects.all()
    boites = Boite.objects.all()

    context = {
        'chocolats': chocolats,
        'boites': boites,
    }
    return render(request, 'simulation_menu.html', context)

@csrf_exempt
def enregistrer_boite(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print('Data received:', data) 

        boite_type = data.get('boite_type')
        chocolats_ids = data.get('chocolats')
        print('Boite type:', boite_type)
        print('Chocolats ids:', chocolats_ids)

        if boite_type and chocolats_ids:
            try:
                boite = Boite.objects.get(type=boite_type)  # Récupère la boîte sélectionnée
                selected_chocolats = Chocolat.objects.filter(id__in=chocolats_ids)  # Récupère les chocolats sélectionnés

                # Dictionnaire pour suivre la quantité de chaque chocolat sélectionné
                selected_chocolats_count = {}

                # Compte le nombre de fois que chaque chocolat a été sélectionné
                for chocolat_id in chocolats_ids:
                    if chocolat_id in selected_chocolats_count:
                        selected_chocolats_count[chocolat_id] += 1
                    else:
                        selected_chocolats_count[chocolat_id] = 1

                # Mettre à jour ou créer les entrées BoiteChocolat
                for chocolat in selected_chocolats:
                    quantite = selected_chocolats_count[str(chocolat.id)]  # Obtient la quantité pour ce chocolat

                    # Vérifie si ce chocolat est déjà présent dans la boîte
                    boite_chocolat, created = BoiteChocolat.objects.get_or_create(
                        boite=boite,
                        chocolat=chocolat,
                        defaults={'quantite': 0}  # Valeur par défaut pour quantite
                    )

                    # Met à jour la quantité de chocolat s'il est déjà présent
                    if not created:
                        boite_chocolat.quantite += quantite
                        boite_chocolat.save()

                return JsonResponse({'message': 'Boîte enregistrée avec succès!'})

            except Boite.DoesNotExist:
                return JsonResponse({'error': 'La boîte sélectionnée n\'existe pas.'}, status=404)

            except Chocolat.DoesNotExist:
                return JsonResponse({'error': 'Certains chocolats sélectionnés n\'existent pas.'}, status=404)

            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)

        else:
            return JsonResponse({'error': 'Données incomplètes ou incorrectes.'}, status=400)

    else:
        return JsonResponse({'error': 'Méthode non autorisée.'}, status=405)