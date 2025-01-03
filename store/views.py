from django.shortcuts import render
from . import models

def show_data(request):
    queryset = models.Comment.objects.select_related('product').all()
    return render(request, 'store/hello.html',context={'comments':queryset})

def practice_two(request):
    queryset = models.Product.objects.prefetch_related('comments').all()
    return render(request, 'store/practice_two.html', context={'products': queryset})
    