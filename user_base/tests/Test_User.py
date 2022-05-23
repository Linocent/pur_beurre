from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class CreationUserTest(TestCase):

    def setUp(self):
        user = User.objects.create(
            email="email@email.com",
            first_name="first_name",
            second_name="second_name",
            password="12345678",
        )
        user.save()

    def test_user(self):
        user = User.objects.get(email="email@email.com")
        self.assertEqual(user.email, "email@email.com")
        self.assertEqual(user.first_name, "first_name")
        self.assertEqual(user.second_name, "second_name")
        self.assertEqual(user.password, "12345678")


class LoginTest(TestCase):

    def setUp(self):
        user = User.objects.create(
            email="email@email.com",
            first_name="first_name",
            second_name="second_name",
            password="12345678"
        )
        user.save()

    def test_login_view(self):
        response = self.client.get(reverse('log_in/'))
        self.assertEqual(response.status_code, 200)

    def test_user(self):
        c = Client()
        response = c.post('log_in/', {'email': 'email@email.com', 'password': '12345678'})
        self.assertEqual(response, response.status_code == '200')

    def test_logout_view(self):
        response = self.client.get(reverse('logged_out/'))
        self.assertEqual(response.status_code, 200)
