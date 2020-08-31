from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('prices', views.price_list, name='price_list')
    ]