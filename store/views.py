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