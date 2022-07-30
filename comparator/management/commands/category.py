"""
For use this command, execute this: python manage.py: python manage.py category
"""
from django.core.management.base import BaseCommand
from comparator.models import Categorie


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
