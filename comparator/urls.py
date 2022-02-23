from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^product_detail/(?P<product_id>[0-9]+)/$', views.detail, name='product_detail'),
    url(r'^search/$', views.search),
    url(r'^addfavorite/', views.add_favorite, name="add_favorite"),
    url(r'^favorite/', views.favorite, name="favorite"),
]
