from django.shortcuts import render
from product.models import Product
import requests

def product(request):
    all_products = {}
    if 'user_product_request' in request.GET:
        
        user_request = request.GET['user_product_request']
        user_request =str(user_request)
        print(user_request)
        
        all_products = Product.objects.filter(product_name = user_request)

        return render(request, 'product/product.html', {"all_products":
        all_products})


def product_detail(request):
    return render(request, 'product/product_detail.html')

