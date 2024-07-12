from django.db import models


class Vendeur(models.Model):
    id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    commercial_name = models.CharField(max_length=100)
    marque_deposer = models.CharField(max_length=100, null=True)
    marque_representer = models.CharField(max_length=100, null=True)
    address = models.TextField()
    phone_siege = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    num_fiscal = models.CharField(max_length=10)
    num_stat = models.CharField(max_length=10)
    num_cin = models.CharField(max_length=10)
    nom_pers = models.CharField(max_length=100)
    phone_pers = models.CharField(max_length=10)
    email_pers = models.CharField(max_length=100)
    liste_pays = models.CharField(max_length=100)
    liste_fournisseur = models.CharField(max_length=100)
    article_phare = models.CharField(max_length=100)
    secteur_activite = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    objects=models.Manager()

   
