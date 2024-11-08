from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


from  .models import Category, Product
from .serializers import ProductSerializer, CategorySerializer

@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        queryset = Product.objects.select_related('category').all()
        serializer = ProductSerializer(queryset, many = True, context = {'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('COol')


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):    
    product = get_object_or_404(
        Product.objects.select_related('category'),
        pk=pk
        )
    if request.method == 'GET':
        serializer = ProductSerializer(product, context = {'request': request})
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        if product.order_items.count() > 0:
            return Response({'error': 'Product is in use'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view()
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    serializer = CategorySerializer(category)
    return Response(serializer.data)



