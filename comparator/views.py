from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Categorie, Product, Favorite
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def index(request):

    query = request.GET.get('query')
    template = loader.get_template('comparator/index.html')
    if query:
        return search(request, query)
    else:
        return HttpResponse(template.render(request=request))


def detail(request, product_id):

    product_choose = get_object_or_404(Product, product_id=product_id)
    nut = product_choose.nutriscore
    query_set_product = (
        Product.objects.filter(categorie_id=product_choose.categorie_id)
            .filter(Q(nutriscore__lte=nut)).exclude(product_id=product_choose.product_id))
    return render(request, "comparator/detail.html", {"substitue": query_set_product, "product": product_choose})


def search(request, query):

    if not query:
        message = "Misère de misère, nous n'avons rien trouvé comme résultat!"
        return HttpResponse(message)
    else:
        answer_prod = Product.objects.filter(name__icontains=query)
        if answer_prod.exists():
            return render(request, "comparator/search_form.html", {"answer_prod": answer_prod})
        if not answer_prod.exists():
            message = "Misère de misère, nous n'avons rien trouvé comme résultat!"
            return HttpResponse(message)


def add_favorite(request):

    if request.method == "POST":
        print("Get data")
    fav = request.POST.get("add_fav")
    print(f"This is fav: {fav}")
    if fav:
        print("product save")
    else:
        print(f"Nothing")


@login_required
def favorite(request):
    pass




