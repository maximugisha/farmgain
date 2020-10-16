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


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ('market',
                  'crop',
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
