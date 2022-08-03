from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from .models import (
    Product,
    Favorite,
    Categorie,
)
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def index(request):
    query = request.GET.get('query')
    if query:
        return search(request, query)
    return render(request, "comparator/index.html")


def detail(request, product_id):
    """Display details of a product."""
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
    return render(
        request,
        "comparator/detail.html",
        {"substitue": query_set_product, "product": product_choose}
    )


def search(request, query):
    """Looking for product in DB"""
    if not query:
        message = "Misère de misère, nous n'avons " \
                  "rien trouvé comme résultat!"
        return page_not_found(request, message)
    else:
        answer_prod = Product.objects.filter(name__icontains=query)
        if answer_prod.exists():
            return render(
                request,
                "comparator/search_form.html",
                {"answer_prod": answer_prod, 'query': query}
            )
        if not answer_prod.exists():
            message = "Misère de misère, nous n'avons " \
                      "rien trouvé comme résultat!"
            return page_not_found(request, message)


@login_required
def add_favorite(request):
    """Add products and their substitute in table Favorite."""
    if request.method == "POST":
        sub = request.POST.get("sub")
        substitute = Product.objects.get(product_id=sub)
        prod = request.POST.get("prod")
        product = Product.objects.get(product_id=prod)
        username = request.user
        user = User.objects.get(username=username)
        favoris = Favorite(
            user=user,
            chosen_product=product,
            substitute=substitute,
        )
        favoris.save()
    return redirect('/')


def page_not_found(request, message):
    """Display error if request doesn't match."""
    cat = Categorie.objects.all()
    return render(
        request,
        "comparator/404.html",
        {"message": message, 'cat': cat}
    )


@login_required
def favorite(request):
    """Get data from favorite table and return it."""
    user = request.user
    username = User.objects.get(username=user)
    prod = Favorite.objects.filter(user=username)
    prod_list = list()
    if prod.exists():
        for item in prod:
            sub = item.substitute
            prod_list.append(sub)
        return render(
            request,
            'comparator/favorite.html',
            context={'sub': prod_list}
        )
    else:
        message = 'Pas de produit enregistré.'
        return render(
            request,
            'comparator/favorite.html',
            {'msg': message}
        )


@login_required
def fav_detail(request, product_id):
    """Display detail of a product save as favorite."""
    product_choose = get_object_or_404(
        Product,
        product_id=product_id
    )
    return render(
        request,
        'comparator/fav_detail.html',
        {'product': product_choose}
    )


@login_required
def my_account(request):
    """display user account page."""
    user = request.user
    username = User.objects.get(username=user)
    mail = username.email
    return render(
        request,
        'comparator/account.html',
        {'username': username, 'mail': mail}
    )


def mention_legal(request):
    """Mention legal of web site"""
    return render(request, 'comparator/mention_legal.html')
