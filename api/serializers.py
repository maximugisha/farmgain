from rest_framework import serializers

from django.contrib.auth.models import User

from fgapp.models import Price, Crop, Country, District, Region, Market
from report.models import Report

from rest_framework.validators import UniqueTogetherValidator


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        )
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['username', 'email']
            )
        ]


class CountrySerializer(serializers.ModelSerializer):
    regions = serializers.StringRelatedField(many=True)

    class Meta:
        model = Country
        fields = '__all__'


class RegionSerializer(serializers.ModelSerializer):
    districts = serializers.StringRelatedField(many=True)

    class Meta:
        model = Region
        fields = '__all__'


class DistrictSerializer(serializers.ModelSerializer):
    markets = serializers.StringRelatedField(many=True)

    class Meta:
        model = District
        fields = '__all__'


class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = '__all__'


class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = '__all__'


class PriceSerializer(serializers.ModelSerializer):
    crop_name = serializers.ReadOnlyField(source="crop.crop_name")
    market_name = serializers.ReadOnlyField(source="market.market_name")

    class Meta:
        model = Price
        fields = '__all__'


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
