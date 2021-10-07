#!/usr/bin/python3.9
# -*- coding:utf-8 -*-

import requests
import json

url_request = 'https://fr.openfoodfacts.org/cgi/search.pl'
products_params = {
    "action": "process",
    "sort_by": "unique_scans_n",
    "page_size": 500,
    "json": 1,
    "page": 1,
    "fields": "pnns_groups_1,generic_name_fr,"
              "code,url,nutrition_grade_fr,image_url,image_nutrition_url"
}

# get API
def api_get_products():
    """Launch the API fetch"""
    try:
        request_response = requests.get(url_request, products_params)
        #print(request_response)
        #print(request_response.url)
        response = json.loads(request_response.text)
        #print(response)
        return response.get('products')
    except Exception as e:
        raise e


