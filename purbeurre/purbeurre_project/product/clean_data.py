#!/usr/bin/python3.9
# -*- coding:utf-8 -*-
from load_data import api_get_products 


def verify_product(product):
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


def get_verify_product():
    extract_product=[]
    for product in api_get_products():
        if verify_product(product):
            extract_product.append(product)
            print(extract_product)

if __name__ == "__main__":
    try:
        get_verify_product()
        print("Récuperation et nettoyage de data OK")
    except Exception as e:
        print(e)