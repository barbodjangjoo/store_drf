from django.shortcuts import render
from . import models

def show_data(request):
    queryset = models.Comment.select_related('product').objects.all() 
    return render(request, 'store/hello.html',context={'comments':queryset})

def practice_two(request):
    queryset = models.Product.objects.prefetch_related('comments').all()
    return render(request, 'store/practice_two.html', context={'products': queryset})
    
def practice_three(request):
    queryset = models.Order.objects.prefetch_related('items__product ').select_related('customer').all()
    return render(request, 'store/practice_three.html', {'orders': queryset})