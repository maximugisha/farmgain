from django.contrib import admin
from .models import Country, Crop, District, Price, Region, Market


class PriceAdmin(admin.ModelAdmin):
    ordering = ['measure']

    list_display = (
        'market',
        'crop',
        'measure',
        'retail_price',
        'wholesale_price',
        'year',
        'month',
    )


class CountryAdmin(admin.ModelAdmin):
    ordering = ['country_name']

    list_display = (
        'country_name',
        'country_code',
        'created_at',
    )


class RegionAdmin(admin.ModelAdmin):
    ordering = ['region_name']

    list_display = (
        'country',
        'region_name',
        'created_at',
    )


class DistrictAdmin(admin.ModelAdmin):
    ordering = ['district_name']

    list_display = (
        'region',
        'district_name',
        'district_number',
    )


class MarketAdmin(admin.ModelAdmin):
    ordering = ['market_name']

    list_display = (
        'market_name',
        'district',
        'created_at',
    )


class CropAdmin(admin.ModelAdmin):
    ordering = ['crop_name']

    list_display = (
        'crop_name',
        'updated_at',
        'created_at',
    )


# Register your models here.
admin.site.register(Crop, CropAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Market, MarketAdmin)
