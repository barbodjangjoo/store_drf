from django.shortcuts import render
from django.db.models import Count, Avg, Max, Min, Sum, F
from . import models

def show_data(request):
    queryset = models.OrderItem.objects.annotate(total_price=F("quantity")* F("unit_price")).all()
    print(queryset)
    return render(request, 'store/hello.html',)
