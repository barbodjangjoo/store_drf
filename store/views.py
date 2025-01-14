from django.shortcuts import render
from django.db.models import Count, Avg, Max, Min, Sum, F, Func, Value, ExpressionWrapper
from . import models

def category(request):
    return render(request, 'store/hello.html',)