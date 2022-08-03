from django.conf.urls import url
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(
        r'^product_detail/(?P<product_id>[0-9]+)/$',
        views.detail,
        name='product_detail'
    ),
    url(
        r'^fav_detail/(?P<product_id>[0-9]+)/$',
        views.fav_detail,
        name='fav_detail',
    ),
    url(r'^search/$', views.search, name='search'),
    url(
        r'^addfavorite/',
        views.add_favorite,
        name='add_favorite'
    ),
    url(r'^favorite/', views.favorite, name='favorite'),
    url(r'^404/', views.page_not_found, name='404'),
    url(r'^my_account/', views.my_account, name='my_account'),
    url(r'^legal_mention/', views.mention_legal, name='legal_mention')
]
