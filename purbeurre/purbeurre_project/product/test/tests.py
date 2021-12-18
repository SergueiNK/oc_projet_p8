from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from product.models import Category, Product, Favorite


class ProductViewsTests(TestCase):

    def setUp(self):
        self.user = User()
        self.product = Product()
        self.category = Category.objects.create(category_name = 'Sugary snack')
        self.favorite = Favorite.objects.create(
            product_fk = self.product,
            user_fk = self.user
        )
        User.objects.create(
            username = 'user4',
            password = 'password',
            email = 'email',
            id = '4'
        )
        Product.objects.create(
            code_product = '7622210449283 ',
            product_name = 'Prince Chocolat',
            product_description = 'Biscuits au chocolat',
            url = 'https://fr.openfoodfacts...',
            nutrition_grade = 'c',
            individual_image_url = 'https://images.openfoodfaacts...',
            list_image_url = 'https://images.openfoodfaacts...',
            image_nutrition_url = 'https://images.openfoodfaacts...',
            category_fk = self.category,
            id = '3'
        )
        Product.objects.create(
            code_product = '7622210449273 ',
            product_name = 'Nutella',
            product_description = 'Biscuits au chocolat',
            url = 'https://fr.openfoodfacts...',
            nutrition_grade = 'a',
            individual_image_url = 'https://images.openfoodfaacts...',
            list_image_url = 'https://images.openfoodfaacts...',
            image_nutrition_url = 'https://images.openfoodfaacts...',
            category_fk = self.category,
            id = '4'
        )
        Product.objects.create(
            code_product = '7622210449873 ',
            product_name = 'Pomme',
            product_description = 'Biscuits au chocolat',
            url = 'https://fr.openfoodfacts...',
            nutrition_grade = 'b',
            individual_image_url = 'https://images.openfoodfaacts...',
            list_image_url = 'https://images.openfoodfaacts...',
            image_nutrition_url = 'https://images.openfoodfaacts...',
            category_fk = self.category,
            id = '5'
        )   

    def test_substitute_page(self):

        product_name = 'Prince Chocolat'
        data = {'user_product_request': product_name}
        url = reverse ('products:product')
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, 302)    


    def test_not_existing_substitute_page(self):
        try:
            data = {'user_request': 'NOTHING',}
            url = reverse('products:product')
            response = self.client.get(url, data)
            self.assertEqual(response.status_code, 302)
        except:
            pass

    def test_detail_page(self):
        product_id = '5'
        url = reverse('products:detail', args=(product_id))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_save_favorite(self):

        self.client.force_login(self.user)
        user_data = self.user
        product_id = '5'
        data = {'substitute_id': product_id, 'user': user_data}
        print(data)
        url = reverse('products:save')
        print(url)
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, 200)