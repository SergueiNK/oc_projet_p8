from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from product.models import Category, Product, Favorite


class PageTestCase(TestCase):

    def setUp(self):
        self.user = User()
        self.product = Product()
        self.category = Category.objects.create(category_name = 'Sugary snack')
        User.objects.create (
            id = '4',
            username = 'blabla4'
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
        """test substitute page"""
        product_name = str('Prince Chocolat')
        response = self.client.get(reverse('products:product'),
                        {'user_request': product_name})
        self.assertEqual(response.status_code, 200)    

    def test_not_existing_substitute_page(self):
        """test no substitute page"""
        try:
            response = self.client.get(reverse('products:product'), {
                'user_request': 'NOTHING',
            })
            self.assertEqual(response.status_code, 404)
        except:
            pass

    def test_detail_page(self):
        product_id = '5'
        response = self.client.get(reverse('products:detail', args=(product_id)))
        self.assertEqual(response.status_code, 200)

    def test_save_favorite(self):
        user_id = str('4')
        product_id = str('5')
        response = self.client.get(reverse('products:save', {'user': user_id, 'product_id':product_id}))
        self.assertEqual(response.status_code, 200)