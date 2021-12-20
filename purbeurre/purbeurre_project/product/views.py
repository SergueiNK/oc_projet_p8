from django.shortcuts import render, redirect
from product.models import Product, Favorite
from django.contrib.auth.models import User
from django.contrib import messages



def product(request):
        """ Given a user input request product after retrieve that object from database. Select 
        it categoty and give in templates the products substitute with the same category type """

        if 'user_product_request' in request.GET:
            # User input
            user_request = request.GET['user_product_request']
            # User input normalization
            user_request =str(user_request).lower().capitalize()

            # Getting object that contain the name of user input
            product = Product.objects.filter(product_name__contains = user_request).first()
            
            if product is not None:
                # Getting the substitutes that have the same category that user request input, have better nutriscore.
                # Ordered by nutriscore and display is limited to 18 products.
                substitut = Product.objects.filter(category_fk = product.category_fk, nutrition_grade__lt= product.nutrition_grade).order_by("nutrition_grade")[:18]

                # Dict that is an charge with data for substitutes products and original user input product
                context = {"all_products": substitut, "product_request": product}
                return render(request, 'product/product.html', context )
            else:
                # In case of not existing product send the error message
                messages.error(request, 'Veuillez refaire la recherche')    
                return redirect("/")
    


def product_detail(request, id):
    """Product detail that display the detail information from selected substitut product"""
    # Getting informations from selected product
    product_data = Product.objects.get(id = id)
    
    return render(request, 'product/product_detail.html', {'product_data': product_data})

def save_favorite(request):
    """ Save favorite is able to take selected product and ssave him into Favorite table from database """
    # Getting actual connected user object 
    user = User.objects.get(id = request.user.id)
    # Getting the product id choiced by user
    product_id = request.POST.get('substitute_id')
    # Getting the related product objects
    product = Product.objects.get(pk=product_id)
    # Saved the object related substitute product and user id in Favorite table
    Favorite.objects.create(user_fk=user, product_fk=product)
    return redirect('users:fav')
