from django.shortcuts import render
from . import models

def practice_one(request):
    queryset = models.OrderItem.objects.filter(product__id=1)
    return render(request, 'store/hello.html', {'products': list(queryset)})

def practice_two(request):
    queryset = models.Product.objects.all().filter(inventory=5)
    return render(request, 'store/hello.html', {'products': list(queryset)})

def practice_three(request):
    queryset = models.Product.objects.filter(name__icontains='site', inventory__gt=3)
    return render(request, 'store/hello.html', {'products': list(queryset)})

def practice_four(request):
    queryset = models.Product.objects.filter(name__icontains='site', inventory__gt=3, inventory__lt=10)
    return render(request, 'store/hello.html', {'products': list(queryset)})

def practice_five(request):
    queryset = models.Order.objects.all().filter(status=models.Order.ORDER_STATUS_UNPAID)
    return render(request, 'store/hello.html', {'products': list(queryset)})

def practice_six(request):
    queryset = models.OrderItem.objects.filter(id=1)
    return render(request, 'store/hello.html', {'products': list(queryset)})

def practice_seven(request):
    queryset = models.OrderItem.objects.filter(order__id=1)
    return render(request, 'store/hello.html', {'products': list(queryset)})

def practice_eight(request):
    queryset = models.Product.objects.filter(unit_price__lt=10)
    return render(request, 'store/hello.html', {'products': list(queryset)})

def practice_nine(request):
    queryset = models.OrderItem.objects.filter(order__customer__first_name__icontains='john')
    return render(request, 'store/hello.html', {'products': list(queryset)})
