from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

def Faq(request):
    template = loader.get_template('faq.html')
    context = {}
    return HttpResponse(template.render(context, request))