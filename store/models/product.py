from django.db import models 
from .category import Category 
  
  
class Products(models.Model): 
    name = models.CharField(max_length=60) 
    price = models.IntegerField(default=0) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1) 
    description = models.CharField( 
        max_length=250, default='', blank=True, null=True) 
    image = models.ImageField(upload_to='uploads/products/', default='default.jpg') 
    image2 = models.ImageField(upload_to='uploads/products/', default='default.jpg') 
    image3 = models.ImageField(upload_to='uploads/products/', default='default.jpg') 
    image4 = models.ImageField(upload_to='uploads/products/', default='default.jpg') 
    image5 = models.ImageField(upload_to='uploads/products/', default='default.jpg') 
    video = models.FileField(upload_to='uploads/products/', null=True, blank=True, ) # Utilisez FileField pour les vidéos
    other_description = models.TextField(blank=True, null=True) # Ajoutez un champ pour d'autres descriptions
  
    @staticmethod
    def get_products_by_id(ids): 
        return Products.objects.filter(id__in=ids) 
  
    @staticmethod
    def get_all_products(): 
        return Products.objects.all() 
  
    @staticmethod
    def get_all_products_by_categoryid(category_id): 
        if category_id: 
            return Products.objects.filter(category=category_id) 
        else: 
            return Products.get_all_products() 
        
    def has_video(self):
        return bool(self.video)