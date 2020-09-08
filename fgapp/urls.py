from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products', views.products, name='products'),
    path('pricing', views.pricing, name='pricing'),
    path('technology', views.technology, name='technology'),
    path('prices', views.price_list, name='price_list')
    ]