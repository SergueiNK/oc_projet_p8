from django.shortcuts import render, redirect
from product.models import Product, Favorite
from product.models import Category
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
import requests

from django.contrib import messages


def product(request):
     
        if 'user_product_request' in request.GET:
        
            user_request = request.GET['user_product_request']
            user_request =str(user_request).lower().capitalize()
     
            product = Product.objects.filter(product_name__contains = user_request).first()
            print(product)
            if product is not None:
                substitut = Product.objects.filter(category_fk = product.category_fk, nutrition_grade__lt= product.nutrition_grade).order_by("nutrition_grade")[:18]
            #print(product.nutrition_grade)
                context = {"all_products": substitut, "product_request": product}


                return render(request, 'product/product.html', context )
            else:
                messages.error(request, 'Veuillez refaire la recherche')    
                return redirect("/")
    


def product_detail(request, id):
    product_data = Product.objects.get(id = id)
    #print(product_data)
    
    return render(request, 'product/product_detail.html', {'product_data': product_data})

def save_favorite(request):
    # Faire l'affichage de model de tous les favoris sauvegardés
    #current_user = request.user.id
    #print(current_user)
  
    user = User.objects.get(id = request.user.id)
    print(user)
    product_id = request.POST.get('substitute_id')
    print(product_id)
    product = Product.objects.get(pk=product_id)
    print(product)
    Favorite.objects.create(user_fk=user, product_fk=product)
    return redirect ('users:fav')
