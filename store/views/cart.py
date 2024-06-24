
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Products
from django.utils.translation import gettext as _
from django.utils.translation import activate

class Cart(View):
    def get(self, request):
        # Activer la langue sélectionnée (si stockée en session par exemple)
        if 'django_language' in request.session:
            activate(request.session['django_language'])
            
        ids = list(request.session.get("cart").keys())
        products = Products.get_products_by_id(ids)
        print(products)
        return render(request, "cart.html", {"products": products})
