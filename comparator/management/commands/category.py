from django.core.management.base import BaseCommand
from requests.exceptions import HTTPError, ConnectionError
import requests as rq
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from comparator.models import Product, Categorie


class Command(BaseCommand):
    help = "Add category in database."

    def handle(self, *args, **options):

        CLEAR_CATEGORY = Categorie.objects.all()
        CATEGORY = ['Sodas', 'cheeses', 'desserts', 'fishes', 'pastas']
        CLEAR_CATEGORY.delete()

        for cat in CATEGORY:
            query = Categorie(
                name=cat
            )
            query.save()
