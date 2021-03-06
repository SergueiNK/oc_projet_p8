from django.test import TestCase
from django.urls import reverse


class PageTestCase(TestCase):

    def test_home_page_200(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_legal_page_200(self):
        response = self.client.get(reverse('legal'))
        self.assertEqual(response.status_code, 200)
