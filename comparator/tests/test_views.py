from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from comparator.models import (
    Categorie,
    Product,
    Favorite,
)


class IndexPageTest(TestCase):
    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_search(self):
        response = self.client.post(
            reverse('index'),
            {'query': 'coca'},
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'search')


class TestProductDetail(TestCase):
    def setUp(self):
        self.categorie = Categorie.objects.create(
            name='name1',
            id=1,
        )
        self.categorie.save()

        self.product = Product.objects.create(
            product_id='123456789',
            image='http://product_url.com',
            name='name1',
            nutriscore='c',
            categorie_id=1,
            url='http://openfoodfact.com/name1',
        )
        self.product.save()

        self.sub = Product.objects.create(
            product_id='987654321',
            image='http://product_url2.com',
            name='name2',
            nutriscore='a',
            categorie_id=1,
            url='http://openfoodfact.com/name2',
        )
        self.sub.save()

    def test_product_detail_view(self):
        response = self.client.get(reverse('product_detail', kwargs={'product_id': '123456789'}))
        self.assertEqual(response.status_code, 200)


class FavoritePageTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            id=1,
            username='test',
            email='email@email.com',
            first_name='first_name',
            password='123456789'
        )
        self.user.save()
        self.client.login(username='test', password='123456789')

        self.categorie = Categorie.objects.create(
            name='name1',
            id=1,
        )
        self.categorie.save()

        self.product = Product.objects.create(
            product_id='123456789',
            image='http://product_url.com',
            name='name1',
            nutriscore='c',
            categorie_id=1,
            url='http://openfoodfact.com/name1',
        )
        self.product.save()

        self.sub = Product.objects.create(
            product_id='987654321',
            image='http://product_url2.com',
            name='name2',
            nutriscore='a',
            categorie_id=1,
            url='http://openfoodfact.com/name2',
        )
        self.sub.save()

        self.fav = Favorite.objects.create(
            user=self.user,
            chosen_product=self.product,
            substitute=self.sub,
        )
        self.fav.save()

    def test_check_fav(self):
        response_conn = self.client.get(reverse('favorite'))
        self.assertEqual(response_conn.status_code, 200)
        saved_fav = self.client.get(reverse('favorite'))
        prod = Favorite.objects.filter(user_id=1)
        prod_list = list()
        for item in prod:
            sub = item.substitute
            prod_list.append(sub)
        self.assertEqual(
            saved_fav.context['sub'],
            prod_list
        )
        self.client.logout()
        anonymous_response = self.client.get(reverse('favorite'))
        self.assertEqual(anonymous_response.status_code, 302)

    def test_add_favorite(self):
        self.client.login(username='test', password='123456789')
        response = self.client.post(
            '/comparator/addfavorite/',
            {
                'prod': self.product.product_id,
                'sub': self.sub.product_id,
            }
        )
        self.assertEqual(response.status_code, 302)


class TestMyAccount(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            id=1,
            username='test',
            email='email@email.com',
            first_name='first_name',
            password='123456789'
        )
        user.save()
        self.client.login(username='test', password='123456789')

    def test_go_to_my_account(self):
        response_conn = self.client.get(reverse('my_account'))
        self.assertEqual(response_conn.status_code, 200)
        user = User.objects.get(id=1)
        self.assertEqual(response_conn.context['mail'], user.email)
        self.client.logout()
        anonymous_response = self.client.get(reverse('my_account'))
        self.assertEqual(anonymous_response.status_code, 302)


class TestLegalMention(TestCase):
    def test_mention_legal_view(self):
        response = self.client.get(reverse('legal_mention'))
        self.assertEqual(response.status_code, 200)

