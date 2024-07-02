from django.db import models
from .customer import Customer  # Assuming Customer model is in the same directory

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

    def nombre_chocolats(self):
        return 9 if self.type == '150g' else 16

    def creer_boite_chocolat(self, client, chocolat=None):
        boite_chocolat = BoiteChocolat.objects.create(
            boite=self,
            prix=self.prix,
            client=client,
            nombre_chocolats=self.nombre_chocolats()
        )

        if chocolat:
            for _ in range(self.nombre_chocolats()):
                boite_chocolat.chocolats.add(chocolat)

        return boite_chocolat

    def __str__(self):
        return self.nom

class BoiteChocolat(models.Model):
    boite = models.ForeignKey(Boite, on_delete=models.CASCADE, related_name='boite_chocolats')
    prix = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    chocolats = models.ManyToManyField(Chocolat, related_name='boite_chocolats', default=None)
    client = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='boite_chocolats')
    nombre_chocolats = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.boite.nom} - {self.prix} Ar - {self.nombre_chocolats} chocolats"

    def ajouter_chocolat(self, chocolat):
        if self.chocolats.count() < self.nombre_chocolats:
            self.chocolats.add(chocolat)

    def retirer_chocolat(self, chocolat):
        self.chocolats.remove(chocolat)

    def vider_boite(self):
        self.chocolats.clear()
