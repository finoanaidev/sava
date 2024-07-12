from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Products
from store.models.orders import Order
from store.middlewares.auth import auth_middleware
from django.utils.translation import gettext as _
from django.utils.translation import activate

class OrderView(View):
    def get(self, request):
        # Activer la langue sélectionnée (si stockée en session par exemple)
        if 'django_language' in request.session:
            activate(request.session['django_language'])
        customer = request.session.get("customer")
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request, "orders.html", {"orders": orders})
