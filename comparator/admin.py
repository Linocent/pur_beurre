from django.contrib import admin

from .models import Categorie, Product, Favorite


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

