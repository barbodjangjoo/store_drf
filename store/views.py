from django.shortcuts import render
from django.db.models import Count, Avg, Max, Min, Sum
from . import models

def show_data(request):
    inventory_10 = models.Product.objects.filter(inventory__gt=10).aggregate(
        price=Avg('unit_price'),
        count= Count('id')
        )
    print(inventory_10)
    return render(request, 'store/hello.html',)
