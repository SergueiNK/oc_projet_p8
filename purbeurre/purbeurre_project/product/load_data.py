import request

url_request = 'https://fr.openfoodfacts.org/cgi/search.pl'
products_params = {
    "action": "process",
    "sort_by": "unique_scans_n",
    "page_size": 500,
    "json": 1,
    "page": 1,
    "fields": "pnns_groups_1,generic_name_fr,"
              "code,url,nutrition_grade_fr,stores"
}

def api_get_products():
    try:
        request_response = request.get(url_request, products_params)
        response = json.loads(request_response.txt)
        return response.get('products')
        print('products')
    except Exception as e:
        raise e

if __name__ == "__main__":
    try:
        create_database()
        print("Base de données créée")
    except Exception as e:
        print(e)