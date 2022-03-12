from django.test import TestCase
from django.urls import reverse


class IndexPageTest(TestCase):
    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


class SearchPageTest(TestCase):
    def test_search_page(self):
        response = self.client.get(reverse('search_product'))
        self.assertEqual(response.status_code, 200)

class FavoritePageTest(TestCase):
    def test_favorite_page(self):

