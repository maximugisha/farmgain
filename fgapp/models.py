from django.db import models
from django.utils import timezone
import datetime


# Create your models here.

class Country(models.Model):
    country_name = models.CharField(max_length=200, default='Uganda')
    country_code = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    edited_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.country_name

    def publish(self):
        self.save()


class Region(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    region_name = models.CharField(max_length=200, default='Central')
    created_at = models.DateTimeField(default=timezone.now)
    edited_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.region_name

    def publish(self):
        self.save()


class District(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    district_name = models.CharField(max_length=200, default='Kampala')
    district_number = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    edited_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.district_name

    def publish(self):
        self.save()


class Market(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    market_name = models.CharField(max_length=200, default='Kasubi')
    created_at = models.DateTimeField(default=timezone.now)
    edited_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.market_name

    def publish(self):
        self.save()


class Crop(models.Model):
    crop_name = models.CharField(max_length=200, default='Beans')
    created_at = models.DateTimeField(default=timezone.now)
    edited_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.crop_name

    def publish(self):
        self.save()


yeardropdown = []
for yr in range(2000, (datetime.datetime.now().year + 5)):
    yeardropdown.append((yr, yr))

monthdropdown = [
    ('January', 'January'),
    ('February', 'February'),
    ('March', 'March'),
    ('April', 'April'),
    ('June', 'June'),
    ('July', 'July'),
    ('August', 'August'),
    ('September', 'September'),
    ('October', 'October'),
    ('November', 'November'),
    ('December', 'December')
]

week_count = []
for week in range(1, 53):
    week_count.append((week, week))

day_enum = [
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
]


class Price(models.Model):
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    measure = models.CharField(max_length=200, default='Kilo')
    retail_price = models.IntegerField(default=0)
    wholesale_price = models.IntegerField(default=0)
    year = models.IntegerField(choices=yeardropdown, default=datetime.datetime.now().year)
    month = models.CharField(max_length=11, choices=monthdropdown, default='January')
    week_number = models.IntegerField(choices=week_count, default=1)
    day = models.CharField(choices=day_enum, max_length=11, default='Monday')
    created_at = models.DateTimeField(default=timezone.now)
    edited_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __int__(self):
        return self.crop_id, self.market_id, self.measure, self.retail_price, self.wholesale_price

    def __str__(self):
        template = '{0.crop_id}, {0.market_id}, {0.measure}, {0.retail_price}, {0.wholesale_price}'
        return template.format(self)

    def publish(self):
        self.save()
