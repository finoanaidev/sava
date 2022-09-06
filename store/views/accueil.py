from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader


def Accueil(request):
    template = loader.get_template("accueil.html")
    context = {}
    return HttpResponse(template.render(context, request))
