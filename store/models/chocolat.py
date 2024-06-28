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
    chocolats = models.ManyToManyField(Chocolat, related_name='boites', blank=True)
    quantite = models.PositiveIntegerField(default=1)

    def nombre_chocolats(self):
        return 9 if self.type == '150g' else 16

    def ajouter_chocolat(self, chocolat):
        if self.chocolats.count() < self.nombre_chocolats():
            self.chocolats.add(chocolat)
            self.save()

    def retirer_chocolat(self, chocolat):
        self.chocolats.remove(chocolat)
        self.save()

    def vider_boite(self):
        self.chocolats.clear()
        self.save()

    def creer_boite_chocolat(self, client):
        # Créer une instance de BoiteChocolat pour enregistrer les détails de cette boîte
        boite_chocolat = BoiteChocolat.objects.create(
            boite=self,
            prix=self.prix,
            nombre_chocolats=self.nombre_chocolats(),
            chocolats=list(self.chocolats.all()),
            client=client
        )
        return boite_chocolat

class BoiteChocolat(models.Model):
    boite = models.ForeignKey(Boite, on_delete=models.CASCADE, related_name='boite_chocolats')
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    nombre_chocolats = models.PositiveIntegerField()
    chocolats = models.ManyToManyField(Chocolat, related_name='boite_chocolats')
    client = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='boite_chocolats')

    def __str__(self):
        return f"{self.boite.nom} - {self.prix} Ar - {self.nombre_chocolats} chocolats"
