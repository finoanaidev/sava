from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from store.models.product import Products

def Detail(request, id):
    products=Products.objects.filter(id=id)
    context={'products':products}

    return render(request,"detail.html",context)
