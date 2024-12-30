from django.shortcuts import render
from . import models

def practice_one(request):

    queryset = models.OrderItem.objects.all().filter(id=1)
    if queryset.exists():
        print('hello')
        return render(request, 'store/hello.html', {'products': list(queryset)})
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