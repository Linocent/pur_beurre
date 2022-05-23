from django.test import TestCase
from django.urls import reverse
from comparator.models import (
    Categorie,
    Product,
    Favorite,
)


class DbRequestTest(TestCase):
    def setUp(self):
        categorie = Categorie.objects.create(
            name='poulet',
        )
