"""
For use this command, execute this: python manage.py product
"""
from django.core.management.base import BaseCommand
from requests.exceptions import HTTPError, ConnectionError
import requests as rq
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from comparator.models import Product, Categorie


class Command(BaseCommand):
    help = "Get data product from OpenFoodFact API."

    def handle(self, *args, **options):

        NUTRISCORE = ["a", "b", "c", "d", "e"]
        CLEAR_PRODUCTS = Product.objects.all()
        CATEGORIES = Categorie.objects.all()
        CLEAR_PRODUCTS.delete()

        for cat in CATEGORIES:
            for nut in NUTRISCORE:
                try:
                    payload = {
                        "action": "process",
                        "json": "true",
                        "page": 1,
                        "tagtype_0": "categories",
                        "tag_contains_0": "contains",
                        "tag_0": cat,
                        "tagtype_1": "nutrition_grades",
                        "tag_contains_1": "contains",
                        "tag_1": nut,
                        "page_size": 100,
                        "countries": "France",
                    }
                    prod = rq.get(
                        'https://world.openfoodfacts.org/cgi/search.pl?',
                        params=payload)
                    response = prod.json()
                    response = response["products"]

                except HTTPError as err:
                    print(
                        "Openfoodfacts server might be busy or has crashed,"
                        "or check your connection : {}\n".format(err))
                except ConnectionError as con_err:
                    print(
                        "Openfoodfacts server is not reachable,"
                        "check your connexion {}".format(con_err))

                for item in response:
                    try:
                        url_validator = URLValidator()
                        url_validator(item["image_small_url"])
                        if isinstance(item.get("id"), str):
                            query = Product(
                                url=item.get('url'),
                                product_id=item.get("id"),
                                image=item.get("image_small_url"),
                                categorie=cat,
                                name=item.get("product_name"),
                                nutriscore=item.get("nutrition_grades")
                            )
                            query.save()
                    except KeyError:
                        pass
                    except ValueError:
                        pass
                    except ValidationError:
                        pass
                    print(f"Extraction of"
                          f" {item.get('product_name')} "
                          f"in {cat}")
        print('Extraction is over.')
