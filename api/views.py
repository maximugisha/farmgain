from django.shortcuts import render, HttpResponse
from .serializers import UserSerializer, CountrySerializer, RegionSerializer, DistrictSerializer, MarketSerializer,\
    CropSerializer, PriceSerializer, ReportSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# view sets for json
from rest_framework import status, viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from django.contrib.auth.models import User
from fgapp.models import Country, Region, Crop, Price, District, Market
from report.models import Report
# from rest_framework.decorators import authentication_classes, permission_classes

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# Create your views here.
def index(request):
    return HttpResponse('Welcome to farmgain')


class UserRecordView(APIView):
    """
    API View to create or get a list of all the registered users.
    GET request returns the registered users whereas a
    POST request allows to create a new user.
    """
    permission_classes = [AllowAny]

    def get(self, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )


# api views for fgapp
class CountryViewSet(viewsets.ModelViewSet):
    """
   A viewset for viewing and editing countries instances.
   """
    serializer_class = CountrySerializer
    queryset = Country.objects.all()


class RegionViewSet(viewsets.ModelViewSet):
    """
   A viewset for viewing and editing region instances.
   """
    serializer_class = RegionSerializer
    queryset = Region.objects.all()


class DistrictViewSet(viewsets.ModelViewSet):
    """
   A viewset for viewing and editing districts instances.
   """
    serializer_class = DistrictSerializer
    queryset = District.objects.all()


class MarketViewSet(viewsets.ModelViewSet):
    """
   A viewset for viewing and editing Market instances.
   """
    serializer_class = MarketSerializer
    queryset = Market.objects.all()


class CropViewSet(viewsets.ModelViewSet):
    """
   A viewset for viewing and editing Crop instances.
   """
    serializer_class = CropSerializer
    queryset = Crop.objects.all()


class PriceViewSet(viewsets.ModelViewSet):
    """
   A viewset for viewing and editing Prices instances.
   """
    serializer_class = PriceSerializer
    queryset = Price.objects.all().order_by('crop')


# api views for report app
class ReportViewSet(viewsets.ModelViewSet):
    """
   A viewset for viewing and editing Reports instances.
   """
    serializer_class = ReportSerializer
    queryset = Report.objects.all()

# # These decorators are used to disable/enable authentication, just import permission classes or authentication classes
# @permission_classes([])
# @authentication_classes([])
