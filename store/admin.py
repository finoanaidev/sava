from django.contrib import admin
from .models.orders import Order
from .models.person import Person
from .models.vendeur import Vendeur
from .models.product import Products
from .models.category import Category
from .models.customer import Customer


class AdminProduct(admin.ModelAdmin):
    list_display = ["name", "price", "category"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


# Register your models here.
admin.site.register(Order)
admin.site.register(Person)
admin.site.register(Vendeur)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Products, AdminProduct)
