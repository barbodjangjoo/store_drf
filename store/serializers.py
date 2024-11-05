from decimal import Decimal
from rest_framework import serializers
from django.utils.text import slugify

from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    num_of_products = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ['id', 'title', 'description', 'num_of_products']

    def get_num_of_products(self, category):
        return category.products_count

    def validate(self, data):
        if len('title') < 3:
            raise serializers.ValidationError('the category should be at least three')
        return data

class ProductSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()
    title = serializers.CharField(max_length=255 , source = 'name')
    price = serializers.DecimalField(max_digits=6, decimal_places=2, source='unit_price')
    unit_price_after_tax = serializers.SerializerMethodField()
    # inventory = serializers.IntegerField()
    # category = serializers.HyperlinkedRelatedField(
    #     queryset = Category.objects.all(),
    #     view_name = 'category-detail',
    # )

    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'inventory', 'category', 'description','unit_price_after_tax']



    def get_unit_price_after_tax(self, product):
        return round(product.unit_price * Decimal(1.09), 2)
    
    def validate(self, data):
        if len('name') > 6 :
            raise serializers.ValidationError('Product title should be at least 6')
        return data
    
    def create(self, validated_data):
        product= Product(**validated_data)
        product.slug = slugify(product.name)
        product.save()
        return product

