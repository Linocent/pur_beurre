from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from django.http import HttpResponse
from .models import (
    Categorie,
    Product,
    Favorite,
)
from django.template import loader
from django.contrib.auth import (
    authenticate,
    login,
    logout,
)
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def index(request):
    query = request.GET.get('query')
    template = loader.get_template('comparator/index.html')
    if query:
        return search(request, query)
    return HttpResponse(template.render(request=request))


def detail(request, product_id):
    product_choose = get_object_or_404(
        Product,
        product_id=product_id
    )
    nut = product_choose.nutriscore
    query_set_product = (
        Product.objects.filter(
            categorie_id=product_choose.categorie_id
        ).filter(Q(nutriscore__lte=nut)).exclude(
            product_id=product_choose.product_id
        ))
    return render(request, "comparator/detail.html",
                  {"substitue": query_set_product, "product": product_choose})


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
        sub = request.POST.get("sub")
        substitute = Product.objects.get(product_id=sub)
        prod = request.POST.get("prod")
        product = Product.objects.get(product_id=prod)
        username = request.user
        user = User.objects.get(username=username)
        print(user, product, sub)
        favoris = Favorite(
            user=user,
            chosen_product=product,
            substitute=substitute,
        )
        favoris.save()
    return redirect('/')


@login_required
def favorite(request):
    user = request.user
    username = User.objects.get(username=user)
    prod = Favorite.objects.filter(user=username)
    if prod.exists():
        return render(request, 'comparator/favorite', {'prod': prod})
