from django.contrib.auth.models import User
from .models import Price, Crop, Country, District, Region, Market
from rest_framework import serializers
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


class CountriesSerializer(serializers.ModelSerializer):
    regions = serializers.StringRelatedField(many=True)

    class Meta:
        model = Country
        fields = ("country_name", "regions")


class PriceSerializer(serializers.ModelSerializer):
    crop_name = serializers.ReadOnlyField(source="crop.crop_name")
    market_name = serializers.ReadOnlyField(source="market.market_name")

    class Meta:
        model = Price
        fields = ('id',
                  'market_name',
                  'crop_name',
                  'measure',
                  'retail_price',
                  'wholesale_price',
                  'year',
                  'month',
                  'week_number',
                  'day',
                  'created_at',
                  'edited_at',
                  'updated_at'
                  )

class RegionsSerializer(serializers.ModelSerializer):
    districts = serializers.StringRelatedField(many=True)

    class Meta:
        model = Region
        fields = ("country_id", "region_name", "districts")


class DistrictsSerializer(serializers.ModelSerializer):
    markets = serializers.StringRelatedField(many=True)

    class Meta:
        model = District
        fields = ("region_id", "district_name", "markets")


class MarketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = ("district_id", "market_name")


class CropsSerializer(serializers.ModelSerializer):
    # prices = PricesSerializer(many=True)

    class Meta:
        model = Crop
        fields = ("crop_name", "prices")