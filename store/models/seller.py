# models/seller.py

from django.db import models
from django.contrib.auth.models import User

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name  # Renvoie le nom de l'entreprise comme représentation de l'objet Seller

