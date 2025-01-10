from django.shortcuts import render
from django.db.models import Count, Avg, Max, Min, Sum, F, Func, Value
from . import models

def show_data(request):
    queryset = models.Customer.objects.annotate(fullname=Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT'))
    print(queryset)
    return render(request, 'store/hello.html',)
