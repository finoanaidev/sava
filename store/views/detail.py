from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from store.models.product import Products
from django.utils.translation import gettext as _
from django.utils.translation import activate

def Detail(request, id):
    # Activer la langue sélectionnée (si stockée en session par exemple)
    if 'django_language' in request.session:
        activate(request.session['django_language'])
        
    products=Products.objects.filter(id=id)
    context={'products':products}

    return render(request,"detail.html",context)
