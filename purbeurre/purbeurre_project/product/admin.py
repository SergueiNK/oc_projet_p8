from django.contrib import admin
from .models import Product

# Pour pouvoir modifier les données de register depuis Product
# Dépuis admin ça permet d'ajouter du site ça permet de faire les modifications
admin.site.register(Product)
# Register your models here.
