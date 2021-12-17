from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from product.models import Category, Product, Favorite

class UserViewsTests(TestCase):

    def setUp(self):
         
        self.category = Category.objects.create(category_name = 'Sugary snack')

        self.product = Product.objects.create(
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
        self.user = User.objects.create(
            username = 'user4',
            password = 'password',
            email = 'email',
            id = '4'
        )
        self.favorite = Favorite.objects.create(
            product_fk = self.product,
            user_fk = self.user
        )

    def test_user_page(self):
        url = reverse('users:user')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_user_logout(self):
        self.client.force_login(self.user)
        url = reverse('users:logout')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_getUser_if_logged(self):
        self.client.force_login(self.user)
        url = reverse('users:userDetails')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_getUser_if_not_logged(self):
        url = reverse('users:userDetails')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)            

    def test_registerPage_page(self):
        data = { 
            'username': 'user1',
            'email': 'user1@gmail.com',
            'password1': 'Tundra8996!*',
            'password1': 'Tundra8996!*'
        }
        url = reverse ('users:register')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200) 

    def test_loginPage_page(self):
        self.client.force_login(self.user)

        url = reverse('users:login')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)

    def test_getFavorite_page(self):    
        url = reverse('users:fav')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)    

                 