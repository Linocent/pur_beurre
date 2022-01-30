from django.db import models
from django.contrib.auth.models import User


class Categorie(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    product_id = models.BigIntegerField(primary_key=True)
    image = models.URLField(null=True, default=None, blank=True)
    name = models.CharField(max_length=200)
    nutriscore = models.CharField(max_length=1)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Favorite(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    user = models.ManyToManyField(User)

    def __str__(self):
        return f"{self.product, self.user}"
