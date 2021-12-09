from django.shortcuts import render, redirect
from product.models import Product, Favorite
from product.models import Category
from django.contrib.auth.models import User
from django.db.models import Q
import requests


def product(request):
    all_products = {}
    if 'user_product_request' in request.GET:
        
        user_request = request.GET['user_product_request']
        user_request =str(user_request)
        #print(user_request)
        
        # On fait sortir la category qui contient le nom du produit (étape1), first() to convert the object to string
        #user_request_category = Category.objects.filter(product__product_name__contains = user_request).first()
        #user_request_category = str(user_request_category)
        #print(user_request_category)
        #products = Product.objects.all()
        #products_by_category = Product.objects.filter(category_fk__category_name = user_request_category)
        # Selection du produit en fonction de son grade nutriscore affichage est limité à 4 [:4]. 
        #products_by_nutriscore = products_by_category.filter(Q(nutrition_grade__contains = "a") | Q(nutrition_grade__contains = "b"))[:10]
        # A tester car non encore fonctionnel
        #user_request_product = products_by_nutriscore.filter(product_name__contains = user_request)
        #print(products_by_nutriscore)
        product = Product.objects.filter(product_name__contains = user_request).first()
        substitut = Product.objects.filter(category_fk = product.category_fk, nutrition_grade__lt= product.nutrition_grade)
        print(product.nutrition_grade)
        

        return render(request, 'product/product.html', {"all_products":
        substitut})


def product_detail(request, id):
    product_data = Product.objects.get(id = id)
    #print(product_data)
    
    return render(request, 'product/product_detail.html', {'product_data': product_data})

def save_favorite(request):
    # Faire l'affichage de model de tous les favoris sauvegardés
    #current_user = request.user.id
    #print(current_user)
    #product_id = Product.objects.get(id=id)
    #user = User.objects.get(id=current_user)
    #user = User.objects.get(id=request.user.id)
    #product = Product.objects.get(id=product_id.id)
    #product = Product.objects.get(id=7001)
    #save_product = Favorite(user_fk=user, product_fk=product)
    #print(save_product)
    #save_product.save()
    user = User.objects.get(id = request.user.id)
    product_id = request.POST.get("substitute_id")
    product = Product.objects.get(pk=product_id)
    #print(user)
    #print(product_id)
    #save_product = Favorite(user_fk=user, product_fk=product)
    #save_product.save()
    Favorite.objects.create(user_fk=user, product_fk=product)
 
    return redirect ('users:fav')
