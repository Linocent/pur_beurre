from django.db import models
from django.contrib.auth.models import User


class Categorie(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    product_id = models.BigIntegerField(primary_key=True)
    url = models.URLField(
        null=False,
        default=None,
        blank=False,
    )
    image = models.URLField(
        null=True,
        default=None,
        blank=True,
    )
    name = models.CharField(max_length=200)
    nutriscore = models.CharField(max_length=1)
    categorie = models.ForeignKey(
        Categorie,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.name}"


class Favorite(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
    )
    chosen_product = models.ForeignKey(
        Product,
        related_name="chosen_product",
        on_delete=models.CASCADE,
        null=True,
    )
    substitute = models.ForeignKey(
        Product,
        related_name="substitute",
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return f"{self.user, self.chosen_product, self.substitute}"
