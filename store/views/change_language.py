from django.shortcuts import redirect
from django.utils.translation import activate

def change_language(request, language_code):
    # Active la langue sélectionnée
    activate(language_code)

        # Stocke la langue sélectionnée dans la session si nécessaire
    request.session['django_language'] = language_code
    
    # Redirige l'utilisateur vers la page précédente
    return redirect(request.META.get('HTTP_REFERER', '/'))
