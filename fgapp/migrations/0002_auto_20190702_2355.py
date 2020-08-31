# Generated by Django 2.2.3 on 2019-07-02 20:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fgapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='country_code',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='country_name',
            field=models.CharField(default='Uganda', max_length=200),
        ),
        migrations.AddField(
            model_name='country',
            name='edited_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='country',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='crop',
            name='crop_name',
            field=models.CharField(default='Beans', max_length=200),
        ),
        migrations.AddField(
            model_name='crop',
            name='edited_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='crop',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='district',
            name='district_name',
            field=models.CharField(default='Kampala', max_length=200),
        ),
        migrations.AddField(
            model_name='district',
            name='district_number',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='district',
            name='edited_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='district',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='market',
            name='edited_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='market',
            name='market_name',
            field=models.CharField(default='Kasubi', max_length=200),
        ),
        migrations.AddField(
            model_name='market',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='price',
            name='day',
            field=models.CharField(default='Monday', max_length=200),
        ),
        migrations.AddField(
            model_name='price',
            name='edited_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='price',
            name='measure',
            field=models.CharField(default='Kilo', max_length=200),
        ),
        migrations.AddField(
            model_name='price',
            name='month',
            field=models.CharField(default='January', max_length=200),
        ),
        migrations.AddField(
            model_name='price',
            name='retail_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='price',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='price',
            name='week_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='price',
            name='wholesale_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='price',
            name='year',
            field=models.CharField(default=2019, max_length=200),
        ),
        migrations.AddField(
            model_name='region',
            name='edited_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='region',
            name='region_name',
            field=models.CharField(default='Central', max_length=200),
        ),
        migrations.AddField(
            model_name='region',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
