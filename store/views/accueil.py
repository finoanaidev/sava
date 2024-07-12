from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.utils.translation import gettext as _
from django.utils.translation import activate


def Accueil(request):
    # Activer la langue sélectionnée (si stockée en session par exemple)
    if 'django_language' in request.session:
        activate(request.session['django_language'])
    
    # Charger le template
    template = 'accueil.html'
    
    # Contexte avec des exemples de messages traduits
    context = {
        'welcome_message': _('Welcome to our website!'),
        'about_message': _('Learn more about us.'),
        # Ajoutez d'autres variables contextuelles selon vos besoins
    }
    
    # Rendre le template avec le contexte traduit
    return render(request, template, context)
