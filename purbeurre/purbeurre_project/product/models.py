from django.db import models

# Create your models here.

class Product(models.Model):
    #code_products = models.IntegerField.primary_key("code of product", primary_key=True)
    pnns_groups_1 = models.CharField("category", max_length=500)
    generic_name_fr = models.CharField("name of product", max_length=100)
    url = models.CharField("url of product", max_length=100)
    nutrition_grade_fr = models.CharField("nutrition grade of product", max_length=100)
    image_url = models.URLField()
    image_nutrition_url = models.URLField()
    
    def __str__(self):
        # Pour transformer et retourner l'objet de façan lisible
        return (f"{self.pnns_groups_1}"
                f"{self.generic_name_fr}"
                f"{self.url}"
                f"{self.image_url}"
                f"{self.image_nutrition_url}"
                )


class Categories(models.Model):
    #code_categories = models.IntegerField.primary_key("code of category", primary_key=True)
    pnns_groups_1 = models.CharField("category", max_length=500)
    #Clés étrangere est sur le code_products.Product en cas de son suppression sauvegarder le model
    code_products_fk = models.ForeignKey(Product, on_delete=models.PROTECT)

    def __str__(self):
        return  (f"{self.pnns_groups_1}"
                )


class Favorites(models.Model):
    #id_favorites = models.AutoField.primary_key("id_favorites", primary_key=True)
    code_products_fk = models.ForeignKey(Product, on_delete=models.PROTECT)

    