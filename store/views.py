from django.shortcuts import render
from . import models

def show_data(request):
    queryset = models.Comment.objects.select_related('product').all()
    return render(request, 'store/hello.html',context={'comments':queryset})
    