from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Products
from store.models.category import Category
from django.http import HttpResponse


def SearchPage(request):
    srh = request.GET["query"]
    product = Products.objects.filter(name__icontains=srh)
    params = {"product": product, "search": srh}
    return render(request, "SearchPage.html", params)


def SearchCategory(request):
    srh = request.GET["query"]
    category = Category.objects.filter(name__icontains=srh)
    params = {"category": category, "search": srh}
    return render(request, "SearchPage.html", params)
