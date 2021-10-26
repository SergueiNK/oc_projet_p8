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
            "page_size": 5,
            "json": 1,
            "page": 1,
            "fields": "pnns_groups_1,generic_name_fr,"
                    "code,url,nutrition_grade_fr,image_url,image_nutrition_url"
        }


    def api_get_products(self):
        """Launch the API fetch"""
        try:
            request_response = requests.get(self.url_request, self.products_params)
            #print(request_response)
            #print(request_response.url)
            response = json.loads(request_response.text)
            #print(response)
            return response.get('products')
        except Exception as e:
            raise e


    def verify_product(self, product):
        """ Check and sort the API before insert in tables """
        if product.get('generic_name_fr') \
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
                and product.get('image_nutrition_url') != '' :
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
                    print(extract_product)
                    #print(type(extract_product.get('pnns_groups_1')))
                    #category_data = Category.objects.create(category_name = extract_product.get('pnns_groups_1'))
                    category_results = Category.objects.filter(category_name = extract_product.get('pnns_groups_1'))
                    
                    if category_results.exists():

                        product_data = Product(
                            code_product = extract_product.get('code'),
                            product_name = extract_product.get('generic_name_fr'),
                            url = extract_product.get('url'),
                            nutrition_grade = extract_product.get('nutrition_grade_fr'),
                            image_url = extract_product.get('image_url'),
                            image_nutrition_url = extract_product.get('image_nutrition_url'),
                            category_fk = category_results[0],
                        )
                        product_data.save()                  
                except Exception as e:
                    print(e)
                    CommandError('Product does not exist')

    #def insert_data(self, product):
        #for product in handle():
            #pass



