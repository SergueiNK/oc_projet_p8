from django.db import models
# module gettext_lazy for traduction
from django.utils.translation import gettext_lazy as _
# Create your models here.
from django.contrib.auth.models import User


class Category(models.Model):
    """Model category, related to product """
    category_name = models.CharField(
        _("category name"),
        unique=True, max_length=500)

    def __str__(self):
        return (f"{self.category_name}"
                )


class Product(models.Model):
    """Model related to products"""
    code_product = models.CharField(
        "code of product",
        unique=True, max_length=500)
    product_name = models.CharField(
        "name of product", max_length=500)
    product_description = models.CharField(
        "description of product", max_length=500)
    url = models.CharField(
        "url of product", max_length=500)
    nutrition_grade = models.CharField(
        "nutrition grade of product", max_length=500)
    individual_image_url = models.URLField()
    list_image_url = models.URLField()
    image_nutrition_url = models.URLField()
    category_fk = models.ForeignKey(
        Category, on_delete=models.PROTECT, default="0")

    def __str__(self):
        """Return transform object into the string"""
        return (f"{self.code_product}"
                f"{self.product_name}"
                f"{self.product_description}"
                f"{self.url}"
                f"{self.nutrition_grade}"
                f"{self.individual_image_url}"
                f"{self.list_image_url}"
                f"{self.image_nutrition_url}"
                f"{self.category_fk}"
                )


class Favorite(models.Model):
    """Model related to saved favorite product and user corresponding"""
    product_fk = models.ForeignKey(
        Product, on_delete=models.PROTECT, default="0")
    user_fk = models.ForeignKey(
        User, on_delete=models.PROTECT, default="0")

    class Meta:
        unique_together = ['product_fk', 'user_fk']

        def __str__(self):
            """Return transform object into the string"""
            return (f"{self.product_fk}"
                    f"{self.user_fk}"
                    )
