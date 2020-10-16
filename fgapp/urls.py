from django.urls import path, include
from rest_framework import routers
from .views import UserRecordView, PriceViewSet, index, ChartData

router = routers.DefaultRouter()
router.register(r'prices', PriceViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
app_name = 'api'
urlpatterns = [
    path('', index, name='index'),
    path('user', UserRecordView.as_view(), name='users'),
    path('', include(router.urls)),
    path('api', ChartData.as_view()),
]

