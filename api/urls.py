from django.urls import path, include
from rest_framework import routers

from .views import UserRecordView, index, CountryViewSet, RegionViewSet, DistrictViewSet, MarketViewSet, CropViewSet,\
    PriceViewSet, ReportViewSet

router = routers.DefaultRouter(trailing_slash=False)


# urls for fgapp
router.register(r'countries', CountryViewSet, basename='country')
router.register(r'regions', RegionViewSet, basename='region')
router.register(r'districts', DistrictViewSet, basename='district')
router.register(r'markets', MarketViewSet, basename='market')
router.register(r'crops', CropViewSet, basename='crop')
router.register(r'prices', PriceViewSet, basename='price')


# urls for report app
router.register(r'reports', ReportViewSet, basename='report')

urlpatterns = [
    path('', index, name='index'),
    path('user', UserRecordView.as_view(), name='users'),
    path('', include(router.urls)),
]

