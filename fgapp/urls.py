from django.urls import path
from .views import UserRecordView
from . import views

app_name = 'api'
urlpatterns = [
    path('', views.index, name='index'),
    path('user', UserRecordView.as_view(), name='users'),
]
