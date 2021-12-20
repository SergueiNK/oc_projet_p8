from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from product.models import Category, Product, Favorite


class ProductViewsTests(TestCase):

    def setUp(self):
        """ Create data for virtual database inside tables: category, user, product, favorite"""    
        self.user = User.objects.create(
            username = 'user4',
            password = 'password',
            email = 'email',
            id = '4'
        )

        self.category = Category.objects.create(category_name = 'Sugary snack')

        self.product = Product.objects.create(
            code_product = '80176800',
            product_name = 'Nutella',
            product_description = 'Pate à tartiner aux noisettes et chocolat',
            url = 'https://fr.openfoodfacts...',
            nutrition_grade = 'e',
            individual_image_url = 'https://images.openfoodfaacts...',
            list_image_url = 'https://images.openfoodfaacts...',
            image_nutrition_url = 'https://images.openfoodfaacts...',
            category_fk = self.category,
            id = '3'
        )

        self.product_sub = Product.objects.create(
            code_product = '3608580823452',
            product_name = 'Abricot intense - Confiture moins sucrée',
            product_description = 'Confiture extra d\'abricots allégée en sucres ',
            url = 'https://fr.openfoodfacts...',
            nutrition_grade = 'c',
            individual_image_url = 'https://images.openfoodfaacts...',
            list_image_url = 'https://images.openfoodfaacts...',
            image_nutrition_url = 'https://images.openfoodfaacts...',
            category_fk = self.category,
            id = '4'
        )
        self.sub_product = Product.objects.create
        #print(self.product)
        #self.favorite = Favorite.objects.create(
            #product_fk = self.product,
            #user_fk = self.user
        #)
        self.favorite = Favorite.objects.create(user_fk=self.user, product_fk=self.product)
        #print(self.favorite.user_fk)   
        #print(self.favorite.product_fk)  

    def test_substitute_page(self):
        """test substitute page"""
        product_name = 'Nutella'
        data = {'user_product_request': product_name}
        url = reverse ('products:product')
        response = self.client.get(url, data)
        #print(response)
        self.assertEqual(response.status_code, 200)

    #def test_contain_return_context(self):
        #product_name_incomplete = 'nut'
        #data = {'user_product_request': product_name_incomplete}
        #url = reverse ('products:product')
        #response = self.client.get(url, data)
        #print(response)
        #product_returned = response.data['product'][0].name
        #self.assertEqual(product_returned, 'Nutella')       


    def test_not_existing_substitute_page(self):
        """Test if input user request is wrong"""
        try:
            data = {'user_request': 'NOTHING',}
            url = reverse('products:product')
            response = self.client.get(url, data)
            self.assertEqual(response.status_code, 302)
        except:
            pass

    def test_detail_page(self):
        """Test detail page"""
        product_id = '3'
        url = reverse('products:detail', args=(product_id))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_save_favorite(self):
        """Test substitute product save"""
        self.client.force_login(self.user)       
        product_id = '3'
        data = {'substitute_id': product_id}
        print(data)
        url = reverse('products:save')
        #print(url)
        response = self.client.get(url, data)
        #print(response)
        
        self.assertEqual(response.status_code, 302)
        
        