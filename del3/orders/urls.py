from django.conf.urls import url

from . import views as orders_views

urlpatterns = [
    url(r'^$', orders_views.index, name='index'),
    # url(r'^delete/(?P<order_id>[0-9]+)/$', catalog_views.delete_product, name='delete_product'),
]