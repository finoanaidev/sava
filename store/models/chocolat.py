# models.py

from django.db import models

class Chocolat(models.Model):
    nom = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chocolats/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.nom

class Boite(models.Model):
    TYPE_CHOICES = [
        ('150g', '150 g (9 chocolats)'),
        ('300g', '300 g (16 chocolats)'),
    ]

    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=4, choices=TYPE_CHOICES)
    chocolats = models.ManyToManyField(Chocolat, through='BoiteChocolat')

    def __str__(self):
        return self.nom

class BoiteChocolat(models.Model):
    boite = models.ForeignKey(Boite, on_delete=models.CASCADE)
    chocolat = models.ForeignKey(Chocolat, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=0)  # Permet de spécifier la quantité de chaque chocolat dans la boîte

    def __str__(self):
        return f"{self.boite.nom} - {self.chocolat.nom}"
