from django.urls import path

from . import views

urlpatterns = [
    path('products/', views.ProductList.as_view(), name='product_list'),
    path('products/<int:pk>/', views.product_detail),
    path('categories/', views.category_list),
    path('categories/<int:pk>/', views.category_detail, name='category-detail'),
]
