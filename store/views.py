from django.shortcuts import render
from django.db.models import Count, Avg, Max, Min, Sum, F, Func, Value
from . import models

def show_data(request):
    queryset = models.Order.unpaid_orders.all()
    print(queryset)
    return render(request, 'store/hello.html',)
