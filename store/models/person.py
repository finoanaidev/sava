from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)
    commercial_name = models.CharField(max_length=100)
    address = models.TextField()
    phone_siege = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    num_fiscal = models.CharField(max_length=10)
    num_stat = models.CharField(max_length=10)
    num_cin = models.CharField(max_length=10)
    nom_pers = models.CharField(max_length=100)
    phone_pers = models.CharField(max_length=10)
    email_pers = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    objects=models.Manager()

   
