from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

def Register(request):
    template = loader.get_template('register.html')
    context = {}
    return HttpResponse(template.render(context, request))