from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User



class HomeTestCase(TestCase):

    def test_home_page_200(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)