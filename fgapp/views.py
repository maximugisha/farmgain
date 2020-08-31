from django.shortcuts import render
from django.template import context
from django.utils import timezone
from .models import Country, Crop, Price, District

# Create your views here.
def index(request):
    return render(request, 'fgapp/index.html', {})

def price_list(request):
    prices = Price.objects.all
    return render(request, 'fgapp/crops.html', {'prices': prices})
