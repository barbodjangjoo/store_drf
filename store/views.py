from django.db.models import Count
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


from  .models import Category, Product
from .serializers import ProductSerializer, CategorySerializer

class ProductList(ListCreateAPIView):
    serializer_class = ProductSerializer
    get_queryset = Product.objects.select_related('category').all()

    # def get_serializer_class(self):
    #     return ProductSerializer
    
    # def get_queryset(self):
    #     return Product.objects.select_related('category').all()
    
    def get_serializer_context(self):
        return {'request': self.request}

# class ProductList(APIView):
#     def get(self, request):
#         queryset = Product.objects.select_related('category').all()
#         serializer = ProductSerializer(
#             queryset, 
#             many = True, 
#             context = {'request': request})
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class ProductDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.select_related('category').all()

    def delete(self, request, pk):
        product = get_object_or_404(
        Product.objects.select_related('category'),
        pk=pk
        )
        if product.order_items.count() > 0:
            return Response({'error': 'Product is in use'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryList(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.prefetch_related('products').all()
    
    

# @api_view(['GET', 'POST'])
# def category_list(request):
#     if request.method == 'GET':
#         queryset = Category.objects.prefetch_related('products').all()
#         serializer = CategorySerializer(queryset, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = CategorySerializer(data= request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class CategoryDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.prefetch_related('products')

    def delete(self, request, pk):
        category = get_object_or_404(Category,pk=pk)
        if category.products.count() > 0:
            return Response({'error' : 'Category can not be deleted'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # def get(self, request, pk):
    #     category = get_object_or_404(Category,pk=pk)
    #     serializer = CategorySerializer(category)
    #     return Response(serializer.data)
    
    # def put(self, request, pk):
    #     category = get_object_or_404(Category,pk=pk)
    #     serializer = CategorySerializer(category ,data= request.data)
    #     serializer.is_valid()
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    

 




