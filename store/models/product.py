from django.db import models
from .category import Category


class Products(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    # price-gros = models.IntegerField(default=0)
    # price-intermediaire = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, default="", blank=True, null=True)
    image = models.ImageField(upload_to="uploads/products/",null=True)
    image2 = models.ImageField(upload_to="uploads/products/",null=True)
    image3 = models.ImageField(upload_to="uploads/products/",null=True)
    image4 = models.ImageField(upload_to="uploads/products/",null=True)
    image5 = models.ImageField(upload_to="uploads/products/",null=True)
    deleted = models.BooleanField(default=False)

    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter(id__in=ids, deleted=False)

    @staticmethod
    def get_all_products():
        return Products.objects.filter(deleted=False)

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Products.objects.filter(category=category_id, deleted=False)
        else:
            return Products.get_all_products()
