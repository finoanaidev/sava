from django.shortcuts import render, get_object_or_404
from store.models.chocolat import Chocolat, Boite, BoiteChocolat
from store.models.customer import Customer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def simulation_menu(request):
    chocolats = Chocolat.objects.all()
    boites = Boite.objects.all()

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            selected_chocolats_data = data.get('selected_chocolats', [])
            box_size = data.get('box_size')
            client_id = data.get('client_id')
            client = get_object_or_404(Customer, id=client_id)

            if selected_chocolats_data and box_size:
                prix = 30000 if box_size == '150g' else 60000
                
                # Vérifiez si une boîte appropriée existe déjà
                existing_box = Boite.objects.filter(type=box_size, prix=prix).first()
            
                if existing_box:
                    # Supprimer tous les chocolats existants dans la boîte
                    existing_box.boitechocolat_set.all().delete()
                    
                    # Utiliser la boîte existante
                    boite_chocolat = existing_box.creer_boite_chocolat(client)
                else:
                    # Créer une nouvelle boîte si aucune n'existe
                    new_box = Boite.objects.create(type=box_size, prix=prix, nom=f"Boîte de {box_size}")
                    boite_chocolat = new_box.creer_boite_chocolat(client)

                # Ajouter les chocolats sélectionnés à la boîte_chocolat
                for chocolate_data in selected_chocolats_data:
                    chocolat_id = chocolate_data['chocolat_id']
                    chocolat = get_object_or_404(Chocolat, id=chocolat_id)
                    boite_chocolat.ajouter_chocolat(chocolat)

                return JsonResponse({'success': True, 'redirect_url': 'simulation'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    context = {
        'chocolats': chocolats,
        'boites': boites,
    }
    return render(request, 'simulation_menu.html', context)
