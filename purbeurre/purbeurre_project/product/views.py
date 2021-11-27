from django.shortcuts import render
from product.models import Product
from product.models import Category
from django.db.models import Q
import requests


def product(request):
    all_products = {}
    if 'user_product_request' in request.GET:
        
        user_request = request.GET['user_product_request']
        user_request =str(user_request)
        print(user_request)
        
        # On fait sortir la category qui contient le nom du produit (étape1), first() to convert the object to string
        user_request_category = Category.objects.filter(product__product_name__contains = user_request).first()
        user_request_category = str(user_request_category)
        print(user_request_category)
        #products = Product.objects.all()
        products_by_category = Product.objects.filter(category_fk__category_name = user_request_category)
        # Selection du produit en fonction de son grade nutriscore affichage est limité à 4 [:4]. 
        products_by_nutriscore = products_by_category.filter(Q(nutrition_grade__contains = "a") | Q(nutrition_grade__contains = "b"))[:10]
        print(products_by_nutriscore)

        return render(request, 'product/product.html', {"all_products":
        products_by_nutriscore})


def product_detail(request, id):
    product_data = Product.objects.get(id = id)
    print(product_data)
    
    return render(request, 'product/product_detail.html', {'product_data': product_data})

def save_product():
    pass

    #return render (request, 'product/saved_product.html', {})

