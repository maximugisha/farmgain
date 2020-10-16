from django.shortcuts import render, HttpResponse
from django.template import context
from django.utils import timezone
from .serializers import UserSerializer, PriceSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# view sets for json
from rest_framework import status, viewsets
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User
from .models import Country, Crop, Price, District

from rest_framework.decorators import authentication_classes, permission_classes


# Create your views here.
def index(request):
    return HttpResponse('Welcome to Farmgain')


class UserRecordView(APIView):
    """
    API View to create or get a list of all the registered
    users. GET request returns the registered users whereas
    a POST request allows to create a new user.
    """
    permission_classes = [IsAdminUser]

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


#These decorators are used to disable/enable authentcation, just import permission classes or authentication classes
@permission_classes([])
@authentication_classes([])
class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all().order_by('crop')
    serializer_class = PriceSerializer
