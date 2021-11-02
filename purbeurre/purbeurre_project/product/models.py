from django.db import models
# module gettext_lazy for traduction
from django.utils.translation import gettext_lazy as _
# Create your models here.
from django.contrib.auth.models import User


class Category(models.Model):

    category_name = models.CharField(_("category name"), unique=True, max_length=500)
    def __str__(self):
        return  (f"{self.category_name}"
                )

                
class Product(models.Model):

    code_product = models.CharField("code of product", unique=True, max_length=500)
    product_name = models.CharField("name of product", max_length=500)
    url = models.CharField("url of product", max_length=500)
    nutrition_grade = models.CharField("nutrition grade of product", max_length=500)
    image_url = models.URLField()
    image_nutrition_url = models.URLField()
    category_fk = models.ForeignKey(Category, on_delete=models.PROTECT, default="0")
    
    def __str__(self):
        
        return (f"{self.code_product}"
                f"{self.product_name}"
                f"{self.url}"
                f"{self.nutrition_grade}"
                f"{self.image_url}"
                f"{self.image_nutrition_url}"
                f"{self.category_fk}"
                )


class Favorite(models.Model):
    #id_favorites = models.AutoField.primary_key("id_favorites", primary_key=True)
    # default="0" Django a besoin de data pour créer les tables
    product_fk = models.ForeignKey(Product, on_delete=models.PROTECT, default="0")
    user_fk = models.ForeignKey(User, on_delete=models.PROTECT, default="0")
    class Meta:
        #Il aura jamais deux mêmes entrées
        unique_together = ['product_fk', 'user_fk']

    