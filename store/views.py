from django.shortcuts import render
from .models import Product

def show_data(request):

    queryset = Product.objects.filter(name__icontains='site', datetime_modified__year=2020,inventory__gt=5)
    return render(request, 'store/hello.html', {'products': list(queryset)})