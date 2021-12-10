#!/usr/bin/python3.9
# -*- coding:utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from product.models import Category, Product, Favorite
import requests
import json


class Command(BaseCommand):


    def __init__(self):
        self.url_request = 'https://fr.openfoodfacts.org/cgi/search.pl'
        self.products_params = {
            "action": "process",
            "sort_by": "unique_scans_n",
            "page_size": 500,
            "json": 1,
            "page": 1,
            "fields": "pnns_groups_1,product_name,generic_name_fr,"
                    "code,url,nutrition_grade_fr,image_url,image_nutrition_url,image_small_url"
        }


    def api_get_products(self):
        """Launch the API fetch"""
        try:
            request_response = requests.get(self.url_request, self.products_params)
            #print(request_response)
            print(request_response.url)
            response = json.loads(request_response.text)
            #print(response)
            return response.get('products')
        except Exception as e:
            raise e


    def verify_product(self, product):
        """ Check and sort the API before insert in tables """
        if product.get('product_name') \
                and product.get('product_name') != 'unknown' \
                and product.get('product_name') != '' \
                and product.get('generic_name_fr') \
                and product.get('generic_name_fr') != 'unknown' \
                and product.get('generic_name_fr') != '' \
                and product.get('code') \
                and product.get('code') != 'unknown' \
                and product.get('code') != '' \
                and product.get('url') \
                and product.get('url') != 'unknown' \
                and product.get('url') != '' \
                and product.get('nutrition_grade_fr') \
                and product.get('nutrition_grade_fr') != 'unknown' \
                and product.get('nutrition_grade_fr') != '' \
                and product.get('pnns_groups_1') \
                and product.get('pnns_groups_1') != 'unknown' \
                and product.get('pnns_groups_1') != '' \
                and product.get('code') \
                and product.get('code') != 'unknown' \
                and product.get('code') != '' \
                and product.get('image_url') \
                and product.get('image_url') != 'unknown' \
                and product.get('image_url') != '' \
                and product.get('image_nutrition_url') \
                and product.get('image_nutrition_url') != 'unknown' \
                and product.get('image_nutrition_url') != '' \
                and product.get('image_small_url') \
                and product.get('image_small_url') != 'unknown' \
                and product.get('image_small_url') != '' :
            return True
        else:
            return False

    #def get_verify_product(self):
        #extract_product={}
        #for product in self.api_get_products():
            #if self.verify_product(product):
                #extract_product.update(product)
                #print(extract_product)


    def handle(self, *args, **options):
        extract_product={}
        for product in self.api_get_products():
            if self.verify_product(product):
                try:
                    extract_product.update(product)
                    #print(extract_product)
                    #print(type(extract_product.get('pnns_groups_1')))
                    #prémiere étape permet de créer l'objet dans la base de donnée
                    #prémiere étape permet de vérifier si le pnns groupe existe 
                    try:
                        category_data = Category.objects.get(category_name = extract_product.get('pnns_groups_1'))

                    except Exception as e:
                        category_data = Category.objects.create(category_name = extract_product.get('pnns_groups_1'))

                    #deuxiéme étape permet de selectionner cette objét
                        #category_results = Category.objects.filter(category_name = extract_product.get('pnns_groups_1'))
                    
                    product_data = Product.objects.create(
                        code_product = extract_product.get('code'),
                        product_name = extract_product.get('product_name'),
                        product_description = extract_product.get('generic_name_fr'),
                        url = extract_product.get('url'),
                        nutrition_grade = extract_product.get('nutrition_grade_fr'),
                        individual_image_url = extract_product.get('image_url'),
                        list_image_url = extract_product.get('image_small_url'),
                        image_nutrition_url = extract_product.get('image_nutrition_url'),
                        category_fk = category_data,
                    )
                    product_data.save() 
                    print(product_data)       

                except Exception as e:
                    print(e)
                    #print(product_data)
                    #print(product_data)
                    CommandError('Product does not exist')

    #def insert_data(self, product):
        #for product in handle():
            #pass



