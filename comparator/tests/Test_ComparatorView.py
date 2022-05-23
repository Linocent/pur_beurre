from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
#from comparator.models import (
#    Categorie,
#    Product,
#    Favorite,
#)

"""
class IndexPageTest(TestCase):
    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_search(self):
        response = self.client.post(reverse('search', {'query': 'coca'}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'search_product')


class TestProductDetail(TestCase):
    def test_product_detail_view(self):
        response = self.client.get(reverse('product_detail'))
        self.assertEqual(response.status_code, 200)


class SearchPageTest(TestCase):
    def test_search_page(self):
        response = self.client.get(reverse('search_product'))
        self.assertEqual(response.status_code, 200)


class TestSearchFavoriteSaved(TestCase):
    def setUp(self):
        user = User.objects.create(
            id=1,
            email="email@email.com",
            first_name="first_name",
            second_name="second_name",
            password="123456789",
        )
        user.save()
        self.client.login(username='email@email.com', password='123456789')

        product = Product.objects.create(
            product_id="123456789",
            image="http://product_url.com",
            name="name1",
            nutriscore="a",
            categorie_id=1,
        )
        product.save()

        substitute = Product.objects.create(
            product_id="987654321",
            image="http://product_url2.com",
            name="name2",
            nutriscore="b",
            categorie_id=1,
        )
        substitute.save()

    def test_add_favorite_view_connected_user(self):
        response = self.client.get(reverse('add_favorite'))
        self.assertEqual(response.status_code, 200)

    def test_add_favorite(self):
        form_data = {"sub": substitute, "prod": product, "user": user}

    def test_add_favorite_view_not_connected_user(self):
        self.client.logout()
        response = self.client.get(reverse('add_favorite'))
        self.assertEqual(response.status_code, 302)


class FavoritePageTest(TestCase):
    def setUp(self):
        user = User.objects.create(
            id=1,
            email="email@email.com",
            first_name="first_name",
            second_name="second_name",
            password="123456789",
        )
        user.save()
        self.client.login(username='email@email.com', password='123456789')

    def test_favorite_page_connected_user(self):
        response = self.client.get(reverse('favorite'))
        self.assertEqual(response.status_code, 200)

    def test_favorite_page_not_connected_user(self):
        self.client.logout()
        response = self.client.get(reverse("favorite"))
        self.assertEqual(response.status_code, 302)


class TestMyAccount(TestCase):
    def test_my_account_view_connected_user(self):
        response = self.client.get(reverse('my_account'))
        self.assertEqual(response.status_code, 200)

    def test_my_account_view_not_connected_user(self):
        response = self.client.get(reverse('my_account'))
        self.assertEqual(response.status_code, 302)


class TestLegalMention(TestCase):
    def test_mention_legal_view(self):
        response = self.client.get(reverse('legal_mention'))
        self.assertEqual(response.status_code, 200)"""

