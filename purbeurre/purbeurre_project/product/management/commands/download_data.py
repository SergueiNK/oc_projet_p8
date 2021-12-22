#!/usr/bin/python3.9
# -*- coding:utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from product.models import Category, Product, Favorite
import requests
import json


class Command(BaseCommand):
    """From API openfoodfacts import and clean data. Insert that data 
    in the the tables of software
    """
    def __init__(self):
        """Init the parameters needed for request the API"""
        self.url_request = 'https://fr.openfoodfacts.org/cgi/search.pl'
        self.products_params = {
            "action": "process",
            "sort_by": "unique_scans_n",
            "page_size": 3000,
            "json": 1,
            "page": 1,
            "fields": "pnns_groups_1,product_name,generic_name_fr,"
                    "code,url,nutrition_grade_fr,image_url,image_nutrition_url,image_front_thumb_url"
        }


    def api_get_products(self):
        """Launch the API fetch"""
        try:
            request_response = requests.get(self.url_request, self.products_params)
            response = json.loads(request_response.text)
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
                and product.get('image_front_thumb_url') \
                and product.get('image_front_thumb_url') != 'unknown' \
                and product.get('image_front_thumb_url') != '' :
            return True
        else:
            return False

    def handle(self, *args, **options):
        """Insert clean data into the tables of database"""
        extract_product={}
        for product in self.api_get_products():
            # Check if the select product is correct
            if self.verify_product(product):
                try:
                    # Append the product into the dictionnary
                    extract_product.update(product)
                    try:
                        # Check if the object of category is already exist in database
                        category_data = Category.objects.get(category_name = extract_product.get('pnns_groups_1'))

                    except Exception as e:
                        # If the object of the category doesn't exist, create it
                        category_data = Category.objects.create(category_name = extract_product.get('pnns_groups_1'))

                    
                    # Create the object of product and insert data in database
                    product_data = Product.objects.create(
                        code_product = extract_product.get('code'),
                        product_name = extract_product.get('product_name'),
                        product_description = extract_product.get('generic_name_fr'),
                        url = extract_product.get('url'),
                        nutrition_grade = extract_product.get('nutrition_grade_fr'),
                        individual_image_url = extract_product.get('image_url'),
                        list_image_url = extract_product.get('image_front_thumb_url'),
                        image_nutrition_url = extract_product.get('image_nutrition_url'),
                        category_fk = category_data,
                    )
                    product_data.save() 
                    print(product_data)       

                except Exception as e:
                    print(e)
                    CommandError('Product does not exist')




