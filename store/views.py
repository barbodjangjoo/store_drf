
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render

@api_view()
def product_list(request):
    return Response('Hello')


@api_view()
def product_detail(request, id):
    return Response(id)



